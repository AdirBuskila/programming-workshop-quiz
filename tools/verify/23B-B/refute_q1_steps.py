import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
q=Q("23B-B",1)
steps=q["steps"]
MAIN=r'''
#include <stdio.h>
#include <stdlib.h>
typedef struct node { int value; struct node* next; } node;
%s
int main(int argc,char**argv){
  int n=atoi(argv[1]), m=atoi(argv[2]); int i;
  node* a=malloc(n*sizeof(node));
  for(i=0;i<n;i++){a[i].value=i+1;a[i].next=&a[(i+1)%%n];}
  node* r=JosephusPermutation(n?a:NULL,m); int cnt=0;
  for(;r&&cnt<100;r=r->next,cnt++) printf("%%d ",r->value);
  printf("\n"); return 0;}
'''
def ref(n,m):
    L=list(range(1,n+1)); out=[]; pos=0
    while L:
        pos=(pos+m-1)%len(L); out.append(L.pop(pos))
        if L: pos%=len(L)
    return out
# own reference vs claim solution
src=sol_code(q)[0]
bad=0
for n in range(1,15):
    for m in range(2,12):
        st,o=run(MAIN%src,[str(n),str(m)])
        exp=" ".join(map(str,ref(n,m)))+" "
        if st!="OK" or o.strip()!=exp.strip(): bad+=1; print("MISMATCH",n,m,st,o,exp)
print("solution mismatches",bad)
print("ref 8,3",ref(8,3),"ref 8,2",ref(8,2))
fb=steps[2]
for o in fb["options"]:
    s="\n".join(fb["lines"]).replace("___",o["value"])
    res=[]
    for n,m in [(8,3),(8,2),(5,4)]:
        st,out=run(MAIN%s,[str(n),str(m)])
        res.append((st,out.strip()==" ".join(map(str,ref(n,m))),out.strip()[:40]))
    print("fb",o["id"],o["value"],res)
bg=steps[3]
s="\n".join(bg["lines"])
for n,m in [(8,3),(8,2)]:
    print("bug",n,m,run(MAIN%s,[str(n),str(m)]), ref(n,m))
# single line diff
good=list(fb["lines"]); good[fb["blankIndex"]]=[o for o in fb["options"] if o["id"]==fb["correctId"]][0]["value"]
print([i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in bg["lines"]])) if a!=b], len(good),len(bg["lines"]))
