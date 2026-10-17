"""Checks the shipped steps of 24B-A with clang. Run: py tools/verify/24B-A/steps_check.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from step_lib import *

C = "24B-A"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"

# ---- Q1 (numListCmp_2)
PRE = INC + "typedef struct item { int digit; struct item* next; } Item;\n"
_, fn = split_at(sol_blocks(C, 1, None)[1], "int numListCmp_2")
DRV = r"""
static Item* mk(const char* s){ Item *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(Item)); (*t)->digit=*s-'0'; (*t)->next=NULL; t=&(*t)->next;} return h; }
int main(void){
    const char* ex[][2]={{"9999","10000"},{"53701","53687"},{"23469","23469"},{"5","7"},{"12345","12346"},{"0","0"},{"100","99"}};
    for(int i=0;i<7;i++) printf("%d ", numListCmp_2(mk(ex[i][0]),mk(ex[i][1]))); puts("");
    return 0; }
"""
it = Item(C, 1, None, lambda L: PRE + "\n".join(L) + DRV, [fn])
print("Q1 ref:", it.ref)
assert it.ref[1].split()[:3] == ["-1", "1", "0"]
it.fill("התנאי שמחזיר"); it.bug("מחזירה `-1` כבר")
it.order("הפקודות של", build=lambda B: PRE + "int numListCmp_2(Item* L1, Item* L2)\n{\n" + "\n".join(B) + "\n}\n" + DRV)
ok &= it.finish()

# ---- Q2 (divNumbers)
PRE2 = INC + "typedef struct { int size; int * ptr; } dyn_array;\n"
_, fn2 = split_at(sol_blocks(C, 2, None)[0], "dyn_array* divNumbers")
DRV2 = r"""
int main(void){
    int A[]={15, 49, -8, 6, -25, 9, 10, -58, 1, 77}; dyn_array* B=divNumbers(A,10,5);
    for(int i=0;i<4;i++){ printf("B[%d] size=%d ptr=%s:", i, B[i].size, B[i].ptr?"set":"NULL"); for(int j=0;j<B[i].size;j++) printf(" %d", B[i].ptr[j]); puts(""); }
    int Z[]={1,3}; dyn_array* E=divNumbers(Z,2,2); printf("E size=%d ptr=%s\n", E[0].size, E[0].ptr?"set":"NULL");
    return 0; }
"""
it = Item(C, 2, None, lambda L: PRE2 + "\n".join(L) + DRV2, [fn2])
print(it.ref[1])
it.fill("הבדיקה"); it.bug("חסר האיבר הראשון")
it.order("שלוש הפקודות", build=lambda B: PRE2 + "dyn_array* divNumbers(int* A, int sz, int n)\n{\n int i, j, k;\n dyn_array* B = (dyn_array*)calloc(n - 1, sizeof(dyn_array));\n for (i = 2; i <= n; i++)\n {\n" + "\n".join(B) + "\n }\n return B;\n}\n" + DRV2)
ok &= it.finish()

# ---- Q3 (boggle)
_, fn3 = split_at(sol_blocks(C, 3, None)[0], "int boggle")
DRV3 = r"""
static int t(const char* board, const char* w){ FILE*f=fopen("t_board.txt","w"); fputs(board,f); fclose(f); return boggle("t_board.txt",w); }
int main(void){
    printf("bag=%d byte=%d baby=%d gat=%d yte=%d eb=%d e=%d tyb=%d\n", t("etybag","bag"),t("etybag","byte"),t("etybag","baby"),t("etybag","gat"),t("etybag","yte"),t("etybag","eb"),t("etybag","e"),t("etybag","tyb"));
    return 0; }
"""
it = Item(C, 3, None, lambda L: INC + "\n".join(L) + DRV3, [fn3])
print(it.ref[1])
it.fill("החזרה אחורה"); it.bug("yte")
it.order("הפקודות של", build=lambda B: INC + "int boggle(char* file_name, char* word)\n{\n" + "\n".join(B) + "\n}\n" + DRV3)
ok &= it.finish()
r = run(INC + r"""int main(void){ FILE*w=fopen("t_b.txt","w"); fputs("etybag",w); fclose(w); char c; FILE*f=fopen("t_b.txt","r");
 while ((c = fgetc(f)) != EOF) if (c == 'b') break; printf("ftell=%ld\n", ftell(f)); return 0; }""")
assert r == (0, "ftell=4\n"), r
print("Q3 ftell:", r[1].strip())

# ---- Q4 / Q6 values by running the programs
V = pathlib.Path(__file__).parent
r4 = run((V / "q4.c").read_text())
assert r4 == (0, "200 400\n300 300\n400 200\n600\n"), r4
print("Q4 output:", repr(r4[1]))
r4b = run(INC + r"""int blabla(int* p1, int* p2) { int y = 300, x = 1; *p2 = 400; x = x + 300; return (*p1 + 200); }
void swap(int* a, int b) { int temp; temp = *a; *a = b; b = temp; }
int main(){ int x=200,y=100; y = blabla(&x,&y); printf("y=%d ", y); x=y; y=300; swap(&x,y); printf("x=%d ", x); x=500; printf("last=%d\n", blabla(&x,&x)); return 0; }""")
assert r4b == (0, "y=400 x=300 last=600\n"), r4b
r6 = run(INC + r"""int main(){ FILE*w=fopen("file.dat","w"); fputs("1234",w); fclose(w); char st[2]; int n=0; FILE* fptr=fopen("file.dat","r");
 while (fgets(st, 2, fptr)) { n++; fputs(fgets(st, 2, fptr),stdout);} printf("\niter=%d len=%d\n", n, (int)strlen(st)); return 0; }""")
assert r6 == (0, "24\niter=2 len=1\n"), r6
print("Q6:", repr(r6[1]))

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
