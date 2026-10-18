import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import struct,random
q=Q("23B-B",2)
steps=q["steps"]
MAIN=r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct { char film_code[10]; int copies; int year; } film;
%s
int main(int argc,char**argv){
  int sz=-7; film* r=appropriateFilm(argv[1],atoi(argv[2]),atoi(argv[3]),&sz);
  printf("size=%%d ptr=%%d\n",sz,r!=NULL);
  for(int i=0;i<sz;i++) printf("%%s %%d %%d\n",r[i].film_code,r[i].copies,r[i].year);
  printf("sizeof=%%d\n",(int)sizeof(film));
  return 0;}
'''
def mk(recs,path):
    with open(W/path,"wb") as f:
        for c,cp,y in recs:
            f.write(c.encode().ljust(10,b"\0")+struct.pack("<ii",cp,y))   # padding 2 bytes after 10 chars
def mk2(recs,path):
    with open(W/path,"wb") as f:
        for c,cp,y in recs:
            f.write(c.encode().ljust(10,b"\0")+b"\0\0"+struct.pack("<ii",cp,y))
ex=[("A346-f",2,1967),("D8120-fx",4,1960),("S516-t",1,1970),("R11-v",2,1972),("G555-xx",3,2010)]
mk2(ex,"ex.bin")
print("filesize",(W/"ex.bin").stat().st_size)
def ref(recs,cl,ly): return [r for r in recs if r[1]<=cl and r[2]<=ly]
def check(src,recs,cl,ly,fn="t.bin"):
    mk2(recs,fn)
    st,o=run(MAIN%src,[str(W/fn),str(cl),str(ly)])
    if st!="OK": return st
    lines=o.strip().split("\n"); exp=ref(recs,cl,ly)
    want=[f"size={len(exp)} ptr={int(bool(exp))}"]+[f"{c} {cp} {y}" for c,cp,y in exp]+["sizeof=20"]
    return "PASS" if lines==want else ("WRONG",lines)
src=sol_code(q)[0]
random.seed(1); bad=0
for t in range(60):
    recs=[("F%d"%i,random.randint(0,5),random.randint(1950,2020)) for i in range(random.randint(0,8))]
    r=check(src,recs,random.randint(0,5),random.randint(1950,2020))
    if r!="PASS": bad+=1; print(r)
print("sol bad",bad, check(src,ex,2,1970), check(src,ex,3,1972))
# nonexistent
print(run(MAIN%src,[str(W/"nonexist.bin"),"1","1"]))
fb=steps[2]
for o in fb["options"]:
    s="\n".join(fb["lines"]).replace("___",o["value"])
    print("fb",o["id"],o["value"],check(s,ex,2,1970),check(s,ex,3,1972))
bg=steps[3]; s="\n".join(bg["lines"])
print("bug",check(s,ex,2,1970))
good=list(fb["lines"]); good[fb["blankIndex"]]=[o for o in fb["options"] if o["id"]==fb["correctId"]][0]["value"]
print([i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in bg["lines"]])) if a!=b])
