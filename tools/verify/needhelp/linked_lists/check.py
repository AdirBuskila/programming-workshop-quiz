"""Machine check of the guided course courses/linked_lists/C01..C08 with clang.
Run from the app root:  PYTHONUTF8=1 py tools/verify/needhelp/linked_lists/check.py
Every stored answer (mcq correctId, numeric answer, fillblank/findbug/order key) is re-derived by compiling and running C;
distractor claims made in explanations are asserted too. Exits 1 on any failure."""
import itertools, json, pathlib, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang"
ROOT = pathlib.Path(__file__).resolve().parents[4]
FAILS = []
COUNT = [0]


def check(cond, msg):
    COUNT[0] += 1
    if not cond:
        FAILS.append(msg)
        print("FAIL", msg)


def run(src, timeout=5):
    """-> ('OK', stdout) | ('CRASH', stdout) | ('TIMEOUT','') | ('BUILD', stderr)"""
    d = pathlib.Path(tempfile.mkdtemp(prefix="nh_ll_"))
    try:
        c, exe = d / "t.c", d / "t.exe"
        c.write_text(src, encoding="utf-8")
        p = subprocess.run([CLANG, "-w", "-O0", "-o", str(exe), str(c)], capture_output=True, text=True, errors="replace", cwd=d)
        if p.returncode:
            return ("BUILD", p.stderr[:200])
        try:
            r = subprocess.run([str(exe)], capture_output=True, text=True, errors="replace", timeout=timeout, cwd=d)
        except subprocess.TimeoutExpired:
            return ("TIMEOUT", "")
        return ("OK" if r.returncode == 0 else "CRASH", " ".join(r.stdout.split()))
    finally:
        shutil.rmtree(d, ignore_errors=True)


def pmap(f, xs):
    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(f, xs))


# ---------------------------------------------------------------- load the course
raw = subprocess.run(["node", "tools/course_load.js"], capture_output=True, cwd=ROOT, check=True)
LV = {e["level"]["id"]: e["level"] for e in json.loads(raw.stdout.decode("utf-8"))["levels"] if e["courseId"] == "linked_lists"}
Q = {}
for lv in LV.values():
    for q in lv["questions"]:
        if "id" in q:
            Q[q["id"]] = q


def strip(s):
    return s.replace("`", "").strip()


def mcq_text(qid):
    q = Q[qid]
    return strip({o["id"]: o["value"] for o in q["options"]}[q["correctId"]])


def opts(step_or_q):
    return {o["id"]: strip(o["value"]) for o in step_or_q["options"]}


def num(qid):
    return Q[qid]["step"]["answer"]


# ---------------------------------------------------------------- C building blocks
HEAD = "#include <stdio.h>\n#include <stdlib.h>\n"
TYPES = "typedef struct item { int data; struct item *next; } Item;\n"
NEW = "Item *new_item(int data, Item *next){ Item *t=(Item*)malloc(sizeof(Item)); t->data=data; t->next=next; return t; }\n"
INS = "void insert_head(Item **head,int data){ *head=new_item(data,*head); }\n"
FROM = "Item *from_array(const int*a,int n){ Item *h=NULL; int i; for(i=n-1;i>=0;i--) insert_head(&h,a[i]); return h; }\n"
FROM2 = "Item *from_array(const int*a,int n){ Item *h=NULL,**t=&h; int i; for(i=0;i<n;i++){ *t=(Item*)malloc(sizeof(Item)); (*t)->data=a[i]; (*t)->next=NULL; t=&(*t)->next; } return h; }\n"
PRT = "void print_list(const Item*p){ int k=0; for(;p&&k<30;p=p->next,k++) printf(\"%d \",p->data); }\n"
BASE = HEAD + TYPES + NEW + INS + FROM + PRT
MK = lambda arr: "{" + ",".join(map(str, arr)) + "}"


def lst(name, arr):
    return f"int {name}_a[]={MK(arr) if arr else '{0}'}; Item *{name}=from_array({name}_a,{len(arr)});\n"


def main_(body):
    return "int main(void){\n" + body + "\nreturn 0;}\n"


# ================================================================= C01
good = HEAD + "typedef struct item { int data; struct item *next; } Item;\nint main(void){return 0;}\n"
bad = HEAD + "typedef struct { int data; Item *next; } Item;\nint main(void){return 0;}\n"
check(run(good)[0] == "OK", "C01-Q1 reference struct must compile")
check(run(bad)[0] == "BUILD", "C01-Q1 typedef without a tag must fail to compile")
check(mcq_text("C01-Q1").startswith("שגיאת הידור"), "C01-Q1 stored answer")

r = run(BASE + main_(lst("h", [3, 5, 2, 4]) + "int s=0; Item*p; for(p=h;p;p=p->next) s+=p->data; printf(\"%d\",s);"))
check(r == ("OK", str(int(num("C01-Q2")))), f"C01-Q2 sum {r}")
r = run(BASE + main_(lst("h", [3, 5, 2, 4]) + "printf(\"%d\",h->next->next->data);"))
check(r == ("OK", mcq_text("C01-Q3")), f"C01-Q3 {r}")
r = run(BASE + main_("Item*h=NULL,*p; int c=0; for(p=h;p;p=p->next) c++; printf(\"%d\",c);"))
check(r == ("OK", str(int(num("C01-Q4")))), f"C01-Q4 {r}")
r = run(BASE + main_(lst("h", [3, 5, 2]) + "Item*p; for(p=h;p;p=p->next) ; printf(p==NULL?\"NULL\":\"other\");"))
check(r == ("OK", mcq_text("C01-Q5")), f"C01-Q5 {r}")

# ================================================================= C02
r = run(BASE + main_("Item*h=NULL; insert_head(&h,1); insert_head(&h,2); insert_head(&h,3); print_list(h);"))
check(r == ("OK", mcq_text("C02-Q1")), f"C02-Q1 {r}")
r = run(BASE + main_(lst("h", list(range(1, 9))) + "Item*p=h; int c=0; while(p->next){p=p->next;c++;} printf(\"%d\",c);"))
check(r == ("OK", str(int(num("C02-Q2")))), f"C02-Q2 {r}")
r = run(BASE + "void add(Item *head,int x){ head=new_item(x,head); }\n" + main_(lst("h", [3, 5]) + "add(h,9); print_list(h);"))
check(r == ("OK", mcq_text("C02-Q3")), f"C02-Q3 {r}")


def findbug(qid, fix, driver, pre, good_out, bad_out):
    st = Q[qid]["step"]
    lines = list(st["lines"])
    bad_src = pre + "\n".join(lines) + "\n" + driver
    lines[st["bugIndex"]] = fix
    good_src = pre + "\n".join(lines) + "\n" + driver
    g, b = run(good_src), run(bad_src)
    check(g == good_out, f"{qid} fixed version {g} != {good_out}")
    check(b == bad_out if bad_out else b != good_out, f"{qid} buggy version {b} (expected {bad_out})")
    # no other single-line replacement by the fix can matter: the bug line is the only one whose fix repairs it
    return g, b


findbug("C02-Q4", "    t->next = *head;",
        main_(lst("h", [2, 1]) + "insert_head(&h,3); print_list(h);"), HEAD + TYPES + NEW + FROM.replace("insert_head(&h,a[i])", "h=new_item(a[i],h)") + PRT,
        ("OK", "3 2 1"), ("OK", "3"))


def fillblank(qid, pre, driver, expect, extra_expect=None):
    st = Q[qid]["step"]
    o = {x["id"]: x["value"] for x in st["options"]}
    outs = {}
    for k, v in o.items():
        lines = list(st["lines"])
        lines[st["blankIndex"]] = lines[st["blankIndex"]].replace("___", v)
        outs[k] = run(pre + "\n".join(lines) + "\n" + driver)
    check(outs[st["correctId"]] == ("OK", expect), f"{qid} correct option gives {outs[st['correctId']]} (want {expect})")
    for k, r in outs.items():
        if k != st["correctId"]:
            check(r != ("OK", expect), f"{qid} distractor {k} reproduces the reference {r}")
    if extra_expect:
        for k, want in extra_expect.items():
            check(outs[k] == want, f"{qid} option {k}: {outs[k]} (explanation says {want})")
    return outs


fillblank("C02-Q5", HEAD + TYPES + NEW,
          main_("Item*h=NULL,*t=NULL,*p; int i; for(i=1;i<=4;i++) append(&h,&t,i); for(p=h;p&&i<40;p=p->next,i++) printf(\"%d \",p->data);"),
          "1 2 3 4", {"b": ("OK", "1"), "c": ("OK", "1 4"), "d": ("OK", "4")})

# ================================================================= C03
r = run(BASE + main_(lst("h", [5, 1, 4, 3, 8]) + "Item*p; int c=0; for(p=h;p;p=p->next) if(p->data>3) c++; printf(\"%d\",c);"))
check(r == ("OK", str(int(num("C03-Q1")))), f"C03-Q1 {r}")
r = run(BASE + main_("Item*h=NULL,*p=h; while(p->next) p=p->next; printf(\"x\");"))
check(r[0] == "CRASH" and mcq_text("C03-Q2").startswith("קריסה"), f"C03-Q2 {r}")
LASTDRV = main_(lst("h", [1, 2, 3]) + "Item*p=last(h); printf(p?\"%d\":\"NULL\",p?p->data:0);")
findbug("C03-Q3", "    while (p && p->next)", LASTDRV, BASE, ("OK", "3"), ("OK", "NULL"))
FINDDRV = main_(lst("h", [4, 9, 1]) + "Item*a=find(h,9),*b=find(h,7),*c=find(h,4); printf(\"%d %s %d\",a?a->data:-1,b?\"found\":\"NULL\",c?c->data:-1);")
fo = fillblank("C03-Q4", BASE, FINDDRV, "9 NULL 4")
# the distractor claims in the explanation
check(fo["b"][1] != "9 NULL 4" and fo["c"][1] != "9 NULL 4", "C03-Q4 distractors differ")
r_ok = run(BASE + "Item *find(Item*head,int x){Item*p=head; while(p && p->data!=x) p=p->next; return p;}\n" + main_(lst("h", [4, 9, 1]) + "Item*b=find(h,7); printf(b?\"found\":\"NULL\");"))
r_sw = run(BASE + "Item *find(Item*head,int x){Item*p=head; while(p->data!=x && p) p=p->next; return p;}\n" + main_(lst("h", [4, 9, 1]) + "Item*b=find(h,7); printf(b?\"found\":\"NULL\");"))
r_sw_found = run(BASE + "Item *find(Item*head,int x){Item*p=head; while(p->data!=x && p) p=p->next; return p;}\n" + main_(lst("h", [4, 9, 1]) + "Item*b=find(h,9); printf(b?\"found\":\"NULL\");"))
check(r_ok == ("OK", "NULL") and r_sw[0] == "CRASH" and r_sw_found == ("OK", "found"), f"C03-Q5 {r_ok} {r_sw} {r_sw_found}")
check(mcq_text("C03-Q5").startswith("כש-x לא נמצא"), "C03-Q5 stored answer")

# ================================================================= C04
FREECNT = "static int nfree=0;\n#define free(p) do{nfree++;free(p);}while(0)\n"
DEL = """void delete_value(Item **head,int val){ Item *curr=*head,*prev=NULL; while(curr){ Item *next=curr->next;
 if(curr->data==val){ if(prev==NULL) *head=next; else prev->next=next; free(curr);} else prev=curr; curr=next; } }\n"""
q1 = Q["C04-Q1"]
o1 = opts(q1)
res = {}
for k, v in o1.items():
    res[k] = run(BASE + main_(lst("h", [1, 2, 3]) + f"Item *prev=h,*curr=h->next; {v}\n print_list(h);"))
check(res[q1["correctId"]] == ("OK", "1 3"), f"C04-Q1 correct option {res[q1['correctId']]}")
for k, v in res.items():
    if k != q1["correctId"]:
        check(v != ("OK", "1 3"), f"C04-Q1 distractor {k} gives the right result {v}")
check(res["b"] == ("OK", "1 2 3") and res["d"] == ("OK", "1 2 3") and "1 2 1 2" in res["c"][1], f"C04-Q1 claims {res}")
check(o1[q1["correctId"]] == "prev->next = curr->next;", "C04-Q1 stored answer")
r = run(BASE + FREECNT + DEL + main_(lst("h", [2, 2, 5, 2, 7]) + "delete_value(&h,2); print_list(h); printf(\"| %d\",nfree);"))
check(r == ("OK", f"5 7 | {int(num('C04-Q2'))}"), f"C04-Q2 {r}")
DELDRV = main_(lst("h", [4, 1, 4, 2]) + "delete_value(&h,4); print_list(h);")
st = Q["C04-Q3"]["step"]
good_lines = list(st["lines"]); good_lines[st["bugIndex"]] = "            if (prev == NULL)"
g = run(BASE + "\n".join(good_lines) + DELDRV)
b = run(BASE + "\n".join(st["lines"]) + DELDRV)
check(g == ("OK", "1 2") and b[0] == "CRASH", f"C04-Q3 {g} {b}")
r = run(BASE + DEL + main_(lst("h", [4, 4, 1, 4, 4, 2, 4]) + "delete_value(&h,4); print_list(h);"))
check(r == ("OK", mcq_text("C04-Q4")), f"C04-Q4 {r}")
DRV5 = main_("".join(lst(f"h{i}", a) + f"delete_value2(&h{i},{v}); print_list(h{i}); printf(\"| \");\n" for i, (a, v) in enumerate(
    [([1, 2, 3, 2], 2), ([2, 2, 1], 2), ([5, 2], 2), ([2], 2), ([1, 3], 2)])))
fo = fillblank("C04-Q5", BASE, DRV5, "1 3 | 1 | 5 | | 1 3 |")

# ================================================================= C05
r = run(BASE + main_(lst("h", [1, 2, 3, 4, 5, 6]) + "Item*res=NULL,*p; for(p=h;p;p=p->next) if(p->data%2==0) insert_head(&res,p->data); print_list(res);"))
check(r == ("OK", mcq_text("C05-Q1")), f"C05-Q1 {r}")
EV_DRV = main_(lst("h", [1, 2, 3, 4]) + "print_list(evens(h));")
fillblank("C05-Q2", BASE, EV_DRV, "2 4", {"b": ("OK", "4"), "c": ("OK", ""), "d": ("OK", "2")})
r = run(HEAD + "static int nm=0;\n#define malloc(n) (nm++,malloc(n))\n" + TYPES + NEW + INS + FROM + PRT +
        "Item *evens(const Item *src){ Item dummy,*tail=&dummy; dummy.next=NULL; for(;src;src=src->next) if(src->data%2==0){ tail->next=new_item(src->data,NULL); tail=tail->next;} return dummy.next; }\n" +
        main_(lst("h", [1, 2, 3, 4, 5, 6, 7]).replace("from_array", "from_array") + "nm=0; Item*e=evens(h); print_list(e); printf(\"| %d\",nm);"))
check(r == ("OK", f"2 4 6 | {int(num('C05-Q3'))}"), f"C05-Q3 {r}")
findbug("C05-Q4", "    for (i = n - 1; i >= 0; i--)",
        main_("int a[]={1,2,3}; print_list(from_array(a,3));"), HEAD + TYPES + NEW + INS + PRT.replace("", ""),
        ("OK", "1 2 3"), ("OK", "3 2 1"))
r = run(BASE + main_("Item *h=NULL,*t; int i,hops=0; for(i=1;i<=5;i++){ Item*n=new_item(i,NULL); if(!h){h=n;continue;} t=h; while(t->next){t=t->next;hops++;} t->next=n; } printf(\"%d\",hops); "))
check(r == ("OK", str(int(num("C05-Q5")))), f"C05-Q5 {r}")

# ================================================================= C06
CIRC = lambda arr, start: lst("h", arr) + f"{{Item*t=h; while(t->next) t=t->next; t->next=h;}} Item*start=h; {{int k; for(k=0;k<{start};k++) start=start->next;}}\n"
r = run(BASE + main_(CIRC([2, 4, 7, 9], 0) + "Item*p=start; long k=0; while(p->next && k<100000) {p=p->next;k++;} printf(k>=100000?\"inf\":\"stops\");"))
check(r == ("OK", "inf") and mcq_text("C06-Q1").startswith("הלולאה אינסופית"), f"C06-Q1 {r}")
r = run(BASE + main_(CIRC([2, 4, 7, 9], 2) + "int s=0; Item*p=start; do{ s+=p->data; p=p->next; }while(p!=start); printf(\"%d\",s);"))
check(r == ("OK", str(int(num("C06-Q2")))), f"C06-Q2 {r}")
r = run(BASE + main_("Item a; a.data=5; a.next=&a; Item*L=&a; int c=0; while(L->data < L->next->data){L=L->next;c++;} printf(\"%d\",c);"))
check(r == ("OK", "0") and mcq_text("C06-Q3") == "אף פעם", f"C06-Q3 {r}")
r = run(BASE + main_(CIRC([3, 5, 8, 12], 1) + "Item*L=start; int c=0; while(L->data < L->next->data){L=L->next;c++;} printf(\"%d %d\",c,L->data);"))
check(r == ("OK", f"{int(num('C06-Q4'))} 12"), f"C06-Q4 {r}")
CNT = main_(CIRC([2, 4, 7, 9], 0) + "printf(\"%d \",count(start)); Item a; a.data=1; a.next=&a; printf(\"%d\",count(&a));")
findbug("C06-Q5", "    } while (p != start);", CNT, BASE, ("OK", "4 1"), ("OK", "3 1"))

# ================================================================= C07
st = Q["C07-Q1"]["step"]
REV_PRE = BASE + "Item *reverse(Item *head){ Item *prev=NULL,*curr=head;\n while(curr){\n"
REV_POST = "\n }\n return prev; }\n" + main_(lst("h", [1, 2, 3, 4]) + "print_list(reverse(h));")
perms = list(itertools.permutations(range(4)))


def try_perm(pm):
    return run(REV_PRE + "\n".join(st["lines"][i] for i in pm) + REV_POST, timeout=2)


outs = pmap(try_perm, perms)
good = [pm for pm, o in zip(perms, outs) if o == ("OK", "4 3 2 1")]
check(good == [(0, 1, 2, 3)], f"C07-Q1 exactly the stored order must work, got {good}")
r = run(BASE + main_(lst("h", [1, 2, 3, 4]) + "Item*prev=NULL,*curr=h; { Item*next=curr->next; curr->next=prev; prev=curr; curr=next; } print_list(h);"))
check(r == ("OK", mcq_text("C07-Q2")), f"C07-Q2 {r}")
EQ_DRV = "int main(void){\n"
for i, (a, b) in enumerate([([1, 2], [1, 2, 3]), ([1, 2, 3], [1, 2]), ([1, 2], [1, 2]), ([1, 3], [1, 2])]):
    EQ_DRV += lst(f"x{i}", a) + lst(f"y{i}", b) + f"printf(\"%d \",equal(x{i},y{i}));\n"
EQ_DRV += "return 0;}\n"
fillblank("C07-Q3", BASE, EQ_DRV, "0 0 1 0", {"b": ("OK", "1 1 1 0"), "c": ("OK", "1 0 1 0"), "d": ("OK", "0 1 1 0")})
CA_DRV = "int main(void){\n" + lst("s1", [7]) + lst("l1", [1, 2, 3]) + lst("s2", [1]) + lst("l2", [1, 2]) + lst("s3", [2, 1]) + lst("l3", [1, 2]) + \
    "printf(\"%d %d %d\",contains_all(s1,l1),contains_all(s2,l2),contains_all(s3,l3));\nreturn 0;}\n"
findbug("C07-Q4", "        while (p && p->data != sub->data)", CA_DRV, BASE, ("OK", "0 1 1"), None)
bad = run(BASE + "\n".join(Q["C07-Q4"]["step"]["lines"]) + CA_DRV)
check(bad[0] == "CRASH", f"C07-Q4 buggy version must crash, got {bad}")
CA = "\n".join(Q["C07-Q4"]["step"]["lines"]).replace("        while (p->data != sub->data)", "        while (p && p->data != sub->data)")
r = run(BASE + CA + main_(
    lst("l0", [1, 2]) + lst("l1", [2, 1, 3]) + lst("l2", [3]) + lst("l3", [1, 2, 3]) + lst("L", [1, 2]) +
    "Item*A[4]={l0,l1,l2,l3}; int i,c=0; for(i=0;i<4;i++) c+=contains_all(L,A[i]); printf(\"%d\",c);"))
check(r == ("OK", str(int(num("C07-Q5")))), f"C07-Q5 {r}")

# ================================================================= C08 boss: bank ids exist, are official and not in the avoid list
bank = json.load(open(ROOT / "questions.json", encoding="utf-8"))["questions"]
byid = {q["id"]: q for q in bank}
AVOID = {"23B-B", "22B-B", "22B-A", "21B-A"}
for b in LV["C08"]["questions"]:
    q = byid.get(b["bankId"])
    check(q is not None and q.get("official") and q["examCode"] not in AVOID and q.get("topic") == "linked_lists" and q.get("stepsSource") in ("ai-verified", "official"),
          f"C08 {b['bankId']} must be an official linked_lists question of a clean sitting")
# the bank solutions themselves: compile and run each reference solution against a driver
SOL = {}
for qid in ("20B-A-Q2", "20B-B-Q2", "25B-A-Q1", "25B-B-Q1"):
    sol = byid[qid]["solution"]
    SOL[qid] = "\n".join(re.findall(r"```c\n(.*?)```", sol, re.S))
d20a = HEAD + TYPES + FROM2 + PRT + SOL["20B-A-Q2"] + main_(
    lst("h", [2, 4, 7, 9]) + "{Item*t=h; while(t->next) t=t->next; t->next=h;} Item*four=h->next; Item*m=cut_cyclic_list(four); print_list(m); "
    "Item a; a.data=5; a.next=&a; Item*s=cut_cyclic_list(&a); printf(\"| %d %d\",s->data,s->next==NULL); printf(\"%d\",cut_cyclic_list(NULL)==NULL);")
check(run(d20a) == ("OK", "2 4 7 9 | 5 11"), f"C08 20B-A-Q2 reference {run(d20a)}")
d20b = HEAD + TYPES + FROM2 + PRT + SOL["20B-B-Q2"] + main_(
    lst("a0", [1, 2, 3]) + lst("a1", [1, 2]) + lst("a2", [4, 1, 2]) + lst("a3", [1, 2, 3, 4]) + lst("L", [1, 2, 3]) +
    "Item*A[4]={a0,a1,a2,a3}; Item*r=arr_of_lists_to_list_of_prefixes(A,4,L); print_list(r);")
check(run(d20b) == ("OK", "0 3"), f"C08 20B-B-Q2 reference {run(d20b)}")
d25a = HEAD + "#include <string.h>\ntypedef struct node { char value; struct node* next; } node;\n" + SOL["25B-A-Q1"] + """
static node* mk(const char* s){ node *h=NULL,**t=&h; for(;*s;s++){ *t=malloc(sizeof(node)); (*t)->value=*s; (*t)->next=NULL; t=&(*t)->next;} return h; }
int main(void){ const char*t[]={"  No  way! ","    ","","x"," a  b ",NULL}; int i; for(i=0;t[i];i++){ node*h=mk(t[i]); node*p; removeExtraSpaces(&h); printf("["); for(p=h;p;p=p->next) putchar(p->value); printf("]"); } return 0;}
"""
check(run(d25a) == ("OK", "[No way!][][][x][a b]"), f"C08 25B-A-Q1 reference {run(d25a)}")
d25b = HEAD + TYPES + FROM2 + PRT + SOL["25B-B-Q1"] + main_(
    lst("a0", [2, 6, 5, 1, 8]) + lst("a1", [8, 3, 5]) + lst("a2", [5]) + lst("a3", [1, 2, 8, 5, 3]) + lst("a4", [8, 5, 2, 8]) + lst("L", [8, 2, 5]) +
    "Item*A[5]={a0,a1,a2,a3,a4}; print_list(lists_with_given_elements(A,5,L));")
check(run(d25b) == ("OK", "0 3 4"), f"C08 25B-B-Q1 reference {run(d25b)}")

print(f"\nassertions: {COUNT[0]}, failures: {len(FAILS)}")
sys.exit(1 if FAILS else 0)
