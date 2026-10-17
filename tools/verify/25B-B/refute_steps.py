import json,subprocess,re,os,sys
d=json.load(open('../../raw/25B-B.json',encoding='utf8'))
Q={q['num']:q for q in d['questions'] if 'part' not in q}
def build(name,src):
    src=src.replace("@N",chr(92)+"n")
    open(name+'.c','w').write(src)
    r=subprocess.run(['clang','-w','-o',name+'.exe',name+'.c'],capture_output=True,text=True)
    if r.returncode: print(name,'COMPILE FAIL',r.stderr[:600]); return False
    return True
def run(name,*a):
    r=subprocess.run(['./'+name+'.exe',*a],capture_output=True,text=True,timeout=20)
    return r.stdout,r.returncode
def fill(st):
    return [ (o['id'],'\n'.join(l if l!='___' else o['value'] for l in st['lines'])) for o in st['options']]
# ---- Q1
pre1='''#include <stdio.h>
#include <stdlib.h>
typedef struct item{int data;struct item*next;}Item;
int List1_elements_in_List2(Item*L1,Item*L2){for(Item*a=L1;a;a=a->next){int f=0;for(Item*b=L2;b;b=b->next)if(b->data==a->data){f=1;break;}if(!f)return 0;}return 1;}
void insert_in_head(int x,Item**pl){Item*t=malloc(sizeof(Item));t->data=x;t->next=*pl;*pl=t;}
'''
# note: my own helper (no length precheck) -> independent
main1='''
static Item* mk(int*a,int k){Item*h=NULL;for(int i=k-1;i>=0;i--){Item*t=malloc(sizeof*t);t->data=a[i];t->next=h;h=t;}return h;}
int main(){int a0[]={2,6,5,1,8},a1[]={8,3,5},a2[]={5},a3[]={1,2,8,5,3},a4[]={8,5,2,8},l[]={8,2,5};
Item*A[]={mk(a0,5),mk(a1,3),mk(a2,1),mk(a3,5),mk(a4,4)};Item*L=mk(l,3);
printf("helper(L,A2)=%d@N",List1_elements_in_List2(L,A[2]));
Item*r=lists_with_given_elements(A,5,L);for(;r;r=r->next)printf("%d ",r->data);printf("@N");return 0;}
'''
st=Q[1]['steps']
for sid,src in fill(st[2]):
    ok=build('refute_q1_fb_'+sid,pre1+src+main1)
    if ok: print('Q1 fill',sid,run('refute_q1_fb_'+sid))
src='\n'.join(st[3]['lines']); 
if build('refute_q1_order',pre1+src+main1): print('Q1 order(as given)',run('refute_q1_order'))
src='\n'.join(st[4]['lines'])
if build('refute_q1_bug',pre1+src+main1): print('Q1 findbug',run('refute_q1_bug'))
# diff of findbug vs correct
def diffidx(a,b): return [i for i,(x,y) in enumerate(zip(a,b)) if x!=y], len(a)==len(b)
print('Q1 bug diff',diffidx(st[3]['lines'],st[4]['lines']), 'bugIndex',st[4]['bugIndex'])
# ---- Q2
pre2='#include <stdio.h>\n#include <stdlib.h>\n'
main2='''
int main(){int n=3;int**lo=malloc(3*sizeof(int*)),**up=malloc(3*sizeof(int*));
int l0[]={76},l1[]={98,4},l2[]={11,19,21};int u0[]={7,-3,13},u1[]={8,42},u2[]={60};
lo[0]=l0;lo[1]=l1;lo[2]=l2;up[0]=u0;up[1]=u1;up[2]=u2;
int**A=triangles_to_matrix(lo,up,n);for(int i=0;i<4;i++){for(int j=0;j<4;j++)printf("%d ",A[i][j]);printf("@N");}
printf("A21=%d A13=%d@N",A[2][1],A[1][3]);return 0;}
'''
st=Q[2]['steps']
for sid,src in fill(st[3]):
    if build('refute_q2_fb_'+sid,pre2+src+main2): print('Q2 fill',sid,run('refute_q2_fb_'+sid)[0].replace('\n','|'))
src='\n'.join(st[4]['lines'])
if build('refute_q2_bug',pre2+src+main2): print('Q2 bug',run('refute_q2_bug')[0].replace('\n','|'))
good=[l if l!='___' else Q[2]['steps'][3]['options'][0]['value'] for l in st[3]['lines']]
print('Q2 diff vs good',[ (i,a,b) for i,(a,b) in enumerate(zip(good,st[4]['lines'])) if a.strip()!=b.strip()], len(good),len(st[4]['lines']))
# ---- Q4/Q6 steps programs
