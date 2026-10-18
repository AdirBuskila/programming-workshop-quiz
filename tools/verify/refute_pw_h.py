import json,subprocess,pathlib,hashlib,re,os,sys
CL=r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang.exe"
HERE=pathlib.Path(__file__).resolve().parent
ROOT=HERE.parents[1]
import tempfile; W=pathlib.Path(tempfile.gettempdir())/"refute_pw_work"; W.mkdir(exist_ok=True)
def load(code): return json.loads((ROOT/"tools/raw"/f"{code}.json").read_text(encoding="utf-8"))
def Q(code,num,part=None):
    for q in load(code)["questions"]:
        if q["num"]==num and q.get("part")==part: return q
def sol_code(q):
    return re.findall(r"```c\n(.*?)```",q["solution"],re.S)
def run(src,args=(),timeout=10,cwd=None,extra=()):
    h=hashlib.md5(src.encode()).hexdigest()[:10]
    c=W/f"{h}.c"; e=W/f"{h}.exe"
    if not e.exists():
        c.write_text(src,encoding="utf-8")
        r=subprocess.run([CL,"-w","-O0","-o",str(e),str(c),*extra],capture_output=True,text=True)
        if r.returncode: return "CE",r.stderr[:300]
    try:
        r=subprocess.run([str(e),*args],capture_output=True,text=True,timeout=timeout,cwd=cwd or W,errors="replace")
    except subprocess.TimeoutExpired: return "HANG",""
    return ("OK" if r.returncode==0 else "RC%d"%(r.returncode & 0xffffffff)), r.stdout
def fill(lines,idx,val):
    L=list(lines); L[idx]=val; return "\n".join(L)+"\n"
