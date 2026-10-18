"""Machine check of courses/c_traps/C01..C09 with clang.
Run from the app root:  PYTHONUTF8=1 py tools/verify/needhelp/c_traps/check.py
Every question whose stem has a C snippet is compiled and run (-O0 and -O2, both must agree) and its
output is compared with the stored answer. Conceptual questions have a proof program in PROOF.
Exits 1 on any failure."""
import json, pathlib, re, shutil, subprocess, sys, tempfile

CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang"
ROOT = pathlib.Path(__file__).resolve().parents[4]
FAILS, COUNT = [], [0]


def check(cond, msg):
    COUNT[0] += 1
    if not cond:
        FAILS.append(msg)
        print("FAIL", msg)


HEAD = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"


def run(src, files=None, opt="-O0"):
    d = pathlib.Path(tempfile.mkdtemp(prefix="nh_ct_"))
    try:
        for k, v in (files or {}).items():
            (d / k).write_bytes(v.encode())
        (d / "t.c").write_text(src, encoding="utf-8")
        p = subprocess.run([CLANG, "-w", opt, "-o", str(d / "t.exe"), str(d / "t.c")], capture_output=True, text=True, cwd=d)
        if p.returncode:
            return ("BUILD", p.stderr[:300])
        r = subprocess.run([str(d / "t.exe")], capture_output=True, text=True, errors="replace", timeout=5, cwd=d)
        return ("OK" if r.returncode == 0 else "CRASH", " ".join(r.stdout.split()))
    finally:
        shutil.rmtree(d, ignore_errors=True)


def both(src, files=None):
    a, b = run(src, files, "-O0"), run(src, files, "-O2")
    check(a == b, f"-O0 and -O2 disagree: {a} vs {b}")
    return a


def wrap(code):
    if "main" in code:
        return HEAD + code
    return HEAD + "int main(void){\n" + code + "\nreturn 0;}\n"


def wrap_globals(code):
    # snippets with top-level definitions and no main: put the snippet before a plain main
    return HEAD + code


raw = subprocess.run(["node", "tools/course_load.js"], capture_output=True, cwd=ROOT, check=True)
LV = {e["level"]["id"]: e["level"] for e in json.loads(raw.stdout.decode("utf-8"))["levels"] if e["courseId"] == "c_traps"}
Q = {q["id"]: q for lv in LV.values() for q in lv["questions"] if "id" in q}


def strip(s):
    return s.replace("`", "").strip()


def stored(q):
    if "step" in q:
        return str(int(q["step"]["answer"]))
    return strip({o["id"]: o["value"] for o in q["options"]}[q["correctId"]])


def stem(q):
    return q["step"]["prompt"] if "step" in q else q["question"]


# files the stems describe
FILES = {
    "C06-Q1": {"data.txt": "abc"},
    "C06-Q2": {"data.txt": "hi"},
    "C06-Q3": {"data.txt": "1 2 3\n"},
    "C06-Q4": {"data.txt": "ab\ncd\n"},
    "C06-Q5": {"data.txt": "5 x"},
    "C06-Q6": {},
}
# stems whose snippets are fragments needing a main with declared globals or a function
SPECIAL = {
    "C07-Q1": None, "C07-Q4": None, "C08-Q4": None,   # complete programs after wrapping (globals + main in stem)
}
# conceptual questions: proof programs (expected output) -- the statement is then asserted below
PROOF = {
    # C01-Q4: exactly one of the four statements prints non-zero
    "C01-Q4": [("printf(\"%d\", '\\0');", "0"), ("printf(\"%d\", '0');", "48"), ("printf(\"%d\", '0' - '0');", "0"), ("printf(\"%d\", 'a' - 'a');", "0")],
    # C04-Q5: sizeof of an array parameter equals sizeof of a pointer to its element type
    "C04-Q5": "void f(int a[]){ printf(\"%d\", (int)(sizeof a == sizeof(int *))); }\nint main(void){ int b[10]; f(b); return 0; }",
    # C05-Q5: it compiles (not a compile error); writing is UB per C11 6.4.5p7
    "C05-Q5": "int main(void){ char *s = \"hi\"; if (0) s[0] = 'H'; printf(\"compiled\"); return 0; }",
    # C07-Q5: it compiles (not a compile error); free of a non-heap address is UB per C11 7.22.3.3
    "C07-Q5": "int main(void){ int a[3]; if (0) free(a); printf(\"compiled\"); return 0; }",
    # C07-Q3: malloc leaves the content indeterminate (C11 7.22.3.4); the program just compiles and the value is not asserted
    "C07-Q3": "int main(void){ int *p = (int *)malloc(sizeof(int)); free(p); printf(\"compiled\"); return 0; }",
    # C08-Q6: the preprocessor accepts the three directives and rejects '#typedef'
    "C08-Q6": None,
}
PROOF_EXPECT = {"C04-Q5": "1", "C05-Q5": "compiled", "C07-Q5": "compiled", "C07-Q3": "compiled"}

# ------------------------------------------------------------ run every snippet
for qid, q in Q.items():
    if qid in PROOF:
        continue
    m = re.search(r"```c\n(.*?)```", stem(q), re.S)
    check(m is not None, f"{qid} has no C snippet and no proof")
    if not m:
        continue
    code = m.group(1)
    src = HEAD + code if "main" in code else wrap(code)
    # a snippet with functions/globals but without main cannot occur here; fragments go into main
    r = both(src, FILES.get(qid, {}))
    check(r[0] == "OK", f"{qid} run status {r}")
    want = stored(q)
    check(r[1] == " ".join(want.split()), f"{qid}: program printed {r[1]!r}, stored answer {want!r}")
    # every other option differs from the real output (so exactly one option is right)
    if "options" in q:
        outs = [strip(o["value"]) for o in q["options"]]
        n = sum(1 for o in outs if " ".join(o.split()) == r[1])
        check(n == 1, f"{qid}: {n} options equal the real output")

# C01-Q4 proofs
for stmt, out in PROOF["C01-Q4"]:
    r = both(HEAD + "int main(void){" + stmt + " return 0;}")
    check(r == ("OK", out), f"C01-Q4 {stmt} -> {r}")
check(stored(Q["C01-Q4"]) == "printf(\"%d\", '0');", "C01-Q4 stored answer is the '0' statement")

for qid in ("C04-Q5", "C05-Q5", "C07-Q5", "C07-Q3"):
    r = both(HEAD + PROOF[qid])
    check(r == ("OK", PROOF_EXPECT[qid]), f"{qid} proof {r}")
check(stored(Q["C04-Q5"]).startswith("sizeof a בתוך f הוא גודל של מצביע"), "C04-Q5 stored answer")
check(stored(Q["C05-Q5"]).startswith("התנהגות לא מוגדרת"), "C05-Q5 stored answer says UB")
check(stored(Q["C07-Q5"]).startswith("התנהגות לא מוגדרת"), "C07-Q5 stored answer says UB")
check(stored(Q["C07-Q3"]).startswith("לא מוגדר"), "C07-Q3 stored answer says indeterminate")

# C08-Q6: '#typedef' is rejected by the preprocessor, the others are accepted
r = run("#typedef int T;\nint main(void){return 0;}\n")
check(r[0] == "BUILD", "C08-Q6 '#typedef' must be a build error")
for d in ("#define A 1\n", "#ifndef A\n#define A 2\n#endif\n", "#include <stdio.h>\n"):
    check(run(d + "int main(void){return 0;}\n")[0] == "OK", f"C08-Q6 directive {d!r}")
check(stored(Q["C08-Q6"]) == "typedef", "C08-Q6 stored answer")

# every own question is covered
for qid in Q:
    check(qid in PROOF or re.search(r"```c", stem(Q[qid])), f"{qid} not covered")

# ------------------------------------------------------------ boss: bank pulls
bank = json.load(open(ROOT / "questions.json", encoding="utf-8"))
bank = bank if isinstance(bank, list) else bank.get("questions", bank)
byid = {b["id"]: b for b in bank}
AVOID = ("23B-B", "22B-B", "22B-A", "21B-A")
for b in LV["C09"]["questions"]:
    q = byid.get(b["bankId"])
    check(q is not None and q.get("official") and not q["id"].startswith(AVOID) and q.get("topic") == "c_traps_mcq"
          and (q["kind"] == "mcq" or q.get("stepsSource") in ("ai-verified", "official")),
          f"C09 {b['bankId']} must be an official, verified c_traps_mcq question of a clean sitting")


def bsrc(qid):
    sol = byid[qid]["question"]
    c = re.search(r"```c\n(.*?)```", sol, re.S).group(1)
    c = re.sub(r"void\s+main\s*\(\s*\)", "int main()", c)   # exam code uses void main; only the exit status differs
    c = c.replace("return;", "return 0;")
    i = c.rstrip().rfind("}")
    return c[:i] + "return 0;\n}\n"


# boss programs, compiled (void main is accepted) and compared with the official solution output
FIL = {"file.dat": "abc"}
r = both(HEAD + bsrc("25B-A-Q6").replace('"file.dat"', '"file.dat"'), FIL)
check(r == ("OK", "111"), f"C09 25B-A-Q6 {r}")
r = both(HEAD + bsrc("25B-B-Q6"))
check(r == ("OK", "10"), f"C09 25B-B-Q6 {r}")
r = both(HEAD + bsrc("19B-A-Q5"))
check(r == ("OK", "1"), f"C09 19B-A-Q5 {r}")
# 19S-A-Q4d: 'typedef' is the only non-directive; 20B-A-Q4a: gets has no size and drops '\n', fgets keeps it
check(run("#typedef int T;\nint main(void){return 0;}\n")[0] == "BUILD", "C09 19S-A-Q4d typedef is not a directive")
check(byid["19S-A-Q4d"]["correctId"] == "e" and byid["20B-A-Q4a"]["correctId"] == "c", "C09 mcq keys")
r = both(HEAD + "int main(void){ char s[10]; FILE*f=fopen(\"d.txt\",\"r\"); fgets(s,10,f); printf(\"%d\",(int)strlen(s)); return 0;}", {"d.txt": "ab\n"})
check(r == ("OK", "3"), f"C09 20B-A-Q4a fgets keeps the newline {r}")

print(f"\nassertions: {COUNT[0]}, failures: {len(FAILS)}")
sys.exit(1 if FAILS else 0)
