"""Machine checks for the 19B-A steps (Q1, Q2, Q3, Q5). Run: PYTHONUTF8=1 py tools/verify/19B-A/steps_check.py
Reads the SHIPPED tools/raw/19B-A.json; every numeric/choice value is re-measured with clang."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

CODE = "19B-A"
ok = True


def correct_lines(step):
    ln = list(step["lines"])
    ln[step["blankIndex"]] = ln[step["blankIndex"]].replace("___", [o for o in step["options"] if o["id"] == step["correctId"]][0]["value"])
    return ln


# ---------------- Q1
PRE1 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN1 = r'''
int main(void){char*str[]={"1 Bill Johns, 28","2 Ron Smith, 367","3 Arthur Mitchell, 84","4 Eduard Stone, 17"};
 cyclic_shift_to_file(str,4,"o.txt");
 FILE*f=fopen("o.txt","rb");int c;while((c=fgetc(f))!=EOF)putchar(c=='\n'?'/':c=='\r'?'~':c);printf("\n");
 char*s2[]={"1 a","2 bb"};cyclic_shift_to_file(s2,2,"p.txt");f=fopen("p.txt","rb");while((c=fgetc(f))!=EOF)putchar(c=='\n'?'/':c=='\r'?'~':c);printf("\n");
 return 0;}
'''
fb = S.find(CODE, 1, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 1, None, lambda L: PRE1 + "\n".join(L) + MAIN1, ref)
print(it.ref)
lines = it.ref[1].replace("~", "").split("\n")[0].split("/")
assert lines[:4] == ["1 Ron Smith, 367", "2 Arthur Mitchell, 84", "3 Eduard Stone, 17", "4 Bill Johns, 28"], lines
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
orders = S.find(CODE, 1, None, "order", "סדרו")["lines"]
it = S.Item(CODE, 1, None, lambda L: PRE1 + "\n".join(L) + MAIN1, orders)
assert it.ref == S.run(PRE1 + "\n".join(ref) + MAIN1)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q2
PRE2 = r'''#include <stdio.h>
#include <stdlib.h>
typedef struct data_item { int data; struct data_item *next; } DataItem;
typedef struct ptr_item { DataItem *ptr; struct ptr_item *next; } PtrItem;
'''
MAIN2 = r'''
static DataItem* mk(int*v,int n){DataItem*h=NULL;for(int i=n-1;i>=0;i--){DataItem*e=malloc(sizeof(DataItem));e->data=v[i];e->next=h;h=e;}return h;}
int main(void){int a[]={3,2,4},b[]={6},d[]={1,7};
 PtrItem*p3=malloc(sizeof*p3),*p2=malloc(sizeof*p2),*p1=malloc(sizeof*p1),*p0=malloc(sizeof*p0);
 p0->ptr=mk(a,3);p0->next=p1;p1->ptr=mk(b,1);p1->next=p2;p2->ptr=NULL;p2->next=p3;p3->ptr=mk(d,2);p3->next=NULL;
 DataItem*r=list_of_lists_to_list(p0);int n=0;for(DataItem*q=r;q&&n<20;q=q->next,n++)printf("%d ",q->data);printf("| n=%d\n",n);
 r=list_of_lists_to_list(NULL);printf("empty:%s\n",r?"nonnull":"NULL");return 0;}
'''
fb = S.find(CODE, 2, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, ref)
print(it.ref)
assert it.ref[1] == "9 6 0 8 | n=4\nempty:NULL\n", it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
orders = S.find(CODE, 2, None, "order", "סדרו")["lines"]
it = S.Item(CODE, 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, orders)
assert it.ref == S.run(PRE2 + "\n".join(ref) + MAIN2)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q3
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN3 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
int main(void){int A[5][COLS]={{20,14,10,13,33,80},{40,10,55,11,12,13},{15,16,17,18,19,21},{41,43,53,41,17,15},{10,20,30,40,50,62}};
 int*S=NULL,rows=-1;stackwipe();int**B=even_sums_odd_numbers(A,5,6,&S,&rows);
 printf("prows=%d\n",rows);for(int i=0;i<rows;i++){printf("S=%d:",S[i]);for(int j=0;j<S[i];j++)printf(" %d",B[i][j]);printf("\n");}return 0;}
'''
fb = S.find(CODE, 3, None, "fillblank", "השלימו")
ref = correct_lines(fb)
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, ref)
print(it.ref)
assert it.ref[1] == "prows=3\nS=2: 13 33\nS=4: 15 17 19 21\nS=6: 41 43 53 41 17 15\n", it.ref
it.fill("השלימו"); it.bug("בגרסה"); ok &= it.finish()
orders = S.find(CODE, 3, None, "order", "סדרו")["lines"]
it = S.Item(CODE, 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, orders)
assert it.ref == S.run(PRE3 + "\n".join(ref) + MAIN3)
it.order("סדרו"); ok &= it.finish()

# ---------------- Q5
r = S.run(r'''#include <stdio.h>
int main(){int i,cnt=0;
 for (i=0; i<sizeof"sizeof"[i]; i++){ printf("%d",sizeof"sizeof"[i]); cnt++; }
 printf("\ncnt=%d size=%d expr=%d\n",cnt,(int)sizeof("sizeof"),(int)sizeof"sizeof"[0]); return 0;}''')
print(r)
assert r[1].splitlines() == ["1", "cnt=1 size=7 expr=1"], r
print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
