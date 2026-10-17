"""Checks the shipped steps of 25B-A with clang. Run: py tools/verify/25B-A/steps_check.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from step_lib import *

C = "25B-A"
ok = True

# ---- Q1
PRE = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct node { char value; struct node* next; } node;\n"
helpers, fn = split_at(sol_blocks(C, 1, None)[0], "void removeExtraSpaces")
DRV = r"""
static node* mk(const char* s){ node *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(node)); (*t)->value=*s; (*t)->next=NULL; t=&(*t)->next;} return h; }
static int str(node* h, char* o){ int n=0; while(h){*o++=h->value;h=h->next;n++;} *o=0; return n; }
int main(void){
    const char* t[]={"  No  way! ","    ","","x","x ","  x","a b","  a  b  ","a   b   c  ","   a b   ",NULL};
    for(int i=0;t[i];i++){ node* h=mk(t[i]); char o[256]; removeExtraSpaces(&h); int n=str(h,o); printf("[%s] -> [%s] n=%d head=%d\n", t[i], o, n, h==NULL); }
    return 0; }
"""
build_full = lambda lines: PRE + helpers + "\n".join(lines) + DRV
build_body = lambda blocks: PRE + helpers + "void removeExtraSpaces(node** head)\n{\n" + "\n".join(blocks) + "\n}\n" + DRV
it = Item(C, 1, None, build_full, [fn])
print(it.ref[1])
it.fill("תנאי הלולאה"); it.bug("רווח שנמצא בסוף"); it.order("הפקודות", build=build_body)
ok &= it.finish()

# ---- Q2
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n#define N 4\n"
DRV2 = r"""
int main(void){
    int A[N][N]={{5,7,-3,13},{76,16,8,0},{98,4,43,6},{11,19,21,2}}; int **lo,**up,i,j;
    triangles(A,N,&lo,&up);
    puts("low"); for(i=0;i<N;i++){for(j=0;j<=i;j++)printf("%d ",lo[i][j]);puts("");}
    puts("up"); for(i=0;i<N;i++){for(j=0;j<N-i;j++)printf("%d ",up[i][j]);puts("");}
    return 0; }
"""
blk = sol_blocks(C, 2, None)[0]
fn2 = blk[blk.index("void triangles"):]
it = Item(C, 2, None, lambda L: PRE2 + "\n".join(L) + DRV2, [fn2])
print(it.ref[1])
it.fill("שורת ההעתקה"); it.bug("האלכסון הראשי")
ok &= it.finish()

# ---- Q3 (second version)
blk = sol_blocks(C, 3, None)[1]
pre3, fn3 = split_at(blk, "int wordAppearanceNum")
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
DRV3 = r"""
int main(void){
    FILE*f=fopen("t_ex.txt","w");
    fputs("I believe that they live here and who does not live here\nMike lives in this house\nAnd who does live here ? We live\n10 alive creatures live in this lived place\n",f); fclose(f);
    f=fopen("t_l4.txt","w"); fputs("10 alive creatures live in this lived place\n",f); fclose(f);
    printf("%d %d %d\n", wordAppearanceNum("t_ex.txt","live"), wordAppearanceNum("t_l4.txt","live"), wordAppearanceNum("nofile.txt","a"));
    return 0; }
"""
fn3 = fn3.split("\n\n")[0] if False else fn3
b3 = lambda L: PRE3 + "\n".join(L) + DRV3
it = Item(C, 3, None, b3, [fn3])
print(it.ref[1])
it.fill("ההצהרה"); it.bug("התוצאה על קובץ הדוגמה"); it.order("הפקודות של הפונקציה",
    build=lambda B: PRE3 + "int wordAppearanceNum(char* file_name, char* word)\n{\n" + "\n".join(B) + "\n}\n" + DRV3)
ok &= it.finish()

# ---- Q4 / Q6: expected values from running the programs
V = pathlib.Path(__file__).parent
r4 = run((V / "q4.c").read_text())
assert r4 == (0, "3 5\n5 5\n4 4\n19 19\n18 18\n"), r4
print("Q4 output:", repr(r4[1]))
r6 = run(r"""#include <stdio.h>
int main(){ FILE*w=fopen("file.dat","w"); fputs("abc",w); fclose(w); char c; FILE* f=fopen("file.dat","r");
 while (c = fgetc(f) != EOF) printf("%d", c); puts(""); return 0; }""")
assert r6 == (0, "111\n"), r6
r6b = run(r"""#include <stdio.h>
int main(){ FILE*w=fopen("file.dat","w"); fputs("abc",w); fclose(w); char c; int n=0; FILE* f=fopen("file.dat","r");
 while ((c = fgetc(f) != EOF)) { n++; if(n==1) printf("first c=%d\n", c);} printf("iterations=%d\n", n); return 0; }""")
assert r6b == (0, "first c=1\niterations=3\n"), r6b
print("Q6 output:", repr(r6[1]), r6b[1].split())

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
