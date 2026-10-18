"""Machine checks for the 19B-B steps (Q1, Q2, Q3, Q5; Q4 is mcq). Run: PYTHONUTF8=1 py tools/verify/19B-B/steps_check.py
Reads the SHIPPED tools/raw/19B-B.json; every numeric/choice/text value is re-measured with clang."""
import pathlib, sys, subprocess, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

C = "19B-B"
ok = True


def correct_lines(step):
    ln = list(step["lines"])
    ln[step["blankIndex"]] = ln[step["blankIndex"]].replace("___", [o for o in step["options"] if o["id"] == step["correctId"]][0]["value"])
    return ln


def sol_fn(num, header):
    """Function text of the stored solution (reference lines for Item)."""
    blk = S.sol_blocks(C, num, None)[0]
    i = blk.index(header)
    return blk[i:]


# ---------------- Q1: add_controls_in_file_rows
PRE1 = "#include <stdio.h>\n#include <stdlib.h>\n#include <setjmp.h>\nstatic jmp_buf JB;\n#define exit(c) longjmp(JB, 1)\n"
MAIN1 = r'''
static void dump(const char*f){FILE*g=fopen(f,"rb");int ch;if(!g){puts("nofile");return;}
 while((ch=fgetc(g))!=EOF){if(ch=='\n')putchar('/');else if(ch=='\r')putchar('~');else if(ch<32||ch>126)printf("<%d>",ch);else putchar(ch);}puts("");fclose(g);}
int main(void){
 FILE*f=fopen("in1.txt","wb"); fputs("abc\n3+2+1=6\nA\nHi!\n",f); fclose(f);
 add_controls_in_file_rows("in1.txt","out1.txt"); dump("out1.txt");
 if(setjmp(JB)==0){ add_controls_in_file_rows("no_such_in.txt","out2.txt"); puts("returned"); } else puts("exit");
 return 0;}
'''
FN1 = lambda L: "\n".join(L)
fn1 = sol_fn(1, "void add_controls_in_file_rows")
build_full = lambda L: PRE1 + "\n".join(L) + MAIN1
it = S.Item(C, 1, None, build_full, fn1.split("\n"))
print(it.ref[1])
assert it.ref[1].startswith("abc 294&~/3+2+1=6 351_~/A 65A~/Hi! 210R~/\n"), it.ref
assert it.ref[1].endswith("exit\n")
fb = S.find(C, 1, None, "fillblank", "שורת הכתיבה")
it.build = build_full
it.fill("שורת הכתיבה"); it.bug("מספר הביקורת בכל שורה שווה")
ok &= it.finish()
ref_blocks = S.find(C, 1, None, "order", "סדרו")["lines"]
it = S.Item(C, 1, None, build_full, fn1.split("\n"))
it.order("סדרו", build=lambda B: PRE1 + "void add_controls_in_file_rows (char *infile, char *outfile)\n{\n" + "\n".join(B) + "\n}\n" + MAIN1)
ok &= it.finish()
# numeric / text
assert sum(map(ord, "Hi!")) == 210 and chr(210 % 128) == "R"
assert "Hi! 210R" in it.ref[1].replace("~/", "")  # real run printed the Hi! line

# ---------------- Q2: sorted insertion
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\ntypedef struct item { char *string; struct item *next; } Item;\n"
MAIN2 = r'''
static void ins_all(char**s,int n,Item**pl){for(int i=0;i<n;i++)insert_string_in_sort_list(s[i],pl);}
static Item* mk(char**s,int n){Item*h=NULL,**t=&h;for(int i=0;i<n;i++){*t=malloc(sizeof(Item));(*t)->string=strdup(s[i]);(*t)->next=NULL;t=&(*t)->next;}return h;}
static void show(Item*h){int n=0;for(;h&&n<30;h=h->next,n++)printf("%s ",h->string);printf("| n=%d\n",n);}
int main(void){
 char*A0[]={"ant","cat"};char*S0[]={"bee","cat","ant","dog"};Item*L=mk(A0,2);ins_all(S0,4,&L);show(L);
 char*A1[]={"bee","dog"};char*S1[]={"cow","ant"};L=mk(A1,2);ins_all(S1,2,&L);show(L);
 char*A2[]={"ant","bee","cat","dog"};char*S2[]={"cat","bee","ant","dog","elk","cat","zoo","dog"};L=mk(A2,4);ins_all(S2,8,&L);show(L);
 char*A3[]={"ant","cat"};char*S3[]={"bee"};L=mk(A3,2);ins_all(S3,1,&L);show(L);
 L=NULL;char*S4[]={"b","a","b"};ins_all(S4,3,&L);show(L);
 return 0;}
'''
fn2 = sol_fn(2, "void insert_string_in_sort_list").split("\nvoid insert_strings_from_array")[0]
b2 = lambda L: PRE2 + "\n".join(L) + MAIN2
it = S.Item(C, 2, None, b2, fn2.split("\n"))
print(it.ref[1])
assert it.ref[1].splitlines() == ["ant bee cat dog | n=4", "ant bee cow dog | n=4", "ant bee cat dog elk zoo | n=6",
                                  "ant bee cat | n=3", "a b | n=2"], it.ref
it.fill("תנאי הלולאה"); it.bug("כל האיברים שאחריה אובדים")
ok &= it.finish()

# ---------------- Q3: sequences
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN3 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
int main(void){
 int A[]={2,4,6,1,3,8,10,5}; int *Sz=NULL,rows=-1; stackwipe();
 int**B=array_to_array_of_sequences(A,8,&Sz,&rows);
 printf("rows=%d\n",rows);for(int i=0;i<rows;i++){printf("S=%d:",Sz[i]);for(int j=0;j<Sz[i];j++)printf(" %d",B[i][j]);printf("\n");}
 int A2[]={3,7,20,12,6,9,13,1,2,7,55,31,9}; Sz=NULL; rows=-1; stackwipe();
 B=array_to_array_of_sequences(A2,13,&Sz,&rows);
 printf("rows=%d\n",rows);for(int i=0;i<rows;i++){printf("S=%d:",Sz[i]);for(int j=0;j<Sz[i];j++)printf(" %d",B[i][j]);printf("\n");}
 return 0;}
'''
fn3 = sol_fn(3, "int **array_to_array_of_sequences")
b3 = lambda L: PRE3 + "\n".join(L) + MAIN3
it = S.Item(C, 3, None, b3, fn3.split("\n"))
print(it.ref[1])
assert it.ref[1].startswith("rows=4\nS=3: 2 4 6\nS=2: 1 3\nS=2: 8 10\nS=1: 5\nrows=5\n"), it.ref
it.fill("התנאי שבודק"); it.bug("לולאה אינסופית")
ok &= it.finish()
it = S.Item(C, 3, None, b3, fn3.split("\n"))
it.order("סדרו", build=lambda B: PRE3 + "int **array_to_array_of_sequences (int *A, int n, int **S, int *prows)\n{\n" + "\n".join(B) + "\n}\n" + MAIN3)
ok &= it.finish()

# ---------------- Q5: sizeof expressions
r = S.run(r'''#include <stdio.h>
int main(){ char *s="ab";
 printf("%d\n",(int)(sizeof s[0]));
 printf("%d\n",(int)sizeof'a');
 printf("%s\n", _Generic('a', int:"int", char:"char", default:"other"));
 printf("%d\n",sizeof s[0]+sizeof s[1]-sizeof'a'-sizeof'b');
 return 0;}''')
print(r)
assert r == (0, "1\n4\nint\n-6\n"), r

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
