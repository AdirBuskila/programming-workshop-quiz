"""Step-author checks for 22B-A (run after gen_22B-A.py): PYTHONUTF8=1 py tools/verify/22B-A/steps_check.py"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ws_util import *  # noqa

C = "22B-A"
ok = True
INC = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n"


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
MAIN1 = """int main(void){ char *r; char *a[]={"ab","x","abc","q"}, *m[]={"-","yy","","-+"}; int t[]={3,1,4,2};
 for(int i=0;i<4;i++){ r=duplicateString(a[i],m[i],t[i]); printf("[%s] %d\\n",r,(int)strlen(r)); } return 0; }
"""
b1 = lambda lines: INC + "\n".join(lines) + "\n" + MAIN1
ref1 = fill_ref(1, None, "כותרת הלולאה")
it = Item(C, 1, None, b1, ref1)
print(it.ref[1])
assert it.ref[1].startswith("[ab-ab-ab] 8\n[x] 1\n[abcabcabcabc] 12\n[q-+q] 4")
it.fill("כותרת הלולאה")
r = check_bug(it, 1, None, ref1, "שורה אחת שונתה")
print("   bug output:", r[1].split("\n")[0])
assert r[1].split("\n")[0] == "[ab-ab--] 7" or "ab-ab--" in r[1]
ok &= it.finish()
HDR1 = "char* duplicateString(char* base, char* middle, int times)"
b1o = lambda body: INC + HDR1 + "\n{\n" + "\n".join(body) + "\n}\n" + MAIN1
s = find(C, 1, None, "order", "גוף הפונקציה")
it = Item(C, 1, None, b1o, s["lines"])
it.order("גוף הפונקציה")
ok &= it.finish()
ok &= numeric(C, 1, None, "strlen", INC + "\n".join(ref1) + """
int main(void){ char *r=duplicateString("ab","-",3); printf("%d\\n",(int)strlen(r)); return 0; }""")
ok &= numeric(C, 1, None, "calloc", """#include <stdio.h>
#include <string.h>
int main(void){ int times=3; printf("%d\\n",(int)(times*strlen("ab")+(times-1)*strlen("-")+1)); return 0; }""")

# ------------------------------------------------------------------ Q2
TYPE2 = """typedef struct item { int data; struct item* next; } Item;
int countDigit(int number){ int j=0; while(number){ ++j; number/=10; } return j; }
"""
MAIN2 = """static Item *mk(int M){ char buf[20]; sprintf(buf,"%d",M); Item *h=NULL,*t=NULL; for(char*c=buf;*c;c++){ Item*x=calloc(1,sizeof(Item)); x->data=*c-'0'; if(!h)h=x; else t->next=x; t=x;} return h; }
int main(void){ int Ms[]={9994,5,99,1,10}, Ns[]={18,4,1,999,5};
 for(int t=0;t<5;t++){ Item *h=mk(Ms[t]); List_num_add(h,Ns[t]); printf("%d+%d:",Ms[t],Ns[t]); for(Item*p=h;p;p=p->next)printf(" %d",p->data); printf("\\n"); }
 return 0; }
"""
b2 = lambda lines: INC + TYPE2 + "\n".join(lines) + "\n" + MAIN2
ref2 = fill_ref(2, None, "הספרה שנכתבת")
it = Item(C, 2, None, b2, ref2)
print(it.ref[1])
assert it.ref[1] == "9994+18: 1 0 0 1 2\n5+4: 9\n99+1: 1 0 0\n1+999: 1 0 0 0\n10+5: 1 5\n"
it.fill("הספרה שנכתבת")
r = check_bug(it, 2, None, ref2, "שורה אחת שונתה")
print("   bug output:", r[1].split("\n")[0])
ok &= it.finish()
HDR2 = "void List_num_add(Item* head, int N)"
b2o = lambda body: INC + TYPE2 + HDR2 + "\n{\n" + "\n".join(body) + "\n}\n" + MAIN2
s = find(C, 2, None, "order", "גוף הפונקציה")
it = Item(C, 2, None, b2o, s["lines"])
it.order("גוף הפונקציה")
ok &= it.finish()
ok &= numeric(C, 2, None, "כמה איברים צריך", INC + TYPE2 + """int main(void){ printf("%d\\n", countDigit(9994+18)-countDigit(9994)); return 0; }""")
# choice: inserting a new head inside the function (head passed by value) is invisible to the caller
out = probe(INC + TYPE2 + """
void add_at_head(Item* head, int N){ Item *x=calloc(1,sizeof(Item)); x->data=1; x->next=head; head=x; (void)N; }
int main(void){ Item *a=calloc(1,sizeof(Item)); a->data=9; add_at_head(a,18); int n=0; for(Item*p=a;p;p=p->next)n++; printf("%d\\n",n); return 0; }""")
print("Q2 choice probe (caller's list length after head insert, was 1):", out.strip())
ok &= out.strip() == "1"

# ------------------------------------------------------------------ Q3
TYPE3 = "typedef struct { char address[30]; int rooms; int price; } apartment;\n"
MAIN3 = """int main(void){
 apartment all[6]={{"Begin 7",3,700000},{"Reznik 4",4,1000000},{"Ben-Gurion 27",5,4000000},{"Dubnov 13",3,1100000},{"Cohen 66",3,900000},{"Eq 1",3,1000000}};
 FILE *f=fopen("ap.bin","wb"); fwrite(all,sizeof(apartment),6,f); fclose(f);
 int n; apartment *r=appropriateAppartment("ap.bin",3,1000000,&n); printf("size=%d\\n",n);
 for(int i=0;i<n;i++) printf("%s %d %d\\n",r[i].address,r[i].rooms,r[i].price);
 r=appropriateAppartment("ap.bin",9,1000000,&n); printf("none: size=%d ptr=%s\\n",n,r?"non-NULL":"NULL");
 r=appropriateAppartment("missing.bin",3,1000000,&n); printf("missing: size=%d ptr=%s\\n",n,r?"non-NULL":"NULL");
 return 0; }
"""
b3 = lambda lines: INC + TYPE3 + "\n".join(lines) + "\n" + MAIN3
ref3 = fill_ref(3, None, "בין שני המעברים")
it = Item(C, 3, None, b3, ref3)
print(it.ref[1])
assert it.ref[1].startswith("size=3\nBegin 7 3 700000\nCohen 66 3 900000\nEq 1 3 1000000\n")
it.fill("בין שני המעברים")
r = check_bug(it, 3, None, ref3, "שורה אחת שונתה")
print("   bug output:", repr(r[1][:80]))
ok &= it.finish()
head3 = """apartment all[5]={{"Begin 7",3,700000},{"Reznik 4",4,1000000},{"Ben-Gurion 27",5,4000000},{"Dubnov 13",3,1100000},{"Cohen 66",3,900000}};
 FILE *f=fopen("ap.bin","wb"); fwrite(all,sizeof(apartment),5,f); fclose(f);"""
ok &= numeric(C, 3, None, "room_number = 3", INC + TYPE3 + "\n".join(ref3) + "\nint main(void){ " + head3 + """ int n; appropriateAppartment("ap.bin",3,1100000,&n); printf("%d\\n",n); return 0; }""")
ok &= numeric(C, 3, None, "sizeof(apartment)", INC + TYPE3 + """int main(void){ printf("%d\\n",(int)sizeof(apartment)); return 0; }""")

# ------------------------------------------------------------------ Q5
PRE5 = INC + "int main(void){ int z='z'-1; "
ok &= numeric(C, 5, None, "אחרי", PRE5 + """printf("%d\\n",z); return 0; }""")
ok &= numeric(C, 5, None, "הביטוי `(z^1)-z`", PRE5 + """printf("%d\\n",(z^1)-z); return 0; }""")
ok &= numeric(C, 5, None, "pow", PRE5 + """printf("%d\\n",(int)pow((z^1)-z,z<<1)); return 0; }""")
ok &= text_out(C, 5, None, "מה מודפס", PRE5 + """putchar(z-(int)pow((z^1)-z,z<<1)); return 0; }""")

print("ALL OK" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
