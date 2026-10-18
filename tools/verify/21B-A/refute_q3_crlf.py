import sys,pathlib; sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1])); from refute_pw_h import *
import random
exec(open(str(pathlib.Path(__file__).with_name('refute_q3_steps.py'))).read().split('print("sol"')[0])
for crlf in (True,False):
    print("CRLF" if crlf else "LF")
    print(" sol",[chk(src,t,crlf) for t in tests].count("P"),len(tests))
    fb=steps[2]
    for o in fb["options"]:
        s="\n".join(fb["lines"]).replace("___",o["value"])
        print("  fb",o["id"],o["value"],[("P" if chk(s,t,crlf)=="P" else "x") for t in tests[:10]])
    bs="\n".join(steps[3]["lines"])
    print("  bug on example:",chk(bs,EXROWS,crlf))
