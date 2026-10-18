import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random
q=Q("21B-A",2); steps=q["steps"]; B=sol_code(q)
PRE="#include <stdio.h>\n#include <stdlib.h>\ntypedef struct item { int data; struct item *next; } Item;\n"
# solution blocks: B[0] has three functions
MAIN=r'''
Item* mk(const char*s){ Item*h=NULL,*t=NULL; char*c=strdup(s); char*tok=strtok(c,","); while(tok){Item*n=calloc(1,sizeof(Item)); n->data=atoi(tok); if(!h)h=t=n; else{t->next=n;t=n;} tok=strtok(NULL,",");} t->next=h; return h;}
int main(int argc,char**argv){
  Item*a=mk(argv[1]),*b=mk(argv[2]);
  Item*c=cyclic_lists_combining(a,b);
  int n=0; Item*p=c; int ok=1;
  do{ printf("%d ",p->data); p=p->next; n++; }while(p!=c && n<100);
  printf("| n=%d closed=%d ret=%d\n",n,p==c,c->data); return 0;}
'''
def parse(s): return [int(x) for x in s.split(",")]
def okcycle(o,A,B_):
    # o: "v v v | n=.. closed=.. ret=.."
    seq,rest=o.split("|"); seq=list(map(int,seq.split()))
    common=set(A)&set(B_); cm=list(common)[0]
    if "closed=1" not in rest: return "notclosed"
    if f"ret={cm}" not in rest: return "badret"
    if seq[0]!=cm: return "retnotcommon"
    if len(seq)!=len(A)+len(B_)-1: return "len%d"%len(seq)
    if sorted(seq)!=sorted(set(A)|set(B_)): return "set"
    # internal order: rotate A,B to start at common (excluding common)
    def rot(L): i=L.index(cm); return L[i+1:]+L[:i]
    ra,rb=rot(A),rot(B_)
    rest_seq=seq[1:]
    if rest_seq==ra+rb or rest_seq==rb+ra: return "OK"
    return "order"
def chk(src,A,B_):
    st,o=run(PRE+"#include <string.h>\n"+src+MAIN,[",".join(map(str,A)),",".join(map(str,B_))])
    if st!="OK": return st
    return okcycle(o.strip(),A,B_)
src="\n".join(B)
random.seed(7)
tests=[([1,2,5,3],[7,5,8]),([5],[5]),([5],[1,5,2]),([1,5,2],[5]),([5,1],[2,5]),([1,5],[5,2]),([5,1],[5,2]),([1,2],[2,3])]
for _ in range(40):
    la=random.randint(1,6); lb=random.randint(1,6)
    vals=random.sample(range(100,200),la+lb)
    A=vals[:la]; Bv=vals[la:la+lb]; cm=1
    A[random.randrange(la)]=cm; Bv[random.randrange(lb)]=cm
    random.shuffle(A); random.shuffle(Bv)
    tests.append((A,Bv))
res=[chk(src,*t) for t in tests]
print("sol",res.count("OK"),len(tests),[ (t,r) for t,r in zip(tests,res) if r!="OK"][:5])
# without the special-case for single-item
nospecial=src.replace("if (L1->next == L1) //L1 has one item\n        return one_item_list(L1, L2);","").replace("if (L2->next == L2) //L2 has one item\n        return one_item_list(L2, L1);","")
print("nospecial applied:", nospecial!=src)
r2=[chk(nospecial,*t) for t in tests]
print("nospecial", [(t,r) for t,r in zip(tests,r2) if r!="OK"][:6])
only_l1=src.replace("if (L2->next == L2) //L2 has one item\n        return one_item_list(L2, L1);","")
only_l2=src.replace("if (L1->next == L1) //L1 has one item\n        return one_item_list(L1, L2);","")
print("no L2 special",[(t,r) for t,r in zip(tests,[chk(only_l1,*t) for t in tests]) if r!="OK"][:4])
print("no L1 special",[(t,r) for t,r in zip(tests,[chk(only_l2,*t) for t in tests]) if r!="OK"][:4])
print("EX order", run(PRE+"#include <string.h>\n"+src+MAIN,["1,2,5,3","7,5,8"]))
# alternative valid answer (B then A) exists per spec -> showing step1 non-unique
fb=steps[2]
pre=src.split("Item *cyclic_lists_combining")[0]
for o in fb["options"]:
    code=pre+"\n".join(fb["lines"]).replace("___",o["value"])
    r=[chk(code,*t) for t in tests[:12]]
    print("fb",o["id"],o["value"],r)
bs=pre+"\n".join(steps[3]["lines"])
print("bug",run(PRE+"#include <string.h>\n"+bs+MAIN,["1,2,5,3","7,5,8"]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
