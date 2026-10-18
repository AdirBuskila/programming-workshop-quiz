# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-B.json -- programming-workshop (C), semester B 2020, moed B (02.08.2020).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of three). Part 2: Q4 (20 pts, four pick-and-justify items).
Part 3: bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + yellow-marked options).
Code solutions compiled and run with clang: tools/verify/20B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_20B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-B.json"
IDS = "abcdefgh"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CHOOSE = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש.*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר מחרוזת כ-**"ממוינת בקבוצות"** אם האותיות הקטנות שבתוכה, האותיות הגדולות שבתוכה, וגם הספרות שבתוכה ממוינות בסדר עולה (לא ממש) מתחילת המחרוזת עד לסופה, לפי קודי ASCII שלהן. מדובר רק על סדר התווים בתוך כל אחת מקבוצות התווים. לא משנה כיצד התווים מהקבוצות השונות ממוקמים יחסית זה לזה. מיקום התווים שאינם שייכים לאף אחת מהקבוצות לא משנה.

**לדוגמא,**
המחרוזת (משמאל לימין) היא ממוינת בקבוצות:
```
"B4$Ca#%ds5P8P&9zY"
```
המחרוזת (משמאל לימין) היא אינה ממוינת בקבוצות (קוד `'s'` הוא גדול מקוד `'r'`):
```
"B4$Ca#%ds5P8P&9rY"
```

כתוב פונקציה אשר מקבלת מחרוזת ומחזירה `1` אם המחרוזת ממוינת בקבוצות ו-`0` אחרת.""" + CHOOSE

Q1_SOL = r"""```c
int group_sort(char *str)
{
    char last_capital, last_small, last_digit;
    int i;
    last_capital = last_small = last_digit = '\0';
    for (i = 0; str[i] != '\0'; i++)
        if (isupper(str[i]))
            if (str[i] < last_capital)
                return 0;
            else
                last_capital = str[i];
        else
            if (islower(str[i]))
                if (str[i] < last_small)
                    return 0;
                else
                    last_small = str[i];
            else
                if (isdigit(str[i]))
                    if (str[i] < last_digit)
                        return 0;
                    else
                        last_digit = str[i];
    return 1;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item
{
  int data;
  struct item *next;
} Item;
```
נאמר שרשימה מקושרת $L_1$ בעלת $n_1$ איברים מסוג `Item` היא **תחילית (prefix)** של רשימה מקושרת $L_2$ בעלת $n_2$ איברים מסוג `Item` אם $n_1 \le n_2$ ושדה `data` של איבר שנמצא במקום `i` מתחילת $L_1$ ($0 \le i < n_1$) שווה לשדה `data` של איבר שנמצא במקום `i` מתחילת $L_2$. רשימה ריקה היא תחילית של כל רשימה.

כתוב פונקציה אשר מקבלת מערך `A` של רשימות מקושרות עם גודלו וגם רשימה מקושרת נפרדת `L`. כל הרשימות מורכבות מאיברים מסוג `Item`.
על הפונקציה לגלות את כל רשימות במערך `A` ש-`L` היא תחילית שלהן. יש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג `Item`) שתכיל את האינדקסים במערך `A` של כל רשימות במערך בהם `L` היא תחילית. אין חשיבות לסדר האיברים ברשימה החדשה.
הפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר `NULL`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.

**דוגמא:** (באיור: המערך `A`, הרשימה `L` והרשימה החדשה)""" + CHOOSE

Q2_SOL = r"""```c
//Auxiliary function - checks whether L1 is prefix of L2
int is_prefix(Item *L1, Item *L2)
{
    while (L1 && L2)
    {
        if (L1->data != L2->data)
            return 0;
        L1 = L1->next;
        L2 = L2->next;
    }
    if (L1)
        return 0;
    return 1;
}

//Auxiliary function
void insert_in_head(int x, Item **pl)
{
    Item *temp = (Item *)malloc(sizeof(Item));
    temp->data = x;
    temp->next = *pl;
    *pl = temp;
}

Item *arr_of_lists_to_list_of_prefixes(Item **A, int n, Item *L)
{
    int i;
    Item *pref_list = NULL;
    for (i = n - 1; i >= 0; i--)
        if (is_prefix(L, A[i]))
            insert_in_head(i, &pref_list);
    return pref_list;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**מטריצה דלילה** הינה מטריצה שמרבית איבריה בעלי ערך אפס.

כתוב פונקציה (`void`) אשר מקבלת **מערך דו-ממדי סטטי** (לא דינאמי) `A` של מספרים שלמים בעל `rows` שורות ו-`cols` עמודות, וגם מחרוזת `fileName`.
המספר הפיסי של העמודות יינתן ע"י קבוע בשם `COLS`. יש להגדיר אותו לפני הפונקציה.

מחרוזת `fileName` תהווה שם של **קובץ טקסט** ששומר מטריצה דלילה בעלת `rows` שורות ו-`cols` עמודות בדרך חסכונית באמצעות אחסון רק איברי המטריצה שאינם בעלי ערך אפס.
הקובץ מכיל `rows` שורות. שורה מס' `i` בקובץ מתאימה לשורה מס' `i` של המטריצה (השורות ממוספרות מ-0). בתחילת כל שורה נמצא מספרה.
כל איבר של המטריצה ששונה מאפס מוצג בקובץ כזוג המספרים: ערך של האיבר ומס' עמודה בה הוא נמצא במטריצה.
המספרים הסמוכים בכל שורה מופרדים ברווח אחד. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה לשחזר את המטריצה כמערך `A`. יש למלא את `A` בהתאם.

**דוגמא:**
המטריצה:
```
0 0 4 0 7
3 0 0 0 0
9 1 0 6 0
0 0 0 0 0
```
תוכן הקובץ:
```
0 4 2 7 4
1 3 0
2 9 0 1 1 6 3
3
```""" + CHOOSE

Q3_SOL = r"""```c
#define COLS 5 //example

void file_to_sparse_matrix(char *filename, int A[][COLS], int
rows, int cols)
{
    int i, j, num;
    char ch;
    FILE *fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            A[i][j] = 0;
    for (i = 0; i < rows; i++)
    {
        fscanf(fptr,"%d", &num); //number of row
        while ((ch = fgetc(fptr)) != '\n')
        {
            fscanf(fptr, "%d%d", &num, &j);
            A[i][j] = num;
        }
    }
    fclose(fptr);
}
```"""

# ---------------------------------------------------------------- Q4 (american items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים. **התשובה הנכונה ללא נימוק או עם נימוק לא נכון תזכה רק בנקודה אחת.** \"לפי כללי שפת C\" הינו גם יכול להיות נימוק מקובל. (שאלה 4, 20 נק' בסך הכול.)\n"

Q4A_TEXT = Q4_INTRO + "מה לא מאותחל כברירת המחדל?"
Q4A_OPTS = opts("משתנה מסוג `static`",
                "משתנה גלובלי",
                "האיבר האחרון של מערך סטטי בו האיברים הראשונים מאותחלים באופן מפורש בהצהרה",
                "איברי מערך דינאמי שהוקצה באמצעות פונקציית `calloc`",
                "התו האחרון במערך תווים סטטי",
                "סמן המיקום הנוכחי בקובץ ברגע פתיחתו",
                "כל הנתונים שניתנו כאן מאותחלים כברירת המחדל")
Q4A_EXPL = r"""כברירת המחדל: משתנים `static` וגלובלי מאותחלים ב-0, איברים אחרונים במערך סטטי מאותחלים ב-0 אם איברים ראשונים מאותחלים במפורש, איברי מערך דינאמי שהוקצה באמצעות `calloc` מאותחלים ב-0, המיקום הנוכחי בקובץ הוא תחילת הקובץ בפתיחה לקריאה או לכתיבה וסוף הקובץ בפתיחה להוספה.
במקרה הכללי אף איבר של מערך סטטי לא מאותחל כברירת המחדל.

**הערה:** "מערך סטטי" בשאלה פירושו מערך רגיל בגודל קבוע (מקומי, לא דינאמי), ובו התו האחרון, כמו שאר האיברים, אינו מאותחל אלא אם הוגדר במפורש. מערך שהוגדר עם המילה `static` (או מערך גלובלי) הוא מקרה אחר: כל איבריו מאותחלים ב-0 לפי כללי C, ולכן על מערך כזה התשובה הזו לא הייתה נכונה."""

Q4B_TEXT = Q4_INTRO + "מה קורה בצד שמאל של מספר `unsigned` לאחר ביצוע פעולת הזזת סיביות ימינה בתוכו?"
Q4B_OPTS = opts("מצד שמאל המספר מתמלא ב-0-ים", "מצד שמאל המספר מתמלא ב-1-ים",
                "מצד שמאל המספר מתמלא בסיביות שהלכו לאיבוד מצד ימין", "שיטת מילוי המספר מצד שמאל תלויה במערכת",
                "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C."

Q4C_TEXT = Q4_INTRO + "מהו `\"abcd\" - \"xyz\"` ?"
Q4C_OPTS = opts("מחרוזת", "כתובת", "מספר שלם", "הפעולה היא בלתי חוקית מבחינת המהדר", "אף תשובה אינה נכונה")
Q4C_EXPL = "מחרוזת כבועה במשפט היא כתובת של התו הראשון שלה. לפי כללי אריתמטיקת מצביעים הפרש הכתובות זה מספר שלם."

Q4D_TEXT = Q4_INTRO + r"""נניח שבן-אדם פותח קובץ בינארי באמצעות עורך טקסט. מהי הטענה הנכונה לגבי נתונים הנשמרים בקובץ?
* "לא ניתן לקריאה על ידי בני אדם" פירושו: אדם יראה ג'יבריש ("קשקוש").
* "ניתן לקריאה על ידי בני אדם" פירושו: אדם יוכל לראות את הערך שבו מדובר ולא ג'יבריש."""
Q4D_OPTS = opts("מספרים שלמים ניתנים לקריאה ע\"י בן-אדם כאשר תווים לא ניתנים לקריאה ע\"י בן-אדם",
                "מספרים שלמים לא ניתנים לקריאה ע\"י בן-אדם כאשר תווים ניתנים לקריאה ע\"י בן-אדם",
                "גם מספרים שלמים וגם תווים לא ניתנים לקריאה ע\"י בן-אדם",
                "גם מספרים שלמים וגם תווים ניתנים לקריאה ע\"י בן-אדם אם רק מספרים שלמים או רק תווים נשמרים בקובץ אולם הם לא ניתנים לקריאה אם מופיעים בקובץ ביחד",
                "גם מספרים שלמים וגם תווים תמיד ניתנים לקריאה ע\"י בן-אדם")
Q4D_EXPL = "קובץ בינארי הוא רצף בתים (כמו בזיכרון פנימי). מצד שני תו זה בית אחד ולכן כל בית מופיע כתו. אזי בן-אדם יראה את התווים כמו שהם אבל מספרים יראה כקשקוש."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <string.h>
#include <math.h>

void main()
{
      int n = strlen("\\\\"), m = strlen("\n\n\0\n"), k =
strlen("////");
      char *s = "Ah!", *x = s + m;
      puts( (char *)( (long long)(pow((int)x, n) - k) / (int)(x + m) )
);
}
```
חובה לנמק את התשובה! התשובה ללא נימוק או עם נימוק לא נכון לא תזכה בנקודות."""

Q5_SOL = r"""**הפלט:**
```
Ah!
```
**נימוק:**
סדרת escape שהתו הראשון שלה הוא `'\'` מציגה לא את עצמה אלא איזה תו אחר. במיוחד `'\n'` זה תו של סוף השורה, `'\0'` זה תו של סוף המחרוזת, `'\\'` זה תו `'\'` עצמו. לכן מחרוזת `"\\\\"` מורכבת מ-2 תווים ואורכה הוא 2.
ב-`"\n\n\0\n"` יש שני תווים עד לסוף המחרוזת ואורכה 2. מחרוזת `"////"` מורכבת מתווים רגילים ואורכה 4. אזי `n=2`, `m=2`, `k=4` ו-`x=s+2`.
Casting ל-`long long` ול-`int` ממיר כתובת (ערך `x`) למספר שלם. `(x^2-4)/(x+2)=(x-2)(x+2)/(x+2)=x-2=s+2-2=s`
Casting ל-`char *` קובע ערך `s` ככתובת של התו הראשון במחרוזת. לכן `puts` מקבלת מחרוזת `s` ומדפיסה את התוכן שלה `"Ah!"`.

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הנימוק מניח שכתובת נכנסת ב-`int` (מערכת של 32 סיביות). בהרצה אמיתית (`tools/verify/20B-B/q5.c`) הקומפילציה ל-32 סיביות מדפיסה `Ah!`, ואילו בקומפילציה ל-64 סיביות ה-cast ל-`int` קוטם את הכתובת והתוכנית קורסת.

**הערה על דיוק:** גם במערכת של 32 סיביות הפלט `Ah!` אינו מובטח. הפונקציה `pow` מחשבת ב-`double`, שמייצג במדויק רק מספרים שלמים עד $2^{53}$. כשהכתובת $x$ גדולה מכ-$2^{26}$ (כ-64MB), הערך $x^2$ גדול מדי ונעגל, והחילוק `(long long)(pow(x,2)-4)/(x+2)` יוצא לעיתים $x-3$ במקום $x-2$, כך שהמצביע שמתקבל הוא `s-1` ולא `s` (בבדיקה על כתובות אקראיות מעל 64MB קרה בכ-30%-45% מהמקרים). הפלט `Ah!` מובטח אפוא רק כשהכתובת קטנה מ-64MB, וגם אז רק בהנחת מערכת של 32 סיביות."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/20B-B-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    M("א", "c_traps_mcq", Q4A_TEXT, Q4A_OPTS, "e", Q4A_EXPL),
    M("ב", "bit_manipulation", Q4B_TEXT, Q4B_OPTS, "a", Q4B_EXPL),
    M("ג", "pointers", Q4C_TEXT, Q4C_OPTS, "c", Q4C_EXPL),
    M("ד", "files", Q4D_TEXT, Q4D_OPTS, "b", Q4D_EXPL),
    Q(5, "code", "c_basics_output", Q5_TEXT, Q5_SOL, points=10),
]

# ---------------------------------------------------------------- steps / rubric / pitfalls (ai-draft)
# Every expected value below was produced by a real clang run: tools/verify/<CODE>/steps_check.py
import re


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def code_of(sol, n=0):
    return re.findall(r"```c\n(.*?)\n```", sol, re.S)[n]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip()]


def ix(lines, text, nth=None):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == text.strip()]
    if nth is None:
        assert len(idx) == 1, (text, idx)
        return idx[0]
    return idx[nth]


def blocks(lines, *starts):
    """Logical blocks: each start is the (unique) first line of a block; block 0 begins at line 0."""
    cuts = [0] + sorted(ix(lines, *(s if isinstance(s, tuple) else (s,))) for s in starts)
    assert len(set(cuts)) == len(cuts), starts
    return ["\n".join(lines[a:b]) for a, b in zip(cuts, cuts[1:] + [len(lines)])]


def swap1(lines, old, new):
    """The lines with exactly one line changed (asserted)."""
    i = ix(lines, old)
    out = list(lines)
    out[i] = out[i].replace(old.strip(), new.strip())
    assert out[i] != lines[i]
    return out, i


def blank(lines, target):
    i = ix(lines, target)
    out = list(lines)
    out[i] = out[i][:len(out[i]) - len(out[i].lstrip())] + "___"
    return out, i


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            assert "hold" not in q and q["kind"] != "mcq", (num, part)
            q.update(kw)
            return
    raise KeyError((num, part))


def step(type_, **kw):
    s = {"type": type_}
    s.update(kw)
    return s

# ---- Q1: group_sort
S1 = lines_of(code_of(Q1_SOL))
S1_bug, S1_bi = swap1(S1, "if (islower(str[i]))", "if (isupper(str[i]))")
S1_fb, S1_bl = blank(S1, "if (str[i] < last_capital)")

add(1,
    rubric=rub(("שלושה משתנים `last_capital`, `last_small`, `last_digit` שמחזיקים את התו האחרון שנראה בכל קבוצה, מאותחלים ל-`'\\0'`", 8),
               ("סיווג כל תו עם `isupper` / `islower` / `isdigit`; תווים אחרים מתעלמים מהם", 8),
               ("השוואת התו רק לתו האחרון מאותה קבוצה: אם הוא קטן ממנו מחזירים `0`", 12),
               ("עדכון התו האחרון של הקבוצה כשאין הפרה (שוויון מותר)", 6),
               ("החזרת `1` רק אחרי שהמחרוזת נסרקה כולה", 6)),
    rubricSource="ai-verified",
    pitfalls=["להשוות כל תו לתו הקודם במחרוזת כולה: התווים מקבוצות אחרות שמשובצים ביניהם גורמים לפסילה שגויה.",
              "להשתמש ב-`<=` במקום `<` ולפסול תו שחוזר פעמיים באותה קבוצה (כמו `P` פעמיים בדוגמה התקינה).",
              "לא להתעלם מתווים שאינם אות או ספרה (כמו `$` או `#`) ולהשוות גם אותם."],
    steps=[
        step("numeric", prompt="במחרוזת השנייה בדוגמה, `\"B4$Ca#%ds5P8P&9rY\"`, באיזה אינדקס (מ-0) נמצא התו שגורם לפונקציה להחזיר `0`?",
             answer=15, tol=0,
             explain="התו `'r'` באינדקס 15 קטן מהאות הקטנה הקודמת `'s'` (אינדקס 8). עד אינדקס 14 כל הקבוצות ממוינות (ריצה אמיתית: הקידומת באורך 15 מחזירה 1 והקידומת באורך 16 מחזירה 0)."),
        step("choice", prompt="לאיזו מהמחרוזות הבאות הפונקציה מחזירה `0`?",
             options=opts("`\"a1Ab2B\"`", "`\"Ba1\"`", "`\"c9Ab0B\"`", "`\"A1a2B\"`"), correctId="c",
             explain="ב-`\"c9Ab0B\"` הספרות הן 9 ואז 0, כלומר ירידה בקבוצת הספרות. בשאר המחרוזות כל קבוצה עולה (אותיות קטנות, אותיות גדולות וספרות בנפרד), ולכן מוחזר `1` (ריצה אמיתית)."),
        step("fillblank", prompt="השלימו את הבדיקה של האותיות הגדולות. שימו לב שאות גדולה יכולה לחזור פעמיים, כמו `P` בדוגמה התקינה.",
             code=True, lines=S1_fb, blankIndex=S1_bl,
             options=opts("if (str[i] < last_capital)", "if (str[i] <= last_capital)",
                          "if (str[i] > last_capital)", "if (str[i] != last_capital)"),
             correctId="a",
             explain="הפרה היא רק אות קטנה יותר מהאחרונה בקבוצה. עם `<=` נפסלת המחרוזת התקינה בגלל `P` פעמיים, ועם `>` או `!=` נפסלת כל סדרה עולה של אותיות גדולות (ריצה אמיתית)."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה והפונקציה מחזירה `1` על המחרוזת השנייה בדוגמה, שאינה ממוינת בקבוצות. מצאו אותה.",
             code=True, lines=S1_bug, bugIndex=S1_bi,
             explain="`isupper` במקום `islower`: האותיות הקטנות אף פעם לא נבדקות, ולכן ההפרה `'r'` אחרי `'s'` לא מתגלה."),
    ],
    stepsSource="ai-verified")

# ---- Q2: arr_of_lists_to_list_of_prefixes
S2 = lines_of(code_of(Q2_SOL))
_i0 = ix(S2, "int is_prefix(Item *L1, Item *L2)")
_i1 = ix(S2, "return 1;") + 1
S2_ord = blocks(S2[_i0:_i1 + 1], "while (L1 && L2)", "if (L1)", "return 1;")
S2_bug, S2_bi = swap1(S2, "if (L1->data != L2->data)", "if (L1->data == L2->data)")
S2_fb, S2_bl = blank(S2, "if (L1)")

add(2,
    rubric=rub(("פונקציית עזר שסורקת שתי רשימות במקביל ומחזירה `0` ברגע ששדות `data` שונים", 10),
               ("אם בסוף הסריקה `L` (הרשימה הנבדקת) עדיין לא נגמרה, היא ארוכה מהרשימה במערך ולכן אינה תחילית, מחזירים `0`", 6),
               ("רשימה ריקה היא תחילית של כל רשימה (הלולאה לא רצה ומחזירים `1`)", 4),
               ("בניית איבר חדש עם `malloc` שמכיל את האינדקס `i` (ולא מצביע לרשימה) והוספתו לרשימה החדשה", 8),
               ("מעבר על כל איברי המערך `A`", 6),
               ("החזרת ראש הרשימה החדשה, או `NULL` כשהיא ריקה", 6)),
    rubricSource="ai-verified",
    pitfalls=["להתעלם מהמקרה ש-`L` ארוכה מהרשימה במערך: אחרי הלולאה הרשימה הקצרה נגמרת ו-`L` עדיין לא, אבל הפונקציה מחזירה `1`.",
              "להשוות כתובות איברים (`L1 == L2`) במקום את שדות `data`.",
              "לשמור ברשימה החדשה מצביעים לרשימות ולא את האינדקסים שלהן."],
    steps=[
        step("numeric", prompt="המערך `A` מכיל ארבע רשימות: $[1,2,3]$, $[1,2]$, $[4,1,2]$, $[1,2,3,4]$, והרשימה הנבדקת היא $L=[1,2,3]$. כמה איברים יש ברשימה החדשה?",
             answer=2, tol=0,
             explain="$L$ היא תחילית של $[1,2,3]$ (אינדקס 0) ושל $[1,2,3,4]$ (אינדקס 3). ב-$[1,2]$ היא ארוכה מדי, וב-$[4,1,2]$ האיבר הראשון שונה (ריצה אמיתית: האינדקסים 0 ו-3)."),
        step("numeric", prompt="מה מחזירה `is_prefix(L, A[1])` עבור $L=[1,2,3]$ ו-$A[1]=[1,2]$?",
             answer=0, tol=0,
             explain="הלולאה נעצרת כש-`A[1]` נגמרת, אבל ב-`L` נשאר האיבר 3, ולכן `if (L1) return 0` מחזירה `0` (ריצה אמיתית: 0)."),
        step("fillblank", prompt="השלימו את הבדיקה שאחרי הלולאה ב-`is_prefix`.",
             code=True, lines=S2_fb, blankIndex=S2_bl,
             options=opts("if (L1)", "if (L2)", "if (!L1)", "if (L1 && L2)"), correctId="a",
             explain="אם `L1` (הרשימה הנבדקת) לא נגמרה, היא ארוכה מ-`L2` ואינה תחילית. עם `L2` נפסלות רשימות ארוכות יותר שבהן `L` היא תחילית, עם `!L1` נפסלות התחיליות התקינות, ועם `L1 && L2` (תמיד שקר אחרי הלולאה) כל רשימה קצרה מדי תתקבל בטעות."),
        step("order", prompt="סדרו את גושי הפונקציה `is_prefix`.",
             code=True, lines=S2_ord,
             explain="קודם סורקים את שתי הרשימות במקביל, אחר כך בודקים אם `L1` נשארה, ורק אם כל הבדיקות עברו מחזירים `1`."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה והפונקציה פוסלת תחיליות תקינות. מצאו אותה.",
             code=True, lines=S2_bug, bugIndex=S2_bi,
             explain="`==` במקום `!=`: הפונקציה מחזירה `0` דווקא כשהערכים שווים, כלומר מקבלת רק רשימות שאינן תחילית."),
    ],
    stepsSource="ai-verified")

# ---- Q3: file_to_sparse_matrix
S3 = lines_of(code_of(Q3_SOL))
S3_ord = blocks(S3, "void file_to_sparse_matrix(char *filename, int A[][COLS], int", "if (!fptr)",
                ("for (i = 0; i < rows; i++)", 1), "fclose(fptr);")
S3_bug, S3_bi = swap1(S3, "for (j = 0; j < cols; j++)", "for (j = 1; j < cols; j++)")
S3_fb, S3_bl = blank(S3, "A[i][j] = num;")

add(3,
    rubric=rub(("הגדרת הקבוע `COLS` לפני הפונקציה, ופרמטר מערך סטטי `int A[][COLS]`", 6),
               ("פתיחת הקובץ לקריאה ויציאה (`exit(1)`) אם לא נפתח", 4),
               ("איפוס כל איברי `A` (`rows` על `cols`) לפני הקריאה", 8),
               ("בכל שורה: קריאת מספר השורה בהתחלה, ואחריו קריאת זוגות עד תו סוף השורה (`fgetc` שמזהה `'\\n'`)", 12),
               ("כל זוג הוא (ערך, עמודה): קריאה עם `\"%d%d\"` והצבת `A[i][j] = num`", 8),
               ("סגירת הקובץ", 2)),
    rubricSource="ai-verified",
    pitfalls=["לא לאפס את `A` לפני הקריאה: האיברים שאינם בקובץ יישארו עם ערכים ישנים.",
              "להחליף בין סדר הערך והעמודה בקובץ (הזוג הוא ערך ואז עמודה), או לשכוח לקרוא את מספר השורה שבתחילת כל שורה.",
              "לקרוא עד סוף הקובץ ללא זיהוי סוף שורה, ולכן לא לדעת איזה זוג שייך לאיזו שורה (שורה בלי זוגות, כמו השורה האחרונה בדוגמה)."],
    steps=[
        step("numeric", prompt="תוכן הקובץ בדוגמה: שורה 2 היא `2 9 0 1 1 6 3`. מה הערך של `A[2][3]` אחרי הקריאה?",
             answer=6, tol=0,
             explain="אחרי מספר השורה 2 באים הזוגות (9, עמודה 0), (1, עמודה 1), (6, עמודה 3). הערך 6 נכתב ב-`A[2][3]` (ריצה אמיתית: 6)."),
        step("numeric", prompt="כמה איברים שאינם אפס יש במטריצה המשוחזרת מהקובץ בדוגמה (ארבע שורות: `0 4 2 7 4`, `1 3 0`, `2 9 0 1 1 6 3`, `3`)?",
             answer=6, tol=0,
             explain="בשורה 0 שני זוגות, בשורה 1 זוג אחד, בשורה 2 שלושה זוגות ובשורה 3 אין זוגות: $2+1+3+0=6$ (ריצה אמיתית: 6)."),
        step("fillblank", prompt="השלימו את ההצבה בתוך הלולאה שקוראת זוג (ערך, עמודה).",
             code=True, lines=S3_fb, blankIndex=S3_bl,
             options=opts("A[i][j] = num;", "A[j][i] = num;", "A[i][j] = 1;", "A[i][i] = num;"), correctId="a",
             explain="`i` הוא מספר השורה ו-`j` העמודה שנקראה מהקובץ, ו-`num` הערך. החלפת השורה והעמודה, כתיבת `1` במקום הערך או כתיבה על האלכסון נותנות מטריצה שונה (ריצה אמיתית)."),
        step("order", prompt="סדרו את גושי הפונקציה `file_to_sparse_matrix`.",
             code=True, lines=S3_ord,
             explain="הקבוע לפני הפונקציה, אחריו פתיחת הקובץ, ואיפוס המטריצה לפני שמציבים בה ערכים; בסוף סוגרים את הקובץ."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה, ועמודה 0 במטריצה לא תמיד מאופסת. מצאו אותה.",
             code=True, lines=S3_bug, bugIndex=S3_bi,
             explain="הלולאה מתחילה מ-`j = 1`, ולכן `A[i][0]` נשאר עם הערך שהיה בו קודם כשאין בקובץ איבר בעמודה 0 של השורה."),
    ],
    stepsSource="ai-verified")

add(5,
    rubric=rub(("אורכי המחרוזות: `strlen(\"\\\\\\\\\")` הוא 2, `strlen(\"\\n\\n\\0\\n\")` הוא 2 (נעצרים ב-`\\0`) ו-`strlen(\"////\")` הוא 4", 4),
               ("`x = s + m = s + 2`", 2),
               ("$(x^2-4)/(x+2) = x-2$, ולכן מקבלים `x - 2 = s`", 2),
               ("`puts` מקבלת את `s` ומדפיסה `Ah!`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לספור את `\"\\\\\\\\\"` כארבעה תווים: כל `\\\\` הוא תו אחד.",
              "לספור את התו שאחרי `\\0` ב-`\"\\n\\n\\0\\n\"`: `strlen` נעצרת ב-`\\0`.",
              "לשכוח שהפתרון הרשמי מניח כתובת בגודל `int` (32 סיביות): ב-64 סיביות ההמרה `(int)x` חותכת את הכתובת."],
    steps=[
        step("numeric", prompt="מה ערך `strlen(\"\\\\\\\\\")`, כלומר אורך המחרוזת שמורכבת מארבעה תווי `\\` בקוד המקור?",
             answer=2, tol=0,
             explain="כל `\\\\` בקוד המקור הוא תו `\\` אחד, ולכן יש 2 תווים (ריצה אמיתית: 2)."),
        step("numeric", prompt="מה ערך `strlen(\"\\n\\n\\0\\n\")`?", answer=2, tol=0,
             explain="`strlen` סופרת עד התו `\\0` הראשון: שני התווים `\\n` לפניו בלבד (ריצה אמיתית: 2)."),
        step("choice", prompt="נסמן `x = s + 2`, כש-`n = 2`, `m = 2`, `k = 4`. למה שווה $(x^n - k)/(x + m)$?",
             options=opts("$x-2$", "$x+2$", "$x$", "$x-4$"), correctId="a",
             explain="$(x^2-4)/(x+2)=(x-2)(x+2)/(x+2)=x-2$ (אומת ב-sympy). אחרי הצבת $x=s+2$ מתקבל $s$."),
        step("text", prompt="מה מודפס? (בהנחה, כמו בפתרון הרשמי, שכתובת נכנסת בתוך `int`)", accept=["Ah!"], normalize="none",
             explain="התוצאה היא הכתובת `s` של המחרוזת `\"Ah!\"`, ו-`puts` מדפיסה אותה: `Ah!` (אומת בריצה עם כתובת בטווח של 32 סיביות)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "20B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תש\"ף, מועד ב'",
    "year": 2020,
    "examDate": "02.08.2020",
    "sourceFile": "20B-B exam",
    "solutionFile": "20B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
