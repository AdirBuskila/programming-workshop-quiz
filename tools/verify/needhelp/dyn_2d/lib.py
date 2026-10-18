# -*- coding: utf-8 -*-
"""Shared helpers for the dyn_2d guided-course generator/checker: compile+run C with clang, harness preambles,
step builders that machine-check every stored answer."""
import itertools, json, pathlib, re, shutil, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor

CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang"
PRE = "#include <stdio.h>\n#include <stdlib.h>\n"
# logging allocator: prints every calloc/realloc request so wrong sizes are observable
LOG = PRE + r'''static void *L_calloc(size_t n, size_t s) { printf("[calloc %d x %d]\n", (int)n, (int)s); return calloc(n, s); }
static void *L_realloc(void *p, size_t s) { printf("[realloc %d]\n", (int)s); return realloc(p, s); }
#define calloc L_calloc
#define realloc L_realloc
'''
# tracker: every calloc gets an id, free() logs which id it releases (real free is skipped so reads stay valid)
TRK = PRE + r'''static void *T_p[64]; static int T_n = 0, T_f[64];
static void *T_calloc(size_t n, size_t s) { void *p = calloc(n, s); T_p[T_n] = p; T_f[T_n] = 0; printf("A%d ", T_n); T_n++; return p; }
static void T_free(void *p) { int i; if (!p) return; for (i = 0; i < T_n; i++) if (T_p[i] == p && !T_f[i]) { T_f[i] = 1; printf("F%d ", i); return; } printf("BAD "); }
static int T_leaks(void) { int i, c = 0; for (i = 0; i < T_n; i++) if (!T_f[i]) c++; return c; }
#define calloc T_calloc
#define free T_free
'''


def run(src, flags=()):
    d = pathlib.Path(tempfile.mkdtemp(prefix="pwd2d"))
    try:
        c, exe = d / "t.c", d / "t.exe"
        c.write_text(src, encoding="utf-8")
        p = subprocess.run([CLANG, *(flags or ("-w",)), "-O0", "-o", str(exe), str(c)], capture_output=True, text=True, errors="replace", cwd=d)
        if p.returncode:
            return ("BUILD-FAIL", p.stderr[:200])
        try:
            r = subprocess.run([str(exe)], capture_output=True, text=True, errors="replace", timeout=10, cwd=d)
        except subprocess.TimeoutExpired:
            return ("TIMEOUT", "")
        return (r.returncode, r.stdout)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def ok_out(src, flags=()):
    rc, out = run(src, flags)
    assert rc == 0, (rc, out, src[-600:])
    return out.strip()


def main_of(defs, body):
    """The text the student sees == the text we compile (plus includes)."""
    b = "\n".join(body) if isinstance(body, list) else body
    return (defs.rstrip() + "\n\n" if defs else "") + "int main(void)\n{\n" + b + "\n    return 0;\n}\n"


def lines_join(lines):
    return "\n".join(lines)


# ------------------------------------------------------------------ builders for questions
def mcq(qid, stem, options, correct, explanation, recap, verify=None):
    """options: list of strings (rich text). correct: index. verify: callable -> index that the machine says is right."""
    if verify is not None:
        got = verify()
        assert got == correct, (qid, "machine says option", got, "but stored", correct)
    ids = "abcdefgh"
    return {"id": qid, "question": stem, "options": [{"id": ids[i], "value": o} for i, o in enumerate(options)],
            "correctId": ids[correct], "explanation": explanation, "recap": recap}


def step_q(qid, step, recap):
    return {"id": qid, "step": step, "recap": recap}


def numeric(qid, prompt, answer, explain, recap):
    return step_q(qid, {"type": "numeric", "prompt": prompt, "answer": answer, "tol": 0, "explain": explain}, recap)


def order(qid, prompt, blocks, build, explain, recap):
    """blocks stored in the correct order. build(blocks)->full program. Every pair swapped must change behaviour."""
    ref = run(build(blocks))
    assert ref[0] == 0, (qid, "reference does not run", ref)
    jobs = []
    for i, j in itertools.combinations(range(len(blocks)), 2):
        b = list(blocks); b[i], b[j] = b[j], b[i]
        jobs.append(((i, j), b))
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(lambda t: run(build(t[1])), jobs))
    for (pair, _), r in zip(jobs, res):
        assert r != ref, (qid, "swap", pair, "does not change behaviour", r)
    return step_q(qid, {"type": "order", "prompt": prompt, "code": True, "lines": list(blocks), "explain": explain}, recap)


def fillblank(qid, prompt, lines, blank_idx, options, correct, build, explain, recap):
    """build(line_text)->program; lines[blank_idx] holds ___. Correct option must reproduce the reference and all others differ."""
    outs = []
    for o in options:
        outs.append(run(build(lines[blank_idx].replace("___", o))))
    ref = outs[correct]
    assert ref[0] == 0, (qid, "correct option does not run", ref)
    for i, r in enumerate(outs):
        if i != correct:
            assert r != ref, (qid, "distractor", options[i], "behaves like the answer", r)
    ids = "abcdefgh"
    return step_q(qid, {"type": "fillblank", "prompt": prompt, "code": True, "lines": list(lines), "blankIndex": blank_idx,
                        "options": [{"id": ids[i], "type": "text", "value": o} for i, o in enumerate(options)],
                        "correctId": ids[correct], "explain": explain}, recap)


def findbug(qid, prompt, lines, bug_idx, fixed_line, build, explain, recap):
    good = list(lines); good[bug_idx] = fixed_line
    ref = run(build(good))
    assert ref[0] == 0, (qid, "fixed version does not run", ref)
    bad = run(build(lines))
    assert bad != ref, (qid, "bug is not observable", bad)
    return step_q(qid, {"type": "findbug", "prompt": prompt, "code": True, "lines": list(lines), "bugIndex": bug_idx, "explain": explain}, recap)
