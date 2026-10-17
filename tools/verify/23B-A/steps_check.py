"""Checks the shipped steps of 23B-A with clang. Run: py tools/verify/23B-A/steps_check.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from step_lib import *

C = "23B-A"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"

# ---- Q1 createPolynom
PRE = INC + "typedef struct monom { double coefficient; int power; } Monom;\ntypedef struct item { Monom mon; struct item * next; } Item;\n"
_, fn = split_at(sol_blocks(C, 1, None)[0], "Item* createPolynom")
DRV = r"""
static Item* mk(int n, double* c, int* p){ Item *h=NULL,**t=&h; for(int i=0;i<n;i++){ *t=malloc(sizeof(Item)); (*t)->mon.coefficient=c[i]; (*t)->mon.power=p[i]; (*t)->next=NULL; t=&(*t)->next;} return h; }
static void pr(Item* P){ for(;P;P=P->next) printf("(%g,%d) ", P->mon.coefficient, P->mon.power); puts(""); }
int main(void){
    double c[]={2,-5,3,6,-8,-3,7.5}; int p[]={4,1,6,4,0,6,3};
    pr(createPolynom(mk(7,c,p)));
    double c2[]={1,-1}; int p2[]={2,2}; pr(createPolynom(mk(2,c2,p2)));
    pr(createPolynom(NULL));
    double c3[]={4}; int p3[]={0}; pr(createPolynom(mk(1,c3,p3)));
    return 0; }
"""
it = Item(C, 1, None, lambda L: PRE + "\n".join(L) + DRV, [fn])
print(it.ref[1])
it.fill("שורת הסכימה"); it.bug("מקדם שלילי")
it.order("הפקודות של", build=lambda B: PRE + "Item* createPolynom(Item* L)\n{\n" + "\n".join(B) + "\n}\n" + DRV)
ok &= it.finish()

# ---- Q2 sortedRowsCols (three functions; each step replaces one of them)
blk = sol_blocks(C, 2, None)[0]
pa, rest = split_at(blk, "int columnSorted")
pc, ps = split_at(rest, "void sortedRowsCols")
PA, PC, PS = "int arrSorted" + pa.split("int arrSorted", 1)[1], pc, ps
DRV2 = r"""
static int** mkm(int m,int n,int* d){ int** a=malloc(m*sizeof(int*)); for(int i=0;i<m;i++){a[i]=malloc(n*sizeof(int)); for(int j=0;j<n;j++)a[i][j]=d[i*n+j];} return a;}
static void t(int m,int n,int* d){ int **ar=mkm(m,n,d); int *rr=(int*)7,*cc=(int*)7,nr=-1,nc=-1; sortedRowsCols(ar,m,n,&rr,&nr,&cc,&nc);
  printf("rows n=%d %s:",nr,rr?"set":"NULL"); for(int i=0;i<nr;i++)printf(" %d",rr[i]); printf(" | cols n=%d %s:",nc,cc?"set":"NULL"); for(int i=0;i<nc;i++)printf(" %d",cc[i]); puts(""); }
int main(void){
    int d1[]={10,13,56,99, 23,57,59,93, 36,19,74,89, 30,75,80,85, 25,73,84,84}; t(5,4,d1);
    int d2[]={1,1,5, 2,3,5, 3,3,4}; t(3,3,d2);
    int d3[]={9,1, 8,2, 7,3}; t(3,2,d3);
    return 0; }
"""
whole = lambda a, c, s: INC + a + "\n" + c + "\n" + s + "\n" + DRV2
it = Item(C, 2, None, lambda L: INC + PA + "\n" + PC + "\n" + "\n".join(L) + "\n" + DRV2, [PS])
print(it.ref[1])
# order step replaces sortedRowsCols' body
it.order("הפקודות של", build=lambda B: whole(PA, PC, "void sortedRowsCols(int** ar, int m, int n, int** ar_s_rows, int* num_s_rows, int** ar_s_cols, int* num_s_cols)\n{\n" + "\n".join(B) + "\n}\n"))
s = find(C, 2, None, "fillblank", "columnSorted")
for o in s["options"]:
    L = list(s["lines"]); L[s["blankIndex"]] = L[s["blankIndex"]].replace("___", o["value"])
    r = run(whole(PA, "\n".join(L), PS)); good = o["id"] == s["correctId"]
    print("Q2 fill", o["id"], "*" if good else " ", "==ref" if r == it.ref else "DIFFERS " + repr(r[1])[:90]); ok &= (r == it.ref) == good
s = find(C, 2, None, "findbug", "arrSorted")
r = run(whole("\n".join(s["lines"]), PC, PS)); print("Q2 bug:", r[0], repr(r[1])[:110]); ok &= r != it.ref
ok &= it.finish()

# ---- Q3 a/b/c
SA = sol_blocks(C, 3, "א")[0]
SB = sol_blocks(C, 3, "ב")[0]
SC = sol_blocks(C, 3, "ג")[0]
_, fa = split_at(SA, "char* nextWord")
DRVA = r"""
int main(void){
    char sep[]="? !.", s1[]="Why?! That's why.", s2[]="why", s3[]="But why?! That's why.", w[64]; char* r; int k;
    memset(w,'X',63); w[63]=0; r=nextWord(s1,sep,w); printf("word=[%s] rest=[%s] off=%d\n",w,r?r:"NULL",r?(int)(r-s1):-1);
    memset(w,'X',63); w[63]=0; r=nextWord(s2,sep,w); printf("word=[%s] rest=%s\n",w,r?"set":"NULL");
    char* q=s3; for(k=0;k<8&&q;k++){ memset(w,'X',63); w[63]=0; q=nextWord(q,sep,w); printf("<%s>",w);} puts("");
    return 0; }
"""
it = Item(C, 3, "א", lambda L: INC + "\n".join(L) + DRVA, [fa])
print(it.ref[1])
it.fill("הלולאה שמעתיקה"); it.bug("אף פעם לא מחזירה")
it.order("הפקודות של", build=lambda B: INC + "char* nextWord(char* sentence, char* separators, char* word)\n{\n" + "\n".join(B) + "\n}\n" + DRVA)
ok &= it.finish()

_, fb = split_at(SB, "int breakSentence")
NW = fa + "\n"
DRVB = r"""
static void dump(const char* f){ FILE*g=fopen(f,"r"); char b[100]; printf("{"); while(fgets(b,100,g)){ for(char*p=b;*p;p++) printf(*p=='\n'?"|":"%c",*p);} printf("}"); fclose(g); }
int main(void){
    char sep[]="? !.", a[]="But why?! That's why.", b[]="", c[]="why", d[]="a!!b?"; 
    printf("%d ", breakSentence(a,sep,"t_out.txt")); dump("t_out.txt"); puts("");
    printf("%d ", breakSentence(b,sep,"t_out.txt")); dump("t_out.txt");
    printf(" %d ", breakSentence(c,sep,"t_out.txt")); dump("t_out.txt");
    printf(" %d ", breakSentence(d,sep,"t_out.txt")); dump("t_out.txt"); puts("");
    return 0; }
"""
it = Item(C, 3, "ב", lambda L: INC + NW + "\n".join(L) + DRVB, [fb])
print(it.ref[1])
it.fill("המילה האחרונה"); it.bug("נדבקות")
it.order("הפקודות של", build=lambda B: INC + NW + "int breakSentence(char* sentence, char* separators, char* file_name)\n{\n" + "\n".join(B) + "\n}\n" + DRVB)
ok &= it.finish()
r = run(INC + NW + fb.replace("if (*word)", 'printf("inloop=%d ", count); if (*word)') + r"""
int main(void){ char sep[]="? !.", a[]="But why?! That's why."; int n=breakSentence(a,sep,"t_o.txt"); printf("total=%d\n", n); return 0; }""")
assert r == (0, "inloop=3 total=4\n"), r
print("Q3b loop count:", r)

_, fc = split_at(SC, "int countWordOccur")
DRVC = r"""
int main(void){
    char sep[]="? !.", s3[]="But why?! That's why. And don't ask me why.", s4[]="why", s5[]="", s6[]="whyx why-why";
    printf("%d %d %d %d\n", countWordOccur(s3,sep,"why"), countWordOccur(s4,sep,"why"), countWordOccur(s5,sep,"why"), countWordOccur(s6,sep,"why")); return 0; }
"""
it = Item(C, 3, "ג", lambda L: INC + NW + "\n".join(L) + DRVC, [fc])
print(it.ref[1])
it.fill("תנאי ההשוואה"); it.bug("2 במקום 3")
it.order("הפקודות של", build=lambda B: INC + NW + "int countWordOccur(char* sentence, char* separators, char* query)\n{\n" + "\n".join(B) + "\n}\n" + DRVC)
ok &= it.finish()
r = run(INC + NW + fc.replace("if (strcmp(word, query) == 0)\n                     count++;\n       if", "if (strcmp(word, query) == 0)\n                     count++;\n       printf(\"inloop=%d \", count);\n       if") + DRVC)
print("Q3c in-loop:", r[1][:40])

# ---- Q4 / Q6
V = pathlib.Path(__file__).parent
r4 = run((V / "q4.c").read_text())
assert r4 == (0, "x=20,y=5\nx=30,y=10\nx=15,y=10\n"), r4
print("Q4 output:", repr(r4[1]))
r6 = run(INC + r"""int main(){ printf("%d %d %d\n", (int)strlen("strlen"), (int)sizeof"sizeof", (int)(-(int)strlen("strlen")+(int)sizeof"sizeof")); puts("puts"-strlen("strlen")+sizeof"sizeof"); return 0; }""")
assert r6 == (0, "6 7 1\nuts\n"), r6
print("Q6:", repr(r6[1]))

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
