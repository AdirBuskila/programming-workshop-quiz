# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-A.json -- programming-workshop (C), semester B 2023, moed A (08.06.2023).
Q1 (40), Q2/Q3 (40 each, answer one; Q3 = parts a 15 / b 15 / c 10), Q4 (10), Q5 a/b (10 total), Q6 bonus (10).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/23B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_23B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""בפולינום $P(x)=\sum_{i=0}^{n-1} a_i x^i$ כל איבר $a_i x^i$ ($a_i$ הוא מקדם ממשי) נקרא **מונום** $i$.

נגדיר מבנה הבא המייצג מונום:
```c
typedef struct monom {
        double coefficient;
        int power;
} Monom;
```
וגם נגדיר מבנה המייצג איבר ברשימה מקושרת:
```c
typedef struct item {
        Monom mon;
        struct item * next;
} Item;
```
כתבו פונקציה `Item * createPolynom(Item * L)` המקבלת רשימה מקושרת חד-כיוונית של איברים מטיפוס `Item`.
על הפונקציה ליצור ולהחזיר רשימה חדשה `P` (של איברים מטיפוס `Item`) המייצגת פולינום כך שאיברי הרשימה יהיו ממוינים לפי חזקות המונומים שהם מכילים (עבור $i < j$, מונום $j$ יהיה יותר קרוב לראש הרשימה מאשר מונום $i$). רשימת `P` תיווצר ע"י **סיכום המונומים** המרכיבים את `L`. ב-`P` לא יהיו מונומים עם מקדמים אפס. הרשימה הריקה (המקורית והחדשה) תייצג מספר 0.

**לדוגמא,** עבור הרשימה `L` הבאה (המספר השמאלי הוא מקדם והמספר הימני הוא חזקה): `(2,4) (-5,1) (3,6) (6,4) (-8,0) (-3,6) (7.5,3)` הפונקציה תיצור את הרשימה `P` הבאה: `(8,4) (7.5,3) (-5,1) (-8,0)` אשר מייצגת את הפולינום `8x^4+7.5x^3-5x-8`.

**שימו לב.** כדי לייעל את העיבוד של הרשימה המקורית יש להשתמש במערך עזר שגודלו תלוי בחזקה המקסימלית ברשימה הזאת. **זוהי דרישה מחייבת!**

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q1_SOL = r"""```c
Item* createPolynom(Item* L)
{
       Item* curr = L, * P = NULL;
       int max_power = 0, power;
       double *arr;

       /* Search of maximum power */
       while (curr)
       {
              if (curr->mon.power > max_power)
                     max_power = curr->mon.power;
              curr = curr->next;
       }

       /* Calculation of coefficients */
       arr = (double*)calloc(max_power + 1, sizeof(double));
       curr = L;
       while (curr)
       {
              arr[curr->mon.power] += curr->mon.coefficient;
              curr = curr->next;
       }

       /* Creation of polynomial list */
       curr = L;
       for (power = 0; power <= max_power; power++)
              if (arr[power] != 0)
              {
                     curr = (Item*)malloc(sizeof(Item));
                     curr->next = P;
                     P = curr;
                     P->mon.coefficient = arr[power];
                     P->mon.power = power;
              }

       free(arr);
       return P;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**שימו לב:** בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).

כתבו פונקציה **יעילה** בשם `sortedRowsCols` המקבלת מערך דו-ממדי דינאמי `ar` של מספרים שלמים בעל `m` שורות ו-`n` עמודות.
על הפונקציה ליצור שני מערכים חד-ממדיים. אחד מהם (בשם `ar_s_rows`) יהיה מורכב ממספרי השורות במערך הדו-ממדי ממוינות בסדר עולה ממש והשני (בשם `ar_s_cols`) יהיה מורכב ממספרי העמודות ממוינות בסדר יורד ממש.
הפונקציה תעביר by reference את המערכים החדשים ואת הגדלים שלהם. במידה ומערך נוצר ריק, הפונקציה תעביר `NULL` ככתובתו ו-0 כגודלו.

**לדוגמא:** עבור המערך `ar` (משמאל לימין, מלמעלה למטה)
```
10  13  56  99
23  57  59  93
36  19  74  89
30  75  80  85
25  73  84  84
```
הפונקציה תעביר מערך `ar_s_rows`: `{0,1,3}` עם גודלו 3 ומערך `ar_s_cols`: `{3}` עם גודלו 1.

החתימה של הפונקציה `sortedRowsCols` תהיה:
```c
void sortedRowsCols(int **ar, int m, int n,
int **ar_s_rows, int *num_s_rows, int **ar_s_cols, int *num_s_cols)
```
לבדיקה האם השורה ממוינת יש להשתמש בפונקציית עזר `int arrSorted(int *a, int n)` המקבלת את השורה כמערך `a` בגודל `n`. הפונקציה תחזיר 1 אם המערך ממוין בסדר עולה ממש ו-0 אחרת.
לבדיקה האם העמודה ממוינת יש להשתמש בפונקציית עזר `columnSorted`. הפונקציה תקבל מערך דו-ממדי `ar`, מספר שורותיו `m`, ומספר העמודה הנבדקת `col`. על הפונקציה להחזיר 1 אם העמודה ממוינת בסדר יורד ממש ו-0 אחרת. חתימת הפונקציה תהיה `int columnSorted(int **ar, int m, int col)`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q2_SOL = r"""```c
int arrSorted(int* a, int n)
{
       int i;
       for (i = 1; i < n; i++)
              if (a[i] <= a[i - 1])
                     return 0;
       return 1;
}

int columnSorted(int** ar, int m, int col)
{
       int i;
       for (i = 1; i < m; i++)
              if (ar[i][col] >= ar[i - 1][col])
                     return 0;
       return 1;
}

void sortedRowsCols(int** ar, int m, int n, int** ar_s_rows, int* num_s_rows, int** ar_s_cols, int* num_s_cols)
{
       int i, j;
       *num_s_rows = *num_s_cols = 0;
       *ar_s_rows = (int*)calloc(m, sizeof(int)); // max size - number of rows
       *ar_s_cols = (int*)calloc(n, sizeof(int)); // max size - number of columns
       for (i = 0; i < m; i++)
              if (arrSorted(ar[i], n))
                     (*ar_s_rows)[(*num_s_rows)++] = i;
       for (j = 0; j < n; j++)
              if (columnSorted(ar, m, j))
                     (*ar_s_cols)[(*num_s_cols)++] = j;
       *ar_s_rows = (int*)realloc(*ar_s_rows, *num_s_rows * sizeof(int));
       *ar_s_cols = (int*)realloc(*ar_s_cols, *num_s_cols * sizeof(int));
}
```"""

# ---------------------------------------------------------------- Q3
Q3_INTRO = r"""**שימו לב:** שאלה זו היא חלופה לשאלה 2 (יש לענות על שאלה אחת מתוך שתיים).

נגדיר כמה תווים מסוימים כ**מפרידים**. במיוחד, תווי פסיק, נקודה, רווח, סימן קריאה, סימן שאלה, נקודתיים וכו' ניתן להגדיר כמפרידים. **מילה** היא רצף של תווים שאינם מפרידים. **משפט** הוא מחרוזת המכילה שרשור של מילים ומפרידים. המילים יכולות להיות מופרדות ע"י מפריד אחד או יותר. משפט לא ריק תמיד מתחיל במילה.

בכל השאלות הבאות אסור להשתמש בפונקציה סטנדרטית `strtok`."""

Q3A_TEXT = r"""**סעיף א (15 נק').**
כתבו פונקציה עם החתימה `char * nextWord(char * sentence, char * separators, char * word)` אשר מקבלת מחרוזת `sentence` המהווה את המשפט ומחרוזת `separators` המורכבת מכל המפרידים שעשויים להופיע במשפט.
על הפונקציה לעדכן את `word` להיות המחרוזת המכילה העתק של המילה הראשונה ב-`sentence` המוגדרת עד למפריד הראשון (ניתן להניח שגודל של מערך `word` יהיה מספיק).
הפונקציה תחזיר מצביע לתחילת המילה הבאה ב-`sentence` או `NULL` אם המשפט לא מכיל מילים נוספות.

לדוגמא: עבור `sentence = "Why?! That's why."` ו-`separators = "? !."` תוכן של `word` יהיה `"Why"` והפונקציה תחזיר מצביע לתת-מחרוזת `"That's why."` מתוך `sentence`."""

Q3A_SOL = r"""```c
char* nextWord(char* sentence, char* separators, char* word)
{
       int i = 0;
       while ( sentence[i] && !strchr(separators, sentence[i]) ) // scan word
              word[i++] = sentence[i];
       word[i] = '\0';
       while (sentence[i] && strchr(separators, sentence[i])) // scan separators
              i++;
       return sentence[i] ? sentence + i : NULL;
}
```"""

Q3B_TEXT = r"""**סעיף ב (15 נק').**
כתבו פונקציה עם החתימה `int breakSentence(char * sentence, char * separators, char * file_name)` אשר מקבלת אותן מחרוזות `sentence` ו-`separators` שבסעיף א' וגם מחרוזת `file_name` המהווה שם של קובץ טקסט.
על הפונקציה לשמור את המילים של המשפט בקובץ שנוצר (כל מילה בשורה נפרדת) ולהחזיר את כמות המילים במשפט.

לדוגמא: עבור `sentence = "But why?! That's why."` ו-`separators = "? !."` הפונקציה תחזיר 4 ותוכן הקובץ יהיה
```
But
why
That's
why
```
יש להשתמש בפונקציה `nextWord` כפונקציית עזר.
אפשר להשתמש במערך עזר. במקרה זה, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3B_SOL = r"""```c
int breakSentence(char* sentence, char* separators, char* file_name)
{
       FILE* fptr = fopen(file_name, "w");
       char* word;
       int count = 0;
       if (!fptr)
              return -1;
       word = (char*)malloc(strlen(sentence) + 1);
       while ( (sentence = nextWord(sentence, separators, word)) != NULL )
       {
              fprintf(fptr, "%s\n", word);
              count++;
       }
       if (*word) // sentence isn't empty
       {
              fprintf(fptr, "%s\n", word); // last word
              count++;
       }
       free(word);
       fclose(fptr);
       return count;
}
```"""

Q3C_TEXT = r"""**סעיף ג (10 נק').**
כתבו פונקציה עם החתימה `int countWordOccur(char * sentence, char * separators, char * query)` אשר מקבלת אותן מחרוזות `sentence` ו-`separators` שבסעיף א' וגם מחרוזת `query` המהווה מילה כלשהי.
על הפונקציה להחזיר את כמות המופעים של המילה `query` ב-`sentence`.

לדוגמא, עבור `sentence = "But why?! That's why. And don't ask me why."`, `separators = "? !."` ו-`query = "why"` הפונקציה תחזיר 3.
יש להשתמש בפונקציה `nextWord` כפונקציית עזר.
אפשר להשתמש במערך עזר. במקרה זה, ניתן להניח שיש בזיכרון מספיק מקום להקצאה."""

Q3C_SOL = r"""```c
int countWordOccur(char* sentence, char* separators, char* query)
{
       char* word;
       int count = 0;
       word = (char*)malloc(strlen(sentence) + 1);
       while ( (sentence = nextWord(sentence, separators, word)) != NULL )
              if (strcmp(word, query) == 0)
                     count++;
       if (strcmp(word, query) == 0) // last word
              count++;
       free(word);
       return count;
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
int x = 30, y = 0;
void f1(int x)
{
    printf("x=%d,y=%d\n", x, y);
    x = y = 10;
}
void f2(int y)
{
    printf("x=%d,y=%d\n", x, y);
    x = y = 15;
}
int main()
{
    y = 5;
    f1(20);
    f2(y);
    printf("x=%d,y=%d\n", x, y);
    return 0;
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
x=20,y=5
x=30,y=10
x=15,y=10
```
**נימוק:**
אין משתנים `x,y` ב-`main`. לכן ב-`main` עובדים עם משתנים גלובליים. `y` שמאותחל ב-0 יקבל ערך חדש 5.
אחרי קריאה ל-`f1(20)` פרמטר פורמלי `x` של `f1` יקבל ערך 20. אין משתנה `y` ב-`f1` ולכן הפונקציה עובדת עם `y` גלובלי אשר שווה ל-5. לכן `printf` ב-`f1` מדפיסה
`x=20,y=5`
לאחר מכן `x` פורמלי ו-`y` גלובלי משתנים ב-10.
אחרי קריאה ל-`f2(y)` פרמטר פורמלי `y` של `f2` יקבל ערך 10 של `y` גלובלי. אין משתנה `x` ב-`f2` ולכן הפונקציה עובדת עם `x` גלובלי אשר מאותחל ב-30. לכן `printf` ב-`f2` מדפיסה
`x=30,y=10`
לאחר מכן `x` גלובלי ו-`y` פורמלי משתנים ב-15.
ואז לאחר חזרה ל-`main`, `x` גלובלי שווה ל-15 ו-`y` גלובלי שווה ל-10. לכן `printf` ב-`main` מדפיסה
`x=15,y=10`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + "מהי הטענה הנכונה?"
Q5A_OPTS = opts(r'הקריאות `puts("abc")` ו-`fputs("abc",stdout)` הן שקולות',
                r'הקריאות `puts("abc")` ו-`fputs("abc\n",stdout)` הן שקולות',
                r'הקריאות `puts("abc\n")` ו-`fputs("abc",stdout)` הן שקולות',
                r'הקריאות `puts("abc")` ו-`fputs("\nabc",stdout)` הן שקולות',
                "אף טענה אינה נכונה")
Q5A_EXPL = r"""לעומת `puts`, `fputs` לא מוסיפה `'\n'` בסוף המחרוזת. לכן `fputs("abc",stdout)` מציגה במסך `abc` ללא הורדת שורה. בזאת `fputs("abc\n",stdout)` מציגה במסך `abc` ומורידה סמן לשורה הבאה, בדיוק כמו `puts("abc")`."""

Q5B_TEXT = Q5_INTRO + "איזה פעולה היא בלתי חוקית?"
Q5B_OPTS = opts("חיבור של מספר שלם למצביע",
                "חיסור של מספר שלם ממצביע",
                "חיבור של מצביע למצביע",
                "חיסור של מצביע ממצביע",
                "השוואת מצביעים",
                "כל הפעולות לעיל הן חוקיות")
Q5B_EXPL = "בשפת C מוגדרות הפעולות הבאות על מצביעים: חיבור (חיסור) מספר שלם למצביע (התוצאה היא כתובת), חיסור מצביעים (התוצאה היא מספר שלם), השוואת מצביעים. פעולת חיבור מצביעים לא מוגדרת."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <string.h>
void main()
{
    puts("puts"-strlen("strlen")+sizeof"sizeof");
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `uts`

**נימוק:**
הפונקציה `strlen` מחזירה מספר תווים במחרוזת עד לתו אפסי לא כולל תו אפסי. לכן `strlen("strlen")` מחזירה 6.
אופרטור `sizeof` מחזיר את גודל האופרנד בבתים. מחרוזת `"sizeof"` מהווה 7 תווים כולל תו אפסי. לכן `sizeof"sizeof"` מחזיר 7.
ואז המשפט שקול ל-`puts("puts"-6+7)` ז"א ל-`puts("puts"+1)`.
למחרוזת קבועה במשפט צריך להתייחס כמו לכתובת התו הראשון שלה. בזאת מקבלים למעשה `puts("uts")`. לכן הפלט יהיה
`uts`"""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/23B-A-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "strings", Q3A_TEXT, Q3A_SOL, points=15, part="א", contextId="c1"),
    Q(3, "code", "files", Q3B_TEXT, Q3B_SOL, points=15, part="ב", contextId="c1"),
    Q(3, "code", "strings", Q3C_TEXT, Q3C_SOL, points=10, part="ג", contextId="c1"),
    Q(4, "code", "storage_classes", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "files", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "b", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "pointers", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "c", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "c_traps_mcq", Q6_TEXT, Q6_SOL, points=10),
]

exam = {
    "examCode": "23B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ג, מועד א'",
    "year": 2023,
    "examDate": "08.06.2023",
    "sourceFile": "23B-A exam",
    "solutionFile": "23B-A official solution",
    "contexts": {"c1": {"kind": "text", "title": "שאלה 3 - הגדרות", "text": Q3_INTRO}},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
