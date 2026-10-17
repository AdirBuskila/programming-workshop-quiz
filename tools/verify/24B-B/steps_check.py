"""Checks the shipped steps of 24B-B with clang. Run: py tools/verify/24B-B/steps_check.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from step_lib import *

C = "24B-B"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n"

# ---- Q1
PRE = INC + "typedef struct item { int number; struct item* next; } Item;\n"
blk = sol_blocks(C, 1, None)[0]
dig, rest = split_at(blk, "void headInsert")
dig = "int " + dig                       # the official text omits the return type
hi, ns = split_at(rest, "Item** numSeparation")
DRV = r"""
int main(void){ int A[]={23,4,-78,34578,79,-185,0,998,9,36}, n, i; Item** L=numSeparation(A,10,&n);
  printf("size=%d\n",n); for(i=0;i<n;i++){ printf("L[%d]:",i); for(Item*p=L[i];p;p=p->next)printf(" %d",p->number); puts(""); }
  printf("d=%d %d %d\n", digitsNumber(-185), digitsNumber(0), digitsNumber(10)); return 0; }
"""
it = Item(C, 1, None, lambda L: PRE + dig + hi + "\n".join(L) + DRV, [ns])
print(it.ref[1])
it.fill("שורת ההכנסה")
it.order("הפקודות של", build=lambda B: PRE + dig + hi + "Item** numSeparation(int* A, int sz, int* p_size)\n{\n" + "\n".join(B) + "\n}\n" + DRV)
# findbug is in digitsNumber: build with the shipped lines in place of the helper
bld = lambda L: PRE + "\n".join(L) + "\n" + hi + ns + DRV
r = run(bld(find(C, 1, None, "findbug", "digitsNumber")["lines"]))
print("Q1 bug:", r[0], repr(r[1])[:150]); assert r != it.ref
ok &= it.finish()

# ---- Q2
PRE2 = INC
blk = sol_blocks(C, 2, None)[0]
fm, fn2 = split_at(blk, "int** matrixToFrame")
DRV2 = r"""
int main(void){
    int r=3,c=4,i,j,z=0; int** M=(int**)malloc(r*sizeof(int*)); for(i=0;i<r;i++){ M[i]=(int*)malloc(c*sizeof(int)); for(j=0;j<c;j++) M[i][j]=i*c+j+1; }
    int** F=matrixToFrame(M,r,c);
    for(i=0;i<r+2;i++){ for(j=0;j<c+2;j++){ printf("%d ",F[i][j]); if(F[i][j]==0) z++; } puts(""); }
    printf("zeros=%d F[2][3]=%d\n", z, F[2][3]); return 0; }
"""
it = Item(C, 2, None, lambda L: PRE2 + fm + "\n".join(L) + DRV2, [fn2])
print(it.ref[1])
it.fill("שורת ההעתקה")
it.bug("העמודה האחרונה")
it.order("הפקודות של", build=lambda B: PRE2 + fm + "int** matrixToFrame(int** M, int rows, int cols)\n{\n" + "\n".join(B) + "\n}\n" + DRV2)
ok &= it.finish()

# ---- Q3
blk = sol_blocks(C, 3, None)[0]
rev, rest = split_at(blk, "int hasUniqueLetters")
has, pf = split_at(rest, "void processFiles")
DRV3 = r"""
int main(void){
    FILE*f=fopen("t_in.txt","w"); fputs("abc#xyz\ntable\nAlisa\nWalla\nMichael\n",f); fclose(f);
    processFiles("t_in.txt","t_out.txt"); f=fopen("t_out.txt","r"); char s[200]; int n=0; while(fgets(s,200,f)){ n++; fputs(s,stdout);} printf("lines=%d\n", n);
    printf("unique: "); const char* w[]={"abc#xyz","table","Alisa","Walla","Michael"}; for(int i=0;i<5;i++) printf("%s=%d ", w[i], hasUniqueLetters(w[i])); puts("");
    return 0; }
"""
it = Item(C, 3, None, lambda L: INC + rev + has + "\n".join(L) + DRV3, [pf])
print(it.ref[1])
it.order("הפקודות של", build=lambda B: INC + rev + has + "void processFiles(const char* inputFilename, const char* outputFilename)\n{\n" + "\n".join(B) + "\n}\n" + DRV3)
# fillblank is in hasUniqueLetters, findbug in reverseString: other builds
s = find(C, 3, None, "fillblank", "מערך המונים")
for o in s["options"]:
    L = list(s["lines"]); L[s["blankIndex"]] = L[s["blankIndex"]].replace("___", o["value"])
    r = run(INC + rev + "\n".join(L) + "\n" + pf + DRV3)
    good = o["id"] == s["correctId"]
    print("Q3 fill", o["id"], "*" if good else " ", "==ref" if r == it.ref else "DIFFERS " + repr(r[1])[:70])
    ok &= (r == it.ref) == good
s = find(C, 3, None, "findbug", "reverseString")
revpre, revfn = split_at(rev, "void reverseString")
r = run(INC + "\n".join(s["lines"]) + "\n" + has + pf + DRV3)
print("Q3 bug:", r[0], repr(r[1])[:100]); ok &= r != it.ref
ok &= it.finish()

# ---- Q4 / Q6
V = pathlib.Path(__file__).parent
r4 = run((V / "q4.c").read_text())
assert r4 == (0, "2 2\n4 2\n2 6\n8 6\n8 10\n"), r4
print("Q4 output:", repr(r4[1]))
r6 = run(INC + r"""int main(){ long long a = 1 << (1 << 1); int s = 1 << ((1 << (1 << 1)) + 1); long long v = ((long long)1 << s) - 1;
 printf("%lld %d %lld ", a, s, v); printf("%d\n", (int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)); return 0; }""")
assert r6 == (0, "4 32 4294967295 -1\n"), r6
print("Q6:", repr(r6[1]))

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
