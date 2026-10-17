"""Machine checks for the 20B-A steps (Q1, Q2, Q3, Q5). Run: PYTHONUTF8=1 py tools/verify/20B-A/steps_check.py
Reads the SHIPPED tools/raw/20B-A.json; every numeric/choice value is re-measured with clang."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

CODE = "20B-A"
ok = True


def correct_lines(step):
    ln = list(step["lines"])
    ln[step["blankIndex"]] = ln[step["blankIndex"]].replace("___", [o for o in step["options"] if o["id"] == step["correctId"]][0]["value"])
    return ln


# ---------------- Q1
PRE1 = "#include <stdio.h>\n#include <stdlib.h>\nstatic int cnt;\n"
MAIN1 = r'''
static void show(int**A,int n,int*SZ){for(int i=0;i<n;i++){printf("[%d:",SZ[i]);for(int j=0;j<SZ[i];j++)printf(" %d",A[i][j]);printf("]");}printf("\n");}
static void go(int n,int*sizes){int*A[8];int SZ[8];for(int i=0;i<n;i++){SZ[i]=sizes[i];A[i]=malloc(sizes[i]*sizeof(int));for(int j=0;j<sizes[i];j++)A[i][j]=i*10+j;}
 show(A,n,SZ);row_reverse((void**)A,n,SZ);show(A,n,SZ);}
int main(void){int s4[]={4,5,2,3},s5[]={3,1,4,1,5},s1[]={2},s7[]={1,2,3,4,5,6,7};
 go(4,s4);go(5,s5);go(1,s1);go(7,s7);printf("cnt=%d\n",cnt);return 0;}
'''
fb = S.find(CODE, 1, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 1, None, lambda L: PRE1 + "\n".join(L).replace("void **q) {", "void **q) { cnt++;", 1) + MAIN1, ref)
print(it.ref)
out = it.ref[1].splitlines()
assert out[0] == "[4: 0 1 2 3][5: 10 11 12 13 14][2: 20 21][3: 30 31 32]"
assert out[1] == "[3: 30 31 32][2: 20 21][5: 10 11 12 13 14][4: 0 1 2 3]"  # SIZE 3,2,5,4
# swaps: n=4 -> 2, n=5 -> 2, n=1 -> 0, n=7 -> 3
assert out[-1] == "cnt=7"
r7 = S.run(PRE1 + "\n".join(ref).replace("void **q) {", "void **q) { cnt++;", 1) + MAIN1.replace("go(4,s4);go(5,s5);go(1,s1);", ""))
assert r7[1].splitlines()[-1] == "cnt=3", r7
it.fill("השלימו"); it.bug("בגרסה")
ok &= it.finish()

# ---------------- Q2
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct item { int data; struct item *next; } Item;\n"
MAIN2 = r'''
static Item* ring(int*v,int n,int*entry_at,Item**entry){Item*nodes[10];for(int i=0;i<n;i++){nodes[i]=malloc(sizeof(Item));nodes[i]->data=v[i];}
 for(int i=0;i<n;i++)nodes[i]->next=nodes[(i+1)%n];*entry=nodes[*entry_at];return nodes[0];}
static void run(int*v,int n,int e){Item*entry;ring(v,n,&e,&entry);Item*r=cut_cyclic_list(entry);
 if(!r){printf("NULL\n");return;}int c=0;printf("ret=%d chain:",r->data);Item*p=r;while(p&&c<20){printf(" %d",p->data);p=p->next;c++;}printf(p?" CYCLE\n":" end\n");}
int main(void){int a[]={2,4,7,9},b[]={5};
 run(a,4,1);run(a,4,3);run(a,4,0);run(b,1,0);
 printf("null:");Item*r=cut_cyclic_list(NULL);printf("%s\n",r?"nonnull":"NULL");
 {int e=1;Item*entry;ring(a,4,&e,&entry);int steps=0;Item*L=entry;while(L->data<L->next->data){L=L->next;steps++;}printf("steps=%d\n",steps);}
 return 0;}
'''
orders = S.find(CODE, 2, None, "order", "סדרו")["lines"]
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, orders)
print(it.ref)
assert "steps=2" in it.ref[1] and "ret=2 chain: 2 4 7 9 end" in it.ref[1] and "ret=5 chain: 5 end" in it.ref[1]
it.order("סדרו"); ok &= it.finish()
fb = S.find(CODE, 2, None, "fillblank", "השלימו")
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, correct_lines(fb))
assert it.ref == S.run(PRE2 + "\n".join(orders) + MAIN2)
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()

# ---------------- Q3
PRE3 = r'''#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
typedef struct pair { int num_text_rows; int num_bin_records; } Pair;
'''
MAIN3 = r'''
static void mkt(const char*n,int rows){FILE*f=fopen(n,"w");for(int i=0;i<rows;i++)fprintf(f,"row %d\n",i);fclose(f);}
static void mkb(const char*n,int bytes){FILE*f=fopen(n,"wb");for(int i=0;i<bytes;i++)fputc(i%251,f);fclose(f);}
int main(void){mkt("MyFile.dat",2);mkb("binFile120.doc",600);mkt("Students.txt",3);mkb("B_Numbers68.xr",272);
 char*in[]={"MyFile.dat","binFile120.doc","Students.txt","B_Numbers68.xr","Letters.dat","binMissing9.dat"};
 Pair*r=numRowsRecords(in,6);for(int i=0;i<6;i++)printf("%d %d\n",r[i].num_text_rows,r[i].num_bin_records);
 printf("gn=%d %d\n",getNumber("binFile120.doc"),getNumber("B_Numbers68.xr"));return 0;}
'''
fb = S.find(CODE, 3, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, ref)
print(it.ref)
assert it.ref[1] == "2 -1\n-1 5\n3 -1\n-1 4\n0 -1\n-1 0\ngn=120 68\n", it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
S3 = ref
orders = S.find(CODE, 3, None, "order", "סדרו")["lines"]
i0 = S3.index("int NumOfRecords(char *fname, int rec_size) {")
i1 = [i for i, l in enumerate(S3) if "return count/rec_size;" in l][0] + 1
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(S3[:i0] + L + S3[i1 + 1:]) + MAIN3, orders)
assert it.ref == S.run(PRE3 + "\n".join(S3) + MAIN3)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q5
r = S.run(r'''#include <stdio.h>
int main(){char C[]="C++", c;
 for (c=0; c<3; c++) C[c]+=!c?'+'-'+':'-'-'+';
 puts(C); int c0=0; printf("%d %d\n", !c0?'+'-'+':'-'-'+', !1?'+'-'+':'-'-'+'); return 0;}''')
print(r)
assert r[1].splitlines() == ["C--", "0 2"]
print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
