"""Machine checks for the 20B-B steps (Q1, Q2, Q3, Q5). Run: PYTHONUTF8=1 py tools/verify/20B-B/steps_check.py
Reads the SHIPPED tools/raw/20B-B.json; every numeric/choice value is re-measured with clang (sympy for the algebra)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

CODE = "20B-B"
ok = True


def correct_lines(step):
    ln = list(step["lines"])
    ln[step["blankIndex"]] = ln[step["blankIndex"]].replace("___", [o for o in step["options"] if o["id"] == step["correctId"]][0]["value"])
    return ln


# ---------------- Q1
PRE1 = "#include <stdio.h>\n#include <ctype.h>\n"
MAIN1 = r'''
int main(void){
 const char*t[]={"B4$Ca#%ds5P8P&9zY","B4$Ca#%ds5P8P&9rY","a1Ab2B","Ba1","c9Ab0B","A1a2B","","zA9yB","aAaA","P8P"};
 for(int i=0;i<10;i++)printf("%d ",group_sort((char*)t[i]));printf("\n");
 char s[40];const char*w=t[1];int first=-1;
 for(int k=1;k<=17;k++){int j;for(j=0;j<k;j++)s[j]=w[j];s[j]=0;if(!group_sort(s)&&first<0)first=k-1;}
 printf("first=%d\n",first);return 0;}
'''
fb = S.find(CODE, 1, None, "fillblank", "השלימו")
it = S.Item(CODE, 1, None, lambda L: PRE1 + "\n".join(L) + MAIN1, correct_lines(fb))
print(it.ref)
assert it.ref[1] == "1 0 1 1 0 1 1 0 1 1 \nfirst=15\n", it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()

# ---------------- Q2
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct item { int data; struct item *next; } Item;\n"
MAIN2 = r'''
static Item* mk(int*v,int n){Item*h=NULL;for(int i=n-1;i>=0;i--){Item*e=malloc(sizeof(Item));e->data=v[i];e->next=h;h=e;}return h;}
static void pl(Item*l){for(;l;l=l->next)printf("%d ",l->data);printf("| ");}
int main(void){int a0[]={1,2,3},a1[]={1,2},a2[]={4,1,2},a3[]={1,2,3,4},L[]={1,2,3},L2[]={1,2,4},L3[]={7};
 Item*A[5]={mk(a0,3),mk(a1,2),mk(a2,3),mk(a3,4),NULL};
 Item*l=mk(L,3);Item*r=arr_of_lists_to_list_of_prefixes(A,5,l);pl(r);
 r=arr_of_lists_to_list_of_prefixes(A,5,mk(L2,3));pl(r);
 r=arr_of_lists_to_list_of_prefixes(A,5,NULL);pl(r);
 r=arr_of_lists_to_list_of_prefixes(A,5,mk(L3,1));printf("%s|",r?"nonnull":"NULL");
 printf(" isp=%d %d %d\n",is_prefix(l,A[1]),is_prefix(l,A[0]),is_prefix(l,A[3]));return 0;}
'''
fb = S.find(CODE, 2, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, ref)
print(it.ref)
assert it.ref[1].startswith("0 3 | | 0 1 2 3 4 | NULL| isp=0 1 1"), it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
orders = S.find(CODE, 2, None, "order", "סדרו")["lines"]
i0 = ref.index("int is_prefix(Item *L1, Item *L2)")
i1 = [i for i, l in enumerate(ref) if l.strip() == "return 1;"][0] + 1
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(ref[:i0] + L + ref[i1 + 1:]) + MAIN2, orders)
assert it.ref == S.run(PRE2 + "\n".join(ref) + MAIN2)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q3
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN3 = r'''
int main(void){FILE*f=fopen("m.txt","w");fputs("0 4 2 7 4\n1 3 0\n2 9 0 1 1 6 3\n3\n",f);fclose(f);
 int A[5][COLS];for(int i=0;i<5;i++)for(int j=0;j<COLS;j++)A[i][j]=99;
 file_to_sparse_matrix("m.txt",A,4,5);int nz=0;
 for(int i=0;i<4;i++){for(int j=0;j<5;j++){printf("%d ",A[i][j]);nz+=A[i][j]!=0;}printf("\n");}
 printf("nz=%d A23=%d\n",nz,A[2][3]);return 0;}
'''
fb = S.find(CODE, 3, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, ref)
print(it.ref)
assert it.ref[1] == "0 0 4 0 7 \n3 0 0 0 0 \n9 1 0 6 0 \n0 0 0 0 0 \nnz=6 A23=6\n", it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
orders = S.find(CODE, 3, None, "order", "סדרו")["lines"]
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, orders)
assert it.ref == S.run(PRE3 + "\n".join(ref) + MAIN3)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q5
r = S.run(r'''#include <stdio.h>
#include <string.h>
#include <math.h>
int main(){int n=strlen("\\\\"),m=strlen("\n\n\0\n"),k=strlen("////");
 printf("%d %d %d\n",n,m,k);
 /* emulate a 32-bit address: s = some value that fits in int; the same arithmetic as the exam */
 long long s=4210688; long long x=s+m;
 long long res=(long long)(pow((int)x,n)-k)/(int)(x+m);
 printf("%d\n", res==s);return 0;}''')
print(r)
assert r[1].splitlines() == ["2 2 4", "1"], r
import sympy
x = sympy.symbols("x")
assert sympy.simplify((x**2 - 4) / (x + 2) - (x - 2)) == 0
print("sympy ok")
# the program itself, compiled for 32-bit if the toolchain allows it
p = S.run(r'''#include <stdio.h>
#include <string.h>
#include <math.h>
int main(){int n=strlen("\\\\"), m=strlen("\n\n\0\n"), k=strlen("////");
 char *s = "Ah!", *x = s + m;
 puts( (char *)( (long long)(pow((int)x, n) - k) / (int)(x + m) ) ); return 0;}''')
print("native (64-bit expected to fail):", p[0])
print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
