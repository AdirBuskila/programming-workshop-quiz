import sys, pathlib, random, itertools, re, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from refute_common import *
C = "23B-A"
random.seed(3)
NL = "\n"

# ---------------- Q1
q = Q(C, 1)
PRE = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct monom { double coefficient; int power; } Monom;\ntypedef struct item { Monom mon; struct item * next; } Item;\n"
cases = [[(2, 4), (-5, 1), (3, 6), (6, 4), (-8, 0), (-3, 6), (7.5, 3)], [], [(1, 0)], [(3, 2), (-3, 2)], [(1, 5), (1, 5), (-2, 5)],
         [(0.5, 3), (0.25, 3), (1, 1)], [(2, 0), (-2, 0), (4, 3)]]
for _ in range(60):
    cases.append([(random.choice([-3, -2, -1, 1, 2, 3, 0.5, -0.5]), random.randint(0, 7)) for _ in range(random.randint(1, 10))])


def model1(L):
    d = {}
    for c, p in L:
        d[p] = d.get(p, 0) + c
    return " ".join("(%g,%d)" % (d[p], p) for p in sorted(d, reverse=True) if d[p] != 0)


exp1 = "".join(model1(L) + "\n" for L in cases)
drv1 = "int main(void){\n"
for L in cases:
    n = len(L)
    cs = ",".join("%r" % float(c) for c, p in L) or "0"
    ps = ",".join(str(p) for c, p in L) or "0"
    drv1 += ('{ double cs[]={%s}; int ps[]={%s}; int n=%d; Item* h=NULL,**t=&h; for(int i=0;i<n;i++){ *t=malloc(sizeof(Item)); (*t)->mon.coefficient=cs[i]; (*t)->mon.power=ps[i]; (*t)->next=NULL; t=&(*t)->next; } '
             'Item* P=createPolynom(h); int first=1; for(Item*p=P;p;p=p->next){ printf(first?"(%%g,%%d)":" (%%g,%%d)",p->mon.coefficient,p->mon.power); first=0;} printf("\\n"); }\n') % (cs, ps, n)
drv1 += "return 0;}\n"
sol = blocks(q["solution"])[0]
print("Q1 official:", verdict(PRE + sol + drv1, exp1))
s = q["steps"]
print("Q1 numerics", s[0]["answer"], 6, s[1]["answer"], 2 + 6)
fb = s[2]
print("Q1 fillblank", fillblank_report(fb, PRE, drv1, exp1), "correct", fb["correctId"])
od = s[3]
print("Q1 order good perms", order_report(od, lambda L: PRE + "Item* createPolynom(Item* L)\n{\n" + NL.join(L) + "\n}\n" + drv1, exp1))
fbug = s[4]
print("Q1 findbug:", verdict(PRE + NL.join(fbug["lines"]) + NL + drv1, exp1), "diff", bug_diff(fb, fbug), fbug["bugIndex"])

# ---------------- Q2
q = Q(C, 2)
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n"
mats = [[[10, 13, 56, 99], [23, 57, 59, 93], [36, 19, 74, 89], [30, 75, 80, 85], [25, 73, 84, 84]]]
for _ in range(80):
    m = random.randint(1, 5)
    n = random.randint(1, 5)
    mats.append([[random.randint(0, 4) for _ in range(n)] for _ in range(m)])
# strictly sorted rows and strictly decreasing columns patterns
mats.append([[1, 2, 3], [3, 2, 1], [0, 5, 9]])
mats.append([[5, 5], [4, 4], [3, 3]])
mats.append([[9, 1], [8, 2], [7, 3]])


def model2(M):
    m, n = len(M), len(M[0])
    rows = [i for i in range(m) if all(M[i][j] > M[i][j - 1] for j in range(1, n))]
    cols = [j for j in range(n) if all(M[i][j] < M[i - 1][j] for i in range(1, m))]
    return "rows(%d):%s cols(%d):%s" % (len(rows), " ".join(map(str, rows)), len(cols), " ".join(map(str, cols)))


exp2 = "".join(model2(M) + "\n" for M in mats)
drv2 = "int main(void){\n"
for M in mats:
    m, n = len(M), len(M[0])
    drv2 += ('{ int m=%d,n=%d,i,j; int v[]={%s}; int** ar=(int**)malloc(m*sizeof(int*)); for(i=0;i<m;i++){ ar[i]=(int*)malloc(n*sizeof(int)); for(j=0;j<n;j++) ar[i][j]=v[i*n+j]; } '
             'int *r,*c,nr,nc; sortedRowsCols(ar,m,n,&r,&nr,&c,&nc); printf("rows(%%d):",nr); for(i=0;i<nr;i++) printf(i?" %%d":"%%d",r[i]); printf(" cols(%%d):",nc); for(i=0;i<nc;i++) printf(i?" %%d":"%%d",c[i]); printf("\\n"); }\n') % (m, n, ",".join(str(x) for row in M for x in row))
drv2 += "return 0;}\n"
# NOTE: signature in the exam has int **ar_s_rows (pointer to int*), driver passes &r, which is int** -> matches only if param is int**.
sol = blocks(q["solution"])[0]
print("Q2 official:", verdict(PRE2 + sol + drv2, exp2))
st, o = run(PRE2 + sol + drv2)
print("  null/size0 check:", [l for l in o.split("\n") if l.startswith("rows(0)")][:1])
s = q["steps"]
print("Q2 numerics", s[0]["answer"], model2(mats[0]))
fb = s[2]
head = sol[:sol.index("int columnSorted")]
print("Q2 fillblank", fillblank_report(fb, PRE2 + sol[:sol.index("int columnSorted")], "\n" + sol[sol.index("void sortedRowsCols"):] + drv2, exp2), "correct", fb["correctId"])
od = s[3]
helpers = sol[:sol.index("void sortedRowsCols")]
sig = "void sortedRowsCols(int** ar, int m, int n, int** ar_s_rows, int* num_s_rows, int** ar_s_cols, int* num_s_cols)"
print("Q2 order good perms", order_report(od, lambda L: PRE2 + helpers + sig + "\n{\n" + NL.join(L) + "\n}\n" + drv2, exp2))
fbug = s[4]
colfn = sol[sol.index("int columnSorted"):]
print("Q2 findbug:", verdict(PRE2 + NL.join(fbug["lines"]) + NL + colfn + drv2, exp2))
ref = ["int arrSorted(int* a, int n)", "{", "int i;", "for (i = 1; i < n; i++)", "if (a[i] <= a[i - 1])", "return 0;", "return 1;", "}"]
print("Q2 findbug diff", [i for i, (a, b) in enumerate(zip(ref, [x.strip() for x in fbug["lines"]])) if a != b], fbug["bugIndex"])

# ---------------- Q3
q3a = Q(C, 3, "א")
q3b = Q(C, 3, "ב")
q3c = Q(C, 3, "ג")
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
nw = blocks(q3a["solution"])[0]
SEP = "? !."
ss = ["Why?! That's why.", "why", "", "a", "a b", "a  b", "ab.. cd!?", "x? ", "hello world", "a.b.c.", "It's"]
for _ in range(40):
    ss.append("a" + "".join(random.choice("ab? !.") for _ in range(random.randint(0, 12))))


def model_nw(s, seps=SEP):
    i = 0
    while i < len(s) and s[i] not in seps:
        i += 1
    w = s[:i]
    while i < len(s) and s[i] in seps:
        i += 1
    return w, (i if i < len(s) else None)


def cstr(x):
    return '"' + x.replace("\\", "\\\\").replace('"', '\\"') + '"'


exp3a = "".join("[%s] %s\n" % (model_nw(s_)[0], model_nw(s_)[1] if model_nw(s_)[1] is not None else "NULL") for s_ in ss)
drv3a = ('int main(void){ const char* S[]={%s}; int n=%d; for(int k=0;k<n;k++){ char word[64]; memset(word,\'#\',63); word[63]=0; char buf[64]; strcpy(buf,S[k]); '
         'char* r=nextWord(buf,"%s",word); if(r) printf("[%%s] %%d\\n",word,(int)(r-buf)); else printf("[%%s] NULL\\n",word);} return 0;}\n') % (",".join(cstr(x) for x in ss), len(ss), SEP)
print("Q3a official (UB word[i++]=sentence[i]):", verdict(PRE3 + nw + drv3a, exp3a))
s = q3a["steps"]
print("Q3a numeric", s[0]["answer"], model_nw("Why?! That's why.")[1])
fb = s[2]
print("Q3a fillblank", fillblank_report(fb, PRE3, drv3a, exp3a), "correct", fb["correctId"])
# also: does the fillblank's own correct program behave (word[i++]=sentence[i]) the same under -O2?
od = s[3]
print("Q3a order good perms", order_report(od, lambda L: PRE3 + "char* nextWord(char* sentence, char* separators, char* word)\n{\n" + NL.join(L) + "\n}\n" + drv3a, exp3a))
fbug = s[4]
print("Q3a findbug:", verdict(PRE3 + NL.join(fbug["lines"]) + NL + drv3a, exp3a), "diff", bug_diff(fb, fbug), fbug["bugIndex"])
# order variants (UB-free version of the loop)
ok_fixed = nw.replace("word[i++] = sentence[i];", "{ word[i] = sentence[i]; i++; }")
print("Q3a UB-free reference:", verdict(PRE3 + ok_fixed + drv3a, exp3a))
# -O2 behaviour of the UB line
import subprocess
def verdict_O2(src, expected):
    h = WORK / "o2.c"
    h.write_text(src, encoding="utf-8")
    exe = WORK / "o2.exe"
    r = subprocess.run([CL, "-w", "-O2", "-o", str(exe), str(h)], capture_output=True, text=True)
    if r.returncode: return "CE"
    o = subprocess.run([str(exe)], capture_output=True, text=True, cwd=WORK)
    return "PASS" if o.stdout.strip() == expected.strip() else "WRONG"
print("Q3a official at -O2:", verdict_O2(PRE3 + nw + drv3a, exp3a))

# 3b
sents = ["But why?! That's why.", "why", "", "   ", "a", "a b", "a.b..c!", "x? ", "Why?! ", "one two  three"] + ["a" + "".join(random.choice("ab? !.") for _ in range(random.randint(0, 14))) for _ in range(30)]


def words(s_):
    out = []
    cur = ""
    for ch in s_:
        if ch in SEP:
            if cur: out.append(cur); cur = ""
        else:
            cur += ch
    if cur: out.append(cur)
    return out


bs = blocks(q3b["solution"])[0]
exp3b = "".join("%d|%s\n" % (len(words(x)), ",".join(words(x))) for x in sents)
drv3b = ('int main(void){ const char* S[]={%s}; int n=%d; for(int k=0;k<n;k++){ char buf[128]; strcpy(buf,S[k]); int c=breakSentence(buf,"%s","bs_out.txt"); '
         'FILE*f=fopen("bs_out.txt","r"); char l[128]; int first=1; printf("%%d|",c); while(fgets(l,128,f)){ l[strcspn(l,"\\r\\n")]=0; printf(first?"%%s":",%%s",l); first=0;} fclose(f); printf("\\n"); } return 0;}\n') % (",".join(cstr(x) for x in sents), len(sents), SEP)
ok_nw = ok_fixed
print("Q3b official:", verdict(PRE3 + ok_nw + bs + drv3b, exp3b))
s = q3b["steps"]
print("Q3b numerics", s[0]["answer"], s[1]["answer"], len(words("But why?! That's why.")))
fb = s[2]
print("Q3b fillblank", fillblank_report(fb, PRE3 + ok_nw, drv3b, exp3b), "correct", fb["correctId"])
od = s[3]
print("Q3b order good perms", order_report(od, lambda L: PRE3 + ok_nw + "int breakSentence(char* sentence, char* separators, char* file_name)\n{\n" + NL.join(L) + "\n}\n" + drv3b, exp3b))
fbug = s[4]
print("Q3b findbug:", verdict(PRE3 + ok_nw + NL.join(fbug["lines"]) + NL + drv3b, exp3b), "diff", bug_diff(fb, fbug), fbug["bugIndex"])

# 3c
cs_ = blocks(q3c["solution"])[0]
queries = ["why", "a", "b", "x", "But", "That's", "zzz"]
cases3 = [(x, qq) for x in sents + ["But why?! That's why. And don't ask me why."] for qq in queries]
exp3c = "".join("%d\n" % sum(1 for w in words(x) if w == qq) for x, qq in cases3)
drv3c = ('int main(void){ const char* S[]={%s}; const char* Qs[]={%s}; int n=%d; for(int k=0;k<n;k++){ char buf[128]; strcpy(buf,S[k]); printf("%%d\\n",countWordOccur(buf,"%s",(char*)Qs[k])); } return 0;}\n') % (
    ",".join(cstr(x) for x, _ in cases3), ",".join(cstr(qq) for _, qq in cases3), len(cases3), SEP)
print("Q3c official:", verdict(PRE3 + ok_nw + cs_ + drv3c, exp3c))
s = q3c["steps"]
print("Q3c numerics", s[0]["answer"], s[1]["answer"], sum(1 for w in words("But why?! That's why. And don't ask me why.") if w == "why"))
fb = s[2]
print("Q3c fillblank", fillblank_report(fb, PRE3 + ok_nw, drv3c, exp3c), "correct", fb["correctId"])
od = s[3]
print("Q3c order good perms", order_report(od, lambda L: PRE3 + ok_nw + "int countWordOccur(char* sentence, char* separators, char* query)\n{\n" + NL.join(L) + "\n}\n" + drv3c, exp3c))
fbug = s[4]
print("Q3c findbug:", verdict(PRE3 + ok_nw + NL.join(fbug["lines"]) + NL + drv3c, exp3c), "diff", bug_diff(fb, fbug), fbug["bugIndex"])
