import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random
q=Q("22B-A",2); steps=q["steps"]; B=sol_code(q)
print(len(B))
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <math.h>\n"
MAIN=r'''
int main(int argc,char**argv){
  long M=atol(argv[1]); int N=atoi(argv[2]);
  char s[32]; sprintf(s,"%%ld",M); Item*head=NULL,*t=NULL; int i;
  for(i=0;s[i];i++){Item*n=calloc(1,sizeof(Item)); n->data=s[i]-'0'; if(!head)head=t=n; else {t->next=n;t=n;}}
  FUNC(head,N);
  for(t=head;t;t=t->next) printf("%%d",t->data); printf("\n"); return 0;}
'''
def chk(body,func,cases):
    out=""
    for M,N in cases:
        st,o=run(PRE+body+(MAIN%()).replace("FUNC",func),[str(M),str(N)])
        out+="P" if st=="OK" and o.strip()==str(M+N) else ("W" if st=="OK" else st)
    return out
random.seed(2)
cases=[(9994,18),(5,3),(999,1),(1,9),(12,88),(100,1),(7,0+1),(99999,1)]+[(random.randint(1,99999),random.randint(1,99999)) for _ in range(20)]
cases=[c for c in cases if True]
print("v1",chk(B[0]+B[1],"List_num_add_1",cases))
print("v2",chk(B[0]+B[2],"List_num_add",cases))
fb=steps[2]
base=B[0]
for o in fb["options"]:
    s="\n".join(fb["lines"]).replace("___",o["value"])
    print("fb",o["id"],o["value"],chk(base+s,"List_num_add",cases[:6]))
bs="\n".join(steps[4]["lines"])
print("bug",chk(base+bs,"List_num_add",cases[:6]), run(PRE+base+bs+(MAIN%()).replace("FUNC","List_num_add"),["9994","18"]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[4]["lines"]])) if a!=b])
od=steps[3]; L=od["lines"]
hdr="void List_num_add(Item* head, int N)\n{\n%s\n}\n"
good=[]
for p in itertools.permutations(range(len(L))):
    c=chk(base+hdr%"\n".join(L[i] for i in p),"List_num_add",cases[:5])
    if set(c)=={"P"}: good.append(p)
print("order perms",good)
