import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import random
q=Q("21B-A",3); steps=q["steps"]; B=sol_code(q)
PRE="#include <stdio.h>\n#include <stdlib.h>\n"
MAIN=r'''
int main(int argc,char**argv){ int*S=NULL; int rows=-1; int**A=file_to_sequences_in_rows(argv[1],&S,&rows);
 printf("rows=%d\n",rows);
 for(int i=0;i<rows;i++){ printf("%d:",S[i]); for(int j=0;j<S[i];j++) printf(" %d",A[i][j]); printf("\n"); }
 return 0;}
'''
def enc(row):
    out=[];i=0
    while i<len(row):
        j=i
        while j<len(row) and row[j]==row[i]: j+=1
        out+= [row[i],j-i]; i=j
    return out
def mkfile(rows,fn,crlf=False):
    nl="\r\n" if crlf else "\n"
    with open(W/fn,"w",newline="") as f:
        for r in rows: f.write(" ".join(map(str,enc(r)))+nl)
def chk(src,rows,crlf=False):
    mkfile(rows,"a.txt",crlf)
    st,o=run(PRE+src+MAIN,[str(W/"a.txt")])
    if st!="OK": return st
    want=f"rows={len(rows)}\n"+"".join(f"{len(r)}:"+"".join(" "+str(x) for x in r)+"\n" for r in rows)
    return "P" if o.replace("\r","")==want else ("W",o)
EXROWS=[[4,4,7,7,7,7,3,3,3],[2,2,2,2,2,2,1,1],[9,12,12,12],[3,3,18,18,18,18,18,0,0]]
random.seed(8)
tests=[EXROWS]+[[ [random.choice([0,1,2,12,-3]) for _ in range(random.randint(1,8))] for _ in range(random.randint(1,4))] for _ in range(25)]
src=B[0]
print("sol",[chk(src,t) for t in tests].count("P"),len(tests))
print("sol crlf (windows text mode)",chk(src,EXROWS,True))
fb=steps[2]
for o in fb["options"]:
    s="\n".join(fb["lines"]).replace("___",o["value"])
    print("fb",o["id"],o["value"],[chk(s,t) if True else 0 for t in tests[:4]].__repr__()[:200])
bs="\n".join(steps[3]["lines"])
r=chk(bs,EXROWS); print("bug",r)
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
# text of S[3], A[1][6]
print(chk(src,EXROWS))
print("----debug")
mkfile(EXROWS,"a.txt")
print(repr(open(W/"a.txt","rb").read()))
print(run(PRE+src+MAIN,[str(W/"a.txt")]))
for i,t in enumerate(tests[:8]): print(i,t,chk(src,t) if True else 0)
