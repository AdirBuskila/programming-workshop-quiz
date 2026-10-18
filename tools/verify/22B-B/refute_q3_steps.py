import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import random,struct
q=Q("22B-B",3); steps=q["steps"]; B=sol_code(q)
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct { char model[20]; int price; int year; } car;\n"
MAIN=r'''
int main(int argc,char**argv){
  Item*l=appropriateCar(argv[1],argv[2],atoi(argv[3]),atoi(argv[4])); int n=0;
  printf("null=%d\n",l==NULL);
  while(l&&n<50){printf("%d|%d\n",l->price,l->year); l=l->next;n++;}
  return 0;}
'''
TD0="typedef struct item { int price; int year; struct item* next; } Item;\n"
def mk(recs,fn):
    with open(W/fn,"wb") as f:
        for m,p,y in recs: f.write(m.encode().ljust(20,b"\0")+struct.pack("<ii",p,y))
EX=[("Subaru",90000,2019),("Mazda",95000,2020),("Subaru",10000,2009),("Toyota",200000,2022),("Subaru",25000,2012)]
def ref(recs,m,mp,my): return [(p,y) for mm,p,y in recs if mm==m and p<=mp and y>=my]
def chk(src,recs,m,mp,my):
    mk(recs,"c.bin")
    st,o=run(PRE+(TD0 if "typedef" not in src else "")+src+MAIN,[str(W/"c.bin"),m,str(mp),str(my)])
    if st!="OK": return st
    e=ref(recs,m,mp,my)
    want=f"null={int(not e)}\n"+"".join(f"{p}|{y}\n" for p,y in e)
    return "P" if o==want.replace("\r","") or o.replace("\r","")==want else ("W",o)
random.seed(5)
tests=[(EX,"Subaru",100000,2010),(EX,"Subaru",100000,2005),(EX,"Mazda",1,1),([],"x",1,1),(EX,"Subaru",90000,2019)]
for _ in range(25):
    recs=[(random.choice(["Subaru","Mazda","Kia"]),random.randint(1,9)*1000,random.randint(2005,2022)) for _ in range(random.randint(0,7))]
    tests.append((recs,random.choice(["Subaru","Mazda","Kia"]),random.randint(1,9)*1000,random.randint(2005,2022)))
src=B[0]
def run_all(s): return "".join("P" if chk(s,*t)=="P" else "x" for t in tests)
print("sol",run_all(src))
fb=steps[2]
for o in fb["options"]:
    print("fb",o["id"],o["value"],run_all("\n".join(fb["lines"]).replace("___",o["value"]))[:12])
bs="\n".join(steps[3]["lines"])
print("bug",run_all(bs)[:12],chk(bs,*tests[0]))
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
print(chk(src,EX,"Subaru",100000,2005), ref(EX,"Subaru",100000,2005))
print("nonexist",run(PRE+src+MAIN,["nofile.bin","a","1","1"]))
