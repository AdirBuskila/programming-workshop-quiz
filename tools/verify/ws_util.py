"""Helpers shared by the step-author checks of 23B-B, 22B-A, 22B-B, 21B-A (builds on step_lib.py).
numeric()/text_out(): run a C probe and compare to the shipped step; fn_lines(): function lines of a stored solution."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from step_lib import ROOT, Item, run, find  # noqa: E402,F401


def raw(code):
    return json.load(open(ROOT / "tools" / "raw" / f"{code}.json", encoding="utf-8"))


def question(code, num, part=None):
    for q in raw(code)["questions"]:
        if q["num"] == num and q.get("part") == part:
            return q
    raise KeyError((num, part))


def fn_lines(code, num, part, header_start):
    """Non-blank lines of the function whose header starts with header_start, from the stored solution."""
    sol = question(code, num, part)["solution"]
    ls = [ln for ln in sol.split("\n") if ln.strip() and not ln.startswith("```")]
    i0 = [i for i, ln in enumerate(ls) if ln.startswith(header_start)]
    assert len(i0) == 1, header_start
    i1 = next(i for i in range(i0[0], len(ls)) if ls[i] == "}")
    return ls[i0[0]:i1 + 1]


def probe(src):
    r = run(src)
    assert r[0] == 0, r
    return r[1]


def numeric(code, num, part, hint, src):
    s = find(code, num, part, "numeric", hint)
    out = probe(src).split()
    got = float(out[-1])
    ok = abs(got - s["answer"]) <= s.get("tol", 0)
    print(f"{code} Q{num}{part or ''} numeric[{hint}] shipped={s['answer']} real={got} {'OK' if ok else 'MISMATCH'}")
    return ok


def text_out(code, num, part, hint, src):
    s = find(code, num, part, "text", hint)
    got = probe(src)
    ok = got in s["accept"]
    print(f"{code} Q{num}{part or ''} text[{hint}] accept={s['accept']} real={got!r} {'OK' if ok else 'MISMATCH'}")
    return ok


def one_line_diff(a, b, idx):
    d = [i for i in range(len(a)) if a[i].strip() != b[i].strip()]
    assert len(a) == len(b) and d == [idx], (d, idx)
