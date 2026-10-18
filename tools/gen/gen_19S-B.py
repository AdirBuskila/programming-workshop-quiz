# -*- coding: utf-8 -*-
"""Generator for tools/raw/19S-B.json -- programming-workshop (C), summer semester 2019, moed B (21.11.19).
Q1, Q2, Q3 (28 pts each, all required), Q4 (16 pts, four pick-and-justify items), Q5 bonus (10 pts).
Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/19S-B/. Run: PYTHONUTF8=1 py tools/gen/gen_19S-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "19S-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזת `infile` וגם מחרוזות `outfile_true` ו-`outfile_false` המהוות שמות של שלושה קבצי טקסט.
תוכן של קובץ ששמו נכלל ב-`infile` הוא טקסט מוצפן שנוצר מהטקסט המקורי באופן הבא:
אחרי תו אחרון של כל שורה בטקסט המקורי מוספים רווח (ניתן להניח שאין רווחים בטקסט המקורי);
אחרי הרווח מוספים מספר ביקורת ששווה לסכום קודי ASCII של כל תווי השורה;
תו של סוף השורה אמור להופיע גם בסוף של השורה האחרונה של הקובץ.

על הפונקציה לבדוק נכונות של מספר הביקורת בכל שורה.
יש להעתיק כל שורה שבה מספר הביקורת נכון לקובץ `outfile_true` וכל שורה שבה מספר הביקורת לא נכון לקובץ `outfile_false`. לא להעתיק את מספרי הביקורת עצמם.
בנוסף הפונקציה תעביר במצביעים (by reference) את מספר השורות בקובץ `outfile_true` ואת מספר השורות בקובץ `outfile_false`.
לא להשתמש במחרוזות ומערכי עזר.

**דוגמא:**
`infile`:
```
abc 294
3+2+1=6 352
A 65
```
`outfile_true`:
```
abc
A
```
`outfile_false`:
```
3+2+1=6
```
**הסבר:**
שורה ראשונה. קודי ASCII של 'a', 'b', 'c' הם 97, 98, 99 בהתאמה. 294=97+98+99.
שורה שנייה. סכום קודי ASCII של כל תווי השורה (ספרות ותווים לפעולות אריתמטיות) הוא 351. לכן מספר ביקורת 352 יהיה לא נכון.
שורה שלישית. קוד ה-ASCII של 'A' שהוא התו היחיד בשורה שווה ל-65.

הפונקציה תעביר 2 (מספר שורות ב-`outfile_true`) ו-1 (מספר שורות ב-`outfile_false`)."""

Q1_SOL = r"""```c
/* auxiliary function */
void copy_row(FILE *in, FILE *out, int start_row, int *rows)
{
      char c;
      fseek(in, start_row, SEEK_SET); //to the beginning of row
      while ( (c = fgetc(in)) != ' ' ) //copy chars till space
            fputc(c, out);
      fputc('\n', out);
      (*rows)++;
}

void copy_true_false_file_rows (char *infile, char *outfile_true,
      char *outfile_false, int *true_rows, int *false_rows)
{
      int sum=0, control_num, start_row=0, end_row;
      char c;
      FILE *in = fopen(infile, "r"),
            *out_true = fopen(outfile_true, "w"),
            *out_false = fopen(outfile_false, "w");
      if( !in || !out_true || !out_false )
            exit(1);
      *true_rows = *false_rows = 0;
      while ( (c = fgetc(in)) != EOF )
      {
            if (c != ' ')
                  sum += c;
            else //start of control number
            {
                  fscanf(in, "%d", &control_num);
                  end_row = ftell(in); //save end of row
                  if (control_num == sum)
                        copy_row(in, out_true, start_row, true_rows);
                  else
                        copy_row(in, out_false, start_row, false_rows);
                  sum = 0;
                  start_row = end_row + 2; //start of next row ('\' and 'n' are two positions)
                  fseek(in, start_row, SEEK_SET);//to the beginning of next row
            }
      }
      fclose(in);
      fclose(out_true);
      fclose(out_false);
}
```

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הפתרון מניח שסוף שורה בקובץ תופס שני מקומות (`\r\n`, קובץ טקסט של Windows). הוא הורץ עם clang (`tools/verify/19S-B/q1.c`) על דוגמת המבחן בקובץ כזה ופלט את התוצאה הנכונה (2 שורות נכונות ושורה אחת לא נכונה)."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונות ההגדרות הבאות של הטיפוסים:
```c
typedef struct data_item {
  int data;
  struct data_item *next;
} DataItem;
```
```c
typedef struct ptr_item {
  int *ptr;
  struct ptr_item *next;
} PtrItem;
```
כתוב פונקציה המקבלת **מערך `AL` של רשימות מקושרות** של מספרים שלמים וגודלו. הרשימות מורכבות מאיברים מסוג `DataItem`.

על הפונקציה לבנות **רשימה מקושרת `LA` של מערכים** של מספרים שלמים. הרשימה תהיה מורכבת מאיברים מסוג `PtrItem`. שדה `ptr` של איבר מס' `i` ב-`LA` יצביע לתחילת **מערך מספרים** מס' `i` ושדה `next` שלו יצביע לאיבר הבא ב-`LA`.

גודל מערך מס' `i` ב-`LA` יהיה שווה לגודל רשימה מס' `i` ב-`AL`. איבר מס' `j` של מערך מס' `i` ב-`LA` יהיה שווה לשדה `data` של איבר מס' `j` ברשימה מס' `i` ב-`AL`. אם רשימה מס' `i` ב-`AL` ריקה אז שדה `ptr` של איבר מס' `i` ב-`LA` יהיה שווה ל-NULL.

הפונקציה תחזיר את **כתובת** ראש הרשימה `LA`.
בנוסף הפונקציה תיצור ותעביר במצביעים (by reference) מערך דינאמי `SIZE` המורכב מגדלי המערכים ב-`LA` כך שאיבר מס' `i` של `SIZE` יהיה שווה לגודל מערך מס' `i` ב-`LA`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
PtrItem *array_of_lists_to_list_of_arrays (DataItem **AL, int n,
                                                  int **SIZE)
{
      PtrItem *LA, *curr_ptr;
      DataItem *data_lst;
      int i, j;

      *SIZE = (int *)calloc(n, sizeof(int));
      LA = (PtrItem *)malloc(sizeof(PtrItem)); //dummy
      curr_ptr = LA;
      for (i=0; i<n; i++)
      {
            curr_ptr->next = (PtrItem *)malloc(sizeof(PtrItem));
            curr_ptr = curr_ptr->next;

            /* Computing size of i-th list in AL (i-th array in LA) */
            (*SIZE)[i] = 0;
            if (AL[i])
            {
                  data_lst = AL[i];
                  while (data_lst)
                  {
                        (*SIZE)[i]++;
                        data_lst = data_lst->next;
                  }
                  curr_ptr->ptr = (int *)calloc((*SIZE)[i], sizeof(int));
            }
            else
                  curr_ptr->ptr = NULL;

            /* Copy i-th array of AL to i-th list in LA */
            data_lst = AL[i];
            j = 0;
            while (data_lst)
            {
                  curr_ptr->ptr[j++] = data_lst->data;
                  data_lst = data_lst->next;
            }
      }
      curr_ptr->next = NULL;

      /* deletion of dummy */
      curr_ptr = LA;
      LA = LA->next;
      free (curr_ptr);
      return LA;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה (void) אשר מקבלת מחרוזת `str` שמורכבת מכמה **מילים** (**מילה** היא רצף תווים שאינם רווח המופרדים ממילים אחרות ע"י רווחים). נתון כי `str` אינה מתחילה ואינה מסתיימת ברווח. מספר רווחים בין מילים רצופות ב-`str` הוא שרירותי. יתכן ש-`str` מורכבת ממילה יחידה בלבד.

על הפונקציה לבצע היסט מחזורי של מילים ב-`str` כך שמילה ראשונה (מתחילת המחרוזת) תהיה שנייה, מילה שנייה תהיה שלישית,..., מילה שלפני אחרונה תהיה אחרונה, מילה אחרונה תהיה ראשונה.

**דוגמא:**
`str` לפני עיבוד:
```
one  two  three   four
```
`str` אחרי עיבוד:
```
four one  two   three
```
מספר רווחים בין מילים רצופות ב-`str` אחרי עיבוד יכול להיות שרירותי אבל על מספר הרווחים הכולל ב-`str` לא לעלות על מספר הרווחים הכולל לפני עיבוד.

אפשר להשתמש במחרוזת עזר. במקרה זה ניתן להניח שיש בזיכרון מספיק מקום להקצאתה."""

Q3_SOL = r"""```c
void cyclic_shift_of_string(char *str)
{
      int len = strlen(str), i, j, k;
      char *temp;
      for (i=len-1; i>=0 && str[i]!=' '; i--); //search of beginning last word
      if (i<0) // //only one word in str
            return;
      temp = malloc(len+1);
      for (j=0, k=i+1; k<len; j++, k++)
            temp[j] = str[k]; //copy last word to auxiliary string
      for (; str[i]==' '; j++, i--) //search of end of penultimate word
            temp[j] = ' ';
      for (k=0; k<=i; j++, k++)
            temp[j] = str[k]; //copy from first to penultimate word
      temp[j] = '\0';
      strcpy(str, temp);
      free(temp);
}
```"""

# ---------------------------------------------------------------- Q4 (16 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 16 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + "מה ההבדל בין מבנה לאיגוד?"
Q4A_OPTS = opts("לשדה של מבנה ניתן לפנות דרך מצביע למשתנה ולשדה של איגוד ניתן לפנות רק דרך שם המשתנה",
                "לשדה של איגוד ניתן לפנות דרך מצביע למשתנה ולשדה של מבנה ניתן לפנות רק דרך שם המשתנה",
                "לעומת מבנה, שדות איגוד משתפים אותו מקום בזיכרון",
                "לעומת איגוד, שדות מבנה משתפים אותו מקום בזיכרון",
                "אף תשובה אינה נכונה")
Q4A_EXPL = "לפי כללי שפת C."

Q4B_TEXT = Q4_INTRO + "מהי הטענה הנכונה?"
Q4B_OPTS = opts("גודל מצביע ל-`double` עולה על גודל מצביע ל-`char`",
                "גודל מצביע ל-`double` שווה לגודל מצביע ל-`char`",
                "גודל מצביע ל-`double` קטן מגודל מצביע ל-`char`",
                "לא ניתן להשוות גדלי מצביעים ל-`char` ול-`double`",
                "אף טענה אינה נכונה")
Q4B_EXPL = "כי גדלי של כל מצביעים שווים."

Q4C_TEXT = Q4_INTRO + r"""מהו פלט של `printf("%d",~0)` ?"""
Q4C_OPTS = opts("`1`", "`-1`", "`0`", "אף תשובה אינה נכונה")
Q4C_EXPL = "ייצוג בינארי של 0 הוא `000…0`. לכן ייצוג בינארי של `~0` הוא `111…1` אשר מהווה ייצוג בינארי של `-1`."

Q4D_TEXT = Q4_INTRO + r"""```c
int *const *q;
```
מה הוא `q`?"""
Q4D_OPTS = opts("פוינטר לפוינטר קבוע שמצביע למשתנה", "פוינטר לפוינטר לקבוע",
                "פוינטר קבוע לפוינטר שמצביע למשתנה", "אף תשובה אינה נכונה")
Q4D_EXPL = "לפי כללי שפת C."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
  int a[100];
  printf("%d", sizeof a + sizeof sizeof a + sizeof sizeof sizeof a);
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
408
```
**נימוק:**
`sizeof a` זה גודל של מערך `a` והוא 400 בתים (100 איברים מסוג `int`, גודל של `int` הוא 4 בתים).
`sizeof sizeof a` זה גודל של 400 אשר טיפוסו `int` ולכן הוא 4 בתים.
`sizeof sizeof sizeof a` זה גודל של 4 אשר טיפוסו `int` ולכן הוא 4 בתים.
`408=400+4+4`

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הנימוק מניח שהטיפוס של `sizeof` הוא בגודל 4 בתים (מערכת של 32 סיביות). בהרצה אמיתית (`tools/verify/19S-B/q5.c`) הקומפילציה ל-32 סיביות מדפיסה `408`, ואילו בקומפילציה ל-64 סיביות מודפס `416` (הטיפוס של `sizeof` הוא בן 8 בתים)."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=28),
    Q(2, "code", "list_manipulation", Q2_TEXT, Q2_SOL, points=28, image="images/exams/19S-B-Q2.png"),
    Q(3, "code", "strings", Q3_TEXT, Q3_SOL, points=28),
    M("א", "structs_unions", Q4A_TEXT, Q4A_OPTS, "c", Q4A_EXPL),
    M("ב", "pointers", Q4B_TEXT, Q4B_OPTS, "b", Q4B_EXPL),
    M("ג", "bit_manipulation", Q4C_TEXT, Q4C_OPTS, "b", Q4C_EXPL),
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


# Q1 -- copy_true_false_file_rows (the official solution assumes Windows text files: CRLF, two positions per line end)
F1a = func_lines(Q1_SOL, "void copy_row")
F1 = func_lines(Q1_SOL, "void copy_true_false_file_rows")
B1 = [r'int sum=0, control_num, start_row=0, end_row; char c; FILE *in = fopen(infile, "r"), *out_true = fopen(outfile_true, "w"), *out_false = fopen(outfile_false, "w");',
      "if( !in || !out_true || !out_false ) exit(1); *true_rows = *false_rows = 0;",
      r'''while ( (c = fgetc(in)) != EOF ) { if (c != ' ') sum += c; else { fscanf(in, "%d", &control_num); end_row = ftell(in); if (control_num == sum) copy_row(in, out_true, start_row, true_rows); else copy_row(in, out_false, start_row, false_rows); sum = 0; start_row = end_row + 2; fseek(in, start_row, SEEK_SET); } }''',
      "fclose(in); fclose(out_true); fclose(out_false);"]
f1, j1 = blank(F1a, "while ( (c = fgetc(in)) != ' ' )")
b1, i1 = swap(F1, "if (control_num == sum)", "if (control_num >= sum)")
WIN = "(קבצי טקסט של Windows: סוף שורה הוא `\\r\\n`, כמו בהנחת הפתרון הרשמי)"
add(1,
    rubric=rub(("פתיחת שלושת הקבצים ובדיקת הצלחה, ואיפוס שני המונים", 5),
               ("קריאה תו תו וצבירת סכום קודי ה-ASCII של תווי השורה עד הרווח", 5),
               ("קריאת מספר הביקורת (`fscanf`) ושמירת מיקום סוף השורה (`ftell`)", 6),
               ("חזרה להתחלת השורה (`fseek`) והעתקת תווי השורה עד הרווח לקובץ המתאים לפי השוואה לסכום, עם עדכון המונה המתאים", 8),
               ("מעבר לשורה הבאה: דילוג על סוף השורה (שני מקומות), איפוס הסכום וסגירת הקבצים", 4)),
    rubricSource="ai-draft",
    pitfalls=["להעתיק גם את הרווח ואת מספר הביקורת לקובץ, כי עוצרים רק בסוף השורה במקום ברווח.",
              "לשכוח לאפס את הסכום או להזיז את תחילת השורה הבאה, ואז כל השורות אחרי הראשונה נבדקות מול סכום שגוי.",
              "להניח שסוף שורה הוא תו אחד ולדלג רק על `'\\n'`, כשבקובץ של Windows סוף שורה תופס שני מקומות."],
    steps=[
        {"type": "numeric",
         "prompt": "`infile` מכיל חמש שורות: `ab 195`, `xy 241`, `q 114`, `zz 0`, `pq 225` " + WIN + ". מה ערכו של `*true_rows` בסוף הפונקציה?",
         "answer": 3, "tol": 0,
         "explain": "מספרי הביקורת של `ab` (195), `xy` (241) ו-`pq` (225) נכונים, ושל `q` (נכון 113) ו-`zz` (נכון 244) שגויים (ריצה אמיתית: 3 שורות נכונות)."},
        {"type": "numeric",
         "prompt": "באותו קובץ, מה ערכו של `*false_rows` בסוף הפונקציה?",
         "answer": 2, "tol": 0,
         "explain": "השורות `q 114` ו-`zz 0` עוברות ל-`outfile_false` (ריצה אמיתית: 2)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הלולאה שמעתיקה את השורה (בלי מספר הביקורת) לקובץ.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": co("while ( (c = fgetc(in)) != ' ' )",
                       "while ( (c = fgetc(in)) != '\\n' )",
                       "while ( (c = fgetc(in)) == ' ' )",
                       "while ( (c = fgetc(in)) != EOF )"),
         "correctId": "a",
         "explain": "מעתיקים עד הרווח שלפני מספר הביקורת. ב' ממשיך עד סוף השורה וכולל את מספר הביקורת, ג' לא מעתיק דבר, ד' מעתיק את כל המשך הקובץ (ריצה אמיתית: כל אחת מהאפשרויות הללו נותנת קבצי פלט שונים)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ושורה שמספר הביקורת שלה גדול מהסכום הנכון מועתקת לקובץ השורות הנכונות. מצאו אותה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "התנאי חייב להיות שוויון מדויק. עם `>=` השורה `q 114` (נכון 113) נחשבת נכונה (ריצה אמיתית: 4 שורות נכונות במקום 3)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של `copy_true_false_file_rows` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "הצהרות ופתיחה, בדיקת הפתיחה ואיפוס המונים, לולאת הבדיקה וההעתקה, וסגירה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת (קובץ קלט שאינו קיים), או נותנת פלט שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-draft")

# Q2 -- array_of_lists_to_list_of_arrays
F2 = func_lines(Q2_SOL, "PtrItem *array_of_lists_to_list_of_arrays")
B2 = ["PtrItem *LA, *curr_ptr; DataItem *data_lst; int i, j;",
      "*SIZE = (int *)calloc(n, sizeof(int)); LA = (PtrItem *)malloc(sizeof(PtrItem)); curr_ptr = LA;",
      "for (i=0; i<n; i++) { curr_ptr->next = (PtrItem *)malloc(sizeof(PtrItem)); curr_ptr = curr_ptr->next; (*SIZE)[i] = 0; if (AL[i]) { data_lst = AL[i]; while (data_lst) { (*SIZE)[i]++; data_lst = data_lst->next; } curr_ptr->ptr = (int *)calloc((*SIZE)[i], sizeof(int)); } else curr_ptr->ptr = NULL; data_lst = AL[i]; j = 0; while (data_lst) { curr_ptr->ptr[j++] = data_lst->data; data_lst = data_lst->next; } }",
      "curr_ptr->next = NULL; curr_ptr = LA; LA = LA->next; free (curr_ptr); return LA;"]
f2, j2 = blank(F2, "curr_ptr->ptr[j++] = data_lst->data;")
b2, i2 = swap(F2, "for (i=0; i<n; i++)", "for (i=0; i<n-1; i++)")
add(2,
    rubric=rub(("הקצאת מערך הגדלים `*SIZE` בגודל `n`", 3),
               ("בניית רשימת `PtrItem` עם איבר לכל רשימה ב-`AL`, לפי הסדר (בעזרת איבר דמה)", 7),
               ("ספירת איברי הרשימה `i` והקצאת מערך בגודל המתאים; `NULL` ברשימה ריקה", 8),
               ("העתקת ערכי `data` של הרשימה למערך, לפי הסדר", 6),
               ("סיום הרשימה ב-`NULL`, הסרת איבר הדמה והחזרת `LA`", 4)),
    rubricSource="ai-draft",
    pitfalls=["להקצות מערך בגודל 0 או לגשת ל-`AL[i]->next` כשהרשימה ריקה, במקום להציב `NULL` ב-`ptr`.",
              "להעתיק את הערכים בלי להתקדם באינדקס `j`, כך שכל הערכים נכנסים לתא הראשון.",
              "לשכוח את מערך הגדלים `SIZE` או לא להעביר אותו by reference."],
    steps=[
        {"type": "choice",
         "prompt": "הרשימה `AL[1]` ריקה. מה ערכו של השדה `ptr` באיבר מספר 1 של `LA`?",
         "options": co("`NULL`", "מצביע למערך בגודל 0", "מצביע לא מאותחל", "מצביע למערך של האיבר הקודם"), "correctId": "a",
         "explain": "הפונקציה מציבה `NULL` ב-`ptr` כשהרשימה ריקה (ריצה אמיתית: `ptr==NULL` ו-`SIZE[1]==0`)."},
        {"type": "numeric",
         "prompt": "`AL` מכיל שלוש רשימות: `5 6 7`, רשימה ריקה, ו-`8 9`. מה ערכו של `LA->next->next->ptr[1]`, כלומר האיבר השני במערך של האיבר השלישי ב-`LA`?",
         "answer": 9, "tol": 0,
         "explain": "האיבר השלישי ב-`LA` מצביע על המערך `8 9` ולכן האיבר השני הוא 9 (ריצה אמיתית: `SIZE = 3 0 2`)."},
        {"type": "fillblank", "prompt": "השלימו את שורת ההעתקה של ערכי הרשימה למערך.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": co("curr_ptr->ptr[j++] = data_lst->data;",
                       "curr_ptr->ptr[j] = data_lst->data;",
                       "curr_ptr->ptr[j++] = data_lst->next->data;",
                       "curr_ptr->ptr[j++] = data_lst->data + j;"),
         "correctId": "a",
         "explain": "יש להעתיק את `data` של האיבר הנוכחי ולהתקדם באינדקס. ב' לא מתקדם, ג' מעתיק את האיבר הבא (וקורס באחרון), ד' משנה את הערך (ריצה אמיתית: כל אחת מהאפשרויות הללו נותנת מערכים שונים או קורסת)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והרשימה האחרונה של `AL` אינה מופיעה ב-`LA`. מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "`i<n-1` מדלג על הרשימה האחרונה (ריצה אמיתית: `LA` מכיל 2 איברים במקום 3, ו-`SIZE[2]` נשאר 0)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של הפונקציה.", "code": True, "lines": B2,
         "explain": "הצהרות, הקצאת `SIZE` ואיבר הדמה, לולאת הבנייה, וסיום הרשימה עם הסרת הדמה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או מחזירה תוצאה שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-draft")

# Q3 -- cyclic_shift_of_string
F3 = func_lines(Q3_SOL, "void cyclic_shift_of_string")
B3 = ["int len = strlen(str), i, j, k; char *temp;",
      "for (i=len-1; i>=0 && str[i]!=' '; i--); if (i<0) return;",
      "temp = malloc(len+1); for (j=0, k=i+1; k<len; j++, k++) temp[j] = str[k];",
      "for (; str[i]==' '; j++, i--) temp[j] = ' ';",
      "for (k=0; k<=i; j++, k++) temp[j] = str[k]; temp[j] = '\\0';",
      "strcpy(str, temp); free(temp);"]
f3, j3 = blank(F3, "for (i=len-1; i>=0 && str[i]!=' '; i--);")
b3, i3 = swap(F3, "for (j=0, k=i+1; k<len; j++, k++)", "for (j=0, k=i+1; k<len-1; j++, k++)")
add(3,
    rubric=rub(("מציאת תחילת המילה האחרונה בסריקה מהסוף, וחזרה בלי שינוי כשיש מילה אחת בלבד", 6),
               ("הקצאת מחרוזת עזר בגודל `len+1`", 4),
               ("הרכבת המחרוזת החדשה בסדר: המילה האחרונה, אחריה הרווחים שלפניה, ואחריהם שאר המחרוזת", 12),
               ("סיום המחרוזת ב-`'\\0'` והעתקתה חזרה אל `str`", 4),
               ("שחרור מחרוזת העזר", 2)),
    rubricSource="ai-draft",
    pitfalls=["לשכוח את המקרה של מילה יחידה: אין רווח במחרוזת והסריקה יוצאת מהגבולות.",
              "לשכוח להעתיק את הרווחים שבין המילה האחרונה לקודמת, ולהדביק את המילים זו לזו.",
              "לשכוח את `'\\0'` בסוף מחרוזת העזר לפני `strcpy`."],
    steps=[
        {"type": "text",
         "prompt": "`str` היא `\"to be or not\"`. מה תכיל `str` אחרי הפונקציה? (כתבו את המחרוזת בלי מרכאות)",
         "accept": ["not to be or"], "normalize": "none",
         "explain": "המילה האחרונה `not` עוברת להתחלה, אחריה הרווח שהיה לפניה ושאר המחרוזת (ריצה אמיתית: `not to be or`)."},
        {"type": "numeric",
         "prompt": "`str` היא `\"one  two  three   four\"`. כמה רווחים יש בין `four` למילה `one` אחרי הפונקציה?",
         "answer": 3, "tol": 0,
         "explain": "הפתרון מעתיק אחרי המילה האחרונה את שלושת הרווחים שהיו לפניה (ריצה אמיתית: `four   one  two  three`)."},
        {"type": "fillblank", "prompt": "השלימו את לולאת החיפוש של תחילת המילה האחרונה (מהסוף להתחלה).", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": co("for (i=len-1; i>=0 && str[i]!=' '; i--);",
                       "for (i=len-1; i>=0 && str[i]==' '; i--);",
                       "for (i=len-1; i>0 && str[i]!=' '; i--);",
                       "for (i=len-1; i>=0 && str[i]!='\\0'; i--);"),
         "correctId": "a",
         "explain": "עוצרים ברווח האחרון או בתחילת המחרוזת. ב' עוצר מיד כי התו האחרון אינו רווח, ג' מפספס מילה יחידה, ד' אף פעם לא עוצר ברווח (ריצה אמיתית: כל אחת מהאפשרויות הללו נותנת תוצאה שונה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ובתוצאה המילה שעברה להתחלה חסרה את התו האחרון שלה. מצאו אותה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`k<len-1` לא מעתיק את התו האחרון של המילה (ריצה אמיתית: `not to be or` הופך ל-`no to be or`)."},
        {"type": "order", "prompt": "סדרו את הבלוקים של הפונקציה.", "code": True, "lines": B3,
         "explain": "הצהרות, חיפוש המילה האחרונה, העתקת המילה, העתקת הרווחים, העתקת שאר המחרוזת עם הסיום, והעתקה חזרה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או נותנת מחרוזת שונה (נבדק בריצה)."},
    ],
    stepsSource="ai-draft")

# Q5 (bonus) -- sizeof; the official answer assumes 32-bit (checked with clang -m32)
add(5,
    rubric=rub(("`sizeof a` הוא גודל המערך כולו: 100 איברים של 4 בתים, כלומר 400", 4),
               ("`sizeof sizeof a` הוא הגודל של הטיפוס של התוצאה (שלם בן 4 בתים), כלומר 4, וכך גם `sizeof sizeof sizeof a`", 4),
               ("סכום: $400+4+4=408$", 2)),
    rubricSource="ai-draft",
    pitfalls=["לחשוב ש-`sizeof a` הוא גודל מצביע (4) ולא גודל המערך כולו, כי כאן `a` הוא מערך ולא פרמטר של פונקציה.",
              "לשכוח שגם `sizeof sizeof a` הוא ביטוי שיש לו גודל (גודל הטיפוס של התוצאה) ולא 400.",
              "לשכוח שהמפתח הרשמי מניח מערכת של 32 סיביות: ב-64 סיביות `sizeof` הוא בן 8 בתים והפלט 416."],
    steps=[
        {"type": "numeric",
         "prompt": "מה ערכו של `sizeof a` עבור `int a[100]`?",
         "answer": 400, "tol": 0,
         "explain": "100 איברים בני 4 בתים כל אחד (ריצה אמיתית: 400)."},
        {"type": "numeric",
         "prompt": "במערכת של 32 סיביות (כמו במפתח הרשמי), מה ערכו של `sizeof sizeof a`?",
         "answer": 4, "tol": 0,
         "explain": "התוצאה של `sizeof` היא מספר שלם בן 4 בבתים במערכת של 32 סיביות (ריצה אמיתית עם `clang -m32`: 4)."},
        {"type": "text",
         "prompt": "מה הפלט של התוכנית, במערכת של 32 סיביות?",
         "accept": ["408"], "normalize": "none",
         "explain": "$400+4+4=408$ (ריצה אמיתית עם `clang -m32`: `408`; ב-64 סיביות הפלט הוא `416`)."},
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "19S-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר קיץ תשע\"ט, מועד ב'",
    "year": 2019,
    "examDate": "21.11.19",
    "sourceFile": "19S-B exam",
    "solutionFile": "19S-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
