"""Step-author checks for 21B-A (run after gen_21B-A.py): PYTHONUTF8=1 py tools/verify/21B-A/steps_check.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ws_util import *  # noqa

C = "21B-A"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"


def fill_ref(num, part, hint):
    s = find(C, num, part, "fillblank", hint)
    lines = list(s["lines"])
    right = next(o["value"] for o in s["options"] if o["id"] == s["correctId"])
    lines[s["blankIndex"]] = lines[s["blankIndex"]].replace("___", right)
    return lines


def check_bug(it, num, part, ref, hint):
    s = find(C, num, part, "findbug", hint)
    one_line_diff(ref, s["lines"], s["bugIndex"])
    return it.bug(hint)


# ------------------------------------------------------------------ Q1
TYPE1 = "typedef struct { char first_name[30], last_name[30]; } name;\n"
MAIN1 = """#define N(a) (int)(sizeof(a)/sizeof(a[0]))
int main(void){
 name ex[]={{"Mike","Asher"},{"David","Bern"},{"Joseph","Borgman"},{"Alon","Kapulski"},{"Ilan","Mizrachi"},{"Oren","Nodel"},{"Abraham","Rosen"}};
 name byfirst[]={{"Aaron","Zed"},{"Ben","Yoni"},{"Carl","Xavi"}};
 name none[]={{"Ben","Zed"},{"Aaron","Yoni"},{"Carl","Xavi"}};
 name both[]={{"Aaron","Abel"},{"Ben","Bell"}};
 name eq[]={{"Dan","Cohen"},{"Ann","Cohen"},{"Zoe","Levi"}};
 name one[]={{"Solo","Name"}};
 printf("%d %d %d %d %d %d\\n", ordered_name_array(ex,N(ex)), ordered_name_array(byfirst,N(byfirst)), ordered_name_array(none,N(none)),
        ordered_name_array(both,N(both)), ordered_name_array(eq,N(eq)), ordered_name_array(one,N(one)));
 return 0; }
"""
b1 = lambda lines: INC + TYPE1 + "\n".join(lines) + "\n" + MAIN1
ref1 = fill_ref(1, None, "סדר יורד בשמות המשפחה")
it = Item(C, 1, None, b1, ref1)
print(it.ref[1])
assert it.ref[1] == "2 1 0 1 2 1\n"
it.fill("סדר יורד בשמות המשפחה")
r = check_bug(it, 1, None, ref1, "שורה אחת שונתה")
print("   bug output:", r[1].strip())
ok &= it.finish()
HDR1 = "int ordered_name_array(name* name_arr, int n)"
b1o = lambda body: INC + TYPE1 + HDR1 + "\n{\n" + "\n".join(body) + "\n}\n" + MAIN1
s = find(C, 1, None, "order", "גוף הפונקציה")
it = Item(C, 1, None, b1o, s["lines"])
it.order("גוף הפונקציה")
ok &= it.finish()
ok &= numeric(C, 1, None, "הזוג הראשון", INC + TYPE1 + """int main(void){
 name ex[]={{"Mike","Asher"},{"David","Bern"},{"Joseph","Borgman"},{"Alon","Kapulski"},{"Ilan","Mizrachi"},{"Oren","Nodel"},{"Abraham","Rosen"}};
 for(int i=1;i<7;i++) if(strcmp(ex[i].first_name,ex[i-1].first_name)<0){ printf("%d\\n",i); break; } return 0; }""")

# ------------------------------------------------------------------ Q2
sol2 = question(C, 2)["solution"]
sol2 = "\n".join(ln for ln in sol2.split("\n") if not ln.startswith("```"))
AUX = sol2[:sol2.index("Item *cyclic_lists_combining")]
TYPE2 = "typedef struct item { int data; struct item *next; } Item;\n"
MAIN2 = """static Item *mk(int*v,int n){ Item*h=NULL,*t=NULL; for(int i=0;i<n;i++){ Item*x=calloc(1,sizeof(Item)); x->data=v[i]; if(!h)h=x; else t->next=x; t=x;} t->next=h; return h; }
static void show(Item*c){ int k=0; printf("common=%d:",c->data); Item*p=c; do{ printf(" %d",p->data); p=p->next; k++; }while(p!=c&&k<20); printf(" (%d)\\n",k); }
int main(void){
 int a1[]={1,2,5,3}, a2[]={7,5,8}, a3[]={5}, a4[]={5,7,8}, a5[]={5,1,2}, a6[]={7,8,5};
 show(cyclic_lists_combining(mk(a1,4),mk(a2,3)));
 show(cyclic_lists_combining(mk(a3,1),mk(a2,3)));
 show(cyclic_lists_combining(mk(a1,4),mk(a3,1)));
 show(cyclic_lists_combining(mk(a1,4),mk(a4,3)));
 show(cyclic_lists_combining(mk(a5,3),mk(a6,3)));
 return 0; }
"""
b2 = lambda lines: INC + TYPE2 + AUX + "\n".join(lines) + "\n" + MAIN2
ref2 = fill_ref(2, None, "האיבר שלפני העותק")
it = Item(C, 2, None, b2, ref2)
print(it.ref[1])
assert it.ref[1].startswith("common=5: 5 3 1 2 8 7 (6)\n")
it.fill("האיבר שלפני העותק")
r = check_bug(it, 2, None, ref2, "שורה אחת שונתה")
print("   bug output:", r[1].split("\n")[0])
assert r[1].startswith("common=5: 5 3 1 2 7 (5)")
ok &= it.finish()
# numeric answers come from the real run of the shipped solution
first = it.ref[1].split("\n")[0]
length = int(first.split("(")[1].rstrip(")"))
after = int(first.split(":")[1].split()[1])
s_len = find(C, 2, None, "numeric", "כמה איברים")["answer"]
s_aft = find(C, 2, None, "numeric", "מיד אחריו")["answer"]
print(f"Q2 numeric: length shipped={s_len} real={length}; after-common shipped={s_aft} real={after}")
ok &= (s_len == length and s_aft == after)

# ------------------------------------------------------------------ Q3
MAIN3 = """int main(void){
 FILE *f=fopen("rle.txt","w"); fputs("4 2 7 4 3 3\\n2 6 1 2\\n9 1 12 3\\n3 2 18 5 0 2\\n",f); fclose(f);
 int *S,rows; int **A=file_to_sequences_in_rows("rle.txt",&S,&rows); printf("rows=%d\\n",rows);
 for(int i=0;i<rows;i++){ printf("S=%d:",S[i]); for(int j=0;j<S[i];j++)printf(" %d",A[i][j]); printf("\\n"); }
 return 0; }
"""
b3 = lambda lines: INC + "\n".join(lines) + "\n" + MAIN3
ref3 = fill_ref(3, None, "חוזרת לתחילת השורה")
it = Item(C, 3, None, b3, ref3)
print(it.ref[1])
assert it.ref[1] == "rows=4\nS=9: 4 4 7 7 7 7 3 3 3\nS=8: 2 2 2 2 2 2 1 1\nS=4: 9 12 12 12\nS=9: 3 3 18 18 18 18 18 0 0\n"
it.fill("חוזרת לתחילת השורה")
r = check_bug(it, 3, None, ref3, "שורה אחת שונתה")
print("   bug output:", repr(r[1][:40]))
ok &= it.finish()
ok &= numeric(C, 3, None, "S[3]", INC + "\n".join(ref3) + MAIN3.replace('printf("rows=%d\\n",rows);', 'printf("%d\\n",S[3]); return 0;'))
ok &= numeric(C, 3, None, "A[1][6]", INC + "\n".join(ref3) + MAIN3.replace('printf("rows=%d\\n",rows);', 'printf("%d\\n",A[1][6]); return 0;'))

# ------------------------------------------------------------------ Q5
ok &= numeric(C, 5, None, "מפורשים", INC + """int main(void){ const char s[]="|0\\0/00\\0/0|"; int z=0; for(int i=0;i<(int)sizeof(s)-1;i++) if(s[i]==0)z++; printf("%d\\n",z); return 0; }""")
ok &= numeric(C, 5, None, "לא כולל תו הסיום", INC + """int main(void){ printf("%d\\n",(int)sizeof("|0\\0/00\\0/0|")-1); return 0; }""")
ok &= numeric(C, 5, None, "sizeof", INC + """int main(void){ printf("%d\\n",(int)sizeof"|0\\0/00\\0/0|"); return 0; }""")

print("ALL OK" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
