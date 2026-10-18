import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import struct,random
q=Q("22B-A",3); steps=q["steps"]
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct { char address[30]; int rooms; int price; } apartment;\n"
MAIN=r'''
int main(int argc,char**argv){ int c=-7; apartment*r=appropriateAppartment(argv[1],atoi(argv[2]),atoi(argv[3]),&c);
 printf("count=%d null=%d\n",c,r==NULL); for(int i=0;i<c;i++) printf("%s %d %d\n",r[i].address,r[i].rooms,r[i].price); printf("sz=%d\n",(int)sizeof(apartment)); return 0;}
'''
def mk(recs,fn):
    with open(W/fn,"wb") as f:
        for a,r,p in recs: f.write(a.encode().ljust(30,b"\0")+b"\0\0"+struct.pack("<ii",r,p))
EX=[("Begin 7",3,700000),("Reznik 4",4,1000000),("Ben-Gurion 27",5,4000000),("Dubnov 13",3,1100000),("Cohen 66",3,900000)]
def chk(src,recs,rn,mp):
    mk(recs,"ap.bin"); st,o=run(PRE+src+MAIN,[str(W/"ap.bin"),str(rn),str(mp)])
    if st!="OK": return st
    e=[x for x in recs if x[1]==rn and x[2]<=mp]
    want=f"count={len(e)} null={int(not e)}\n"+"".join(f"{a} {r} {p}\n" for a,r,p in e)+"sz=40\n"
    return "P" if o==want else ("W",o)
src=sol_code(q)[0]
random.seed(9)
tests=[(EX,3,1000000),(EX,3,1100000),(EX,9,1),([],3,1)]
for _ in range(20):
    tests.append(([("A%d"%i,random.randint(1,4),random.randint(1,5)*100) for i in range(random.randint(0,6))],random.randint(1,4),random.randint(1,5)*100))
ra=lambda s:"".join("P" if chk(s,*t)=="P" else "x" for t in tests)
print("sol",ra(src))
fb=steps[2]
for o in fb["options"]: print("fb",o["id"],o["value"],ra("\n".join(fb["lines"]).replace("___",o["value"]))[:10])
bs="\n".join(steps[3]["lines"]); print("bug",ra(bs)[:10],chk(bs,*tests[1]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
print(chk(src,EX,3,1100000))
