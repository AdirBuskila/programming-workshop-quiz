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
