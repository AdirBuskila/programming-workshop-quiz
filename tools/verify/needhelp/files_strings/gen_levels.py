# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import LEVELS, COURSE
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "courses", COURSE)
os.makedirs(out, exist_ok=True)
for lv in LEVELS:
    s = "/* %s, level %d - %s */\nCOURSE_LEVEL(%s, %s);\n" % (COURSE, lv["order"], lv["id"], json.dumps(COURSE), json.dumps(lv, ensure_ascii=False, indent=2))
    with open(os.path.join(out, lv["id"] + ".js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
print("wrote", len(LEVELS))
