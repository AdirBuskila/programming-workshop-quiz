import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random,struct
q=Q("22B-B",2); steps=q["steps"]; B=sol_code(q)
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
MAIN=r'''
int main(int argc,char**argv){
  int n=atoi(argv[1]); const char*bits=argv[2]; int i,j;
  int**M=malloc(n*sizeof(int*)); for(i=0;i<n;i++){M[i]=malloc(n*sizeof(int)); for(j=0;j<n;j++) M[i][j]=bits[i*n+j]-'0';}
  int ns=-5; pair*p=indirect_friends(M,n,&ns);
  printf("n=%d null=%d\n",ns,p==NULL);
  for(i=0;i<ns;i++) printf("%d,%d\n",p[i].i,p[i].j);
  return 0;}
'''
EX=["01000100","10100010","01001001","00000101","00100100","10011010","01000101","00110010"]
def flat(rows): return "".join(rows)
def ref(rows):
    n=len(rows); M=[[int(c) for c in r] for r in rows]; out=[]
    for i in range(n):
        for j in range(n):
            if i!=j and M[i][j]==0 and any(M[i][k] and M[k][j] for k in range(n)): out.append((i,j))
    return out
def norm(pairs): return sorted(set(tuple(sorted(p)) for p in pairs))
def chk(src,rows):
    n=len(rows)
    st,o=run(PRE+src+MAIN,[str(n),flat(rows)])
    if st!="OK": return st
    L=o.strip().split("\n"); cnt=int(L[0].split()[0][2:]); got=[tuple(map(int,x.split(","))) for x in L[1:]]
    exp=norm(ref(rows))
    # unordered unique
    if cnt!=len(got): return "CNT"
    if norm(got)!=exp or len(set(tuple(sorted(g)) for g in got))!=len(got): return "W"
    return "P"
print("example count (own)",len(set(tuple(sorted(p)) for p in ref(EX))))
for sz in [1,2]:
    pass
src=B[0]
def randsym(n):
    M=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            M[i][j]=M[j][i]=random.randint(0,1)
    return ["".join(map(str,r)) for r in M]
random.seed(4)
tests=[EX,["0"],["00","00"],["01","10"],["011","101","110"]]+[randsym(random.randint(2,8)) for _ in range(40)]
print("sol",[chk(src,t) for t in tests].count("P"),len(tests), [ (i,chk(src,t)) for i,t in enumerate(tests) if chk(src,t)!="P"][:5])
print("size1 raw:",run(PRE+src+MAIN,["1","0"]))
fb=steps[2]
for o in fb["options"]:
    s=B[0].split("\n")  # not used
    code="\n".join(fb["lines"]).replace("___",o["value"])
    full=B[0].split("pair* indirect_friends")[0]+code
    print("fb",o["id"],o["value"],[chk(full,t) for t in tests[:8]], sum(chk(full,t)!="P" for t in tests))
code="\n".join(steps[3]["lines"]); full=B[0].split("pair* indirect_friends")[0]+code
print("bug",[chk(full,t) for t in tests[:5]],sum(chk(full,t)!="P" for t in tests), run(PRE+full+MAIN,["8",flat(EX)])[1][:20])
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
# triangle claim
print("triangle with bug:",chk(full,["011","101","110"]), run(PRE+full+MAIN,["3","011101110"]))
