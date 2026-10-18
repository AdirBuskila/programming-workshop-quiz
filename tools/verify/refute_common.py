"""Refuter helpers (independent of the authors' step_lib). Compiles C with clang, runs, compares."""
import json, pathlib, re, subprocess, itertools, os, shutil, tempfile, hashlib
CL = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang.exe"
ROOT = pathlib.Path(__file__).resolve().parents[2]
WORK = pathlib.Path(tempfile.gettempdir()) / "refute_work"
WORK.mkdir(exist_ok=True)

def load(code):
    return json.loads((ROOT / "tools/raw" / f"{code}.json").read_text(encoding="utf-8"))

def Q(code, num, part=None):
    for q in load(code)["questions"]:
        if q["num"] == num and q.get("part") == part:
            return q
    raise KeyError((code, num, part))

def blocks(sol):
    return re.findall(r"```c\n(.*?)```", sol, re.S)

def build(src, extra=()):
    h = hashlib.md5(src.encode()).hexdigest()[:12]
    c = WORK / f"{h}.c"; exe = WORK / f"{h}.exe"
    if not exe.exists():
        c.write_text(src, encoding="utf-8")
        r = subprocess.run([CL, "-w", "-O0", "-o", str(exe), str(c), *extra], capture_output=True, text=True)
        if r.returncode != 0:
            return None, r.stderr[:400]
    return exe, ""

def run(src, args=(), cwd=None, timeout=10, stdin=None):
    exe, err = build(src)
    if exe is None:
        return "CE", err
    try:
        r = subprocess.run([str(exe), *args], capture_output=True, text=True, cwd=cwd or WORK, timeout=timeout, input=stdin, errors="replace")
    except subprocess.TimeoutExpired:
        return "HANG", ""
    if r.returncode != 0:
        return "RC%d" % r.returncode, r.stdout
    return "OK", r.stdout

def verdict(src, expected, **kw):
    st, out = run(src, **kw)
    if st != "OK":
        return st
    return "PASS" if out.strip() == expected.strip() else "WRONG"

def fill(lines, idx, repl):
    L = list(lines); L[idx] = repl; return "\n".join(L) + "\n"

def fillblank_report(step, prefix, suffix, expected, **kw):
    """returns {optionId: verdict}"""
    res = {}
    for o in step["options"]:
        res[o["id"]] = verdict(prefix + fill(step["lines"], step["blankIndex"], o["value"]) + suffix, expected, **kw)
    return res

def order_report(step, make_src, expected, **kw):
    """make_src(list_of_lines)->src. returns list of permutations (as index tuples) that PASS."""
    n = len(step["lines"]); good = []
    for p in itertools.permutations(range(n)):
        if verdict(make_src([step["lines"][i] for i in p]), expected, **kw) == "PASS":
            good.append(p)
    return good

def bug_diff(fb_step, bug_step):
    """lines of the findbug that differ from the fillblank program (blank filled with the key)."""
    key = [o for o in fb_step["options"] if o["id"] == fb_step["correctId"]][0]["value"]
    good = list(fb_step["lines"]); good[fb_step["blankIndex"]] = key
    gl = [l.strip() for l in "\n".join(good).split("\n")]
    bl = [l.strip() for l in bug_step["lines"]]
    if len(gl) != len(bl):
        return ("LEN", len(gl), len(bl))
    return [i for i, (a, b) in enumerate(zip(gl, bl)) if a != b]

def why(src):
    return build(src)[1]
