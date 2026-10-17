# -*- coding: utf-8 -*-
"""Generator for tools/raw/19B-B.json -- programming-workshop (C), semester B 2019, moed B (14.08.19).
Q1, Q2, Q3 (28 pts each, all required), Q4 (16 pts, four pick-and-justify items), Q5 bonus (10 pts).
Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/19B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_19B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזות `infile` ו-`outfile` המהוות שמות של שני קבצי טקסט.
קובץ `infile` מורכב משורות טקסט.

על הפונקציה להעתיק את התוכן של קובץ `infile` לקובץ `outfile` ולהוסיף מספר ביקורת ותו ביקורת בסוף כל שורה באופן הבא:
מספר הביקורת יהיה מספר ששווה לסכום קודי ASCII של כל תווי השורה;
תו הביקורת יהיה תו שקוד ASCII שלו הוא שארית החלוקה של מספר הביקורת ב-128;
בחישוב מספר הביקורת ותו הביקורת נא **לא להתחשב** בתו של סוף השורה;
יש להכניס רווח בין התו האחרון של השורה המקורית למספר הביקורת, וצמוד למספר הביקורת לכתוב את תו הביקורת.

תו של סוף השורה אמור להופיע גם בסוף של **השורה האחרונה** בקובץ `infile` ובקובץ `outfile`.

**דוגמא:**
`infile`:
```
abc
3+2+1=6
A
```
`outfile`:
```
abc 294&
3+2+1=6 351_
A 65A
```
**הסבר:**
שורה ראשונה. קודי ASCII של 'a', 'b', 'c' הם 97, 98, 99 בהתאמה. 294=97+98+99, 294%128=38. 38 הוא קוד ה-ASCII של '&'.
שורה שנייה. סכום קודי ASCII של כל תווי השורה (ספרות ותווים לפעולות אריתמטיות) הוא 351. 351%128=95. 95 הוא קוד ה-ASCII של '_'.
שורה שלישית. קוד ה-ASCII של 'A' שהוא התו היחיד בשורה שווה ל-65. 65%128=65."""

Q1_SOL = r"""```c
void add_controls_in_file_rows (char *infile, char *outfile)
{
      int sum=0;
      char c;
      FILE *in = fopen(infile, "r"),
             *out = fopen(outfile, "w");
      if( !in || !out )
            exit(1);
      while ( (c = fgetc(in)) != EOF )
            if (c != '\n')
            {
                  fputc(c, out);
                  sum += c;
            }
            else
            {
                  fprintf(out, " %d%c\n", sum, sum%128);
                  sum = 0;
            }
      fclose(in);
      fclose(out);
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרת הטיפוס הבאה:
```c
typedef struct item {
  char *string;
  struct item *next;
} Item;
```
כתוב פונקציית `void` אשר מקבלת מערך מחרוזות `S` עם גודלו, וגם רשימה מקושרת `L` של מחרוזות המורכבת מאיברים מסוג `Item`.
שדה ה-`string` של כל איבר (חוליה) ב-`L` מצביע למחרוזת דינאמית.
כל המחרוזות של `L` הן שונות וממוינות בסדר לקסיקוגרפי (מילולי) עולה כך שמחרוזת באיבר מס' `i` מתחילת הרשימה גדולה לקסיקוגרפית ממחרוזת באיבר מס' `i-1`.

על הפונקציה להכניס ל-`L` את כל המחרוזות של `S` אשר **עוד לא נמצאות** ב-`L` (יש להקצות מקום גם לאיברים החדשים וגם למחרוזות). האיברים יוכנסו במקומות הנכונים כך שהמחרוזות ב-`L` יהיו ממוינות גם אחרי ההכנסתם.

אין ב-`L` איבר דמה. לכן המצביע לאיבר הראשון של הרשימה יכול להשתנות אחרי ההכנסות. מסיבה זו יש להעביר את המצביע by reference.

ניתן להניח שיש בזיכרון מספיק מקום להקצאות."""

Q2_SOL = r"""```c
void insert_string_in_sort_list (char* str, Item **plist)
{
    Item *curr_point = *plist, *prev_point, *temp;

      //search place for insert into sorting list
      while ( curr_point && strcmp(str, curr_point->string)==1 )
      {
            prev_point = curr_point;
            curr_point = curr_point->next;
      }

      //check whether string is already in list
      if ( curr_point && strcmp(str, curr_point->string)==0 )
            return;

      //allocation place for new item and string
      temp = (Item *)malloc(sizeof(Item));
      temp->string = (char *)malloc(strlen(str)+1);
      strcpy(temp->string, str);

      if (curr_point != *plist) // inserting in the middle or in the end
      {
            temp->next = curr_point;
            prev_point->next = temp;
      }
      else  // inserting before first item
      {
            temp->next = *plist;
            *plist = temp;
      }
}

void insert_strings_from_array_in_sort_list (char** str, int n, Item
**plist)
{
      int i;
      for (i=0; i<n; i++)
            insert_string_in_sort_list (str[i], plist);
}
```

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הבדיקה `strcmp(...)==1` מניחה ש-`strcmp` מחזירה בדיוק 1 או -1. בהרצה עם clang (`tools/verify/19B-B/q2.c`) זה מתקיים והדוגמה של המבחן מתקבלת נכון; בספריות שבהן `strcmp` מחזירה הפרש בין תווים הבדיקה לא תעבוד."""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה אשר מקבלת מערך `A` של מספרים שלמים.

על הפונקציה ליצור מערך דו-ממדי דינאמי `B` בו מספר השורות יהיה שווה למספר הרצפים של מספרים זוגיים ושל מספרים אי-זוגיים ב-`A`. שורה מס' `i` ב-`B` תהיה זהה (אותם איברים באותו סדר) לרצף מס' `i` ב-`A` (כאשר הרצפים ב-`A` ממוספרים החל מ-0).

הפונקציה תחזיר את הכתובת של מערך `B` ותעביר by reference את מספר השורות בתוכו. בנוסף הפונקציה תעביר by reference מערך דינאמי `S` המורכב מגדלי השורות של מערך `B`. איבר מס' `i` של מערך `S` יהיה שווה לגודל שורה מס' `i` של `B`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאות.

**דוגמא:**
`A` (משמאל לימין):
```
3 7 20 12 6 9 13 1 2 7 55 31 9
```
`B`:
```
3 7
20 12 6
9 13 1
2
7 55 31 9
```
`S`:
```
2
3
3
1
4
```
הפונקציה גם תעביר by reference 5 כמספר השורות במערך `B`."""

Q3_SOL = r"""```c
int **array_to_array_of_sequences (int *A, int n, int **S, int *prows)
{
      int i, j=0, k, **B;
      *prows = 0;
      *S = (int *)calloc(n, sizeof(int));
      (*S)[0] = 1;
      for (i=1; i<n; i++)
            if (A[i]%2 == A[i-1]%2) //the same sequence
                  (*S)[j]++;
            else //new sequence
            {
                  j++;
                  (*S)[j] = 1;
            }
            *prows = j+1;

      B = (int **)calloc(*prows, sizeof(int *));

      i=j=0;
      while (i<n)
      {
            B[j] = (int *)calloc((*S)[j], sizeof(int));
            for (k=0; k<(*S)[j]; k++)
                  B[j][k] = A[i++];
            j++;
      }
      *S = (int *)realloc(*S, *prows*sizeof(int));
      return B;
}
```"""

# ---------------------------------------------------------------- Q4 (16 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 16 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + "איזה סוג של מצביע **לא מוגדר** בשפת C?"
Q4A_OPTS = opts("מצביע לפונקציה", "מצביע לקובץ", "מצביע למצביע", "מצביע לסיבית", "מצביע להכל",
                "כל הסוגים לעיל מוגדרים")
Q4A_EXPL = "לפי כללי שפת C."

Q4B_TEXT = Q4_INTRO + "מהי כמות הזיכרון שצריך מבנה כלשהו?"
Q4B_OPTS = opts("היא שווה לסך הזיכרון שדורשים כל השדות שלו",
                "היא גדולה או שווה לסך הזיכרון שדורשים כל השדות שלו",
                "היא שווה לגודל מקסימלי בין גדלים של כל השדות שלו",
                "אף תשובה אינה נכונה")
Q4B_EXPL = "סוגים בסיסיים של הנתונים מאוחסנים בכתובות שהן כפולות של הגדלים שלהם. לכן בין שדות של מבנה יכולים להיות פערים."

Q4C_TEXT = Q4_INTRO + r"""נתונה התוכנית הבאה:
```c
#include <stdio.h>

int x;
void main()
{
     x++;
     printf("%d",x);
}
```
מהי הטענה הנכונה?"""
Q4C_OPTS = opts("התכנית שגויה כי `x` לא מאותחל",
                "התכנית שגויה כי אסור להצהיר על משתנה מעל פונקציות",
                "התכנית שגויה משתי הסיבות לעיל",
                "התכנית תקינה",
                "התכנית תקינה אבל לא מומלץ להשתמש בסגנון ללא סיבה מוצדקת",
                "אף טענה אינה נכונה")
Q4C_EXPL = "`x` הוא משתנה גלובלי (לא מומלץ להשתמש) וברירת המחדל ערך התחלתי שלו הוא 0."

Q4D_TEXT = Q4_INTRO + r"""נתונה התוכנית הבאה:
```c
#include <stdio.h>

int size (double arr[])
{
     return sizeof(arr);
}

void main()
{
     double arr[10];
     printf ("%d\n", size(arr));
}
```
מהו פלט התוכנית?"""
Q4D_OPTS = opts("`4`", "`8`", "`10`", "`80`", "אף תשובה אינה נכונה")
Q4D_EXPL = ("כי `arr` הוא מצביע וגודל של מצביע שווה ל-4.\n\n"
            "**הערת מתמלל (לא חלק מהפתרון הרשמי):** התשובה מניחה מערכת של 32 סיביות. בהרצה אמיתית "
            "(`tools/verify/19B-B/q4.c`) הקומפילציה ל-32 סיביות מדפיסה `4`, ואילו ל-64 סיביות `8`.")

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
     char *s="ab";
     printf("%d\n",sizeof s[0]+sizeof s[1]-sizeof'a'-sizeof'b');
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
-6
```
**נימוק:**
גודל של משתנה מסוג `char` הוא 1. תו קבוע הוא פשוט ייצוג של מספר שלם בקוד ASCII שלו וגודל של קבוע שלם הוא 4. לכן `1+1-4-4=-6`."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=28),
    Q(2, "code", "list_manipulation", Q2_TEXT, Q2_SOL, points=28, image="images/exams/19B-B-Q2.png"),
    Q(3, "code", "dynamic_arrays_2d", Q3_TEXT, Q3_SOL, points=28),
    M("א", "pointers", Q4A_TEXT, Q4A_OPTS, "d", Q4A_EXPL),
    M("ב", "structs_unions", Q4B_TEXT, Q4B_OPTS, "b", Q4B_EXPL),
    M("ג", "storage_classes", Q4C_TEXT, Q4C_OPTS, "e", Q4C_EXPL),
    M("ד", "pointers", Q4D_TEXT, Q4D_OPTS, "a", Q4D_EXPL),
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "19B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשע\"ט, מועד ב'",
    "year": 2019,
    "examDate": "14.08.19",
    "sourceFile": "19B-B exam",
    "solutionFile": "19B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
