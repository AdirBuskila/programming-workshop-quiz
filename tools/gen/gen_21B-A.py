# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-A.json -- programming-workshop (C), semester B 2021, moed A (15.06.21).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of the three), Part 2: Q4 parts 1-4 (20 pts, MCQ with justification;
stored as parts a-d), Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code
+ marked options). Code solutions compiled and run with clang: tools/verify/21B-A/.
Run: PYTHONUTF8=1 py tools/gen/gen_21B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


PART1 = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש (שאלות 1, 2 ו-3).*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נתונה הגדרה הבאה של הטיפוס `name` אשר מהווה שם פרטי ושם משפחה של בן-אדם:
```c
typedef struct
{
    char first_name[30],
    last_name[30];
} name;
```
כתוב פונקציה אשר מקבלת מערך איברים מסוג `name` וגודלו.
על הפונקציה לבדוק האם איברי המערך ממוינים בסדר לקסיקוגרפי עולה לפי השמות (שדה `first_name`) או לפי שמות המשפחה (שדה `last_name`). אם המערך ממוין לפי השמות, הפונקציה תחזיר 1 ואם לפי שמות המשפחה - הפונקציה תחזיר 2. אם איברי המערך לא ממוינים בכלל, הפונקציה תחזיר 0.

**דוגמה:** עבור המערך הבא
```
0 Mike Asher
1 David Bern
2 Joseph Borgman
3 Alon Kapulski
4 Ilan Mizrachi
5 Oren Nodel
6 Abraham Rosen
```
הפונקציה תחזיר 2.""" + PART1

Q1_SOL = r"""```c
int ordered_name_array(name* name_arr, int n)
{
    int i;
    for (i = 1; i < n; i++)
        if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) < 0)
        {
            for (i = 1; i < n; i++)
                if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0)
                    return 0;
            return 2;
        }
    return 1;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item {
    int data;
    struct item *next;
} Item;
```
כתוב פונקציה אשר מקבלת שתי רשימות מקושרות **מעגליות** (רשימה מעגלית מועברת לפונקציה כמצביע לאחד מהאיברים שלה) המורכבות מאיברים מסוג `Item`.
הרשימות מכילות מספרים שונים כאשר ישנו רק מספר אחד המופיע בשתי הרשימות.

על הפונקציה לאחד את הרשימות לרשימה מעגלית אחת כך שהמספר המשותף יופיע פעם אחת ויחצוץ בין שתי הרשימות המקוריות, שתשמורנה על סידרן הפנימי לאחר האיחוד.
לא משנה מאיזו רשימה מקורית יהיו איברים "אחרי" המספר המשותף ברשימה המאוחדת ומאיזו רשימה יהיו "לפניו". גם לא משנה איזה איבר המכיל את המספר המשותף ייכלל ברשימה המאוחדת.
הפונקציה תחזיר את כתובת האיבר המכיל את המספר המשותף ברשימה המאוחדת.

**שים לב.** הפונקציה לא תקצה זיכרון לרשימה החדשה אלא תעדכן שדה `next` באיברים המתאימים של הרשימות המקוריות.

**דוגמא:** (באיור) המספר המשותף הוא 5.

**שים לב.** כל אחת מרשימות מקוריות יכולה להיות מורכבת גם רק מאיבר אחד (שדה `next` שלו מצביע לאיבר עצמו). במקרה זה האיבר היחיד מכיל את המספר המשותף.""" + PART1

Q2_SOL = r"""```c
/* Auxiliary function. Search of common items.
   The function gives addresses of items preceding common ones */
void addresses_of_items_preceding_common(Item *L1, Item *L2, Item **p1, Item **p2){
    Item *prev1 = L1, *prev2, *curr1 = prev1->next, *curr2;
    while (1) //external loop: scan first list
    {
        prev2 = L2;
        curr2 = prev2->next;
        do //internal loop: scan second list
        {
            if (curr2->data != curr1->data)
            {
                prev2 = curr2;
                curr2 = curr2->next;
            }
            else //common items are found
            {
                *p1 = prev1;
                *p2 = prev2;
                return;
            }
        } while (curr2 != L2->next);
        prev1 = curr1;
        curr1 = curr1->next;
    } //while (1)
}

/* Special case: list L1 has one item */
Item *one_item_list(Item *L1, Item *L2){
    int common = L1->data;
    free(L1);
    while (L2->data != common) //search of common item in L2
        L2 = L2->next;
    return L2;
}

Item *cyclic_lists_combining(Item *L1, Item *L2){
    Item *p1, *p2, *common;
    if (L1->next == L1) //L1 has one item
        return one_item_list(L1, L2);
    if (L2->next == L2) //L2 has one item
        return one_item_list(L2, L1);

    //p1 and p2 are addresses of items preceding common ones
    addresses_of_items_preceding_common(L1, L2, &p1, &p2);

    /* Combining of L1 and L2*/
    common = p1->next;
    p1->next = p2->next->next;
    free(p2->next);
    p2->next = common;
    return common;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזת `fileName` המהווה שם של **קובץ טקסט**. הקובץ שומר תוכן של מערך דו-ממדי של מספרים שלמים שבו כל שורה מורכבת מרצפים של מספרים זהים בדרך חסכונית.

שורה מס' `i` בקובץ מתאימה לשורה מס' `i` של המערך (שורות הקובץ ממוספרות מ-0).
כל רצף של מספרים זהים בשורת המערך (מתחילתה עד סופה) מוצג בשורת הקובץ (מתחילתה עד סופה) בהתאם כזוג מספרים: ערך האיברים ברצף וכמות האיברים ברצף.
המספרים הסמוכים בכל שורה מופרדים ברווח אחד. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה לשחזר מערך דו-ממדי דינאמי `A`. יש למלא את `A` בהתאם לתוכן הקובץ.
בנוסף הפונקציה תיצור מערך דינאמי `S` המורכב מגדלי שורות של `A` כך שאיבר מס' `i` ב-`S` יהיה שווה לגודל שורה מס' `i` ב-`A`.
הפונקציה תחזיר את `A` ותעביר (`by reference`) את `S` ואת מספר השורות ב-`A`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.

**דוגמא:**
```
תוכן הקובץ        המערך A                    S
4 2 7 4 3 3       4 4 7 7 7 7 3 3 3          9
2 6 1 2           2 2 2 2 2 2 1 1            8
9 1 12 3          9 12 12 12                 4
3 2 18 5 0 2      3 3 18 18 18 18 18 0 0     9
```
הפונקציה תעביר 4 כמספר השורות ב-`A`.""" + PART1

Q3_SOL = r"""```c
int **file_to_sequences_in_rows(char* filename, int **S, int *rows)
{
    char ch;
    int **A, num, size, start_row, i, j, k;
    FILE* fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);

    /* Estimation of the number of rows */
    *rows = 0;
    while ((ch = fgetc(fptr)) != EOF)
        if (ch == '\n')
            (*rows)++;

    A = (int**)calloc(*rows, sizeof(int*)); //pointer array allocation
    *S = (int*)calloc(*rows, sizeof(int)); //array of row sizes allocation

    rewind(fptr);
    for (i = 0; i < *rows; i++)
    {
        start_row = ftell(fptr);
        /* Estimation of row size */
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            (*S)[i] += size;
        } while ((ch = fgetc(fptr)) != '\n');

        A[i] = (int*)calloc((*S)[i], sizeof(int)); //row allocation

        /* File row -> array row */
        fseek(fptr, start_row, SEEK_SET);
        k = 0;
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            for (j = 1; j <= size; j++, k++)
                A[i][k] = num;
        } while ((ch = fgetc(fptr)) != '\n');
    } //for i
    fclose(fptr);
    return A;
}
```

**הערה:** הפתרון הרשמי תלוי בסוף שורה של Windows (CRLF) ובמצב טקסט של `ftell`/`fseek`. בבדיקה ב-Windows הוא עובד עם קובץ CRLF, אבל עם קובץ שבו סוף השורה הוא `\n` בלבד הוא עלול להיתקע או לקרוס (המיקום ש-`ftell` מחזיר במצב טקסט אינו מתאים). בלינוקס המצב הפוך: תו `'\r'` לפני `'\n'` מפר את בדיקת סוף השורה. בנוסף, `char ch` מושווה ל-`EOF` ולכן הקוד מניח ש-`char` הוא signed. תיקון נייד: לקרוא כל שורה עם `fgets` לתוך מחסנית תווים ולפרק אותה עם `sscanf("%d%d%n")` בלולאה (פעם לחישוב הגודל ופעם למילוי), בלי `ftell`/`fseek` ובלי תלות בסוף השורה, ולהגדיר `int ch`. תיקון זה נבדק בהרצה על קובץ LF ועל קובץ CRLF."""

# ---------------------------------------------------------------- Q4 (parts 1-4 of the printed exam, stored as a-d)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים (שאלה 4, 20 נק' בסך הכול; חובה לרשום את הבחירה והנימוק במחברת). זהו סעיף {n} בשאלה.\n"

Q4A_TEXT = Q4_INTRO.format(n=1) + "מה מאותחל כברירת המחדל?"
Q4A_OPTS = opts("משתנה מסוג `int` שמוגדר בתוך פונקציה, למשל `int x;`",
                "משתנה מסוג פוינטר ל-`int` שמוגדר בתוך פונקציה, למשל `int *p;`",
                "קבועים של טיפוס `enum`",
                "משתנה בקרה בלולאת `for` אשר לא מאותחל במפורש בחלק הראשון של הלולאה, למשל `for( ; i<n; i++)`",
                "איברי מערך דינאמי שהוקצה באמצעות פונקציית `malloc`",
                "אף תשובה אינה נכונה")
Q4A_EXPL = "ערכים של הקבועים של `enum` נקבעים אוטומטית, מתחילים מ-0 וגדלים ב-1."

Q4B_TEXT = Q4_INTRO.format(n=2) + "מה קורה בצד שמאל של מספר `int` חיובי לאחר ביצוע פעולת הזזת סיביות ימינה בתוכו?"
Q4B_OPTS = opts("מצד שמאל המספר מתמלא ב-0-ים", "מצד שמאל המספר מתמלא ב-1-ים",
                "מצד שמאל המספר מתמלא בסיביות שהלכו לאיבוד מצד ימין",
                "שיטת מילוי המספר מצד שמאל תלויה במערכת", "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C."

Q4C_TEXT = Q4_INTRO.format(n=3) + "איזה מערך מועבר לפונקציה `by value` (ז\"א הפונקציה מקבלת גישה להעתק של תוכנו אבל לא לתוכן המקורי שלו)?"
Q4C_OPTS = opts("מערך סטטי חד-ממדי", "מערך דינאמי חד-ממדי", "מערך סטטי דו-ממדי", "מערך דינאמי דו-ממדי",
                "מערך סטטי אשר מהווה שדה של המבנה כאשר המבנה מועבר לפונקציה `by value`", "אף תשובה אינה נכונה")
Q4C_EXPL = "מערך עצמו תמיד מועבר `by reference` כי הפונקציה מקבלת לא מערך עצמו אלא כתובתו. אבל מבנה מועבר `by value` כך שכל השדות שלו מועתקים כולל שדות שהם מערכים."

Q4D_TEXT = Q4_INTRO.format(n=4) + r"""נתונה הפונקציה הבאה:
```c
int *fun() {
    static int x;
    x++;
    return &x;
}
```
מהי הטענה הנכונה?"""
Q4D_OPTS = opts("הפונקציה לא תקינה רק מכיוון שהיא מחזירה כתובת של משתנה אשר לא קיים מעבר לפונקציה",
                "הפונקציה לא תקינה רק מכיוון שניגשים בתוכה למשתנה אשר לא מאותחל",
                "הפונקציה לא תקינה גם מכיוון שהיא מחזירה כתובת של משתנה אשר לא קיים מעבר לפונקציה וגם מכוון שניגשים בתוכה למשתנה אשר לא מאותחל",
                "הפונקציה תקינה", "אף טענה אינה נכונה")
Q4D_EXPL = "משתנה `static` נשמר בזיכרון גם אחרי יציאה מהפונקציה. משתנה `static` ללא אתחול מפורש מאותחל ב-0."

# ---------------------------------------------------------------- Q5
Q5_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
    printf("%d\n", sizeof"|0\0/00\0/0|");
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:** `11`

**נימוק:**
בטקסט שבתוך המירכאות יש 12 סימנים. ביניהם פעמיים מופיעה סדרת `'\0'` אשר מהווה תו אחד. לכן מופיעים פה 10 תווים. בסוף כל מחרוזת קבועה יש עוד תו אפסי (`'\0'`). לכן סה"כ המערך מורכב מ-11 תווים. אופרטור `sizeof` מחזיר את גודל האופרנד בבתים. כל תו תופס בית אחד. לכן הפלט יהיה 11."""

questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/21B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    {"num": 4, "part": "א", "kind": "mcq", "topic": "c_traps_mcq", "question": Q4A_TEXT,
     "options": Q4A_OPTS, "correctId": "c", "explanation": Q4A_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "a", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "structs_unions", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "e", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "storage_classes", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "d", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run: tools/verify/21B-A/steps_check.py
# (probes + order/fillblank/findbug checks through verify/step_lib.py). Lines of order/findbug/fillblank come from the stored solutions.
def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip() and not ln.startswith("```")]


def clean(lines):
    """Drop comment-only lines and trailing // comments (they are not part of the logic being asked about)."""
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("/*") or s.startswith("//"):
            continue
        if "//" in ln:
            ln = ln[:ln.index("//")].rstrip()
        out.append(ln)
    return out


def func_lines(src, header_start):
    """The code lines of the function whose header line starts with header_start, to its closing brace."""
    ls = clean(lines_of(src))
    i0 = [i for i, ln in enumerate(ls) if ln.startswith(header_start)]
    assert len(i0) == 1, header_start
    i1 = next(i for i in range(i0[0], len(ls)) if ls[i] == "}")
    return ls[i0[0]:i1 + 1]


def swap(lines, old, new, nth=0):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == old.strip()]
    assert len(idx) > nth and (nth > 0 or len(idx) == 1), old
    out = list(lines)
    out[idx[nth]] = out[idx[nth]].replace(old.strip(), new.strip())
    return out, idx[nth]


def blank(lines, target, nth=0):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == target]
    assert len(idx) > nth and (nth > 0 or len(idx) == 1), target
    return [("___" if i == idx[nth] else ln) for i, ln in enumerate(lines)], idx[nth]


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError(num)


# Q1
F1 = func_lines(Q1_SOL, "int ordered_name_array")
b1, i1 = swap(F1, "if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) < 0)",
              "if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) > 0)")
f1, j1 = blank(F1, "if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0)")
Q1_BODY = ["int i;",
           "for (i = 1; i < n; i++) if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) < 0) { for (i = 1; i < n; i++) if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0) return 0; return 2; }",
           "return 1;"]
add(1,
    rubric=rub(("לולאה על זוגות סמוכים שמשווה `first_name` עם `strcmp`, ומזהה סדר יורד (`strcmp(...) < 0`)", 10),
               ("כשנמצא זוג בסדר יורד בשמות הפרטיים, בדיקה של כל המערך לפי `last_name`", 12),
               ("החזרת 1 כשכל המערך ממוין לפי השמות הפרטיים", 6),
               ("החזרת 2 כשהמערך ממוין לפי שמות המשפחה", 6),
               ("החזרת 0 כשיש זוג בסדר יורד גם בשמות המשפחה", 6)),
    rubricSource="ai-verified",
    pitfalls=["לסמן שם כחוסר סדר גם כשהוא שווה לקודם (`<= 0` במקום `< 0`): מערך ממוין יכול להכיל שמות זהים.",
              "להשוות מחרוזות עם `<` או `==` (השוואת כתובות) במקום `strcmp`.",
              "להחזיר 2 כשהמערך כבר ממוין לפי השמות הפרטיים: הבדיקה לפי שם פרטי באה קודם, והתוצאה היא 1."],
    steps=[
        {"type": "numeric",
         "prompt": "במערך הדוגמה, באיזה אינדקס `i` נמצא הזוג הראשון שבו `first_name[i]` קטן מ-`first_name[i-1]` (בסדר לקסיקוגרפי)?",
         "answer": 1, "tol": 0,
         "explain": "`David` קודם ל-`Mike` בסדר האלפבית, ולכן כבר באינדקס 1 המערך אינו ממוין לפי שמות פרטיים (ריצה אמיתית: 1). אז הפונקציה עוברת לבדוק לפי שמות משפחה."},
        {"type": "fillblank", "prompt": "השלימו את התנאי שמזהה סדר יורד בשמות המשפחה.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": opts("if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0)",
                         "if (strcmp(name_arr[i - 1].last_name, name_arr[i].last_name) < 0)",
                         "if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) > 0)",
                         "if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) != 0)"),
         "correctId": "a",
         "explain": "סדר יורד פירושו שהשם הנוכחי קטן ממש מהקודם. בחלופות האחרות הדוגמה מחזירה 0 במקום 2: `> 0` ו-`!= 0` מזהים גם זוג בסדר עולה כחוסר סדר, וההשוואה עם הארגומנטים בסדר הפוך מזהה בדיוק זוג בסדר עולה (ריצה אמיתית: רק עם `< 0` בסדר המקורי הדוגמה מחזירה 2)."},
        {"type": "order", "prompt": "סדרו את גוף הפונקציה `ordered_name_array`. כל שורה היא בלוק לוגי אחד.", "code": True,
         "lines": Q1_BODY,
         "explain": "הצהרה על `i`, הלולאה שבודקת שמות פרטיים (ובתוכה בדיקת שמות משפחה), ובסוף `return 1`. החלפת בלוקים שוברת את הקומפילציה או מחזירה תמיד 1 (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ועבור מערך שממוין לפי שמות פרטיים בלבד (`Aaron Zed`, `Ben Yoni`, `Carl Xavi`) מתקבל 0 במקום 1. מצאו אותה.",
         "code": True, "lines": b1, "bugIndex": i1,
         "explain": "`> 0` מזהה כל זוג בסדר עולה כחוסר סדר, ולכן הפונקציה עוברת לבדוק שמות משפחה ומחזירה 0 (ריצה אמיתית: 0)."},
    ],
    stepsSource="ai-verified")

# Q2
F2 = func_lines(Q2_SOL, "Item *cyclic_lists_combining")
b2, i2 = swap(F2, "p1->next = p2->next->next;", "p1->next = p2;")
f2, j2 = blank(F2, "p2->next = common;")
add(2,
    rubric=rub(("טיפול במקרה של רשימה בת איבר אחד (`next` מצביע על האיבר עצמו): הערך שלו הוא המשותף, והאיבר משוחרר", 10),
               ("חיפוש האיבר המשותף בשתי הרשימות, תוך שמירת הכתובות של האיברים שלפניו (`p1`, `p2`)", 10),
               ("חיבור הרשימות: שמירת `common = p1->next`, `p1->next = p2->next->next`, שחרור העותק השני ו-`p2->next = common`", 14),
               ("החזרת כתובת האיבר המשותף ברשימה המאוחדת", 6)),
    rubricSource="ai-verified",
    pitfalls=["לא לטפל ברשימה בת איבר אחד (`next` מצביע על האיבר עצמו): למשל כש-`L2` בת איבר אחד, הקוד שמשחרר ומחבר איברים ניגש לזיכרון ששוחרר, והרשימה המאוחדת שגויה (באורך לא נכון).",
              "לדרוס את `p1->next` לפני ששומרים אותו ב-`common`, ולאבד את האיבר המשותף.",
              "להשאיר את האיבר המשותף פעמיים ברשימה המאוחדת (בלי לדלג על העותק שברשימה השנייה)."],
    steps=[
        {"type": "numeric",
         "prompt": "הרשימות המעגליות הן `L1: 1,2,5,3` ו-`L2: 7,5,8` והמספר המשותף הוא 5. כמה איברים יש ברשימה המעגלית המאוחדת?",
         "answer": 6, "tol": 0,
         "explain": "4 + 3 - 1 = 6, כי המספר המשותף מופיע פעם אחת (ריצה אמיתית: 6)."},
        {"type": "numeric",
         "prompt": "באותה דוגמה, הפונקציה מחזירה את האיבר המשותף ב-`L1`. נקבע שבפתרון הרשמי האיברים שאחרי המשותף הם אלה של `L1` (בסדרם הפנימי), ואלה שלפניו הם של `L2`. איזה ערך מופיע מיד אחרי 5 ברשימה המאוחדת?",
         "answer": 3, "tol": 0,
         "explain": "לפי המוסכמה שנקבעה, המשכה של `L1` אחרי 5 נשאר כפי שהיה (`3`), ואילו לפני 5 מופיעים איברי `L2`: 8 ואז 7 (ריצה אמיתית: הסדר 5, 3, 1, 2, 8, 7). בשאלה עצמה גם הסדר ההפוך תקין, ולכן המוסכמה נקבעת בשאלת הצעד."},
        {"type": "fillblank", "prompt": "השלימו את השורה שמחברת את האיבר שלפני העותק השני לאיבר המשותף.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": opts("p2->next = common;", "p2->next = p1->next;", "p2->next = common->next;", "p2->next = p2;"),
         "correctId": "a",
         "explain": "אחרי שהעותק השני שוחרר, האיבר שלפניו (`p2`) צריך להצביע על האיבר המשותף שנשאר ברשימה. בחלופות האחרות המעגל לא מכיל את כל האיברים (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ובדוגמה האיבר 8 חסר ברשימה המאוחדת (נוצרת רשימה בת 5 איברים). מצאו אותה.",
         "code": True, "lines": b2, "bugIndex": i2,
         "explain": "אחרי `p1->next = p2` נדלג על כל האיברים שאחרי העותק השני ב-`L2`, ולכן 8 אובד (ריצה אמיתית: 5 איברים)."},
    ],
    stepsSource="ai-verified")

# Q3
F3 = func_lines(Q3_SOL, "int **file_to_sequences_in_rows")
b3, i3 = swap(F3, "for (j = 1; j <= size; j++, k++)", "for (j = 1; j < size; j++, k++)")
f3, j3 = blank(F3, "fseek(fptr, start_row, SEEK_SET);")
add(3,
    rubric=rub(("ספירת השורות בקובץ לפי תווי `'\\n'`, והקצאת `A` (מערך מצביעים) ו-`S`", 8),
               ("בכל שורה: קריאת זוגות (ערך, כמות) עד סוף השורה וחישוב גודל השורה כסכום הכמויות", 12),
               ("הקצאת שורה `A[i]` בגודל המתאים", 8),
               ("חזרה לתחילת השורה בקובץ (`ftell` ו-`fseek`) וקריאה חוזרת שממלאת את האיברים בערך החוזר", 12)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב שהמספר השני בכל זוג הוא ערך ולא כמות, ולהקצות שורה לפי מספר הזוגות במקום סכום הכמויות.",
              "לא לזכור את תחילת השורה (`ftell`) לפני הסריקה הראשונה, ולכן לא ניתן לקרוא אותה שוב כדי למלא.",
              "לבדוק את סוף השורה לפני קריאת הזוג הראשון, ולדלג על שורה."],
    steps=[
        {"type": "numeric",
         "prompt": "בקובץ הדוגמה, מה הערך של `S[3]`, כלומר גודל שורה 3 של `A`? (שורת הקובץ: `3 2 18 5 0 2`)",
         "answer": 9, "tol": 0,
         "explain": "2 + 5 + 2 = 9: הכמויות הן המספרים השני, הרביעי והשישי בשורה (ריצה אמיתית: 9)."},
        {"type": "numeric",
         "prompt": "בקובץ הדוגמה, מה הערך של `A[1][6]`? (שורת הקובץ: `2 6 1 2`)",
         "answer": 1, "tol": 0,
         "explain": "השורה מתפרשת כשישה פעמים 2 ואחריהם פעמיים 1, ולכן באינדקס 6 נמצא 1 (ריצה אמיתית: 1)."},
        {"type": "fillblank", "prompt": "בהנחה שקובץ הקלט נוצר ב-Windows (סוף שורה CRLF), כמו בפתרון הרשמי: השלימו את השורה שחוזרת לתחילת השורה הנוכחית בקובץ.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": opts("fseek(fptr, start_row, SEEK_SET);", "rewind(fptr);", "fseek(fptr, start_row - 1, SEEK_SET);"),
         "correctId": "a",
         "explain": "`start_row` נשמר ב-`ftell` לפני הסריקה הראשונה, וחוזרים אליו במדויק. `rewind` חוזרת לתחילת הקובץ ולא לתחילת השורה, ו-`start_row - 1` נכשלת בשורה הראשונה (ריצה אמיתית: הפלט שונה)."},
        {"type": "findbug",
         "prompt": "בהנחה שהקובץ הוא בפורמט Windows (CRLF): בגרסה הבאה שורה אחת שונתה, ובקובץ הדוגמה השורה הראשונה של `A` מסתיימת באפסים (`4 7 7 7 3 3 0 0 0`) במקום `4 4 7 7 7 7 3 3 3`. מצאו אותה.",
         "code": True, "lines": b3, "bugIndex": i3,
         "explain": "`j < size` ממלא כל רצף באיבר אחד פחות מהכמות, ולכן המערך מתמלא בחסר והסוף נשאר אפסים (ריצה אמיתית: `4 7 7 7 3 3 0 0 0`)."},
    ],
    stepsSource="ai-verified")

# Q5 (bonus; checked with a probe program)
add(5,
    rubric=rub(("זיהוי ש-`\\0` הוא תו אחד, ולכן בין המירכאות 10 תווים (לא 12 סימנים)", 4),
               ("ליטרל של מחרוזת מסתיים בתו `'\\0'` אוטומטי נוסף, ולכן 11 תווים במערך", 3),
               ("`sizeof` מחזיר גודל בבתים, ותו תופס בית אחד: הפלט 11", 3)),
    rubricSource="ai-verified",
    pitfalls=["לספור את `\\0` כשני תווים, או לעצור את הספירה ב-`\\0` הראשון (כמו `strlen`) ולקבל 2.",
              "לשכוח את תו הסיום האוטומטי שבסוף הליטרל ולהדפיס 10."],
    steps=[
        {"type": "numeric", "prompt": r'כמה תווי `\0` מפורשים מופיעים בליטרל `"|0\0/00\0/0|"`?', "answer": 2, "tol": 0,
         "explain": r"`\0` מופיע פעמיים, וכל מופע הוא תו אחד (ריצה אמיתית: 2 בתים אפס לפני הסיום)."},
        {"type": "numeric", "prompt": "כמה תווים יש בליטרל, לא כולל תו הסיום שהקומפיילר מוסיף?", "answer": 10, "tol": 0,
         "explain": "`|`, `0`, `\\0`, `/`, `0`, `0`, `\\0`, `/`, `0`, `|`: עשרה תווים (ריצה אמיתית: 10)."},
        {"type": "numeric", "prompt": "מה מדפיסה התוכנית (`sizeof` של הליטרל)?", "answer": 11, "tol": 0,
         "explain": "10 תווים ועוד תו סיום: 11 בתים (ריצה אמיתית: 11)."},
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "21B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"א, מועד א'",
    "year": 2021,
    "examDate": "15.06.2021",
    "sourceFile": "21B-A exam",
    "solutionFile": "21B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
