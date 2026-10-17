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
