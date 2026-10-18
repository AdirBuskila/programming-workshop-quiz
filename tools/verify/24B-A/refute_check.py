import sys, pathlib, random, itertools, re, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from refute_common import *
C = "24B-A"
random.seed(11)

# ---------------- Q1
q = Q(C, 1)
PRE = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct item { int digit; struct item* next; } Item;\n"
def nums():
    out = [0, 9999, 10000, 53701, 53687, 23469, 5, 10, 100, 99, 9, 1]
    out += [random.randint(0, 10**random.randint(1, 9)) for _ in range(150)]
    out += [random.choice([x for x in range(0, 30)]) for _ in range(30)]
    return out
N = nums()
pairs = [(a, b) for a in N[:25] for b in N[:25]] + [(random.choice(N), random.choice(N)) for _ in range(300)]
cmp = lambda a, b: (a > b) - (a < b)
exp1 = "".join("%d %d %d\n" % (a, b, cmp(a, b)) for a, b in pairs)
drv1 = r"""
static Item* mk(const char* s){ Item *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(Item)); (*t)->digit=*s-'0'; (*t)->next=NULL; t=&(*t)->next;} return h; }
int main(void){ long long P[][2]={""" + ",".join("{%d,%d}" % p for p in pairs) + r"""}; int n=sizeof(P)/sizeof(P[0]); char a[32],b[32];
 for(int i=0;i<n;i++){ sprintf(a,"%lld",P[i][0]); sprintf(b,"%lld",P[i][1]); printf("%lld %lld %d\n",P[i][0],P[i][1],NAME(mk(a),mk(b))); } return 0; }
"""
sols = blocks(q["solution"])
for i, sv in enumerate(sols):
    nm = "numListCmp" if i == 0 else "numListCmp_2"
    print("Q1 official v%d:" % (i + 1), verdict(PRE + sv + "#define NAME " + nm + "\n" + drv1, exp1))
s = q["steps"]
d1 = "#define NAME numListCmp_2\n" + drv1
print("Q1 numerics", s[0]["answer"], cmp(9999, 10000), s[1]["answer"], cmp(53701, 53687))
fb = s[2]
print("Q1 fillblank", fillblank_report(fb, PRE, d1, exp1), "correct", fb["correctId"])
od = s[3]
good = order_report(od, lambda L: PRE + "int numListCmp_2(Item* L1, Item* L2)\n{\n" + "\n".join(L) + "\n}\n" + d1, exp1)
print("Q1 order good perms", good)
fbug = s[4]
print("Q1 findbug:", verdict(PRE + "\n".join(fbug["lines"]) + "\n" + d1, exp1), "diff", bug_diff(fb, fbug), fbug["bugIndex"])

# ---------------- Q2
q = Q(C, 2)
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct { int size; int* ptr; } dyn_array;\n"
cases = [([15, 49, -8, 6, -25, 9, 10, -58, 1, 77], 5), ([1, 3, 5], 4), ([], 3), ([0], 2), ([7], 2), ([12, -12, 0, 5], 6), ([2], 2)]
for _ in range(25):
    cases.append(([random.randint(-60, 60) for _ in range(random.randint(1, 12))], random.randint(2, 9)))
def model2(A, n):
    r = ""
    for i in range(2, n + 1):
        el = [a for a in A if a % i == 0]
        r += "d%d size=%d ptrnull=%d:%s\n" % (i, len(el), 1 if not el else 0, " ".join(map(str, el)))
    return r
exp2 = ""
for ci, (A, n) in enumerate(cases):
    exp2 += "case%d\n" % ci + model2(A, n)
drv2 = "int main(void){\n"
for ci, (A, n) in enumerate(cases):
    arr = ",".join(map(str, A)) if A else "0"
    drv2 += "{ int A[]={%s}; int sz=%d; int n=%d; dyn_array* B=divNumbers(A,sz,n); printf(\"case%d\\n\"); for(int i=2;i<=n;i++){ printf(\"d%%d size=%%d ptrnull=%%d:\",i,B[i-2].size,B[i-2].ptr==NULL); for(int k=0;k<B[i-2].size;k++) printf(k?\" %%d\":\"%%d\",B[i-2].ptr[k]); printf(\"\\n\"); } }\n" % (arr, len(A), n, ci)
drv2 += "return 0; }\n"
sol = blocks(q["solution"])[0]
print("Q2 official:", verdict(PRE2 + sol + drv2, exp2))
st, o = run(PRE2 + sol + drv2)
if st == "OK":
    # show only failing lines (null-ptr)
    diffl = [(a, b) for a, b in zip(o.strip().split("\n"), exp2.strip().split("\n")) if a != b]
    print("  Q2 official diff lines (first 3):", diffl[:3])
s = q["steps"]
A0 = cases[0][0]
print("Q2 numeric", s[0]["answer"], len([a for a in A0 if a % 2 == 0]), s[1]["answer"], len([a for a in A0 if a % 5 == 0]))
fb = s[2]
print("Q2 fillblank", fillblank_report(fb, PRE2, drv2, exp2), "correct", fb["correctId"])
od = s[3]
fnhead = "dyn_array* divNumbers(int* A, int sz, int n)\n{\n int i, j, k;\n dyn_array* B = (dyn_array*)calloc(n - 1, sizeof(dyn_array));\n for (i = 2; i <= n; i++)\n {\n"
good = order_report(od, lambda L: PRE2 + fnhead + "\n".join(L) + "\n}\nreturn B;\n}\n" + drv2, exp2)
print("Q2 order good perms", good)
fbug = s[4]
print("Q2 findbug:", verdict(PRE2 + "\n".join(fbug["lines"]) + drv2, exp2), "diff", bug_diff(fb, fbug), fbug["bugIndex"])

# ---------------- Q3
q = Q(C, 3)
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
def model3(board, w):
    # distinct letters: start at the (unique) first letter then step left/right
    if w[0] not in board: return 0
    pos = board.index(w[0])
    for ch in w[1:]:
        if pos + 1 < len(board) and board[pos + 1] == ch: pos += 1
        elif pos - 1 >= 0 and board[pos - 1] == ch: pos -= 1
        else: return 0
    return 1
import string
boards = ["etybag", "a", "ab", "abc", "zyxw"] + ["".join(random.sample(string.ascii_lowercase, random.randint(1, 8))) for _ in range(40)]
tests = []
for b in boards:
    ws = set()
    for _ in range(40):
        k = random.randint(1, 6)
        pos = random.randrange(len(b)); w = b[pos]
        for _ in range(k - 1):
            c = [p for p in (pos - 1, pos + 1) if 0 <= p < len(b)]
            if random.random() < .15 or not c:
                w += random.choice(string.ascii_lowercase)
            else:
                pos = random.choice(c); w += b[pos]
        ws.add(w)
    ws |= {"byte", "baby", "bag", "gat", "yte", "e", "ge", "ab", "ba"}
    for w in ws: tests.append((b, w))
bfiles = {}
for i, b in enumerate(boards):
    (WORK / ("b%d.txt" % i)).write_bytes((b).encode())  # no trailing newline
    (WORK / ("n%d.txt" % i)).write_bytes((b + "\n").encode())  # with trailing newline
exp3 = ""
call = ""
for i, b in enumerate(boards):
    for suf in "bn":
        pass
for (b, w) in tests:
    i = boards.index(b)
    exp3 += "%s %s %d\n" % (b, w, model3(b, w))
drv3 = "int main(void){\n"
for (b, w) in tests:
    i = boards.index(b)
    drv3 += 'printf("%%s %%s %%d\\n","%s","%s",boggle("b%d.txt","%s"));\n' % (b, w, i, w)
drv3 += "return 0;}\n"
sol = blocks(q["solution"])[0]
print("Q3 tests", len(tests))
print("Q3 official (no trailing NL):", verdict(PRE3 + sol + drv3, exp3))
st, o = run(PRE3 + sol + drv3)
if st == "OK":
    dl = [(a, b) for a, b in zip(o.strip().split("\n"), exp3.strip().split("\n")) if a != b]
    print("  diffs", dl[:5], len(dl))
drv3n = drv3.replace('"b', '"n').replace("\"n%d", "\"n%d")
drv3n = re.sub(r'boggle\("b(\d+)', r'boggle("n\1', drv3)
print("Q3 official (trailing NL, rb emulating POSIX):", verdict(PRE3 + sol.replace(chr(34)+"r"+chr(34), chr(34)+"rb"+chr(34)) + drv3n, exp3))
s = q["steps"]
print("Q3 choice:", [(w, model3("etybag", w)) for w in ["byte", "baby", "gat"]], s[0]["correctId"])
print("Q3 ftell after b in etybag:", "etybag".index("b") + 1, s[1]["answer"])
fb = s[2]
print("Q3 fillblank", fillblank_report(fb, PRE3, drv3, exp3), "correct", fb["correctId"])
od = s[3]
print("Q3 order good perms", order_report(od, lambda L: PRE3 + "int boggle(char* file_name, char* word)\n{\n" + "\n".join(L) + "\n}\n" + drv3, exp3))
fbug = s[4]
print("Q3 findbug:", verdict(PRE3 + "\n".join(fbug["lines"]) + drv3, exp3), "diff", bug_diff(fb, fbug), fbug["bugIndex"])
print("Q3 yte model", model3("etybag", "yte"))
