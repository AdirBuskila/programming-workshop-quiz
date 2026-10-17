# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-A.json -- programming-workshop (C), semester B 2024, moed A.
Q1 (40), Q2/Q3 (40 each, answer one), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/24B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_24B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר מבנה המייצג איבר ברשימה מקושרת:
```c
typedef struct item {
        int digit;
        struct item* next;
} Item;
```
נייצג מספר לא שלילי שלם `M` באמצעות רשימה מקושרת חד-ממדית `L` של איברים מטיפוס `Item`, כך ששדה `digit` של כל איבר ברשימה מכיל ספרה אחת של המספר (הספרה המשמעותית ביותר של `M` - באיבר הראשון של `L`, ..., הספרה הכי פחות משמעותית של `M` - באיבר האחרון של `L`). שדה `digit` של האיבר הראשון של `L` יהיה 0 רק עבור `M=0`. במקרה זה, `L` תהיה מורכבת מהאיבר היחיד.

כתבו פונקציה `int numListCmp(Item * L1, Item * L2)` המקבלת רשימות `L1` ו-`L2` אשר משווה את המספרים המיוצגים ע"י הרשימות.
אם המספר המיוצג ע"י `L1` קטן מהמספר המיוצג ע"י `L2` הפונקציה תחזיר `-1`. אם המספר המיוצג ע"י `L1` גדול מהמספר המיוצג ע"י `L2` הפונקציה תחזיר `1`. עבור המספרים השווים הפונקציה תחזיר `0`.

**דוגמאות:** (איור: שלוש זוגות רשימות, ראו התמונה)
- `L1: 9,9,9,9` ו-`L2: 1,0,0,0,0` - הפונקציה תחזיר `-1`.
- `L1: 5,3,7,0,1` ו-`L2: 5,3,6,8,7` - הפונקציה תחזיר `1`.
- `L1: 2,3,4,6,9` ו-`L2: 2,3,4,6,9` - הפונקציה תחזיר `0`.

**שימו לב:** יש לבצע את ההשוואה אך ורק ישירות על הרשימות. הפתרון של המרת הרשימות למספרים ולאחר מכן השוואת המספרים אינו מתקבל!"""

Q1_SOL = r"""**גרסה ראשונה:**
```c
int numListCmp(Item* L1, Item* L2)
{
       int diff = 0;
       while (!diff && L1 && L2)
       { /* search of the first difference and of a list end */
              if (L1->digit < L2->digit)
                     diff = -1;
              else
                     if (L1->digit > L2->digit)
                            diff = 1;
              L1 = L1->next;
              L2 = L2->next;
       }
       if (!diff)
       { /* if no unequal digits than the result is determined by list lengths */
              if (!L1 && L2)
                     return -1;
              else
                     if (L1 && !L2)
                            return 1;
              return 0;
       }
       /* there are unequal digits */
       while (L1 && L2)
       {
              L1 = L1->next;
              L2 = L2->next;
       }
       /* longer list represents greater number */
       if (!L1 && L2)
              return -1;
       else
              if (L1 && !L2)
                     return 1;
       return diff; // for equal-length lists the result is determined by the first difference
}
```
**גרסה שנייה:**
```c
int numListCmp_2(Item* L1, Item* L2)
{
       Item* ptr1 = L1, * ptr2 = L2;
       int diff = 0;
       /* comparison of list lengths */
       while (ptr1 && ptr2)
       {
              ptr1 = ptr1->next;
              ptr2 = ptr2->next;
       }
       if (!ptr1 && ptr2)
              return -1;
       else
              if (ptr1 && !ptr2)
                     return 1;
       /* search of the first difference in lists of equal lengths */
       while (L1)
       {
              if (L1->digit < L2->digit)
                     return -1;
              else
                     if (L1->digit > L2->digit)
                            return 1;
              L1 = L1->next;
              L2 = L2->next;
       }
       return 0;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

נתונה הגדרה הבאה של המבנה:
```c
typedef struct {
        int size;
        int * ptr;
} dyn_array;
```
המייצג מערך דינאמי של מספרים שלמים, כאשר `size` הוא גודל המערך ו-`ptr` הוא מצביע לתחילת המערך.

כתבו פונקציה עם החתימה `dyn_array * divNumbers(int * A, int sz, int n)` אשר מקבלת מערך `A` של מספרים שלמים עם גודלו `sz` וגם מספר שלם חיובי `n`, אשר מחשבת ומוצאת ב-`A` את כל המספרים המתחלקים ללא שארית ב-`2,3,4,…n`.
על הפונקציה ליצור מערך דינאמי `B` עם `n-1` איברים מטיפוס `dyn_aray` כך ששדה `ptr` של `B[0]` יצביע למערך של איברי `A` המתחלקים ב-2, שדה `ptr` של `B[1]` יצביע למערך של איברי `A` המתחלקים ב-3, וכן הלאה. שדה `ptr` של `B[n-2]` יצביע למערך של איברי `A` המתחלקים ב-`n`. אם אף איבר של `A` לא מתחלק ב-`i` (`2≤i≤n`), שדות `size` ו-`ptr` של `B[i-2]` יהיו שווים ל-0 ול-`NULL` בהתאמה.
הפונקציה תחזיר את הכתובת של תחילת המערך `B`.

**דוגמא:** עבור `A={15, 49, -8, 6, -25, 9, 10, -58, 1, 77}` ו-`n=5` הפונקציה תיצור את המערך הבא (באיור: `B[0]` בגודל 4 ומצביע ל-`-8, 6, 10, -58`; `B[1]` בגודל 3 ומצביע ל-`15, 6, 9`; `B[2]` בגודל 1 ומצביע ל-`-8`; `B[3]` בגודל 3 ומצביע ל-`15, -25, 10`).

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
dyn_array* divNumbers(int* A, int sz, int n)
{
       int i, j, k;
       dyn_array* B = (dyn_array*)calloc(n - 1, sizeof(dyn_array)); //array of structs
       for (i = 2; i <= n; i++)
       {
              k = 0;
              B[i - 2].ptr = (int*)calloc(sz, sizeof(int)); //maximum: all elements of initial array
              for (j = 0; j < sz; j++)
                     if (A[j] % i == 0)
                            B[i - 2].ptr[k++] = A[j]; //new appropriate element is found
              B[i - 2].ptr = (int*)realloc(B[i - 2].ptr, k * sizeof(int)); //k is real number of appropriate elements
              B[i - 2].size = k;
       }
       return B;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

במשחק ה-boggle נתון לוח שגודלו `n` של אותיות קטנות באנגלית **שונות זו מזו** (ז"א כל אות מופיעה בלוח פעם אחת בלבד). על מנת להרכיב את המילה הנתונה - השחקן מחפש בלוח אות התחלתית של המילה, וממנה הוא ממשיך בחיפוש אותיות הבאות של המילה בתאים הסמוכים מימין ומשמאל. המשחק מסתיים כאשר מתקבלת מילת החיפוש או כאשר מימין ומשמאל מהתא הנוכחי נמצאות אותיות לא מתאימות.

לדוגמא, בלוח הבא ניתן להרכיב את המילים `baby`, `byte`, `bag` (איור: הלוח `etybag`):
- המילה `bag`: אות `b` נמצאת בלוח, אות `a` ממוקמת מצד ימין מ-`b`, אות `g` ממוקמת מצד ימין מ-`a`.
- המילה `byte`: אות `b` נמצאת בלוח, אות `y` ממוקמת מצד שמאל מ-`b`, אות `t` ממוקמת מצד שמאל מ-`y`, אות `e` ממוקמת מצד שמאל מ-`t`.
- המילה `baby`: אות `b` נמצאת בלוח, אות `a` ממוקמת מצד ימין מ-`b`, אות `b` ממוקמת מצד שמאל מ-`a`, אות `y` ממוקמת מצד שמאל מ-`b`. **שימו לב** שאותה האות יכולה לשמש כמה פעמים באותה מילה.
- המילה `gat` (דוגמא לחיפוש לא מוצלח): אות `g` נמצאת בלוח, אות `a` ממוקמת מצד שמאל מ-`g`, אות `t` לא נמצאת מימין ולא נמצאת משמאל מ-`a`.

כתבו פונקציה `int boggle(char *file_name, char *word)` אשר מקבלת מחרוזת `file_name` המהווה שם של קובץ טקסט שתוכנו הוא **לוח המשחק** ומחרוזת `word` המהווה את **מילת החיפוש**.
הפונקציה תחזיר 1 אם המילה נמצאת בקובץ בהתאם לכללי המשחק ואחרת 0.

**שימו לב:** אין לקרוא את כל הקובץ לתוך מחרוזת או לתוך מאגר נתונים אחר! יש לבצע את החיפוש ישירות בקובץ.

**רמז:** ניתן להשתמש בפונקציות סטנדרטיות `fseek` ו-`ftell`."""

Q3_SOL = r"""```c
int boggle(char* file_name, char* word)
{
       char c;
       FILE* fptr = fopen(file_name, "r");
       int w = 0;
       if (!fptr) exit(1);
       /* search of the first letter of word */
       while ((c = fgetc(fptr)) != EOF)
              if (c == word[0])
              {
                     w++;
                     break;
              }
       if (w == 0)
       {
              fclose(fptr); return 0;
       }
       /* search of next letters of word */
       while (word[w] != '\0')
       {
              if ((c = fgetc(fptr)) == word[w]) // on right
                     w++;
              else // on left
              {
                     if (c != EOF)
                            fseek(fptr, -1, SEEK_CUR); // back from right
                     if (ftell(fptr) - 2 < 0) // left border
                     {
                            fclose(fptr); return 0;
                     }
                     // 2 positions back: itself, left
                     fseek(fptr, -2, SEEK_CUR);
                     if (fgetc(fptr) == word[w])
                            w++;
                     else
                     {
                            fclose(fptr); return 0;
                     }
              }
       }
       fclose(fptr);
       return 1;
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void swap(int* a, int b)
{
    int temp;
    temp = *a;
    *a = b;
    b = temp;
}
int blabla(int* p1, int* p2)
{
    int y = 300, x = 1;
    *p2 = 400;
    x = x + 300;
    return (*p1 + 200);
}
int main()
{
    int x, y = 100;
    x = 200;
    y = blabla(&x, &y);
    printf("%d %d\n", x, y);
    x = y;
    y = 300;
    swap(&x, y);
    printf("%d %d\n", x, y);
    y = 200;
    x = blabla(&y, &x);
    printf("%d %d\n", x, y);
    x = 500;
    printf("%d\n", blabla(&x, &x));
    return 0;
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
200 400
300 300
400 200
600
```
(הפלט הרשמי מופיע ללא פירוט נימוק בקובץ הפתרון; הערכים נבדקו בהרצה.)"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + r"""נתונה התוכנית הבאה:
```c
#include <malloc.h>
void main()
{
    int a[5], ** p = (int **)malloc(sizeof(int*));
         //מניחים שיש מקום להקצאה
    *p = a;
    free(*p);
}
```
מה יקרה עקב ביצוע פונקציית `free`?"""
Q5A_OPTS = opts("ישתחרר מערך `a`",
                "ישתחרר איבר מס' 0 של מערך `a`",
                "ישתחרר זיכרון בו נמצא מצביע למערך `a`",
                "שגיאת ריצה",
                "אף תשובה אינה נכונה")
Q5A_EXPL = "`*p` זה פוינטר עליו מצביע פוינטר `p`. הפוינטר שווה ל-`a`, ז\"א מצביע למערך `a`. לכן מנסים פה לשחרר מערך `a` אבל הוא סטטי ואסור לשחרר אותו. מהסיבה הזו תהיה שגיאת ריצה."

Q5B_TEXT = Q5_INTRO + r"""בחרו מהו ערך של הביטוי `3 ^ 2`"""
Q5B_OPTS = opts("0", "1", "2", "3", "8", "אף תשובה אינה נכונה")
Q5B_EXPL = "`2` בבינארי הוא `000…10`, `3` הוא `000…11`. פעולת XOR נותנת `000…01`, כלומר 1."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** בהינתן קובץ הטקסט `file.dat` (שנפתח בהצלחה) בעל התוכן `1234` מהו הפלט למסך של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
    char st[2];
    FILE* fptr = fopen("file.dat", "r");
    if (!fptr) return;
    while (fgets(st, 2, fptr))
        fputs(fgets(st, 2, fptr),stdout);
    fclose(fptr);
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `24`

**נימוק:**
הפונקציה `fgets` קולטת 2 תווים כולל תו אפסי, ז"א רק תו אחד מהקובץ ומחזירה מחרוזת שנקלטה (המורכבת מתו אחד).
איטרציה ראשונה. בקריאה הראשונה `fgets` קולטת ומחזירה `"1"`. הקלט מוצלח. בקריאה השנייה `fgets` קולטת ומחזירה `"2"`. הפונקציה `fputs` מציגה את המחרוזת במסך (כי הקובץ הוא `stdout`).
איטרציה שנייה. בקריאה הראשונה `fgets` קולטת ומחזירה `"3"`. הקלט מוצלח. בקריאה השנייה `fgets` קולטת ומחזירה `"4"`. הפונקציה `fputs` מציגה את המחרוזת במסך.
תחילת איטרציה שלישית. אנו בסוף הקובץ. לכן הקלט לא מוצלח, `fgets` מחזירה `NULL` והלולאה מסתיימת.
`24`"""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/24B-A-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40, image="images/exams/24B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40, image="images/exams/24B-A-Q3.png"),
    Q(4, "code", "pointers", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "dynamic_memory", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "d", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "b", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "files", Q6_TEXT, Q6_SOL, points=10),
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


# Q1 -- numListCmp (steps follow the second version, numListCmp_2)
F1 = func_lines(Q1_SOL, "int numListCmp_2")
B1 = ["Item* ptr1 = L1, * ptr2 = L2;",
      "while (ptr1 && ptr2) { ptr1 = ptr1->next; ptr2 = ptr2->next; }",
      "if (!ptr1 && ptr2) return -1; else if (ptr1 && !ptr2) return 1;",
      "while (L1) { if (L1->digit < L2->digit) return -1; else if (L1->digit > L2->digit) return 1; L1 = L1->next; L2 = L2->next; }",
      "return 0;"]
f1, j1 = blank(F1, "if (!ptr1 && ptr2)")
b1, i1 = swap(F1, "if (L1->digit < L2->digit)", "if (L1->digit <= L2->digit)")
add(1,
    rubric=rub(("השוואת האורכים של הרשימות בלי המרה למספר: מעבר מקביל על שתי הרשימות, והרשימה הארוכה יותר מייצגת מספר גדול יותר", 14),
               ("עבור רשימות באותו אורך: מעבר מקביל והשוואת ספרה מול ספרה מהמשמעותית ביותר, עד ההבדל הראשון", 14),
               ("החזרת `-1`, `1` או `0` בהתאם לתוצאת ההשוואה, כולל `0` כשכל הספרות שוות", 6),
               ("עבודה ישירה על הרשימות בלי שינוי שלהן ובלי גישה ל-`NULL`", 6)),
    rubricSource="ai-draft",
    pitfalls=["להשוות ספרה מול ספרה בלי לבדוק קודם את האורכים, ולהחליט לפי הספרה הראשונה: `9,9,9,9` מול `1,0,0,0,0` נותן `1` במקום `-1`.",
              "לעצור בהבדל הראשון בספרות ולהחזיר תשובה גם כשהרשימות באורכים שונים, או להמשיך לעבור על רשימה שהסתיימה ולגשת ל-`NULL`.",
              "להמיר את הרשימות למספרים (חריגה מהדרישה, ובנוסף גלישה במספרים ארוכים)."],
    steps=[
        {"type": "numeric",
         "prompt": "מה מחזירה `numListCmp` עבור `L1: 9,9,9,9` ו-`L2: 1,0,0,0,0`?",
         "answer": -1, "tol": 0,
         "explain": "ל-`L2` יש יותר ספרות, ולכן המספר שלה גדול יותר ו-`L1` קטנה (ריצה אמיתית: -1)."},
        {"type": "numeric",
         "prompt": "מה מחזירה `numListCmp` עבור `L1: 5,3,7,0,1` ו-`L2: 5,3,6,8,7` (שתי הרשימות באורך 5)?",
         "answer": 1, "tol": 0,
         "explain": "האורכים שווים, והספרות הראשונות שונות בספרה השלישית: 7 > 6, ולכן `L1` גדולה יותר (ריצה אמיתית: 1)."},
        {"type": "fillblank", "prompt": "השלימו את התנאי שמחזיר `-1` אחרי השוואת האורכים.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": T("if (!ptr1 && ptr2)", "if (ptr1 && !ptr2)", "if (!ptr1 || ptr2)", "if (!ptr1)"),
         "correctId": "a",
         "explain": "`L1` קצרה מ-`L2` כש-`ptr1` הסתיים (`NULL`) ו-`ptr2` עדיין לא. ב' מחליף בין התפקידים, וג' ו-ד' מחזירים `-1` גם כשהאורכים שווים (ריצה אמיתית: תוצאות שגויות על הדוגמאות)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `numListCmp_2` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "קודם הצבת הסמנים, אחר כך התקדמות עד סוף אחת הרשימות, אחר כך החלטה לפי האורך, ורק אז השוואת הספרות ברשימות באורך שווה; `return 0` רק בסוף. כל החלפה של שני בלוקים נכשלת בבנייה או נותנת תוצאה שגויה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ו-`numListCmp_2` מחזירה `-1` כבר כשהספרה הראשונה שווה (למשל עבור `5,3,7,0,1` מול `5,3,6,8,7`). מצאו את השורה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "`<=` במקום `<` מחזיר `-1` גם כשהספרות שוות, ולכן הלולאה נעצרת בספרה הראשונה (ריצה אמיתית: -1 במקום 1)."},
    ],
    stepsSource="ai-draft")

# Q2 -- divNumbers
F2 = func_lines(Q2_SOL, "dyn_array* divNumbers")
B2 = ["k = 0; B[i - 2].ptr = (int*)calloc(sz, sizeof(int));",
      "for (j = 0; j < sz; j++) if (A[j] % i == 0) B[i - 2].ptr[k++] = A[j];",
      "B[i - 2].ptr = (int*)realloc(B[i - 2].ptr, k * sizeof(int)); B[i - 2].size = k;"]
f2, j2 = blank(F2, "if (A[j] % i == 0)")
b2, i2 = swap(F2, "for (j = 0; j < sz; j++)", "for (j = 1; j < sz; j++)")
add(2,
    rubric=rub(("הקצאת מערך `B` של `n-1` מבנים מטיפוס `dyn_array` (שורה `i-2` עבור המחלק `i`)", 8),
               ("לולאה על המחלקים `2..n` ולולאה פנימית על `A` עם בדיקת התחלקות `A[j] % i == 0`", 12),
               ("איסוף האיברים המתחלקים למערך דינמי מתאים: הקצאה בגודל מקסימלי, מילוי, וצמצום ל-`k` עם `realloc`", 12),
               ("עדכון `size` ל-`k` (0 ו-`NULL` כשאין איבר מתחלק) והחזרת `B`", 8)),
    rubricSource="ai-draft",
    pitfalls=["לכתוב `B[i].ptr` במקום `B[i - 2].ptr`: המחלק `i` מתחיל ב-2 והאינדקס ב-0.",
              "לשכוח לעדכן את `size`, או לא לצמצם את המערך לגודל האמיתי, כך שיש בו תאים לא מאותחלים.",
              "לבדוק `i % A[j]` במקום `A[j] % i`, ולחלק באפס כש-`A[j]` שווה 0."],
    steps=[
        {"type": "numeric",
         "prompt": "עבור `A={15, 49, -8, 6, -25, 9, 10, -58, 1, 77}` ו-`n=5`, מה `B[0].size` (האיברים המתחלקים ב-2)?",
         "answer": 4, "tol": 0,
         "explain": "האיברים הם `-8, 6, 10, -58` (ריצה אמיתית: 4)."},
        {"type": "numeric",
         "prompt": "באותה דוגמה, מה `B[3].size` (האיברים המתחלקים ב-5)?",
         "answer": 3, "tol": 0,
         "explain": "האיברים הם `15, -25, 10` (ריצה אמיתית: 3)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הבדיקה בלולאה הפנימית.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": T("if (A[j] % i == 0)", "if (A[j] / i == 0)", "if (A[j] % i != 0)", "if (i % A[j] == 0)"),
         "correctId": "a",
         "explain": "מספר מתחלק ב-`i` ללא שארית כש-`A[j] % i == 0`. ג' בוחר את האיברים שאינם מתחלקים, וב' ו-ד' בוחרים איברים אחרים לגמרי (ריצה אמיתית: גדלים שונים מ-4, 3, 1, 3)."},
        {"type": "order", "prompt": "סדרו את שלוש הפקודות שבגוף הלולאה החיצונית `for (i = 2; i <= n; i++)`.", "code": True, "lines": B2,
         "explain": "קודם הקצאת המערך בגודל מקסימלי, אחר כך מילויו, ולבסוף צמצום והגדרת `size`. כל החלפה כותבת למצביע שעדיין לא הוקצה או מצמצמת מערך לפני המילוי (ריצה אמיתית: קריסה או תוצאה שונה בכל החלפה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ובכל המערכים `B[i]` חסר האיבר הראשון של `A` אם הוא מתחלק (`15` חסר ב-`B[1]` וב-`B[3]`). מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "הלולאה מתחילה מ-`j = 1` ומדלגת על `A[0]` (ריצה אמיתית: `B[1]` הוא `6, 9` במקום `15, 6, 9`)."},
    ],
    stepsSource="ai-draft")

# Q3 -- boggle
F3 = func_lines(Q3_SOL, "int boggle")
B3 = ["char c; FILE* fptr = fopen(file_name, \"r\"); int w = 0; if (!fptr) exit(1);",
      "while ((c = fgetc(fptr)) != EOF) if (c == word[0]) { w++; break; } if (w == 0) { fclose(fptr); return 0; }",
      "while (word[w] != '\\0') { if ((c = fgetc(fptr)) == word[w]) w++; else { if (c != EOF) fseek(fptr, -1, SEEK_CUR); if (ftell(fptr) - 2 < 0) { fclose(fptr); return 0; } fseek(fptr, -2, SEEK_CUR); if (fgetc(fptr) == word[w]) w++; else { fclose(fptr); return 0; } } }",
      "fclose(fptr); return 1;"]
f3, j3 = blank(F3, "fseek(fptr, -2, SEEK_CUR);")
b3, i3 = swap(F3, "if (ftell(fptr) - 2 < 0)", "if (ftell(fptr) - 2 <= 0)")
add(3,
    rubric=rub(("פתיחת הקובץ לקריאה וסגירתו בכל מסלול יציאה", 4),
               ("חיפוש האות הראשונה של המילה בקובץ בקריאה תו אחר תו, והחזרת 0 אם היא לא נמצאה", 8),
               ("המשך החיפוש: קריאת התו הבא מימין והשוואה לאות הנוכחית של המילה", 10),
               ("כשהאות אינה מימין: חזרה אחורה עם `fseek` (צעד אחד מהקריאה, ועוד שניים כדי להגיע לתו שמשמאל) ובדיקת התו משמאל", 12),
               ("טיפול בגבולות: התא הראשון בקובץ אין משמאלו תא (בדיקה עם `ftell`), וסוף הקובץ מימין; החזרת 1 כשכל המילה נמצאה", 6)),
    rubricSource="ai-draft",
    pitfalls=["לקרוא את כל הקובץ למחרוזת, בניגוד לדרישה, או לא להשתמש ב-`fseek` ו-`ftell`.",
              "לחזור אחורה בצעד שגוי: אחרי קריאה מימין צריך `-1` כדי לחזור למקום, ועוד `-2` כדי לקרוא את התו שמשמאל לתו הנוכחי (במקום `-1` בלבד).",
              "לא לבדוק את הגבול השמאלי, ולנסות לקרוא לפני תחילת הקובץ."],
    steps=[
        {"type": "choice", "prompt": "הלוח הוא `etybag`. אילו מהמילים `byte`, `baby`, `gat` ניתנות להרכבה?",
         "options": T("`byte` ו-`baby` בלבד", "שלושתן", "`byte` בלבד", "`baby` ו-`gat` בלבד"), "correctId": "a",
         "explain": "ריצה אמיתית של הפונקציה: `byte` ו-`baby` מחזירות 1, ו-`gat` מחזירה 0 (אחרי `g`, `a` משמאל, אין `t` לא מימין ולא משמאל של `a`)."},
        {"type": "numeric",
         "prompt": "בחיפוש המילה `bag` בלוח `etybag`: מה ערך `ftell(fptr)` מיד אחרי שהלולאה הראשונה מצאה את האות `b`?",
         "answer": 4, "tol": 0,
         "explain": "האות `b` נמצאת במקום 3 (מתחילים מ-0), ו-`fgetc` כבר קדמה את המיקום ל-4 (ריצה אמיתית: 4)."},
        {"type": "fillblank", "prompt": "השלימו את החזרה אחורה אל התו שמשמאל לתו הנוכחי (לפני כן כבר בוצעה חזרה של צעד אחד).", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": T("fseek(fptr, -2, SEEK_CUR);", "fseek(fptr, -1, SEEK_CUR);", "fseek(fptr, -3, SEEK_CUR);", "fseek(fptr, 0, SEEK_CUR);"),
         "correctId": "a",
         "explain": "אחרי החזרה של צעד אחד המיקום הוא מיד אחרי התו הנוכחי; כדי לקרוא את התו שמשמאל לו צריך לחזור עוד שני מקומות. ב' קורא את התו הנוכחי, ג' קורא תו רחוק מדי וד' קורא את התו מימין (ריצה אמיתית: `byte` מחזירה 0 בכל אחת מהן)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `boggle` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3,
         "explain": "הצהרות ופתיחה, חיפוש האות הראשונה (והחזרת 0 אם לא נמצאה), חיפוש שאר האותיות ואז סגירה והחזרת 1. כל החלפה של שני בלוקים נכשלת בבנייה או נותנת תוצאה שגויה על המילים בדוגמה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והמילה `yte` בלוח `etybag` (שמשתמשת בתא הראשון בקובץ) כבר לא נמצאת. מצאו את השורה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`<= 0` פוסל גם מצב שבו מיקום 0 עדיין נגיש (התו הראשון בקובץ), ולכן `yte` מחזירה 0 במקום 1 (ריצה אמיתית). הבדיקה הנכונה היא `< 0`."},
    ],
    stepsSource="ai-draft")

# Q4 -- pointers output (values from running q4.c)
Q4_OUT = ["200 400", "300 300", "400 200", "600"]
add(4,
    rubric=rub(("בקריאה הראשונה `p2` מצביע על `y` של `main`: `*p2 = 400` משנה אותו, וההחזרה היא `*p1 + 200 = 400`, ולכן `200 400`", 3),
               ("`swap(&x, y)` משנה את `x` ל-300 (הפרמטר `b` הוא עותק), ולכן `300 300`", 2),
               ("`blabla(&y, &x)`: `*p2 = 400` קובע את `x` ל-400, ההחזרה היא `*p1 + 200 = 400` ונשמרת ב-`x`, ולכן `400 200`", 2),
               ("`blabla(&x, &x)`: שני המצביעים מצביעים על אותו משתנה, `*p2 = 400` ואז `*p1 + 200 = 600`", 3)),
    rubricSource="ai-draft",
    pitfalls=["לבלבל בין המשתנים המקומיים `x`,`y` של `blabla` לבין המשתנים של `main`: ההשמות המקומיות אינן משפיעות על `main`.",
              "לחשוב ש-`swap` מחליפה את `x` ו-`y`: `b` הוא עותק, ולכן רק `*a` משתנה.",
              "לחשב `500 + 200 = 700` בקריאה האחרונה ולשכוח ש-`*p2 = 400` דורס את `x` לפני שהוא נקרא דרך `p1`."],
    steps=[
        {"type": "numeric",
         "prompt": "אחרי `y = blabla(&x, &y);` (עם `x = 200`, `y = 100` לפני הקריאה), מה ערך `y`?",
         "answer": 400, "tol": 0,
         "explain": "`*p2 = 400` מציב 400 ב-`y`, ו-`*p1 + 200` נותן 400, שגם נשמר ב-`y` (ריצה אמיתית: השורה `200 400`)."},
        {"type": "numeric",
         "prompt": "אחרי `x = y; y = 300; swap(&x, y);` מה ערך `x`?",
         "answer": 300, "tol": 0,
         "explain": "`*a = b` מציבה ב-`x` את הערך 300 (ריצה אמיתית: השורה `300 300`)."},
        {"type": "numeric",
         "prompt": "מה מדפיסה השורה האחרונה: `printf(\"%d\\n\", blabla(&x, &x))` כאשר `x = 500`?",
         "answer": 600, "tol": 0,
         "explain": "שני המצביעים מצביעים על `x`: `*p2 = 400`, ואז `*p1 + 200 = 600` (ריצה אמיתית: 600)."},
        {"type": "order", "prompt": "סדרו את ארבע שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True, "lines": Q4_OUT,
         "explain": "ריצה אמיתית: אותן ארבע שורות."},
    ],
    stepsSource="ai-draft")

# Q6 -- bonus: fgets(st, 2, f) reads one character; the file is 1234
add(6,
    rubric=rub(("`fgets(st, 2, fptr)` קוראת תו אחד בלבד (מקום אחד למחרוזת ועוד תו סיום)", 3),
               ("בכל איטרציה הקריאה בתנאי הלולאה צורכת תו אחד והקריאה בתוך `fputs` תו נוסף שמודפס", 4),
               ("בסוף הקובץ `fgets` מחזירה `NULL` והלולאה נעצרת, והפלט הסופי `24`", 3)),
    rubricSource="ai-draft",
    pitfalls=["לחשוב ש-`fgets` עם גודל 2 קוראת שני תווים, ולהדפיס `12` או `1234`.",
              "לשכוח שהקריאה בתנאי הלולאה צורכת תו שלא מודפס, ולהדפיס `1234`."],
    steps=[
        {"type": "numeric",
         "prompt": "כמה תווים מהקובץ קולטת הקריאה `fgets(st, 2, fptr)`?",
         "answer": 1, "tol": 0,
         "explain": "הפרמטר 2 כולל את תו הסיום, ולכן נקלט תו אחד (ריצה אמיתית: `st` מכיל תו אחד בכל קריאה)."},
        {"type": "numeric",
         "prompt": "כמה איטרציות מבצעת הלולאה על הקובץ `1234`?",
         "answer": 2, "tol": 0,
         "explain": "כל איטרציה צורכת שני תווים (אחד בתנאי ואחד ב-`fputs`), ובשלישית `fgets` מחזירה `NULL` (ריצה אמיתית: 2 איטרציות)."},
        {"type": "text", "prompt": "מה הפלט של התוכנית? (רצף ספרות, ללא רווחים)",
         "accept": ["24"], "normalize": "none",
         "explain": "מודפסים התווים השני והרביעי (ריצה אמיתית: `24`)."},
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "24B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ד, מועד א'",
    "year": 2024,
    "examDate": "08.07.2024",
    "sourceFile": "24B-A exam",
    "solutionFile": "24B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
