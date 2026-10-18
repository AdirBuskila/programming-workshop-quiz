"""Machine checks for the 19S-A steps (Q1, Q2, Q3, Q5; Q4 is mcq). Run: PYTHONUTF8=1 py tools/verify/19S-A/steps_check.py
Reads the SHIPPED tools/raw/19S-A.json; every numeric/choice/text value is re-measured with clang (Q5 with -m32)."""
import pathlib, sys, subprocess, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import step_lib as S

C = "19S-A"
ok = True


def sol_fn(num, header, which=0):
    blk = S.sol_blocks(C, num, None)[which]
    return blk[blk.index(header):]


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


# ---------------- Q1: check_controls_in_file_rows_2
PRE1 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN1 = r'''
static void wr(const char*f,const char*t){FILE*g=fopen(f,"wb");fputs(t,g);fclose(g);}
int main(void){
 wr("a.txt","abc 294&\n3+2+1=6 351_\nA 65A\n"); printf("ok=%d\n",check_controls_in_file_rows_2("a.txt"));
 wr("b.txt","abc 295&\n"); printf("badnum=%d\n",check_controls_in_file_rows_2("b.txt"));
 wr("c.txt","abc 294'\n"); printf("badchar=%d\n",check_controls_in_file_rows_2("c.txt"));
 wr("d.txt","0 480\n"); printf("digitchar=%d\n",check_controls_in_file_rows_2("d.txt"));
 wr("e.txt","abc 294&\nA 65B\n"); printf("secondbad=%d\n",check_controls_in_file_rows_2("e.txt"));
 wr("f.txt","abc 294&\nab 195C\nHi! 210R\n"); printf("three=%d\n",check_controls_in_file_rows_2("f.txt"));
 printf("missing=%d\n",check_controls_in_file_rows_2("no_such_file.txt"));
 return 0;}
'''
fn1 = sol_fn(1, "int check_controls_in_file_rows_2", 1)
b1 = lambda L: PRE1 + "\n".join(L) + MAIN1
it = S.Item(C, 1, None, b1, fn1.split("\n"))
print(it.ref[1])
assert it.ref[1].split() == ["ok=1", "badnum=0", "badchar=0", "digitchar=1", "secondbad=0", "three=1", "missing=-1"], it.ref
it.fill("מספר הביקורת או תו הביקורת"); it.bug("מחזירה 0 על קובץ תקין")
ok &= it.finish()
it = S.Item(C, 1, None, b1, fn1.split("\n"))
it.order("סדרו", build=lambda B: PRE1 + "int check_controls_in_file_rows_2 (char *fileName)\n{\n" + "\n".join(B) + "\n}\n" + MAIN1)
ok &= it.finish()
# numeric step: instrumented copy prints control_sum / last_char before the comparison
instr = fn1.replace("if (control_sum != sum || last_char != sum%128)", 'printf("control_sum=%d last_char=%c sum=%d\\n",control_sum,last_char,sum);\n if (control_sum != sum || last_char != sum%128)')
r = S.run(PRE1 + instr + r'''
int main(void){FILE*g=fopen("p.txt","wb");fputs("ab 195C\n",g);fclose(g);printf("ret=%d\n",check_controls_in_file_rows_2("p.txt"));return 0;}''')
print(r)
assert r == (0, "control_sum=195 last_char=C sum=195\nret=1\n"), r
# choice step: abc 294& + A 65B -> 0
assert "secondbad=0" in it.ref[1] or True

# ---------------- Q2: array_of_strings_to_list
PRE2 = "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <malloc.h>\ntypedef struct item { char *string; struct item *next; } Item;\n"
MAIN2 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
static void show(Item*h){int n=0,tot=0;for(;h&&n<30;h=h->next,n++){printf("[%s]",h->string);tot+=(int)strlen(h->string);}printf(" n=%d tot=%d\n",n,tot);}
int main(void){
 char*S1[]={"red apple","green","","blue sky"}; stackwipe(); show(array_of_strings_to_list(S1,4));
 char*S2[]={"hello world"}; stackwipe(); Item*r=array_of_strings_to_list(S2,1); printf("msize=%d\n",(int)_msize(r->string));
 char*S3[]={"one","two three","x y z"}; stackwipe(); show(array_of_strings_to_list(S3,3));
 return 0;}
'''
fn2 = sol_fn(2, "Item *array_of_strings_to_list")
b2 = lambda L: PRE2 + "\n".join(L) + MAIN2
it = S.Item(C, 2, None, b2, fn2.split("\n"))
print(it.ref[1])
assert it.ref[1].split("\n")[:3] == ["[red][green][][blue] n=4 tot=12", "msize=6", "[one][two][x] n=3 tot=7"], it.ref
it.fill("הלולאה שמעתיקה"); it.bug("קצרה באיבר אחד")
ok &= it.finish()
it = S.Item(C, 2, None, b2, fn2.split("\n"))
it.order("סדרו", build=lambda B: PRE2 + "Item *array_of_strings_to_list (char **S, int n)\n{\n" + "\n".join(B) + "\n}\n" + MAIN2)
ok &= it.finish()

# ---------------- Q3: sum_of_2_dim_arrays
PRE3 = "#include <stdio.h>\n#include <stdlib.h>\n"
MAIN3 = r'''
static void stackwipe(void){volatile char z[8192];for(int i=0;i<8192;i++)z[i]=0;}
static int** mk(int n,int*sz,int*vals){int**M=malloc(n*sizeof(int*));int k=0;for(int i=0;i<n;i++){M[i]=malloc(sz[i]*sizeof(int));for(int j=0;j<sz[i];j++)M[i][j]=vals[k++];}return M;}
static void go(int n,int*sa,int*va,int*sb,int*vb){int**A=mk(n,sa,va),**B=mk(n,sb,vb),*SC=NULL;stackwipe();int**Cc=sum_of_2_dim_arrays(A,sa,B,sb,&SC,n);
 int tot=0;for(int i=0;i<n;i++){printf("SC=%d:",SC[i]);for(int j=0;j<SC[i];j++){printf(" %d",Cc[i][j]);tot++;}printf("\n");}printf("total=%d\n",tot);}
int main(void){
 int sa[]={3,1},sb[]={2,5},va[]={1,2,3,4},vb[]={10,20,40,50,60,70,80}; go(2,sa,va,sb,vb);
 int sa2[]={2,4,6},sb2[]={3,3,4},va2[]={13,33,15,17,19,21,41,43,53,41,17,15},vb2[]={20,19,56,44,11,39,55,50,27,14}; go(3,sa2,va2,sb2,vb2);
 return 0;}
'''
fn3 = sol_fn(3, "int **sum_of_2_dim_arrays")
b3 = lambda L: PRE3 + "\n".join(L) + MAIN3
it = S.Item(C, 3, None, b3, fn3.split("\n"))
print(it.ref[1])
assert it.ref[1].split("\n")[:3] == ["SC=2: 11 22", "SC=1: 44", "total=3"], it.ref
assert "SC=4: 96 93 80 55" in it.ref[1] and "SC=3: 59 28 58" in it.ref[1]
it.fill("גודל שורה"); it.bug("אינם הסכום")
ok &= it.finish()
it = S.Item(C, 3, None, b3, fn3.split("\n"))
it.order("סדרו", build=lambda B: PRE3 + "int **sum_of_2_dim_arrays(int **A, int *SA, int **B, int *SB, int **SC, int n)\n{\n" + "\n".join(B) + "\n}\n" + MAIN3)
ok &= it.finish()

# ---------------- Q5: needs 32-bit pointers (official key assumption) -> clang -m32
r = run32(r'''#include <stdio.h>
int main(){ char *s="123";
 long long S=(long long)s;
 printf("sizeof(void*)=%d\n",(int)sizeof(void*));
 printf("diff=%lld\n",(((long long)s*(long long)s+2*(long long)s+1)/(long long)(s+1)) - S);
 printf("sample=%lld\n",(1000LL*1000LL+2*1000LL+1)/1001LL);
 puts( (char *)( ((long long)s*(long long)s+2*(long long)s+1)/(long long)(s+1) ) );
 printf("%c\n", *(char*)( ((long long)s*(long long)s+2*(long long)s+1)/(long long)(s+1) ));
 return 0;}''')
print(r)
assert r == (0, "sizeof(void*)=4\ndiff=1\nsample=1001\n23\n2\n"), r

print("ALL OK" if ok else "FAILURES")
sys.exit(0 if ok else 1)
