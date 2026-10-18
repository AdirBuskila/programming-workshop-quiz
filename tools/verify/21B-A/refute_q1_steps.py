import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import itertools,random
q=Q("21B-A",1); steps=q["steps"]
PRE="#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct { char first_name[30], last_name[30]; } name;\n"
MAIN=r'''
int main(int argc,char**argv){ int n=(argc-1)/2; name*a=malloc((n+1)*sizeof(name)); int i;
 for(i=0;i<n;i++){strcpy(a[i].first_name,argv[1+2*i]);strcpy(a[i].last_name,argv[2+2*i]);}
 printf("%d\n",ordered_name_array(a,n)); return 0;}
'''
def ref(recs):
    f=[r[0] for r in recs]; l=[r[1] for r in recs]
    if f==sorted(f): return 1
    if l==sorted(l): return 2
    return 0
EX=[("Mike","Asher"),("David","Bern"),("Joseph","Borgman"),("Alon","Kapulski"),("Ilan","Mizrachi"),("Oren","Nodel"),("Abraham","Rosen")]
random.seed(6)
words=["a","b","c","d","e"]
tests=[EX,[],[("A","Z")],[("Aaron","Zed"),("Ben","Yoni"),("Carl","Xavi")],[("A","B"),("A","B")],[("B","A"),("A","A")],[("B","C"),("A","C"),("C","D")]]
for _ in range(120):
    tests.append([(random.choice(words),random.choice(words)) for _ in range(random.randint(0,5))])
def chk(src):
    bad=[];
    for t in tests:
        args=[x for p in t for x in p]
        st,o=run(PRE+src+MAIN,args)
        if st!="OK" or o.strip()!=str(ref(t)): bad.append(t)
    return len(bad),bad[:1]
src=sol_code(q)[0]
print("sol",chk(src))
fb=steps[1]
for o in fb["options"]:
    print("fb",o["id"],o["value"],chk("\n".join(fb["lines"]).replace("___","            "+o["value"])), "EX ->", run(PRE+"\n".join(fb["lines"]).replace("___",o["value"])+MAIN,[x for p in EX for x in p])[1].strip())
bs="\n".join(steps[3]["lines"])
print("bug",chk(bs)[0], run(PRE+bs+MAIN,["Aaron","Zed","Ben","Yoni","Carl","Xavi"])[1].strip())
good=list(fb["lines"]); good[fb["blankIndex"]]=fb["options"][0]["value"]
print("diff",[i for i,(a,b) in enumerate(zip([x.strip() for x in good],[x.strip() for x in steps[3]["lines"]])) if a!=b])
L=steps[2]["lines"]
hdr="int ordered_name_array(name* name_arr, int n)\n{\n%s\n}\n"
good=[]
for p in itertools.permutations(range(len(L))):
    s=hdr%"\n".join(L[i] for i in p)
    if chk(s)[0]==0: good.append(p)
print("order perms",good)
