"""Arbiter checks for the 21B-B Q1 steps (official filesMerge + minimal fix). Run: PYTHONUTF8=1 py tools/verify/21B-B/arb_steps_check.py
Reads the SHIPPED tools/raw/21B-B.json; every value is re-measured with clang (see also arb_q1.c)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

PRE = r'''#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
'''
MAIN = r'''
static void w(const char *n, const char *s){ FILE *f=fopen(n,"wb"); fputs(s,f); fclose(f); }
static void show(const char *n){ FILE *f=fopen(n,"rb"); int c; while((c=fgetc(f))!=EOF) putchar(c); fclose(f); puts("|"); }
int main(void){
 _set_fmode(_O_BINARY);
 const char* C[][2] = {{"3 8 12 16 20\n0 2 2 6\n9 10 10 11 19 26\n4 4 4 5\n", "9 17\n2 6 7 11\n5 13 14 18\n"},
   {"1 5\n", "2 3\n7 8\n9\n"}, {"1 4\n2\n", "3\n1 1\n"}, {"", "5 6\n"}, {"5 6\n7\n", ""}};
 for (int i = 0; i < 5; i++) { w("a.txt", C[i][0]); w("b.txt", C[i][1]); filesMerge("a.txt","b.txt","o.txt"); show("o.txt"); }
 return 0;}
'''
def build(L): return PRE + "\n".join(L) + MAIN

fb = S.find("21B-B", 1, None, "fillblank", "השלימו")
ref = list(fb["lines"]); ref[fb["blankIndex"]] = ref[fb["blankIndex"]].replace("___", "if (!feof(in1))")
it = S.Item("21B-B", 1, None, build, ref)
print(it.ref[1])
want = ("3 8 9 12 16 17 20 \n0 2 2 2 6 6 7 11 \n5 9 10 10 11 13 14 18 19 26 \n4 4 4 5\n|\n"
        "1 2 3 5 \n7 8\n9\n|\n1 3 4 \n1 1 2 \n|\n5 6\n|\n5 6\n7\n|\n")
assert it.ref[1] == want, "fixed solution does not give the expected outfiles"
it.fill("השלימו"); it.bug("בגרסה הבאה")

# numeric: blank lines produced by the ORIGINAL official code on the exam example
orig = [l for l in ref if "fix:" not in l]
k = [i for i, l in enumerate(orig) if l.strip() == "if (!feof(in1))"][0]
orig[k:k + 2] = ["    fseek(in1, -1, SEEK_CUR);", "    fseek(in2, -1, SEEK_CUR);"]
r = S.run(build(orig))
ex = r[1].split("|\n")[0]
blanks = sum(1 for ln in ex.split("\n")[:-1] if ln == "")
num = S.find("21B-B", 1, None, "numeric", "המקורי")
print("original example outfile:", repr(ex), "blank lines:", blanks)
ok = it.finish() and blanks == num["answer"] == 1
print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
