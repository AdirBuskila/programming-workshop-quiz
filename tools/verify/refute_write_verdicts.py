"""Writes tools/raw/_verify_<CODE>.json for the refutation of 25B-A, 24B-A, 24B-B, 23B-A (verdicts come from refute_check.py runs)."""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from richtext import part_suffix

ROOT = pathlib.Path(__file__).resolve().parents[2]
V = {}
V["25B-A"] = dict(
    derivations={"q4": "3 5 / 5 5 / 4 4 / 19 19 / 18 18", "q5a": "444 with 4-byte pointers (b); 888 on 64-bit (no option -> f)", "q5b": "d (48)", "q6": "111"},
    items={
        "1": {"solution": "agree (exhaustive strings len<=7 over space,a,b plus 300 random; result nodes are reused ones)", "rubric": "agree (12+6+14+8=40)", "pitfalls": "agree",
              "steps": ["agree numeric 7", "agree numeric 3",
                        "agree fillblank a unique (b crashes on all-space list, c/d wrong output); note: deleteHead/deleteNext are used but not shown in the step",
                        "DISAGREE order: not forced. Permutation (1,2,3,0), i.e. the leading-space deletion block moved to the END, gives identical output on every test (the main loop already removes repeated and trailing spaces, the last while strips the leading ones). First divergence: block 0 vs block 3. Fix: merge blocks 0 and 1 or drop the order step",
                        "agree findbug idx 11 (single line differs, trailing space stays)"]},
        "2": {"solution": "agree", "rubric": "agree (8+10+14+8=40)", "pitfalls": "agree",
              "steps": ["agree 3", "agree 21", "agree fillblank a unique (b,c,d wrong values)", "agree findbug idx 7 (single line differs, diagonal 0)"]},
        "3": {"solution": "agree (both versions; 60 random files, edge 99-char line, missing file)", "rubric": "agree (6+8+14+8+4=40)", "pitfalls": "agree",
              "steps": ["agree 5", "agree 1", "agree fillblank a unique (b gives 4, c/d give 0)", "agree order (only identity passes)", "agree findbug idx 7 (fgets(...,10) cuts words)"]},
        "4": {"solution": "agree (clang run)", "rubric": "agree (3+2+2+3=10)", "pitfalls": "agree",
              "steps": ["agree 5", "agree 4", "agree choice a (18 18)", "agree output order"]},
        "5א": {"key": "b under 4-byte pointers; own clang run on 64-bit prints 888 (no matching option, would be f). Key is platform dependent.",
               "explanation": "agree: it states explicitly that the key assumes 4-byte pointers and that a 64-bit compiler prints 888. Minor: the first sentence asserts 4 bytes as fact, and printing size_t with %d is itself UB on 64-bit"},
        "5ב": {"key": "agree d (48)", "explanation": "agree"},
        "6": {"solution": "agree 111", "rubric": "agree (4+3+3=10)", "pitfalls": "agree", "steps": ["agree 1", "agree 3", "agree text 111"]}})
V["24B-A"] = dict(
    derivations={"q4": "200 400 / 300 300 / 400 200 / 600", "q5a": "d (free of a stack array: UB / runtime error)", "q5b": "b (3^2 = 1)", "q6": "24"},
    items={
        "1": {"solution": "agree (both versions, 450 pairs incl. 9999 vs 10000)", "rubric": "agree (14+14+6+6=40)", "pitfalls": "agree",
              "steps": ["agree -1", "agree 1", "agree fillblank a unique (b swaps, c/d wrong on equal lengths)", "agree order (only identity passes)", "agree findbug idx 16 (<= returns -1 on equal first digit)"]},
        "2": {"solution": "agree (35 cases; empty results give size 0 and NULL on this clang/UCRT, but realloc(p,0) returning NULL is implementation-specific)", "rubric": "agree (8+12+12+8=40)", "pitfalls": "agree",
              "steps": ["agree 4", "agree 3", "agree fillblank a unique (b,c wrong; d wrong, crashes on A[j]==0)", "agree order (only identity passes)", "agree findbug idx 8"]},
        "3": {"solution": "agree (1776 board/word pairs vs python model). Environment quirk, not an exam error: Windows text-mode ftell/fseek is wrong on files that contain a newline; binary mode reproduces POSIX behaviour", "rubric": "agree (4+8+10+12+6=40)", "pitfalls": "agree",
              "steps": ["agree choice a (byte, baby yes; gat no)", "agree 4", "agree fillblank a unique (-1,-3,0 fail)", "agree order (only identity passes)", "agree findbug idx 24 (yte fails)"]},
        "4": {"solution": "agree", "rubric": "agree (3+2+2+3=10)", "pitfalls": "agree", "steps": ["agree 400", "agree 300", "agree 600", "agree output order"]},
        "5א": {"key": "agree d", "explanation": "agree (calls the array static, it is automatic; minor wording; free() on non-heap memory is UB, runtime error is the expected answer)"},
        "5ב": {"key": "agree b (3^2=1)", "explanation": "agree"},
        "6": {"solution": "agree 24", "rubric": "agree (3+4+3=10)", "pitfalls": "agree", "steps": ["agree 1", "agree 2", "agree text 24"]}})
V["24B-B"] = dict(
    derivations={"q4": "2 2 / 4 2 / 2 6 / 8 6 / 8 10", "q5a": "d", "q5b": "c", "q6": "-1 ((int)4294967295: implementation-defined conversion, 32-bit int)"},
    items={
        "1": {"solution": "agree once int is added to digitsNumber (as printed it does not compile, as the note already says); 46 arrays compared as per-list multisets", "rubric": "agree (8+8+8+10+6=40)", "pitfalls": "agree",
              "steps": ["agree 3", "agree 5", "agree fillblank a unique", "agree order (only identity passes)", "agree findbug idx 2"]},
        "2": {"solution": "agree (20 matrices)", "rubric": "agree (14+14+8+4=40)", "pitfalls": "agree",
              "steps": ["agree 18", "agree 7", "agree fillblank a unique", "agree order (only identity passes)", "agree findbug idx 6"]},
        "3": {"solution": "agree on newline-terminated inputs. Official quirks not covered by the question: a last line without trailing newline loses its last char (abc -> ba); an empty line is written as an empty line", "rubric": "agree (8+12+6+8+6=40)", "pitfalls": "agree",
              "steps": ["agree 2", "agree choice a (Alisa)", "agree fillblank a unique (b accepts Alisa, c rejects table, d rejects everything)", "agree order (only identity passes; swaps give compile error or wrong output)", "agree findbug idx 2 (empty lines)"]},
        "4": {"solution": "agree", "rubric": "agree (3+2+3+2=10)", "pitfalls": "agree", "steps": ["agree 4", "agree choice a (2 6)", "agree 10", "agree output order"]},
        "5א": {"key": "agree d", "explanation": "agree"},
        "5ב": {"key": "agree c (realloc(NULL,n) == malloc(n); option a is wrong because sizeof(int) bytes are allocated)", "explanation": "agree"},
        "6": {"solution": "agree -1 (needs 32-bit int and two's-complement truncation, implementation-defined; neither the solution nor the steps say so)", "rubric": "agree (4+3+3=10)", "pitfalls": "agree",
              "steps": ["agree 4", "agree 32", "agree 4294967295", "agree -1"]}})
V["23B-A"] = dict(
    derivations={"q4": "x=20,y=5 / x=30,y=10 / x=15,y=10", "q5a": "b", "q5b": "c", "q6": "uts"},
    items={
        "1": {"solution": "agree (67 lists incl. cancelling monomials and empty list)", "rubric": "agree (8+14+12+6=40)", "pitfalls": "agree",
              "steps": ["agree 6", "agree 8", "agree fillblank a unique", "agree order (only identity passes)", "agree findbug idx 20"]},
        "2": {"solution": "agree (84 matrices; empty results give size 0 and NULL on this clang/UCRT; realloc(p,0) is implementation-specific)", "rubric": "agree (8+8+8+10+6=40)", "pitfalls": "agree",
              "steps": ["agree 3", "agree 1", "agree fillblank a unique (option b differs only on a column with equal adjacent values, which the exam example lacks; it fails on my matrices)", "agree order (only identity passes)", "agree findbug idx 4"]},
        "3א": {"solution": "agree. Official line `word[i++] = sentence[i];` is unsequenced (UB); clang -O0 and -O2 happen to read the old i. The fillblank and findbug steps reuse this line; the order step uses the UB-free two-statement form", "rubric": "agree (6+3+3+3=15)", "pitfalls": "agree",
               "steps": ["agree 6", "agree choice a (NULL)", "agree fillblank a unique", "agree order (only identity passes, buffer pre-filled with #)", "agree findbug idx 8"]},
        "3ב": {"solution": "agree", "rubric": "agree (3+2+5+3+2=15)", "pitfalls": "agree",
               "steps": ["agree 3", "agree 4", "agree fillblank a unique (d fails only on one-word sentences)", "agree order (only identity passes)", "agree findbug idx 10"]},
        "3ג": {"solution": "agree", "rubric": "agree (2+4+3+1=10)", "pitfalls": "agree",
               "steps": ["agree 2", "agree 3", "agree fillblank a unique", "agree order (only identity passes)", "agree findbug idx 8"]},
        "4": {"solution": "agree", "rubric": "agree (2+3+3+2=10)", "pitfalls": "agree", "steps": ["agree 20", "agree 30", "agree 10", "agree output order"]},
        "5א": {"key": "agree b", "explanation": "agree"},
        "5ב": {"key": "agree c", "explanation": "agree"},
        "6": {"solution": "agree uts (the intermediate pointer \"puts\"-6 is outside the array: UB in theory, works)", "rubric": "agree (3+3+4=10)", "pitfalls": "agree",
              "steps": ["agree 6", "agree 7", "agree 1", "agree text uts"]}})
MCQ = {"25B-A": {"5א": "b", "5ב": "d"}, "24B-A": {"5א": "d", "5ב": "b"}, "24B-B": {"5א": "d", "5ב": "c"}, "23B-A": {"5א": "b", "5ב": "c"}}
for code, v in V.items():
    raw = json.loads((ROOT / "tools/raw" / f"{code}.json").read_text(encoding="utf-8"))
    answers = {}
    for q in raw["questions"]:
        part = q.get("part")
        hkey = f"{q['num']}{part or ''}"
        akey = f"{q['num']}{part_suffix(part) or ''}"
        if q["kind"] == "mcq":
            answers[akey] = {"answer": MCQ[code][hkey], "confident": True}
        else:
            bad = any(s.startswith("DISAGREE") for s in v["items"][hkey]["steps"])
            answers[akey] = {"agrees": not bad, "confident": True}
            if bad:
                answers[akey]["note"] = "order step not forced, see items"
    out = {"examCode": code, "refuter": "claude",
           "method": "own derivation recorded first (derivations); independent clang runs and python models in tools/verify/%s/refute_* and refute_check.py (shared helper tools/verify/refute_common.py)" % code,
           "derivations": v["derivations"], "items": v["items"], "answers": answers}
    (ROOT / "tools/raw" / f"_verify_{code}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", code)
