"""Machine checks for the 19S-B steps (Q1, Q2, Q3, Q5; Q4 is mcq). Run: PYTHONUTF8=1 py tools/verify/19S-B/steps_check.py
Reads the SHIPPED tools/raw/19S-B.json; every numeric/choice/text value is re-measured with clang (Q5 with -m32)."""
import pathlib, sys, subprocess, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

C = "19S-B"
ok = True


def sol(num):
    return S.sol_blocks(C, num, None)[0]


def run32(src):
    d = pathlib.Path(tempfile.mkdtemp(prefix="stp32"))
    try:
        (d / "t.c").write_text(src, encoding="utf-8")
        p = subprocess.run([S.CLANG, "-w", "-m32", "-O0", "-o", str(d / "t.exe"), str(d / "t.c")], capture_output=True, text=True, cwd=d)
        assert p.returncode == 0, p.stderr
        r = subprocess.run([str(d / "t.exe")], capture_output=True, text=True, cwd=d, timeout=10)
        return (r.returncode, r.stdout)
    finally:
        shutil.rmtree(d, ignore_errors=True)


# ---------------- Q1
PRE1 = "#include <stdio.h>\n#include <stdlib.h>\n#include <setjmp.h>\nstatic jmp_buf JB;\n#define exit(c) longjmp(JB, 1)\n"
COPYROW = r'''void copy_row(FILE *in, FILE *out, int start_row, int *rows)
{
      char c;
      fseek(in, start_row, SEEK_SET);
      while ( (c = fgetc(in)) != ' ' )
            fputc(c, out);
      fputc('\n', out);
      (*rows)++;
}
'''
HDR = "void copy_true_false_file_rows (char *infile, char *outfile_true, char *outfile_false, int *true_rows, int *false_rows)"
MAIN1 = r'''
static void show(const char *n){ FILE*f=fopen(n,"rb"); int c; printf("[%s]",n); while((c=fgetc(f))!=EOF) putchar(c=='\n'?'/':c=='\r'?'~':c); fclose(f); puts("");}
int main(void){
 FILE *f = fopen("in.txt","wb"); fputs("ab 195\r\nxy 241\r\nq 114\r\nzz 0\r\npq 225\r\n", f); fclose(f);
 int t=-1, fl=-1;
 copy_true_false_file_rows("in.txt","t.txt","f.txt",&t,&fl);
 printf("true_rows=%d false_rows=%d\n", t, fl); show("t.txt"); show("f.txt");
 f = fopen("in2.txt","wb"); fputs("abc 294\r\n3+2+1=6 352\r\nA 65\r\n", f); fclose(f);
 copy_true_false_file_rows("in2.txt","t2.txt","f2.txt",&t,&fl);
 printf("true_rows=%d false_rows=%d\n", t, fl); show("t2.txt"); show("f2.txt");
 if(setjmp(JB)==0){ copy_true_false_file_rows("no_such.txt","t3.txt","f3.txt",&t,&fl); puts("returned"); } else puts("exit");
 return 0;}
'''
body = sol(1)
fn = body[body.index(HDR[:30]):]
rowfn = body[body.index("void copy_row"):body.index("void copy_true_false_file_rows")]
b1 = lambda L: PRE1 + "\n".join(L) + MAIN1
# reference: whole solution text (both functions)
ref_lines = body.split("\n")
it = S.Item(C, 1, None, b1, ref_lines)
print(it.ref[1])
assert it.ref[1].split("\n")[0] == "true_rows=3 false_rows=2", it.ref
assert "[t.txt]ab~/xy~/pq~/" in it.ref[1] and "[f.txt]q~/zz~/" in it.ref[1].replace("\n", ""), it.ref
assert "true_rows=2 false_rows=1" in it.ref[1] and it.ref[1].endswith("exit\n")
# fillblank is inside copy_row: build = prefix + new copy_row + main function
mainfn = body[body.index("void copy_true_false_file_rows"):]
it.build = lambda L: PRE1 + "\n".join(L) + "\n" + mainfn + MAIN1
it.fill("תנאי הלולאה")
it.build = lambda L: PRE1 + rowfn + "\n".join(L) + MAIN1
it.bug("גדול מהסכום הנכון")
ok &= it.finish()
it = S.Item(C, 1, None, b1, ref_lines)
it.order("סדרו", build=lambda B: PRE1 + rowfn + HDR + "\n{\n" + "\n".join(B) + "\n}\n" + MAIN1)
ok &= it.finish()

# ---------------- Q2
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\ntypedef struct data_item { int data; struct data_item *next; } DataItem;\ntypedef struct ptr_item { int *ptr; struct ptr_item *next; } PtrItem;\n"
MAIN2 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
static DataItem* mk(int*v,int n){DataItem*h=NULL;for(int i=n-1;i>=0;i--){DataItem*e=malloc(sizeof(DataItem));e->data=v[i];e->next=h;h=e;}return h;}
int main(void){
 int a[]={5,6,7},c[]={8,9}; DataItem*AL[3]={mk(a,3),NULL,mk(c,2)}; int*SZ=NULL; stackwipe();
 PtrItem*LA=array_of_lists_to_list_of_arrays(AL,3,&SZ); int k=0;
 for(PtrItem*p=LA;p&&k<10;p=p->next,k++){printf("item%d size=%d ptr%s:",k,SZ[k],p->ptr?"":"=NULL");for(int j=0;p->ptr&&j<SZ[k];j++)printf(" %d",p->ptr[j]);puts("");}
 printf("items=%d\n",k);
 printf("second_of_third=%d\n",LA->next->next->ptr[1]);
 return 0;}
'''
body = sol(2)
b2 = lambda L: PRE2 + "\n".join(L) + MAIN2
it = S.Item(C, 2, None, b2, body.split("\n"))
print(it.ref[1])
assert it.ref[1].split("\n")[:5] == ["item0 size=3 ptr: 5 6 7", "item1 size=0 ptr=NULL:", "item2 size=2 ptr: 8 9", "items=3", "second_of_third=9"], it.ref
it.fill("שורת ההעתקה"); it.bug("אינה מופיעה")
ok &= it.finish()
it = S.Item(C, 2, None, b2, body.split("\n"))
it.order("סדרו", build=lambda B: PRE2 + "PtrItem *array_of_lists_to_list_of_arrays (DataItem **AL, int n, int **SIZE)\n{\n" + "\n".join(B) + "\n}\n" + MAIN2)
ok &= it.finish()

# ---------------- Q3
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n"
MAIN3 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
static void t(const char*s){char buf[64];strcpy(buf,s);stackwipe();cyclic_shift_of_string(buf);printf("[%s] -> [%s]\n",s,buf);}
int main(void){ t("to be or not"); t("one  two  three   four"); t("hello"); t("a b"); t("ab  cd"); return 0;}
'''
body = sol(3)
b3 = lambda L: PRE3 + "\n".join(L) + MAIN3
it = S.Item(C, 3, None, b3, body.split("\n"))
print(it.ref[1])
assert it.ref[1].split("\n")[:5] == ["[to be or not] -> [not to be or]", "[one  two  three   four] -> [four   one  two  three]",
                                       "[hello] -> [hello]", "[a b] -> [b a]", "[ab  cd] -> [cd  ab]"], it.ref
it.fill("לולאת החיפוש"); it.bug("חסרה את התו האחרון")
ok &= it.finish()
it = S.Item(C, 3, None, b3, body.split("\n"))
it.order("סדרו", build=lambda B: PRE3 + "void cyclic_shift_of_string(char *str)\n{\n" + "\n".join(B) + "\n}\n" + MAIN3)
ok &= it.finish()

# ---------------- Q5: 32-bit
r = run32(r'''#include <stdio.h>
int main(){ int a[100];
 printf("%d\n",(int)(sizeof a));
 printf("%d\n",(int)(sizeof sizeof a));
 printf("%d", sizeof a + sizeof sizeof a + sizeof sizeof sizeof a); puts("");
 return 0;}''')
print(r)
assert r == (0, "400\n4\n408\n"), r
r64 = S.run(r'''#include <stdio.h>
int main(){ int a[100]; printf("%d", sizeof a + sizeof sizeof a + sizeof sizeof sizeof a); return 0;}''')
assert r64 == (0, "416"), r64

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
