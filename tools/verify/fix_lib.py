# Shared helper for the refuter-fix checks: build a C variant from ordered blocks, run it, compare to the reference.
import itertools, os, subprocess, tempfile, pathlib
CLANG = r"C:\Users\Adir\AppData\Local\Programs\Swift\Toolchains\6.1.0+Asserts\usr\bin\clang"
PRE = r"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
static unsigned long long rs=88172645463325252ULL;
static unsigned rnd(void){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return (unsigned)(rs>>11);}
"""
TMP = pathlib.Path(tempfile.gettempdir()) / "fixcheck"
TMP.mkdir(exist_ok=True)


def run(func_src, driver, tag="v"):
    c = TMP / f"{tag}.c"
    exe = TMP / f"{tag}.exe"
    c.write_text(PRE + func_src + "\n" + driver, encoding="utf-8")
    if exe.exists():
        exe.unlink()
    p = subprocess.run([CLANG, "-w", "-O0", str(c), "-o", str(exe)], capture_output=True, text=True)
    if p.returncode:
        return ("COMPILE-ERROR", p.stderr[:200])
    try:
        r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        return ("TIMEOUT", "")
    return (r.returncode, r.stdout)


def check_swaps(blocks, driver, label):
    """blocks: list of source lines in solution order. Every pair swap must change (output, status)."""
    ref = run("\n".join(blocks), driver, "ref")
    assert ref[0] == 0, (label, ref)
    bad = []
    for i, j in itertools.combinations(range(len(blocks)), 2):
        b = list(blocks)
        if b[i].strip() == b[j].strip():
            bad.append((i, j, "identical text"))
            continue
        b[i], b[j] = b[j], b[i]
        v = run("\n".join(b), driver, "sw")
        if v == ref:
            bad.append((i, j, "same output"))
    print(f"{label}: {len(blocks)} blocks, {len(blocks)*(len(blocks)-1)//2} swaps, unforced: {bad or 'none'}")
    return ref, bad


def check_variant(blocks, idx, new, driver, label, must_differ=True):
    ref = run("\n".join(blocks), driver, "ref")
    b = list(blocks)
    b[idx] = new
    v = run("\n".join(b), driver, "var")
    print(f"{label}: {'DIFFERS' if v != ref else 'SAME'} ({v[0]}) {new.strip()}")
    return v != ref
