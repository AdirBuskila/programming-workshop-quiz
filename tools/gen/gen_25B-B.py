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

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run in tools/verify/25B-B/
# (q1..q6.c, steps_q1/2/3.c, q5*.c, q6_vals.c, mutants.sh). Lines of order/findbug/fillblank come from the stored solutions.
def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip()]


def func_lines(src, header_start):
    """The code lines of the function whose header line starts with header_start, to its closing brace."""
    ls = lines_of(src)
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
    idx = [i for i, ln in enumerate(lines) if ln.strip() == target]
    assert len(idx) > nth and (nth or len(idx) == 1 or True), target
    return [("___" if i == idx[nth] else ln) for i, ln in enumerate(lines)], idx[nth]


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError(num)


# Q1
F1 = func_lines(Q1_SOL, "Item *lists_with_given_elements")
AUX1 = func_lines(Q1_SOL, "int List1_elements_in_List2")
b1, i1 = swap(F1, "for (i = n - 1; i >= 0; i--)", "for (i = n - 1; i > 0; i--)")
f1, j1 = blank(F1, "insert_in_head(i, &ind_list);")
add(1,
    rubric=rub(("פונקציית עזר שבודקת אם כל איברי `L` נמצאים ברשימה אחרת: לכל איבר של `L` חיפוש ברשימה, והחזרת 0 כשאיבר חסר", 14),
               ("מעבר על כל `n` הרשימות במערך `A` וקריאה לפונקציית העזר עבור כל אחת", 9),
               ("יצירת איבר `Item` חדש עם האינדקס `i` בשדה `data` (הקצאה דינמית) והוספתו לרשימה החדשה", 9),
               ("החזרת כתובת האיבר הראשון של הרשימה החדשה, ו-`NULL` כשאין אף רשימה מתאימה", 8)),
    rubricSource="ai-verified",
    pitfalls=["לבדוק רק שאורך הרשימה ב-`A[i]` שווה לאורך `L` או שהאיבר הראשון זהה, במקום לחפש כל איבר של `L` ברשימה.",
              "להוסיף לרשימה החדשה את `A[i]` או כתובת של איבר קיים במקום ליצור איבר `Item` חדש שמחזיק את האינדקס `i`.",
              "החזרת ערך שלא אותחל כאשר לא נמצא אף איבר מתאים"],
    steps=[
        {"type": "numeric",
         "prompt": "בדוגמה (`L` היא `8,2,5`) כמה רשימות במערך `A` מכילות את כל איברי `L`? כלומר, מה אורך הרשימה החדשה?",
         "answer": 3, "tol": 0,
         "explain": "הרשימות באינדקסים 0, 3 ו-4 מכילות את `8`, `2` ו-`5`, ולכן האורך 3 (ריצה אמיתית: 3, הרשימה `0 3 4`)."},
        {"type": "choice",
         "prompt": "מה מחזירה פונקציית העזר `List1_elements_in_List2(L, A[2])`, כאשר `A[2]` היא הרשימה `5` בלבד?",
         "options": opts("`0`", "`1`", "`NULL`", "`2`"), "correctId": "a",
         "explain": "`A[2]` קצרה מ-`L`, ולכן הבדיקה הראשונה בפונקציה מחזירה 0 לפני החיפוש (ריצה אמיתית: 0). הפונקציה מחזירה 1 רק כשכל האיברים נמצאו."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה בפונקציה הראשית.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": opts("insert_in_head(i, &ind_list);", "insert_in_head(A[i], &ind_list);",
                         "insert_in_head(L->data, &ind_list);", "ind_list = A[i];"), "correctId": "a",
         "explain": "לרשימה החדשה מוסיפים איבר חדש שמחזיק את האינדקס `i` (ולא את `A[i]`), והכתובת המעודכנת של הראש נשמרת דרך `&ind_list`."},
        {"type": "order", "prompt": "סדרו את שורות הפונקציה `lists_with_given_elements`.", "code": True, "lines": F1,
         "explain": "הכרזה על המשתנים, אתחול הרשימה החדשה ל-`NULL`, לולאה על האינדקסים, בדיקה והוספה, ובסוף החזרת הראש."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה. הפלט על הדוגמה הוא `3 4` במקום `0 3 4`. מצאו את השורה.", "code": True,
         "lines": b1, "bugIndex": i1,
         "explain": "`i > 0` במקום `i >= 0` מדלג על האינדקס 0, ולכן האינדקס 0 חסר (ריצה אמיתית: `3 4`)."},
    ],
    stepsSource="ai-verified")

# Q2
F2 = func_lines(Q2_SOL, "int** triangles_to_matrix")
b2, i2 = swap(F2, "for (j = i + 1; j < n + 1; j++)", "for (j = i + 1; j < n; j++)")
f2, j2 = blank(F2, "A[i][j] = tr_up[i][j - i - 1];")
add(2,
    rubric=rub(("הקצאת מערך מצביעים בגודל `n+1` והקצאת כל שורה בגודל `n+1` עם איפוס (`calloc`) כך שהאלכסון הראשי 0", 10),
               ("העתקת המשולש התחתון: `A[i][j] = tr_low[i-1][j]` עבור `i` מ-1 עד `n` ו-`j < i`", 12),
               ("העתקת המשולש העליון עם הזזה: `A[i][j] = tr_up[i][j-i-1]` עבור `j` מ-`i+1` עד `n`", 12),
               ("החזרת כתובת המערך", 6)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח שהמטריצה בגודל `(n+1)×(n+1)` ולהקצות `n×n`, או לא לאפס את האלכסון הראשי (שימוש ב-`malloc` במקום `calloc`).",
              "לגשת למשולש העליון ב-`tr_up[i][j]` במקום `tr_up[i][j-i-1]`, בלי להתחשב בכך ששורותיו מוזזות שמאלה בזיכרון.",
              "לחשב שורות של המשולש התחתון ב-`tr_low[i][j]` במקום `tr_low[i-1][j]`: ל-`tr_low` יש `n` שורות והראשונה מתאימה לשורה 1 של המטריצה."],
    steps=[
        {"type": "numeric",
         "prompt": "בדוגמה (`n = 3`), מה ערך `A[2][1]` בסוף הפונקציה? (תא מתחת לאלכסון הראשי)",
         "answer": 4, "tol": 0,
         "explain": "`A[2][1] = tr_low[1][1] = 4` (ריצה אמיתית: 4)."},
        {"type": "numeric",
         "prompt": "באותה דוגמה, מה ערך `A[1][3]`?",
         "answer": 42, "tol": 0,
         "explain": "`A[1][3] = tr_up[1][3-1-1] = tr_up[1][1] = 42` (ריצה אמיתית: 42)."},
        {"type": "choice",
         "prompt": "באיזה אינדקס בשורה `tr_up[i]` נמצא האיבר של `A[i][j]` (כש-`j > i`)?",
         "options": opts("`j - i - 1`", "`j`", "`j - i`", "`j + i`"), "correctId": "a",
         "explain": "שורה `i` של המשולש העליון מתחילה באיבר `A[i][i+1]`, ולכן האינדקס הוא `j-i-1` (הדוגמה: `A[1][3]` נמצא באינדקס 1)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה בפונקציה.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": opts("A[i][j] = tr_up[i][j - i - 1];", "A[i][j] = tr_up[i][j];",
                         "A[i][j] = tr_up[i - 1][j];", "A[i][j] = tr_low[i][j - i - 1];"), "correctId": "a",
         "explain": "שורות המשולש העליון מוזזות שמאלה, ולכן הגישה היא עם `j - i - 1`."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה והעמודה האחרונה של המטריצה נשארת 0 במקום `13, 42, 60`. מצאו אותה.",
         "code": True, "lines": b2, "bugIndex": i2,
         "explain": "`j < n` במקום `j < n + 1` לא ממלא את העמודה האחרונה (ריצה אמיתית: `A[0][3]` יצא 0 במקום 13)."},
    ],
    stepsSource="ai-verified")

# Q3
F3 = func_lines(Q3_SOL, "void text_to_binary")
b3, i3 = swap(F3, "fwrite(&client, sizeof(clientData), 1, fout);", "fwrite(&client, sizeof(client.id), 1, fout);")
f3, j3 = blank(F3, 'fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);', nth=0)
add(3,
    rubric=rub(("פתיחת קובץ הטקסט לקריאה וקובץ הבינארי לכתיבה, ובדיקה שהפתיחה הצליחה", 8),
               ("קריאת שורה עם `fscanf` ובפורמט שמתאים לשדות: מחרוזת של עד 9 תווים, מחרוזת של עד 30 תווים ו-`double`", 12),
               ("כתיבת הרשומה לקובץ הבינארי עם `fwrite` בגודל `sizeof(clientData)` לכל שורה", 12),
               ("לולאה שמסתיימת בסוף הקובץ ושלא מפספסת שורה, וסגירת שני הקבצים", 8)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב ל-`fwrite` גודל שגוי, למשל `sizeof(client.id)` במקום `sizeof(clientData)`, ולקבל רשומות חלקיות בקובץ הבינארי.",
              "לקלוט את השם עם `%s` ללא הגבלת רוחב (או `%10s` ל-`id`), ולכתוב מחוץ לגבולות המערך `char id[10]`.",
              "לבצע בדיקת `feof` לפני הקריאה הראשונה או רק אחרי הקריאה של השורה, ולכתוב רשומה אחת יותר או פחות מדי."],
    steps=[
        {"type": "numeric",
         "prompt": "מה `sizeof(clientData)` במחשב שעליו נבדק הקוד (`id[10]`, `name[31]`, `double total`)?",
         "answer": 56, "tol": 0,
         "explain": "10 + 31 = 41 בתים, אחריהם ריפוד עד 48 (היסט `total`), ועוד 8 בתים ל-`double`, בסך הכול 56 (במערכת 64 ביט) (ריצה אמיתית: 56 (במערכת 64 ביט))."},
        {"type": "numeric",
         "prompt": "קובץ הטקסט מהדוגמה (שלוש שורות, והשורה האחרונה מסתיימת בתו שורה חדשה) עבר המרה. מה גודל הקובץ הבינארי בבתים?",
         "answer": 168, "tol": 0,
         "explain": "שלוש רשומות של 56 (במערכת 64 ביט) בתים: 3 × 56 = 168 (ריצה אמיתית: 168 בתים, 3 רשומות)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה בפונקציה: הקריאה הראשונה של לקוח.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": opts('fscanf(fin, "%9s%30s%lf", client.id, client.name, &client.total);',
                         'fscanf(fin, "%10s%31s%lf", client.id, client.name, &client.total);',
                         'fscanf(fin, "%9s%30s%lf", client.id, client.name, client.total);',
                         'fscanf(fin, "%9s%30s%f", client.id, client.name, &client.total);'), "correctId": "a",
         "explain": "רוחב 9 ל-`id[10]` ו-30 ל-`name[31]` משאיר מקום לתו הסיום, ולקליטת `double` נדרש `%lf` עם כתובת `&client.total`. האפשרות ב' (`%10s%31s`) עובדת על קובץ הדוגמה, אך נכשלת כאשר מזהה בן 9 תווים נצמד ישירות לשם בן 30 תווים."},
        {"type": "order", "prompt": "סדרו את שורות הפונקציה `text_to_binary`.", "code": True, "lines": F3,
         "explain": "פתיחת הקבצים ובדיקות, קריאה ראשונה, לולאה שכותבת וקוראת את הבאה, ובסוף סגירת הקבצים."},
        {"type": "findbug", "prompt": "בגרסה הבאה שורה אחת שונתה, ובקובץ הבינארי יש רק 30 בתים במקום 168. מצאו אותה.", "code": True,
         "lines": b3, "bugIndex": i3,
         "explain": "`sizeof(client.id)` הוא 10, ולכן נכתבים 10 בתים לכל לקוח במקום הרשומה כולה (ריצה אמיתית: 30 בתים לשלוש רשומות)."},
    ],
    stepsSource="ai-verified")

# Q4 (output verified by running q4.c)
Q4_OUT = ["1 1", "1 2", "1 3", "2 8", "3 8"]
add(4,
    rubric=rub(("זיהוי ש-`y` ב-`f4` הוא `static` עם ערך התחלתי 0 ושהשינוי בו נשמר בין הקריאות, בעוד `x` מאותחל מחדש בכל קריאה", 3),
               ("שלוש השורות הראשונות נכונות: `1 1`, `1 2`, `1 3`", 3),
               ("זיהוי ש-`f5` משתמשת במשתנה הגלובלי `y` (2, ואחר כך 3) ו-`main` מדפיסה את `y` המקומי (8)", 2),
               ("שתי השורות האחרונות נכונות: `2 8` ו-`3 8`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`y` הסטטי מאותחל מחדש בכל קריאה ל-`f4` ולהדפיס `1 1` בשלוש השורות.",
              "לבלבל בין שלושת ה-`y`: הגלובלי, הסטטי ב-`f4` והמקומי ב-`main`, ולכן להדפיס `5 8` או `2 5` ב-`f5`.",
              "לשכוח שאחרי הלולאה `y` של `main` שווה 8 (הלולאה יוצאת כש-`y <= 7` לא מתקיים) ולכתוב 7."],
    steps=[
        {"type": "choice", "prompt": "מה מדפיסה השורה השנייה של הפלט?",
         "options": opts("`1 2`", "`1 1`", "`2 2`", "`2 1`"), "correctId": "a",
         "explain": "בקריאה השנייה `x = 0` ו-`y` הסטטי שווה 1, לכן נקראות `f1` ו-`f2` (ריצה אמיתית: `1 2`)."},
        {"type": "choice", "prompt": "מה מדפיסה השורה השלישית של הפלט?",
         "options": opts("`1 3`", "`1 2`", "`3 3`", "`1 1`"), "correctId": "a",
         "explain": "בקריאה השלישית ה-`y` הסטטי שווה 2, לכן נקראות `f1` ו-`f3` (ריצה אמיתית: `1 3`)."},
        {"type": "numeric",
         "prompt": "מה הערך של `y` של `main` שמודפס אחרי הקריאה הראשונה ל-`f5`?",
         "answer": 8, "tol": 0,
         "explain": "הלולאה מסתיימת כש-`y` הופך ל-8 (ריצה אמיתית: השורה `2 8`). `f5` משנה רק את הגלובלי."},
        {"type": "order", "prompt": "סדרו את שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True,
         "lines": Q4_OUT,
         "explain": "שלוש קריאות ל-`f4`, ואז שתי קריאות ל-`f5` עם ההדפסה של `y` המקומי (ריצה אמיתית: אותן חמש שורות)."},
    ],
    stepsSource="ai-verified")

# Q5 (mcq): short pitfalls only, checked by compiling q5a_bad.c / q5a_ok.c / q5.c
add(5, "א",
    pitfalls=["לחשוב שמצביע למבנה לא יכול להיות שדה של אותו מבנה: זה המקרה של `struct item *next` ברשימה מקושרת, והוא מתקמפל (ריצה אמיתית). רק שדה מאותו מבנה עצמו (`struct s inner;`) נכשל בקומפילציה עם `field has incomplete type`."])
add(5, "ב",
    pitfalls=["לחשוב ש-`==` על שני שמות של מחרוזות משווה תוכן: הוא משווה כתובות. בריצה אמיתית `str1 == str2` נותן 0 והטקסט `yes` לא מודפס (`strcmp` היא ההשוואה של התוכן)."])

# Q6 (s = {47, 1, 0, 47} verified by q6_vals.c)
add(6,
    rubric=rub(("חישוב ערכי איברי המערך: `s[0] = '/'` (47), `s[1] = '/' / '/' = 1`, `s[2] = 0`", 4),
               ("זיהוי שהלולאה נעצרת באיבר 0 (`s[2]`), כך שרצים רק על שני האיברים הראשונים", 2),
               ("הדפסת `s[i] / '/'` בכל איטרציה: 1 ואחר כך 0", 3),
               ("הפלט הסופי `10` (רצף ללא רווחים)", 1)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא את המערך כארבעה תווי `/` ולהדפיס `1111`: האופרטור `/` בתוך הסוגריים המסולסלים הוא חילוק של קודי ASCII.",
              "לשכוח שחילוק שלם של 1 ב-47 נותן 0, ושהלולאה נעצרת באיבר שערכו 0 ולא ממשיכה לאיבר `s[3]`."],
    steps=[
        {"type": "numeric", "prompt": "מה ערך האיבר `s[1]`, כלומר `'/' / '/'`?",
         "answer": 1, "tol": 0,
         "explain": "חילוק של קוד ASCII בעצמו נותן 1 (ריצה אמיתית: `s[1] = 1`)."},
        {"type": "numeric", "prompt": "מה ערך האיבר `s[2]`, כלומר `'/' / '/' / '/'`?",
         "answer": 0, "tol": 0,
         "explain": "`(47/47)/47 = 1/47 = 0` בחילוק שלם (ריצה אמיתית: `s[2] = 0`)."},
        {"type": "numeric", "prompt": "כמה איטרציות מבצעת הלולאה `for (i=0; s[i]; i++)`?",
         "answer": 2, "tol": 0,
         "explain": "הלולאה נעצרת ב-`s[2] = 0` (ריצה אמיתית: הודפסו הערכים של `i = 0` ו-`i = 1` בלבד)."},
        {"type": "text", "prompt": "מה הפלט של התוכנית? (רצף ספרות, ללא רווחים)",
         "accept": ["10"], "normalize": "none",
         "explain": "האיטרציות מדפיסות `1` ואחר כך `0` (ריצה אמיתית: `10`)."},
    ],
    stepsSource="ai-verified")


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
