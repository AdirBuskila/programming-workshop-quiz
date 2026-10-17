# -*- coding: utf-8 -*-
"""Generator for tools/raw/24B-B.json -- programming-workshop (C), semester B 2024, moed B (30.07.2024).
Q1 (40), Q2/Q3 (40 each, answer one), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/24B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_24B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "24B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר את המבנה הבא המייצג איבר ברשימה מקושרת חד-כיוונית:
```c
typedef struct item {
        int number;
        struct item* next;
} Item;
```
כתבו פונקציה `Item ** numSeparation(int * A, int sz, int * p_size)` המקבלת מערך `A` של מספרים שלמים עם גודלו `sz`.
על הפונקציה **לסווג** את האיברים של `A` לרשימות של איברים מטיפוס `Item` לפי **כמות הספרות** שבהם. הפונקציה תבנה מערך `L` של מצביעים אשר למעשה מהווה מערך של רשימות כך ש-`L[i]` יצביע לתחילת הרשימה בה שדות `number` של איבריה הם איברים של `A` בעלי `i+1` ספרות. `L` יהיה מורכב מ-`n` איברים, כאשר `n` הוא הכמות המקסימלית של ספרות במספר בין איברי `A`. אם ב-`A` אין אף איבר בעל `m` ספרות (`m<n`) אז `L[m+1]` יהיה שווה ל-`NULL`.
הפונקציה תחזיר את הכתובת של תחילת המערך `L` ותעביר by reference (באמצעות מצביע `p_size`) את גודלו.

**דוגמא:** עבור `A = {23, 4, -78, 34578, 79, -185, 0, 998, 9, 36}` הפונקציה תיצור את המערך `L` הבא (באיור: `L[0]: 4,0,9`; `L[1]: 23,-78,79,36`; `L[2]: -185,998`; `L[3]: NULL`; `L[4]: 34578`) ותעביר 5 כגודל המערך החדש.

יש לכתוב ולהשתמש בפונקציית עזר `int digitsNumber(int num)` אשר מחזירה את כמות הספרות במספר `num`.
להכנסת איבר חדש לרשימה אין צורך לסרוק את הרשימה מתחילתה עד סופה. יש לשמור כתובות של איברים אחרונים ברשימות או להכניס את האיבר לראש הרשימה (סדר האיברים ברשימות אינו משנה).
אפשר (אבל לא חובה) להשתמש במערכי עזר.
ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q1_SOL = r"""```c
digitsNumber(int num)
{
       int count = 1, abs_num = abs(num);
       while (abs_num > 9)
       {
              count++;
              abs_num /= 10;
       }
       return count;
}

void headInsert(Item** plst, int key)
{
       Item* temp = (Item*)malloc(sizeof(Item));
       temp->number = key;
       temp->next = *plst;
       *plst = temp;
}

Item** numSeparation(int* A, int sz, int* p_size)
{
       int i, max_dig_num = 1,
              *dig_num = (int *)calloc(sz, sizeof(int)); //auxiliary array: digit numbers of A's elements
       Item** L;

       /* Search of maximum number of digits */
       for (i = 0; i < sz; i++)
       {
              dig_num[i] = digitsNumber(A[i]);
              if (dig_num[i] > max_dig_num)
                     max_dig_num = dig_num[i];
       }

       L = (Item**)calloc(max_dig_num, sizeof(Item*)); //array of pointers to lists
       for (i = sz - 1; i >= 0; i--)
              headInsert(L + dig_num[i] - 1, A[i]); //insert A[i] into the head of corresponding list

       free(dig_num);
       *p_size = max_dig_num;
       return L;
}
```
**הערה:** בפתרון הרשמי כותרת הפונקציה `digitsNumber` נכתבה ללא טיפוס החזרה `int` (שאלה מחייבת `int digitsNumber(int num)`). במהדר clang בתקן C99 ומעלה ללא `int` זו שגיאת קומפילציה; עם `int` הקוד עובר ומחזיר את הרשימות מהדוגמא."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

כתבו פונקציה `int ** matrixToFrame(int ** M, int rows, int cols)` אשר מקבלת מערך דו-ממדי דינאמי `M` של מספרים שלמים בעל `rows` שורות ו-`cols` עמודות.
`M` מבוסס על מערך דינאמי של פוינטרים אשר מצביעים על מערכים דינאמיים המהווים שורות (כפי שלמדנו בכיתה).

על הפונקציה לבנות מערך דו-ממדי דינאמי `F` בעל `rows+2` שורות ו-`cols+2` עמודות המהווה את תוכן המערך המקורי `M` מוקף ב**מסגרת** המורכבת מאפסים.

**דוגמא:** (איור: המערך `M` בעל 3 שורות ו-4 עמודות, והמערך `F` בעל 5 שורות ו-6 עמודות)

בסוף הפונקציה **תשחרר** את המערך המקורי `M` ו**תחזיר** את הכתובת של המערך `F`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
void freeMatrix(int** M, int rows)
{
       int i;
       for (i = 0; i < rows; i++)
              free(M[i]);
       free(M);
}

int** matrixToFrame(int** M, int rows, int cols)
{
       int rows2 = rows + 2, cols2 = cols + 2, ** F = (int**)calloc(rows2, sizeof(int*)), i, j;
       for (i = 0; i < rows2; i++)
              F[i] = (int*)calloc(cols2, sizeof(int)); //all elements are zeros
       for (i = 0; i < rows; i++)
              for (j = 0; j < cols; j++)
                     F[i + 1][j + 1] = M[i][j];
       freeMatrix(M, rows);
       return F;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

כתבו פונקציה עם החתימה `void processFiles(const char* inputFilename, const char* outputFilename)` אשר מקבלת שמות שני קבצי טקסט (קובץ קלט וקובץ פלט בהתאמה). קובץ הקלט מורכב משורות של תווים שרירותיים.
על הפונקציה למצוא שורות בקובץ הקלט שמורכבות רק מאותיות (באנגלית) ובנוסף מכילות אותיות שונות זו מזו בלבד. יש להתייחס אל אותיות קטנות וגדולות בטקסט באותו האופן (כך שלמשל `'a'` וגם `'A'` יחשבו כאותה אות).
הפונקציה תשמור את השורות הנ"ל בקובץ הפלט כך שסדר האותיות בכל שורה יהיה הפוך.
ניתן להניח שאורך כל שורה בקובץ הקלט אינו עולה על 99 תווים (לא כולל `'\n'`). יש להשתמש במחרוזת עזר.

**דוגמא:**

קובץ הקלט:
```
abc#xyz
table
Alisa
Walla
Michael
```
קובץ הפלט:
```
elbat
leahciM
```
יש לכתוב ולהשתמש בפונקציית עזר `void reverseString(char* str)` להפיכת סדר התווים במחרוזת.
יש לכתוב ולהשתמש בפונקציית עזר יעילה `int hasUniqueLetters(const char* str)` שבודקת האם המחרוזת מכילה רק אותיות והאם כל האותיות במחרוזת שונות. הפונקציה תחזיר 1 אם שני התנאים מתקיימים ו-0 אחרת.
אפשר להשתמש במערך עזר.
במידה ויהיה צורך בהקצאת זיכרון דינאמי, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3_SOL = r"""```c
void reverseString(char* str)
{
       int i = 0, j = strlen(str) - 1;
       char temp;
       for (; i < j; i++, j--)
       {
              temp = str[i];
              str[i] = str[j];
              str[j] = temp;
       }
}

int hasUniqueLetters(const char* str)
{
       char temp[26] = { 0 }; //counters of 26 english letters
       int i, index;
       for (i = 0; str[i] != '\0'; i++)
       {
              if (!isalpha(str[i]))
                     return 0;
              index = tolower(str[i]) - 'a';
              if (temp[index] > 0)
                     return 0;
              temp[index]++;
       }
       return 1;
}

void processFiles(const char* inputFilename, const char* outputFilename)
{
       char str[101];
       FILE* fin = fopen(inputFilename, "r"), *fout = fopen(outputFilename, "w");
       if (!fin || !fout)
              exit(1);
       while (fgets(str, 101, fin)) //together with '\n' and '\0': 99+1+1=101
       {
              str[strlen(str) - 1] = '\0'; //removing '\n'
              if (hasUniqueLetters(str))
              {
                     reverseString(str);
                     fprintf(fout, "%s\n", str);
              } //if
       }  //while
       fclose(fin);
       fclose(fout);
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
int* fun(int *);
void main()
{
    int x, y;
    x = *fun(&y);
    printf("%d %d\n", x, y);
    x = ++(*fun(&y));
    printf("%d %d\n", x, y);
    y = ++(*fun(&x));
    printf("%d %d\n", x, y);
    x = ++(*fun(&x));
    printf("%d %d\n", x, y);
    y = ++(*fun(&y));
    printf("%d %d\n", x, y);
}
int* fun(int* q)
{
    static int x = 1;
    int y = 1;
    x++;
    y++;
    *q = y;
    return &x;
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
2 2
4 2
2 6
8 6
8 10
```
**נימוק:**
**הקריאה הראשונה ל-`fun`.** `x` ו-`y` של הפונקציה מאותחלים ב-1 ומתקדמים ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. `x` ב-`main` מקבל ערך 2 של `static x` שנמצא בכתובת המוחזרת. לכן הפלט:
`2 2`
**הקריאה השנייה ל-`fun`.** `static x` זוכר את ערכו 2 ומתקדם ל-3. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-4 ב-`main` וערך זה הוכנס ל-`x` של `main`. לכן הפלט:
`4 2`
**הקריאה השלישית ל-`fun`.** `static x` זוכר את ערכו 4 ומתקדם ל-5. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`x` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-6 ב-`main` וערך זה הוכנס ל-`y` של `main`. לכן הפלט:
`2 6`
**הקריאה הרביעית ל-`fun`.** `static x` זוכר את ערכו 6 ומתקדם ל-7. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`x` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-8 ב-`main` וערך זה הוכנס ל-`x` של `main`. `y` של `main` נישאר 6 ללא שינוי. לכן הפלט:
`8 6`
**הקריאה החמישית ל-`fun`.** `static x` זוכר את ערכו 8 ומתקדם ל-9. `y` של הפונקציה שוב מאותחל ב-1 ומתקדם ל-2. הפונקציה מעבירה ערך 2 של `y` שלה ל-`y` של `main` ומחזירה כתובת של `x` שלה. המשתנה שבכתובת (ז"א `static x` של הפונקציה) מתקדם ל-10 ב-`main` וערך זה הוכנס ל-`y` של `main`. `x` של `main` נישאר 8 ללא שינוי. לכן הפלט:
`8 10`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + r"""נתונה ההצהרה הבאה:
```c
struct a { int b, c; } d;
```
מהו `d`?"""
Q5A_OPTS = opts("שם הפונקציה", "שם הטיפוס", "שם השדה", "שם המשתנה", "אף תשובה אינה נכונה")
Q5A_EXPL = "כאן מוגדר מבנה `a` בעל שדות `b` ו-`c` ומיד מוצהר משתנה `d` מטיפוס `struct a` המוגדר."

Q5B_TEXT = Q5_INTRO + r"""נתון פוינטר ל-`int` בשם `p`. בחרו מה יקרה אחרי ביצוע הפעולה
```c
p = (int*)realloc(NULL, sizeof(int));
```"""
Q5B_OPTS = opts("יוקצה בית אחד", "`p` יהיה שווה ל-`NULL`", "יוקצה משתנה אחד מסוג `int`",
                "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q5B_EXPL = "אם הפרמטר הראשון (המצביע) של `realloc` שווה ל-`NULL`, הקריאה שקולה לקריאה ל-`malloc`. לכן מקצים פה מקום למשתנה אחד מסוג `int`."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
    printf("%d", (int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1));
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `-1`

**נימוק:**
נתחיל מהביטוי הפנימי ביותר.
`( 1 << 1 )` = `10` בבינארי = 2
`( 1 << (1 << 1) )` = `1<<2` = `100` בבינארי = 4
`( (1 << (1 << 1)) + 1 )` = 4+1 = 5
`( 1 << ((1 << (1 << 1)) + 1) )` = `1<<5` = `100000` בבינארי = 32
`( (long long)1 << (1 << ((1 << (1 << 1)) + 1)) )` = `(long long)1 << 32` = 2^32 (64 סיביות)
`( ((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1 )` = 2^32 - 1 (64 סיביות)
`(int)(((long long)1 << (1 << ((1 << (1 << 1)) + 1))) - 1)` = `(int)(2^32 - 1)` = `111…1` בבינארי (32 סיביות)
התוצאה היא ייצוג בינארי של -1."""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/24B-B-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40, image="images/exams/24B-B-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    Q(4, "code", "storage_classes", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "structs_unions", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "d", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "dynamic_memory", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "c", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "bit_manipulation", Q6_TEXT, Q6_SOL, points=10),
]

exam = {
    "examCode": "24B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ד, מועד ב'",
    "year": 2024,
    "examDate": "30.07.2024",
    "sourceFile": "24B-B exam",
    "solutionFile": "24B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
