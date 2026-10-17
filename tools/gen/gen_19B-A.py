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
```"""

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
