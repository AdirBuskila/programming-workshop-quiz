"""Shared checker for step-author code steps. Reads the SHIPPED tools/raw/<CODE>.json and, per step, compiles with clang
and compares (return code, stdout) of a driver program against the reference solution:
  order    : every pair of blocks swapped must change behaviour (build error, crash, hang or different output)
  fillblank: the correct option reproduces the reference, every distractor must differ
  findbug  : the broken version must differ from the reference
build(lines) -> full C source. Usage: see steps_check.py in each tools/verify/<CODE>/ folder."""
import itertools, json, os, pathlib, subprocess, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor

CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang"
ROOT = pathlib.Path(__file__).resolve().parents[2]
_cnt = [0]


def run(src, stdin="", timeout=10):
    d = pathlib.Path(tempfile.mkdtemp(prefix="stp"))
    try:
        c, exe = d / "t.c", d / "t.exe"
        c.write_text(src, encoding="utf-8")
        p = subprocess.run([CLANG, "-w", "-O0", "-o", str(exe), str(c)], capture_output=True, text=True, errors="replace", cwd=d)
        if p.returncode:
            return ("BUILD-FAIL", p.stderr[:150])
        try:
            r = subprocess.run([str(exe)], capture_output=True, text=True, errors="replace", timeout=timeout, cwd=d, input=stdin)
        except subprocess.TimeoutExpired:
            return ("TIMEOUT", "")
        return (r.returncode, r.stdout)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def find(code, num, part, typ, hint):
    d = json.load(open(ROOT / "tools" / "raw" / f"{code}.json", encoding="utf-8"))
    for q in d["questions"]:
        if q["num"] == num and q.get("part") == part:
            hits = [s for s in q.get("steps", []) if s["type"] == typ and hint in s["prompt"]]
            assert len(hits) == 1, (code, num, part, typ, hint, len(hits))
            return hits[0]
    raise KeyError((num, part))


def _pmap(f, xs):
    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(f, xs))


class Item:
    def __init__(self, code, num, part, build, ref_lines):
        self.code, self.num, self.part, self.build = code, num, part, build
        self.ref = run(build(ref_lines))
        self.label = f"{code} Q{num}{part or ''}"
        assert self.ref[0] == 0, (self.label, "reference does not run cleanly", self.ref)
        self.ok = True

    def _flag(self, cond, msg):
        if not cond:
            self.ok = False
            print("   FAIL", msg)

    def order(self, hint, build=None):
        build = build or self.build
        s = find(self.code, self.num, self.part, "order", hint)
        lines = s["lines"]
        pairs = list(itertools.combinations(range(len(lines)), 2))

        def one(ij):
            i, j = ij
            b = list(lines)
            b[i], b[j] = b[j], b[i]
            return run(build(b))
        res = _pmap(one, pairs)
        assert run(build(lines)) == self.ref, "order identity differs from reference"
        bad = [(p, r) for p, r in zip(pairs, res) if r == self.ref]
        kinds = [("BUILD" if r[0] == "BUILD-FAIL" else "HANG" if r[0] == "TIMEOUT" else "DIFF") for r in res]
        print(f"{self.label} order[{hint}]: {len(lines)} blocks, {len(pairs)} swaps, kinds={sorted(set(kinds))}, unforced={bad or 'none'}")
        self._flag(not bad, f"{self.label} order unforced {bad}")

    def fill(self, hint, build=None):
        build = build or self.build
        s = find(self.code, self.num, self.part, "fillblank", hint)
        outs = []
        for o in s["options"]:
            lines = list(s["lines"])
            assert "___" in lines[s["blankIndex"]]
            lines[s["blankIndex"]] = lines[s["blankIndex"]].replace("___", o["value"])
            outs.append((o["id"], run(build(lines))))
        for oid, r in outs:
            good = oid == s["correctId"]
            print(f"{self.label} fill[{hint}] {oid}{'*' if good else ' '}: {'==ref' if r == self.ref else 'DIFFERS ' + str(r[0]) + ' ' + repr(r[1])[:40]}")
            self._flag((r == self.ref) == good, f"{self.label} fill option {oid}")

    def bug(self, hint, build=None):
        build = build or self.build
        s = find(self.code, self.num, self.part, "findbug", hint)
        r = run(build(s["lines"]))
        print(f"{self.label} bug[{hint}] line {s['bugIndex']}: {'SAME (bad)' if r == self.ref else 'differs ' + str(r[0]) + ' ' + repr(r[1])[:70]}")
        self._flag(r != self.ref, f"{self.label} bug does not fail")
        return r

    def finish(self):
        return self.ok


def sol_blocks(code, num, part):
    """Fenced ```c blocks of a stored solution (raw text)."""
    import re
    d = json.load(open(ROOT / "tools" / "raw" / f"{code}.json", encoding="utf-8"))
    for q in d["questions"]:
        if q["num"] == num and q.get("part") == part:
            return re.findall(r"```c?\n(.*?)\n```", q["solution"], re.S)
    raise KeyError((num, part))


def split_at(block, header):
    """(text before header, function text from header on)."""
    i = block.index(header)
    return block[:i], block[i:]
