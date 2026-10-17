"""Step-author checks for 22B-B (run after gen_22B-B.py): PYTHONUTF8=1 py tools/verify/22B-B/steps_check.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ws_util import *  # noqa

C = "22B-B"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n"


def fill_ref(num, part, hint):
    s = find(C, num, part, "fillblank", hint)
    lines = list(s["lines"])
    right = next(o["value"] for o in s["options"] if o["id"] == s["correctId"])
    lines[s["blankIndex"]] = lines[s["blankIndex"]].replace("___", right)
    return lines


def check_bug(it, num, part, ref, hint):
    s = find(C, num, part, "findbug", hint)
    one_line_diff(ref, s["lines"], s["bugIndex"])
    return it.bug(hint)


# ------------------------------------------------------------------ Q1
MAIN1 = """int main(void){
 const char *S[]={"t&u5Y%as3k$R","t&u5Y%4as3k$R","t&u5Y%&as3k$R","aBc","abCDef","xyz5WQ","a","","ab1CD"};
 for(int t=0;t<9;t++){ int a=-9,b=-9; int r=nums_in_halves((char*)S[t],&a,&b); printf("%-16s %d %d %d\\n",S[t],a,b,r); } return 0; }
"""
b1 = lambda lines: INC + "\n".join(lines) + "\n" + MAIN1
ref1 = fill_ref(1, None, "המחצית השנייה")
it = Item(C, 1, None, b1, ref1)
print(it.ref[1])
assert "t&u5Y%as3k$R     2 1 0" in it.ref[1] and "t&u5Y%4as3k$R    2 1 1" in it.ref[1] and "t&u5Y%&as3k$R    2 1 -1" in it.ref[1]
it.fill("המחצית השנייה")
r = check_bug(it, 1, None, ref1, "שורה אחת שונתה")
print("   bug output:", r[1].split("\n")[0])
assert r[1].split("\n")[0].split()[1:] == ["3", "1", "0"]
ok &= it.finish()
HDR1 = "int nums_in_halves(char* str, int* num1, int* num2)"
b1o = lambda body: INC + HDR1 + "\n{\n" + "\n".join(body) + "\n}\n" + MAIN1
s = find(C, 1, None, "order", "גוף הפונקציה")
it = Item(C, 1, None, b1o, s["lines"])
it.order("גוף הפונקציה")
ok &= it.finish()
ok &= numeric(C, 1, None, "מתחילה המחצית השנייה", INC + """int main(void){ const char*s="t&u5Y%4as3k$R"; printf("%d %d\\n",(int)strlen(s),(int)((strlen(s)+1)/2)); return 0; }""")
out = probe(INC + "\n".join(ref1) + """
int main(void){ int a,b; printf("%d\\n", nums_in_halves("t&u5Y%&as3k$R",&a,&b)); return 0; }""")
s = find(C, 1, None, "choice", "מה מחזירה")
right = next(o["value"] for o in s["options"] if o["id"] == s["correctId"]).strip("`")
print("Q1 choice: real return", out.strip(), "shipped", right)
ok &= out.strip() == right

# ------------------------------------------------------------------ Q2
TYPE2 = "typedef struct { int i, j; } pair;\n"
MAIN2 = """int main(void){
 int E[8][8]={{0,1,0,0,0,1,0,0},{1,0,1,0,0,0,1,0},{0,1,0,0,1,0,0,1},{0,0,0,0,0,1,0,1},{0,0,1,0,0,1,0,0},{1,0,0,1,1,0,1,0},{0,1,0,0,0,1,0,1},{0,0,1,1,0,0,1,0}};
 int T[3][3]={{0,1,1},{1,0,1},{1,1,0}};
 int **M=malloc(8*sizeof(int*)); for(int i=0;i<8;i++){ M[i]=malloc(8*sizeof(int)); for(int j=0;j<8;j++)M[i][j]=E[i][j]; }
 int n; pair *p=indirect_friends(M,8,&n); printf("n=%d\\n",n); for(int i=0;i<n;i++)printf("%d,%d\\n",p[i].i,p[i].j);
 int **K=malloc(3*sizeof(int*)); for(int i=0;i<3;i++){ K[i]=malloc(3*sizeof(int)); for(int j=0;j<3;j++)K[i][j]=T[i][j]; }
 p=indirect_friends(K,3,&n); printf("triangle: n=%d ptr=%s\\n",n,p?"non-NULL":"NULL");
 return 0; }
"""
b2 = lambda lines: INC + TYPE2 + "\n".join(lines) + "\n" + MAIN2
ref2 = fill_ref(2, None, "החבר המשותף")
it = Item(C, 2, None, b2, ref2)
print(it.ref[1])
it.fill("החבר המשותף")
r = check_bug(it, 2, None, ref2, "שורה אחת שונתה")
print("   bug output:", repr(r[1][:60]))
ok &= it.finish()
# independent brute force over the example matrix
E = [[0,1,0,0,0,1,0,0],[1,0,1,0,0,0,1,0],[0,1,0,0,1,0,0,1],[0,0,0,0,0,1,0,1],[0,0,1,0,0,1,0,0],[1,0,0,1,1,0,1,0],[0,1,0,0,0,1,0,1],[0,0,1,1,0,0,1,0]]
brute = [(i, j) for i in range(8) for j in range(i) if E[i][j] == 0 and any(E[i][k] and E[k][j] for k in range(8))]
print("brute-force indirect pairs:", len(brute), brute)
real_n = int(it.ref[1].split("\n")[0].split("=")[1])
ok &= real_n == len(brute)
ok &= numeric(C, 2, None, "מטריצת הדוגמה", INC + TYPE2 + "\n".join(ref2) + MAIN2.replace('printf("n=%d\\n",n); for', 'printf("%d\\n",n); return 0; for'))
ok &= numeric(C, 2, None, "החסם העליון", INC + """int main(void){ int size=8; printf("%d\\n",(size*size-size)/2); return 0; }""")

# ------------------------------------------------------------------ Q3
TYPE3 = """typedef struct { char model[20]; int price; int year; } car;
typedef struct item { int price; int year; struct item* next; } Item;
"""
MAIN3 = """static void show(Item*l){ int c=0; for(;l&&c<20;l=l->next,c++)printf("[%d|%d] ",l->price,l->year); printf("(%d)\\n",c); }
int main(void){
 car all[5]={{"Subaru",90000,2019},{"Mazda",95000,2020},{"Subaru",10000,2009},{"Toyota",200000,2022},{"Subaru",25000,2012}};
 FILE *f=fopen("cars.bin","wb"); fwrite(all,sizeof(car),5,f); fclose(f);
 show(appropriateCar("cars.bin","Subaru",100000,2010));
 show(appropriateCar("cars.bin","Subaru",100000,2005));
 show(appropriateCar("cars.bin","Subaru",25000,2012));
 show(appropriateCar("cars.bin","Lada",100000,2005));
 show(appropriateCar("missing.bin","Subaru",100000,2005));
 return 0; }
"""
b3 = lambda lines: INC + TYPE3 + "\n".join(lines) + "\n" + MAIN3
ref3 = fill_ref(3, None, "אחרי יצירת האיבר")
it = Item(C, 3, None, b3, ref3)
print(it.ref[1])
assert it.ref[1].startswith("[90000|2019] [25000|2012] (2)\n[90000|2019] [10000|2009] [25000|2012] (3)\n[25000|2012] (1)\n(0)\n(0)")
it.fill("אחרי יצירת האיבר")
r = check_bug(it, 3, None, ref3, "שורה אחת שונתה")
print("   bug output:", repr(r[1][:140]))
ok &= it.finish()
base3 = INC + TYPE3 + "\n".join(ref3) + "\n"
f3 = """car all[5]={{"Subaru",90000,2019},{"Mazda",95000,2020},{"Subaru",10000,2009},{"Toyota",200000,2022},{"Subaru",25000,2012}};
 FILE *f=fopen("cars.bin","wb"); fwrite(all,sizeof(car),5,f); fclose(f);"""
ok &= numeric(C, 3, None, "כמה איברים", base3 + "int main(void){ " + f3 + """ Item*l=appropriateCar("cars.bin","Subaru",100000,2005); int c=0; for(;l;l=l->next)c++; printf("%d\\n",c); return 0; }""")
ok &= numeric(C, 3, None, "איבר השני", base3 + "int main(void){ " + f3 + """ Item*l=appropriateCar("cars.bin","Subaru",100000,2005); printf("%d\\n",l->next->price); return 0; }""")

# ------------------------------------------------------------------ Q5
PRE5 = INC + "int main(void){ "
full = "printf(\"%d\",strcmp(\"&\",\"&&\")&strcmp(\"&\",\"&&\")|(\"strcmp(&,&&)\"&&\"strcmp(&,&&)\"));"
out = probe(PRE5 + "printf(\"%d %d\", strcmp(\"&\",\"&&\"), strcmp(\"&\",\"&&\")<0); return 0; }")
print("Q5 strcmp:", out)
ok &= out.split()[0] == "-1"
ok &= numeric(C, 5, None, "strcmp(&,&&)", PRE5 + "printf(\"%d\\n\",(\"strcmp(&,&&)\"&&\"strcmp(&,&&)\")); return 0; }")
ok &= numeric(C, 5, None, "מדפיסה התוכנית", PRE5 + full + " return 0; }")

print("ALL OK" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
