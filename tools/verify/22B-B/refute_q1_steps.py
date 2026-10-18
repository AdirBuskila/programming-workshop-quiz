import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random,string
q=Q("22B-B",1); steps=q["steps"]
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n"
MAIN=r'''
int main(int argc,char**argv){ int a=-9,b=-9; int r=nums_in_halves(argv[1],&a,&b); printf("%d %d %d\n",a,b,r); return 0;}
'''
def ref(s):
    L=len(s); n=L//2
    h1=s[:n]; h2=s[n:] if L%2==0 else s[n+1:]
    a=sum(c.islower() for c in h1); b=sum(c.isupper() for c in h2)
    r=0 if L%2==0 else (1 if s[n].isdigit() else -1)
    return f"{a} {b} {r}"
random.seed(3)
alpha="aAbB1&$% x9Zq"
tests=["t&u5Y%as3k$R","t&u5Y%4as3k$R","t&u5Y%&as3k$R","","a","A","5","ab","aB","abC","aBC","aXb","a1B"]+["".join(random.choice(alpha) for _ in range(random.randint(0,12))) for _ in range(150)]
def chk(src):
    # compile once with a driver that loops all tests? simpler: one exe, many runs
    bad=0;first=None
    for t in tests:
        st,o=run(PRE+src+MAIN,[t]) if t else run(PRE+src+MAIN,[""])
        if st!="OK" or o.strip()!=ref(t):
            bad+=1; first=first or (t,st,o.strip(),ref(t))
    return bad,first
src=sol_code(q)[0]
print("sol",chk(src))
fb=steps[2]
for o in fb["options"]:
    print("fb",o["id"],o["value"],chk("\n".join(fb["lines"]).replace("___",o["value"])))
print("bug",chk("\n".join(steps[4]["lines"])), run(PRE+"\n".join(steps[4]["lines"])+MAIN,["t&u5Y%as3k$R"]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[4]["lines"]])) if a!=b])
L=steps[3]["lines"]
hdr="int nums_in_halves(char* str, int* num1, int* num2)\n{\n%s\n}\n"
good=[]
for p in itertools.permutations(range(len(L))):
    s=hdr%"\n".join(L[i] for i in p)
    # quick check on a subset of tests to prune
    ok=True
    for t in tests[:40]:
        st,o=run(PRE+s+MAIN,[t])
        if st!="OK" or o.strip()!=ref(t): ok=False;break
    if ok: good.append(p)
print("order perms passing 40 tests",good)
print("step1:",ref("t&u5Y%&as3k$R"),"len13?",len("t&u5Y%4as3k$R"),"len with backslash",len("t&u5Y%4as3k\$R"))
