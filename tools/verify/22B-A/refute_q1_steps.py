import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random
# ---- Q1
q=Q("22B-A",1); steps=q["steps"]
MAIN=r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%s
int main(int argc,char**argv){ char*r=duplicateString(argv[1],argv[2],atoi(argv[3])); printf("[%%s] %%d\n",r,(int)strlen(r)); return 0;}
'''
def ref(b,m,t): return m.join([b]*t)
tests=[("ab","-",3),("ab","-",1),("ab","-",2),("x","yy",5),("","-",3),("abc","",4),("q","-",2)]
def chk(src):
    out=""
    for b,m,t in tests:
        st,o=run(MAIN%src,[b,m,str(t)])
        e=ref(b,m,t)
        out+="P" if st=="OK" and o.strip()==f"[{e}] {len(e)}" else ("W" if st=="OK" else st)
    return out
src=sol_code(q)[0]
print("Q1 sol",chk("#include <stdlib.h>\n"+src))
fb=steps[2]
for o in fb["options"]:
    print(" fb",o["id"],o["value"],chk("\n".join(fb["lines"]).replace("___",o["value"])), run(MAIN%"\n".join(fb["lines"]).replace("___",o["value"]),["ab","-","3"]))
print(" bug",chk("\n".join(steps[4]["lines"])),run(MAIN%"\n".join(steps[4]["lines"]),["ab","-","3"]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print(" diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[4]["lines"]])) if a!=b])
od=steps[3]; L=od["lines"]
hdr="char* duplicateString(char* base, char* middle, int times)\n{\n%s\n}\n"
good=[]
for p in itertools.permutations(range(len(L))):
    c=chk(hdr%"\n".join(L[i] for i in p))
    if set(c)=={"P"}: good.append(p)
print(" Q1 order passing perms",good)
