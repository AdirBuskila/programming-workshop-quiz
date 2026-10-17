# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-A.json -- programming-workshop (C), semester B 2025, moed A (11.06.2025).
Q1 (40), Q2/Q3 (40 each, answer one), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/25B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_25B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-A.json"
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
typedef struct node {
  char value;
  struct node* next;
} node;
```
כתבו פונקציה `void removeExtraSpaces(node** head)` אשר מקבלת פוינטר `head` המצביע על ראש רשימה מקושרת חד כיוונית של איברים מסוג `node` המייצגת משפט כלשהו.
על הפונקציה להסיר איברים מתוך הרשימה המהווים תווי רווח (`' '`) **מיותרים**. תו רווח נחשב **מיותר** אם הוא מופיע **מיד אחרי תו רווח אחר**, או נמצא **בתחילת הרשימה**, או נמצא **בסוף הרשימה**.

**הערות:**
- הפונקציה לא אמורה לייצר איברים חדשים.
- אם הרשימה מכילה רק רווחים, הפונקציה תהפוך אותה לרשימה ריקה.
- במידה והרשימה ריקה, היא תישאר ריקה לאחר סיום הפונקציה.

**דוגמאות:** עבור הרשימה המייצגת את המשפט `"  No  way! "` הפונקציה תעדכן את הרשימה כך שתייצג `"No way!"`. עבור רשימה המכילה ארבעה רווחים בלבד ישוחררו כל איברי הרשימה ויתקבל `head` המצביע על `NULL`."""

Q1_SOL = r"""```c
void deleteHead(node** head)
{
       node* temp = *head;
       *head = temp->next;
       free(temp);
}

void deleteNext(node* pos)
{
       node* temp = pos->next;
       pos->next = temp->next;
       free(temp);
}

void removeExtraSpaces(node** head)
{
       node* curr, *prev;
       while (*head && (*head)->value == ' ')
              deleteHead(head); //remove first spaces
       if (*head == NULL)
              return;
       prev = *head;
       curr = prev->next;
       while (curr)
       {
              if (curr->value == ' ' && (!curr->next || curr->next->value == ' '))
                     deleteNext(prev); //remove space if no next or the next is space too
              else
                     prev = curr;
              curr = prev->next;
       }
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

**האלכסון הראשי** של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית העליונה של המטריצה עד לפינה הימנית התחתונה.
**האלכסון המשני** של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית התחתונה של המטריצה עד לפינה הימנית העליונה.
כל איברי המטריצה הריבועית הנמצאים באלכסון הראשי שלה ומתחתיו מרכיבים את **המשולש השמאלי התחתון** של המטריצה.
כל איברי המטריצה הריבועית הנמצאים באלכסון המשני שלה ומעליו מרכיבים את **המשולש השמאלי העליון** של המטריצה.

**דוגמא:** (איור: המטריצה, המשולש השמאלי התחתון והמשולש השמאלי העליון)

כתבו פונקציה `void triangles(int A[][N], int n, int ***tr_low, int ***tr_up)` אשר מקבלת מטריצה ריבועית של מספרים שלמים המיושמת כ**מערך דו-ממדי סטטי** (לא דינאמי) `A` בגודל `n×n`. המספר הפיסי של השורות (העמודות) יינתן ע"י קבוע בשם `N`. יש להגדיר אותו לפני הפונקציה.
על הפונקציה ליצור שני **מערכים דו-ממדיים דינאמיים** (בעלי שורות בגדלים שונים) המיישמים את המשולש השמאלי התחתון ואת המשולש השמאלי העליון של המטריצה. גדלי השורות במערכים יהיו שווים לכמויות האיברים בשורות המתאימות של המשולשים. יש להעביר את המערכים by reference באמצעות מצביעים `tr_up` ו-`tr_low` בהתאמה.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
#define N 4

void triangles(int A[][N], int n, int*** tr_low, int*** tr_up)
{
       int i, j, ** low, ** up;

       low = (int**)calloc(n, sizeof(int*));
       for (i = 0; i < n; i++)
       {
              low[i] = (int*)calloc(i + 1, sizeof(int));
              for (j = 0; j <= i; j++)
                     low[i][j] = A[i][j];
       }

       up = (int**)calloc(n, sizeof(int*));
       for (i = 0; i < n; i++)
       {
              up[i] = (int*)calloc(n - i, sizeof(int));
              for (j = 0; j < n - i; j++)
                     up[i][j] = A[i][j];
       }

       *tr_low = low;
       *tr_up = up;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

כתבו פונקציה `int wordAppearanceNum(char *file_name, char *word)` אשר מקבלת מחרוזת `file_name` המהווה שם של קובץ טקסט ומחרוזת `word`.
תוכן הקובץ מורכב משורות. ידוע שאורך השורה (כולל `'\n'`) לא עולה על 100. השורה האחרונה גם מסתיימת ב-`'\n'`.
על הפונקציה להחזיר את **כמות המופעים** של המילה `word` בקובץ (**מילה** היא רצף תווים שאינם רווח או `'\n'` המופרדים ממילים אחרות ע"י רווחים או תווי `'\n'`). אם הקובץ לא נפתח, הפונקציה תחזיר `-1`.

**שימו לב:** יש להתייחס רק למילה שלמה. אין להתייחס לרצף שהוא תת-מילה במילה אחרת.

**דוגמא:** עבור הקובץ הבא והמילה `live`
```
I believe that they live here and who does not live here
Mike lives in this house
And who does live here ? We live
10 alive creatures live in this lived place
```
הפונקציה תחזיר 5.

אפשר (אבל לא חובה) להשתמש במערך עזר של תווים בגודל שאינו עולה על 101.

**רמז:** ניתן להשתמש בפונקציות סטנדרטיות."""

Q3_SOL = r"""**גרסה 1:**
```c
int wordAppearanceNum(char* file_name, char* word)
{
       FILE* fptr = fopen(file_name, "r");
       char str[101], *sub_str, *p;
       int count = 0, len = strlen(word);
       if (!fptr)
              return -1;
       while (fgets(str, 101, fptr))
       {
              sub_str = str;
              while ((p = strstr(sub_str, word)) != NULL) //p - the first occurrence of word in substring
              {
                     //checking edges: is the found word complete or subword
                     if ((p == str || *(p - 1) == ' ') && (*(p + len) == ' ' || *(p + len) == '\n'))
                            count++;
                     sub_str = p + len + 1; //the next substring
              }
       }
       fclose(fptr);
       return count;
}
```
**גרסה 2:**
```c
int wordAppearanceNum(char* file_name, char* word)
{
       FILE* fptr = fopen(file_name, "r");
       char str[100], *separators = " \n", *token;
       int count = 0;
       if (!fptr)
              return -1;
       while (fgets(str, 100, fptr))
       {
              token = strtok(str, separators); //the first token
              while (token != NULL)
              {
                     if (strcmp(token, word) == 0) //comparison of token with word
                            count++;
                     token = strtok(NULL, separators); //the next token
              }
       }
       fclose(fptr);
       return count;
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
typedef struct
{
    int x;
    int y;
} type1;
typedef union
{
    int x;
    int y;
} type2;
void fun(type2 b) {
    b.x++;
    printf("%d %d\n", b.x, b.y);
}
void main() {
    type1 a;
    type2 b;
    a.x = b.x = 3;
    a.y = b.y = 5;
    printf("%d %d\n", a.x, a.y);
    printf("%d %d\n", b.x, b.y);
    b.x = 8;
    b.y = 4;
    a.x = b.x;
    a.y = b.y;
    printf("%d %d\n", a.x, a.y);
    b.x = 15;
    b.y = 18;
    fun(b);
    printf("%d %d\n", b.x, b.y);
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
3 5
5 5
4 4
19 19
18 18
```
**נימוק:**
שדות `x,y` של המבנה מקבלים ערכים 3,5 בהתאמה.
שדות `x,y` של האיגוד מקבלים ערכים 3,5 בהתאמה. השדות תופסים אותו מקום בזיכרון ולכן שניהם שווים לערך 5 של העדכון האחרון.
לכן שני הפלטים הראשונים
`3 5`
`5 5`
שדות `x,y` של האיגוד מקבלים ערכים 8,4 בהתאמה. השדות תופסים אותו מקום בזיכרון ולכן שניהם שווים לערך 4 של העדכון האחרון. שדות `x,y` של המבנה מקבלים ערכי שדות `x,y` של האיגוד בהתאמה. לכן שניהם גם שווים ל-4. לכן הפלט השלישי הוא
`4 4`
שדות `x,y` של האיגוד מקבלים ערכים 15,18 בהתאמה. השדות תופסים אותו מקום בזיכרון ולכן שניהם שווים לערך 18 של העדכון האחרון.
האיגוד מועבר לפונקציה `fun` והאיגוד מועתק לאיגוד שהוא פרמטר פורמאלי של `fun`. שדה `x` שלו (ובהתאם שדה `y`) מתקדם ב-1 וכך שני השדות שלו יהיו שווים ל-19. לכן הפלט הרביעי הוא
`19 19`
אחרי יציאה מהפונקציה חוזרים לאיגוד המקורי בו שני השדות שווים ל-18. לכן הפלט החמישי הוא
`18 18`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + r"""מהו פלט (משמאל לימין) של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
     printf("%d%d%d", sizeof(char*), sizeof(double*), sizeof(void*));
}
```"""
Q5A_OPTS = opts("184", "444", "180", "440",
                "לא יהיה פלט כי גודל של מצביע ל-`void` לא מוגדר",
                "אף תשובה אינה נכונה")
Q5A_EXPL = "גדלי כל המצביעים ללא קשר לטיפוס (גם של מצביע כללי) הם 4 בתים. (המפתח הרשמי מניח מצביעים של 4 בתים; במהדר של 64 סיביות הגודל הוא 8 והפלט 888.)"

Q5B_TEXT = Q5_INTRO + r"""בחרו מהו ערך של הביטוי `24 << 1`"""
Q5B_OPTS = opts("240", "2", "2.4", "48", "12", "אף תשובה אינה נכונה")
Q5B_EXPL = "הזזת סיבית אחת שמאלה במספר בה הסיבית בשמאלית היא 0 שווה ערך להוספת סיבית 0 לימין, כלומר הכפלת המספר ב-2. 24×2=48."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** בהינתן קובץ הטקסט `file.dat` (שנפתח בהצלחה) בעל התוכן `abc` מהו הפלט למסך של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
     char c;
     FILE* fptr = fopen("file.dat", "r");
     if (!fptr) return;
     while (c = fgetc(fptr) != EOF)
          printf("%d", c);
     fclose(fptr);
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `111`

**נימוק:**
בהיעדר סוגריים, לפי סדר הקדימות, פעולת השוואה מבוצעת לפני פעולת השמה. עבור תווי `'a'`, `'b'`, `'c'` התנאי `fgetc(fptr) != EOF` מתקיים ולכן ערך הביטוי יהיה 1. כלומר `c` בשלוש האיטרציות יהיה 1, תנאי המשך הלולאה יתקיים ובהתאם 1 יודפס שלוש פעמים. עבור `EOF` התנאי `fgetc(fptr) != EOF` לא מתקיים ולכן ערך הביטוי יהיה 0. כלומר `c` יהיה 0 ותנאי המשך הלולאה לא יתקיים.
`111`"""

questions = [
    Q(1, "code", "linked_lists", Q1_TEXT, Q1_SOL, points=40, image="images/exams/25B-A-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40, image="images/exams/25B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    Q(4, "code", "structs_unions", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "c_traps_mcq", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "b", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "d", "explanation": Q5B_EXPL,
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


# Q1 -- removeExtraSpaces
F1 = func_lines(Q1_SOL, "void removeExtraSpaces")
B1 = ["while (*head && (*head)->value == ' ') deleteHead(head);",
      "if (*head == NULL) return;",
      "node* curr, *prev = *head; curr = prev->next;",
      "while (curr) { if (curr->value == ' ' && (!curr->next || curr->next->value == ' ')) deleteNext(prev); else prev = curr; curr = prev->next; }"]
f1, j1 = blank(F1, "while (*head && (*head)->value == ' ')")
b1, i1 = swap(F1, "if (curr->value == ' ' && (!curr->next || curr->next->value == ' '))",
              "if (curr->value == ' ' && (curr->next && curr->next->value == ' '))")
add(1,
    rubric=rub(("מחיקת הרווחים שבתחילת הרשימה בלולאה על `*head`, כך שהראש מתעדכן דרך המצביע הכפול ואיברים נמחקים עם `free`", 12),
               ("טיפול ברשימה שנהפכה לריקה (כולה רווחים או ריקה מההתחלה): חזרה מהפונקציה כש-`*head` הוא `NULL`", 6),
               ("מעבר על שאר הרשימה עם שני מצביעים `prev` ו-`curr`, ומחיקת רווח שאחריו רווח נוסף או שהוא האיבר האחרון", 14),
               ("שמירה על תקינות המצביעים אחרי מחיקה: `prev` לא מתקדם כשנמחק איבר, ו-`curr` נקרא מחדש מ-`prev->next`", 8)),
    rubricSource="ai-draft",
    pitfalls=["להניח שהראש לא משתנה ולקבל `node*` במקום `node**`, או לגשת ל-`(*head)->value` כשהרשימה כבר ריקה (קריסה ברשימה שכולה רווחים).",
              "להתקדם ב-`prev` גם אחרי מחיקה, ואז לדלג על איבר או להשאיר שני רווחים רצופים.",
              "לא לבדוק את הרווח האחרון ברשימה: התנאי חייב לכלול גם `curr->next == NULL`, אחרת נשאר רווח בסוף."],
    steps=[
        {"type": "numeric",
         "prompt": "הרשימה מייצגת את המשפט `\"  No  way! \"` (שני רווחים בתחילה, שני רווחים בין המילים ורווח בסוף). כמה איברים נשארים ברשימה אחרי `removeExtraSpaces`?",
         "answer": 7, "tol": 0,
         "explain": "מתקבל `\"No way!\"`: שבעה תווים (ריצה אמיתית: 7 איברים)."},
        {"type": "numeric",
         "prompt": "הרשימה מורכבת מהתווים: רווח, רווח, `a`, רווח, רווח, `b`, רווח, רווח. כמה איברים נשארים ברשימה בסוף הפונקציה?",
         "answer": 3, "tol": 0,
         "explain": "מתקבל `\"a b\"`: שני הרווחים בתחילה נמחקים בלולאה הראשונה, רווח אחד מבין שני הרווחים שבאמצע נמחק, ושני הרווחים בסוף נמחקים (ריצה אמיתית: 3 איברים)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי הלולאה שמוחקת את הרווחים שבתחילת הרשימה.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": [{"id": "a", "type": "text", "value": "while (*head && (*head)->value == ' ')"},
                     {"id": "b", "type": "text", "value": "while ((*head)->value == ' ')"},
                     {"id": "c", "type": "text", "value": "while (*head && (*head)->value != ' ')"},
                     {"id": "d", "type": "text", "value": "while (*head && (*head)->value == ' ' && (*head)->next)"}],
         "correctId": "a",
         "explain": "הבדיקה `*head &&` מונעת גישה ל-`NULL` ברשימה שכולה רווחים (ב' קורס עליה), ו-ד' משאיר רווח אחד ברשימה שכולה רווחים. ג' מוחק את האותיות במקום את הרווחים (ריצה אמיתית: כל אחת מהאפשרויות הללו נכשלת)."},
        {"type": "order", "prompt": "סדרו את הפקודות של `removeExtraSpaces` (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B1,
         "explain": "קודם מחיקת הרווחים מההתחלה, אז חזרה אם הרשימה ריקה, אחר כך הצהרה ואתחול של `prev` ו-`curr`, ולבסוף הלולאה הראשית. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או מחזירה פלט שונה (נבדק בריצה)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ורווח שנמצא בסוף הרשימה אינו נמחק (למשל אחרי `x` נשאר רווח). מצאו את השורה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "התנאי `curr->next && ...` לא מתקיים באיבר האחרון, ולכן רווח אחרון נשאר (ריצה אמיתית: אחרי `x` נשאר רווח). בפתרון הנכון התנאי הוא `!curr->next || ...`."},
    ],
    stepsSource="ai-draft")

# Q2 -- triangles
F2 = func_lines(Q2_SOL, "void triangles")
f2, j2 = blank(F2, "up[i][j] = A[i][j];")
b2, i2 = swap(F2, "for (j = 0; j <= i; j++)", "for (j = 0; j < i; j++)")
add(2,
    rubric=rub(("הגדרת הקבוע `N` לפני הפונקציה והקצאת מערך מצביעים בגודל `n` לכל אחד משני המשולשים", 8),
               ("המשולש התחתון: שורה `i` מוקצית בגודל `i+1` ומועתקים אליה `A[i][0..i]`", 10),
               ("המשולש העליון: שורה `i` מוקצית בגודל `n-i` ומועתקים אליה `A[i][0..n-i-1]`", 14),
               ("העברה by reference: `*tr_low = low` ו-`*tr_up = up`", 8)),
    rubricSource="ai-draft",
    pitfalls=["להקצות לכל שורה `n` תאים במקום גודל השורה במשולש (המשולש אינו מלבני), או לחשב את גודל שורה `i` של המשולש העליון כ-`i+1`.",
              "לשכוח את האיבר שעל האלכסון: `j < i` במקום `j <= i` במשולש התחתון, או `j < n-i-1` במשולש העליון.",
              "לכתוב `tr_low = low` במקום `*tr_low = low`, כך שהמערך לא מגיע לפונקציה הקוראת."],
    steps=[
        {"type": "numeric",
         "prompt": "עבור `n = 4`, מה גודל שורה מספר 1 (השנייה) במשולש השמאלי העליון?",
         "answer": 3, "tol": 0,
         "explain": "בשורה `i` של המשולש העליון יש `n - i` איברים: 4 - 1 = 3 (ריצה אמיתית: שורות בגדלים 4, 3, 2, 1)."},
        {"type": "numeric",
         "prompt": "המטריצה היא `A = {{5,7,-3,13},{76,16,8,0},{98,4,43,6},{11,19,21,2}}`. מה ערך `tr_low[3][2]`?",
         "answer": 21, "tol": 0,
         "explain": "`tr_low[3][2] = A[3][2] = 21` (ריצה אמיתית)."},
        {"type": "fillblank", "prompt": "השלימו את שורת ההעתקה של המשולש העליון (באותה מטריצה).", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": [{"id": "a", "type": "text", "value": "up[i][j] = A[i][j];"},
                     {"id": "b", "type": "text", "value": "up[i][j] = A[j][i];"},
                     {"id": "c", "type": "text", "value": "up[i][j] = A[i][j + i];"},
                     {"id": "d", "type": "text", "value": "up[i][j] = A[i][n - 1 - j];"}],
         "correctId": "a",
         "explain": "השורות של המשולש העליון הן תחילת השורות של `A`, ולכן `up[i][j] = A[i][j]`. ב' מעתיק את המשוחלפת, ג' ו-ד' מעתיקים תאים אחרים (ריצה אמיתית: ערכים שונים)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ובמשולש התחתון האיברים שעל האלכסון הראשי יוצאים 0 במקום ערכי `A`. מצאו אותה.", "code": True,
         "lines": b2, "bugIndex": i2,
         "explain": "`j < i` במקום `j <= i` מדלג על התא `A[i][i]` (ריצה אמיתית: האיברים 5, 16, 43, 2 יצאו 0)."},
    ],
    stepsSource="ai-draft")

# Q3 -- wordAppearanceNum (steps follow the second version of the official solution)
F3 = func_lines(Q3_SOL.split("**גרסה 2:**")[1], "int wordAppearanceNum")
B3 = ['FILE* fptr = fopen(file_name, "r"); char str[100], *separators = " \\n", *token; int count = 0;',
      "if (!fptr) return -1;",
      "while (fgets(str, 100, fptr)) { token = strtok(str, separators); while (token != NULL) { if (strcmp(token, word) == 0) count++; token = strtok(NULL, separators); } }",
      "fclose(fptr); return count;"]
f3, j3 = blank(F3, 'char str[100], *separators = " \\n", *token;')
b3, i3 = swap(F3, "while (fgets(str, 100, fptr))", "while (fgets(str, 10, fptr))")
add(3,
    rubric=rub(("פתיחת הקובץ לקריאה והחזרת `-1` כשהפתיחה נכשלת", 6),
               ("קריאת הקובץ שורה אחרי שורה (`fgets` עם מערך עזר של 101 תווים לכל היותר)", 8),
               ("פירוק כל שורה למילים לפי רווח ותו שורה חדשה (`strtok` עם `\" \\n\"`) או בדיקת גבולות המילה בחיפוש `strstr`", 14),
               ("השוואת כל מילה שלמה ל-`word` וספירה; מילה שהיא תת-מחרוזת של מילה אחרת (`lives`, `alive`) לא נספרת", 8),
               ("סגירת הקובץ והחזרת הספירה", 4)),
    rubricSource="ai-draft",
    pitfalls=["לספור כל מופע של `strstr` בלי לבדוק גבולות: `lives`, `alive` ו-`lived` נספרות בטעות והתוצאה גדולה מ-5.",
              "לשכוח שהמילה האחרונה בשורה מסתיימת ב-`'\\n'`, ולהפריד רק לפי רווח: אז `live\\n` לא שווה ל-`live`.",
              "להחזיר 0 או לקרוא מ-`NULL` כשהקובץ לא נפתח, במקום להחזיר `-1`."],
    steps=[
        {"type": "numeric",
         "prompt": "כמה פעמים מופיעה המילה `live` בקובץ הדוגמה (כמילה שלמה)?",
         "answer": 5, "tol": 0,
         "explain": "ריצה אמיתית של שתי הגרסאות על הדוגמה: 5. המילים `lives`, `alive` ו-`lived` אינן נספרות."},
        {"type": "numeric",
         "prompt": "כמה פעמים נספרת המילה `live` בשורה `10 alive creatures live in this lived place` בלבד?",
         "answer": 1, "tol": 0,
         "explain": "רק `live` האמצעית היא מילה שלמה; `alive` ו-`lived` רק מכילות אותה (ריצה אמיתית: 1)."},
        {"type": "fillblank", "prompt": "השלימו את ההצהרה, כך שכל שורה תפורק למילים (תו שורה חדשה בסוף השורה אינו חלק ממילה).", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": [{"id": "a", "type": "text", "value": 'char str[100], *separators = " \\n", *token;'},
                     {"id": "b", "type": "text", "value": 'char str[100], *separators = " ", *token;'},
                     {"id": "c", "type": "text", "value": 'char str[100], *separators = "\\n", *token;'},
                     {"id": "d", "type": "text", "value": 'char str[100], *separators = ".,;", *token;'}],
         "correctId": "a",
         "explain": "יש להפריד גם לפי רווח וגם לפי `'\\n'`. עם רווח בלבד המילה האחרונה בשורה היא `live\\n` ולא נספרת (ריצה אמיתית: 4 במקום 5), ועם `'\\n'` בלבד או סימני פיסוק כל שורה היא \"מילה\" אחת (ריצה אמיתית: 0)."},
        {"type": "order", "prompt": "סדרו את הפקודות של הפונקציה (כל שורה היא בלוק לוגי אחד).", "code": True, "lines": B3,
         "explain": "הצהרות, בדיקת פתיחה, לולאת הקריאה והספירה, ובסוף סגירה והחזרה. כל החלפה של שני בלוקים נכשלת בבנייה, קורסת או נותנת פלט שונה (נבדק בריצה, כולל קובץ שאינו קיים)."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, והתוצאה על קובץ הדוגמה אינה 5. מצאו את השורה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`fgets(str, 10, fptr)` קורא עד 9 תווים בכל פעם, ולכן שורות ארוכות נחתכות באמצע מילים (ריצה אמיתית: תוצאה שונה מ-5)."},
    ],
    stepsSource="ai-draft")

# Q4 -- union output (values from running the program, tools/verify/25B-A/q4.c)
Q4_OUT = ["3 5", "5 5", "4 4", "19 19", "18 18"]
add(4,
    rubric=rub(("זיהוי שבאיגוד `x` ו-`y` חולקים את אותו מקום בזיכרון, ובמבנה לא", 3),
               ("שתי השורות הראשונות: `3 5` למבנה ו-`5 5` לאיגוד", 2),
               ("השורה השלישית `4 4`: ההשמה האחרונה לאיגוד (4) נכנסת לשני השדות של המבנה", 2),
               ("העברת האיגוד לפונקציה by value: בתוך `fun` מודפס `19 19` ובחזרה ל-`main` נשאר `18 18`", 3)),
    rubricSource="ai-draft",
    pitfalls=["להתייחס לאיגוד כמו למבנה ולהדפיס `3 5` גם לאיגוד, במקום `5 5`.",
              "לחשוב ש-`b.x++` ב-`fun` משנה את `b` של `main` (האיגוד מועבר by value), ולהדפיס `19 19` בשורה האחרונה.",
              "לשכוח שאחרי `b.x = 15; b.y = 18;` שני השדות שווים ל-18, ולכן `b.x++` נותן 19 בשני השדות."],
    steps=[
        {"type": "numeric",
         "prompt": "אחרי `a.x = b.x = 3; a.y = b.y = 5;` מה ערכו של `b.x`? (`b` הוא האיגוד)",
         "answer": 5, "tol": 0,
         "explain": "`b.x` ו-`b.y` חולקים אותו מקום, וההשמה האחרונה היא 5 (ריצה אמיתית: השורה `5 5`)."},
        {"type": "numeric",
         "prompt": "אחרי `b.x = 8; b.y = 4; a.x = b.x; a.y = b.y;` מה ערכו של `a.x`? (`a` הוא המבנה)",
         "answer": 4, "tol": 0,
         "explain": "`b.x` כבר שווה ל-4 (ההשמה ל-`b.y` דרסה אותו), ולכן גם `a.x` מקבל 4 (ריצה אמיתית: השורה `4 4`)."},
        {"type": "choice", "prompt": "מה מדפיסה השורה האחרונה בתוכנית (ההדפסה ב-`main` אחרי החזרה מ-`fun`)?",
         "options": [{"id": "a", "type": "text", "value": "`18 18`"}, {"id": "b", "type": "text", "value": "`19 19`"},
                     {"id": "c", "type": "text", "value": "`15 18`"}, {"id": "d", "type": "text", "value": "`19 18`"}],
         "correctId": "a",
         "explain": "`fun` מקבל עותק של האיגוד, ולכן `b` של `main` נשאר עם 18 בשני השדות (ריצה אמיתית: `18 18`)."},
        {"type": "order", "prompt": "סדרו את חמש שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True,
         "lines": Q4_OUT,
         "explain": "המבנה (3 5), האיגוד (5 5), המבנה אחרי ההעתקה (4 4), `fun` (19 19) ו-`main` (18 18); ריצה אמיתית: אותן חמש שורות."},
    ],
    stepsSource="ai-draft")

# Q6 -- bonus: c = fgetc(fptr) != EOF (precedence), file "abc"
add(6,
    rubric=rub(("זיהוי סדר הקדימות: ההשוואה `!=` מתבצעת לפני ההשמה, כך ש-`c = (fgetc(fptr) != EOF)`", 4),
               ("`c` שווה ל-1 בכל אחד משלושת התווים, ו-`printf(\"%d\", c)` מדפיס `1`", 3),
               ("בסוף הקובץ ההשוואה נותנת 0, הלולאה נעצרת, והפלט הסופי `111`", 3)),
    rubricSource="ai-draft",
    pitfalls=["לחשוב ש-`c` מקבל את קוד התו, ולהדפיס `979899` (קודי ASCII של `abc`). בגלל הקדימות `c` מקבל את תוצאת ההשוואה.",
              "לחשוב שהפלט מכיל גם 0 בסוף: בתוצאה 0 הלולאה נעצרת לפני ההדפסה."],
    steps=[
        {"type": "numeric",
         "prompt": "בלי סוגריים, מה ערכו של `c` באיטרציה הראשונה (הקובץ מכיל `abc`)?",
         "answer": 1, "tol": 0,
         "explain": "`c = (fgetc(fptr) != EOF)`: התנאי נכון, ולכן `c` שווה ל-1 (ריצה אמיתית: הודפס 1)."},
        {"type": "numeric",
         "prompt": "כמה איטרציות מבצעת הלולאה על הקובץ `abc`?",
         "answer": 3, "tol": 0,
         "explain": "שלושה תווים נקראים בהצלחה; בקריאה הרביעית מתקבל EOF, `c` הופך ל-0 והלולאה נעצרת (ריצה אמיתית: 3 הדפסות)."},
        {"type": "text", "prompt": "מה הפלט של התוכנית? (רצף ספרות, ללא רווחים)",
         "accept": ["111"], "normalize": "none",
         "explain": "הודפס `1` שלוש פעמים (ריצה אמיתית: `111`)."},
    ],
    stepsSource="ai-draft")


exam = {
    "examCode": "25B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד א'",
    "year": 2025,
    "examDate": "11.06.2025",
    "sourceFile": "25B-A exam",
    "solutionFile": "25B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
