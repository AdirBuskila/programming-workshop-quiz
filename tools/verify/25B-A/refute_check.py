import sys, pathlib, random, itertools, re, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from refute_common import *
C = "25B-A"
random.seed(7)
out = {}

# ---------------- Q1
q = Q(C, 1)
PRE = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct node { char value; struct node* next; } node;\n"
tests = set()
for n in range(0, 8):
    for t in itertools.product(" ab", repeat=n):
        tests.add("".join(t))
for _ in range(300):
    tests.add("".join(random.choice("  ab") for _ in range(random.randint(8, 25))))
tests = sorted(tests, key=lambda s: (len(s), s))
def model1(s): return re.sub(" +", " ", s).strip(" ")
exp1 = "".join("[%s] n=%d head=%d ok=1\n" % (model1(s), len(model1(s)), 1 if model1(s) == "" else 0) for s in tests)
lits = ",".join('"%s"' % t for t in tests)
DRV1 = r"""
static node* mk(const char* s,node**all,int*na){ node *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(node)); (*t)->value=*s; (*t)->next=NULL; all[(*na)++]=*t; t=&(*t)->next;} return h; }
int main(void){
  const char* t[]={""" + lits + r"""};
  int T=sizeof(t)/sizeof(t[0]);
  for(int i=0;i<T;i++){ node* all[64]; int na=0; node* h=mk(t[i],all,&na); removeExtraSpaces(&h);
    char o[128]; int n=0, ok=1; node* p=h; while(p){ int f=0; for(int k=0;k<na;k++) if(all[k]==p) f=1; if(!f) ok=0; o[n++]=p->value; p=p->next; if(n>100){ok=0;break;} } o[n]=0;
    printf("[%s] n=%d head=%d ok=%d\n", o, n, h==NULL, ok); }
  return 0; }
"""
sol = blocks(q["solution"])[0]
print("Q1 official solution:", verdict(PRE + sol + DRV1, exp1))
# steps
s = q["steps"]
print("Q1 step0 numeric", s[0]["answer"], "model:", len(model1("  No  way! ")))
print("Q1 step1 numeric", s[1]["answer"], "model:", len(model1("  a  b  ")))
helpers = sol[:sol.index("void removeExtraSpaces")]
fb = s[2]
print("Q1 fillblank", fillblank_report(fb, PRE + helpers, DRV1, exp1), "correct", fb["correctId"])
od = s[3]
def mk_order(L): return PRE + helpers + "void removeExtraSpaces(node** head)\n{\n" + "\n".join(L) + "\n}\n" + DRV1
good = order_report(od, mk_order, exp1)
print("Q1 order passing permutations:", good)
fbug = s[4]
bugsrc = PRE + helpers + "\n".join(fbug["lines"]) + DRV1
print("Q1 findbug buggy verdict:", verdict(bugsrc, exp1))
ref = sol[sol.index("void removeExtraSpaces"):].split("\n")
diff = [i for i, (a, b) in enumerate(zip([l.rstrip() for l in ref], [l.rstrip() for l in fbug["lines"]])) if a.strip() != b.strip()]
print("Q1 findbug lines differing vs solution:", diff, "bugIndex", fbug["bugIndex"], "len", len(ref), len(fbug["lines"]))

# ---------------- Q2
q = Q(C, 2)
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n#define N 4\n"
mats = []
mats.append([[5,7,-3,13],[76,16,8,0],[98,4,43,6],[11,19,21,2]])
for _ in range(6): mats.append([[random.randint(-50, 50) for _ in range(4)] for _ in range(4)])
def drv2():
    ms = ",".join("{" + ",".join("{" + ",".join(map(str, r)) + "}" for r in m) + "}" for m in mats)
    return r"""
int main(void){ int M[][N][N]={""" + ms + r"""}; int nm=%d;
 for(int m=0;m<nm;m++) for(int n=1;n<=N;n++){ int **lo,**up; triangles(M[m],n,&lo,&up);
  printf("m%%d n%%d low:",m,n); for(int i=0;i<n;i++){for(int j=0;j<=i;j++)printf(" %%d",lo[i][j]);printf(" |");}
  printf(" up:"); for(int i=0;i<n;i++){for(int j=0;j<n-i;j++)printf(" %%d",up[i][j]);printf(" |");} printf("\n"); }
 return 0; }
""" % len(mats)
exp2 = ""
for mi, m in enumerate(mats):
    for n in range(1, 5):
        exp2 += "m%d n%d low:" % (mi, n) + "".join("".join(" %d" % m[i][j] for j in range(i + 1)) + " |" for i in range(n)) + " up:" + "".join("".join(" %d" % m[i][j] for j in range(n - i)) + " |" for i in range(n)) + "\n"
sol = blocks(q["solution"])[0]
fn = sol[sol.index("void triangles"):]
print("Q2 official solution:", verdict(PRE2 + fn + drv2(), exp2))
s = q["steps"]
print("Q2 step0 ", s[0]["answer"], "model n-i for i=1,n=4:", 4 - 1, "; step1", s[1]["answer"], "model", mats[0][3][2])
fb = s[2]
print("Q2 fillblank", fillblank_report(fb, PRE2, drv2(), exp2), "correct", fb["correctId"])
fbug = s[3]
print("Q2 findbug:", verdict(PRE2 + "\n".join(fbug["lines"]) + drv2(), exp2))
ref = fn.split("\n")
print("Q2 diff", [i for i,(a,b) in enumerate(zip(ref, fbug["lines"])) if a.strip()!=b.strip()], fbug["bugIndex"], len(ref), len(fbug["lines"]))

# ---------------- Q3
q = Q(C, 3)
words = ["live", "lives", "alive", "lived", "x", "Live", "livelive"]
def mkfile(i):
    lines = []
    for _ in range(random.randint(0, 6)):
        k = random.randint(1, 12)
        ws = [random.choice(words) for _ in range(k)]
        line = random.choice([" ", "  "]).join(ws)
        if random.random() < .15: line = line.lstrip() 
        lines.append(line[:98])
    return lines
files = {}
files["ex.txt"] = ["I believe that they live here and who does not live here","Mike lives in this house","And who does live here ? We live","10 alive creatures live in this lived place"]
for i in range(60): files["r%d.txt" % i] = mkfile(i)
# edge: exactly 99 chars + \n, word at end
l99 = ("a " * 47) + "live"; l99 = (" " * (99 - len(l99))) + l99 if len(l99) < 99 else l99
files["edge.txt"] = [l99, "live", "x live"]
files["empty.txt"] = []
for name, ls in files.items():
    (WORK / name).write_text("".join(l + "\n" for l in ls), encoding="utf-8", newline="")
def model3(ls, w): return sum(1 for l in ls for t in l.replace("\n", " ").split(" ") if t == w)
names = list(files)
exp3 = "".join("%s %d\n" % (n, model3(files[n], "live")) for n in names) + "nofile.txt -1\n"
drv3 = r"""
int main(void){ const char* n[]={""" + ",".join('"%s"' % x for x in names) + r""",NULL};
 for(int i=0;n[i];i++) printf("%s %d\n", n[i], wordAppearanceNum((char*)n[i],"live"));
 printf("nofile.txt %d\n", wordAppearanceNum("nofile.txt","live")); return 0; }
"""
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
sols = blocks(q["solution"])
print("Q3 edge line len", len(l99))
for i, sv in enumerate(sols):
    print("Q3 official v%d:" % (i + 1), verdict(PRE3 + sv + drv3, exp3))
s = q["steps"]
print("Q3 numeric", s[0]["answer"], model3(files["ex.txt"], "live"), s[1]["answer"], model3(["10 alive creatures live in this lived place"], "live"))
fb = s[2]
print("Q3 fillblank", fillblank_report(fb, PRE3, drv3, exp3), "correct", fb["correctId"])
od = s[3]
print("Q3 order good perms", order_report(od, lambda L: PRE3 + "int wordAppearanceNum(char* file_name, char* word)\n{\n" + "\n".join(L) + "\n}\n" + drv3, exp3))
fbug = s[4]
print("Q3 findbug:", verdict(PRE3 + "\n".join(fbug["lines"]) + drv3, exp3))
ref = sols[1].split("\n")
print("Q3 diff", [i for i,(a,b) in enumerate(zip(ref, fbug["lines"])) if a.strip()!=b.strip()], fbug["bugIndex"], len(ref), len(fbug["lines"]))
print("---- bug_diffs")
print("Q1", bug_diff(Q(C,1)["steps"][2], Q(C,1)["steps"][4]), Q(C,1)["steps"][4]["bugIndex"])
print("Q2", bug_diff(Q(C,2)["steps"][2], Q(C,2)["steps"][3]), Q(C,2)["steps"][3]["bugIndex"])
print("Q3", bug_diff(Q(C,3)["steps"][2], Q(C,3)["steps"][4]), Q(C,3)["steps"][4]["bugIndex"])
