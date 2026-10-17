# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-A.json -- programming-workshop (C), semester B 2021, moed A (15.06.21).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of the three), Part 2: Q4 parts 1-4 (20 pts, MCQ with justification;
stored as parts a-d), Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code
+ marked options). Code solutions compiled and run with clang: tools/verify/21B-A/.
Run: PYTHONUTF8=1 py tools/gen/gen_21B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


PART1 = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש (שאלות 1, 2 ו-3).*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נתונה הגדרה הבאה של הטיפוס `name` אשר מהווה שם פרטי ושם משפחה של בן-אדם:
```c
typedef struct
{
    char first_name[30],
    last_name[30];
} name;
```
כתוב פונקציה אשר מקבלת מערך איברים מסוג `name` וגודלו.
על הפונקציה לבדוק האם איברי המערך ממוינים בסדר לקסיקוגרפי עולה לפי השמות (שדה `first_name`) או לפי שמות המשפחה (שדה `last_name`). אם המערך ממוין לפי השמות, הפונקציה תחזיר 1 ואם לפי שמות המשפחה - הפונקציה תחזיר 2. אם איברי המערך לא ממוינים בכלל, הפונקציה תחזיר 0.

**דוגמה:** עבור המערך הבא
```
0 Mike Asher
1 David Bern
2 Joseph Borgman
3 Alon Kapulski
4 Ilan Mizrachi
5 Oren Nodel
6 Abraham Rosen
```
הפונקציה תחזיר 2.""" + PART1

Q1_SOL = r"""```c
int ordered_name_array(name* name_arr, int n)
{
    int i;
    for (i = 1; i < n; i++)
        if (strcmp(name_arr[i].first_name, name_arr[i - 1].first_name) < 0)
        {
            for (i = 1; i < n; i++)
                if (strcmp(name_arr[i].last_name, name_arr[i - 1].last_name) < 0)
                    return 0;
            return 2;
        }
    return 1;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item {
    int data;
    struct item *next;
} Item;
```
כתוב פונקציה אשר מקבלת שתי רשימות מקושרות **מעגליות** (רשימה מעגלית מועברת לפונקציה כמצביע לאחד מהאיברים שלה) המורכבות מאיברים מסוג `Item`.
הרשימות מכילות מספרים שונים כאשר ישנו רק מספר אחד המופיע בשתי הרשימות.

על הפונקציה לאחד את הרשימות לרשימה מעגלית אחת כך שהמספר המשותף יופיע פעם אחת ויחצוץ בין שתי הרשימות המקוריות, שתשמורנה על סידרן הפנימי לאחר האיחוד.
לא משנה מאיזו רשימה מקורית יהיו איברים "אחרי" המספר המשותף ברשימה המאוחדת ומאיזו רשימה יהיו "לפניו". גם לא משנה איזה איבר המכיל את המספר המשותף ייכלל ברשימה המאוחדת.
הפונקציה תחזיר את כתובת האיבר המכיל את המספר המשותף ברשימה המאוחדת.

**שים לב.** הפונקציה לא תקצה זיכרון לרשימה החדשה אלא תעדכן שדה `next` באיברים המתאימים של הרשימות המקוריות.

**דוגמא:** (באיור) המספר המשותף הוא 5.

**שים לב.** כל אחת מרשימות מקוריות יכולה להיות מורכבת גם רק מאיבר אחד (שדה `next` שלו מצביע לאיבר עצמו). במקרה זה האיבר היחיד מכיל את המספר המשותף.""" + PART1

Q2_SOL = r"""```c
/* Auxiliary function. Search of common items.
   The function gives addresses of items preceding common ones */
void addresses_of_items_preceding_common(Item *L1, Item *L2, Item **p1, Item **p2){
    Item *prev1 = L1, *prev2, *curr1 = prev1->next, *curr2;
    while (1) //external loop: scan first list
    {
        prev2 = L2;
        curr2 = prev2->next;
        do //internal loop: scan second list
        {
            if (curr2->data != curr1->data)
            {
                prev2 = curr2;
                curr2 = curr2->next;
            }
            else //common items are found
            {
                *p1 = prev1;
                *p2 = prev2;
                return;
            }
        } while (curr2 != L2->next);
        prev1 = curr1;
        curr1 = curr1->next;
    } //while (1)
}

/* Special case: list L1 has one item */
Item *one_item_list(Item *L1, Item *L2){
    int common = L1->data;
    free(L1);
    while (L2->data != common) //search of common item in L2
        L2 = L2->next;
    return L2;
}

Item *cyclic_lists_combining(Item *L1, Item *L2){
    Item *p1, *p2, *common;
    if (L1->next == L1) //L1 has one item
        return one_item_list(L1, L2);
    if (L2->next == L2) //L2 has one item
        return one_item_list(L2, L1);

    //p1 and p2 are addresses of items preceding common ones
    addresses_of_items_preceding_common(L1, L2, &p1, &p2);

    /* Combining of L1 and L2*/
    common = p1->next;
    p1->next = p2->next->next;
    free(p2->next);
    p2->next = common;
    return common;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזת `fileName` המהווה שם של **קובץ טקסט**. הקובץ שומר תוכן של מערך דו-ממדי של מספרים שלמים שבו כל שורה מורכבת מרצפים של מספרים זהים בדרך חסכונית.

שורה מס' `i` בקובץ מתאימה לשורה מס' `i` של המערך (שורות הקובץ ממוספרות מ-0).
כל רצף של מספרים זהים בשורת המערך (מתחילתה עד סופה) מוצג בשורת הקובץ (מתחילתה עד סופה) בהתאם כזוג מספרים: ערך האיברים ברצף וכמות האיברים ברצף.
המספרים הסמוכים בכל שורה מופרדים ברווח אחד. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה לשחזר מערך דו-ממדי דינאמי `A`. יש למלא את `A` בהתאם לתוכן הקובץ.
בנוסף הפונקציה תיצור מערך דינאמי `S` המורכב מגדלי שורות של `A` כך שאיבר מס' `i` ב-`S` יהיה שווה לגודל שורה מס' `i` ב-`A`.
הפונקציה תחזיר את `A` ותעביר (`by reference`) את `S` ואת מספר השורות ב-`A`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.

**דוגמא:**
```
תוכן הקובץ        המערך A                    S
4 2 7 4 3 3       4 4 7 7 7 7 3 3 3          9
2 6 1 2           2 2 2 2 2 2 1 1            8
9 1 12 3          9 12 12 12                 4
3 2 18 5 0 2      3 3 18 18 18 18 18 0 0     9
```
הפונקציה תעביר 4 כמספר השורות ב-`A`.""" + PART1

Q3_SOL = r"""```c
int **file_to_sequences_in_rows(char* filename, int **S, int *rows)
{
    char ch;
    int **A, num, size, start_row, i, j, k;
    FILE* fptr = fopen(filename, "r");
    if (!fptr)
        exit(1);

    /* Estimation of the number of rows */
    *rows = 0;
    while ((ch = fgetc(fptr)) != EOF)
        if (ch == '\n')
            (*rows)++;

    A = (int**)calloc(*rows, sizeof(int*)); //pointer array allocation
    *S = (int*)calloc(*rows, sizeof(int)); //array of row sizes allocation

    rewind(fptr);
    for (i = 0; i < *rows; i++)
    {
        start_row = ftell(fptr);
        /* Estimation of row size */
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            (*S)[i] += size;
        } while ((ch = fgetc(fptr)) != '\n');

        A[i] = (int*)calloc((*S)[i], sizeof(int)); //row allocation

        /* File row -> array row */
        fseek(fptr, start_row, SEEK_SET);
        k = 0;
        do
        {
            fscanf(fptr, "%d%d", &num, &size);
            for (j = 1; j <= size; j++, k++)
                A[i][k] = num;
        } while ((ch = fgetc(fptr)) != '\n');
    } //for i
    fclose(fptr);
    return A;
}
```"""

# ---------------------------------------------------------------- Q4 (parts 1-4 of the printed exam, stored as a-d)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים (שאלה 4, 20 נק' בסך הכול; חובה לרשום את הבחירה והנימוק במחברת). זהו סעיף {n} בשאלה.\n"

Q4A_TEXT = Q4_INTRO.format(n=1) + "מה מאותחל כברירת המחדל?"
Q4A_OPTS = opts("משתנה מסוג `int` שמוגדר בתוך פונקציה, למשל `int x;`",
                "משתנה מסוג פוינטר ל-`int` שמוגדר בתוך פונקציה, למשל `int *p;`",
                "קבועים של טיפוס `enum`",
                "משתנה בקרה בלולאת `for` אשר לא מאותחל במפורש בחלק הראשון של הלולאה, למשל `for( ; i<n; i++)`",
                "איברי מערך דינאמי שהוקצה באמצעות פונקציית `malloc`",
                "אף תשובה אינה נכונה")
Q4A_EXPL = "ערכים של הקבועים של `enum` נקבעים אוטומטית, מתחילים מ-0 וגדלים ב-1."

Q4B_TEXT = Q4_INTRO.format(n=2) + "מה קורה בצד שמאל של מספר `int` חיובי לאחר ביצוע פעולת הזזת סיביות ימינה בתוכו?"
Q4B_OPTS = opts("מצד שמאל המספר מתמלא ב-0-ים", "מצד שמאל המספר מתמלא ב-1-ים",
                "מצד שמאל המספר מתמלא בסיביות שהלכו לאיבוד מצד ימין",
                "שיטת מילוי המספר מצד שמאל תלויה במערכת", "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C."

Q4C_TEXT = Q4_INTRO.format(n=3) + "איזה מערך מועבר לפונקציה `by value` (ז\"א הפונקציה מקבלת גישה להעתק של תוכנו אבל לא לתוכן המקורי שלו)?"
Q4C_OPTS = opts("מערך סטטי חד-ממדי", "מערך דינאמי חד-ממדי", "מערך סטטי דו-ממדי", "מערך דינאמי דו-ממדי",
                "מערך סטטי אשר מהווה שדה של המבנה כאשר המבנה מועבר לפונקציה `by value`", "אף תשובה אינה נכונה")
Q4C_EXPL = "מערך עצמו תמיד מועבר `by reference` כי הפונקציה מקבלת לא מערך עצמו אלא כתובתו. אבל מבנה מועבר `by value` כך שכל השדות שלו מועתקים כולל שדות שהם מערכים."

Q4D_TEXT = Q4_INTRO.format(n=4) + r"""נתונה הפונקציה הבאה:
```c
int *fun() {
    static int x;
    x++;
    return &x;
}
```
מהי הטענה הנכונה?"""
Q4D_OPTS = opts("הפונקציה לא תקינה רק מכיוון שהיא מחזירה כתובת של משתנה אשר לא קיים מעבר לפונקציה",
                "הפונקציה לא תקינה רק מכיוון שניגשים בתוכה למשתנה אשר לא מאותחל",
                "הפונקציה לא תקינה גם מכיוון שהיא מחזירה כתובת של משתנה אשר לא קיים מעבר לפונקציה וגם מכוון שניגשים בתוכה למשתנה אשר לא מאותחל",
                "הפונקציה תקינה", "אף טענה אינה נכונה")
Q4D_EXPL = "משתנה `static` נשמר בזיכרון גם אחרי יציאה מהפונקציה. משתנה `static` ללא אתחול מפורש מאותחל ב-0."

# ---------------------------------------------------------------- Q5
Q5_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
    printf("%d\n", sizeof"|0\0/00\0/0|");
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:** `11`

**נימוק:**
בטקסט שבתוך המירכאות יש 12 סימנים. ביניהם פעמיים מופיעה סדרת `'\0'` אשר מהווה תו אחד. לכן מופיעים פה 10 תווים. בסוף כל מחרוזת קבועה יש עוד תו אפסי (`'\0'`). לכן סה"כ המערך מורכב מ-11 תווים. אופרטור `sizeof` מחזיר את גודל האופרנד בבתים. כל תו תופס בית אחד. לכן הפלט יהיה 11."""

questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/21B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    {"num": 4, "part": "א", "kind": "mcq", "topic": "c_traps_mcq", "question": Q4A_TEXT,
     "options": Q4A_OPTS, "correctId": "c", "explanation": Q4A_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "a", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "structs_unions", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "e", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "storage_classes", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "d", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "21B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"א, מועד א'",
    "year": 2021,
    "examDate": "15.06.2021",
    "sourceFile": "21B-A exam",
    "solutionFile": "21B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
