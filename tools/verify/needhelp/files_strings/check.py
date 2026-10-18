# -*- coding: utf-8 -*-
"""Machine-check every stored answer of files_strings with clang. Run: py check.py"""
import os, subprocess, sys, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import LEVELS

CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang.exe"
PRE = ('#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n'
       'static void put(const char*n,const char*s){FILE*f=fopen(n,"wb");fputs(s,f);fclose(f);}\n'
       'typedef struct{int id;int score;}rec;\n')
Q = {}
for lv in LEVELS:
    for q in lv["questions"]:
        if "id" in q:
            Q[q["id"]] = q
work = tempfile.mkdtemp(prefix="tmp_files_strings_")
n = [0]


def run(body, decl=""):
    n[0] += 1
    src = PRE + decl + "int main(void){\n" + body + "\nreturn 0;}\n"
    c = os.path.join(work, "p%d.c" % n[0])
    e = os.path.join(work, "p%d.exe" % n[0])
    open(c, "w", encoding="utf-8").write(src)
    r = subprocess.run([CLANG, "-w", c, "-o", e], capture_output=True, text=True)
    assert r.returncode == 0, "compile failed:\n" + r.stderr + src
    r = subprocess.run([e], cwd=work, capture_output=True, timeout=10)
    return r.stdout.decode().replace("\r\n", "\n")


def stored(qid):
    q = Q[qid]
    s = q.get("step", q)
    if "options" in s:
        return [o["value"] for o in s["options"] if o["id"] == s["correctId"]][0]
    if s.get("type") == "numeric":
        return s["answer"]
    if s.get("type") == "text":
        return s["accept"][0]
    return None


def case(qid, body, out, ans, decl=""):
    got = run(body, decl)
    assert got == out, (qid, got, out)
    if qid in Q and ans is not None:
        assert stored(qid) == ans, (qid, stored(qid), ans)
    print("ok", qid)


READ = 'FILE*f=fopen("t.txt","rb");'
W = 'put("t.txt","%s");'
# C01
case("C01-Q1", 'FILE*f=fopen("nope_zz.txt","r");printf("%d",f==NULL);', "1", "`NULL`")
case("C01-Q2", 'put("t.txt","AB");FILE*f=fopen("t.txt","w");fputs("C",f);fclose(f);f=fopen("t.txt","rb");int c;while((c=fgetc(f))!=EOF)putchar(c);', "C", "`C`")
case("C01-Q3", 'put("t.txt","x1");FILE*f=fopen("t.txt","a");fprintf(f,"%d",25);fclose(f);f=fopen("t.txt","rb");int c;while((c=fgetc(f))!=EOF)putchar(c);', "x125", "x125")
case("C01-Q4", 'FILE*f=fopen("t.txt","wb");fputs("ab",f);fputc(\'c\',f);fprintf(f,"%d-%d",12,3);fclose(f);f=fopen("t.txt","rb");fseek(f,0,SEEK_END);printf("%ld",ftell(f));', "7", 7)
case("C01-Q5", 'puts("a");fputs("b",stdout);puts("c");', "a\nbc\n", None)
assert stored("C01-Q5") == 2
case("C01-Q6", 'FILE *f = fopen("out.txt", "w");if (!f) return 1;fprintf(f, "%d", 5);fclose(f);f=fopen("out.txt","rb");putchar(fgetc(f));', "5", None)
# C02
case("C02-Q1", W % "4 10 -3\\n8" + READ + 'int x,sum=0;while(fscanf(f,"%d",&x)==1)sum+=x;printf("%d",sum);', "19", 19)
case("C02-Q2", W % "5" + READ + 'int x;fscanf(f,"%d",&x);int r=fscanf(f,"%d",&x);printf("%d",r==EOF);', "1", "`EOF`")
case("C02-Q3", W % "12 abc 5" + READ + 'int x,n=0;while(fscanf(f,"%d",&x)==1)n++;printf("%d",n);', "1", 1)
case("C02-Q4", W % "red  green\\nblue" + READ + 'char w[20];int n=0;while(fscanf(f,"%19s",w)==1)n++;printf("%d",n);', "3", 3)
for op, exp in (("==", "19"), ("!=", "0"), ("<", "0"), (">", "0")):
    case("C02-Q5:" + op, W % "4 10 -3 8" + READ + 'int sum=0,x;while(fscanf(f,"%d",&x) ' + op + ' 1)sum+=x;printf("%d",sum);', exp, None)
assert Q["C02-Q5"]["step"]["correctId"] == "a" and Q["C02-Q5"]["step"]["options"][0]["value"] == "=="
case("C02-Q6", W % "abcdefg hi" + READ + 'char w[4];while(fscanf(f,"%3s",w)==1)printf("%s|",w);', "abc|def|g|hi|", "abc|def|g|hi|")
# C03
S = W % "a\\nbb\\n\\nc\\n"
case("C03-Q1", S + READ + 'int ch,n=0;while((ch=fgetc(f))!=EOF)n++;printf("%d",n);', "8", 8)
case("C03-Q2", S + READ + 'char line[20];int n=0;while(fgets(line,20,f))n++;printf("%d",n);', "4", 4)
case("C03-Q4", W % "ab\\ncd\\n" + READ + 'char buf[10];fgets(buf,10,f);printf("%d",(int)strlen(buf));', "3", 3)
case("C03-Q5", W % "abcdefgh\\n" + READ + 'char buf[10];fgets(buf,4,f);printf("%d",(int)strlen(buf));', "3", 3)
for idx, exp in (("len - 1", "2"), ("len", "3"), ("0", "0"), ("1", "1")):
    case("C03-Q6:" + idx, 'char line[20]="hi\\n";size_t len=strlen(line);if(len>0&&line[len-1]==\'\\n\')line[' + idx + ']=0;printf("%d",(int)strlen(line));', exp, None)
assert Q["C03-Q6"]["step"]["options"][0]["value"] == "len - 1" and Q["C03-Q3"]["options"][0]["value"] == "`int ch;`"
# C04
case("C04-Q1", W % "1 2 3 " + READ + 'int x=0,n=0;while(!feof(f)){fscanf(f,"%d",&x);n++;}printf("%d",n);', "4", 4)
case("C04-Q2", W % "1 2 3" + READ + 'int x=0,n=0;while(!feof(f)){fscanf(f,"%d",&x);n++;}printf("%d",n);', "3", 3)
case("C04-Q3", W % "a\\nb\\n" + READ.replace('"rb"', '"r"') + 'char line[10];int n=0;while(!feof(f)){fgets(line,10,f);n++;fputs(line,stdout);}printf("%d",n);', "a\nb\nb\n3", 3)
case("C04-Q4", W % "ab" + READ + 'fgetc(f);fgetc(f);printf("%d",feof(f)!=0);', "0", "ערך שקר (0), כי עוד לא ניסו לקרוא מעבר לסוף")
base = W % "1 2 3 " + READ + 'int x=0;'
case("C04-Q5:a", base + 'while(fscanf(f,"%d",&x)==1)printf("%d ",x);', "1 2 3 ", None)
case("C04-Q5:b", base + 'while(!feof(f)){fscanf(f,"%d",&x);printf("%d ",x);}', "1 2 3 3 ", None)
case("C04-Q5:c", base + 'do{fscanf(f,"%d",&x);printf("%d ",x);}while(!feof(f));', "1 2 3 3 ", None)
case("C04-Q5:d", base + 'while(feof(f)==0){fscanf(f,"%d",&x);printf("%d ",x);}', "1 2 3 3 ", None)
assert Q["C04-Q5"]["options"][0]["value"].startswith("`while (fscanf")
case("C04-Q6", W % "hey" + READ + 'int ch=fgetc(f);while(ch!=EOF){putchar(ch);ch=fgetc(f);}', "hey", None)
# C05
WR = ('rec r;FILE*f=fopen("r.bin","wb");int ids[]={1,2,3,4,5},sc[]={50,90,70,95,60},i;'
      'for(i=0;i<5;i++){r.id=ids[i];r.score=sc[i];fwrite(&r,sizeof(r),1,f);}fclose(f);f=fopen("r.bin","rb");')
case("C05-Q1:ok", 'rec r={7,8};FILE*f=fopen("r.bin","wb");fwrite(&r,sizeof(r),1,f);fclose(f);f=fopen("r.bin","rb");fseek(f,0,SEEK_END);printf("%d",(long)ftell(f)==(long)sizeof(rec));', "1", None)
case("C05-Q1:short", 'rec r={7,8};FILE*f=fopen("r.bin","wb");fwrite(&r,sizeof(r.id),1,f);fclose(f);f=fopen("r.bin","rb");fseek(f,0,SEEK_END);printf("%d",(long)ftell(f)==(long)sizeof(rec));', "0", None)
assert Q["C05-Q1"]["options"][0]["value"] == "`fwrite(&r, sizeof(r), 1, f);`"
r = subprocess.run([CLANG, "-fsyntax-only", "-x", "c", "-"], input=PRE + 'int main(){rec r;FILE*f=0;fwrite(r,sizeof(r),1,f);}', capture_output=True, text=True)
assert r.returncode != 0, "fwrite(r,...) must not compile"
case("C05-Q2", WR + 'rec a;int count=0;while(fread(&a,sizeof(a),1,f)==1)if(a.score>=70)count++;printf("%d",count);', "3", 3)
case("C05-Q3", WR.replace("i<5", "i<2") + 'rec a;int n=0;for(i=0;i<3;i++)n=(int)fread(&a,sizeof(a),1,f);printf("%d",n);', "0", 0)
case("C05-Q4", 'int v[2]={7,1234567},i;long fw[2],fp[2];for(i=0;i<2;i++){FILE*f=fopen("a.bin","wb");fwrite(&v[i],sizeof(int),1,f);fclose(f);f=fopen("a.bin","rb");fseek(f,0,SEEK_END);fw[i]=ftell(f);fclose(f);f=fopen("b.bin","wb");fprintf(f,"%d",v[i]);fclose(f);f=fopen("b.bin","rb");fseek(f,0,SEEK_END);fp[i]=ftell(f);fclose(f);}printf("%d %d",fw[0]==fw[1],fp[0]<fp[1]);', "1 1", None)
assert Q["C05-Q4"]["options"][0]["value"].startswith("ב-`fwrite")
APT = 'typedef struct{char address[30];int rooms;int price;}apartment;\n'


def apt(cond):
    return ('apartment a;int rs[]={3,2,3,4},ps[]={500,400,900,300},i;FILE*g=fopen("a.bin","wb");for(i=0;i<4;i++){strcpy(a.address,"x");a.rooms=rs[i];a.price=ps[i];fwrite(&a,sizeof(a),1,g);}fclose(g);'
            'int rooms=3,max_price=600,count=0;FILE*f=fopen("a.bin","rb");while(fread(&a,sizeof(apartment),1,f)==1)if(' + cond + ')count++;printf("%d",count);')


case("C05-Q5:ok", apt("a.rooms == rooms && a.price <= max_price"), "1", None, APT)
case("C05-Q5:bug", apt("a.rooms == rooms || a.price <= max_price"), "4", None, APT)
bl = Q["C05-Q5"]["step"]
assert "||" in bl["lines"][bl["bugIndex"]]
case("C05-Q6", WR + 'rec a;while(fread(&a,sizeof(a),1,f)==1)printf("%d\\n",a.id);', "1\n2\n3\n4\n5\n", None)
# C06
ABC = W % "ABCDEFGH" + READ
case("C06-Q1", ABC + 'fgetc(f);fgetc(f);fgetc(f);printf("%ld",ftell(f));', "3", 3)
case("C06-Q2", ABC + 'fseek(f,2,SEEK_SET);putchar(fgetc(f));', "C", "C")
case("C06-Q3", ABC + 'fseek(f,0,SEEK_END);printf("%ld",ftell(f));', "8", 8)
case("C06-Q4", WR + 'rec a;fseek(f,2*sizeof(rec),SEEK_SET);fread(&a,sizeof(a),1,f);printf("%d",a.id);', "3", None)
case("C06-Q4:wrong", WR + 'rec a;int i2=2;fseek(f,(i2+1)*sizeof(rec),SEEK_SET);fread(&a,sizeof(a),1,f);printf("%d",a.id);', "4", None)
assert Q["C06-Q4"]["options"][0]["value"] == "`fseek(f, i * sizeof(rec), SEEK_SET);`"
case("C06-Q5", ABC + 'fgetc(f);fgetc(f);fseek(f,1,SEEK_CUR);putchar(fgetc(f));', "D", "D")
case("C06-end", ABC + 'fseek(f,-1,SEEK_END);putchar(fgetc(f));', "H", None)


def two(mid):
    return WR + 'rec a,*arr;int n=0,k=0,s=0;while(fread(&a,sizeof(a),1,f)==1)n++;' + mid + 'arr=(rec*)calloc(n,sizeof(rec));while(fread(&a,sizeof(a),1,f)==1)arr[k++]=a;for(i=0;i<n;i++)s+=arr[i].id;printf("%d",s);'


case("C06-Q6:ok", two("rewind(f);"), "15", None)
case("C06-Q6:bug", two("fseek(f,0,SEEK_END);"), "0", None)
bl = Q["C06-Q6"]["step"]
assert "SEEK_END" in bl["lines"][bl["bugIndex"]]
# C07
LV = W % "live lives alive live" + READ
case("C07-Q1", LV + 'char buf[101];int count=0;while(fscanf(f,"%100s",buf)==1)if(strstr(buf,"live"))count++;printf("%d",count);', "4", 4)
case("C07-Q1:strcmp", LV + 'char buf[101];int count=0;while(fscanf(f,"%100s",buf)==1)if(strcmp(buf,"live")==0)count++;printf("%d",count);', "2", None)
case("C07-Q2", W % "1234567890123" + READ + 'char id[10];fscanf(f,"%9s",id);printf("%s",id);', "123456789", "123456789")
HU = ('int hu(const char *s){int seen[26]={0},i,k;for(i=0;s[i];i++){if(!isalpha((unsigned char)s[i]))return 0;k=tolower((unsigned char)s[i])-\'a\';if(seen[k])return 0;seen[k]=1;}return 1;}\n')
case("C07-Q3", 'printf("%d%d%d%d",hu("Table"),hu("Alisa"),hu("ab#c"),hu("Noon"));', "1000", None, HU)
assert Q["C07-Q3"]["options"][0]["value"] == "`Table`"
case("C07-Q4", W % "abcd\\nab\\nabcde\\nx\\n" + 'FILE*in=fopen("t.txt","r"),*out=fopen("o.txt","w");char line[101];while(fgets(line,101,in)){size_t len=strlen(line);if(len>0&&line[len-1]==\'\\n\')line[len-1]=0;if(strlen(line)>3)fprintf(out,"%s\\n",line);}fclose(in);fclose(out);in=fopen("o.txt","r");int n=0;while(fgets(line,101,in))n++;printf("%d",n);', "2", 2)
CD = 'typedef struct{char id[10];char name[31];double total;}clientData;\n'


def t2b(sz):
    return (W % "06842151 Moshe 71.25\\n330578795 Benjamin 1755.65\\n" + 'clientData c;FILE*in=fopen("t.txt","r"),*out=fopen("o.bin","wb");while(fscanf(in,"%9s%30s%lf",c.id,c.name,&c.total)==3)fwrite(&c,' + sz + ',1,out);fclose(out);out=fopen("o.bin","rb");fseek(out,0,SEEK_END);printf("%d",(int)(ftell(out)==2*(long)sizeof(clientData)));')


case("C07-Q5:ok", t2b("sizeof(clientData)"), "1", None, CD)
case("C07-Q5:bug", t2b("sizeof(c.id)"), "0", None, CD)
bl = Q["C07-Q5"]["step"]
assert "c.id" in bl["lines"][bl["bugIndex"]]
case("C07-Q6", W % "x\\nyz\\n" + 'FILE *in = fopen("t.txt", "r"), *out = fopen("o.txt", "wb");char line[101];if (!in || !out) return 1;while (fgets(line, 101, in))    fputs(line, out);fclose(in); fclose(out);in=fopen("o.txt","rb");int c;while((c=fgetc(in))!=EOF)putchar(c);', "x\nyz\n", None)
shutil.rmtree(work, ignore_errors=True)
print("ALL OK")
