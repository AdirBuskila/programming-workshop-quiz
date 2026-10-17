"""Machine checks for the 21B-B steps (Q2, Q3, Q5). Run: PYTHONUTF8=1 py tools/verify/21B-B/steps_check.py
Reads the SHIPPED tools/raw/21B-B.json; every numeric/choice value is re-measured with clang."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

ok = True

# ---------------- Q2
PRE2 = r'''#include <stdio.h>
#include <string.h>
typedef struct { char last_name[30], first_name[30]; unsigned id; } person;
'''
MAIN2 = r'''
static person mk(const char*l,const char*f,unsigned id){person p;strcpy(p.last_name,l);strcpy(p.first_name,f);p.id=id;return p;}
int main(void){
 person e1[10]={mk("Asher","Mike",231567809),mk("Bern","David",216578900),mk("Borgman","Joseph",354678903),
  mk("Cohen","Abraham",224567821),mk("Cohen","Den",206666431),mk("Levi","Ilan",290876441),
  mk("Levi","Omri",245689432),mk("Levi","Omri",245689436),mk("Smith","Jack",345389010),mk("Smith","John",311232111)};
 person e2[10]; memcpy(e2,e1,sizeof e1); person t=e2[6]; e2[6]=e2[7]; e2[7]=t;
 printf("e1=%d e2=%d\n",ordered_person_array(e1,10),ordered_person_array(e2,10));
 int first=-1; for(int k=1;k<=10;k++) if(!ordered_person_array(e2,k)){first=k-1;break;}
 printf("firstfail=%d\n",first);
 person dup[2]={mk("A","B",5),mk("A","B",5)};
 person lb[2]={mk("B","x",1),mk("A","x",2)};
 person fb[2]={mk("A","z",1),mk("A","b",2)};
 person idq[2]={mk("A","b",9),mk("A","c",1)};
 printf("dup=%d lastbad=%d firstbad=%d idq=%d n1=%d n0=%d\n",ordered_person_array(dup,2),ordered_person_array(lb,2),
   ordered_person_array(fb,2),ordered_person_array(idq,2),ordered_person_array(e1,1),ordered_person_array(e1,0));
 printf("strcmp=%d %d\n",strcmp("Asher","Bern")<0,strcmp("Bern","Asher")>0);
 return 0;}
'''
import json
fb = S.find("21B-B", 2, None, "fillblank", "מתי מחזירים")
ref = list(fb["lines"]); ref[fb["blankIndex"]] = ref[fb["blankIndex"]].replace("___", [o for o in fb["options"] if o["id"] == fb["correctId"]][0]["value"])
it = S.Item("21B-B", 2, None, lambda L: PRE2 + "\n".join(L) + MAIN2, ref)
print(it.ref)
assert "firstfail=7" in it.ref[1] and "e1=1 e2=0" in it.ref[1] and "strcmp=1 1" in it.ref[1]
assert "dup=1 lastbad=0 firstbad=0 idq=1 n1=1 n0=1" in it.ref[1]
it.fill("מתי מחזירים"); it.bug("בגרסה הבאה")
ok &= it.finish()

# ---------------- Q3
PRE3 = r'''#include <stdio.h>
#include <stdlib.h>
'''
MAIN3 = r'''
static element* mk(int d,int c,element*n){element*e=malloc(sizeof(element));e->data=d;e->col=c;e->ptr_next=n;return e;}
static void pr(int**a,int r,int c){for(int i=0;i<r;i++){for(int j=0;j<c;j++)printf("%d ",a[i][j]);printf("\n");}}
static void stackwipe(void){volatile char z[4096];for(int i=0;i<4096;i++)z[i]=0;}
int main(void){
 element* l[4]; l[0]=mk(1,3,mk(2,1,NULL)); l[1]=NULL; l[2]=mk(3,0,NULL); l[3]=mk(2,2,mk(1,0,mk(3,3,NULL)));
 stackwipe();
 int**m=lists_to_sparse_matrix(l,4,4); pr(m,4,4);
 element* k[3]; k[0]=mk(5,2,mk(7,4,NULL)); k[1]=NULL; k[2]=mk(3,0,NULL);
 int**n=lists_to_sparse_matrix(k,3,5); int z=0; for(int i=0;i<3;i++)for(int j=0;j<5;j++)z+=(n[i][j]==0);
 printf("zeros=%d\n",z);
 return 0;}
'''
orders = S.find("21B-B", 3, None, "order", "סדרו")["lines"]
it = S.Item("21B-B", 3, None, lambda L: PRE3 + "\n".join(L) + MAIN3, orders)
print(it.ref)
assert "zeros=12" in it.ref[1]
it.order("סדרו"); it.fill("השלימו"); it.bug("בגרסה")
ok &= it.finish()

# ---------------- Q5
r = S.run(r'''#include <stdio.h>
int main(){printf("%d",printf("%d%d",printf("%d",11),printf("%d",11)));
 puts("");int a=printf("%d",11);int b=printf("%d%d",a,a);printf("|a=%d b=%d\n",a,b);return 0;}''')
print(r)
assert r[1].splitlines()[0] == "1111222" and "|a=2 b=2" in r[1]
print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
