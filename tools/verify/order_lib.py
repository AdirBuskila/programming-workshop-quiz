"""Shared checker for `order` steps: every pair of blocks swapped must change the observable behaviour
(a build failure, a hang or a different output all count). Reads the shipped tools/raw/<CODE>.json."""
import json, os, subprocess, sys, tempfile, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]


def find_step(code, num, part, prompt_part):
    d = json.load(open(ROOT / "tools" / "raw" / f"{code}.json", encoding="utf-8"))
    for q in d["questions"]:
        if q["num"] == num and q.get("part") == part:
            for s in q["steps"]:
                if s["type"] == "order" and prompt_part in s["prompt"]:
                    return s["lines"]
    raise KeyError((num, part, prompt_part))


def run(src, tag, stdin=""):
    tmp = pathlib.Path(tempfile.mkdtemp())
    c, exe = tmp / "t.c", tmp / "t.exe"
    c.write_text(src)
    r = subprocess.run(["clang", "-w", "-O0", "-o", str(exe), str(c)], capture_output=True, text=True)
    if r.returncode:
        return "BUILD-FAIL"
    try:
        r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=5, input=stdin)
        return f"rc={r.returncode} " + r.stdout[:4000]
    except subprocess.TimeoutExpired:
        return "TIMEOUT"


def check(code, label, blocks, build, stdin=""):
    """build(list_of_blocks) -> full C source (includes + blocks joined + main)."""
    base = run(build(blocks), "base", stdin)
    print(f"[{code} {label}] {len(blocks)} blocks, identity output: {base[:60]!r}")
    bad = 0
    if base.startswith(("BUILD-FAIL", "TIMEOUT")):
        print("  identity does not run"); return 1
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            b = list(blocks); b[i], b[j] = b[j], b[i]
            out = run(build(b), "x", stdin)
            same = out == base
            kind = "BUILD" if out == "BUILD-FAIL" else ("HANG" if out == "TIMEOUT" else ("DIFF" if not same else "SAME"))
            if same:
                bad += 1
            print(f"  swap {i}<->{j}: {kind}")
    print("  RESULT:", "FORCED" if not bad else f"{bad} commuting pair(s)")
    return bad
