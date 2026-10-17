# -*- coding: utf-8 -*-
"""Generator for tools/raw/19S-A.json -- programming-workshop (C), summer semester 2019, moed A (23.10.19).
Q1, Q2, Q3 (28 pts each, all required), Q4 (16 pts, four pick-and-justify items), Q5 bonus (10 pts).
Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/19S-A/. Run: PYTHONUTF8=1 py tools/gen/gen_19S-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19S-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזת `fileName`.
תוכן של קובץ טקסט ששמו נכלל ב-`fileName` הוא טקסט מוצפן שנוצר מהטקסט המקורי באופן הבא:
אחרי תו אחרון של כל שורה בטקסט המקורי מוספים רווח (ניתן להניח שאין רווחים בטקסט המקורי);
אחרי הרווח מוספים מספר ביקורת וצמוד למספר מוספים תו ביקורת;
מספר הביקורת יהיה מספר ששווה לסכום קודי ASCII של כל תווי השורה;
תו הביקורת יהיה תו שקוד ASCII שלו הוא שארית החלוקה של מספר הביקורת ב-128;
תו של סוף השורה אמור להופיע גם בסוף של השורה האחרונה של הקובץ.

**דוגמא:**
טקסט מקורי:
```
abc
3+2+1=6
A
```
תוכן הקובץ:
```
abc 294&
3+2+1=6 351_
A 65A
```
**הסבר:**
שורה ראשונה. קודי ASCII של 'a', 'b', 'c' הם 97, 98, 99 בהתאמה. 294=97+98+99, 294%128=38. 38 הוא קוד ה-ASCII של '&'.
שורה שנייה. סכום קודי ASCII של כל תווי השורה (ספרות ותווים לפעולות אריתמטיות) הוא 351. 351%128=95. 95 הוא קוד ה-ASCII של '_'.
שורה שלישית. קוד ה-ASCII של 'A' שהוא התו היחיד בשורה שווה ל-65. 65%128=65.

על הפונקציה לבדוק נכונות של מספר ביקורת ותו ביקורת בכל שורה.
אם המספר והתו נכונים בכל שורה הפונקציה תחזיר **1**. אם לפחות בשורה אחת המספר או התו לא נכונים, היא תחזיר **0**. אם הקובץ לא נפתח יש להחזיר **-1**."""

Q1_SOL = r"""**גרסה 1**
```c
int check_controls_in_file_rows (char *fileName)
{
      int sum=0, control_num;
      char c, control_char;
      FILE *fptr = fopen(fileName, "r");
      if( !fptr )
            return -1;
      while ( (c = fgetc(fptr)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else
            {
                  fscanf(fptr, "%d%c", &control_num, &control_char);
                  if (control_char == '\n')
      //real control char is digit that was interpreted as last digit of control number
                  {
                         control_char = control_num%10 + '0';
                         control_num /= 10;
                  }
                  else
                         fgetc(fptr); //input '/n'
                  if (control_num != sum || control_char != sum%128)
                  {
                         fclose(fptr);
                         return 0;
                  }
                  else
                        sum = 0;
            } //else
      } //while
      fclose(fptr);
      return 1;
}
```
**גרסה 2**
```c
int check_controls_in_file_rows_2 (char *fileName)
{
      int sum=0, control_sum;
      char c, last_char;
      FILE *fptr = fopen(fileName, "r");
      if( !fptr )
            return -1;
      while ( (c = fgetc(fptr)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else
            {
                  control_sum = fgetc(fptr)-'0'; //first digit
                  last_char = fgetc(fptr);
                  while ( (c = fgetc(fptr)) != '\n' )
                  {
                        //last_char is current digit of control_sum
                        control_sum = control_sum*10 + last_char-'0';
                        last_char = c;
                  }
                  if (control_sum != sum || last_char != sum%128)
                  {
                        fclose(fptr);
                        return 0;
                  }
                  else
                        sum = 0;
            }
      }
      fclose(fptr);
      return 1;
}
```
**הערת מתמלל (לא חלק מהפתרון הרשמי):** שתי הגרסאות הורצו עם clang (`tools/verify/19S-A/q1.c`) על דוגמת המבחן ועל קבצים עם מספר או תו ביקורת שגויים ועל תו ביקורת שהוא ספרה, וכולן החזירו את הערך הנכון."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה ההגדרה הבאה של הטיפוס:
```c
typedef struct item
{
  char *string;
  struct item *next;
} Item;
```
כתוב פונקציה אשר מקבלת מערך מחרוזות `S` עם גודלו ובונה רשימה מקושרת `L` של **מחרוזות** המורכבת מאיברים מסוג `Item`.

שדה ה-`string` של האיבר ה-`i` (חוליה) ברשימה `L` (מתחילתה) יצביע ל**מחרוזת דינאמית** החדשה המכילה את **המילה הראשונה** במחרוזת `S[i]` (**מילה** היא רצף תווים שאינם רווח המופרדים ממילים אחרות ע"י רווחים). אם `S[i]` היא מחרוזת ריקה אז המחרוזת המתאימה באיבר ה-`i` של `L` גם תהיה ריקה.
נתון כי אף מחרוזת ב-`S` אינה מתחילה ברווח. תתכן מחרוזת המורכבת ממילה יחידה בלבד.

הפונקציה תחזיר את **כתובת** ראש הרשימה `L`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאות."""

Q2_SOL = r"""```c
Item *array_of_strings_to_list (char **S, int n)
{
      Item *lst, *curr_ptr;
      int i, j;
      lst = (Item *)malloc(sizeof(Item)); //dummy
      curr_ptr = lst;
      for (j=0; j<n; j++)
      {
            curr_ptr->next = (Item *)malloc(sizeof(Item));
            curr_ptr = curr_ptr->next;
            //initial allocation - for all the string with '\0'
            curr_ptr->string = (char *)malloc(strlen(S[j])+1);
            for (i=0; S[j][i]!='\0' && S[j][i]!=' '; i++)
                  curr_ptr->string[i] = S[j][i];
            curr_ptr->string[i] = '\0';
            //reallocation for the first word in a string with '\0'
            curr_ptr->string = (char *)realloc(curr_ptr->string, i+1);
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
Q3_TEXT = r"""כתוב פונקציה אשר מקבלת שני מערכים דו-ממדיים דינאמיים `A` ו-`B` בעלי אותה כמות שורות `n`. יחד עם `n`, הפונקציה מקבלת מערכים חד-ממדיים `SA` ו-`SB` של גדלי השורות ב-`A` וב-`B` בהתאמה כך ש-`SA[i]` יהיה שווה לגודל שורה `A[i]` ו-`SB[i]` יהיה שווה לגודל שורה `B[i]`.

על הפונקציה ליצור מערך דו-ממדי דינאמי `C` בעל `n` שורות.
גודל שורה `C[i]` יהיה שווה למינימום בין גדלי השורות `A[i]` ו-`B[i]` וכל איבר `C[i][j]` יהיה שווה ל-`A[i][j]+B[i][j]`.

הפונקציה תחזיר את הכתובת של מערך `C` ותעביר במצביעים (by reference) מערך דינאמי `SC` המורכב מגדלי שורות של `C` כך ש-`SC[i]` יהיה שווה לגודל שורה `C[i]`.

ניתן להניח שיש בזיכרון מקום להקצאות.

**דוגמא:**
`SA`: `2, 4, 6`
`A`:
```
13 33
15 17 19 21
41 43 53 41 17 15
```
`SB`: `3, 3, 4`
`B`:
```
20 19 56
44 11 39
55 50 27 14
```
`SC`: `2, 3, 4`
`C`:
```
33 52
59 28 58
96 93 80 55
```"""

Q3_SOL = r"""```c
int **sum_of_2_dim_arrays(int **A, int *SA, int **B, int *SB, int **SC,
int n)
{
      int i, j, **C;
      C = (int **)calloc(n, sizeof(int *));
      *SC = (int *)calloc(n, sizeof(int));
      for (i=0; i<n; i++) {
            (*SC)[i] = (SA[i]<SB[i])? SA[i] : SB[i];
            C[i] = (int *)calloc((*SC)[i], sizeof(int));
            for (j=0; j<(*SC)[i]; j++)
                  C[i][j] = A[i][j]+B[i][j];
      }
      return C;
}
```"""

# ---------------------------------------------------------------- Q4 (16 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 16 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + "איזה פעולה לא מוגדרת למבנים?"
Q4A_OPTS = opts("השמה", "לקיחת כתובת", "גישה לאיבר", "השוואה", "`sizeof`", "כל הפעולות לעיל מוגדרות")
Q4A_EXPL = "לפי כללי שפת C, כדי להימנע מהשוואת תכני המרווחים בין איברי המבנה."

Q4B_TEXT = Q4_INTRO + "מהי הטענה הנכונה?"
Q4B_OPTS = opts("אחרי ביצוע פעולת הזזה שמאלה במספר, מצד ימין המספר מתמלא ב-0-ים",
                "אחרי ביצוע פעולת הזזה שמאלה במספר, מצד ימין המספר מתמלא ב-1-ים",
                "אחרי ביצוע פעולת הזזה שמאלה במספר, מצד ימין המספר מתמלא בסיביות שהלכו לאיבוד מצד שמאל",
                "אחרי ביצוע פעולת הזזה שמאלה במספר, שיטת מילוי המספר מצד ימין תלויה במערכת",
                "אף טענה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C."

Q4C_TEXT = Q4_INTRO + r"""```c
int x, *ptr1;
const int y = 5, *ptr2;
```
איזו פעולה תהיה בלתי חוקית?"""
Q4C_OPTS = opts("`ptr1 = &x;`", "`ptr2 = &y;`", "`ptr1 = &y;`", "`ptr2 = &x;`", "כל הפעולות לעיל חוקיות")
Q4C_EXPL = "כי גישה לקבוע דרך מצביע רגיל תאפשר לשנות את הקבוע."

Q4D_TEXT = Q4_INTRO + "איזו מילה היא לא חלק של הנחית קדם-מעבד?"
Q4D_OPTS = opts("`define`", "`ifdef`", "`undef`", "`ifndef`", "`typedef`",
                "כל המילים לעיל הן חלקים של הנחיות קדם-מעבד")
Q4D_EXPL = "משתמשים ב-`typedef` להגדרת טיפוס חדש."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
  char *s="123";
  puts( (char *)( ((long long)s*(long long)s+2*(long long)s+1)/(long long)(s+1) ) );
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
23
```
**נימוק:**
`Casting` ל-`long long` ממיר כתובת (ערך `s`) למספר שלם. מקבלים
`(s^2+2s+1)/(s+1)=(s+1)^2/(s+1)=s+1`
`Casting` ל-`char *` קובע ערך `s+1` ככתובת של תו מס' 1 במחרוזת.
פלט מתו מס' 1 עד סוף המחרוזת: `23`

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הנימוק מניח שכתובת ו-`s*s` נכנסים בטווח של `long long` ללא גלישה. בהרצה אמיתית (`tools/verify/19S-A/q5.c`) הקומפילציה ל-32 סיביות מדפיסה `23`, ואילו בקומפילציה ל-64 סיביות ריבוע הכתובת גולש והתוכנית קורסת."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=28),
    Q(2, "code", "strings", Q2_TEXT, Q2_SOL, points=28, image="images/exams/19S-A-Q2.png"),
    Q(3, "code", "dynamic_arrays_2d", Q3_TEXT, Q3_SOL, points=28),
    M("א", "structs_unions", Q4A_TEXT, Q4A_OPTS, "d", Q4A_EXPL),
    M("ב", "bit_manipulation", Q4B_TEXT, Q4B_OPTS, "a", Q4B_EXPL),
    M("ג", "storage_classes", Q4C_TEXT, Q4C_OPTS, "c", Q4C_EXPL),
    M("ד", "c_traps_mcq", Q4D_TEXT, Q4D_OPTS, "e", Q4D_EXPL),
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "19S-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר קיץ תשע\"ט, מועד א'",
    "year": 2019,
    "examDate": "23.10.19",
    "sourceFile": "19S-A exam",
    "solutionFile": "19S-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
