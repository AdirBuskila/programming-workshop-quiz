# -*- coding: utf-8 -*-
"""Generator for tools/raw/25B-B.json -- programming-workshop (C), semester B 2025, moed B (29.07.2025).
Flagship sitting. Q1, Q2, Q3 (40 pts each; Q2/Q3 choose one), Q4, Q5 a/b (10 pts), Q6 bonus (10 pts).
Solutions transcribed from the official solution PDF (typed). Code solutions compiled and run with clang:
tools/verify/25B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_25B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "25B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item
{
  int data;
  struct item *next;
} Item;
```
כתבו פונקציה `Item *lists_with_given_elements(Item **A, int n, Item *L)` אשר מקבלת מערך `A` של רשימות מקושרות עם גודלו `n` וגם רשימה מקושרת נפרדת `L`. כל הרשימות מורכבות מאיברים מסוג `Item`. שדות `data` של איברי `L` שונים זה מזה.
על הפונקציה לגלות את כל הרשימות במערך `A` שמכילות בתוכן את כל האיברים שמופיעים גם ב-`L`.
יש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג `Item`) שתכיל את האינדקסים במערך `A` של כל הרשימות במערך שהן עומדות בדרישה הנ"ל. אין חשיבות לסדר האיברים ברשימה החדשה.
הפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר `NULL`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.

**דוגמא:** באיור, הרשימות במערך `A` הן (לפי אינדקס) `0: 2,6,5,1,8`, `1: 8,3,5`, `2: 5`, `3: 1,2,8,5,3`, `4: 8,5,2,8`, והרשימה `L` היא `8,2,5`. הרשימות שמכילות את כל איברי `L` הן באינדקסים 0, 3 ו-4, ולכן הרשימה החדשה היא `0,3,4`."""

Q1_SOL = r"""```c
//Auxiliary function - checks whether all elements of L1 are in L2
int List1_elements_in_List2(Item* L1, Item* L2)
{
    Item* ptr1 = L1, * ptr2 = L2;
    int found;

    /* whether L2 is not shorter L1*/
    while (ptr1 && ptr2)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    if (ptr1 && !ptr2)
        return 0;
    /*---------------------------------*/
    /* searching each element of L1 in L2 */
    ptr1 = L1;
    while (ptr1)
    {
        found = 0;
        ptr2 = L2;
        while (ptr2)
        {
            if (ptr1->data == ptr2->data)
            {
                found = 1;
                break;
            }
            ptr2 = ptr2->next;
        } // while (ptr2)
        if (!found)
            return 0;
        ptr1 = ptr1->next;
    } // while (ptr1)
    /*---------------------------------*/
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

Item *lists_with_given_elements(Item** A, int n, Item* L)
{
    int i;
    Item *ind_list = NULL;
    for (i = n - 1; i >= 0; i--)
        if (List1_elements_in_List2(L, A[i]))
            insert_in_head(i, &ind_list);
    return ind_list;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**האלכסון הראשי** של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית העליונה של המטריצה עד לפינה הימנית התחתונה.
כל איברי המטריצה הריבועית הנמצאים מתחת לאלכסון הראשי שלה מרכיבים את **המשולש התחתון ממש** של המטריצה.
כל איברי המטריצה הריבועית הנמצאים מעל האלכסון הראשי שלה מרכיבים את **המשולש העליון ממש** של המטריצה.

כתבו פונקציה `int **triangles_to_matrix(int **tr_low, int **tr_up, int n)` אשר מקבלת שני **מערכים דו-ממדיים דינאמיים** של מספרים שלמים (בעלי `n` שורות בגדלים שונים) המיישמים את המשולש התחתון ממש ואת המשולש העליון ממש בהתאמה.
על הפונקציה ליצור מטריצה ריבועית בגודל `(n+1)×(n+1)` המבוססת על שני המשולשים הנ"ל בה איברי האלכסון הראשי שווים ל-0. המטריצה מיושמת כ**מערך דו-ממדי דינאמי**. הפונקציה תחזיר את כתובת המערך.

**דוגמא:**
המטריצה:
```
 0   7  -3  13
76   0   8  42
98   4   0  60
11  19  21   0
```
המשולש העליון:
```
7  -3  13
    8  42
       60
```
המשולש התחתון:
```
76
98   4
11  19  21
```
גדלי השורות במערכים שהפונקציה מקבלת שווים לכמויות האיברים בשורות המתאימות של המשולשים. המשולש התחתון מוצג בזיכרון בצורתו הטבעית. שורות המשולש העליון בזיכרון מוזזות שמאלה בהשוואה לייצוג הטבעי שלהן.

למשל, המשולש התחתון והמשולש העליון של הדוגמא לעיל יוצגו בזיכרון באופן הבא (באיור).

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.

*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*"""

Q2_SOL = r"""```c
int** triangles_to_matrix(int** tr_low, int** tr_up, int n)
{
    int i, j, ** A;

    A = (int**)calloc(n + 1, sizeof(int*));
    for (i = 0; i < n + 1; i++)
        A[i] = (int*)calloc(n + 1, sizeof(int));

    /* lower triangle */
    for (i = 1; i < n + 1; i++)
        for (j = 0; j < i; j++)
            A[i][j] = tr_low[i - 1][j];

    /* upper triangle */
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n + 1; j++)
            A[i][j] = tr_up[i][j - i - 1];

    return A;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתבו פונקציה `void text_to_binary(char *text_name, char *binary_name)` אשר מקבלת מחרוזות `text_name` ו-`binary_name` המהוות שמות של **קובץ טקסט** ושל **קובץ בינארי** בהתאמה.

תוכן **קובץ הטקסט** מורכב משורות. בכל שורה נמצא מידע עבור לקוח בייצוג הבא:
- מס' ת.ז. (9 תווים),
- שם לקוח (30 תווים),
- סכום סה"כ קניות (מספר מסוג `double` שתופס 8 עמודות).

**דוגמא:**
```
06842151          Moshe    71.25
330578795      Benjamin  1755.65
20051546           Dina   560.10
```
על הפונקציה ליצור **קובץ בינארי** בעל אותו מידע שיש ב**קובץ הטקסט**. כל שורה של **קובץ הטקסט** תהפוך לרשומה ב**קובץ הבינארי**. הפורמט של כל רשומה יהיה מתאים למבנה `clientData` הבא:
```c
typedef struct {
    char id[10];
    char name[31];
    double total;
} clientData;
```
כך ש-
- `id` - מס' ת.ז.,
- `name` - שם לקוח,
- `total` - סכום סה"כ קניות.

**שימו לב:** פונקציה `fscanf` אשר ניתן להשתמש במהלך סריקת **קובץ הטקסט** מתעלמת מהרווחים השמאליים של המחרוזת הנקלטת ומתחילה את הקלט מהתו הראשון שאחריהם.

*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*"""

Q3_SOL = r"""```c
void text_to_binary(char* text_name, char* binary_name)
{
    clientData client;

    FILE* fin = fopen(text_name, "r");
    FILE* fout = fopen(binary_name, "w");
    if (!fin)  exit(1);
    if (!fout)  exit(1);

    fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);
    while (!feof(fin))
    {
        fwrite(&client, sizeof(clientData), 1, fout);
        fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);
    }

    fclose(fin);
    fclose(fout);
}
```

**הערת מתמלל (לא חלק מהפתרון הרשמי):** הפתרון הרשמי עובד על הדוגמה כאשר השורה האחרונה בקובץ מסתיימת בתו שורה חדשה. אם אין תו שורה חדשה אחרי השורה האחרונה, הקריאה האחרונה מגיעה ל-EOF כבר בקליטת `total`, ו-`feof` מחזיר אמת לפני כתיבת הרשומה האחרונה, כך שהיא אובדת. כמו כן הקובץ נפתח ב-`"w"` ולא ב-`"wb"`."""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

int y = 2;

void f1() {
    printf("1 ");
}

void f2() {
    printf("2 ");
}

void f3() {
    printf("3 ");
}

void f4() {
    int x = 0;
    static int y;
    void (*p[3])() = {f1, f2, f3};

    p[x]();
    p[y]();
    x++;
    y++;
}

void f5() {
    printf("%d ", y);
    y++;
}

void main() {
    int y;

    for (y = 5; y <= 7; y++) {
        f4();
        printf("\n");
    }
    f5();
    printf("%d\n", y);
    f5();
    printf("%d\n", y);
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
1 1
1 2
1 3
2 8
3 8
```
**נימוק:**
פונקציה `f4` בלולאה של `main` נקראת שלוש פעמים.
`p` ב-פונקציה `f4` הוא מערך של שלושה מצביעים לפונקציות אשר מאותחל לפונקציות `f1`, `f2`, `f3`.
משתנה `x` מאותחל ל-0. משתנה `y` הוא `static` ולכן ערך התחלתי שלו 0 כברירת מחדל.
לכן `p[x]` ו-`p[y]` הם גישות לאיבר `p[0]`, ז"א קריאות לפונקציה `f1()` אשר מדפיסה 1. לכן הפלט באיטרציה הראשונה הוא
`1 1`
בסוף הפונקציה `f4`, מתקדמים `x` ו-`y`. בקריאה השנייה ל-`f4`, משתנה `x` שוב מאותחל ל-0. משתנה `y` הוא `static` ולכן השינוי שלו נשמר. אזי ערכי `x` ו-`y` הם 0 ו-1 בהתאמה.
לכן `p[x]` ו-`p[y]` הם גישות לאיברי `p[0]` ו-`p[1]` בהתאמה, ז"א קריאות לפונקציה `f1()` אשר מדפיסה 1 ולפונקציה `f2()` אשר מדפיסה 2. אזי הפלט באיטרציה השנייה הוא
`1 2`
בסוף הפונקציה `f4`, `x` ו-`y` מתקדמים שוב. בקריאה השלישית ל-`f4`, משתנה `x` שוב מאותחל ל-0. משתנה `y` הוא `static` ולכן השינוי שלו שוב נשמר. אזי ערכי `x` ו-`y` הם 0 ו-2 בהתאמה.
לכן `p[x]` ו-`p[y]` הם גישות לאיברי `p[0]` ו-`p[2]` בהתאמה, ז"א קריאות לפונקציה `f1()` אשר מדפיסה 1 ולפונקציה `f3()` אשר מדפיסה 3. אזי הפלט באיטרציה השלישית הוא
`1 3`
אחרי יציאה מהלולאה, נקראת פונקצית `f5` אשר מדפיסה ערך משתנה גלובלי `y` המאותחל ל-2 ומקדמת את `y` לאחר מכאן. מיד אחרי יציאה מ-`f5`, מודפס ערך `y` של `main`, אשר אחרי יציאה מהלולאה שווה ל-8. לכן הפלט בשורה הרביעית הוא
`2 8`
אחר כך, שוב נקראת פונקצית `f5` אשר מדפיסה ערך משתנה גלובלי `y` אשר אחרי השינוי בקריאה הקודמת שווה ל-3. מיד אחרי יציאה מ-`f5`, מודפס ערך `y` של `main`, אשר עדיין שווה ל-8. לכן הפלט בשורה החמישית הוא
`3 8`"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + "מהי הטענה הלא נכונה?"
Q5A_OPTS = opts("מבנה יכול להיות שדה של מבנה אחר",
                "מצביע למבנה יכול להיות שדה של מבנה אחר",
                "מבנה יכול להיות שדה של אותו מבנה",
                "מצביע למבנה יכול להיות שדה של אותו מבנה",
                "כל הטענות לעיל הן נכונות")
Q5A_EXPL = "אם המבנה יתבסס על עצמו זו תהיה הגדרה אינסופית. והזיכרון הדרוש לא יהיה ידוע במהלך ההגדרה."

Q5B_TEXT = Q5_INTRO + """מה עושים בקטע הבא?
```c
char str1[] = "hello", *str2 = "hello";
if (str1 == str2)   printf("yes");
```"""
Q5B_OPTS = opts("משווים את כתובות המחרוזות",
                "משווים את תכני המחרוזות",
                "משווים את אורכי המחרוזות",
                "משווים תווים ראשונים של המחרוזות",
                "הקטע שגוי ויגרום לשגיאת קומפילציה",
                "אף תשובה אינה נכונה")
Q5B_EXPL = "גם `str1` וגם `str2` הם כתובות (כי `str1` הוא מערך ו-`str2` הוא מצביע במפורש)."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
     char s[]={'/','/'/'/','/'/'/'/'/','/'};
     int i;
     for (i=0;s[i];i++) printf("%d",s[i]/'/');
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `10`

**נימוק:**
איבר מס' 0 ב-`s` שווה ל-`'/'`. איבר מס' 1 ב-`s` שווה ל-`'/' / '/'`, ז"א, ל-1. איבר מס' 2 הוא `'/' / '/' / '/'` ששווה ל-0 (קוד ASCII של `'/'` גדול מ-1 ולכן `'/' / 1` שווה ל-0).
בלולאה סורקים את המערך מאיבר מס' 0. מכיוון שאיבר מס' 2 הוא 0, מטפלים רק באיברי מס' 0 ומס' 1. באיטרציה הראשונה מדפיסים ערך של `'/' / '/'`, ז"א **1**. באיטרציה השנייה מדפיסים ערך של `'/' / 1`, ז"א **0**. לכן הפלט יהיה
`10`"""

questions = [
    Q(1, "code", "linked_lists", Q1_TEXT, Q1_SOL, points=40, image="images/exams/25B-B-Q1.png"),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40, image="images/exams/25B-B-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    Q(4, "code", "storage_classes", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "structs_unions", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "c", "explanation": Q5A_EXPL,
     "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "strings", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "a", "explanation": Q5B_EXPL,
     "official": True, "confidence": "high"},
    Q(6, "code", "c_traps_mcq", Q6_TEXT, Q6_SOL, points=10),
]

exam = {
    "examCode": "25B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
    "year": 2025,
    "examDate": "29.07.2025",
    "sourceFile": "25B-B exam",
    "solutionFile": "25B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
