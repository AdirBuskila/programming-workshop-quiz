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
