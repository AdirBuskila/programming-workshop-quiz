# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json -- programming-workshop (C), semester B 2024, moed B (30.07.2024).
Q1 (40), Q2/Q3 (40 each, answer one), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/24B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_24B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר את המבנה הבא המייצג איבר ברשימה מקושרת חד-כיוונית:
```c
typedef struct item {
        int number;
        struct item* next;
} Item;
```
כתבו פונקציה `Item ** numSeparation(int * A, int sz, int * p_size)` המקבלת מערך `A` של מספרים שלמים עם גודלו `sz`.
על הפונקציה **לסווג** את האיברים של `A` לרשימות של איברים מטיפוס `Item` לפי **כמות הספרות** שבהם. הפונקציה תבנה מערך `L` של מצביעים אשר למעשה מהווה מערך של רשימות כך ש-`L[i]` יצביע לתחילת הרשימה בה שדות `number` של איבריה הם איברים של `A` בעלי `i+1` ספרות. `L` יהיה מורכב מ-`n` איברים, כאשר `n` הוא הכמות המקסימלית של ספרות במספר בין איברי `A`. אם ב-`A` אין אף איבר בעל `m` ספרות (`m<n`) אז `L[m+1]` יהיה שווה ל-`NULL`.
הפונקציה תחזיר את הכתובת של תחילת המערך `L` ותעביר by reference (באמצעות מצביע `p_size`) את גודלו.

**דוגמא:** עבור `A = {23, 4, -78, 34578, 79, -185, 0, 998, 9, 36}` הפונקציה תיצור את המערך `L` הבא (באיור: `L[0]: 4,0,9`; `L[1]: 23,-78,79,36`; `L[2]: -185,998`; `L[3]: NULL`; `L[4]: 34578`) ותעביר 5 כגודל המערך החדש.

יש לכתוב ולהשתמש בפונקציית עזר `int digitsNumber(int num)` אשר מחזירה את כמות הספרות במספר `num`.
להכנסת איבר חדש לרשימה אין צורך לסרוק את הרשימה מתחילתה עד סופה. יש לשמור כתובות של איברים אחרונים ברשימות או להכניס את האיבר לראש הרשימה (סדר האיברים ברשימות אינו משנה).
אפשר (אבל לא חובה) להשתמש במערכי עזר.
ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q1_SOL = r"""```c
digitsNumber(int num)
{
       int count = 1, abs_num = abs(num);
       while (abs_num > 9)
       {
              count++;
              abs_num /= 10;
       }
       return count;
}

void headInsert(Item** plst, int key)
{
       Item* temp = (Item*)malloc(sizeof(Item));
       temp->number = key;
       temp->next = *plst;
       *plst = temp;
}

Item** numSeparation(int* A, int sz, int* p_size)
{
       int i, max_dig_num = 1,
              *dig_num = (int *)calloc(sz, sizeof(int)); //auxiliary array: digit numbers of A's elements
       Item** L;

       /* Search of maximum number of digits */
       for (i = 0; i < sz; i++)
       {
              dig_num[i] = digitsNumber(A[i]);
              if (dig_num[i] > max_dig_num)
                     max_dig_num = dig_num[i];
       }

       L = (Item**)calloc(max_dig_num, sizeof(Item*)); //array of pointers to lists
       for (i = sz - 1; i >= 0; i--)
              headInsert(L + dig_num[i] - 1, A[i]); //insert A[i] into the head of corresponding list

       free(dig_num);
       *p_size = max_dig_num;
       return L;
}
```
**הערה:** בפתרון הרשמי כותרת הפונקציה `digitsNumber` נכתבה ללא טיפוס החזרה `int` (שאלה מחייבת `int digitsNumber(int num)`). במהדר clang בתקן C99 ומעלה ללא `int` זו שגיאת קומפילציה; עם `int` הקוד עובר ומחזיר את הרשימות מהדוגמא."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

כתבו פונקציה `int ** matrixToFrame(int ** M, int rows, int cols)` אשר מקבלת מערך דו-ממדי דינאמי `M` של מספרים שלמים בעל `rows` שורות ו-`cols` עמודות.
`M` מבוסס על מערך דינאמי של פוינטרים אשר מצביעים על מערכים דינאמיים המהווים שורות (כפי שלמדנו בכיתה).

על הפונקציה לבנות מערך דו-ממדי דינאמי `F` בעל `rows+2` שורות ו-`cols+2` עמודות המהווה את תוכן המערך המקורי `M` מוקף ב**מסגרת** המורכבת מאפסים.

**דוגמא:** (איור: המערך `M` בעל 3 שורות ו-4 עמודות, והמערך `F` בעל 5 שורות ו-6 עמודות)

בסוף הפונקציה **תשחרר** את המערך המקורי `M` ו**תחזיר** את הכתובת של המערך `F`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
void freeMatrix(int** M, int rows)
{
       int i;
       for (i = 0; i < rows; i++)
              free(M[i]);
       free(M);
}

int** matrixToFrame(int** M, int rows, int cols)
{
       int rows2 = rows + 2, cols2 = cols + 2, ** F = (int**)calloc(rows2, sizeof(int*)), i, j;
       for (i = 0; i < rows2; i++)
              F[i] = (int*)calloc(cols2, sizeof(int)); //all elements are zeros
       for (i = 0; i < rows; i++)
              for (j = 0; j < cols; j++)
                     F[i + 1][j + 1] = M[i][j];
       freeMatrix(M, rows);
       return F;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

כתבו פונקציה עם החתימה `void processFiles(const char* inputFilename, const char* outputFilename)` אשר מקבלת שמות שני קבצי טקסט (קובץ קלט וקובץ פלט בהתאמה). קובץ הקלט מורכב משורות של תווים שרירותיים.
על הפונקציה למצוא שורות בקובץ הקלט שמורכבות רק מאותיות (באנגלית) ובנוסף מכילות אותיות שונות זו מזו בלבד. יש להתייחס אל אותיות קטנות וגדולות בטקסט באותו האופן (כך שלמשל `'a'` וגם `'A'` יחשבו כאותה אות).
הפונקציה תשמור את השורות הנ"ל בקובץ הפלט כך שסדר האותיות בכל שורה יהיה הפוך.
ניתן להניח שאורך כל שורה בקובץ הקלט אינו עולה על 99 תווים (לא כולל `'\n'`). יש להשתמש במחרוזת עזר.

**דוגמא:**

קובץ הקלט:
```
abc#xyz
table
Alisa
Walla
Michael
```
קובץ הפלט:
```
elbat
leahciM
```
יש לכתוב ולהשתמש בפונקציית עזר `void reverseString(char* str)` להפיכת סדר התווים במחרוזת.
יש לכתוב ולהשתמש בפונקציית עזר יעילה `int hasUniqueLetters(const char* str)` שבודקת האם המחרוזת מכילה רק אותיות והאם כל האותיות במחרוזת שונות. הפונקציה תחזיר 1 אם שני התנאים מתקיימים ו-0 אחרת.
אפשר להשתמש במערך עזר.
במידה ויהיה צורך בהקצאת זיכרון דינאמי, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3_SOL = r"""```c
void reverseString(char* str)
{
       int i = 0, j = strlen(str) - 1;
       char temp;
       for (; i < j; i++, j--)
       {
              temp = str[i];
              str[i] = str[j];
              str[j] = temp;
       }
}

int hasUniqueLetters(const char* str)
{
       char temp[26] = { 0 }; //counters of 26 english letters
       int i, index;
       for (i = 0; str[i] != '\0'; i++)
       {
              if (!isalpha(str[i]))
                     return 0;
              index = tolower(str[i]) - 'a';
              if (temp[index] > 0)
                     return 0;
              temp[index]++;
       }
       return 1;
}

void processFiles(const char* inputFilename, const char* outputFilename)
{
       char str[101];
       FILE* fin = fopen(inputFilename, "r"), *fout = fopen(outputFilename, "w");
       if (!fin || !fout)
              exit(1);
       while (fgets(str, 101, fin)) //together with '\n' and '\0': 99+1+1=101
       {
              str[strlen(str) - 1] = '\0'; //removing '\n'
              if (hasUniqueLetters(str))
              {
                     reverseString(str);
                     fprintf(fout, "%s\n", str);
              } //if
       }  //while
       fclose(fin);
       fclose(fout);
}
```

**הערה:** הפתרון מניח שכל שורה, גם האחרונה, מסתיימת ב-`'\n'`. אם השורה האחרונה בקובץ הקלט אינה מסתיימת ב-`'\n'`, ההוראה `str[strlen(str) - 1] = '\0'` מוחקת את התו האחרון של המילה עצמה (למשל `abc` ללא שורה חדשה נכתבת כ-`ba`). בנוסף, שורה ריקה נחשבת כמורכבת מאותיות שונות ונכתבת לפלט כשורה ריקה. תיקון: למחוק את התו האחרון רק אם הוא `'\n'`."""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
int* fun(int *);
void main()
{
    int x, y;
    x = *fun(&y);
    printf("%d %d\n", x, y);
    x = ++(*fun(&y));
    printf("%d %d\n", x, y);
    y = ++(*fun(&x));
    printf("%d %d\n", x, y);
    x = ++(*fun(&x));
    printf("%d %d\n", x, y);
    y = ++(*fun(&y));
    printf("%d %d\n", x, y);
}
int* fun(int* q)
{
    static int x = 1;
    int y = 1;
    x++;
    y++;
    *q = y;
    return &x;
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
2 2
4 2
2 6
8 6
8 10
```
**נימוק:**
**הקריאה הראשונה ל-`fun`.** `x` ו-`y` של הפונקציה מאותחלים ב-1 ומתקדמים ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. `x` ב-`main` מקבל ערך 2 של `static x` שנמצא בכתובת המוחזרת. לכן הפלט:
`2 2`
**הקריאה השנייה ל-`fun`.** `static x` זוכר את ערכו 2 ומתקדם ל-3. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-4 ב-`main` וערך זה הוכנס ל-`x` של `main`. לכן הפלט:
`4 2`
**הקריאה השלישית ל-`fun`.** `static x` זוכר את ערכו 4 ומתקדם ל-5. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`x` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-6 ב-`main` וערך זה הוכנס ל-`y` של `main`. לכן הפלט:
`2 6`
**הקריאה הרביעית ל-`fun`.** `static x` זוכר את ערכו 6 ומתקדם ל-7. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`x` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-8 ב-`main` וערך זה הוכנס ל-`x` של `main`. `y` של `main` נישאר 6 ללא שינוי. לכן הפלט:
`8 6`
**הקריאה החמישית ל-`fun`.** `static x` זוכר את ערכו 8 ומתקדם ל-9. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-10 ב-`main` וערך זה הוכנס ל-`y` של `main`. `x` של `main` נישאר 8 ללא שינוי. לכן הפלט:
`8 10`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + r"""נתונה ההצהרה הבאה:
```c
struct a { int b, c; } d;
```
מהו `d`?"""
Q5A_OPTS = opts("שם הפונקציה", "שם הטיפוס", "שם השדה", "שם המשתנה", "אף תשובה אינה נכונה")
Q5A_EXPL = "כאן מוגדר מבנה `a` בעל שדות `b` ו-`c` ומיד מוצהר משתנה `d` מטיפוס `struct a` המוגדר."

Q5B_TEXT = Q5_INTRO + r"""נתון פוינטר ל-`int` בשם `p`. בחרו מה יקרה אחרי ביצוע הפעולה
```c
p = (int*)realloc(NULL, sizeof(int));
```"""
Q5B_OPTS = opts("יוקצה בית אחד", "`p` יהיה שווה ל-`NULL`", "יוקצה משתנה אחד מסוג `int`",
                "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q5B_EXPL = "אם הפרמטר הראשון (המצביע) של `realloc` שווה ל-`NULL`, הקריאה שקולה לקריאה ל-`malloc`. לכן מקצים פה מקום למשתנה אחד מסוג `int`."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
    printf("%d", (int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1));
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `-1`

**נימוק:**
נתחיל מהביטוי הפנימי ביותר.
`( 1 << 1 )` = `10` בבינארי = 2
`( 1 << (1 << 1) )` = `1<<2` = `100` בבינארי = 4
`( (1 << (1 << 1)) + 1 )` = 4+1 = 5
`( 1 << ((1 << (1 << 1)) + 1) )` = `1<<5` = `100000` בבינארי = 32
`( (long long)1 << (1 << ((1 << (1 << 1)) + 1)) )` = `(long long)1 << 32` = $2^{32}$ (64 סיביות)
`( ((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1 )` = $2^{32}-1$ (64 סיביות)
`(int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)` = `(int)(2^32 - 1)` = `111…1` בבינארי (32 סיביות)
התוצאה היא ייצוג בינארי של -1.

**הערה:** התוצאה `-1` תלויה בפלטפורמה: היא מניחה ש-`int` הוא בן 32 סיביות (כך שהערך `4294967295` אינו נכנס ב-`int`), והמרה של ערך שאינו נכנס ב-`int` לטיפוס `int` היא מוגדרת-מימוש בתקן C. במהדרים הנפוצים, שמייצגים מספרים בשיטת המשלים ל-2, ההמרה פשוט חותכת ל-32 הסיביות התחתונות ומתקבל `-1`."""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/24B-B-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40, image="images/exams/24B-B-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    Q(4, "code", "storage_classes", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "structs_unions", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "d", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "dynamic_memory", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "c", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "bit_manipulation", Q6_TEXT, Q6_SOL, points=10),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run in tools/verify/<CODE>/
# (steps_check.py compiles the shipped steps; q*.c are the solution harnesses). Lines of order/findbug/fillblank come from the stored solutions.
import re


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def strip_c(ln):
    ln = re.sub(r"\s*//.*$", "", ln)
    ln = re.sub(r"\s*/\*.*?\*/\s*", " ", ln)
    return ln.rstrip()


def code_lines(src):
    """Non-blank code lines of a solution, trailing comments removed."""
    out = []
    for ln in src.strip("\n").split("\n"):
        ln = strip_c(ln)
        if ln.strip() and not ln.startswith("```") and not ln.startswith("**"):
            out.append(ln)
    return out


def func_lines(src, header_start):
    """The lines of the function whose header starts with header_start, down to its closing brace at column 0."""
    ls = code_lines(src)
    i0 = [i for i, ln in enumerate(ls) if ln.startswith(header_start)]
    assert len(i0) == 1, header_start
    i1 = next(i for i in range(i0[0], len(ls)) if ls[i] == "}")
    return ls[i0[0]:i1 + 1]


def swap(lines, old, new):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == old.strip()]
    assert len(idx) == 1, old
    out = list(lines)
    out[idx[0]] = out[idx[0]].replace(old.strip(), new.strip())
    return out, idx[0]


def blank(lines, target, nth=0):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == target.strip()]
    assert len(idx) > nth, target
    return [("___" if i == idx[nth] else ln) for i, ln in enumerate(lines)], idx[nth]


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError(num)


def T(*vals):
    return [{"id": "abcdef"[i], "type": "text", "value": v} for i, v in enumerate(vals)]


# Q1 -- numSeparation (the official text of digitsNumber lacks the return type; the steps show it with `int`)
FD1 = ["int " + ln for ln in func_lines(Q1_SOL, "digitsNumber(int num)")[:1]] + func_lines(Q1_SOL, "digitsNumber(int num)")[1:]
FN1 = func_lines(Q1_SOL, "Item** numSeparation")
B1 = ["int i, max_dig_num = 1, *dig_num = (int *)calloc(sz, sizeof(int)); Item** L;",
      "for (i = 0; i < sz; i++) { dig_num[i] = digitsNumber(A[i]); if (dig_num[i] > max_dig_num) max_dig_num = dig_num[i]; }",
      "L = (Item**)calloc(max_dig_num, sizeof(Item*));",
      "for (i = sz - 1; i >= 0; i--) headInsert(L + dig_num[i] - 1, A[i]);",
      "free(dig_num); *p_size = max_dig_num; return L;"]
f1, j1 = blank(FN1, "headInsert(L + dig_num[i] - 1, A[i]);")
b1, i1 = swap(FD1, "int count = 1, abs_num = abs(num);", "int count = 1, abs_num = num;")
add(1,
    rubric=rub(("פונקציית עזר `digitsNumber` שסופרת ספרות של מספר, כולל מספר שלילי (ערך מוחלט) ואת המספר 0 (ספרה אחת)", 8),
               ("חישוב כמות הספרות של כל איבר ב-`A` (במערך עזר או בחישוב חוזר) והכמות המקסימלית `n`", 8),
               ("הקצאת מערך `L` של `n` מצביעים עם איפוס (`calloc`), כך שרשימה ריקה היא `NULL`", 8),
               ("הכנסת כל איבר לראש הרשימה המתאימה `L[digits-1]` ללא סריקה, עם איבר `Item` חדש לכל מספר", 10),
               ("העברת הגודל `n` דרך `p_size`, שחרור מערך העזר והחזרת `L`", 6)),
    rubricSource="ai-verified",
    pitfalls=["לחשב את מספר הספרות של מספר שלילי בלי ערך מוחלט, כך ש-`-78` נספר כספרה אחת.",
              "להשתמש ב-`malloc` במקום ב-`calloc` ולהשאיר ב-`L[m]` ערך לא מאותחל כשאין מספרים בעלי `m+1` ספרות (צריך `NULL`).",
              "להכניס ל-`L[digits]` במקום ל-`L[digits-1]`, ולחרוג מגבולות המערך."],
    steps=[
        {"type": "numeric",
         "prompt": "מה מחזירה `digitsNumber(-185)`?",
         "answer": 3, "tol": 0,
         "explain": "בלי הסימן יש ב-185 שלוש ספרות (ריצה אמיתית: 3)."},
        {"type": "numeric",
         "prompt": "עבור `A = {23, 4, -78, 34578, 79, -185, 0, 998, 9, 36}`, מה ערך `*p_size` (הגודל של `L`) בסוף הפונקציה?",
         "answer": 5, "tol": 0,
         "explain": "הכמות המקסימלית של ספרות היא 5 (המספר `34578`), ולכן `L` בגודל 5 (ריצה אמיתית: size=5; `L[3]` ריק)."},
        {"type": "fillblank", "prompt": "השלימו את שורת ההכנסה: לאיזו רשימה מכניסים את `A[i]`?", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": T("headInsert(L + dig_num[i] - 1, A[i]);", "headInsert(L + max_dig_num - 1, A[i]);",
                      "headInsert(L + dig_num[i] % max_dig_num, A[i]);", "headInsert(L, A[i]);"),
         "correctId": "a",
         "explain": "מספר בעל `d` ספרות שייך לרשימה `L[d-1]`, והכתובת שמועברת ל-`headInsert` היא `L + d - 1`. ב' מכניס הכול לרשימה האחרונה, ג' מזיז כל רשימה בצעד אחד (ו-5 ספרות חוזרות ל-0) וד' מכניס הכול לרשימה הראשונה (ריצה אמיתית: רשימות שגויות בכל אחת מהן)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `numSeparation` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "קודם הצהרות, אחר כך חישוב הכמות המקסימלית, רק אז הקצאת `L` בגודל הנכון, אחר כך ההכנסה, ובסוף שחרור, עדכון הגודל והחזרה. כל החלפה נכשלת בבנייה, קורסת או נותנת תוצאה שגויה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה של `digitsNumber` שורה אחת שונתה, והמספרים השליליים (`-78`, `-185`) נכנסים לרשימה שגויה. מצאו את השורה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "בלי `abs`, הערך השלילי אינו גדול מ-9 והלולאה לא רצה: `-78` נספר כספרה אחת (ריצה אמיתית: `-78` ו-`-185` ב-`L[0]`)."},
    ],
    stepsSource="ai-verified")

# Q2 -- matrixToFrame
FN2 = func_lines(Q2_SOL, "int** matrixToFrame")
B2 = ["int rows2 = rows + 2, cols2 = cols + 2, ** F = (int**)calloc(rows2, sizeof(int*)), i, j;",
      "for (i = 0; i < rows2; i++) F[i] = (int*)calloc(cols2, sizeof(int));",
      "for (i = 0; i < rows; i++) for (j = 0; j < cols; j++) F[i + 1][j + 1] = M[i][j]; freeMatrix(M, rows);",
      "return F;"]
f2, j2 = blank(FN2, "F[i + 1][j + 1] = M[i][j];")
b2, i2 = swap(FN2, "for (j = 0; j < cols; j++)", "for (j = 0; j < cols - 1; j++)")
add(2,
    rubric=rub(("הקצאת מערך מצביעים בגודל `rows+2` והקצאת כל שורה בגודל `cols+2` עם איפוס (`calloc`), כך שהמסגרת כולה אפסים", 14),
               ("העתקת `M[i][j]` ל-`F[i+1][j+1]` לכל `i < rows` ו-`j < cols`", 14),
               ("שחרור `M` במלואו: כל שורה ואחר כך מערך המצביעים (אחרי ההעתקה)", 8),
               ("החזרת הכתובת של `F`", 4)),
    rubricSource="ai-verified",
    pitfalls=["להקצות את `F` בגודל `rows × cols` או לשכוח את תוספת 2 בכל מימד.",
              "להעתיק ל-`F[i][j]` במקום ל-`F[i+1][j+1]`, כך שהמסגרת לא נוצרת ותוכן `M` מוזז.",
              "לשחרר את `M` לפני ההעתקה, או לשחרר רק את מערך המצביעים בלי השורות."],
    steps=[
        {"type": "numeric",
         "prompt": "המטריצה `M` בעלת 3 שורות ו-4 עמודות, ואף איבר בה אינו 0. כמה איברים שווים ל-0 במטריצה `F` שמתקבלת?",
         "answer": 18, "tol": 0,
         "explain": "ל-`F` יש 5 × 6 = 30 איברים, 12 מהם מ-`M`, ולכן 18 איברי המסגרת הם 0 (ריצה אמיתית: 18)."},
        {"type": "numeric",
         "prompt": "המטריצה היא `M = {{1,2,3,4},{5,6,7,8},{9,10,11,12}}`. מה ערך `F[2][3]`?",
         "answer": 7, "tol": 0,
         "explain": "`F[2][3] = M[1][2] = 7` (ריצה אמיתית: 7)."},
        {"type": "fillblank", "prompt": "השלימו את שורת ההעתקה.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": T("F[i + 1][j + 1] = M[i][j];", "F[i][j] = M[i][j];", "F[i + 1][j] = M[i][j];", "F[i][j + 1] = M[i][j];"),
         "correctId": "a",
         "explain": "המסגרת מוסיפה שורה אחת למעלה ועמודה אחת משמאל, ולכן `M[i][j]` נכנס ל-`F[i+1][j+1]`. שאר האפשרויות מזיזות את התוכן לתאים שגויים ומשאירות אפס במקום שבו צריך להיות ערך (ריצה אמיתית: מטריצות שונות)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `matrixToFrame` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B2,
         "explain": "הצהרת המשתנים והקצאת מערך השורות, הקצאת כל שורה, העתקה ושחרור `M` ולבסוף החזרה. כל החלפה נכשלת בבנייה, קורסת או נותנת מטריצה שגויה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והעמודה האחרונה של `M` אינה מועתקת (במקומה אפסים). מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "`j < cols - 1` מדלג על העמודה האחרונה (ריצה אמיתית: העמודה `4, 8, 12` יצאה 0)."},
    ],
    stepsSource="ai-verified")

# Q3 -- processFiles
FN3 = func_lines(Q3_SOL, "void processFiles")
FR3 = func_lines(Q3_SOL, "void reverseString")
FH3 = func_lines(Q3_SOL, "int hasUniqueLetters")
B3 = ["char str[101]; FILE* fin = fopen(inputFilename, \"r\"), *fout = fopen(outputFilename, \"w\"); if (!fin || !fout) exit(1);",
      "while (fgets(str, 101, fin)) { str[strlen(str) - 1] = '\\0'; if (hasUniqueLetters(str)) { reverseString(str); fprintf(fout, \"%s\\n\", str); } }",
      "fclose(fin); fclose(fout);"]
f3, j3 = blank(FH3, "index = tolower(str[i]) - 'a';")
b3, i3 = swap(FR3, "int i = 0, j = strlen(str) - 1;", "int i = 0, j = strlen(str);")
add(3,
    rubric=rub(("`reverseString`: החלפת תווים מהקצוות פנימה עם שני אינדקסים (או מערך עזר) עד המפגש", 8),
               ("`hasUniqueLetters`: דחיית כל תו שאינו אות, והתעלמות מהבדל בין אות קטנה לגדולה (`tolower`) ובדיקת חזרה במערך מונים בן 26 תאים", 12),
               ("פתיחת שני הקבצים (קלט לקריאה, פלט לכתיבה) ובדיקת הצלחה", 6),
               ("קריאת שורה אחר שורה עם מערך עזר בגודל 101, והסרת תו השורה החדשה לפני הבדיקה", 8),
               ("כתיבת השורה ההפוכה לקובץ הפלט רק כשהיא עברה את הבדיקה, וסגירת שני הקבצים", 6)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח להסיר את `'\\n'` לפני `hasUniqueLetters`: התו אינו אות, והפונקציה דוחה כל שורה.",
              "להתייחס ל-`A` ול-`a` כאותיות שונות: `Alisa` נכנסת לפלט בטעות.",
              "להשתמש ב-`str[i] - 'a'` כאינדקס, ולגשת מחוץ לגבולות מערך המונים כשהאות גדולה."],
    steps=[
        {"type": "numeric",
         "prompt": "כמה שורות יש בקובץ הפלט עבור קובץ הקלט מהדוגמה (`abc#xyz`, `table`, `Alisa`, `Walla`, `Michael`)?",
         "answer": 2, "tol": 0,
         "explain": "רק `table` ו-`Michael` מורכבות מאותיות שונות בלבד (ריצה אמיתית: `elbat` ו-`leahciM`)."},
        {"type": "choice",
         "prompt": "איזו שורה מהדוגמה נדחית **רק** כי `A` ו-`a` נחשבות לאותה אות?",
         "options": T("`Alisa`", "`Walla`", "`table`", "`abc#xyz`"), "correctId": "a",
         "explain": "ב-`Alisa` האות היחידה החוזרת היא `A` / `a`. ב-`Walla` יש גם `ll`, ב-`abc#xyz` יש תו שאינו אות, ו-`table` מתקבלת (ריצה אמיתית: רק `Alisa` נכנסת לפלט כשמשווים בלי הבדל בין אותיות)."},
        {"type": "fillblank", "prompt": "השלימו את חישוב האינדקס של האות במערך המונים.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": T("index = tolower(str[i]) - 'a';", "index = str[i] % 26;",
                      "index = (tolower(str[i]) - 'a') / 2;", "index = 0;"),
         "correctId": "a",
         "explain": "האינדקס הוא מקום האות באלפבית אחרי המרה לאות קטנה. ב' מבחין בין `A` ל-`a` ולכן `Alisa` נכנסת לפלט, ג' מאחד אותיות סמוכות ולכן `table` נדחית, וד' דוחה כל שורה שיש בה יותר מאות אחת (ריצה אמיתית: פלט שונה בכל אחת מהן)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `processFiles` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3,
         "explain": "פתיחת הקבצים, קריאה וכתיבה בלולאה, ובסוף סגירה. כל החלפה נכשלת בבנייה או משנה את הפלט (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה של `reverseString` שורה אחת שונתה, ובקובץ הפלט מופיעות שורות ריקות במקום השורות ההפוכות. מצאו אותה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`j = strlen(str)` מצביע על תו הסיום, ולכן הוא מוחלף עם התו הראשון והמחרוזת הופכת לריקה (ריצה אמיתית: שורות ריקות)."},
    ],
    stepsSource="ai-verified")

# Q4 -- static x in fun (values from running q4.c)
Q4_OUT = ["2 2", "4 2", "2 6", "8 6", "8 10"]
add(4,
    rubric=rub(("זיהוי ש-`x` ב-`fun` הוא `static` ולכן ערכו נשמר בין הקריאות (2, 3, 4, ...), ו-`y` המקומי מאותחל ל-1 מחדש בכל קריאה ולכן תמיד 2", 3),
               ("זיהוי ש-`fun` מחזירה את הכתובת של ה-`static` ולכן הפעולה `++(*fun(...))` מקדמת אותו", 2),
               ("שלוש השורות הראשונות: `2 2`, `4 2`, `2 6`", 3),
               ("שתי השורות האחרונות: `8 6` ו-`8 10`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`x` של `fun` מאותחל ל-1 בכל קריאה, ולהדפיס `2 2` בכל השורות.",
              "לבלבל בין `x`,`y` של `main` לבין אלה של `fun`; הפרמטר `q` מצביע לעתים על `x` או `y` של `main`.",
              "לשכוח שההשמה ב-`x = ++(*fun(&x))` דורסת את `x` של `main`, ושאחרי `fun` ה-`y` של `main` נשאר 6."],
    steps=[
        {"type": "numeric",
         "prompt": "מה ערך `x` של `main` אחרי ההשמה `x = ++(*fun(&y))` בקריאה השנייה?",
         "answer": 4, "tol": 0,
         "explain": "אחרי הקריאה השנייה ה-`static x` הוא 3, והקידום נותן 4 (ריצה אמיתית: השורה `4 2`)."},
        {"type": "choice", "prompt": "מה מדפיסה השורה השלישית של הפלט?",
         "options": T("`2 6`", "`2 2`", "`6 2`", "`3 6`"), "correctId": "a",
         "explain": "בקריאה השלישית `*q = 2` נכתב ל-`x` של `main`, וה-`static x` שווה 5 ומקודם ל-6 ונכנס ל-`y` (ריצה אמיתית: `2 6`)."},
        {"type": "numeric",
         "prompt": "מה הערך השני (של `y`) בשורה האחרונה של הפלט?",
         "answer": 10, "tol": 0,
         "explain": "בקריאה החמישית ה-`static x` מגיע ל-9 ואחרי הקידום ל-10, והוא נכנס ל-`y` (ריצה אמיתית: `8 10`)."},
        {"type": "order", "prompt": "סדרו את חמש שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True, "lines": Q4_OUT,
         "explain": "ריצה אמיתית: אותן חמש שורות."},
    ],
    stepsSource="ai-verified")

# Q6 -- bonus: nested shifts
add(6,
    rubric=rub(("חישוב הביטוי הפנימי `1 << (1 << 1) = 4`, ואחריו `4 + 1 = 5` ו-`1 << 5 = 32`", 4),
               ("זיהוי ש-`(long long)1 << 32` שווה ל-$2^{32}$ ושההפחתה של 1 נותנת $2^{32}-1$ בטיפוס של 64 סיביות", 3),
               ("ההמרה ל-`int` חותכת ל-32 סיביות שכולן 1, ולכן הפלט `-1`", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחשב `1 << 32` ב-`int` (שמוגבל ל-32 סיביות) ולהגיע להתנהגות לא מוגדרת; ההמרה ל-`long long` קודמת להזזה.",
              "לחשוב שהתוצאה היא `4294967295`, ולשכוח שההמרה ל-`int` והדפסה עם `%d` נותנות `-1`."],
    steps=[
        {"type": "numeric",
         "prompt": "מה ערך `1 << (1 << 1)`?",
         "answer": 4, "tol": 0,
         "explain": "`1 << 1` הוא 2, ו-`1 << 2` הוא 4 (ריצה אמיתית: 4)."},
        {"type": "numeric",
         "prompt": "מה ערך `1 << ((1 << (1 << 1)) + 1)`, כלומר כמה סיביות מזיזים את `(long long)1`?",
         "answer": 32, "tol": 0,
         "explain": "`(1 << (1 << 1)) + 1 = 5`, ו-`1 << 5 = 32` (ריצה אמיתית: 32)."},
        {"type": "numeric",
         "prompt": "מה ערך הביטוי `((long long)1 << 32) - 1` לפני ההמרה ל-`int`?",
         "answer": 4294967295, "tol": 0,
         "explain": "$2^{32}-1 = 4294967295$ (ריצה אמיתית: 4294967295)."},
        {"type": "numeric",
         "prompt": "מה מודפס בסוף (אחרי ההמרה ל-`int` והדפסה עם `%d`)?",
         "answer": -1, "tol": 0,
         "explain": "32 הסיביות התחתונות כולן 1, שזה `-1` בייצוג משלים ל-2 (ריצה אמיתית: -1)."},
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "24B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "30.07.2024",
    "sourceFile": "24B-B exam",
    "solutionFile": "24B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
