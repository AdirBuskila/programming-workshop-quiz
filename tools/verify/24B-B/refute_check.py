import sys, pathlib, random, itertools, re, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from refute_common import *
C = "24B-B"
random.seed(5)
NL = "\n"
BSN = "\\n"

# ---------------- Q1
q = Q(C, 1)
PRE = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct item { int number; struct item* next; } Item;\n"
cases = [[23, 4, -78, 34578, 79, -185, 0, 998, 9, 36], [5], [-5], [0], [123456789, -1], [10, -10, 99, -99, 100]]
for _ in range(40):
    cases.append([random.choice([1, -1]) * random.randint(0, 10 ** random.randint(0, 9)) for _ in range(random.randint(1, 12))])


def model1(A):
    n = max(len(str(abs(a))) for a in A)
    ls = [sorted(a for a in A if len(str(abs(a))) == d + 1) for d in range(n)]
    return "size=%d" % n + "".join(" |" + ",".join(map(str, l)) for l in ls)


exp1 = NL.join(model1(A) for A in cases) + NL
drv1 = "static int cmp(const void*a,const void*b){return *(int*)a-*(int*)b;}\nint main(void){\n"
for A in cases:
    drv1 += ('{ int A[]={%s}; int sz=%d,n; Item** L=numSeparation(A,sz,&n); printf("size=%%d",n); '
             'for(int d=0;d<n;d++){ int b[64],k=0; for(Item*p=L[d];p;p=p->next) b[k++]=p->number; qsort(b,k,sizeof(int),cmp); '
             'printf(" |"); for(int t=0;t<k;t++) printf(t?",%%d":"%%d",b[t]); } printf("\\n"); }\n') % (",".join(map(str, A)), len(A))
drv1 += "return 0;}\n"
sol = blocks(q["solution"])[0]
fixed = sol.replace("digitsNumber(int num)", "int digitsNumber(int num)", 1)
print("Q1 official as printed (no int on digitsNumber):", verdict(PRE + sol + drv1, exp1))
print("Q1 official with int:", verdict(PRE + fixed + drv1, exp1))
s = q["steps"]
print("Q1 numerics", s[0]["answer"], len(str(abs(-185))), s[1]["answer"], model1(cases[0]).split()[0])
helpers = fixed[:fixed.index("Item** numSeparation")]
fb = s[2]
print("Q1 fillblank", fillblank_report(fb, PRE + helpers, drv1, exp1), "correct", fb["correctId"])
od = s[3]
print("Q1 order good perms", order_report(od, lambda L: PRE + helpers + "Item** numSeparation(int* A, int sz, int* p_size)\n{\n" + NL.join(L) + "\n}\n" + drv1, exp1))
fbug = s[4]
hs = helpers[helpers.index("void headInsert"):]
print("Q1 findbug:", verdict(PRE + NL.join(fbug["lines"]) + NL + hs + fixed[fixed.index("Item** numSeparation"):] + drv1, exp1))
ref = ["int digitsNumber(int num)", "{", "       int count = 1, abs_num = abs(num);", "       while (abs_num > 9)", "       {", "              count++;", "              abs_num /= 10;", "       }", "       return count;", "}"]
print("Q1 diff lines", [i for i, (a, b) in enumerate(zip(ref, fbug["lines"])) if a.strip() != b.strip()], fbug["bugIndex"])

# ---------------- Q2
q = Q(C, 2)
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n"
dims = [(3, 4), (1, 1), (1, 5), (5, 1), (2, 2)] + [(random.randint(1, 6), random.randint(1, 6)) for _ in range(15)]
mats = [[[random.randint(1, 99) for _ in range(c)] for _ in range(r)] for r, c in dims]
mats[0] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def model2(M):
    r, c = len(M), len(M[0])
    F = [[0] * (c + 2) for _ in range(r + 2)]
    for i in range(r):
        for j in range(c):
            F[i + 1][j + 1] = M[i][j]
    return NL.join(" ".join(map(str, row)) for row in F)


exp2 = NL.join(model2(M) + NL + "--" for M in mats) + NL
drv2 = "int main(void){\n"
for M in mats:
    r, c = len(M), len(M[0])
    drv2 += ('{ int r=%d,c=%d,i,j; int** M=(int**)malloc(r*sizeof(int*)); int v[]={%s}; '
             'for(i=0;i<r;i++){M[i]=(int*)malloc(c*sizeof(int)); for(j=0;j<c;j++) M[i][j]=v[i*c+j];} '
             'int** F=matrixToFrame(M,r,c); for(i=0;i<r+2;i++){ for(j=0;j<c+2;j++) printf(j?" %%d":"%%d",F[i][j]); printf("\\n"); } printf("--\\n"); }\n') % (
        r, c, ",".join(str(x) for row in M for x in row))
drv2 += "return 0;}\n"
sol = blocks(q["solution"])[0]
print("Q2 official:", verdict(PRE2 + sol + drv2, exp2))
s = q["steps"]
print("Q2 numerics", s[0]["answer"], 5 * 6 - 12, s[1]["answer"], mats[0][1][2])
fb = s[2]
head = sol[:sol.index("int** matrixToFrame")]
print("Q2 fillblank", fillblank_report(fb, PRE2 + head, drv2, exp2), "correct", fb["correctId"])
od = s[3]
print("Q2 order good perms", order_report(od, lambda L: PRE2 + head + "int** matrixToFrame(int** M, int rows, int cols)\n{\n" + NL.join(L) + "\n}\n" + drv2, exp2))
fbug = s[4]
print("Q2 findbug:", verdict(PRE2 + head + NL.join(fbug["lines"]) + NL + drv2, exp2), "diff", bug_diff(fb, fbug), fbug["bugIndex"])

# ---------------- Q3
q = Q(C, 3)
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n"


def uniq(l):
    return l.isalpha() and l.isascii() and len(set(l.lower())) == len(l)


lines = ["abc#xyz", "table", "Alisa", "Walla", "Michael", "aA", "Ab", "", "a", "zz", "abcdefghijklmnopqrstuvwxyz",
         "ABCDEFGHIJKLMNOPQRSTUVWXYZa", "ab c", "q1", "Zq", "xyzX"]
for _ in range(40):
    lines.append("".join(random.choice("abcdeABCDE#") for _ in range(random.randint(1, 6))))
(WORK / "in1.txt").write_bytes((NL.join(lines) + NL).encode())
(WORK / "in2.txt").write_bytes(NL.join(["table", "Michael", "abc"]).encode())  # last line w/o newline
exp_keep = "".join(l[::-1] + NL for l in lines if uniq(l) or l == "")
exp_drop = "".join(l[::-1] + NL for l in lines if l != "" and uniq(l))
drv3 = 'int main(void){ processFiles("in1.txt","out1.txt"); processFiles("in2.txt","out2.txt"); return 0; }\n'


def run3(src, which="out1.txt"):
    for f in ("out1.txt", "out2.txt"):
        p = WORK / f
        if p.exists():
            p.unlink()
    st, o = run(src)
    if st != "OK":
        return st, None
    return st, ((WORK / which).read_bytes().decode().replace(chr(13)+chr(10), chr(10)) if (WORK / which).exists() else None)


sol = blocks(q["solution"])[0]
st, out = run3(PRE3 + sol + drv3)
print("Q3 official status", st, "| matches empty-line-kept:", out == exp_keep, "| empty-line-dropped:", out == exp_drop)
st, out2 = run3(PRE3 + sol + drv3, "out2.txt")
print("Q3 official, last line w/o newline ->", repr(out2), "(ideal: elbat/leahciM/cba)")
s = q["steps"]
ex = ["abc#xyz", "table", "Alisa", "Walla", "Michael"]
print("Q3 numeric", s[0]["answer"], sum(1 for l in ex if uniq(l)), "| rejected only by case:", [l for l in ex if l.isalpha() and len(set(l)) == len(l) and not uniq(l)], "| (Alisa is case-sensitive-unique):", len(set("Alisa")) == 5, s[1]["correctId"])
helpers = sol[:sol.index("void processFiles")]
rs = sol[:sol.index("int hasUniqueLetters")]
pf = sol[sol.index("void processFiles"):]
hu = sol[sol.index("int hasUniqueLetters"):sol.index("void processFiles")]
fb = s[2]
exp = exp_keep
for o in fb["options"]:
    src = PRE3 + rs + fill(fb["lines"], fb["blankIndex"], o["value"]) + pf + drv3
    st, out = run3(src)
    print("  Q3 fb", o["id"], st, "PASS" if out == exp else "WRONG")
od = s[3]
good = []
for p in itertools.permutations(range(3)):
    L = [od["lines"][i] for i in p]
    src = PRE3 + helpers + "void processFiles(const char* inputFilename, const char* outputFilename)\n{\n" + NL.join(L) + "\n}\n" + drv3
    st, out = run3(src)
    print("   perm", p, st, "PASS" if out == exp else "WRONG")
    if st == "OK" and out == exp:
        good.append(p)
print("Q3 order good perms", good)
fbug = s[4]
src = PRE3 + NL.join(fbug["lines"]) + NL + hu + pf + drv3
st, out = run3(src)
print("Q3 findbug:", st, "PASS" if out == exp else "WRONG", repr(out[:40]) if out else out)
good_rev = ["void reverseString(char* str)", "{", "       int i = 0, j = strlen(str) - 1;", "       char temp;", "       for (; i < j; i++, j--)", "       {", "              temp = str[i];", "              str[i] = str[j];", "              str[j] = temp;", "       }", "}"]
print("Q3 findbug diff", [i for i, (a, b) in enumerate(zip(good_rev, fbug["lines"])) if a.strip() != b.strip()], fbug["bugIndex"])
