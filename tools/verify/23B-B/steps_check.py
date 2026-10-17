"""Step-author checks for 23B-B (run after gen_23B-B.py): PYTHONUTF8=1 py tools/verify/23B-B/steps_check.py"""
import itertools, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ws_util import *  # noqa

C = "23B-B"
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
    it.bug(hint)


# ------------------------------------------------------------------ Q1
TYPE1 = "typedef struct node { int value; struct node* next; } node;\n"
CYC = """static node *cyc(int n){ node *h=NULL,*t=NULL; for(int i=1;i<=n;i++){ node *x=calloc(1,sizeof(node)); x->value=i; if(!h)h=x; else t->next=x; t=x;} t->next=h; return h; }
"""
MAIN1 = """int main(void){ int ms[]={3,2,5,10}, ns[]={8,8,1,4};
 for(int t=0;t<4;t++){ node *r=JosephusPermutation(cyc(ns[t]),ms[t]); printf("n=%d m=%d:",ns[t],ms[t]); for(;r;r=r->next)printf(" %d",r->value); printf("\\n"); }
 node *e=JosephusPermutation(NULL,3); printf("empty -> %s\\n", e?"non-NULL":"NULL"); return 0; }
"""
b1 = lambda lines: INC + TYPE1 + "\n".join(lines) + "\n" + CYC + MAIN1
ref1 = fill_ref(1, None, "מנתקת")
it = Item(C, 1, None, b1, ref1)
assert "n=8 m=3: 3 6 1 5 2 8 4 7" in it.ref[1]
it.fill("מנתקת")
check_bug(it, 1, None, ref1, "שורה אחת שונתה")
ok &= it.finish()
probe1 = INC + TYPE1 + "\n".join(ref1) + "\n" + CYC + """int main(void){ node *r=JosephusPermutation(cyc(8),2); int last=0; for(;r;r=r->next) last=r->value; printf("%d\\n",last); return 0; }"""
ok &= numeric(C, 1, None, "m = 2", probe1)
# choice: position of lst after the advance loop (m = 3, list 1..8)
out = probe(INC + TYPE1 + CYC + """int main(void){ node *lst=cyc(8); int m=3,i; for(i=0;i<m-2;i++) lst=lst->next; node *tmp=lst->next; printf("lst=%d tmp=%d\\n",lst->value,tmp->value); return 0; }""")
print("Q1 choice probe:", out.strip())
ok &= out.strip() == "lst=2 tmp=3"

# ------------------------------------------------------------------ Q2
TYPE2 = "typedef struct { char film_code[10]; int copies; int year; } film;\n"
MAIN2 = """int main(void){
 film all[5]={{"A346-f",2,1967},{"D8120-fx",4,1960},{"S516-t",1,1970},{"R11-v",2,1972},{"G555-xx",3,2010}};
 FILE *f=fopen("films.bin","wb"); fwrite(all,sizeof(film),5,f); fclose(f);
 int n; film *r=appropriateFilm("films.bin",2,1970,&n); printf("size=%d\\n",n);
 for(int i=0;i<n;i++) printf("%s %d %d\\n",r[i].film_code,r[i].copies,r[i].year);
 r=appropriateFilm("films.bin",0,1970,&n); printf("none: size=%d ptr=%s\\n",n,r?"non-NULL":"NULL");
 r=appropriateFilm("films.bin",3,1972,&n); printf("size=%d\\n",n);
 r=appropriateFilm("missing.bin",2,1970,&n); printf("missing: size=%d ptr=%s\\n",n,r?"non-NULL":"NULL");
 return 0; }
"""
b2 = lambda lines: INC + TYPE2 + "\n".join(lines) + "\n" + MAIN2
ref2 = fill_ref(2, None, "בין שני המעברים")
it = Item(C, 2, None, b2, ref2)
it.fill("בין שני המעברים")
check_bug(it, 2, None, ref2, "שורה אחת שונתה")
print(it.ref[1])
ok &= it.finish()
src2 = INC + TYPE2 + "\n".join(ref2) + "\n"
head2 = """film all[5]={{"A346-f",2,1967},{"D8120-fx",4,1960},{"S516-t",1,1970},{"R11-v",2,1972},{"G555-xx",3,2010}};
 FILE *f=fopen("films.bin","wb"); fwrite(all,sizeof(film),5,f); fclose(f);"""
ok &= numeric(C, 2, None, "copies_limit = 3", src2 + "int main(void){ " + head2 + """ int n; appropriateFilm("films.bin",3,1972,&n); printf("%d\\n",n); return 0; }""")
ok &= numeric(C, 2, None, "גודל קובץ הדוגמה", src2 + "int main(void){ " + head2 + """ f=fopen("films.bin","rb"); fseek(f,0,SEEK_END); printf("%d %d\\n",(int)sizeof(film),(int)ftell(f)); return 0; }""")

# ------------------------------------------------------------------ Q3
MAIN3 = """int main(void){
 char sentence[]="   Why?! That's why."; char sep[]="? !."; char *w=my_strtok(sentence,sep);
 while(w){ printf("\\"%s\\"\\n",w); free(w); w=my_strtok(NULL,sep); }
 printf("last call -> NULL\\n");
 char only[]="?!.  "; w=my_strtok(only,sep); printf("only separators -> %s\\n",w?w:"NULL");
 char empty[]=""; w=my_strtok(empty,sep); printf("empty sentence -> %s\\n",w?w:"NULL");
 char tail[]="abc"; w=my_strtok(tail,sep); printf("\\"%s\\"",w); w=my_strtok(NULL,sep); printf(" then %s\\n",w?w:"NULL");
 return 0; }
"""
HDR3 = "char* my_strtok(char* sentence, char* separators)"
b3f = lambda lines: INC + "\n".join(lines) + "\n" + MAIN3
ref3 = fill_ref(3, None, "קריאה הראשונה")
it = Item(C, 3, None, b3f, ref3)
it.fill("קריאה הראשונה")
check_bug(it, 3, None, ref3, "שורה אחת שונתה")
ok &= it.finish()
b3o = lambda body: INC + HDR3 + "\n{\n" + "\n".join(body) + "\n}\n" + MAIN3
s3 = find(C, 3, None, "order", "גוף הפונקציה")
it = Item(C, 3, None, b3o, s3["lines"])
it.order("גוף הפונקציה")
ok &= it.finish()
ok &= numeric(C, 3, None, "a,,b,c,", INC + "\n".join(ref3) + """
int main(void){ char s[]="a,,b,c,"; int n=0; char *w=my_strtok(s,","); while(w){ n++; w=my_strtok(NULL,","); } printf("%d\\n",n); return 0; }""")

# ------------------------------------------------------------------ Q4
q4 = question(C, 4)["question"]
code4 = re.search(r"```c\n(.*?)\n```", q4, re.S).group(1).replace("void main()", "int main()")
r = run(code4)
assert r[0] == 0, r
real = [ln.rstrip() for ln in r[1].split("\n") if ln.strip()]
print("Q4 real output:", real)
q = question(C, 4)
ok &= real == find(C, 4, None, "order", "ששת")["lines"]
for hint in ("p1 Print2", "p1 Print3"):
    s = find(C, 4, None, "choice", hint)
    for o in s["options"]:
        val = o["value"].strip("`")
        inout = val in real
        print(f"  Q4 choice[{hint}] {o['id']}{'*' if o['id'] == s['correctId'] else ' '} in real output: {inout}")
        ok &= inout == (o["id"] == s["correctId"])
# the 'why' step: p1.val2 must stay bbb after p2.val2[0]='Z' (array copied, pointer shared)
ok &= "p1 Print2: 20, bbb, Zaa" in real

# ------------------------------------------------------------------ Q6
ok &= numeric(C, 6, None, "sizeof(s)", INC + """int main(void){ char s[]={'^','^','^'^'^','^'}; printf("%d\\n",(int)sizeof(s)); return 0; }""")
ok &= numeric(C, 6, None, "s[2]", INC + """int main(void){ char s[]={'^','^','^'^'^','^'}; printf("%d\\n",s[2]); return 0; }""")
ok &= text_out(C, 6, None, "מה מודפס", INC + """int main(void){ char s[]={'^','^','^'^'^','^'}; printf("%s",s); return 0; }""")

print("ALL OK" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
