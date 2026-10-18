import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools
q=Q("23B-B",3); steps=q["steps"]
MAIN=r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%s
int main(int argc,char**argv){
  char buf[200]; strcpy(buf,argv[1]); char orig[200]; strcpy(orig,buf);
  char*w=my_strtok(buf,argv[2]); int n=0;
  while(w&&n<50){ printf("[%%s]",w); free(w); n++; w=my_strtok(NULL,argv[2]); }
  printf(" n=%%d unchanged=%%d\n",n,strcmp(buf,orig)==0); return 0;}
'''
def ref(s,sep):
    out=[];cur=""
    for ch in s:
        if ch in sep:
            if cur: out.append(cur);cur=""
        else: cur+=ch
    if cur: out.append(cur)
    return out
def exp(s,sep):
    r=ref(s,sep); return "".join(f"[{x}]" for x in r)+f" n={len(r)} unchanged=1"
tests=[("   Why?! That's why.","? !."),("a,,b,c,",","),("",","),(",,,",","),("abc",","),("x y",""),(" a",""),("a b c d e f g"," ")]
def chk(src,early=False):
    res=[]
    for s,sep in tests:
        st,o=run(MAIN%src,[s,sep],timeout=3)
        res.append("P" if st=="OK" and o.replace(chr(13),"").rstrip(chr(10))==exp(s,sep) else st if st!="OK" else "W")
        if early and res[-1]!="P": break
    return "".join(res)
src=sol_code(q)[0]
print("sol",chk(src))
fb=steps[1]
for o in fb["options"]:
    print("fb",o["id"],o["value"],chk("\n".join(fb["lines"]).replace("___",o["value"])))
print("bug",chk("\n".join(steps[3]["lines"])), run(MAIN%"\n".join(steps[3]["lines"]),["   Why?! That's why.","? !."]))
od=steps[2]; L=od["lines"]
print(len(L))
# body assembly: the L list is claimed order
hdr="char* my_strtok(char* sentence, char* separators)\n{\n%s\n}\n"
good=[]
for p in itertools.permutations(range(len(L))):
    body="\n".join(L[i] for i in p)
    c=chk(hdr%body,True)
    if set(c)=={"P"} and len(c)==len(tests): good.append(p)
print("passing perms",good)
bg=steps[3]
print([i for i,(a,b) in enumerate(zip([x.strip() for x in fb["lines"][:6]]+["start = sentence;"]+[x.strip() for x in fb["lines"][7:]],[x.strip() for x in bg["lines"]])) if a!=b])
