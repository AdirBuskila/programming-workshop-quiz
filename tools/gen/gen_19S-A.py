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
**הערה:** המשתנה `c` מוגדר כ-`char` ומושווה ל-`EOF` (שהוא `int`). במערכת שבה `char` הוא ללא סימן הלולאה לא נגמרת, ובמערכת עם סימן היא נעצרת מוקדם כשנקרא הבייט `0xFF`. הנכון הוא `int c`.

**הערה:** אם תו הביקורת הוא `'\n'` (סכום הקודים בשורה מתחלק ב-128 עם שארית 10, למשל השורה `AI`), הוא שובר את מבנה השורה בקובץ ושתי הגרסאות מחזירות 0 גם עבור קובץ תקין.

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
Q4C_EXPL = "כי גישה לקבוע דרך מצביע רגיל תאפשר לשנות את הקבוע.\n\n**הערה:** לפי התקן ההשמה `ptr1 = &y;` היא הפרת אילוץ, אבל ב-gcc וב-clang היא מייצרת רק אזהרה (והקוד מתקמפל), ולכן התשובה 'בלתי חוקית' נכונה לפי כללי השפה ולא לפי התנהגות המהדר."

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


# Q1 -- check_controls_in_file_rows (steps follow the second version of the official solution)
Q1_V2 = Q1_SOL.split("**גרסה 2**")[1]
F1 = func_lines(Q1_V2, "int check_controls_in_file_rows_2")
B1 = [r'int sum=0, control_sum; char c, last_char; FILE *fptr = fopen(fileName, "r");',
      "if( !fptr ) return -1;",
      r'''while ( (c = fgetc(fptr)) != EOF ) { if (c != ' ') sum += c; else { control_sum = fgetc(fptr)-'0'; last_char = fgetc(fptr); while ( (c = fgetc(fptr)) != '\n' ) { control_sum = control_sum*10 + last_char-'0'; last_char = c; } if (control_sum != sum || last_char != sum%128) { fclose(fptr); return 0; } else sum = 0; } }''',
      "fclose(fptr); return 1;"]
f1, j1 = blank(F1, "if (control_sum != sum || last_char != sum%128)")
b1, i1 = swap(F1, "sum += c;", "sum = c;")
add(1,
    rubric=rub(("פתיחת הקובץ לקריאה והחזרת `-1` כשהפתיחה נכשלת", 4),
               ("קריאה תו אחר תו וצבירת סכום קודי ה-ASCII של תווי השורה עד הרווח", 6),
               ("קריאת מספר הביקורת אחרי הרווח והפרדת תו הביקורת שצמוד אליו (התו האחרון לפני סוף השורה)", 8),
               ("השוואה: מספר הביקורת מול הסכום, ותו הביקורת מול `sum%128`; החזרת 0 ויציאה כשיש אי-התאמה ואיפוס הסכום לשורה הבאה", 6),
               ("סגירת הקובץ בכל יציאה והחזרת 1 כשכל השורות תקינות", 4)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא את מספר הביקורת עם `%d` ולאבד את תו הביקורת כשהוא ספרה (למשל השורה `0 480`), כי הספרה נבלעת במספר.",
              "להשוות את מספר הביקורת ל-`sum%128` או את תו הביקורת ל-`sum`, במקום מספר מול `sum` ותו מול `sum%128`.",
              "לא לאפס את הסכום בין שורות, או לא לסגור את הקובץ לפני `return 0`."],
    steps=[
        {"type": "choice",
         "prompt": "הקובץ מכיל את שתי השורות `abc 294&` ו-`A 65B`. מה מחזירה הפונקציה?",
         "options": co("`1`", "`0`", "`-1`"), "correctId": "b",
         "explain": "בשורה הראשונה הכול נכון, אבל בשורה השנייה תו הביקורת הנכון הוא `A` ולא `B`, ולכן מוחזר 0 (ריצה אמיתית: 0)."},
        {"type": "numeric",
         "prompt": "הקובץ מכיל את השורה `ab 195C`. מה ערכו של `control_sum` בסוף הלולאה הפנימית, כלומר מה מספר הביקורת שנקרא?",
         "answer": 195, "tol": 0,
         "explain": "הספרות 1, 9, 5 נצברות ל-195, והתו האחרון `C` נשאר ב-`last_char` (ריצה אמיתית: `control_sum=195 last_char=C`)."},
        {"type": "fillblank", "prompt": "השלימו את התנאי שמזהה שורה שבה מספר הביקורת או תו הביקורת שגויים.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": co("if (control_sum != sum || last_char != sum%128)",
                       "if (control_sum != sum && last_char != sum%128)",
                       "if (control_sum != sum || last_char != sum)",
                       "if (control_sum != sum%128 || last_char != sum%128)"),
         "correctId": "a",
         "explain": "מספיק שאחד מהשניים שגוי (`||`). ב' דורש ששניהם שגויים, ג' משווה את התו לסכום עצמו, ד' משווה את המספר לשארית (ריצה אמיתית: כל אחת מהאפשרויות הללו מחזירה ערך שגוי על אחד הקבצים)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה 0 על קובץ תקין עם שורות של יותר מתו אחד. מצאו אותה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "`sum = c;` דורס את הסכום בכל תו, ולכן הסכום שווה לקוד התו האחרון בלבד. הפתרון הנכון צובר עם `+=` (ריצה אמיתית: על `abc 294&` מוחזר 0)."},
        {"type": "order", "prompt": "סדרו את הפקודות של הפונקציה (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "הצהרות ופתיחה, בדיקת הפתיחה לפני הקריאה, לולאת הבדיקה, ובסוף סגירה והחזרת 1. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת (קובץ שאינו קיים) או מחזירה ערך שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-verified")

# Q2 -- array_of_strings_to_list
F2 = func_lines(Q2_SOL, "Item *array_of_strings_to_list")
B2 = ["Item *lst, *curr_ptr; int i, j;",
      "lst = (Item *)malloc(sizeof(Item)); curr_ptr = lst;",
      r'''for (j=0; j<n; j++) { curr_ptr->next = (Item *)malloc(sizeof(Item)); curr_ptr = curr_ptr->next; curr_ptr->string = (char *)malloc(strlen(S[j])+1); for (i=0; S[j][i]!='\0' && S[j][i]!=' '; i++) curr_ptr->string[i] = S[j][i]; curr_ptr->string[i] = '\0'; curr_ptr->string = (char *)realloc(curr_ptr->string, i+1); }''',
      "curr_ptr->next = NULL; curr_ptr = lst; lst = lst->next; free (curr_ptr); return lst;"]
f2, j2 = blank(F2, r"for (i=0; S[j][i]!='\0' && S[j][i]!=' '; i++)")
b2, i2 = swap(F2, "for (j=0; j<n; j++)", "for (j=0; j<n-1; j++)")
add(2,
    rubric=rub(("בניית רשימה מקושרת עם איבר אחד לכל מחרוזת של `S`, לפי הסדר (בעזרת איבר דמה)", 7),
               ("מציאת המילה הראשונה: מעבר על התווים עד רווח או עד `'\\0'`, והעתקתם למחרוזת דינמית חדשה", 9),
               ("סיום המחרוזת ב-`'\\0'` בגודל מתאים (`realloc` ל-`i+1`), כך שמחרוזת ריקה נותנת מחרוזת ריקה", 6),
               ("סיום הרשימה ב-`NULL`, הסרת איבר הדמה והחזרת כתובת הראש", 6)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא רק עד `'\\0'` ולהעתיק את כל המחרוזת במקום עד הרווח הראשון.",
              "לשכוח את התו `'\\0'` במחרוזת החדשה, או להקצות מקום בלי אותו תו.",
              "להחזיר את כתובת איבר הדמה, או לא לסיים את הרשימה ב-`NULL`."],
    steps=[
        {"type": "numeric",
         "prompt": "המערך הוא `S = {\"red apple\", \"green\", \"\", \"blue sky\"}`. מה סכום האורכים של ארבע המחרוזות ברשימה שנבנית?",
         "answer": 12, "tol": 0,
         "explain": "`red` (3), `green` (5), מחרוזת ריקה (0) ו-`blue` (4): 12 (ריצה אמיתית: 12)."},
        {"type": "numeric",
         "prompt": "עבור המחרוזת `\"hello world\"`, כמה בתים מוקצים למחרוזת החדשה אחרי ה-`realloc`?",
         "answer": 6, "tol": 0,
         "explain": "המילה `hello` היא 5 תווים ועוד `'\\0'`: 6 בתים (ריצה אמיתית: גודל הבלוק 6)."},
        {"type": "fillblank", "prompt": "השלימו את הלולאה שמעתיקה את המילה הראשונה של `S[j]`.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": co(r"for (i=0; S[j][i]!='\0' && S[j][i]!=' '; i++)",
                       r"for (i=0; S[j][i]!='\0'; i++)",
                       r"for (i=0; S[j][i]!='\0' && S[j][i]==' '; i++)",
                       r"for (i=0; S[j][i]!='\0' && i<3; i++)"),
         "correctId": "a",
         "explain": "עוצרים בסוף המחרוזת או ברווח הראשון. ב' מעתיק את כל המחרוזת, ג' עוצר מיד כי התו הראשון אינו רווח, ד' חותך אחרי 3 תווים (ריצה אמיתית: כל אחת מהאפשרויות הללו נותנת רשימה שונה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והרשימה שנבנית קצרה באיבר אחד מהמערך `S`. מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "`j<n-1` מדלג על המחרוזת האחרונה (ריצה אמיתית: מערך של 4 מחרוזות נותן רשימה של 3 איברים, ומערך של מחרוזת אחת גורם לקריסה)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של הפונקציה.", "code": True, "lines": B2,
         "explain": "הצהרות, יצירת איבר הדמה, לולאת הבנייה, ולבסוף סיום הרשימה והסרת הדמה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או מחזירה רשימה שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-verified")

# Q3 -- sum_of_2_dim_arrays
F3 = func_lines(Q3_SOL, "int **sum_of_2_dim_arrays")
B3 = ["int i, j, **C;",
      "C = (int **)calloc(n, sizeof(int *)); *SC = (int *)calloc(n, sizeof(int));",
      "for (i=0; i<n; i++) { (*SC)[i] = (SA[i]<SB[i])? SA[i] : SB[i]; C[i] = (int *)calloc((*SC)[i], sizeof(int)); for (j=0; j<(*SC)[i]; j++) C[i][j] = A[i][j]+B[i][j]; }",
      "return C;"]
f3, j3 = blank(F3, "(*SC)[i] = (SA[i]<SB[i])? SA[i] : SB[i];")
b3, i3 = swap(F3, "C[i][j] = A[i][j]+B[i][j];", "C[i][j] = A[i][j]+B[j][i];")
add(3,
    rubric=rub(("הקצאת מערך המצביעים `C` בגודל `n` והקצאת `*SC` בגודל `n`", 6),
               ("חישוב גודל שורה `i` של `C` כמינימום בין `SA[i]` ל-`SB[i]` ושמירתו ב-`(*SC)[i]`", 7),
               ("הקצאת שורה `C[i]` בגודל `(*SC)[i]`", 6),
               ("חישוב כל איבר `C[i][j] = A[i][j] + B[i][j]` בטווח המשותף של שתי השורות", 6),
               ("החזרת `C` והעברת `SC` by reference דרך המצביע", 3)),
    rubricSource="ai-verified",
    pitfalls=["לקחת את הגודל המקסימלי או את `SA[i]` בלבד, ואז לקרוא מעבר לסוף השורה הקצרה יותר.",
              "לכתוב `SC[i]` במקום `(*SC)[i]`, כך שהמערך לא מועבר לפונקציה הקוראת.",
              "להקצות את כל השורות של `C` לפני שידוע גודלן, או לשכוח להקצות את מערך הגדלים `*SC`."],
    steps=[
        {"type": "numeric",
         "prompt": "נתון `SA = {3, 1}`, `SB = {2, 5}`, `A = {{1,2,3},{4}}` ו-`B = {{10,20},{40,50,60,70,80}}`. כמה איברים יש בסך הכול ב-`C`?",
         "answer": 3, "tol": 0,
         "explain": "גדלי השורות הם $\\min(3,2)=2$ ו-$\\min(1,5)=1$, ולכן `SC = {2, 1}` ובסך הכול 3 איברים (ריצה אמיתית)."},
        {"type": "numeric",
         "prompt": "באותם נתונים, מה ערכו של `C[1][0]`?",
         "answer": 44, "tol": 0,
         "explain": "$A[1][0]+B[1][0]=4+40=44$ (ריצה אמיתית: `C = {{11,22},{44}}`)."},
        {"type": "fillblank", "prompt": "השלימו את השורה שקובעת את גודל שורה `i` של `C`.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": co("(*SC)[i] = (SA[i]<SB[i])? SA[i] : SB[i];",
                       "(*SC)[i] = (SA[i]>SB[i])? SA[i] : SB[i];",
                       "(*SC)[i] = SA[i];",
                       "(*SC)[i] = SA[i] + SB[i];"),
         "correctId": "a",
         "explain": "גודל השורה הוא המינימום בין שני הגדלים. ב' בוחר מקסימום, ג' את `SA[i]` בלבד, ד' את הסכום (ריצה אמיתית: כל אחת מהאפשרויות הללו נותנת `SC` שונה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ואיברים בשורות של `C` אינם הסכום של האיברים באותו מקום ב-`A` וב-`B`. מצאו אותה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`B[j][i]` מחליף את האינדקסים. הסכום חייב להיות של התאים `A[i][j]` ו-`B[i][j]` (ריצה אמיתית: `C[0][1]` יוצא 42 במקום 22, ועל מערכים גדולים יותר התוכנית קוראת מחוץ לגבולות)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של הפונקציה.", "code": True, "lines": B3,
         "explain": "הצהרות, הקצאת `C` ו-`*SC`, לולאה שממלאת את הגדלים והשורות, והחזרה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או מחזירה תוצאה שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-verified")

# Q5 (bonus) -- address arithmetic; the official answer assumes 32-bit pointers (checked with clang -m32)
add(5,
    rubric=rub(("זיהוי שההמרה ל-`long long` הופכת את הכתובת `s` למספר שלם, כך שהמונה הוא $s^2+2s+1$", 3),
               ("פישוט: $(s+1)^2/(s+1)=s+1$ (בחילוק שלמים מדויק)", 4),
               ("המרה חזרה ל-`char *`: הכתובת `s+1` מצביעה על התו השני במחרוזת, ו-`puts` מדפיס `23`", 3)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב שהתוכנית מדפיסה את הכתובת כמספר, ולשכוח שההמרה ל-`char *` והקריאה ל-`puts` מדפיסות מחרוזת.",
              "לפשט ל-`s` במקום ל-`s+1`, ולהדפיס את כל המחרוזת `123`.",
              "לשכוח שהפתרון הרשמי מניח כתובות של 32 סיביות: במערכת של 64 סיביות ריבוע הכתובת גולש והתוכנית קורסת."],
    steps=[
        {"type": "numeric",
         "prompt": "נניח ש-`s` שווה ל-1000 (כתובת). מה ערכו של `(s*s+2*s+1)/(s+1)` בחשבון שלמים?",
         "answer": 1001, "tol": 0,
         "explain": "$(1000+1)^2/(1000+1)=1001$, כלומר $s+1$ (ריצה אמיתית ב-`long long`: 1001)."},
        {"type": "choice",
         "prompt": "לאיזה תו במחרוזת `\"123\"` מצביעה הכתובת שמועברת ל-`puts`?",
         "options": co("`'1'`", "`'2'`", "`'3'`", "`'\\0'`"), "correctId": "b",
         "explain": "הכתובת היא `s+1`, כלומר מיקום 1 במחרוזת: התו `'2'` (ריצה אמיתית ב-32 סיביות: ההפרש בין הכתובת שהועברה ל-`s` הוא 1)."},
        {"type": "text",
         "prompt": "מה הפלט של התוכנית? (בהנחה של מערכת 32 סיביות, כמו במפתח הרשמי)",
         "accept": ["23"], "normalize": "none",
         "explain": "`puts` מדפיס מהתו `'2'` עד סוף המחרוזת: `23` (ריצה אמיתית עם `clang -m32`: `23`; ב-64 סיביות התוכנית קורסת)."},
    ],
    stepsSource="ai-verified")


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
