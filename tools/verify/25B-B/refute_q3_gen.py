import json,subprocess,os
d=json.load(open('../../raw/25B-B.json',encoding='utf8'))
q=[x for x in d['questions'] if x['num']==3][0]
st=q['steps']
pre='#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct {char id[10];char name[31];double total;} clientData;\n'
rd='''
int main(int c,char**v){text_to_binary(v[1],v[2]);FILE*f=fopen(v[2],"rb");fseek(f,0,SEEK_END);long n=ftell(f);printf("size=%ld recs=%ld sizeof=%d|",n,n/(long)sizeof(clientData),(int)sizeof(clientData));
rewind(f);clientData r;while(fread(&r,sizeof r,1,f)==1)printf("[%s|%s|%.2f]",r.id,r.name,r.total);printf("@N");return 0;}
'''.replace('@N',chr(92)+'n')
def build(n,src):
    open(n+'.c','w').write(src)
    r=subprocess.run(['clang','-w','-o',n+'.exe',n+'.c'],capture_output=True,text=True)
    if r.returncode: print(n,'COMPILE FAIL',r.stderr[:300]);return False
    return True
def run(n,t,b):
    try:
        r=subprocess.run(['./'+n+'.exe',t,b],capture_output=True,text=True,timeout=10)
        return r.returncode,r.stdout.strip()
    except Exception as e: return 'ERR',str(e)
ex=("06842151          Moshe    71.25\n330578795      Benjamin  1755.65\n20051546           Dina   560.10\n")
# fixed width: id9 + name30 + total8 edge: 30-char name, 9-char id, 8-col total
n30='A'*30
edge="123456789"+n30+"12345.67\n"+"987654321"+"       Bob".rjust(30)+"   99.50\n"
open('t_ex.txt','w',newline='').write(ex)
open('t_ex_nonl.txt','w',newline='').write(ex.rstrip('\n'))
open('t_edge.txt','w',newline='').write(edge)
fb=st[2]
for o in fb['options']:
    src='\n'.join(l if l!='___' else o['value'] for l in fb['lines'])
    n='refute_q3_fb_'+o['id']
    if build(n,pre+src+rd):
        print(o['id'],o['value'])
        for t in ['t_ex.txt','t_edge.txt']:
            print('   ',t,run(n,t,'t_out.bin'))
# official as given, no trailing newline + w vs wb
src='\n'.join(l if l!='___' else fb['options'][0]['value'] for l in fb['lines'])
build('refute_q3_good',pre+src+rd)
print('good nonl',run('refute_q3_good','t_ex_nonl.txt','t_out.bin'))
# findbug
src='\n'.join(st[4]['lines']);build('refute_q3_bug',pre+src+rd);print('bug',run('refute_q3_bug','t_ex.txt','t_out.bin'))
a=st[3]['lines'];b=[l if l!='___' else fb['options'][0]['value'] for l in fb['lines']];print('order==fill-good',a==b)
good=[l for l in a];print('bug diff',[i for i,(x,y) in enumerate(zip(good,st[4]['lines'])) if x!=y],st[4]['bugIndex'])
