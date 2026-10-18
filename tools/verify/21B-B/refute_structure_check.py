import json,re,sys
def code(sol):
    m=re.search(r"```c\n(.*?)```",sol,re.S); return m.group(1) if m else None
def norm(s): return re.sub(r'\s+',' ',s).strip()
for c in ['21B-B','20B-A','20B-B','19B-A']:
    d=json.load(open(f'raw/{c}.json',encoding='utf-8'))
    for q in d['questions']:
        if q['kind']!='code' or q.get('hold'): continue
        sol=code(q['solution'])
        for i,s in enumerate(q.get('steps') or []):
            t=s['type']
            if t=='order':
                ok = sol is not None and norm(''.join(s['lines']))==norm(sol)
                print(c,q['num'],i,t,'joined==solution',ok)
            elif t in('fillblank','findbug'):
                ls=list(s['lines'])
                if t=='fillblank':
                    bi=s['blankIndex']; opt=[o for o in s['options'] if o['id']==s['correctId']][0]['value']
                    assert ls[bi].strip()=='___',(c,q['num'],i,ls[bi])
                    ls[bi]=opt
                    ok=norm('\n'.join(ls))==norm(sol); print(c,q['num'],i,t,'filled==solution',ok, 'opts',len(s['options']))
                else:
                    sl=[l for l in sol.split('\n')]
                    a=[norm(x) for x in ls if norm(x)]; b=[norm(x) for x in sl if norm(x)]
                    diff=[k for k in range(min(len(a),len(b))) if a[k]!=b[k]]
                    # map bugIndex to nonblank index
                    nb=[k for k,x in enumerate(ls) if norm(x)]
                    bi=s['bugIndex']; 
                    print(c,q['num'],i,t,'len',len(a)==len(b),'diff nonblank idx',[nb[k] for k in diff],'bugIndex',bi)
