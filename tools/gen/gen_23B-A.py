# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-A.json -- programming-workshop (C), semester B 2023, moed A (08.06.2023).
Q1 (40), Q2/Q3 (40 each, answer one; Q3 = parts a 15 / b 15 / c 10), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/23B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_23B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""בפולינום $P(x)=\sum_{i=0}^{n-1} a_i x^i$ כל איבר $a_i x^i$ ($a_i$ הוא מקדם ממשי) נקרא **מונום** $i$.

נגדיר מבנה הבא המייצג מונום:
```c
typedef struct monom {
        double coefficient;
        int power;
} Monom;
```
וגם נגדיר מבנה המייצג איבר ברשימה מקושרת:
```c
typedef struct item {
        Monom mon;
        struct item * next;
} Item;
```
כתבו פונקציה `Item * createPolynom(Item * L)` המקבלת רשימה מקושרת חד-כיוונית של איברים מטיפוס `Item`.
על הפונקציה ליצור ולהחזיר רשימה חדשה `P` (של איברים מטיפוס `Item`) המייצגת פולינום כך שאיברי הרשימה יהיו ממוינים לפי חזקות המונומים שהם מכילים (עבור $i < j$, מונום $j$ יהיה יותר קרוב לראש הרשימה מאשר מונום $i$). רשימת `P` תיווצר ע"י **סיכום המונומים** המרכיבים את `L`. ב-`P` לא יהיו מונומים עם מקדמים אפס. הרשימה הריקה (המקורית והחדשה) תייצג מספר 0.

**לדוגמא,** עבור הרשימה `L` הבאה (המספר השמאלי הוא מקדם והמספר הימני הוא חזקה): `(2,4) (-5,1) (3,6) (6,4) (-8,0) (-3,6) (7.5,3)` הפונקציה תיצור את הרשימה `P` הבאה: `(8,4) (7.5,3) (-5,1) (-8,0)` אשר מייצגת את הפולינום `8x^4+7.5x^3-5x-8`.

**שימו לב.** כדי לייעל את העיבוד של הרשימה המקורית יש להשתמש במערך עזר שגודלו תלוי בחזקה המקסימלית ברשימה הזאת. **זוהי דרישה מחייבת!**

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q1_SOL = r"""```c
Item* createPolynom(Item* L)
{
       Item* curr = L, * P = NULL;
       int max_power = 0, power;
       double *arr;

       /* Search of maximum power */
       while (curr)
       {
              if (curr->mon.power > max_power)
                     max_power = curr->mon.power;
              curr = curr->next;
       }

       /* Calculation of coefficients */
       arr = (double*)calloc(max_power + 1, sizeof(double));
       curr = L;
       while (curr)
       {
              arr[curr->mon.power] += curr->mon.coefficient;
              curr = curr->next;
       }

       /* Creation of polynomial list */
       curr = L;
       for (power = 0; power <= max_power; power++)
              if (arr[power] != 0)
              {
                     curr = (Item*)malloc(sizeof(Item));
                     curr->next = P;
                     P = curr;
                     P->mon.coefficient = arr[power];
                     P->mon.power = power;
              }

       free(arr);
       return P;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

כתבו פונקציה **יעילה** בשם `sortedRowsCols` המקבלת מערך דו-ממדי דינאמי `ar` של מספרים שלמים בעל `m` שורות ו-`n` עמודות.
על הפונקציה ליצור שני מערכים חד-ממדיים. אחד מהם (בשם `ar_s_rows`) יהיה מורכב ממספרי השורות במערך הדו-ממדי ממוינות בסדר עולה ממש והשני (בשם `ar_s_cols`) יהיה מורכב ממספרי העמודות ממוינות בסדר יורד ממש.
הפונקציה תעביר by reference את המערכים החדשים ואת הגדלים שלהם. במידה ומערך נוצר ריק, הפונקציה תעביר `NULL` ככתובתו ו-0 כגודלו.

**לדוגמא:** עבור המערך `ar` (משמאל לימין, מלמעלה למטה)
```
10  13  56  99
23  57  59  93
36  19  74  89
30  75  80  85
25  73  84  84
```
הפונקציה תעביר מערך `ar_s_rows`: `{0,1,3}` עם גודלו 3 ומערך `ar_s_cols`: `{3}` עם גודלו 1.

החתימה של הפונקציה `sortedRowsCols` תהיה:
```c
void sortedRowsCols(int **ar, int m, int n,
int **ar_s_rows, int *num_s_rows, int **ar_s_cols, int *num_s_cols)
```
לבדיקה האם השורה ממוינת יש להשתמש בפונקציית עזר `int arrSorted(int *a, int n)` המקבלת את השורה כמערך `a` בגודל `n`. הפונקציה תחזיר 1 אם המערך ממוין בסדר עולה ממש ו-0 אחרת.
לבדיקה האם העמודה ממוינת יש להשתמש בפונקציית עזר `columnSorted`. הפונקציה תקבל מערך דו-ממדי `ar`, מספר שורותיו `m`, ומספר העמודה הנבדקת `col`. על הפונקציה להחזיר 1 אם העמודה ממוינת בסדר יורד ממש ו-0 אחרת. חתימת הפונקציה תהיה `int columnSorted(int **ar, int m, int col)`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
int arrSorted(int* a, int n)
{
       int i;
       for (i = 1; i < n; i++)
              if (a[i] <= a[i - 1])
                     return 0;
       return 1;
}

int columnSorted(int** ar, int m, int col)
{
       int i;
       for (i = 1; i < m; i++)
              if (ar[i][col] >= ar[i - 1][col])
                     return 0;
       return 1;
}

void sortedRowsCols(int** ar, int m, int n, int** ar_s_rows, int* num_s_rows, int** ar_s_cols, int* num_s_cols)
{
       int i, j;
       *num_s_rows = *num_s_cols = 0;
       *ar_s_rows = (int*)calloc(m, sizeof(int)); // max size - number of rows
       *ar_s_cols = (int*)calloc(n, sizeof(int)); // max size - number of columns
       for (i = 0; i < m; i++)
              if (arrSorted(ar[i], n))
                     (*ar_s_rows)[(*num_s_rows)++] = i;
       for (j = 0; j < n; j++)
              if (columnSorted(ar, m, j))
                     (*ar_s_cols)[(*num_s_cols)++] = j;
       *ar_s_rows = (int*)realloc(*ar_s_rows, *num_s_rows * sizeof(int));
       *ar_s_cols = (int*)realloc(*ar_s_cols, *num_s_cols * sizeof(int));
}
```

**הערה:** כשאין אף שורה (או עמודה) ממוינת, גודל ההקצאה החדש הוא 0, והפתרון מסתמך על כך ש-`realloc(p, 0)` מחזיר `NULL`. זה תלוי במימוש: ב-C17 התוצאה מוגדרת-מימוש (במהדרים הנפוצים כמו glibc ו-MSVC מתקבל `NULL`, אך ספריות אחרות מחזירות מצביע ייחודי), וב-C23 ההתנהגות אינה מוגדרת. כדי להבטיח `NULL` בכל מימוש אפשר לבדוק את הגודל, ולשחרר עם `free` ולהציב `NULL` כשהוא 0."""

# ---------------------------------------------------------------- Q3
Q3_INTRO = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

נגדיר כמה תווים מסוימים כ**מפרידים**. במיוחד, תווי פסיק, נקודה, רווח, סימן קריאה, סימן שאלה, נקודתיים וכו' ניתן להגדיר כמפרידים. **מילה** היא רצף של תווים שאינם מפרידים. **משפט** הוא מחרוזת המכילה שרשור של מילים ומפרידים. המילים יכולות להיות מופרדות ע"י מפריד אחד או יותר. משפט לא ריק תמיד מתחיל במילה.

בכל השאלות הבאות אסור להשתמש בפונקציה סטנדרטית `strtok`."""

Q3A_TEXT = r"""**סעיף א (15 נק').**
כתבו פונקציה עם החתימה `char * nextWord(char * sentence, char * separators, char * word)` אשר מקבלת מחרוזת `sentence` המהווה את המשפט ומחרוזת `separators` המורכבת מכל המפרידים שעשויים להופיע במשפט.
על הפונקציה לעדכן את `word` להיות המחרוזת המכילה העתק של המילה הראשונה ב-`sentence` המוגדרת עד למפריד הראשון (ניתן להניח שגודל של מערך `word` יהיה מספיק).
הפונקציה תחזיר מצביע לתחילת המילה הבאה ב-`sentence` או `NULL` אם המשפט לא מכיל מילים נוספות.

לדוגמא: עבור `sentence = "Why?! That's why."` ו-`separators = "? !."` תוכן של `word` יהיה `"Why"` והפונקציה תחזיר מצביע לתת-מחרוזת `"That's why."` מתוך `sentence`."""

Q3A_SOL = r"""```c
char* nextWord(char* sentence, char* separators, char* word)
{
       int i = 0;
       while ( sentence[i] && !strchr(separators, sentence[i]) ) // scan word
              word[i++] = sentence[i];
       word[i] = '\0';
       while (sentence[i] && strchr(separators, sentence[i])) // scan separators
              i++;
       return sentence[i] ? sentence + i : NULL;
}
```

**הערה:** השורה `word[i++] = sentence[i];` מהפתרון הרשמי משתמשת ב-`i` ומשנה אותו באותו ביטוי בלי נקודת רצף ביניהם, ולכן לפי תקן C ההתנהגות שלה אינה מוגדרת (התוצאה תלויה בסדר שבו המהדר מעריך את שני האגפים). במהדרים הנפוצים מתקבל הערך הצפוי, אבל כדאי לכתוב את השקול המוגדר היטב: `word[i] = sentence[i]; i++;` (בגוף לולאה עם סוגריים מסולסלים)."""

Q3B_TEXT = r"""**סעיף ב (15 נק').**
כתבו פונקציה עם החתימה `int breakSentence(char * sentence, char * separators, char * file_name)` אשר מקבלת אותן מחרוזות `sentence` ו-`separators` שבסעיף א' וגם מחרוזת `file_name` המהווה שם של קובץ טקסט.
על הפונקציה לשמור את המילים של המשפט בקובץ שנוצר (כל מילה בשורה נפרדת) ולהחזיר את כמות המילים במשפט.

לדוגמא: עבור `sentence = "But why?! That's why."` ו-`separators = "? !."` הפונקציה תחזיר 4 ותוכן הקובץ יהיה
```
But
why
That's
why
```
יש להשתמש בפונקציה `nextWord` כפונקציית עזר.
אפשר להשתמש במערך עזר. במקרה זה, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3B_SOL = r"""```c
int breakSentence(char* sentence, char* separators, char* file_name)
{
       FILE* fptr = fopen(file_name, "w");
       char* word;
       int count = 0;
       if (!fptr)
              return -1;
       word = (char*)malloc(strlen(sentence) + 1);
       while ( (sentence = nextWord(sentence, separators, word)) != NULL )
       {
              fprintf(fptr, "%s\n", word);
              count++;
       }
       if (*word) // sentence isn't empty
       {
              fprintf(fptr, "%s\n", word); // last word
              count++;
       }
       free(word);
       fclose(fptr);
       return count;
}
```"""

Q3C_TEXT = r"""**סעיף ג (10 נק').**
כתבו פונקציה עם החתימה `int countWordOccur(char * sentence, char * separators, char * query)` אשר מקבלת אותן מחרוזות `sentence` ו-`separators` שבסעיף א' וגם מחרוזת `query` המהווה מילה כלשהי.
על הפונקציה להחזיר את כמות המופעים של המילה `query` ב-`sentence`.

לדוגמא, עבור `sentence = "But why?! That's why. And don't ask me why."`, `separators = "? !."` ו-`query = "why"` הפונקציה תחזיר 3.
יש להשתמש בפונקציה `nextWord` כפונקציית עזר.
אפשר להשתמש במערך עזר. במקרה זה, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3C_SOL = r"""```c
int countWordOccur(char* sentence, char* separators, char* query)
{
       char* word;
       int count = 0;
       word = (char*)malloc(strlen(sentence) + 1);
       while ( (sentence = nextWord(sentence, separators, word)) != NULL )
              if (strcmp(word, query) == 0)
                     count++;
       if (strcmp(word, query) == 0) // last word
              count++;
       free(word);
       return count;
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
int x = 30, y = 0;
void f1(int x)
{
    printf("x=%d,y=%d\n", x, y);
    x = y = 10;
}
void f2(int y)
{
    printf("x=%d,y=%d\n", x, y);
    x = y = 15;
}
int main()
{
    y = 5;
    f1(20);
    f2(y);
    printf("x=%d,y=%d\n", x, y);
    return 0;
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
x=20,y=5
x=30,y=10
x=15,y=10
```
**נימוק:**
אין משתנים `x,y` ב-`main`. לכן ב-`main` עובדים עם משתנים גלובליים. `y` שמאותחל ב-0 יקבל ערך חדש 5.
אחרי קריאה ל-`f1(20)` פרמטר פורמלי `x` של `f1` יקבל ערך 20. אין משתנה `y` ב-`f1` ולכן הפונקציה עובדת עם `y` גלובלי אשר שווה ל-5. לכן `printf` ב-`f1` מדפיסה
`x=20,y=5`
לאחר מכן `x` פורמלי ו-`y` גלובלי משתנים ב-10.
אחרי קריאה ל-`f2(y)` פרמטר פורמלי `y` של `f2` יקבל ערך 10 של `y` גלובלי. אין משתנה `x` ב-`f2` ולכן הפונקציה עובדת עם `x` גלובלי אשר מאותחל ב-30. לכן `printf` ב-`f2` מדפיסה
`x=30,y=10`
לאחר מכן `x` גלובלי ו-`y` פורמלי משתנים ב-15.
ואז לאחר חזרה ל-`main`, `x` גלובלי שווה ל-15 ו-`y` גלובלי שווה ל-10. לכן `printf` ב-`main` מדפיסה
`x=15,y=10`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + "מהי הטענה הנכונה?"
Q5A_OPTS = opts(r'הקריאות `puts("abc")` ו-`fputs("abc",stdout)` הן שקולות',
                r'הקריאות `puts("abc")` ו-`fputs("abc\n",stdout)` הן שקולות',
                r'הקריאות `puts("abc\n")` ו-`fputs("abc",stdout)` הן שקולות',
                r'הקריאות `puts("abc")` ו-`fputs("\nabc",stdout)` הן שקולות',
                "אף טענה אינה נכונה")
Q5A_EXPL = r"""לעומת `puts`, `fputs` לא מוסיפה `'\n'` בסוף המחרוזת. לכן `fputs("abc",stdout)` מציגה במסך `abc` ללא הורדת שורה. בזאת `fputs("abc\n",stdout)` מציגה במסך `abc` ומורידה סמן לשורה הבאה, בדיוק כמו `puts("abc")`."""

Q5B_TEXT = Q5_INTRO + "איזה פעולה היא בלתי חוקית?"
Q5B_OPTS = opts("חיבור של מספר שלם למצביע",
                "חיסור של מספר שלם ממצביע",
                "חיבור של מצביע למצביע",
                "חיסור של מצביע ממצביע",
                "השוואת מצביעים",
                "כל הפעולות לעיל הן חוקיות")
Q5B_EXPL = "בשפת C מוגדרות הפעולות הבאות על מצביעים: חיבור (חיסור) מספר שלם למצביע (התוצאה היא כתובת), חיסור מצביעים (התוצאה היא מספר שלם), השוואת מצביעים. פעולת חיבור מצביעים לא מוגדרת."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <string.h>
void main()
{
    puts("puts"-strlen("strlen")+sizeof"sizeof");
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `uts`

**נימוק:**
הפונקציה `strlen` מחזירה מספר תווים במחרוזת עד לתו אפסי לא כולל תו אפסי. לכן `strlen("strlen")` מחזירה 6.
אופרטור `sizeof` מחזיר את גודל האופרנד בבתים. מחרוזת `"sizeof"` מהווה 7 תווים כולל תו אפסי. לכן `sizeof"sizeof"` מחזיר 7.
ואז המשפט שקול ל-`puts("puts"-6+7)` ז"א ל-`puts("puts"+1)`.
למחרוזת קבועה במשפט צריך להתייחס כמו לכתובת התו הראשון שלה. בזאת מקבלים למעשה `puts("uts")`. לכן הפלט יהיה
`uts`"""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/23B-A-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "strings", Q3A_TEXT, Q3A_SOL, points=15, part="א", contextId="c1"),
    Q(3, "code", "files", Q3B_TEXT, Q3B_SOL, points=15, part="ב", contextId="c1"),
    Q(3, "code", "strings", Q3C_TEXT, Q3C_SOL, points=10, part="ג", contextId="c1"),
    Q(4, "code", "storage_classes", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "files", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "b", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "pointers", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "c", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "c_traps_mcq", Q6_TEXT, Q6_SOL, points=10),
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


def swap_nth(lines, old, new, nth):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == old.strip()]
    assert len(idx) > nth, old
    out = list(lines)
    out[idx[nth]] = out[idx[nth]].replace(old.strip(), new.strip())
    return out, idx[nth]


# Q1 -- createPolynom
F1 = func_lines(Q1_SOL, "Item* createPolynom")
B1 = ["Item* curr = L, * P = NULL; int max_power = 0, power; double *arr;",
      "while (curr) { if (curr->mon.power > max_power) max_power = curr->mon.power; curr = curr->next; } arr = (double*)calloc(max_power + 1, sizeof(double));",
      "curr = L; while (curr) { arr[curr->mon.power] += curr->mon.coefficient; curr = curr->next; }",
      "for (power = 0; power <= max_power; power++) if (arr[power] != 0) { curr = (Item*)malloc(sizeof(Item)); curr->next = P; P = curr; P->mon.coefficient = arr[power]; P->mon.power = power; }",
      "free(arr); return P;"]
f1, j1 = blank(F1, "arr[curr->mon.power] += curr->mon.coefficient;")
b1, i1 = swap(F1, "if (arr[power] != 0)", "if (arr[power] > 0)")
add(1,
    rubric=rub(("מציאת החזקה המקסימלית ברשימה `L` במעבר אחד", 8),
               ("הקצאת מערך עזר מאופס בגודל `max_power+1` וסכימת המקדמים לפי חזקה: `arr[power] += coefficient`", 14),
               ("בניית הרשימה החדשה מהמערך: איבר `Item` חדש רק לכל מקדם שונה מ-0, והכנסה לראש הרשימה במעבר מחזקה קטנה לגדולה כדי שהרשימה תהיה ממוינת בסדר יורד", 12),
               ("שחרור מערך העזר והחזרת הרשימה (`NULL` לרשימה ריקה או כשכל המקדמים מתאפסים)", 6)),
    rubricSource="ai-verified",
    pitfalls=["להקצות את מערך העזר בגודל `n` (מספר האיברים) ולא `max_power+1`, או להשתמש ב-`malloc` בלי איפוס.",
              "לכלול ברשימה החדשה מונומים שהמקדם הסופי שלהם 0 (למשל `(3,6)` ו-`(-3,6)` שמתבטלים).",
              "להכניס לסוף הרשימה או לעבור על המערך מהחזקה הגדולה לקטנה, ולקבל רשימה ממוינת בסדר עולה."],
    steps=[
        {"type": "numeric",
         "prompt": "מה החזקה המקסימלית ברשימה `L` מהדוגמה: `(2,4) (-5,1) (3,6) (6,4) (-8,0) (-3,6) (7.5,3)`?",
         "answer": 6, "tol": 0,
         "explain": "החזקות הן 4, 1, 6, 4, 0, 6, 3 והגדולה שבהן 6, ולכן מערך העזר בגודל 7 (ריצה אמיתית: 6)."},
        {"type": "numeric",
         "prompt": "אחרי הסכימה, מה ערך `arr[4]` בדוגמה?",
         "answer": 8, "tol": 0,
         "explain": "שני המונומים בחזקה 4 הם `2` ו-`6`, וסכומם 8 (ריצה אמיתית: 8, המונום `(8,4)` ברשימה החדשה)."},
        {"type": "fillblank", "prompt": "השלימו את שורת הסכימה.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": T("arr[curr->mon.power] += curr->mon.coefficient;", "arr[curr->mon.power] = curr->mon.coefficient;",
                      "arr[curr->mon.power] += curr->mon.power;", "arr[max_power - curr->mon.power] += curr->mon.coefficient;"),
         "correctId": "a",
         "explain": "יש לסכום את המקדמים של אותה חזקה באותו תא. ב' דורס את הערך הקודם (`arr[4]` היה 6 במקום 8), ג' מוסיף חזקות במקום מקדמים, וד' מציב בתא שגוי (ריצה אמיתית: רשימות שונות בכל אחת מהן)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `createPolynom` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "הצהרות, חישוב החזקה המקסימלית והקצאת מערך העזר, סכימת המקדמים, בניית הרשימה מהמערך, ובסוף שחרור והחזרה. כל החלפה נכשלת בבנייה, קורסת או נותנת רשימה שגויה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והרשימה החדשה אינה כוללת את המונומים בעלי מקדם שלילי (`(-5,1)` ו-`(-8,0)`). מצאו את השורה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "התנאי `> 0` מדלג על מקדם שלילי; הנכון הוא `!= 0` (ריצה אמיתית: נשארים רק `(8,4)` ו-`(7.5,3)`)."},
    ],
    stepsSource="ai-verified")

# Q2 -- sortedRowsCols
FA2 = func_lines(Q2_SOL, "int arrSorted")
FC2 = func_lines(Q2_SOL, "int columnSorted")
FS2 = func_lines(Q2_SOL, "void sortedRowsCols")
B2 = ["int i, j; *num_s_rows = *num_s_cols = 0; *ar_s_rows = (int*)calloc(m, sizeof(int)); *ar_s_cols = (int*)calloc(n, sizeof(int));",
      "for (i = 0; i < m; i++) if (arrSorted(ar[i], n)) (*ar_s_rows)[(*num_s_rows)++] = i; for (j = 0; j < n; j++) if (columnSorted(ar, m, j)) (*ar_s_cols)[(*num_s_cols)++] = j;",
      "*ar_s_rows = (int*)realloc(*ar_s_rows, *num_s_rows * sizeof(int)); *ar_s_cols = (int*)realloc(*ar_s_cols, *num_s_cols * sizeof(int));"]
f2, j2 = blank(FC2, "if (ar[i][col] >= ar[i - 1][col])")
b2, i2 = swap(FA2, "if (a[i] <= a[i - 1])", "if (a[i] < a[i - 1])")
add(2,
    rubric=rub(("`arrSorted`: מעבר על השורה והחזרת 0 כשיש זוג סמוך שאינו עולה ממש (`a[i] <= a[i-1]`)", 8),
               ("`columnSorted`: מעבר על העמודה והחזרת 0 כשיש זוג סמוך שאינו יורד ממש (`>=`)", 8),
               ("הקצאת שני מערכים בגודל המרבי (`m` ו-`n`) ואיפוס הגדלים", 8),
               ("מעבר על כל השורות והעמודות, שימוש בפונקציות העזר ואיסוף האינדקסים בסדר", 10),
               ("כיווץ המערכים לגודל המדויק עם `realloc`, כך שמערך ריק הוא `NULL` וגודלו 0", 6)),
    rubricSource="ai-verified",
    pitfalls=["לבדוק מיון חלש (`a[i] < a[i-1]` במקום `<=`) ולקבל שורות עם ערכים שווים כמו `25 73 84 84`.",
              "לבדוק עמודה בסדר עולה במקום יורד, או לעבור על העמודה עם מספר העמודות במקום מספר השורות.",
              "לא לכווץ את המערכים, ולהשאיר בהם תאים מיותרים ולא מאופסים כשחלק מהשורות אינן ממוינות."],
    steps=[
        {"type": "numeric",
         "prompt": "בדוגמה (מטריצה 5 × 4), כמה שורות ממוינות בסדר עולה ממש? זהו `*num_s_rows`.",
         "answer": 3, "tol": 0,
         "explain": "שורות 0, 1 ו-3 עולות ממש; שורה 2 (`36 19 ...`) ושורה 4 (`... 84 84`) אינן (ריצה אמיתית: `0 1 3`)."},
        {"type": "numeric",
         "prompt": "בדוגמה, כמה עמודות ממוינות בסדר יורד ממש? זהו `*num_s_cols`.",
         "answer": 1, "tol": 0,
         "explain": "רק עמודה 3 (`99 93 89 85 84`) יורדת ממש (ריצה אמיתית: `3`)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הדחייה ב-`columnSorted`: העמודה יורדת ממש, ולכן...", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": T("if (ar[i][col] >= ar[i - 1][col])", "if (ar[i][col] > ar[i - 1][col])",
                      "if (ar[i][col] <= ar[i - 1][col])", "if (ar[i][col] < ar[i - 1][col])"),
         "correctId": "a",
         "explain": "עמודה יורדת ממש כשכל איבר קטן ממש מקודמו, ולכן דוחים כשהאיבר גדול או שווה (`>=`). ב' מקבל עמודות עם ערכים שווים, וג' ו-ד' בודקים סדר עולה (ריצה אמיתית: אינדקסים שונים על מטריצות הבדיקה)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `sortedRowsCols` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B2,
         "explain": "הכנה (הצהרות, איפוס והקצאה), מעבר שמאסף את האינדקסים, ובסוף כיווץ המערכים. כל החלפה כותבת למערך שלא הוקצה או מכווצת לפני האיסוף (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה של `arrSorted` שורה אחת שונתה, והשורה `25 73 84 84` נחשבת בטעות לממוינת. מצאו את השורה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "`<` במקום `<=` מקבל שני ערכים שווים (`84 84`) כאילו הם עולים ממש; בריצה אמיתית מתקבל `0 1 3 4` במקום `0 1 3`."},
    ],
    stepsSource="ai-verified")

# Q3 -- parts a, b, c (nextWord, breakSentence, countWordOccur)
FN3A = func_lines(Q3A_SOL, "char* nextWord")
# the official `word[i++] = sentence[i];` is UB (unsequenced): the steps use the well-defined equivalent
_k = [n for n, ln in enumerate(FN3A) if ln.strip() == "word[i++] = sentence[i];"]
assert len(_k) == 1
FN3A[_k[0]:_k[0] + 1] = ["       {", "              word[i] = sentence[i];", "              i++;", "       }"]
B3A = ["int i = 0;",
       "while ( sentence[i] && !strchr(separators, sentence[i]) ) { word[i] = sentence[i]; i++; }",
       "word[i] = '\\0';",
       "while (sentence[i] && strchr(separators, sentence[i])) i++;",
       "return sentence[i] ? sentence + i : NULL;"]
f3a, j3a = blank(FN3A, "while ( sentence[i] && !strchr(separators, sentence[i]) )")
b3a, i3a = swap(FN3A, "return sentence[i] ? sentence + i : NULL;", "return sentence + i;")
add(3, "א",
    rubric=rub(("העתקת תווי המילה הראשונה ל-`word` עד המפריד הראשון או סוף המחרוזת (הבדיקה בעזרת `strchr` על `separators`)", 6),
               ("סיום `word` ב-`'\\0'`", 3),
               ("דילוג על כל המפרידים שאחרי המילה", 3),
               ("החזרת מצביע לתחילת המילה הבאה, או `NULL` כשאין מילה נוספת", 3)),
    rubricSource="ai-verified",
    pitfalls=["לעצור רק ברווח ולא בכל אחד מהמפרידים (למשל `Why?!` תועתק כולה).",
              "לדלג על מפריד אחד בלבד, ולהחזיר מצביע שמצביע על מפריד נוסף.",
              "להחזיר מצביע לסוף המחרוזת במקום `NULL` כשהמשפט נגמר, ולגרום ללולאה אינסופית אצל הקורא."],
    steps=[
        {"type": "numeric",
         "prompt": "עבור `sentence = \"Why?! That's why.\"` ו-`separators = \"? !.\"`, באיזה אינדקס ב-`sentence` מתחילה המחרוזת שהפונקציה מחזירה?",
         "answer": 6, "tol": 0,
         "explain": "המילה `Why` תופסת את האינדקסים 0 עד 2, אחריה שלושה מפרידים באינדקסים 3, 4, 5 (`?`, `!` ורווח), ולכן המילה הבאה מתחילה באינדקס 6 (ריצה אמיתית: `That's why.`)."},
        {"type": "choice",
         "prompt": "מה מחזירה הפונקציה כשהמילה הראשונה היא האחרונה במשפט (למשל `sentence = \"why\"`)?",
         "options": T("`NULL`", "מצביע לתו הסיום של `sentence`", "מצביע לתחילת `sentence`", "מצביע לתחילת `word`"), "correctId": "a",
         "explain": "אחרי המילה אין עוד תווים, ולכן `sentence[i]` הוא `'\\0'` והפונקציה מחזירה `NULL` (ריצה אמיתית: `NULL`)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הלולאה שמעתיקה את המילה.", "code": True,
         "lines": f3a, "blankIndex": j3a,
         "options": T("while ( sentence[i] && !strchr(separators, sentence[i]) )", "while ( sentence[i] && strchr(separators, sentence[i]) )",
                      "while ( sentence[i] && sentence[i] != ' ' )", "while ( sentence[i] && sentence[i] != '?' && sentence[i] != '!' )"),
         "correctId": "a",
         "explain": "מעתיקים כל עוד התו אינו מפריד (ואינו סוף המחרוזת). ב' מעתיק את המפרידים במקום את המילה, ג' מתעלם מהמפרידים שאינם רווח, וד' מכיר רק שני מפרידים (ריצה אמיתית: רשימת מילים שגויה במשפט המלא)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `nextWord` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3A,
         "explain": "אתחול `i`, העתקת המילה, סיום המחרוזת, דילוג על המפרידים והחזרה. כל החלפה נכשלת בבנייה או משנה את `word` או את הערך המוחזר (נבדק בריצה, עם מאגר שמלא בתו אחר מההתחלה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והפונקציה אף פעם לא מחזירה `NULL`, ולכן הלולאה אצל הקורא לא נעצרת. מצאו את השורה.", "code": True,
         "lines": b3a, "bugIndex": i3a,
         "explain": "`return sentence + i;` מחזירה תמיד מצביע (גם לסוף המחרוזת) ולכן הקורא לא מזהה את סוף המשפט (ריצה אמיתית: התוכנית ממשיכה לקבל מצביע שאינו `NULL`)."},
    ],
    stepsSource="ai-verified")

FN3B = func_lines(Q3B_SOL, "int breakSentence")
B3B = ["FILE* fptr = fopen(file_name, \"w\"); char* word; int count = 0; if (!fptr) return -1;",
       "word = (char*)malloc(strlen(sentence) + 1);",
       "while ( (sentence = nextWord(sentence, separators, word)) != NULL ) { fprintf(fptr, \"%s\\n\", word); count++; }",
       "if (*word) { fprintf(fptr, \"%s\\n\", word); count++; }",
       "free(word); fclose(fptr); return count;"]
f3b, j3b = blank(FN3B, "if (*word)")
b3b, i3b = swap_nth(FN3B, 'fprintf(fptr, "%s\\n", word);', 'fprintf(fptr, "%s", word);', 0)
add(3, "ב",
    rubric=rub(("פתיחת הקובץ לכתיבה ובדיקת הצלחה", 3),
               ("הקצאת מערך עזר ל-`word` בגודל מספיק (`strlen(sentence)+1`)", 2),
               ("לולאה שקוראת ל-`nextWord`, כותבת כל מילה לשורה נפרדת וסופרת", 5),
               ("טיפול במילה האחרונה אחרי הלולאה (כש-`nextWord` מחזירה `NULL`), ובמשפט ריק שבו אין מילה", 3),
               ("שחרור המערך, סגירת הקובץ והחזרת כמות המילים", 2)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את המילה האחרונה: `nextWord` מחזירה `NULL` כשהיא כבר העתיקה את המילה האחרונה ל-`word`, והלולאה נגמרת לפניה.",
              "לכתוב מילה ריקה לקובץ כשהמשפט ריק, בלי לבדוק `*word`.",
              "לכתוב מילים בלי `'\\n'` ולקבל שורה אחת בקובץ."],
    steps=[
        {"type": "numeric",
         "prompt": "עבור `sentence = \"But why?! That's why.\"` כמה מילים נכתבות לקובץ **בתוך הלולאה** (לפני הטיפול במילה האחרונה)?",
         "answer": 3, "tol": 0,
         "explain": "המילים `But`, `why`, `That's` נכתבות בלולאה, והמילה `why` האחרונה נכתבת אחריה (ריצה אמיתית: הלולאה כתבה 3, והפונקציה החזירה 4)."},
        {"type": "numeric",
         "prompt": "מה מחזירה `breakSentence` עבור אותו משפט?",
         "answer": 4, "tol": 0,
         "explain": "ארבע מילים: `But`, `why`, `That's`, `why` (ריצה אמיתית: 4)."},
        {"type": "fillblank", "prompt": "השלימו את התנאי לכתיבת המילה האחרונה אחרי הלולאה.", "code": True,
         "lines": f3b, "blankIndex": j3b,
         "options": T("if (*word)", "if (word)", "if (!*word)", "if (count > 0)"),
         "correctId": "a",
         "explain": "יש מילה אחרונה כש-`word` אינו מחרוזת ריקה. ב' תמיד נכון וכותב מילה ריקה למשפט ריק, ג' הפוך, וד' מפספס משפט בן מילה אחת (שבו `count` נשאר 0) (ריצה אמיתית: ספירות שגויות על משפט ריק ועל משפט בן מילה אחת)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `breakSentence` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3B,
         "explain": "פתיחה, הקצאת `word`, לולאת הכתיבה, כתיבת המילה האחרונה ובסוף שחרור, סגירה והחזרה. כל החלפה נכשלת בבנייה, קורסת או משנה את תוכן הקובץ או את הספירה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ובקובץ כל המילים נדבקות זו לזו בשורה אחת. מצאו את השורה.", "code": True,
         "lines": b3b, "bugIndex": i3b,
         "explain": "הפורמט `\"%s\"` בלי `'\\n'` בתוך הלולאה כותב את המילים ברצף (ריצה אמיתית: הקובץ הוא שורה אחת, `ButwhyThat'swhy`, במקום ארבע שורות)."},
    ],
    stepsSource="ai-verified")

FN3C = func_lines(Q3C_SOL, "int countWordOccur")
B3C = ["char* word; int count = 0; word = (char*)malloc(strlen(sentence) + 1);",
       "while ( (sentence = nextWord(sentence, separators, word)) != NULL ) if (strcmp(word, query) == 0) count++;",
       "if (strcmp(word, query) == 0) count++;",
       "free(word); return count;"]
f3c, j3c = blank(FN3C, "if (strcmp(word, query) == 0)", nth=0)
b3c, i3c = swap_nth(FN3C, "if (strcmp(word, query) == 0)", "if (strcmp(word, query) != 0)", 1)
add(3, "ג",
    rubric=rub(("הקצאת מערך עזר ל-`word` ואתחול מונה", 2),
               ("לולאה על המילים עם `nextWord` והשוואת כל מילה ל-`query` עם `strcmp` (ולא השוואת מצביעים)", 4),
               ("בדיקת המילה האחרונה אחרי הלולאה", 3),
               ("שחרור והחזרת המונה", 1)),
    rubricSource="ai-verified",
    pitfalls=["להשוות `word == query` (כתובות) במקום `strcmp`.",
              "לשכוח את המילה האחרונה שנשארה ב-`word` אחרי שהלולאה נגמרה.",
              "לספור מילים שמכילות את `query` כתת-מחרוזת, באמצעות `strstr`."],
    steps=[
        {"type": "numeric",
         "prompt": "עבור `\"But why?! That's why. And don't ask me why.\"` ו-`query = \"why\"`, כמה פעמים נספרת המילה `why` **בתוך הלולאה** (לפני בדיקת המילה האחרונה)?",
         "answer": 2, "tol": 0,
         "explain": "שתי המילים `why` הראשונות נספרות בלולאה, והשלישית נשארת ב-`word` ונבדקת אחריה (ריצה אמיתית: 2 בלולאה, ו-3 בסך הכול)."},
        {"type": "numeric",
         "prompt": "מה מחזירה `countWordOccur` עבור אותו משפט?",
         "answer": 3, "tol": 0,
         "explain": "המילה `why` מופיעה שלוש פעמים (ריצה אמיתית: 3)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי ההשוואה בלולאה.", "code": True,
         "lines": f3c, "blankIndex": j3c,
         "options": T("if (strcmp(word, query) == 0)", "if (strcmp(word, query))", "if (word == query)", "if (strlen(word) == strlen(query))"),
         "correctId": "a",
         "explain": "`strcmp` מחזירה 0 כשהמחרוזות שוות. ב' סופר את המילים השונות, ג' משווה כתובות (אף פעם לא שוות) וד' סופר כל מילה באותו אורך (ריצה אמיתית: ספירות שגויות בכל אחת מהן)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `countWordOccur` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3C,
         "explain": "הכנה, לולאת המילים, בדיקת המילה האחרונה ובסוף שחרור והחזרה. כל החלפה נכשלת בבנייה או נותנת ספירה שגויה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה 2 במקום 3 על המשפט הנתון. מצאו את השורה.", "code": True,
         "lines": b3c, "bugIndex": i3c,
         "explain": "בבדיקת המילה האחרונה `!= 0` סופר אותה רק כשהיא שונה מ-`query` (ריצה אמיתית: 2)."},
    ],
    stepsSource="ai-verified")

# Q4 -- globals and parameters (values from running q4.c)
Q4_OUT = ["x=20,y=5", "x=30,y=10", "x=15,y=10"]
add(4,
    rubric=rub(("`main` עובדת עם `x`,`y` הגלובליים, ולכן `y = 5`", 2),
               ("`f1(20)`: הפרמטר `x` מסתיר את הגלובלי, `y` גלובלי, והפלט `x=20,y=5`", 3),
               ("`f2(y)`: הפרמטר `y` (עותק של 10) מסתיר את הגלובלי, ו-`x` גלובלי 30, והפלט `x=30,y=10`", 3),
               ("הפלט ב-`main`: `x=15,y=10`, כי ההשמה ב-`f2` שינתה את `x` הגלובלי ל-15, וההשמה ב-`f1` שינתה את `y` הגלובלי ל-10", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`x = y = 10` ב-`f1` משנה את `x` הגלובלי: הוא משנה את הפרמטר `x`, ורק את `y` הגלובלי.",
              "לחשוב ש-`x = y = 15` ב-`f2` משנה את `y` הגלובלי: הוא משנה רק את הפרמטר `y` ואת `x` הגלובלי.",
              "להדפיס `x=30` בשורה האחרונה בלי לשים לב ש-`f2` שינתה את `x` הגלובלי."],
    steps=[
        {"type": "numeric",
         "prompt": "מה ערך `x` שמדפיסה `f1(20)`?",
         "answer": 20, "tol": 0,
         "explain": "הפרמטר `x` מסתיר את `x` הגלובלי (ריצה אמיתית: `x=20,y=5`)."},
        {"type": "numeric",
         "prompt": "מה ערך `x` שמדפיסה `f2(y)` (בקריאה השנייה)?",
         "answer": 30, "tol": 0,
         "explain": "ב-`f2` אין פרמטר או משתנה בשם `x`, ולכן זה `x` הגלובלי, ש-`f1` לא שינתה (ריצה אמיתית: `x=30,y=10`)."},
        {"type": "numeric",
         "prompt": "מה ערך `y` שמדפיסה `printf` האחרונה ב-`main`?",
         "answer": 10, "tol": 0,
         "explain": "`f1` שינתה את `y` הגלובלי ל-10, ו-`f2` שינתה רק את הפרמטר `y` שלה (ריצה אמיתית: `x=15,y=10`)."},
        {"type": "order", "prompt": "סדרו את שלוש שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True, "lines": Q4_OUT,
         "explain": "ריצה אמיתית: אותן שלוש שורות."},
    ],
    stepsSource="ai-verified")

# Q6 -- bonus: "puts" - strlen("strlen") + sizeof "sizeof"
add(6,
    rubric=rub(("`strlen(\"strlen\")` שווה 6", 3),
               ("`sizeof\"sizeof\"` שווה 7 (שבעה תווים כולל התו האפסי)", 3),
               ("המחרוזת הקבועה היא כתובת: `\"puts\" - 6 + 7` שקול ל-`\"puts\" + 1`, ולכן `puts` מדפיסה `uts`", 4)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`sizeof\"sizeof\"` שווה 6 ולשכוח את התו האפסי, ולקבל `puts`.",
              "לנסות לחסר מספר ממחרוזת כערך מספרי, במקום לראות בה כתובת של התו הראשון."],
    steps=[
        {"type": "numeric",
         "prompt": "מה ערך `strlen(\"strlen\")`?",
         "answer": 6, "tol": 0,
         "explain": "שישה תווים, בלי התו האפסי (ריצה אמיתית: 6)."},
        {"type": "numeric",
         "prompt": "מה ערך `sizeof\"sizeof\"`?",
         "answer": 7, "tol": 0,
         "explain": "מחרוזת קבועה בת שישה תווים תופסת 7 בתים כולל התו האפסי (ריצה אמיתית: 7)."},
        {"type": "numeric",
         "prompt": "בכמה תווים מוזזת הכתובת `\"puts\"` בביטוי `\"puts\" - strlen(\"strlen\") + sizeof\"sizeof\"`?",
         "answer": 1, "tol": 0,
         "explain": "-6 + 7 = 1, ולכן המצביע מצביע על התו השני (ריצה אמיתית: מודפס `uts`)."},
        {"type": "text", "prompt": "מה הפלט של התוכנית?",
         "accept": ["uts"], "normalize": "none",
         "explain": "`puts(\"puts\" + 1)` מדפיסה את `uts` (ריצה אמיתית: `uts`)."},
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "23B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ג, מועד א'",
    "year": 2023,
    "examDate": "08.06.2023",
    "sourceFile": "23B-A exam",
    "solutionFile": "23B-A official solution",
    "contexts": {"c1": {"kind": "text", "title": "שאלה 3 - הגדרות", "text": Q3_INTRO}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
