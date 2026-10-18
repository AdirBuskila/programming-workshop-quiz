# -*- coding: utf-8 -*-
"""dyn_2d guided course: AUTHORS courses/dyn_2d/C01..C08.js and MACHINE-CHECKS every stored answer with clang.
Run:  PYTHONUTF8=1 py tools/verify/needhelp/dyn_2d/check.py      (from the app root)
Every mcq/numeric/order/fillblank/findbug answer is recomputed by compiling and running C; the files are only written
when every assertion holds."""
import html, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lib import *  # noqa

ROOT = HERE.parents[3]
OUT = ROOT / "courses" / "dyn_2d"
E = html.escape
FL = ("-Werror=incompatible-pointer-types", "-Werror=int-conversion")


def pre(code):
    return "<pre><code>" + E(code.strip("\n"), quote=False) + "</code></pre>"


def fence(code):
    return "```c\n" + code.strip("\n") + "\n```"


def idx(opts, text):
    return [o.strip("`") for o in opts].index(text)


ALLOC = '''int **alloc_matrix(int rows, int cols)
{
    int i;
    int **m = (int **)calloc(rows, sizeof(int *));
    for (i = 0; i < rows; i++)
        m[i] = (int *)calloc(cols, sizeof(int));
    return m;
}
'''
FREEM = '''void free_matrix(int **m, int rows)
{
    int i;
    for (i = 0; i < rows; i++)
        free(m[i]);
    free(m);
}
'''


# =============================================================== C01
def c01():
    qs = []
    tn = PRE + '#define TN(x) _Generic((x), int: "int", int *: "int *", int **: "int **", int ***: "int ***", default: "other")\nint main(void){ int **m = NULL; printf("%s", TN(m[1])); return 0; }\n'
    o = ["`int`", "`int *`", "`int **`", "`int ***`"]
    qs.append(mcq("C01-Q1", "מגדירים `int **m;` ו-`m` מצביע על מערך מצביעים שהוקצה. מהו הטיפוס של הביטוי `m[1]`?", o, 1,
        "`m` הוא `int **`, ו-`m[1]` הוא איבר אחד במערך המצביעים, כלומר `int *`: כתובת של שורה שלמה. `int` הוא רק `m[1][j]`, אחרי שני אינדקסים. `int **` הוא `m` עצמו, ו-`int ***` הוא `&m`.",
        "אינדקס אחד על `int **` נותן שורה (`int *`), שני אינדקסים נותנים איבר (`int`).",
        lambda: idx(o, ok_out(tn))))
    body = ['    int **m = (int **)calloc(2, sizeof(int *));', '    int i, j;', '    for (i = 0; i < 2; i++)', '    {',
            '        m[i] = (int *)calloc(3, sizeof(int));', '        for (j = 0; j < 3; j++)', '            m[i][j] = i * 10 + j;', '    }',
            '    printf("%d %d", m[1][2], *(*m + 1));']
    code = main_of("", body)
    o = ["`12 10`", "`12 1`", "`2 1`", "`21 1`"]
    qs.append(mcq("C01-Q2", "מה מדפיס הקוד? (כל ההקצאות מצליחות)\n" + fence(code), o, 1,
        "האיבר בשורה 1 ובעמודה 2 הוא `1 * 10 + 2 = 12`. הביטוי `*m` הוא `m[0]`, כלומר שורה 0, ו-`*(*m + 1)` הוא `m[0][1] = 0 * 10 + 1 = 1`. הפלט `12 10` מתעלם מכך ש-`m[0][1]` הוא 1 ולא 10. `2 1` ו-`21 1` מחליפים ספרות או אינדקסים.",
        "`m[i][j]` שווה ל-`*(*(m + i) + j)`.",
        lambda: idx(o, ok_out(PRE + code))))
    cnt = PRE + '''static int cnt = 0;
static void *C(size_t n, size_t s) { cnt++; return calloc(n, s); }
#define calloc C
''' + ALLOC + 'int main(void){ alloc_matrix(4, 5); printf("%d", cnt); return 0; }\n'
    ans = int(ok_out(cnt))
    qs.append(numeric("C01-Q3", "כמה קריאות להקצאה (`calloc`) נדרשות כדי לבנות מטריצה דינמית עם 4 שורות ו-5 עמודות?", ans,
        "קריאה אחת למערך המצביעים ועוד קריאה לכל שורה: $1 + 4 = 5$. אין קריאה אחת לכל התאים.", "מטריצה עם $r$ שורות = $r + 1$ הקצאות."))
    sz = PRE + 'int main(void){ printf("%d %d", (int)sizeof(int *), (int)sizeof(int)); return 0; }\n'
    a, b = map(int, ok_out(sz).split())
    assert (a, b) == (8, 4)
    o = ["`2`", "`4`", "`8`", "`16`"]
    qs.append(mcq("C01-Q4", "בהידור ל-64 סיביות, כמה בתים תופס מצביע, כלומר מהו `sizeof(int *)`?", o, 2,
        "במחשב 64 סיביות כל כתובת היא 8 בתים. הערך 4 הוא `sizeof(int)` ולא גודל מצביע. לכן מערך של $r$ מצביעים דורש $8r$ בתים, ולא $4r$.",
        "מצביע = 8 בתים ב-64 סיביות; `int` = 4 בתים.", lambda: idx(o, str(a))))
    lines = ["int **m = (int **)calloc(3, sizeof(int *));", "int i, j;", "for (i = 0; i < 3; i++)", "{",
             "    m[i] = (int *)calloc(3, sizeof(int));", "    for (j = 0; j < 3; j++)", "        m[i][j] = i * 3 + j;", "}",
             "for (i = 0; i < 3; i++)", "{", "    for (j = 0; j < 3; j++)", "        printf(\"%d \", m[j][i]);", "    printf(\"\\n\");", "}"]
    qs.append(findbug("C01-Q5", "הקוד אמור להדפיס את המטריצה שורה אחר שורה: `0 1 2` ואז `3 4 5` ואז `6 7 8`. מצאו את השורה השגויה.",
        lines, 11, "        printf(\"%d \", m[i][j]);",
        lambda L: PRE + "int main(void)\n{\n" + "\n".join("    " + l for l in L) + "\n    return 0;\n}\n",
        "האינדקס הראשון הוא השורה והשני העמודה. `m[j][i]` מחליף ביניהם, ולכן מודפסת המטריצה המשוחלפת (`0 3 6` בשורה הראשונה).",
        "`m[i][j]`: קודם שורה (`i`), אחר כך עמודה (`j`)."))
    lesson = '''
    <p>מטריצה דינמית אינה בלוק אחד. היא <b>מערך של מצביעים</b>, וכל מצביע מראה על שורה שהוקצתה בנפרד. את המערך החיצוני מחזיקים במצביע מסוג <code>int **</code>.</p>
    <pre><code>m ──► [ m[0] ][ m[1] ][ m[2] ]     (int **)
         │        │        └──► [ . . . . ]   row 2
         │        └───────────► [ . . . . ]   row 1
         └────────────────────► [ . . . . ]   row 0</code></pre>
    <ul>
      <li><code>m[i]</code> הוא מצביע <code>int *</code> לשורה <code>i</code>.</li>
      <li><code>m[i][j]</code> הוא האיבר בשורה <code>i</code> ובעמודה <code>j</code>, מסוג <code>int</code>. זה שקול ל-<code>*(*(m + i) + j)</code>.</li>
      <li>ב-64 סיביות <code>sizeof(int *)</code> הוא 8 בתים, ו-<code>sizeof(int)</code> הוא 4.</li>
    </ul>
    <div class="lesson-rule">🔑 אינדקס אחד על <code>int **</code> נותן שורה. שני אינדקסים נותנים איבר. ומטריצה עם $r$ שורות דורשת $r+1$ הקצאות: אחת למערך המצביעים ועוד אחת לכל שורה.</div>
    <div class="lesson-ex">דוגמה: אחרי הבנייה של מטריצה 2×3 עם <code>m[i][j] = i * 10 + j</code> מתקבל <code>m[0] = {0, 1, 2}</code> ו-<code>m[1] = {10, 11, 12}</code>. אז <code>m[1][2]</code> הוא 12, וגם <code>*(*m + 1)</code> הוא <code>m[0][1]</code>, כלומר 1.</div>
    <div class="lesson-trap">⚠️ <code>m[j][i]</code> במקום <code>m[i][j]</code> מדפיס את המטריצה המשוחלפת, ובמטריצה לא ריבועית גם קורא מחוץ לגבולות.</div>'''
    return dict(id="C01", order=1, icon="🧱", title="מערך של מצביעים: int **", goal="אחרי השלב הזה אפשר להסביר מה מטריצה דינמית היא בזיכרון, מה הטיפוס של m, של m[i] ושל m[i][j], וכמה הקצאות היא דורשת.", lesson=lesson, questions=qs)


# =============================================================== C02
def c02():
    qs = []
    main_blocks = ["int **m = alloc_matrix(2, 3);", "m[1][2] = 7;", "printf(\"%d\", m[1][2]);", "return 0;"]
    qs.append(order("C02-Q1", "הפונקציה `alloc_matrix` כבר כתובה. סדרו את הפקודות ב-`main` כך שתוקצה מטריצה, יוכנס 7 לשורה 1 עמודה 2, והערך יודפס.",
        main_blocks, lambda B: PRE + ALLOC + "int main(void)\n{\n" + "\n".join("    " + b for b in B) + "\n}\n",
        "קודם מקצים (בלי מטריצה אין לאן לכתוב), אחר כך כותבים, אחר כך קוראים ומדפיסים, ורק בסוף `return`.",
        "הקצאה, כתיבה, שימוש, ואז `return`."))
    # Observable, UB-free: each option is run through the logging allocator and the bytes it REQUESTS are compared
    # with the 24 bytes (3 pointers, 64-bit) the question asks for. Nothing is written into the block.
    o = ["`calloc(3, sizeof(int *))`", "`calloc(3, sizeof(int))`", "`calloc(4, sizeof(int))`", "`calloc(3, 3 * sizeof(int *))`"]
    calls = ["calloc(3, sizeof(int *))", "calloc(3, sizeof(int))", "calloc(4, sizeof(int))", "calloc(3, 3 * sizeof(int *))"]
    need = 3 * 8

    def v():
        for flags in (("-w",), ("-w", "-O2")):
            got = []
            for c in calls:
                log = ok_out(LOG + "int main(void){ void *p = " + c + "; free(p); return 0; }\n", flags)
                (n, s), = [(int(x), int(y)) for x, y in re.findall(r"\[calloc (\d+) x (\d+)\]", log)]
                got.append(n * s)
            assert got == [24, 12, 16, 72], got
            good = [i for i, g in enumerate(got) if g == need]
            assert len(good) == 1
        return good[0]
    qs.append(mcq("C02-Q2", "צריך להקצות את מערך המצביעים של מטריצה עם 3 שורות ו-4 עמודות, ב-64 סיביות, בגודל של בדיוק מצביע אחד לכל שורה. איזו קריאה מבקשת בדיוק את הכמות הזאת?", o, 0,
        "שלוש שורות = שלושה מצביעים = $3 \\cdot 8 = 24$ בתים, וזה `calloc(3, sizeof(int *))`. `calloc(3, sizeof(int))` מבקשת $3 \\cdot 4 = 12$ בתים, `calloc(4, sizeof(int))` מבקשת $4 \\cdot 4 = 16$, ו-`calloc(3, 3 * sizeof(int *))` מבקשת $3 \\cdot 24 = 72$. רק הראשונה מבקשת בדיוק 24 (נבדק עם מקצה מתעד).",
        "למערך המצביעים: מספר השורות כפול `sizeof(int *)`.", v))
    lines = ["int **alloc_matrix(int rows, int cols)", "{", "    int i;", "    int **m = (int **)calloc(rows, ___);",
             "    for (i = 0; i < rows; i++)", "        m[i] = (int *)calloc(cols, sizeof(int));", "    return m;", "}"]
    qs.append(fillblank("C02-Q3", "השלימו את גודל האיבר בהקצאת מערך המצביעים.", lines, 3,
        ["sizeof(int *)", "sizeof(int)", "cols * sizeof(int)", "rows"], 0,
        lambda ln: LOG + "\n".join(lines[:3] + [ln] + lines[4:]) + "\nint main(void){ alloc_matrix(2, 3); return 0; }\n",
        "איבר במערך המצביעים הוא `int *`, ולכן גודלו `sizeof(int *)`. כל אחת מהאפשרויות האחרות מבקשת גודל איבר שאינו 8 בתים.",
        "גודל איבר במערך השורות: `sizeof(int *)`."))
    log = ok_out(LOG + ALLOC + "int main(void){ alloc_matrix(3, 4); return 0; }\n")
    tot = sum(int(a) * int(b) for a, b in re.findall(r"\[calloc (\d+) x (\d+)\]", log))
    assert tot == 72
    qs.append(numeric("C02-Q4", "כמה בתים בסך הכל מקצה הקריאה `alloc_matrix(3, 4)` ב-64 סיביות, כולל מערך המצביעים?", tot,
        "מערך המצביעים: $3 \\cdot 8 = 24$ בתים. שלוש שורות של 4 מספרים: $3 \\cdot 4 \\cdot 4 = 48$ בתים. סך הכל $24 + 48 = 72$.", "בתים = שורות$\\cdot 8$ + שורות$\\cdot$עמודות$\\cdot 4$."))
    lines = ["int **alloc_matrix(int rows, int cols)", "{", "    int i;", "    int **m = (int **)calloc(rows, sizeof(int *));",
             "    for (i = 0; i < rows; i++)", "        m[i] = (int *)calloc(rows, sizeof(int));", "    return m;", "}"]
    fixed = "        m[i] = (int *)calloc(cols, sizeof(int));"
    qs.append(findbug("C02-Q5", "הפונקציה אמורה להקצות מטריצה `rows` על `cols`, אבל במטריצה 2 על 3 השורות קצרות מדי. מצאו את השורה השגויה.",
        lines, 5, fixed, lambda L: LOG + "\n".join(L) + "\nint main(void){ alloc_matrix(2, 3); return 0; }\n",
        "אורך כל שורה הוא מספר העמודות. `calloc(rows, ...)` מקצה שורות באורך `rows`, ובמטריצה לא ריבועית זה קטן (או גדול) מדי.",
        "אורך שורה = `cols`, מספר השורות = `rows`."))
    lesson = '''
    <p>בונים מטריצה <code>rows × cols</code> בשני שלבים: קודם <b>מערך המצביעים</b>, ואז <b>כל שורה בנפרד</b> בלולאה.</p>
    ''' + pre(ALLOC) + '''
    <ul>
      <li><code>calloc(n, size)</code> מקצה <code>n</code> איברים בגודל <code>size</code> ומאפס אותם. <code>malloc</code> לא מאפס, והתאים מכילים זבל.</li>
      <li>גודל איבר במערך המצביעים: <code>sizeof(int *)</code> (8 בתים). גודל איבר בשורה: <code>sizeof(int)</code> (4 בתים).</li>
      <li>סך הבתים הוא <code>n * size</code> של כל קריאה: למטריצה 3×4 מקבלים $3 \\cdot 8 + 3 \\cdot 4 \\cdot 4 = 72$.</li>
    </ul>
    <div class="lesson-rule">🔑 מערך המצביעים: <code>rows</code> איברים של <code>sizeof(int *)</code>. כל שורה: <code>cols</code> איברים של <code>sizeof(int)</code>.</div>
    <div class="lesson-ex">דוגמה: <code>alloc_matrix(2, 3)</code> קורא ל-<code>calloc(2, 8)</code> ואז פעמיים ל-<code>calloc(3, 4)</code>. כל התאים מתחילים באפס.</div>
    <div class="lesson-trap">⚠️ <code>calloc(rows, sizeof(int))</code> למערך המצביעים מקצה חצי ממה שצריך ב-64 סיביות. ו-<code>malloc</code> במקום <code>calloc</code> משאיר ערכי זבל כשהמטריצה אמורה להתחיל באפסים.</div>'''
    return dict(id="C02", order=2, icon="🏗️", title="הקצאת מטריצה rows × cols", goal="אחרי השלב הזה אפשר לכתוב פונקציה שמקצה מטריצה דינמית מאופסת, ולחשב כמה בתים היא תופסת.", lesson=lesson, questions=qs)


# =============================================================== C03
def c03():
    qs = []
    log = ok_out(TRK + ALLOC + FREEM + "int main(void){ free_matrix(alloc_matrix(5, 3), 5); return 0; }\n")
    nf = len(re.findall(r"F\d+", log))
    assert nf == 6 and "BAD" not in log
    qs.append(numeric("C03-Q1", "כמה קריאות ל-`free` נדרשות כדי לשחרר מטריצה דינמית עם 5 שורות?", nf,
        "כל שורה משוחררת בנפרד (5 קריאות) ועוד מערך המצביעים עצמו: $5 + 1 = 6$, בדיוק כמספר ההקצאות.", "כל `calloc` מקבל `free`: $r + 1$ שחרורים."))
    blocks = ["int i, **m = alloc_matrix(3, 2);", "for (i = 0; i < 3; i++)\n        free(m[i]);", "free(m);"]
    qs.append(order("C03-Q2", "סדרו את הפקודות כך שהמטריצה תשוחרר נכון: קודם השורות ואחר כך מערך המצביעים.", blocks,
        lambda B: TRK + ALLOC + "int main(void)\n{\n" + "\n".join("    " + b for b in B) + '\n    printf("leaks=%d", T_leaks());\n    return 0;\n}\n',
        "אם משחררים את `m` לפני השורות, כתובות השורות (`m[i]`) אבדו ואי אפשר לשחרר אותן אחרי כן באופן חוקי. הסדר הנכון הוא שורות ואז `m`.",
        "קודם השורות, אחר כך המערך החיצוני."))
    code = main_of(ALLOC, ["    int **m = alloc_matrix(3, 4);", "    free(m);"])
    o = ["`0`", "`1`", "`3`", "`4`"]

    def v():
        return idx(o, ok_out(TRK + code.replace("    return 0;\n}", '    printf("%d", T_leaks());\n    return 0;\n}')).split()[-1])
    qs.append(mcq("C03-Q3", "בסוף התוכנית הבאה, כמה בלוקים שהוקצו נשארו בלי שחרור (דליפה)?\n" + fence(code), o, 2,
        "הוקצו 4 בלוקים: מערך המצביעים ו-3 שורות. שוחרר רק מערך המצביעים, ולכן 3 שורות דלפו. התשובה 4 שוכחת שאחד מהם שוחרר, ו-1 סופרת רק את המערך החיצוני.",
        "`free(m)` לבד משחרר רק את מערך המצביעים; השורות דולפות.", v))
    lines = ["void free_matrix(int **m, int rows)", "{", "    int i;", "    for (i = 1; i < rows; i++)", "        free(m[i]);", "    free(m);", "}"]
    qs.append(findbug("C03-Q4", "הפונקציה אמורה לשחרר את כל המטריצה בלי דליפות, אבל שורה אחת נשארת. מצאו את השורה השגויה.", lines, 3,
        "    for (i = 0; i < rows; i++)",
        lambda L: TRK + ALLOC + "\n".join(L) + '\nint main(void){ free_matrix(alloc_matrix(3, 2), 3); printf("leaks=%d", T_leaks()); return 0; }\n',
        "הלולאה מתחילה מ-`i = 1` ולכן שורה 0 לא משוחררת. אינדקסים בלולאה על שורות מתחילים מ-0.", "לולאה על שורות: `i` מ-0 עד `rows - 1`."))
    snippet = ['    int *p = NULL;', '    free(p);', '    printf("A");', '    free(p);', '    printf("B");']
    code = main_of("", snippet)
    o = ["`AB`", "`A`", "קריסה לפני כל פלט", "שגיאת הידור"]
    qs.append(mcq("C03-Q5", "מה קורה בקוד הבא?\n" + fence(code), o, 0,
        "`free(NULL)` מוגדר היטב ולא עושה כלום, גם פעמיים. לכן מודפס `AB`. לא קורסים ולא מקבלים שגיאת הידור. (`free` כפול על כתובת שאינה NULL הוא כבר באג.)",
        "`free(NULL)` בטוח ולא עושה כלום.", lambda: 0 if ok_out(PRE + code) == "AB" else -1))
    lesson = '''
    <p>כל <code>calloc</code> צריך <code>free</code> אחד. במטריצה דינמית יש <b>$r + 1$ בלוקים נפרדים</b>, ולכן $r + 1$ שחרורים.</p>
    ''' + pre(FREEM) + '''
    <ul>
      <li><b>קודם השורות, אחר כך מערך המצביעים.</b> השורות מוכרות רק דרך <code>m[i]</code>; אחרי <code>free(m)</code> הכתובות האלה אבדו.</li>
      <li><code>free(m)</code> לבד משחרר רק את מערך המצביעים, והשורות דולפות (דליפת זיכרון).</li>
      <li><code>free(NULL)</code> בטוח ולא עושה כלום. אבל <code>free</code> פעמיים על אותה כתובת אמיתית הוא באג.</li>
      <li>מערך סטטי (<code>int A[3][3]</code>) לא הוקצה ב-<code>calloc</code>, ולכן אסור לעשות לו <code>free</code>.</li>
    </ul>
    <div class="lesson-rule">🔑 שחרור מטריצה: לולאה על כל השורות עם <code>free(m[i])</code>, ורק אחריה <code>free(m)</code>.</div>
    <div class="lesson-ex">דוגמה: עבור מטריצה עם 3 שורות מבצעים <code>free(m[0])</code>, <code>free(m[1])</code>, <code>free(m[2])</code> ואז <code>free(m)</code>: ארבעה שחרורים לארבע הקצאות.</div>
    <div class="lesson-trap">⚠️ לולאת שחרור שמתחילה מ-<code>i = 1</code>, או שמסתיימת מוקדם מדי, משאירה שורה בלי שחרור. ולולאה עם <code>i &lt;= rows</code> קוראת את <code>m[rows]</code> שאינו קיים.</div>'''
    return dict(id="C03", order=3, icon="🧹", title="שחרור: שורות ואז המערך החיצוני", goal="אחרי השלב הזה אפשר לשחרר מטריצה דינמית נכון, לספור את השחרורים הנדרשים ולזהות דליפות.", lesson=lesson, questions=qs)


# =============================================================== C04
CP = '''#define N 2
int **copy_matrix(int A[][N], int n)
{
    int i, j;
    int **B = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        B[i] = (int *)calloc(n, sizeof(int));
        for (j = 0; j < n; j++)
            B[i][j] = A[i][j];
    }
    return B;
}
'''


def c04():
    qs = []
    D = '#define N 3\nint sum(int A[][N], int n) { int i, j, s = 0; for (i = 0; i < n; i++) for (j = 0; j < n; j++) s += A[i][j]; return s; }\n'
    o = ["`sum(S, 3)`", "`sum(m, 3)`", "`sum(&m, 3)`", "`sum(*m, 3)`"]

    def v():
        good = []
        for i, c in enumerate(o):
            r = run(PRE + D + "int main(void){ int S[3][3] = {{1,2,3},{4,5,6},{7,8,9}}; int **m = NULL; int t = " + c.strip("`") + "; return 0; }\n", FL)
            if r[0] == 0:
                good.append(i)
        assert len(good) == 1
        return good[0]
    qs.append(mcq("C04-Q1", "הפונקציה `int sum(int A[][N], int n)` מקבלת מטריצה סטטית (`N` קבוע). יש `int S[3][3]` ו-`int **m` (מטריצה דינמית). איזו קריאה תקינה?", o, 0,
        "הפרמטר `int A[][N]` הוא מצביע לשורה של $N$ מספרים, וזה מה שמתקבל משם של מערך דו-ממדי סטטי. `int **m` הוא מערך מצביעים, טיפוס אחר: ההידור נכשל או מתקבלת אזהרה, ואם מריצים, הקריאה מפרשת מצביעים כמספרים. גם `&m` וגם `*m` אינם מצביע-לשורה.",
        "`int A[][N]` לא שווה ל-`int **`. סטטי ודינמי אינם ניתנים להחלפה.", v))
    code = main_of(CP, ['    int A[2][2] = {{1, 2}, {3, 4}};', '    int **B = copy_matrix(A, 2);', '    B[0][0] = 9;', '    printf("%d %d", A[0][0], B[0][0]);'])
    o = ["`9 9`", "`1 9`", "`1 1`", "`9 1`"]
    qs.append(mcq("C04-Q2", "מה מדפיס הקוד?\n" + fence(code), o, 1,
        "`copy_matrix` בונה מטריצה דינמית חדשה ומעתיקה אליה ערכים. שינוי `B[0][0]` משנה רק את ההעתק, ולכן `A[0][0]` נשאר 1 ו-`B[0][0]` הוא 9. תשובות אחרות מניחות שהמטריצות חולקות זיכרון.",
        "ההעתק עצמאי: שינוי בו לא משנה את המקור.", lambda: idx(o, ok_out(PRE + code))))
    lines = ["int **copy_matrix(int A[][N], int n)", "{", "    int i, j;", "    int **B = (int **)calloc(n, sizeof(int *));",
             "    for (i = 0; i < n; i++)", "    {", "        B[i] = (int *)calloc(n, sizeof(int));", "        for (j = 0; j < n; j++)",
             "            B[i][j] = ___;", "    }", "    return B;", "}"]

    def bld(ln):
        L = lines[:8] + [ln] + lines[9:]
        return PRE + "#define N 3\n" + "\n".join(L) + '''
int main(void)
{
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int **B = copy_matrix(A, 3);
    int i, j;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            printf("%d ", B[i][j]);
    return 0;
}
'''
    qs.append(fillblank("C04-Q3", "השלימו את השורה שמעתיקה איבר מהמטריצה הסטטית `A` להעתק `B`, כך ש-`B` זהה ל-`A`.", lines, 8,
        ["A[i][j]", "A[j][i]", "A[i][j] * 2", "A[i][j] + i"], 0, bld,
        "ההעתק זהה למקור כשכל תא מועתק מאותו מקום: `A[i][j]`. `A[j][i]` משחלף, והאחרות משנות את הערך.", "העתקה: `B[i][j] = A[i][j]`."))
    body = ['    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};', '    int **B = (int **)calloc(3, sizeof(int *));', '    int i, j, s = 0;',
            '    for (i = 0; i < 3; i++)', '    {', '        B[i] = (int *)calloc(3, sizeof(int));', '        for (j = 0; j <= i; j++)',
            '            B[i][j] = A[i][j];', '    }', '    for (i = 0; i < 3; i++)', '        for (j = 0; j < 3; j++)', '            s += B[i][j];', '    printf("%d", s);']
    code = main_of("", body)
    ans = int(ok_out(PRE + code))
    assert ans == 34
    qs.append(numeric("C04-Q4", "מה מדפיס הקוד הבא?\n" + fence(code), ans,
        "רק התאים עם $j \\le i$ מועתקים, והשאר נשארים אפס (`calloc`): $1 + 4 + 5 + 7 + 8 + 9 = 34$. האיברים $2, 3, 6$ מעל האלכסון לא נכנסים.", "תא שלא הועתק נשאר 0."))
    blocks = ["int **B = alloc_matrix(n, n);", "for (i = 0; i < n; i++) for (j = 0; j < n; j++) B[i][j] = A[i][j];", "return B;"]

    def bld5(B):
        return PRE + "#define N 3\n" + ALLOC + "int **copy_matrix(int A[][N], int n)\n{\n    int i, j;\n" + "\n".join("    " + b for b in B) + '''
}
int main(void)
{
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int **B = copy_matrix(A, 3);
    printf("%d", B[1][1]);
    return 0;
}
'''
    qs.append(order("C04-Q5", "סדרו את גוף `copy_matrix`, שמשתמשת ב-`alloc_matrix` שכבר כתובה: להקצות, להעתיק, להחזיר.", blocks, bld5,
        "קודם מקצים את `B` (אחרת אין לאן להעתיק), אחר כך מעתיקים, ורק אז מחזירים. `return` לפני ההעתקה מחזיר מטריצה מאופסת.", "הקצאה, העתקה, `return`."))
    lesson = '''
    <p>במבחן הקלט הוא לעיתים מטריצה <b>סטטית</b> והפלט מבנה <b>דינמי</b>. הפרמטר הסטטי נכתב עם קבוע עמודות:</p>
    ''' + pre('#define N 3\nint **copy_matrix(int A[][N], int n);') + '''
    <ul>
      <li><code>int A[][N]</code> הוא מצביע לשורה של $N$ מספרים. מעבירים לו מערך כמו <code>int S[3][3]</code>.</li>
      <li><code>int **m</code> הוא מערך מצביעים, <b>טיפוס אחר</b>: לא מעבירים אחד במקום השני.</li>
      <li>הפלט הדינמי נבנה בנפרד (<code>calloc</code>), מועתק מהקלט, ומוחזר ב-<code>return</code>. ההעתק עצמאי מהמקור.</li>
      <li>תא שלא כותבים אליו נשאר 0, כי <code>calloc</code> מאפס.</li>
    </ul>
    ''' + pre(CP.replace('#define N 2', '#define N 3')) + '''
    <div class="lesson-rule">🔑 העתקה: מקצים מטריצה חדשה בגודל המתאים, ואז <code>B[i][j] = A[i][j]</code> בלולאה כפולה.</div>
    <div class="lesson-ex">דוגמה: אחרי <code>B = copy_matrix(A, 3)</code>, השינוי <code>B[0][0] = 9</code> לא משנה את <code>A[0][0]</code>.</div>
    <div class="lesson-trap">⚠️ מערך סטטי שהועבר לפונקציה לא משחררים עם <code>free</code>: הוא לא הוקצה ב-<code>calloc</code>.</div>'''
    return dict(id="C04", order=4, icon="📋", title="מטריצה סטטית לדינמית", goal="אחרי השלב הזה אפשר להעתיק מטריצה סטטית A[][N] למטריצה דינמית חדשה ולהבחין בין int A[][N] ל-int **.", lesson=lesson, questions=qs)


# =============================================================== C05
LOWT = '''#define N 4
int **low_triangle(int A[][N], int n)
{
    int i, j;
    int **low = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        low[i] = (int *)calloc(i + 1, sizeof(int));
        for (j = 0; j <= i; j++)
            low[i][j] = A[i][j];
    }
    return low;
}
'''
UPT = '''#define N 4
int **strict_upper(int A[][N], int n)
{
    int i, j;
    int **up = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        up[i] = (int *)calloc(n - 1 - i, sizeof(int));
        for (j = i + 1; j < n; j++)
            up[i][j - i - 1] = A[i][j];
    }
    return up;
}
'''


def c05():
    qs = []
    log = ok_out(LOG + LOWT.replace("#define N 4", "#define N 6") + "int main(void){ int A[6][6] = {{0}}; low_triangle(A, 6); return 0; }\n")
    tot = sum(int(a) for a, b in re.findall(r"\[calloc (\d+) x (\d+)\]", log) if b == "4")
    assert tot == 21
    qs.append(numeric("C05-Q1", "כמה איברים נשמרים בסך הכל במשולש התחתון (כולל האלכסון) של מטריצה 6 על 6, כששורה $i$ מקבלת $i+1$ איברים?", tot,
        "$1 + 2 + 3 + 4 + 5 + 6 = 21$, כלומר $\\frac{6 \\cdot 7}{2}$. זה חצי ממטריצה מלאה (36), בלי מקום מבוזבז.", "משולש עם $n$ שורות: $\\frac{n(n+1)}{2}$ איברים."))
    log = ok_out(LOG + UPT + "int main(void){ int A[4][4] = {{0}}; strict_upper(A, 4); return 0; }\n")
    lens = [a for a, b in re.findall(r"\[calloc (\d+) x (\d+)\]", log) if b == "4"]
    o = ["`3 2 1 0`", "`4 3 2 1`", "`3 3 3 3`", "`1 2 3 4`"]
    qs.append(mcq("C05-Q2", "ב-`strict_upper` למטריצה 4 על 4 (המשולש שמעל האלכסון, בלי האלכסון), מה אורכי השורות `up[0]` עד `up[3]`?", o, 0,
        "שורה $i$ מכילה את `A[i][i+1..n-1]`, כלומר $n-1-i$ איברים: $3, 2, 1, 0$. הרצף `4 3 2 1` כולל את האלכסון, `1 2 3 4` הפוך, ו-`3 3 3 3` שומר מקום מבוזבז.",
        "משולש עליון ממש: שורה $i$ באורך $n-1-i$.", lambda: idx(o, " ".join(lens))))
    probe = PRE + UPT + '''int main(void)
{
    int A[4][4], i, j, k, **up;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) A[i][j] = 10 * i + j;
    up = strict_upper(A, 4);
    for (k = 0; k < 2; k++) if (up[1][k] == 13) printf("%d", k);
    return 0;
}
'''
    ans = int(ok_out(probe))
    assert ans == 1
    qs.append(numeric("C05-Q3", "ב-`strict_upper` נשמר האיבר `A[i][j]` (עבור $j > i$) בתא `up[i][j - i - 1]`. באיזה אינדקס בתוך `up[1]` נשמר `A[1][3]`?", ans,
        "$j - i - 1 = 3 - 1 - 1 = 1$. השורה `up[1]` מחזיקה את `A[1][2]` באינדקס 0 ואת `A[1][3]` באינדקס 1.", "אינדקס בתוך שורת המשולש העליון: $j - i - 1$."))
    lines = ["#define N 4", "int **low_triangle(int A[][N], int n)", "{", "    int i, j;", "    int **low = (int **)calloc(n, sizeof(int *));",
             "    for (i = 0; i < n; i++)", "    {", "        low[i] = (int *)calloc(___, sizeof(int));", "        for (j = 0; j <= i; j++)",
             "            low[i][j] = A[i][j];", "    }", "    return low;", "}"]
    qs.append(fillblank("C05-Q4", "השלימו את אורך השורה `i` במשולש התחתון (עם האלכסון).", lines, 7, ["i + 1", "i", "n", "n - i"], 0,
        lambda ln: LOG + "\n".join(lines[:7] + [ln] + lines[8:]) + "\nint main(void){ int A[4][4] = {{0}}; low_triangle(A, 4); return 0; }\n",
        "שורה $i$ מכילה את `A[i][0..i]`, כלומר $i+1$ איברים. עם `i` הלולאה `j <= i` כותבת איבר אחד מעבר לסוף. עם `n` כל השורות ארוכות (בזבוז), ועם `n - i` המשולש הפוך.", "משולש תחתון: שורה $i$ באורך $i+1$."))
    lines = ["#define N 4", "int **strict_upper(int A[][N], int n)", "{", "    int i, j;", "    int **up = (int **)calloc(n, sizeof(int *));",
             "    for (i = 0; i < n; i++)", "    {", "        up[i] = (int *)calloc(n - 1 - i, sizeof(int));", "        for (j = i + 1; j < n; j++)",
             "            up[i][j] = A[i][j];", "    }", "    return up;", "}"]
    drv = '''
int main(void)
{
    int A[4][4], i, j, k, **up;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) A[i][j] = 10 * i + j;
    up = strict_upper(A, 4);
    for (i = 0; i < 3; i++) { for (k = 0; k < 3 - i; k++) printf("%d ", up[i][k]); printf("\\n"); }
    return 0;
}
'''
    qs.append(findbug("C05-Q5", "הפונקציה אמורה לשמור בשורה $i$ את `A[i][i+1..n-1]` החל מאינדקס 0, אבל התוצאה שגויה. מצאו את השורה השגויה.", lines, 9,
        "            up[i][j - i - 1] = A[i][j];", lambda L: PRE + "\n".join(L) + drv,
        "השורה `up[i]` קצרה ($n-1-i$ איברים), ואינדקס `j` הולך עד $n-1$. הכתיבה ל-`up[i][j]` חורגת מהגבולות ומשאירה את התא הראשון ריק. האינדקס הנכון הוא `j - i - 1`.",
        "מקור בעמודה $j$ הולך ליעד $j - i - 1$."))
    lesson = '''
    <p>שורות המטריצה הדינמית יכולות להיות <b>באורכים שונים</b>: מערך משונן (jagged). כך חוסכים זיכרון כשצריך רק חלק מהמטריצה, והמבחן אוהב את זה.</p>
    ''' + pre(LOWT) + '''
    <ul>
      <li><b>משולש תחתון</b> (כולל האלכסון): שורה $i$ מכילה את <code>A[i][0..i]</code>, כלומר $i+1$ איברים. סך הכל $\\frac{n(n+1)}{2}$.</li>
      <li><b>משולש עליון ממש</b> (בלי האלכסון): שורה $i$ מכילה את <code>A[i][i+1..n-1]</code>, כלומר $n-1-i$ איברים. הערך <code>A[i][j]</code> נשמר באינדקס <code>j - i - 1</code>.</li>
      <li>השורה האחרונה במשולש העליון ריקה (אורך 0), ו-<code>calloc(0, ...)</code> תלוי במימוש. בשאלה אמיתית קראו כמה איברים יש בכל שורה.</li>
    </ul>
    ''' + pre(UPT) + '''
    <div class="lesson-rule">🔑 לפני שכותבים קוד: רשמו אורך כל שורה ונוסחה של אינדקס מקור מול אינדקס יעד. אחר כך הקצו שורה בגודל הנכון והעתיקו.</div>
    <div class="lesson-ex">דוגמה: עבור $n = 4$ אורכי השורות במשולש העליון הם $3, 2, 1, 0$. האיבר <code>A[1][3]</code> נשמר ב-<code>up[1][1]</code> כי $3 - 1 - 1 = 1$.</div>
    <div class="lesson-trap">⚠️ <code>up[i][j]</code> במקום <code>up[i][j - i - 1]</code> כותב מחוץ לגבולות השורה הקצרה.</div>'''
    return dict(id="C05", order=5, icon="📐", title="מערך משונן: משולשים", goal="אחרי השלב הזה אפשר להקצות משולש תחתון או עליון עם שורות באורכים שונים ולחשב אורכי שורות ואינדקסים.", lesson=lesson, questions=qs)


# =============================================================== C06
EV = '''void evens(int *A, int n, int **out, int *cnt)
{
    int i, k;
    *cnt = 0;
    for (i = 0; i < n; i++)
        if (A[i] % 2 == 0)
            (*cnt)++;
    *out = (int *)calloc(*cnt, sizeof(int));
    k = 0;
    for (i = 0; i < n; i++)
        if (A[i] % 2 == 0)
            (*out)[k++] = A[i];
}
'''


def c06():
    qs = []
    base = '''#define N 3
void low_triangle(int A[][N], int n, int ***out)
{
    int i, j;
    int **low = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        low[i] = (int *)calloc(i + 1, sizeof(int));
        for (j = 0; j <= i; j++)
            low[i][j] = A[i][j];
    }
    ___
}
'''
    o = ["`*out = low;`", "`out = low;`", "`**out = low;`", "`out[0] = *low;`"]

    def v():
        good = []
        for i, c in enumerate(o):
            r = run(PRE + base.replace("___", c.strip("`")) + '''int main(void)
{
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int **T = NULL;
    low_triangle(A, 3, &T);
    printf("%d", T[2][1]);
    return 0;
}
''', FL)
            if r == (0, "8"):
                good.append(i)
        assert len(good) == 1
        return good[0]
    stem = "הפונקציה מחזירה את המשולש התחתון דרך הפרמטר `int ***out` (הקורא מעביר `&T` כש-`T` הוא `int **`). איזו פקודה במקום `___` מוסרת את התוצאה לקורא?\n" + fence(base)
    qs.append(mcq("C06-Q1", stem, o, 0,
        "`out` הוא כתובת של משתנה `int **` אצל הקורא. כדי לשנות את אותו משתנה כותבים דרך הכתובת: `*out = low`. `out = low` משנה רק את העותק המקומי של הפרמטר (וגם הטיפוס לא תואם), ו-`**out = low` ו-`out[0] = *low` מערבבים רמות הפניה: ההידור נכשל.",
        "מחזירים דרך פרמטר `X *p` בכתיבה `*p = ...`. כאן `X` הוא `int **`.", v))
    D = '''void fill(int **out, int *cnt)
{
    *out = (int *)calloc(3, sizeof(int));
    (*out)[0] = 4;
    (*out)[2] = 9;
    *cnt = 3;
}
'''
    code = main_of(D, ['    int *a;', '    int c;', '    fill(&a, &c);', '    printf("%d %d", a[2], c);'])
    o = ["`9 3`", "`4 3`", "`9 9`", "`3 9`"]
    qs.append(mcq("C06-Q2", "מה מדפיס הקוד?\n" + fence(code), o, 0,
        "`fill` כותבת דרך `out` אל `a`, וגם דרך `cnt` אל `c`. אחרי הקריאה `a` מצביע על מערך `{4, 0, 9}` ו-`c` הוא 3, ולכן `a[2]` הוא 9 והפלט `9 3`. ב-`4 3` נבחר האיבר הראשון, ושתי האפשרויות האחרות מחליפות ערכים.",
        "`*out` הוא המצביע של הקורא; `(*out)[k]` הוא האיבר ה-`k` במערך שלו.", lambda: idx(o, ok_out(PRE + code))))
    code = main_of(EV, ['    int A[5] = {3, 4, 8, 5, 6};', '    int *a = NULL;', '    int c = 77;', '    evens(A, 5, &a, &c);', '    printf("%d", c);'])
    ans = int(ok_out(PRE + code))
    assert ans == 3
    qs.append(numeric("C06-Q3", "מה מדפיס הקוד?\n" + fence(code), ans,
        "`evens` סופרת את הזוגיים (4, 8, 6) ושומרת 3 ב-`*cnt`. הערך ההתחלתי 77 נדרס בפקודה `*cnt = 0` בתחילת הפונקציה.", "ערך שמוחזר בפרמטר נקבע בתוך הפונקציה (`*cnt = ...`)."))
    blocks = ["*cnt = 0;", "for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;", "*out = (int *)calloc(*cnt, sizeof(int));",
              "k = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];"]

    def bld(B):
        return LOG + "void evens(int *A, int n, int **out, int *cnt)\n{\n    int i, k;\n" + "\n".join("    " + b for b in B) + '''
}
int main(void)
{
    int A[5] = {3, 4, 8, 5, 6};
    int *a = NULL;
    int c = 77;
    evens(A, 5, &a, &c);
    printf("%d: %d %d %d", c, a[0], a[1], a[2]);
    return 0;
}
'''
    qs.append(order("C06-Q4", "סדרו את גוף `evens`: לאפס מונה, לספור זוגיים, להקצות בדיוק לפי המונה, ולמלא.", blocks, bld,
        "המונה מתאפס קודם, אחר כך נספרים הזוגיים, רק אחר כך מקצים `*cnt` תאים (כך מקצים בדיוק), ובסוף ממלאים. מילוי לפני הקצאה כותב ל-NULL, והקצאה לפני הספירה מקצה לפי הערך הישן.", "מאפסים, סופרים, מקצים, ממלאים."))
    o = ["`evens(A, 5, &a, &c);`", "`evens(A, 5, a, c);`", "`evens(A, 5, &a, c);`", "`evens(A, 5, *a, *c);`"]

    def v5():
        good = []
        for i, c in enumerate(o):
            r = run(PRE + EV + "int main(void){ int A[5] = {3,4,8,5,6}; int *a = NULL; int c = 0; " + c.strip("`") + " return 0; }\n", FL)
            if r[0] == 0:
                good.append(i)
        assert good == [0], good
        return 0
    qs.append(mcq("C06-Q5", "הפונקציה `evens(int *A, int n, int **out, int *cnt)` מחזירה מערך דרך `out` וגודלו דרך `cnt`. הקורא הצהיר `int A[5]; int *a; int c;`. איזו קריאה נכונה?", o, 0,
        "כדי שהפונקציה תשנה את `a` ואת `c` מעבירים את הכתובות שלהם: `&a` (מסוג `int **`) ו-`&c` (מסוג `int *`). העברת `a` ו-`c` עצמם, או `&a` עם `c`, או `*a` ו-`*c`, לא מתאימה לטיפוסים ולא משנה דבר אצל הקורא.",
        "פרמטר פלט: מעבירים `&משתנה`.", v5))
    lesson = '''
    <p>פונקציה יכולה להחזיר ב-<code>return</code> רק דבר אחד. כשצריך שניים (מבנה וגם גודל), את השני מעבירים <b>by reference</b>: הקורא שולח <b>כתובת</b> של משתנה, והפונקציה כותבת דרכה.</p>
    <ul>
      <li>כדי להחזיר מערך (<code>int *</code>) דרך פרמטר, הפרמטר הוא <code>int **out</code> והקריאה שולחת <code>&amp;a</code>. כדי להחזיר מטריצה (<code>int **</code>) הפרמטר הוא <code>int ***out</code>.</li>
      <li>כותבים <code>*out = ...</code> כדי לשנות את המשתנה של הקורא. <code>out = ...</code> משנה רק עותק מקומי.</li>
      <li>איבר במערך המוחזר: <code>(*out)[k]</code>. הסוגריים חובה: <code>*out[k]</code> פירושו <code>*(out[k])</code>.</li>
      <li>גודל: <code>int *cnt</code>, והעלאה כ-<code>(*cnt)++</code> (בלי סוגריים, <code>*cnt++</code> מקדם את המצביע עצמו).</li>
    </ul>
    ''' + pre(EV) + '''
    <div class="lesson-rule">🔑 פרמטר פלט מסוג <code>T</code> מוגדר <code>T *p</code>, נכתב <code>*p = ...</code>, ומועבר בקריאה כ-<code>&amp;x</code>.</div>
    <div class="lesson-ex">דוגמה: הקורא כותב <code>int *a; int c; evens(A, 5, &amp;a, &amp;c);</code>. אחרי הקריאה <code>a</code> מצביע על המערך החדש ו-<code>c</code> מחזיק את אורכו.</div>
    <div class="lesson-trap">⚠️ <code>*cnt++</code> במקום <code>(*cnt)++</code>, ו-<code>*out[k]</code> במקום <code>(*out)[k]</code>: שתי טעויות סוגריים נפוצות.</div>'''
    return dict(id="C06", order=6, icon="🔁", title="החזרה by reference: ***out ו-*size", goal="אחרי השלב הזה אפשר להחזיר מערך או מטריצה וגם גודל דרך פרמטרים, עם הכתובות והסוגריים הנכונים.", lesson=lesson, questions=qs)


# =============================================================== C07
DYN = '''typedef struct
{
    int size;
    int *ptr;
} dyn_array;
'''
DIVFN = '''dyn_array *div_numbers(const int *A, int sz, int n)
{
    int i, j, k = 0;
    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));
    for (i = 2; i <= n; i++)
    {
        int *tmp = (int *)calloc(sz, sizeof(int));
        for (j = 0, k = 0; j < sz; j++)
            if (A[j] % i == 0)
                tmp[k++] = A[j];
        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));
        B[i - 2].size = k;
    }
    return B;
}
'''
DRV7 = '''
int main(void)
{
    int A[6] = {4, 6, 8, 9, 10, 12};
    dyn_array *B = div_numbers(A, 6, 4);
    int i, j;
    for (i = 0; i < 3; i++)
    {
        printf("%d:", B[i].size);
        for (j = 0; j < B[i].size; j++)
            printf(" %d", B[i].ptr[j]);
        printf("\\n");
    }
    return 0;
}
'''


def c07():
    qs = []
    code = main_of(DYN, ['    dyn_array *B = (dyn_array *)calloc(3, sizeof(dyn_array));', '    printf("%d %s", B[1].size, B[1].ptr ? "ptr" : "NULL");'])
    o = ["`0 NULL`", "`0 ptr`", "`3 NULL`", "ערכי זבל, התוצאה אינה צפויה"]
    qs.append(mcq("C07-Q1", "מה מדפיס הקוד?\n" + fence(code), o, 0,
        "`calloc` מאפס את כל הבתים, ולכן בכל איבר `size` הוא 0 ו-`ptr` הוא `NULL`. זה בדיוק מה שמתאים לשורות ריקות. זבל היה מתקבל רק מ-`malloc`.",
        "מערך מבנים מ-`calloc`: `size = 0` ו-`ptr = NULL` בכל איבר.", lambda: idx(o, ok_out(PRE + code))))
    probe = PRE + DYN + 'int main(void){ printf("%d", (int)sizeof(dyn_array)); return 0; }\n'
    ans = int(ok_out(probe))
    assert ans == 16
    qs.append(numeric("C07-Q2", "ב-64 סיביות, מה `sizeof(dyn_array)` של המבנה מהשיעור (`int size; int *ptr;`)?", ans,
        "`int` תופס 4 בתים, ואחריו 4 בתים ריפוד כדי שהמצביע (8 בתים) יתחיל בכתובת שמתחלקת ב-8. סך הכל $4 + 4 + 8 = 16$.", "גודל מבנה כולל ריפוד לפי השדה הרחב ביותר."))
    L = DIVFN.strip("\n").split("\n")
    bi = next(i for i, l in enumerate(L) if "realloc(tmp" in l)
    Lb = list(L)
    Lb[bi] = "        B[i - 2].ptr = (int *)realloc(tmp, ___);"
    opts = ["k * sizeof(int)", "k", "sz * sizeof(int)", "sizeof(int)"]
    qs.append(fillblank("C07-Q3", "השלימו את גודל ההקטנה של `tmp` למספר האיברים שנמצאו בפועל (`k`).", Lb, bi, opts, 0,
        lambda ln: LOG + DYN + "\n".join(Lb[:bi] + [ln] + Lb[bi + 1:]) + DRV7,
        "`realloc` מקבל גודל בבתים, כלומר `k` איברים כפול `sizeof(int)`. `k` לבד הוא `k` בתים בלבד, `sz * sizeof(int)` לא מקטין כלום, ו-`sizeof(int)` משאיר איבר אחד.", "`realloc(p, k * sizeof(int))`: הגודל בבתים."))
    blocks = ["int *tmp = (int *)calloc(sz, sizeof(int));",
              "for (j = 0, k = 0; j < sz; j++)\n            if (A[j] % i == 0)\n                tmp[k++] = A[j];",
              "B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));\n        B[i - 2].size = k;"]

    def bld(B):
        return LOG + DYN + '''
dyn_array *div_numbers(const int *A, int sz, int n)
{
    int i, j, k = 0;
    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));
    for (i = 2; i <= n; i++)
    {
''' + "\n".join("        " + b for b in B) + '''
    }
    return B;
}
''' + DRV7
    qs.append(order("C07-Q4", "סדרו את גוף הלולאה של `div_numbers` עבור מחלק `i`: להקצות מערך זמני, למלא אותו, ולהקטין ולשמור.", blocks, bld,
        "קודם מקצים `tmp` בגודל המרבי, אחר כך ממלאים ומחשבים את `k`, ורק אז מקטינים ל-`k` איברים ושומרים את הגודל. הקטנה לפני המילוי משתמשת ב-`k` שעדיין לא חושב.", "מקצים מקסימום, ממלאים, מקטינים ושומרים."))
    bi = next(i for i, l in enumerate(L) if "A[j] % i == 0" in l)
    fixed = L[bi]
    Lbug = list(L)
    Lbug[bi] = "            if (i % A[j] == 0)"
    qs.append(findbug("C07-Q5", "בשורה $i$ של התוצאה אמורים להיכנס המספרים מ-`A` שמתחלקים ב-`i`. התוצאה שגויה. מצאו את השורה השגויה.", Lbug, bi, fixed,
        lambda X: LOG + DYN + "\n".join(X) + DRV7,
        "התנאי הוא ש-`A[j]` מתחלק ב-`i`: `A[j] % i == 0`. הגרסה `i % A[j] == 0` שואלת את ההפך (האם `i` מתחלק ב-`A[j]`), ולכן אף מספר גדול מ-`i` לא נכנס.", "`x % d == 0`: `x` מתחלק ב-`d`."))
    lesson = '''
    <p>לפעמים כל שורה היא <b>מבנה</b> שמחזיק גם מערך דינמי וגם את גודלו, ומחזירים מערך של מבנים:</p>
    ''' + pre(DYN) + '''
    <ul>
      <li><code>calloc(n, sizeof(dyn_array))</code> נותן לכל איבר <code>size = 0</code> ו-<code>ptr = NULL</code>, וזה מתאים לשורה ריקה.</li>
      <li>גישה לשדות באיבר של מערך: <code>B[i].size</code> ו-<code>B[i].ptr[j]</code> (נקודה, כי <code>B[i]</code> הוא מבנה ולא מצביע).</li>
      <li>גודל המבנה ב-64 סיביות הוא 16 בתים: <code>int</code> (4) + ריפוד (4) + מצביע (8).</li>
      <li><b>הקטנה עם <code>realloc</code></b>: מקצים מערך זמני בגודל המרבי, ממלאים ומחשבים <code>k</code>, ואז <code>p = realloc(p, k * sizeof(int))</code>. הגודל בבתים.</li>
      <li>אם <code>k == 0</code>, התנהגות <code>realloc(p, 0)</code> תלויה במימוש: עדיף <code>free(p)</code> ולהשאיר <code>NULL</code>.</li>
    </ul>
    ''' + pre(DIVFN) + '''
    <div class="lesson-rule">🔑 מערך מבנים: מקצים עם <code>calloc</code>, ממלאים כל איבר בנפרד, ומקטינים כל מערך פנימי עם <code>realloc</code> בגודל <code>k * sizeof(int)</code>.</div>
    <div class="lesson-ex">דוגמה: עבור <code>A = {4, 6, 8, 9, 10, 12}</code> ו-<code>n = 4</code>: <code>B[0]</code> מחזיק את הזוגיים (5 איברים), <code>B[1]</code> את המתחלקים ב-3, ו-<code>B[2]</code> את המתחלקים ב-4.</div>
    <div class="lesson-trap">⚠️ <code>realloc(tmp, k)</code> בלי <code>sizeof</code> מקצה <code>k</code> בתים ולא <code>k</code> מספרים. ו-<code>malloc</code> במקום <code>calloc</code> משאיר <code>size</code> ו-<code>ptr</code> עם זבל בשורות שלא מילאתם.</div>'''
    return dict(id="C07", order=7, icon="🧮", title="מערך של מבנים ו-realloc", goal="אחרי השלב הזה אפשר לבנות מערך של struct {size, ptr}, למלא כל שורה ולהקטין אותה עם realloc.", lesson=lesson, questions=qs)


# =============================================================== C08 boss
def c08():
    qs = [{"bankId": b, "recap": r} for b, r in [
        ("24B-B-Q2", "מסגרת סביב מטריצה: `calloc` לאפסים, העתקה עם היסט 1, ושחרור המקור אחרי ההעתקה."),
        ("24B-A-Q2", "מערך של מבנים: `calloc` נותן `size = 0` ו-`ptr = NULL`, ו-`realloc` מקטין לגודל הסופי."),
        ("25B-A-Q2", "ממטריצה סטטית לשני משולשים משוננים דרך `int ***`."),
        ("25B-B-Q2", "משני משולשים למטריצה $(n+1) \\times (n+1)$ עם אלכסון אפס: נוסחאות אינדקס."),
        ("23B-A-Q2", "שני מערכי פלט דרך פרמטרים, אורך מקסימלי ואז `realloc`.")]]
    lesson = '''
    <p>זה שלב האלוף: שאלות אמיתיות ממבחנים קודמים. בכל אחת מהן אותו שלד:</p>
    <ul>
      <li>שרטטו קלט ופלט עם דוגמה 3×3, וכתבו אורך כל שורה ונוסחת אינדקס (מקור מול יעד).</li>
      <li>הקצו קודם את מערך המצביעים, ואז כל שורה בלולאה. <code>calloc</code> כשצריך אפסים.</li>
      <li>החזרה: ב-<code>return</code> או דרך <code>int ***out</code> / <code>int *size</code>, עם <code>*out = ...</code> ו-<code>(*out)[k]</code>.</li>
      <li>שחרור: קודם השורות ואז המערך החיצוני, ורק אחרי שהעתקתם.</li>
    </ul>
    <div class="lesson-rule">🔑 בדקו תמיד מקרה קטן (למשל $n = 1$) ואת כל הקצאה: האם יש לה שחרור, והאם הגודל הוא <code>sizeof</code> של הטיפוס הנכון.</div>'''
    return dict(id="C08", order=8, icon="🏆", title="אלוף: שאלות אמיתיות ממבחנים", goal="אחרי השלב הזה אפשר לפתור שאלות אמיתיות על מטריצות דינמיות, משולשים ומערכי מבנים.", boss=True, lesson=lesson, questions=qs)


def emit(L):
    out = [f'/* dyn_2d, level {L["order"]} - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */',
           'COURSE_LEVEL("dyn_2d", {',
           f'  id: {json.dumps(L["id"])}, order: {L["order"]}, icon: {json.dumps(L["icon"], ensure_ascii=False)}, title: {json.dumps(L["title"], ensure_ascii=False)},',
           f'  goal: {json.dumps(L["goal"], ensure_ascii=False)},']
    if L.get("boss"):
        out.append("  boss: true,")
    out.append('  source: "ai-verified",')
    h = L["lesson"]
    assert "`" not in h and "${" not in h, L["id"]
    out.append("  lesson: { html: String.raw`" + h + "` },")
    out.append("  questions: [")
    for q in L["questions"]:
        out.append("    " + json.dumps(q, ensure_ascii=False) + ",")
    out.append("  ],")
    out.append("});")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    built = [f() for f in (c01, c02, c03, c04, c05, c06, c07, c08)]
    ids = set()
    for L in built:
        for q in L["questions"]:
            k = q.get("id") or q.get("bankId")
            assert k not in ids
            ids.add(k)
    OUT.mkdir(parents=True, exist_ok=True)
    for L in built:
        (OUT / (L["id"] + ".js")).write_text(emit(L), encoding="utf-8", newline="\n")
        print(L["id"], len(L["questions"]), "questions OK")
