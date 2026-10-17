# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-B.json -- programming-workshop (C), semester B 2020, moed B (02.08.2020).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of three). Part 2: Q4 (20 pts, four pick-and-justify items).
Part 3: bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + yellow-marked options).
Code solutions compiled and run with clang: tools/verify/20B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_20B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CHOOSE = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש.*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר מחרוזת כ-**"ממוינת בקבוצות"** אם האותיות הקטנות שבתוכה, האותיות הגדולות שבתוכה, וגם הספרות שבתוכה ממוינות בסדר עולה (לא ממש) מתחילת המחרוזת עד לסופה, לפי קודי ASCII שלהן. מדובר רק על סדר התווים בתוך כל אחת מקבוצות התווים. לא משנה כיצד התווים מהקבוצות השונות ממוקמים יחסית זה לזה. מיקום התווים שאינם שייכים לאף אחת מהקבוצות לא משנה.

**לדוגמא,**
המחרוזת (משמאל לימין) היא ממוינת בקבוצות:
```
"B4$Ca#%ds5P8P&9zY"
```
המחרוזת (משמאל לימין) היא אינה ממוינת בקבוצות (קוד `'s'` הוא גדול מקוד `'r'`):
```
"B4$Ca#%ds5P8P&9rY"
```

כתוב פונקציה אשר מקבלת מחרוזת ומחזירה `1` אם המחרוזת ממוינת בקבוצות ו-`0` אחרת.""" + CHOOSE

Q1_SOL = r"""```c
int group_sort(char *str)
{
    char last_capital, last_small, last_digit;
    int i;
    last_capital = last_small = last_digit = '\0';
    for (i = 0; str[i] != '\0'; i++)
        if (isupper(str[i]))
            if (str[i] < last_capital)
                return 0;
            else
                last_capital = str[i];
        else
            if (islower(str[i]))
                if (str[i] < last_small)
                    return 0;
                else
                    last_small = str[i];
            else
                if (isdigit(str[i]))
                    if (str[i] < last_digit)
                        return 0;
                    else
                        last_digit = str[i];
    return 1;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item
{
  int data;
  struct item *next;
} Item;
```
נאמר שרשימה מקושרת $L_1$ בעלת $n_1$ איברים מסוג `Item` היא **תחילית (prefix)** של רשימה מקושרת $L_2$ בעלת $n_2$ איברים מסוג `Item` אם $n_1 \le n_2$ ושדה `data` של איבר שנמצא במקום `i` מתחילת $L_1$ ($0 \le i < n_1$) שווה לשדה `data` של איבר שנמצא במקום `i` מתחילת $L_2$. רשימה ריקה היא תחילית של כל רשימה.

כתוב פונקציה אשר מקבלת מערך `A` של רשימות מקושרות עם גודלו וגם רשימה מקושרת נפרדת `L`. כל הרשימות מורכבות מאיברים מסוג `Item`.
על הפונקציה לגלות את כל רשימות במערך `A` ש-`L` היא תחילית שלהן. יש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג `Item`) שתכיל את האינדקסים במערך `A` של כל רשימות במערך בהם `L` היא תחילית. אין חשיבות לסדר האיברים ברשימה החדשה.
הפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר `NULL`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.

**דוגמא:** (באיור: המערך `A`, הרשימה `L` והרשימה החדשה)""" + CHOOSE

Q2_SOL = r"""```c
//Auxiliary function - checks whether L1 is prefix of L2
int is_prefix(Item *L1, Item *L2)
{
    while (L1 && L2)
    {
        if (L1->data != L2->data)
            return 0;
        L1 = L1->next;
        L2 = L2->next;
    }
    if (L1)
        return 0;
    return 1;
}

//Auxiliary function
void insert_in_head(int x, Item **pl)
{
    Item *temp = (Item *)malloc(sizeof(Item));
    temp->data = x;
    temp->next = *pl;
    *pl = temp;
}

Item *arr_of_lists_to_list_of_prefixes(Item **A, int n, Item *L)
{
    int i;
    Item *pref_list = NULL;
    for (i = n - 1; i >= 0; i--)
        if (is_prefix(L, A[i]))
            insert_in_head(i, &pref_list);
    return pref_list;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**מטריצה דלילה** הינה מטריצה שמרבית איבריה בעלי ערך אפס.

כתוב פונקציה (`void`) אשר מקבלת **מערך דו-ממדי סטטי** (לא דינאמי) `A` של מספרים שלמים בעל `rows` שורות ו-`cols` עמודות, וגם מחרוזת `fileName`.
המספר הפיסי של העמודות יינתן ע"י קבוע בשם `COLS`. יש להגדיר אותו לפני הפונקציה.

מחרוזת `fileName` תהווה שם של **קובץ טקסט** ששומר מטריצה דלילה בעלת `rows` שורות ו-`cols` עמודות בדרך חסכונית באמצעות אחסון רק איברי המטריצה שאינם בעלי ערך אפס.
הקובץ מכיל `rows` שורות. שורה מס' `i` בקובץ מתאימה לשורה מס' `i` של המטריצה (השורות ממוספרות מ-0). בתחילת כל שורה נמצא מספרה.
כל איבר של המטריצה ששונה מאפס מוצג בקובץ כזוג המספרים: ערך של האיבר ומס' עמודה בה הוא נמצא במטריצה.
המספרים הסמוכים בכל שורה מופרדים ברווח אחד. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה לשחזר את המטריצה כמערך `A`. יש למלא את `A` בהתאם.

**דוגמא:**
המטריצה:
```
0 0 4 0 7
3 0 0 0 0
9 1 0 6 0
0 0 0 0 0
```
תוכן הקובץ:
```
0 4 2 7 4
1 3 0
2 9 0 1 1 6 3
3
```""" + CHOOSE

Q3_SOL = r"""```c
#define COLS 5 //example

void file_to_sparse_matrix(char *filename, int A[][COLS], int
rows, int cols)
{
    int i, j, num;
    char ch;
    FILE *fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            A[i][j] = 0;
    for (i = 0; i < rows; i++)
    {
        fscanf(fptr,"%d", &num); //number of row
        while ((ch = fgetc(fptr)) != '\n')
        {
            fscanf(fptr, "%d%d", &num, &j);
            A[i][j] = num;
        }
    }
    fclose(fptr);
}
```"""

# ---------------------------------------------------------------- Q4 (american items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים. **התשובה הנכונה ללא נימוק או עם נימוק לא נכון תזכה רק בנקודה אחת.** \"לפי כללי שפת C\" הינו גם יכול להיות נימוק מקובל. (שאלה 4, 20 נק' בסך הכול.)\n"

Q4A_TEXT = Q4_INTRO + "מה לא מאותחל כברירת המחדל?"
Q4A_TEXT_FULL = Q4_INTRO + r"""מה לא מאותחל כברירת המחדל?
(1) משתנה מסוג `static`
(2) משתנה גלובלי
(3) האיבר האחרון של מערך סטטי בו האיברים הראשונים מאותחלים באופן מפורש בהצהרה
(4) איברי מערך דינאמי שהוקצה באמצעות פונקציית `calloc`
(5) התו האחרון במערך תווים סטטי
(6) סמן המיקום הנוכחי בקובץ ברגע פתיחתו
(7) כל הנתונים שניתנו כאן מאותחלים כברירת המחדל"""
Q4A_SOL = r"""**התשובה:** (5) התו האחרון במערך תווים סטטי

**נימוק:**
כברירת המחדל: משתנים `static` וגלובלי מאותחלים ב-0, איברים אחרונים במערך סטטי מאותחלים ב-0 אם איברים ראשונים מאותחלים במפורש, איברי מערך דינאמי שהוקצה באמצעות `calloc` מאותחלים ב-0, המיקום הנוכחי בקובץ הוא תחילת הקובץ בפתיחה לקריאה או לכתיבה וסוף הקובץ בפתיחה להוספה.
במקרה הכללי אף איבר של מערך סטטי לא מאותחל כברירת המחדל."""

Q4B_TEXT = Q4_INTRO + "מה קורה בצד שמאל של מספר `unsigned` לאחר ביצוע פעולת הזזת סיביות ימינה בתוכו?"
Q4B_OPTS = opts("מצד שמאל המספר מתמלא ב-0-ים", "מצד שמאל המספר מתמלא ב-1-ים",
                "מצד שמאל המספר מתמלא בסיביות שהלכו לאיבוד מצד ימין", "שיטת מילוי המספר מצד שמאל תלויה במערכת",
                "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C."

Q4C_TEXT = Q4_INTRO + "מהו `\"abcd\" - \"xyz\"` ?"
Q4C_OPTS = opts("מחרוזת", "כתובת", "מספר שלם", "הפעולה היא בלתי חוקית מבחינת המהדר", "אף תשובה אינה נכונה")
Q4C_EXPL = "מחרוזת כבועה במשפט היא כתובת של התו הראשון שלה. לפי כללי אריתמטיקת מצביעים הפרש הכתובות זה מספר שלם."

Q4D_TEXT = Q4_INTRO + r"""נניח שבן-אדם פותח קובץ בינארי באמצעות עורך טקסט. מהי הטענה הנכונה לגבי נתונים הנשמרים בקובץ?
* "לא ניתן לקריאה על ידי בני אדם" פירושו: אדם יראה ג'יבריש ("קשקוש").
* "ניתן לקריאה על ידי בני אדם" פירושו: אדם יוכל לראות את הערך שבו מדובר ולא ג'יבריש."""
Q4D_OPTS = opts("מספרים שלמים ניתנים לקריאה ע\"י בן-אדם כאשר תווים לא ניתנים לקריאה ע\"י בן-אדם",
                "מספרים שלמים לא ניתנים לקריאה ע\"י בן-אדם כאשר תווים ניתנים לקריאה ע\"י בן-אדם",
                "גם מספרים שלמים וגם תווים לא ניתנים לקריאה ע\"י בן-אדם",
                "גם מספרים שלמים וגם תווים ניתנים לקריאה ע\"י בן-אדם אם רק מספרים שלמים או רק תווים נשמרים בקובץ אולם הם לא ניתנים לקריאה אם מופיעים בקובץ ביחד",
                "גם מספרים שלמים וגם תווים תמיד ניתנים לקריאה ע\"י בן-אדם")
Q4D_EXPL = "קובץ בינארי הוא רצף בתים (כמו בזיכרון פנימי). מצד שני תו זה בית אחד ולכן כל בית מופיע כתו. אזי בן-אדם יראה את התווים כמו שהם אבל מספרים יראה כקשקוש."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <string.h>
#include <math.h>

void main()
{
      int n = strlen("\\\\"), m = strlen("\n\n\0\n"), k =
strlen("////");
      char *s = "Ah!", *x = s + m;
      puts( (char *)( (long long)(pow((int)x, n) - k) / (int)(x + m) )
);
}
```
חובה לנמק את התשובה! התשובה ללא נימוק או עם נימוק לא נכון לא תזכה בנקודות."""

Q5_SOL = r"""**הפלט:**
```
Ah!
```
**נימוק:**
סדרת escape שהתו הראשון שלה הוא `'\'` מציגה לא את עצמה אלא איזה תו אחר. במיוחד `'\n'` זה תו של סוף השורה, `'\0'` זה תו של סוף המחרוזת, `'\\'` זה תו `'\'` עצמו. לכן מחרוזת `"\\\\"` מורכבת מ-2 תווים ואורכה הוא 2.
ב-`"\n\n\0\n"` יש שני תווים עד לסוף המחרוזת ואורכה 2. מחרוזת `"////"` מורכבת מתווים רגילים ואורכה 4. אזי `n=2`, `m=2`, `k=4` ו-`x=s+2`.
Casting ל-`long long` ול-`int` ממיר כתובת (ערך `x`) למספר שלם. `(x^2-4)/(x+2)=(x-2)(x+2)/(x+2)=x-2=s+2-2=s`
Casting ל-`char *` קובע ערך `s` ככתובת של התו הראשון במחרוזת. לכן `puts` מקבלת מחרוזת `s` ומדפיסה את התוכן שלה `"Ah!"`.

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הנימוק מניח שכתובת נכנסת ב-`int` (מערכת של 32 סיביות). בהרצה אמיתית (`tools/verify/20B-B/q5.c`) הקומפילציה ל-32 סיביות מדפיסה `Ah!`, ואילו בקומפילציה ל-64 סיביות ה-cast ל-`int` קוטם את הכתובת והתוכנית קורסת."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/20B-B-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    # Q4 a has seven printed options (an mcq holds at most six), so it is an open item with the options in the text
    Q(4, "code", "c_traps_mcq", Q4A_TEXT_FULL, Q4A_SOL, part="א"),
    M("ב", "bit_manipulation", Q4B_TEXT, Q4B_OPTS, "a", Q4B_EXPL),
    M("ג", "pointers", Q4C_TEXT, Q4C_OPTS, "c", Q4C_EXPL),
    M("ד", "files", Q4D_TEXT, Q4D_OPTS, "b", Q4D_EXPL),
    Q(5, "code", "c_basics_output", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "20B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תש\"ף, מועד ב'",
    "year": 2020,
    "examDate": "02.08.2020",
    "sourceFile": "20B-B exam",
    "solutionFile": "20B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
