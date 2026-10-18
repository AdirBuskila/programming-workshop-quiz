# -*- coding: utf-8 -*-
"""Generator for tools/raw/19B-A.json -- programming-workshop (C), semester B 2019, moed A (10.07.2019).
Q1, Q2, Q3 (28 pts each, all required), Q4 (16 pts, four pick-and-justify items), Q5 bonus (10 pts).
Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/19B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_19B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מערך מחרוזות `str`, גודלו `n` וגם מחרוזת `fileName`.
תו מס' 0 של מחרוזת `str[i]` הוא ספרה בעלת ערך `i+1` (ניתן להניח ש-`n` לא עולה על 9).

על הפונקציה ליצור קובץ טקסט ששמו נכלל ב-`fileName` ולהעתיק את תוכן המערך לקובץ באופן מחזורי כך שמחרוזת `str[1]` תהיה שורה ראשונה בקובץ, מחרוזת `str[2]` תהיה שורה שנייה בקובץ, ..., מחרוזת `str[n-1]` תהיה שורה שלפני אחרונה בקובץ ומחרוזת `str[0]` תהיה שורה אחרונה בקובץ.
יש לעדכן תו ראשון בתחילת כל שורה כך ששורות כמו מחרוזות המערך יהיו ממוספרות מ-1 עד `n`.

**דוגמא:**
`str`:
```
1 Bill Johns, 28
2 Ron Smith, 367
3 Arthur Mitchell, 84
4 Eduard Stone, 17
```
תוכן הקובץ:
```
1 Ron Smith, 367
2 Arthur Mitchell, 84
3 Eduard Stone, 17
4 Bill Johns, 28
```"""

Q1_SOL = r"""```c
void cyclic_shift_to_file (char **str, int n, char *fileName)
{
    int i;
    FILE *fptr = fopen(fileName, "w");
    if (!fptr)
        exit(1);
    for (i=1; i<n; i++)
    {
        fputc(i+'0', fptr);
        fputs(str[i]+1, fptr);
        fputc('\n', fptr);
    }
    fputc(n+'0', fptr);
    fputs(str[0]+1, fptr);
    fputc('\n', fptr);
    fclose(fptr);
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונות ההגדרות הבאות של טיפוסים:
```c
typedef struct data_item {
  int data;
  struct data_item *next;
} DataItem;
```
```c
typedef struct ptr_item {
  DataItem *ptr;
  struct ptr_item *next;
} PtrItem;
```
כתוב פונקציה המקבלת **רשימה מקושרת** `L` של **רשימות מקושרות** אשר מורכבת מאיברים מסוג `PtrItem`. השדה `ptr` של איבר מס' `i` ב-`L` יצביע לראש **רשימת המספרים** מס' `i` ושדה ה-`next` שלו יצביע לאיבר הבא ב-`L`. רשימות מספרים יהיו מורכבות מאיברים מסוג `DataItem`.

על הפונקציה לבנות רשימה מקושרת חדשה `R` אשר מורכבת מאיברים מסוג `DataItem`. כמות האיברים ב-`R` תהיה שווה לכמות הרשימות ב-`L`. שדה `data` של איבר מס' `i` ב-`R` יהיה שווה לסכום שדות `data` של איברי הרשימה מס' `i` של `L`.

הפונקציה תחזיר את כתובת האיבר הראשון של רשימת `R`.

**דוגמא:** (באיור: `L` היא רשימה של ארבעה איברים `PtrItem` שמצביעים, לפי הסדר, על הרשימות `3,2,4`, `6`, רשימה ריקה ו-`1,7`; `R` היא רשימה בת ארבעה איברים)

ניתן להניח שיש בזיכרון מספיק מקום להקצאות."""

Q2_SOL = r"""```c
DataItem *list_of_lists_to_list (PtrItem *L)
{
    DataItem *data_item_list, *curr_ptr,
        *lst = (DataItem *)malloc(sizeof(DataItem)); //dummy
    PtrItem *temp = L;
    curr_ptr = lst;
    while (temp) // scan list of lists
    {
        data_item_list = temp->ptr;
        curr_ptr->next = (DataItem *)malloc(sizeof(DataItem));
        curr_ptr = curr_ptr->next;
        curr_ptr->data = 0;
        while (data_item_list) // scan internal list
        {
            curr_ptr->data += data_item_list->data;
            data_item_list = data_item_list->next;
        }
        temp = temp->next;
    }
    curr_ptr->next = NULL;
    /* deletion of dummy */
    curr_ptr = lst;
    lst = lst->next;
    free (curr_ptr);
    return lst;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה אשר מקבלת **מערך דו-ממדי סטטי** (לא דינאמי) `A` של מספרים שלמים בעל `rows` שורות ו-`cols` עמודות.
המספר הפיסי של העמודות יינתן ע"י קבוע בשם `COLS`. יש להגדיר אותו לפני הפונקציה.

על הפונקציה ליצור מערך דו-ממדי דינאמי `B` אשר יהיה מורכב אך ורק מהשורות של `A` שסכומי האיברים שלהן הם מספרים זוגיים. עם זאת רק איברים אי-זוגיים מועתקים מ-`A` ל-`B`.
יש לשמור את סדר השורות מעותקות מ-`A` ל-`B` וגם את סדר האיברים מעותקים מ-`A` ל-`B` בכל שורה.
אם סכום האיברים בשורה של `A` הוא מספר זוגי אבל גם כל האיברים בשורה הם זוגיים אז לא להעתיק את השורה מ-`A` ל-`B`.

הפונקציה תחזיר את הכתובת של מערך `B` ותעביר by reference את מספר השורות בתוכו. בנוסף הפונקציה תעביר by reference מערך דינאמי `S` המורכב מגדלי השורות של מערך `B`. איבר מס' `i` של מערך `S` יהיה שווה לגודל שורה מס' `i` של `B`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאות.

**דוגמא:**
`A`:
```
20 14 10 13 33 80  sum=170
40 10 55 11 12 13  sum=141
15 16 17 18 19 21  sum=106
41 43 53 41 17 15  sum=210
10 20 30 40 50 62  sum=212
```
`B`:
```
13 33
15 17 19 21
41 43 53 41 17 15
```
`S`:
```
2
4
6
```
הפונקציה גם תעביר by reference 3 כמספר השורות במערך `B`."""

Q3_SOL = r"""```c
#define COLS 6 //example

int **even_sums_odd_numbers (int A[][COLS], int rows, int cols, int **S,
                             int *prows)
{
    int i, j, k, sum, odd_count, **B;
    *prows = 0;
    B = (int **)calloc(rows, sizeof(int *));
    *S = (int *)calloc(rows, sizeof(int));
    for (i=0; i<rows; i++)
    {
        sum = odd_count = k = 0;
        for (j=0; j<cols; j++)
        {
            sum += A[i][j];
            odd_count += A[i][j]%2;
        }
        if (sum%2 == 0 && odd_count>0)
        {
            B[*prows] = (int *)calloc(odd_count, sizeof(int));
            for (j=0; j<cols; j++)
                if (A[i][j]%2 == 1)
                    B[*prows][k++] = A[i][j];
            (*S)[*prows] = odd_count;
            (*prows)++;
        }
    }
    B = (int **)realloc(B, *prows*sizeof(int *));
    *S = (int *)realloc(*S, *prows*sizeof(int));
    return B;
}
```

**הערה:** הפתרון הרשמי בודק אי-זוגיות עם `A[i][j]%2 == 1` וסוכם `odd_count += A[i][j]%2`. בשאלה מדובר במספרים שלמים בלי הגבלת סימן, ואצל מספר אי-זוגי שלילי `%2` נותן `-1` ולא `1`: הוא לא נספר ולא מועתק, ו-`odd_count` נפגע (למשל השורה `{-3,-5,2,4,6,8}` נפסלת). התיקון: לבדוק `A[i][j]%2 != 0` (ולספור `odd_count += A[i][j]%2 != 0`). על מטריצת הדוגמה, שכל איבריה אינם שליליים, שתי הגרסאות נותנות אותה תוצאה. בנוסף, כשאף שורה לא נבחרת, `realloc(B, 0)` מוגדר-מימוש (C17) ואינו מוגדר ב-C23; במהדרים הנפוצים מתקבל `NULL`."""

# ---------------------------------------------------------------- Q4 (16 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 16 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + r"""```c
int (*p) (int *);
```
מה זה `p`?"""
Q4A_OPTS = opts("מצביע לפונקציה שמקבלת מצביע ל-`int` ומחזירה `int`",
                "פונקציה שמקבלת מצביע ל-`int` ומחזירה מצביע ל-`int`",
                "מצביע לפונקציה שמקבלת מצביע ל-`int` ומחזירה מצביע ל-`int`",
                "אף תשובה אינה נכונה")
Q4A_EXPL = "לפי התחביר של שפת C."

Q4B_TEXT = Q4_INTRO + r"""```c
z = x^y;
```
מה יהיה ערך של `z`?"""
Q4B_OPTS = opts("`x` בחזקת `y`", "המספר המתקבל מהזזת `y` סיביות שמאלה ב-`x`",
                "המספר המתקבל מהזזת `y` סיביות ימינה ב-`x`", "אף תשובה אינה נכונה")
Q4B_EXPL = "כי `^` זה XOR."

Q4C_TEXT = Q4_INTRO + r"""```c
static int c;
```
מה הוא ערך התחלתי של `c`?"""
Q4C_OPTS = opts("`c` לא מאותחל", "0", "1", "אף תשובה אינה נכונה")
Q4C_EXPL = "כי ברירת המחדל ערך התחלתי של משתנה `static` הוא 0."

Q4D_TEXT = Q4_INTRO + r"""```c
const int* q;
```
מה הוא `q`?"""
Q4D_OPTS = opts("מצביע קבוע למשתנה", "מצביע שיכול להשתנות לקבוע", "מצביע קבוע לקבוע", "אף תשובה אינה נכונה")
Q4D_EXPL = "לפי התחביר של שפת C."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
     int i;
     for (i=0; i<sizeof"sizeof"[i]; i++)
          printf("%d",sizeof"sizeof"[i]);
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
1
```
**נימוק:**
`sizeof"sizeof"[i]` זה גודל של תו מס' `i` במחרוזת `"sizeof"`. גודל של כל תו הוא 1 (בית אחד). לכן באיטרציה הראשונה `i=0` והתנאי `0 < 1` מתקיים. נכנסים לגוף הלולאה ומדפיסים 1. באיטרציה השנייה `i=1` והתנאי `1 < 1` לא מתקיים. יוצאים מהלולאה."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=28),
    Q(2, "code", "list_manipulation", Q2_TEXT, Q2_SOL, points=28, image="images/exams/19B-A-Q2.png"),
    Q(3, "code", "dynamic_arrays_2d", Q3_TEXT, Q3_SOL, points=28),
    M("א", "pointers", Q4A_TEXT, Q4A_OPTS, "a", Q4A_EXPL),
    M("ב", "bit_manipulation", Q4B_TEXT, Q4B_OPTS, "d", Q4B_EXPL),
    M("ג", "storage_classes", Q4C_TEXT, Q4C_OPTS, "b", Q4C_EXPL),
    M("ד", "pointers", Q4D_TEXT, Q4D_OPTS, "b", Q4D_EXPL),
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
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

# ---- Q1: cyclic_shift_to_file
S1 = lines_of(code_of(Q1_SOL))
S1_ord = blocks(S1, "for (i=1; i<n; i++)", "fputc(n+'0', fptr);", "fclose(fptr);")
S1_bug, S1_bi = swap1(S1, "fputc(n+'0', fptr);", "fputc(n, fptr);")
S1_fb, S1_bl = blank(S1, "fputs(str[i]+1, fptr);")

add(1,
    rubric=rub(("פתיחת הקובץ לכתיבה (`\"w\"`) ויציאה אם לא נפתח", 4),
               ("שורות `1` עד `n-1` נכתבות מהמחרוזות `str[1]` עד `str[n-1]`, עם ספרה חדשה `i+'0'` בתחילת כל שורה", 6),
               ("דילוג על התו הראשון הישן של המחרוזת (`str[i]+1`), כדי שהמספור הישן לא יופיע בקובץ", 6),
               ("כל שורה מסתיימת ב-`'\\n'`", 4),
               ("`str[0]` נכתבת אחרונה, כשורה מספר `n` (`n+'0'`)", 6),
               ("סגירת הקובץ", 2)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב את המחרוזת כולה (`str[i]`) ולא מהתו השני: בתחילת השורה יופיעו שתי ספרות, החדשה והישנה.",
              "לשכוח את `n+'0'` או לכתוב `n` ולא `n+'0'`: נכתב תו בקרה במקום הספרה.",
              "לכתוב את `str[0]` ראשונה ולא אחרונה, כך שההיסט המחזורי לא מתקבל."],
    steps=[
        step("choice", prompt="במערך מהדוגמה (`n = 4`, `str[0]` היא `\"1 Bill Johns, 28\"`), מהי השורה האחרונה שנכתבת לקובץ?",
             options=opts("`4 Bill Johns, 28`", "`1 Bill Johns, 28`", "`41 Bill Johns, 28`", "`4 Eduard Stone, 17`"), correctId="a",
             explain="השורה האחרונה נבנית מ-`str[0]` בלי התו הראשון שלה, עם הספרה `n+'0'` בתחילתה. `1 Bill...` הוא ללא מספור מחדש, ו-`41 Bill...` נובע משכחת `+1` (ריצה אמיתית: `4 Bill Johns, 28`)."),
        step("fillblank", prompt="השלימו את השורה שכותבת את שאר המחרוזת `str[i]` אחרי הספרה החדשה.",
             code=True, lines=S1_fb, blankIndex=S1_bl,
             options=opts("fputs(str[i]+1, fptr);", "fputs(str[i], fptr);", "fputs(str[i-1]+1, fptr);", "fputs(str[i]+2, fptr);"),
             correctId="a",
             explain="`str[i]+1` מדלגת על הספרה הישנה ושומרת את הרווח והטקסט. `str[i]` משאירה את הספרה הישנה, `str[i-1]+1` כותבת את המחרוזת הלא נכונה, ו-`str[i]+2` מוחקת גם את הרווח (ריצה אמיתית)."),
        step("order", prompt="סדרו את גושי הפונקציה `cyclic_shift_to_file`.",
             code=True, lines=S1_ord,
             explain="קודם פותחים את הקובץ, אחר כך כותבים את `str[1]` עד `str[n-1]`, אחריהן את `str[0]` כשורה האחרונה, ובסוף סוגרים."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה, והשורה האחרונה בקובץ אינה מתחילה בספרה. מצאו אותה.",
             code=True, lines=S1_bug, bugIndex=S1_bi,
             explain="`fputc(n, fptr)` כותבת את התו שקודו `n` (תו בקרה) ולא את הספרה. צריך `n+'0'`."),
    ],
    stepsSource="ai-verified")

# ---- Q2: list_of_lists_to_list
S2 = lines_of(code_of(Q2_SOL))
S2_ord = blocks(S2, "while (temp) // scan list of lists", "curr_ptr->next = NULL;", "return lst;")
S2_bug, S2_bi = swap1(S2, "curr_ptr->data += data_item_list->data;", "curr_ptr->data = data_item_list->data;")
S2_fb, S2_bl = blank(S2, "curr_ptr->data = 0;")

add(2,
    rubric=rub(("בניית הרשימה `R` באיבר דמה (`dummy`) ובמצביע זנב `curr_ptr`, כך שאין טיפול מיוחד באיבר הראשון", 6),
               ("מעבר על כל איברי `L`, ויצירת איבר אחד חדש ב-`R` לכל איבר, גם כשהרשימה הפנימית ריקה", 8),
               ("איפוס `data` של האיבר החדש ל-0 ואז צבירת כל איברי הרשימה הפנימית אליו", 8),
               ("סיום הרשימה: `curr_ptr->next = NULL`", 3),
               ("מחיקת איבר הדמה (`free`) והחזרת האיבר הראשון האמיתי", 3)),
    rubricSource="ai-verified",
    pitfalls=["לדלג על רשימה פנימית ריקה ולא ליצור לה איבר ב-`R`, כך שמספר האיברים ב-`R` קטן ממספר הרשימות.",
              "לא לאפס את `data` של האיבר החדש (`malloc` לא מאפס) ולצבור על ערך זבל.",
              "לשכוח `next = NULL` בסוף, או להחזיר את איבר הדמה עצמו."],
    steps=[
        step("choice", prompt="הרשימות הפנימיות ב-`L` הן $[3,2,4]$, $[6]$, רשימה ריקה ו-$[1,7]$. מה הערכים של `data` באיברי `R` לפי הסדר?",
             options=opts("`9, 6, 0, 8`", "`9, 6, 8`", "`3, 6, 0, 1`", "`9, 6, 0, 7`"), correctId="a",
             explain="לכל רשימה איבר אחד: $3+2+4=9$, $6$, רשימה ריקה נותנת $0$, ו-$1+7=8$ (ריצה אמיתית: 9, 6, 0, 8). `9, 6, 8` מדלג על הרשימה הריקה."),
        step("fillblank", prompt="השלימו את השורה שמאתחלת את `data` של האיבר החדש לפני צבירת הרשימה הפנימית.",
             code=True, lines=S2_fb, blankIndex=S2_bl,
             options=opts("curr_ptr->data = 0;", "curr_ptr->data = 1;", "curr_ptr->data = -1;",
                          "curr_ptr->data = data_item_list ? data_item_list->data : 0;"),
             correctId="a",
             explain="הסכום מתחיל מאפס. כל התחלה אחרת מוסיפה קבוע לכל סכום, והתחלה מהאיבר הראשון סופרת אותו פעמיים כי הלולאה הפנימית מוסיפה גם אותו (ריצה אמיתית)."),
        step("order", prompt="סדרו את גושי הפונקציה `list_of_lists_to_list`.",
             code=True, lines=S2_ord,
             explain="מכינים את איבר הדמה, בונים את `R` בסריקת `L`, מסיימים אותה ב-`NULL`, ורק אחר כך מוחקים את הדמה ומחזירים את הראש."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה, והערכים ב-`R` אינם הסכומים. מצאו אותה.",
             code=True, lines=S2_bug, bugIndex=S2_bi,
             explain="`=` במקום `+=`: כל איבר ברשימה הפנימית דורס את הקודם, ולכן נשאר רק האיבר האחרון ולא הסכום."),
    ],
    stepsSource="ai-verified")

# ---- Q3: even_sums_odd_numbers
S3 = lines_of(code_of(Q3_SOL))
# the official `%2` / `%2 == 1` fail on negative odd numbers: the steps use the correct test (`%2 != 0`)
S3 = [ln.replace("odd_count += A[i][j]%2;", "odd_count += A[i][j]%2 != 0;").replace("if (A[i][j]%2 == 1)", "if (A[i][j]%2 != 0)") for ln in S3]
assert sum("%2 != 0" in ln for ln in S3) == 2
S3_ord = blocks(S3, "int **even_sums_odd_numbers (int A[][COLS], int rows, int cols, int **S,", "*prows = 0;",
                "for (i=0; i<rows; i++)", "B = (int **)realloc(B, *prows*sizeof(int *));")
S3_bug, S3_bi = swap1(S3, "odd_count += A[i][j]%2 != 0;", "odd_count += 1;")
S3_fb, S3_bl = blank(S3, "if (sum%2 == 0 && odd_count>0)")

add(3,
    rubric=rub(("הקצאת מערך המצביעים `B` ומערך הגדלים `S` (בגודל `rows` לכל היותר), והעברת `S` ו-`*prows` by reference", 4),
               ("לכל שורה: חישוב סכום השורה וספירת האיברים האי-זוגיים (עם איפוס בכל שורה)", 6),
               ("תנאי העתקה: הסכום זוגי **וגם** יש לפחות איבר אי-זוגי אחד", 6),
               ("הקצאת שורה ב-`B` בגודל מספר האי-זוגיים, והעתקת האי-זוגיים בלבד לפי הסדר המקורי", 8),
               ("עדכון `S` ו-`*prows`", 2),
               ("כיווץ `B` ו-`S` (`realloc`) לגודל האמיתי והחזרת `B`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לבדוק רק שהסכום זוגי: שורה שכולה זוגית (כמו השורה האחרונה בדוגמה) תיכנס ל-`B` כשורה ריקה.",
              "להעתיק גם איברים זוגיים, או לשכוח לאפס `sum`, `odd_count`, `k` בין שורות.",
              "לא להעביר את `S` ו-`*prows` by reference (מצביע-למצביע), כך שהקורא לא מקבל את המערך והגודל."],
    steps=[
        step("numeric", prompt="עבור המטריצה $A$ מהדוגמה (5 שורות, 6 עמודות), מה הערך ש-`*prows` מכיל בסוף?",
             answer=3, tol=0,
             explain="שורות 0, 2, 3 עומדות בתנאי: הסכום זוגי ויש בהן איבר אי-זוגי. שורה 1 בעלת סכום אי-זוגי, ושורה 4 זוגית לחלוטין (ריצה אמיתית: 3)."),
        step("choice", prompt="אילו שורות של $A$ (מ-0) מועתקות ל-$B$ בדוגמה?",
             options=opts("`0, 2, 3`", "`0, 3, 4`", "`0, 1, 2, 3, 4`", "`0, 2, 3, 4`"), correctId="a",
             explain="הסכומים הם 170, 141, 106, 210, 212. שורה 1 (141) אי-זוגית, ושורה 4 (212) זוגית אבל כל איבריה זוגיים ולכן לא מועתקת (ריצה אמיתית: השורות 0, 2, 3)."),
        step("fillblank", prompt="השלימו את תנאי ההעתקה של השורה.",
             code=True, lines=S3_fb, blankIndex=S3_bl,
             options=opts("if (sum%2 == 0 && odd_count>0)", "if (sum%2 == 0)", "if (odd_count>0)", "if (sum%2 == 0 || odd_count>0)"),
             correctId="a",
             explain="צריך את שני התנאים יחד. בלי `odd_count>0` נכנסת שורה 4 כשורה ריקה, בלי הסכום הזוגי נכנסת שורה 1, ועם `||` נכנסות שתיהן (ריצה אמיתית)."),
        step("order", prompt="סדרו את גושי הפונקציה `even_sums_odd_numbers`.",
             code=True, lines=S3_ord,
             explain="הקבוע לפני הפונקציה, אחריו הכנת `B`, `S` ו-`*prows`, אחר כך הלולאה על השורות, ורק בסוף כיווץ המערכים והחזרה."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה, והפונקציה מעתיקה גם את השורה הזוגית לחלוטין. מצאו אותה.",
             code=True, lines=S3_bug, bugIndex=S3_bi,
             explain="`odd_count += 1` סופר כל איבר, לא רק אי-זוגי, ולכן `odd_count>0` תמיד נכון ושורה 4 נכנסת (ריצה אמיתית: `*prows` יוצא 4)."),
    ],
    stepsSource="ai-verified")

add(5,
    rubric=rub(("`sizeof\"sizeof\"[i]` הוא `sizeof` של התו `\"sizeof\"[i]` (ולא של כל המחרוזת)", 3),
               ("גודל תו הוא 1 בית, ולכן תנאי הלולאה הוא `i < 1`", 2),
               ("הלולאה רצה רק עבור `i = 0`", 3),
               ("מודפס `1`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא את הביטוי כגודל המחרוזת כולה (7 בתים, כולל `\\0`) ולחשוב שהלולאה רצה 7 פעמים.",
              "לשכוח ש-`sizeof` היא אופרטור שחל על הביטוי `\"sizeof\"[i]`, ולא על `\"sizeof\"`."],
    steps=[
        step("numeric", prompt="מה ערך הביטוי `sizeof\"sizeof\"[i]` (בית אחד לכל תו)?", answer=1, tol=0,
             explain="האינדקס חל קודם על המחרוזת, ו-`sizeof` של תו הוא 1 (ריצה אמיתית: 1). לעומת זאת `sizeof(\"sizeof\")` הוא 7."),
        step("numeric", prompt="כמה פעמים מתבצע גוף הלולאה?", answer=1, tol=0,
             explain="עבור `i = 0` התנאי `0 < 1` נכון, ועבור `i = 1` התנאי `1 < 1` שקרי (ריצה אמיתית: איטרציה אחת)."),
        step("text", prompt="מה הפלט של התוכנית?", accept=["1"], normalize="none",
             explain="באיטרציה היחידה מודפס הערך `1` (ריצה אמיתית: `1`)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "19B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשע\"ט, מועד א'",
    "year": 2019,
    "examDate": "10.07.2019",
    "sourceFile": "19B-A exam",
    "solutionFile": "19B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
