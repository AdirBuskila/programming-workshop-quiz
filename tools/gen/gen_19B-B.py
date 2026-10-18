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
```

**הערה:** המשתנה `c` מוגדר כ-`char` ומושווה ל-`EOF` (שהוא `int`). במערכת שבה `char` הוא ללא סימן הלולאה לא נגמרת, ובמערכת עם סימן היא נעצרת מוקדם כשנקרא הבייט `0xFF`. הנכון הוא `int c`."""

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
```

**הערה:** הבדיקה `A[i]%2 == A[i-1]%2` שגויה עבור מספרים אי-זוגיים שליליים, כי `-3%2` הוא `-1` ו-`1%2` הוא `1`, ולכן `{-3, 1, -5, 2}` מפוצל ל-4 רצפים במקום 2. התיקון: `(A[i]&1) == (A[i-1]&1)` (או `abs(A[i]%2)`). בנוסף, כש-`n==0` הפקודה `(*S)[0] = 1` כותבת מעבר לזיכרון שהוקצה, ולכן יש להוסיף בתחילת הפונקציה (אחרי `*prows = 0`) את הבדיקה `if (n==0) { *S = NULL; return NULL; }`. התיקון נבדק בריצה (`tools/verify/19B-B/fix_q3_neg_n0.c`: שתי שורות, `S = 3 1`, ו-`n==0` מחזיר 0 שורות)."""

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
Q4C_EXPL = ("**הערה:** בניסוח המילולי של השאלה גם אפשרות ד' (\"התכנית תקינה\") נכונה מילולית. המפתח הרשמי הוא ה' (תקינה אך לא מומלצת), והוא שיקול סגנוני.\n\n"
             "`x` הוא משתנה גלובלי (לא מומלץ להשתמש) וברירת המחדל ערך התחלתי שלו הוא 0.")

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
            "**הערה:** התשובה תלויה בפלטפורמה ומניחה מערכת של 32 סיביות. בהרצה אמיתית "
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
גודל של משתנה מסוג `char` הוא 1. תו קבוע הוא פשוט ייצוג של מספר שלם בקוד ASCII שלו וגודל של קבוע שלם הוא 4. לכן `1+1-4-4=-6`.

**הערה:** התוצאה `-6` תלויה בפלטפורמה: הביטוי הוא מטיפוס `size_t` (ללא סימן), ולכן `2-4-4` גולש ל-`2^64-6` (ב-64 סיביות), ורק החיתוך של `printf` עם `%d` (התנהגות לא מוגדרת) מדפיס `-6`. בהדפסה עם `%zu` מתקבל `18446744073709551610`."""


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

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run in tools/verify/<CODE>/steps_check.py
# (it compiles the shipped steps and the stored solutions). Lines of order/findbug/fillblank come from the stored solutions.
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


def co(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


# Q1 -- add_controls_in_file_rows
F1 = func_lines(Q1_SOL, "void add_controls_in_file_rows")
B1 = [r'int sum=0; char c; FILE *in = fopen(infile, "r"), *out = fopen(outfile, "w");',
      "if( !in || !out ) exit(1);",
      r'''while ( (c = fgetc(in)) != EOF ) if (c != '\n') { fputc(c, out); sum += c; } else { fprintf(out, " %d%c\n", sum, sum%128); sum = 0; }''',
      "fclose(in); fclose(out);"]
f1, j1 = blank(F1, r'''fprintf(out, " %d%c\n", sum, sum%128);''')
b1, i1 = swap(F1, "sum += c;", "sum = c;")
add(1,
    rubric=rub(("פתיחת `infile` לקריאה ו-`outfile` לכתיבה ובדיקה שהפתיחה הצליחה", 6),
               ("קריאה תו אחר תו עד `EOF` והעתקת כל תו שאינו סוף שורה אל `outfile`", 6),
               ("צבירת סכום קודי ה-ASCII של תווי השורה, בלי תו סוף השורה", 6),
               ("בסוף כל שורה: כתיבת רווח, מספר הביקורת, תו הביקורת (`sum%128`) ותו סוף שורה, ואיפוס הסכום לשורה הבאה", 7),
               ("סגירת שני הקבצים", 3)),
    rubricSource="ai-verified",
    pitfalls=["לא לאפס את הסכום אחרי כל שורה, כך שמספר הביקורת של כל שורה כולל את השורות שלפניה.",
              "לצרף לסכום גם את `'\\n'`, למרות שההוראה היא לא להתחשב בו.",
              "לכתוב את הסכום עצמו כתו הביקורת במקום את `sum%128`, או לשכוח את הרווח שמפריד בין השורה המקורית למספר הביקורת."],
    steps=[
        {"type": "numeric",
         "prompt": "`infile` מכיל את השורה `Hi!` בלבד. מה מספר הביקורת שייכתב אחריה ב-`outfile`?",
         "answer": 210, "tol": 0,
         "explain": "$72 + 105 + 33 = 210$ (קודי `H`, `i`, `!`; ריצה אמיתית: הקובץ מכיל `Hi! 210R`)."},
        {"type": "text",
         "prompt": "באותו קובץ (`Hi!`), מהו תו הביקורת שייכתב אחרי מספר הביקורת? (תו בודד)",
         "accept": ["R"], "normalize": "none",
         "explain": "$210 \\bmod 128 = 82$ וקוד ה-ASCII 82 הוא `R` (ריצה אמיתית: `Hi! 210R`)."},
        {"type": "fillblank", "prompt": "השלימו את שורת הכתיבה לסוף כל שורה (רווח, מספר הביקורת, תו הביקורת, סוף שורה).", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": co(r'''fprintf(out, " %d%c\n", sum, sum%128);''',
                       r'''fprintf(out, "%d%c\n", sum, sum%128);''',
                       r'''fprintf(out, " %d%c\n", sum, sum/128);''',
                       r'''fprintf(out, " %c%d\n", sum%128, sum);'''),
         "correctId": "a",
         "explain": "ב' שוכח את הרווח (`abc294&`), ג' מחשב מנה במקום שארית, ד' מחליף את סדר המספר והתו (ריצה אמיתית: כל אחת מהאפשרויות הללו מייצרת קובץ שונה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ומספר הביקורת בכל שורה שווה לקוד התו האחרון בשורה בלבד. מצאו אותה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "`sum = c;` דורס את הסכום בכל תו במקום להוסיף אליו; בפתרון הנכון `sum += c;` (ריצה אמיתית: אחרי `abc` נכתב `99` במקום `294`)."},
        {"type": "order", "prompt": "סדרו את הפקודות של הפונקציה (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "הצהרות ופתיחה, בדיקת הפתיחה לפני הקריאה, לולאת ההעתקה, ובסוף סגירה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או מייצרת קובץ שונה (נבדק בריצה, כולל קובץ קלט שאינו קיים)."},
    ],
    stepsSource="ai-verified")

# Q2 -- sorted insertion of strings into a linked list
F2 = func_lines(Q2_SOL, "void insert_string_in_sort_list")
f2, j2 = blank(F2, "while ( curr_point && strcmp(str, curr_point->string)==1 )")
b2, i2 = swap(F2, "temp->next = curr_point;", "temp->next = NULL;")
add(2,
    rubric=rub(("חיפוש המקום המתאים ברשימה הממוינת בעזרת `strcmp`, תוך שמירת האיבר הקודם `prev_point`", 7),
               ("זיהוי מחרוזת שכבר נמצאת ברשימה (`strcmp == 0`) וחזרה בלי להוסיף אותה", 5),
               ("הקצאת איבר חדש והקצאת עותק של המחרוזת (`malloc(strlen+1)` ו-`strcpy`)", 6),
               ("קישור האיבר החדש: באמצע או בסוף דרך `prev_point`, ולפני האיבר הראשון עם עדכון `*plist`", 6),
               ("פונקציה שעוברת על מערך המחרוזות וקוראת להכנסה לכל מחרוזת, כשהמצביע לראש מועבר by reference", 4)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את המקרה של הכנסה לפני האיבר הראשון, שבו צריך לעדכן את `*plist` ולא איבר קודם.",
              "לבדוק כפילות רק מול האיבר הראשון ברשימה, או להכניס מחרוזת שכבר קיימת.",
              "לשמור בשדה `string` את המצביע `str` שקיבלנו במקום להקצות עותק חדש."],
    steps=[
        {"type": "numeric",
         "prompt": "הרשימה `L` מכילה `ant`, `cat`, והמערך הוא `S = {\"bee\", \"cat\", \"ant\", \"dog\"}`. כמה איברים יהיו ב-`L` אחרי ההכנסות?",
         "answer": 4, "tol": 0,
         "explain": "`bee` ו-`dog` חדשות, `cat` ו-`ant` כבר קיימות ואינן מוכנסות שוב: ant, bee, cat, dog (ריצה אמיתית: 4 איברים)."},
        {"type": "choice",
         "prompt": "הרשימה `L` מכילה `bee`, `dog`, והמערך הוא `S = {\"cow\", \"ant\"}`. איזו מחרוזת נמצאת באיבר הראשון של `L` אחרי ההכנסות?",
         "options": co("`ant`", "`bee`", "`cow`", "`dog`"), "correctId": "a",
         "explain": "`ant` קטנה מכל המחרוזות ולכן מוכנסת לפני האיבר הראשון, ו-`*plist` מתעדכן (ריצה אמיתית: ant, bee, cow, dog)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הלולאה שמחפשת את מקום ההכנסה.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": co("while ( curr_point && strcmp(str, curr_point->string)==1 )",
                       "while ( curr_point && strcmp(str, curr_point->string)==-1 )",
                       "while ( strcmp(str, curr_point->string)==1 )",
                       "while ( curr_point && strcmp(str, curr_point->string)>=0 )"),
         "correctId": "a",
         "explain": "ב' מתקדם בכיוון ההפוך ומכניס במקום שגוי, ג' קורס כשמכניסים מחרוזת שגדולה מכולן (`curr_point` הוא `NULL`), ו-ד' ממשיך גם על מחרוזת זהה ולכן לא מזהה כפילויות (ריצה אמיתית: כל אחת מהאפשרויות הללו נכשלת)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ואחרי הכנסה של מחרוזת באמצע הרשימה כל האיברים שאחריה אובדים. מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "האיבר החדש חייב להצביע על `curr_point`, האיבר הבא ברשימה. עם `NULL` הזנב נחתך (ריצה אמיתית: אחרי הכנסת `bee` בין `ant` ל-`cat` נשארים רק `ant`, `bee`)."},
    ],
    stepsSource="ai-verified")

# Q3 -- array_to_array_of_sequences
F3 = func_lines(Q3_SOL, "int **array_to_array_of_sequences")
B3 = ["int i, j=0, k, **B; *prows = 0; *S = (int *)calloc(n, sizeof(int)); (*S)[0] = 1;",
      "for (i=1; i<n; i++) if (A[i]%2 == A[i-1]%2) (*S)[j]++; else { j++; (*S)[j] = 1; }",
      "*prows = j+1; B = (int **)calloc(*prows, sizeof(int *));",
      "i=j=0; while (i<n) { B[j] = (int *)calloc((*S)[j], sizeof(int)); for (k=0; k<(*S)[j]; k++) B[j][k] = A[i++]; j++; }",
      "*S = (int *)realloc(*S, *prows*sizeof(int)); return B;"]
f3, j3 = blank(F3, "if (A[i]%2 == A[i-1]%2)")
b3, i3 = swap(F3, "B[j][k] = A[i++];", "B[j][k] = A[i];")
add(3,
    rubric=rub(("חישוב גדלי הרצפים: מעבר על `A` והשוואת הזוגיות של כל איבר לקודמו, בניית `S`", 8),
               ("קביעת מספר השורות `*prows` כמספר הרצפים", 4),
               ("הקצאת מערך המצביעים `B` והקצאת שורה `i` בגודל `S[i]`", 8),
               ("העתקת איברי כל רצף של `A` לשורה שלו, תוך התקדמות ב-`A` בכל איבר", 5),
               ("החזרת `B` והעברת `S` ו-`*prows` by reference", 3)),
    rubricSource="ai-verified",
    pitfalls=["להשוות את `A[i]` ל-`A[i-1]` עצמם ולא את הזוגיות שלהם (`%2`), ולקבל רצפים של איברים שווים בלבד.",
              "לשכוח שיש רצף אחד לפחות, ולהתחיל את הספירה של `S[0]` מ-0 במקום מ-1.",
              "להקצות את `B` לפני שידוע מספר הרצפים, או להקצות כל שורה בגודל `n` במקום בגודל הרצף."],
    steps=[
        {"type": "numeric",
         "prompt": "המערך הוא `A = {2, 4, 6, 1, 3, 8, 10, 5}`. כמה רצפים (שורות ב-`B`) יש בו?",
         "answer": 4, "tol": 0,
         "explain": "`2 4 6`, `1 3`, `8 10`, `5`: ארבעה רצפים (ריצה אמיתית: `*prows` הוא 4)."},
        {"type": "numeric",
         "prompt": "עבור אותו מערך, מה ערכו של `S[0]`, גודל השורה הראשונה?",
         "answer": 3, "tol": 0,
         "explain": "השורה הראשונה היא `2 4 6`; ריצה אמיתית: `S` הוא `3 2 2 1`."},
        {"type": "fillblank", "prompt": "השלימו את התנאי שבודק אם `A[i]` ממשיך את הרצף של `A[i-1]`.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": co("if (A[i]%2 == A[i-1]%2)", "if (A[i] == A[i-1])", "if (A[i]%2 != A[i-1]%2)", "if (A[i]%2 == 0)"),
         "correctId": "a",
         "explain": "ממשיכים רצף כשהזוגיות זהה. ב' בודק שוויון של הערכים, ג' הפוך, ד' בודק רק זוגיות של האיבר הנוכחי (ריצה אמיתית: כל אחת מהאפשרויות הללו מחלקת את המערך לרצפים אחרים)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והפונקציה אינה מסתיימת (לולאה אינסופית) כשמעתיקים את הרצפים. מצאו אותה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "בלי `i++` האינדקס ב-`A` לא מתקדם, ולכן `i<n` נשאר נכון לתמיד והלולאה החיצונית אינה נגמרת (ריצה אמיתית: התוכנית נתקעת)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של הפונקציה.", "code": True, "lines": B3,
         "explain": "קודם הצהרות ואתחול `S`, אחר כך חישוב הגדלים, אחר כך קביעת `*prows` והקצאת `B` (אחרי שהמספר ידוע), העתקת הרצפים והחזרה. כל החלפה של שני בלוקים קורסת, נכשלת בבנייה או נותנת פלט שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-verified")

# Q5 (bonus) -- sizes inside sizeof expressions
add(5,
    rubric=rub(("זיהוי ש-`s[0]` ו-`s[1]` הם `char` ולכן הגודל של כל אחד מהם הוא 1", 3),
               ("זיהוי שקבוע תו כמו `'a'` הוא מטיפוס `int` בשפת C, ולכן הגודל שלו הוא 4", 4),
               ("חישוב $1+1-4-4=-6$", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב שגם `sizeof 'a'` שווה ל-1 כי התו הוא `char`, ולקבל 0 במקום `-6`.",
              "להתבלבל בין `sizeof s[0]` (גודל התו) לבין `sizeof s` (גודל המצביע)."],
    steps=[
        {"type": "numeric", "prompt": "מה ערכו של `sizeof s[0]`?",
         "answer": 1, "tol": 0, "explain": "`s[0]` הוא `char` (ריצה אמיתית: 1)."},
        {"type": "choice", "prompt": "מהו הטיפוס של הקבוע `'a'` בשפת C?",
         "options": co("`char`", "`int`", "`unsigned char`", "`short`"), "correctId": "b",
         "explain": "בשפת C קבוע תו הוא `int` (ריצה אמיתית: `_Generic` בוחר את הענף של `int`, ו-`sizeof 'a'` הוא 4)."},
        {"type": "numeric", "prompt": "מה הפלט של התוכנית?",
         "answer": -6, "tol": 0, "explain": "$1+1-4-4=-6$ (ריצה אמיתית: `-6`)."},
    ],
    stepsSource="ai-verified")


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
