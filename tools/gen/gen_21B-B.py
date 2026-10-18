# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-B.json -- programming-workshop (C), semester B 2021, moed B (13.07.2021).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of three). Part 2: Q4 (20 pts, four pick-and-justify items).
Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/21B-B/. Q1: official solution with a minimal fix (arbiter, tools/verify/21B-B/arb_*).
Run: PYTHONUTF8=1 py tools/gen/gen_21B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-B.json"
IDS = "abcdefgh"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CHOOSE = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש.*"

# ---------------------------------------------------------------- Q1 (official + minimal fix)
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזות `infile_1`, `infile_2` ו-`outfile` המהוות שמות של שלושה קבצי טקסט.
תוכן של כל שורה בקבצים `infile_1` ו-`infile_2` הוא רצף של מספרים שלמים **ממוינים** (מתחילת השורה עד סופה) מופרדים ברווחים. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה למלא קובץ `outfile` כך שתוכן שורה מס' `i` בתוכו יהיה רצף **ממוין** (מתחילת השורה עד סופה) של כל המספרים ששייכים לשורות מס' `i` בקבצים `infile_1` ו-`infile_2`.
אם מספרי השורות בקבצים `infile_1` ו-`infile_2` הם שונים (נסמן אותם ב-`n` ו-`m` כך שלמשל `n>m`) אז קובץ `outfile` יכלול `n` שורות כך ש-`n-m` השורות האחרונות יועתקו מהקובץ התואם.

**דוגמא:**
`infile_1`:
```
3 8 12 16 20
0 2 2 6
9 10 10 11 19 26
4 4 4 5
```
`infile_2`:
```
9 17
2 6 7 11
5 13 14 18
```
`outfile`:
```
3 8 9 12 16 17 20
0 2 2 2 6 6 7 11
5 9 10 10 11 13 14 18 19 26
4 4 4 5
```""" + CHOOSE

Q1_SOL = r"""**הפתרון הרשמי עם תיקון:** אחרי לולאת המיזוג הפתרון הרשמי מחזיר את שני הקבצים תו אחד אחורה (`fseek(in1, -1, SEEK_CUR); fseek(in2, -1, SEEK_CUR);`), וזה מוסיף ל-`outfile` שורות ריקות (בדוגמה: שורה ריקה בסוף). התיקון: רק `in1` מחזירים תו אחורה, ורק אם הוא לא הגיע ל-EOF (`if (!feof(in1))`). שאר הקוד הוא הפתרון הרשמי.

```c
/* Auxiliary function. Copy a number from file to file
and input of a next number */
void next_number(FILE* in, FILE* out, int* num, char* ch)
{
    fprintf(out, "%d ", *num);
    if ((*ch = fgetc(in)) != '\n')
        fscanf(in, "%d", num);
}

/* Auxiliary function.
Merging 2 sorted rows of 2 files into a sorted row in a new file */
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{
    char ch1=0, ch2=0;
    int num1, num2;

    /* Merging rows until one of the rows ends */
    fscanf(in1, "%d", &num1);
    fscanf(in2, "%d", &num2);
    while (ch1 != '\n' && ch2 != '\n')
        if (num1 < num2)
            next_number(in1, out, &num1, &ch1);
        else
            next_number(in2, out, &num2, &ch2);

    /* Copying remainder of a longer row */
    while (ch1 != '\n')
        next_number(in1, out, &num1, &ch1);
    while (ch2 != '\n')
        next_number(in2, out, &num2, &ch2);

    fputc('\n', out);
}

/* Auxiliary function */
void copy_file(FILE* in, FILE* out)
{
    char ch;
    while ((ch = fgetc(in)) != EOF)
        fputc(ch, out);
}

void filesMerge(char* infile1, char* infile2, char* outfile)
{
    FILE* in1 = fopen(infile1, "r");
    FILE* in2 = fopen(infile2, "r");
    FILE* out = fopen(outfile, "w");
    if (!in1 || !in2 || !out)
        exit(1);

    /* Merging file rows until one of the files ends */
    while (fgetc(in1) != EOF && fgetc(in2) != EOF)
    {
        fseek(in1, -1, SEEK_CUR);
        fseek(in2, -1, SEEK_CUR);
        rows_merge(in1, in2, out);
    }

    /* Copying remainder of a larger file */
    /* fix: only in1 can have one character read past the common rows */
    if (!feof(in1))
        fseek(in1, -1, SEEK_CUR);
    copy_file(in1, out);
    copy_file(in2, out);

    fclose(in1);
    fclose(in2);
    fclose(out);
}
```

**הערה:** למה התיקון נכון: הלולאה `while (fgetc(in1) != EOF && fgetc(in2) != EOF)` נעצרת באחד משני מצבים. אם `in1` נגמר, `fgetc(in2)` לא מתבצע בכלל (הערכה מקוצרת של `&&`), ולכן `in2` עומד בדיוק בתחילת השורות שנותרו בו. אם `in2` נגמר, מ-`in1` כבר נקרא התו הראשון של השורה הבאה, ורק אותו צריך להחזיר. בפתרון הרשמי המקורי `fseek(-1)` על קובץ שלא נקרא או שכבר הגיע ל-EOF מחזיר אותו אל ה-`
` של השורה הקודמת, ו-`copy_file` מעתיק אותו כשורה ריקה (כש-`infile_2` ארוך יותר השורות הריקות נוצרות באמצע הקובץ).

בנוסף: כל מספר נכתב עם `"%d "`, ולכן בשורות הממוזגות יש רווח לפני `
`. בהרצה ב-Windows הקבצים נפתחו במצב בינארי, כי `fseek` אחורה בקובץ שנפתח במצב טקסט אינו מובטח בתקן ונכשל בספרייה של Windows (`tools/verify/21B-B/arb_q1.c`)."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס `person` אשר מהווה שם משפחה, שם פרטי ומס' זהות של בן-אדם:
```c
typedef struct {
    char last_name[30], first_name[30];
    unsigned id;
} person;
```
כתוב פונקציה בוליאנית אשר מקבלת מערך איברים מסוג `person` וגודלו.
על הפונקציה להחזיר `1` אם המערך ממוין בסדר עולה ולהחזיר `0` אחרת.

נגדיר מערך איברים מסוג `person` כ**ממוין בסדר עולה** אם:
1. איברי המערך ממוינים בסדר לקסיקוגרפי עולה ממש לפי שמות המשפחה (שדה `last_name`);
2. כאשר בין איברי המערך יש איברים בעלי שדות `last_name` זהים, האיברים הללו ממוינים בסדר לקסיקוגרפי עולה ממש לפי שמות פרטיים (שדה `first_name`);
3. כאשר בין איברי המערך יש איברים בעלי שדות `last_name` זהים וגם שדות `first_name` זהים, האיברים הללו ממוינים בסדר עולה לפי מספרי הזהות (שדה `id`).

**דוגמאות:**
עבור המערך הבא
```
0 Asher Mike 231567809
1 Bern David 216578900
2 Borgman Joseph 354678903
3 Cohen Abraham 224567821
4 Cohen Den 206666431
5 Levi Ilan 290876441
6 Levi Omri 245689432
7 Levi Omri 245689436
8 Smith Jack 345389010
9 Smith John 311232111
```
הפונקציה תחזיר `1`.

עבור המערך הבא
```
0 Asher Mike 231567809
1 Bern David 216578900
2 Borgman Joseph 354678903
3 Cohen Abraham 224567821
4 Cohen Den 206666431
5 Levi Ilan 290876441
6 Levi Omri 245689436
7 Levi Omri 245689432
8 Smith Jack 345389010
9 Smith John 311232111
```
הפונקציה תחזיר `0`.""" + CHOOSE

Q2_SOL = r"""```c
int ordered_person_array(person* person_arr, int n)
{
    int i, cmp;
    for (i = 1; i < n; i++)
        if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) < 0 )
            return 0;
        else
            if (cmp == 0)
                if ((cmp=strcmp(person_arr[i].first_name, person_arr[i-1].first_name))<0)
                    return 0;
                else
                    if (cmp == 0)
                        if (person_arr[i].id < person_arr[i - 1].id)
                            return 0;
    return 1;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**מטריצה דלילה** הינה מטריצה שמרבית איבריה בעלי ערך אפס.

כתוב פונקציה אשר מקבלת מטריצה דלילה `A` המיושמת כמערך של רשימות מקושרות (היישום החסכוני, כאשר מופיעים ברשימה רק איברי המטריצה שאינם בעלי ערך אפס). רשימה מס' `i` של המערך תתאים לשורה מס' `i` של מטריצה `A`.
איברי הרשימות יכילו ערך שהוא איבר המטריצה וגם ערך שהוא מס' העמודה בה הוא נמצא במטריצה.
הפונקציה תקבל כפרמטרים את מערך הרשימות וגודלו וגם את מספר העמודות במטריצה.

על הפונקציה לשחזר את המטריצה כמערך דו-ממדי **דינאמי** שכל שורותיו באותו גודל.
הפונקציה תחזיר כתובת של המערך הדו-ממדי הדינאמי הבנוי.

**דוגמא:** (באיור: משמאל המטריצה `A`, מימין מערך הרשימות שלה)

בדוגמא הנ"ל הפונקציה תקבל את `A` כמערך רשימות, את גודל המערך, 4, וגם את מספר העמודות ב-`A`, 5.

יש להגדיר את הטיפוס של איברי הרשימה מעל הפונקציה.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.""" + CHOOSE

Q3_SOL = r"""```c
typedef struct element
{
    int data;
    int col;
    struct element* ptr_next;
} element;

int** lists_to_sparse_matrix(element** list_row, int rows, int cols)
{
    int** arr, i;
    element* ptr;
    arr = (int**)calloc(rows, sizeof(int*));
    for (i = 0; i < rows; i++)
        arr[i] = (int*)calloc(cols, sizeof(int));

    for (i = 0; i < rows; i++)
    {
        ptr = list_row[i];
        while (ptr)
        {
            arr[i][ptr->col] = ptr->data;
            ptr = ptr->ptr_next;
        }
    } // for i
    return arr;
}
```"""

# ---------------------------------------------------------------- Q4 (20 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 20 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + r"""מהו פלט (משמאל לימין) של התוכנית הבאה?
```c
#include <stdio.h>

int x;

void f() {
    static int x;
    printf("%d", x);
    printf("%d", ++x);
}

void main() {
    f();
    printf("%d", x);
    printf("%d", ++x);
    f();
}
```"""
Q4A_OPTS = opts("`010101`", "`000000`", "`000011`", "`010112`", "`011223`", "התוכנית אינה תקינה", "אף תשובה אינה נכונה")

Q4A_EXPL = r"""כברירת מחדל ערך התחלתי של `static x` הוא 0. לכן בקריאה ראשונה של `f()` מדפיסים 0, מקדמים `x` ומדפיסים 1. אחרי זה מדפיסים ערך התחלתי של `x` גלובלי ששווה ל-0, מקדמים `x` גלובלי ומדפיסים 1. בקריאה שנייה של `f()` מדפיסים `static x` שערכו נשאר 1, מקדמים `x` ומדפיסים 2."""

Q4B_TEXT = Q4_INTRO + r"""כמה פעמים יודפס `Hi` עקב ביצוע התוכנית הבאה?
```c
#include <stdio.h>
void main() {
    int i = 64;
    for (; i; i >>= 1)
        printf("Hi \n");
}
```"""
Q4B_OPTS = opts("פעם אחת", "7 פעמים", "64 פעמים", "אף פעם", "תהיה לולאה אינסופית", "אף תשובה אינה נכונה")
Q4B_EXPL = r"""ייצוג בינארי של 64 הוא 1000000 (6 אפסים, 7 סיביות). כל פעולה `i >>= 1` מביאה להזזה של 1 בסיבית אחת ימינה. לכן תוך 7 בדיקות (6 הזזות) סיבית 1 תהיה עוד במספר `i`, ערך של `i` יהיה שונה מ-0 ותנאי המשך הלולאה יתקיים. אחרי הזזה שביעית 1 יצאה מייצוג בינארי של `i` אשר יהיה מורכב רק מאפסים, ולכן ערך עשרוני שלו יהיה 0 כך שתנאי המשך הלולאה בבדיקה שמינית לא יתקיים."""

Q4C_TEXT = Q4_INTRO + r"""נתון פוינטר ל-`int p` שמצביע למערך דינאמי. למה יצביע `p` אחרי ביצוע פעולת `p = (int*)realloc(p, 0);`?"""
Q4C_OPTS = opts("לאותו מערך", "לאיזשהו מקום חדש", "`p` יהיה שווה ל-`NULL`", "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4C_EXPL = r"""לפי כללי שפת C כאשר גודל חדש של בלוק זיכרון ב-`realloc` שווה ל-0, הפונקציה מחזירה `NULL`.

**הערה:** זו התשובה לפי המפתח הרשמי, אבל היא תלויה במימוש: ב-C17 התוצאה של `realloc(p, 0)` מוגדרת-מימוש (חלק מהספריות משחררות את הבלוק ומחזירות `NULL`, כמו glibc ו-MSVC, וחלק מחזירות מצביע ייחודי), וב-C23 ההתנהגות אינה מוגדרת."""

Q4D_TEXT = Q4_INTRO + r"""בתוכנית בה `a` מוגדר כמשתנה מסוג `int` ו-`fptr1` ו-`fptr2` הם פוינטרים לקבצים בינאריים קיימות שתי השורות הבאות:
```c
fread(&a, sizeof(a), 1, fptr1);
fwrite(&a, sizeof(a), 1, fptr2);
```
מהי הטענה הנכונה?"""
Q4D_OPTS = opts("ברשימת פרמטרי `fread` בשורה הראשונה יש סימן `&` מיותר והשורה השנייה תקינה",
                "ברשימת פרמטרי `fwrite` בשורה השנייה יש סימן `&` מיותר והשורה הראשונה תקינה",
                "ברשימות פרמטרי `fread` ו-`fwrite` יש סימן `&` מיותר",
                "שתי השורות תקינות",
                "באחת מהשורות או בשתי השורות סימן `&` נמצא במקום לא נכון",
                "אף טענה אינה נכונה")
Q4D_EXPL = r"""גם `fread` וגם `fwrite` מקבלות כפרמטר מצביע לבלוק הזיכרון. לכן צריך להציב כתובת של המשתנה."""

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
    printf("%d",printf("%d%d",printf("%d",11),printf("%d",11)));
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
1111222
```
**נימוק:**
כל אחת מהפונקציות `printf("%d",11)` מדפיסה 11, סה"כ 1111. פונקציית `printf` מחזירה מספר בתים כתובים, לכן כל אחת מהפונקציות הנ"ל מחזירה 2. אז `printf` שלישית (מימין) מדפיסה 22 (שני תווים) ומחזירה 2. לכן `printf` חיצונית (רביעית מימין) מדפיסה 2."""

questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=40,
      solutionSource="solved", official=False, confidence="med"),
    Q(2, "code", "structs_unions", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "list_manipulation", Q3_TEXT, Q3_SOL, points=40, image="images/exams/21B-B-Q3.png"),
    {"num": 4, "part": "א", "kind": "mcq", "topic": "storage_classes", "question": Q4A_TEXT,
     "options": Q4A_OPTS, "correctId": "d", "explanation": Q4A_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "b", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "dynamic_memory", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "c", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "files", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "d", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
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

S1 = lines_of(code_of(Q1_SOL))
S1_fb, S1_bl = blank(S1, "if (!feof(in1))")
S1_bug, S1_bi = swap1(S1, "if (num1 < num2)", "if (num1 > num2)")

add(1,
    rubric=rub(("פתיחת שלושת הקבצים (שניים לקריאה, אחד לכתיבה) ובדיקת הצלחה", 4),
               ("לולאה על השורות כל עוד בשני הקבצים יש שורה נוספת", 8),
               ("מיזוג שתי שורות ממוינות לשורה ממוינת אחת: השוואת המספרים הנוכחיים וקידום הקטן מביניהם, זיהוי סוף שורה לפי `\n`", 14),
               ("העתקת שארית השורה הארוכה יותר וכתיבת `\n` בסוף כל שורה ממוזגת", 6),
               ("העתקת השורות הנותרות מהקובץ הארוך יותר בלי שורות ריקות או תווים חסרים, וסגירת הקבצים", 8)),
    rubricSource="ai-verified",
    pitfalls=["להחזיר את שני הקבצים תו אחד אחורה אחרי הלולאה (כמו בפתרון הרשמי המקורי): קובץ שלא נקרא או שהגיע ל-EOF חוזר ל-`\n` הקודם, ו-`outfile` מקבל שורות ריקות.",
              "לשכוח שתנאי כמו `fgetc(in1) != EOF && fgetc(in2) != EOF` צורך תו מהקובץ, ולא להחזיר אותו (תו ראשון חסר בשורה).",
              "לזהות סוף שורה רק לפי `fscanf`, שמדלג על `\n` כרווח לבן, וכך למזג שורות שלמות זו לתוך זו."],
    steps=[
        step("numeric", prompt="מריצים את הפתרון הרשמי **המקורי** (עם `fseek(in1, -1, SEEK_CUR); fseek(in2, -1, SEEK_CUR);` אחרי הלולאה) על קבצי הדוגמה. כמה שורות ריקות יש ב-`outfile`?",
             answer=1, tol=0,
             explain="`in2` נגמר, ולכן `fseek(in2, -1, SEEK_CUR)` מחזיר אותו אל ה-`\n` האחרון שלו, ו-`copy_file(in2, out)` מעתיק אותו כשורה ריקה בסוף הקובץ (ריצה אמיתית: 1)."),
        step("fillblank", prompt="השלימו את השורה החסרה בפתרון המתוקן: מתי צריך להחזיר את `in1` תו אחד אחורה אחרי לולאת המיזוג?",
             code=True, lines=S1_fb, blankIndex=S1_bl,
             options=opts("if (!feof(in1))", "if (!feof(in2))", "if (feof(in1))", "while (!feof(in1))"),
             correctId="a",
             explain="אם `in1` לא הגיע ל-EOF, הלולאה נעצרה כי `in2` נגמר, ומ-`in1` כבר נקרא התו הראשון של השורה הבאה. `!feof(in2)` ו-`feof(in1)` לא מחזירים אותו בדוגמה, ולכן התו `4` נעלם מהשורה האחרונה, ו-`while` לא נעצר לעולם כי `fseek` לא מעלה את דגל ה-EOF (ריצה אמיתית)."),
        step("findbug", prompt="בגרסה הבאה של הפתרון המתוקן שורה אחת שונתה, והשורות הממוזגות כבר אינן ממוינות. מצאו אותה.",
             code=True, lines=S1_bug, bugIndex=S1_bi,
             explain="`num1 > num2` במקום `num1 < num2`: בכל צעד נכתב המספר הגדול מבין השניים, ולכן השורה הממוזגת אינה ממוינת (בדוגמה השורה הראשונה מתחילה ב-`9` במקום ב-`3`)."),
    ],
    stepsSource="ai-verified")


S2 = lines_of(code_of(Q2_SOL))
S2_bug, S2_bi = swap1(S2, "if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) < 0 )",
                      "if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) <= 0 )")
S2_fb, S2_bl = blank(S2, "if (person_arr[i].id < person_arr[i - 1].id)")

add(2,
    rubric=rub(("מעבר על המערך מהאיבר השני ואילך והשוואת כל איבר לקודם לו (זוגות סמוכים)", 8),
               ("השוואת שמות משפחה עם `strcmp` (ולא עם `<` על מערכי תווים); ערך שלילי מחזיר `0`", 10),
               ("כששמות המשפחה זהים (`cmp == 0`) משווים שמות פרטיים באותו אופן", 10),
               ("רק כששני השמות זהים משווים מספרי זהות, ואיבר עם `id` קטן מהקודם מחזיר `0`", 8),
               ("אם לא נמצאה הפרה בכל הזוגות מחזירים `1`", 4)),
    rubricSource="ai-verified",
    pitfalls=["להשוות מחרוזות עם `<` או `==` במקום `strcmp`: מושווים כתובות המערכים ולא התוכן.",
              "להחזיר `0` גם כששמות המשפחה זהים (תנאי `<= 0`), ובכך לפסול מערך תקין שבו יש כמה אנשים עם אותו שם משפחה.",
              "להשוות את מספר הזהות כבר כששמות המשפחה זהים אבל השמות הפרטיים שונים, במקום רק כששני השמות זהים."],
    steps=[
        step("numeric", prompt="במערך הדוגמה השני (שני ה-`Levi Omri` מוחלפים זה בזה, כך שהמספרים `245689436` ו-`245689432` מופיעים בסדר הפוך) הפונקציה מחזירה `0`. באיזה אינדקס `i` מתגלה ההפרה, כלומר איזה איבר גורם ל-`return 0`?",
             answer=7, tol=0,
             explain="האיברים 0 עד 6 עוברים את כל ההשוואות, ובאיבר 7 (`id` קטן מזה של איבר 6 עם אותם שמות) מתקבל `return 0` (ריצה אמיתית: 7)."),
        step("choice", prompt="מה משמעות התנאי `strcmp(person_arr[i].last_name, person_arr[i - 1].last_name) < 0` בפונקציה?",
             options=opts("שם המשפחה של איבר `i` קודם לקסיקוגרפית לשם המשפחה של איבר `i-1`, ולכן הסדר מופר",
                          "שם המשפחה של איבר `i` מאוחר לקסיקוגרפית לשם המשפחה של איבר `i-1`, ולכן הסדר מופר",
                          "שני שמות המשפחה זהים, ולכן עוברים להשוות שמות פרטיים",
                          "הכתובת של `last_name` באיבר `i` נמוכה מהכתובת באיבר `i-1`"),
             correctId="a",
             explain="`strcmp(x, y) < 0` אומר ש-`x` קודם ל-`y`. כאן `x` הוא שם המשפחה של האיבר המאוחר במערך, ולכן הוא צריך להיות לא קטן מהקודם, וערך שלילי הוא הפרה (ריצה אמיתית: `strcmp(\"Asher\", \"Bern\") < 0`). שוויון הוא `cmp == 0`, ואין כאן השוואת כתובות."),
        step("fillblank", prompt="השלימו את השורה החסרה: מתי מחזירים `0` לפי מספרי הזהות? (הנחה: שני האיברים בעלי אותו שם משפחה ואותו שם פרטי.)",
             code=True, lines=S2_fb, blankIndex=S2_bl,
             options=opts("if (person_arr[i].id < person_arr[i - 1].id)", "if (person_arr[i].id <= person_arr[i - 1].id)",
                          "if (person_arr[i].id > person_arr[i - 1].id)", "if (person_arr[i].id != person_arr[i - 1].id)"),
             correctId="a",
             explain="הסדר לפי `id` עולה לא ממש, ולכן הפרה היא רק `id` קטן מהקודם. עם `<=` נפסל מערך עם שני איברים זהים לחלוטין, ועם `>` או `!=` נפסל מערך ממוין תקין (בדוגמה הראשונה `245689432 < 245689436`)."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה והפונקציה נכשלת על המערך התקין מהדוגמה הראשונה. מצאו אותה.",
             code=True, lines=S2_bug, bugIndex=S2_bi,
             explain="`<= 0` במקום `< 0`: כששני שמות משפחה זהים (`Cohen`, `Levi`) הפונקציה מחזירה `0` מיד ולא עוברת להשוואת שמות פרטיים."),
    ],
    stepsSource="ai-verified")


S3 = lines_of(code_of(Q3_SOL))
S3_ord = blocks(S3, "int** lists_to_sparse_matrix(element** list_row, int rows, int cols)",
                "arr = (int**)calloc(rows, sizeof(int*));", ("for (i = 0; i < rows; i++)", 1), "return arr;")
S3_bug, S3_bi = swap1(S3, "while (ptr)", "if (ptr)")
S3_fb, S3_bl = blank(S3, "arr[i][ptr->col] = ptr->data;")

add(3,
    rubric=rub(("הגדרת טיפוס איבר הרשימה מעל הפונקציה: שדה ערך, שדה מספר עמודה ומצביע לאיבר הבא", 6),
               ("הקצאת מערך של `rows` מצביעים לשורות (`int**`)", 8),
               ("הקצאת כל שורה בגודל `cols` עם איפוס (`calloc`), כך שהאיברים החסרים ברשימה הם 0", 10),
               ("מעבר על רשימה `i` כולה והצבת `data` של כל איבר בעמודה `col` שלו בשורה `i`", 13),
               ("החזרת כתובת המערך הדו-ממדי", 3)),
    rubricSource="ai-verified",
    pitfalls=["להקצות שורות עם `malloc` בלי לאפס: האיברים שאינם ברשימה יישארו עם ערכי זבל במקום 0.",
              "להחליף בין השדות: `arr[i][ptr->data] = ptr->col` במקום `arr[i][ptr->col] = ptr->data`.",
              "לעצור אחרי האיבר הראשון של כל רשימה (`if` במקום `while`), או להקצות את המערך החיצוני עם `sizeof(int)` במקום `sizeof(int*)`."],
    steps=[
        step("numeric", prompt="מטריצה דלילה בת 3 שורות ו-5 עמודות נתונה כמערך רשימות: רשימה 0 מכילה את הזוגות (ערך 5, עמודה 2) ו-(ערך 7, עמודה 4), רשימה 1 ריקה, ורשימה 2 מכילה את (ערך 3, עמודה 0). כמה איברים במטריצה המשוחזרת שווים ל-0?",
             answer=12, tol=0,
             explain="יש 15 איברים ו-3 מהם מגיעים מהרשימות, ולכן 12 איברים נשארים 0 (ריצה אמיתית: 12). אלה האיברים שחייבים להיות מאופסים בהקצאה."),
        step("fillblank", prompt="השלימו את השורה החסרה: מה מציבים בתא של האיבר הנוכחי ברשימה? (נניח שכל הערכים והעמודות קטנים מ-4 במטריצה 4 על 4.)",
             code=True, lines=S3_fb, blankIndex=S3_bl,
             options=opts("arr[i][ptr->col] = ptr->data;", "arr[i][ptr->data] = ptr->col;",
                          "arr[ptr->col][i] = ptr->data;", "arr[i][ptr->col] = ptr->col;"),
             correctId="a",
             explain="השורה היא `i` והעמודה היא `col`, והערך שנכתב הוא `data`. החלפת השדות, החלפת השורה והעמודה (שחלוף) או כתיבת `col` במקום `data` נותנים מטריצה שונה."),
        step("order", prompt="סדרו את גושי הקוד של הפתרון (הגדרת הטיפוס, פתיחת הפונקציה והצהרות, הקצאות, מילוי, החזרה).",
             code=True, lines=S3_ord,
             explain="הטיפוס חייב להופיע לפני הפונקציה שמשתמשת בו, ההקצאה של מערך השורות לפני הקצאת השורות, ושתיהן לפני המילוי; ההחזרה בסוף."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה והמטריצה המשוחזרת חסרה איברים. מצאו את השורה.",
             code=True, lines=S3_bug, bugIndex=S3_bi,
             explain="`if (ptr)` במקום `while (ptr)`: רק האיבר הראשון בכל רשימה נכתב למטריצה, ושאר איברי הרשימה אובדים."),
    ],
    stepsSource="ai-verified")

add(5,
    rubric=rub(("שני ה-`printf(\"%d\", 11)` הפנימיים מדפיסים `11` כל אחד, ולכן `1111`", 3),
               ("`printf` מחזירה את מספר התווים שהודפסו, ולכן כל אחד מהפנימיים מחזיר `2`", 3),
               ("ה-`printf(\"%d%d\", ...)` האמצעי מדפיס `22` ומחזיר `2`", 2),
               ("ה-`printf` החיצוני מדפיס את `2`, והפלט הכולל הוא `1111222`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`printf` מחזירה את הערך שהודפס (`11`) או `1`, ולא את מספר התווים.",
              "לשכוח שהפרמטרים הפנימיים מודפסים לפני הפלט של ה-`printf` שעוטף אותם, ולכן הפלט מתחיל ב-`1111`."],
    steps=[
        step("numeric", prompt="מה מחזירה הקריאה `printf(\"%d\", 11)`?", answer=2, tol=0,
             explain="`printf` מחזירה את מספר התווים שנכתבו, ו-`11` הם שני תווים (ריצה אמיתית: 2)."),
        step("numeric", prompt="מה מחזירה הקריאה האמצעית `printf(\"%d%d\", printf(\"%d\",11), printf(\"%d\",11))`?", answer=2, tol=0,
             explain="היא מקבלת `2` ו-`2`, מדפיסה `22` ולכן מחזירה 2 (ריצה אמיתית: 2). הערך הזה הוא מה שהקריאה החיצונית מדפיסה."),
        step("text", prompt="מה הפלט המלא של התוכנית? (רצף תווים אחד, בלי רווחים)", accept=["1111222"], normalize="none",
             explain="`11` ו-`11` מהקריאות הפנימיות, אחר כך `22` מהאמצעית, ולבסוף `2` מהחיצונית: `1111222` (ריצה אמיתית)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "21B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"א, מועד ב'",
    "year": 2021,
    "examDate": "13.07.2021",
    "sourceFile": "21B-B exam",
    "solutionFile": "21B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
