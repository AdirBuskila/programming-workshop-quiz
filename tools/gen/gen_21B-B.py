# -*- coding: utf-8 -*-
"""Generator for tools/raw/21B-B.json -- programming-workshop (C), semester B 2021, moed B (13.07.2021).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of three). Part 2: Q4 (20 pts, four pick-and-justify items).
Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/21B-B/. Q1 is held: the official solution fails its own example.
Run: PYTHONUTF8=1 py tools/gen/gen_21B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "21B-B.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CHOOSE = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש.*"

# ---------------------------------------------------------------- Q1 (held)
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מחרוזות `infile_1`, `infile_2` ו-`outfile` המהוות שמות של שלושה קבצי טקסט.
תוכן של כל שורה בקבצים `infile_1` ו-`infile_2` הוא רצף של מספרים שלמים **ממוינים** (מתחילת השורה עד סופה) מופרדים ברווחים. התו של סוף השורה מופיע מיד אחרי המספר האחרון בכל שורה, כולל השורה האחרונה.

על הפונקציה למלא קובץ `outfile` כך שתוכן שורה מס' `i` בתוכו יהיה רצף **ממוין** (מתחילת השורה עד סופה) של כל המספרים ששייכים לשורות מס' `i` בקבצים `infile_1` ו-`infile_2`.
אם מספרי השורות בקבצים `infile_1` ו-`infile_2` הם שונים (נסמן אותם ב-`n` ו-`m` כך שלמשל `n>m`) אז קובץ `outfile` יכלול `n` שורות כך ש-`n-m` השורות האחרונות יועתקו מהקובץ התואם.

**דוגמא:**
`infile_1`:
```
3 8 12 16 20
0 2 2 6
9 10 10 11 19 26
4 4 4 5
```
`infile_2`:
```
9 17
2 6 7 11
5 13 14 18
```
`outfile`:
```
3 8 9 12 16 17 20
0 2 2 2 6 6 7 11
5 9 10 10 11 13 14 18 19 26
4 4 4 5
```""" + CHOOSE

Q1_SOL = r"""```c
/* Auxiliary function. Copy a number from file to file
and input of a next number */
void next_number(FILE* in, FILE* out, int* num, char* ch)
{
    fprintf(out, "%d ", *num);
    if ((*ch = fgetc(in)) != '\n')
        fscanf(in, "%d", num);
}

/* Auxiliary function.
Merging 2 sorted rows of 2 files into a sorted row in a new file */
void rows_merge(FILE* in1, FILE* in2, FILE* out)
{
    char ch1=0, ch2=0;
    int num1, num2;

    /* Merging rows until one of the rows ends */
    fscanf(in1, "%d", &num1);
    fscanf(in2, "%d", &num2);
    while (ch1 != '\n' && ch2 != '\n')
        if (num1 < num2)
            next_number(in1, out, &num1, &ch1);
        else
            next_number(in2, out, &num2, &ch2);

    /* Copying remainder of a longer row */
    while (ch1 != '\n')
        next_number(in1, out, &num1, &ch1);
    while (ch2 != '\n')
        next_number(in2, out, &num2, &ch2);

    fputc('\n', out);
}

/* Auxiliary function */
void copy_file(FILE* in, FILE* out)
{
    char ch;
    while ((ch = fgetc(in)) != EOF)
        fputc(ch, out);
}

void filesMerge(char* infile1, char* infile2, char* outfile)
{
    FILE* in1 = fopen(infile1, "r");
    FILE* in2 = fopen(infile2, "r");
    FILE* out = fopen(outfile, "w");
    if (!in1 || !in2 || !out)
        exit(1);

    /* Merging file rows until one of the files ends */
    while (fgetc(in1) != EOF && fgetc(in2) != EOF)
    {
        fseek(in1, -1, SEEK_CUR);
        fseek(in2, -1, SEEK_CUR);
        rows_merge(in1, in2, out);
    }

    /* Copying remainder of a larger file */
    fseek(in1, -1, SEEK_CUR);
    fseek(in2, -1, SEEK_CUR);
    copy_file(in1, out);
    copy_file(in2, out);

    fclose(in1);
    fclose(in2);
    fclose(out);
}
```

**הערת מתמלל (לא חלק מהפתרון הרשמי):** בהרצה אמיתית (`tools/verify/21B-B/q1.c`) הפתרון הרשמי ממזג נכון את השורות המשותפות, אך אינו מייצר את הפלט של הדוגמה. כשאחד הקבצים נגמר לפני השני, `fseek(..., -1, SEEK_CUR)` על הקובץ שלא נקרא (או שכבר הגיע ל-EOF) מחזיר אותו תו אחד אחורה, ו-`copy_file` מעתיק אליו תו `\n` עודף. בדוגמה (ל-`infile_1` ארבע שורות ול-`infile_2` שלוש) מתקבלת שורה ריקה בסוף `outfile`, וכש-`infile_2` ארוך יותר מ-`infile_1` מתקבלות שורות ריקות בין השורות. בנוסף, ב-Windows עם הספרייה המודרנית `fseek` בכיוון אחורה על קובץ שנפתח במצב טקסט נכשל, ולכן ההרצה נעשתה במצב בינארי."""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס `person` אשר מהווה שם משפחה, שם פרטי ומס' זהות של בן-אדם:
```c
typedef struct {
    char last_name[30], first_name[30];
    unsigned id;
} person;
```
כתוב פונקציה בוליאנית אשר מקבלת מערך איברים מסוג `person` וגודלו.
על הפונקציה להחזיר `1` אם המערך ממוין בסדר עולה ולהחזיר `0` אחרת.

נגדיר מערך איברים מסוג `person` כ**ממוין בסדר עולה** אם:
1. איברי המערך ממוינים בסדר לקסיקוגרפי עולה ממש לפי שמות המשפחה (שדה `last_name`);
2. כאשר בין איברי המערך יש איברים בעלי שדות `last_name` זהים, האיברים הללו ממוינים בסדר לקסיקוגרפי עולה ממש לפי שמות פרטיים (שדה `first_name`);
3. כאשר בין איברי המערך יש איברים בעלי שדות `last_name` זהים וגם שדות `first_name` זהים, האיברים הללו ממוינים בסדר עולה לפי מספרי הזהות (שדה `id`).

**דוגמאות:**
עבור המערך הבא
```
0 Asher Mike 231567809
1 Bern David 216578900
2 Borgman Joseph 354678903
3 Cohen Abraham 224567821
4 Cohen Den 206666431
5 Levi Ilan 290876441
6 Levi Omri 245689432
7 Levi Omri 245689436
8 Smith Jack 345389010
9 Smith John 311232111
```
הפונקציה תחזיר `1`.

עבור המערך הבא
```
0 Asher Mike 231567809
1 Bern David 216578900
2 Borgman Joseph 354678903
3 Cohen Abraham 224567821
4 Cohen Den 206666431
5 Levi Ilan 290876441
6 Levi Omri 245689436
7 Levi Omri 245689432
8 Smith Jack 345389010
9 Smith John 311232111
```
הפונקציה תחזיר `0`.""" + CHOOSE

Q2_SOL = r"""```c
int ordered_person_array(person* person_arr, int n)
{
    int i, cmp;
    for (i = 1; i < n; i++)
        if ( (cmp = strcmp(person_arr[i].last_name, person_arr[i - 1].last_name)) < 0 )
            return 0;
        else
            if (cmp == 0)
                if ((cmp=strcmp(person_arr[i].first_name, person_arr[i-1].first_name))<0)
                    return 0;
                else
                    if (cmp == 0)
                        if (person_arr[i].id < person_arr[i - 1].id)
                            return 0;
    return 1;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""**מטריצה דלילה** הינה מטריצה שמרבית איבריה בעלי ערך אפס.

כתוב פונקציה אשר מקבלת מטריצה דלילה `A` המיושמת כמערך של רשימות מקושרות (היישום החסכוני, כאשר מופיעים ברשימה רק איברי המטריצה שאינם בעלי ערך אפס). רשימה מס' `i` של המערך תתאים לשורה מס' `i` של מטריצה `A`.
איברי הרשימות יכילו ערך שהוא איבר המטריצה וגם ערך שהוא מס' העמודה בה הוא נמצא במטריצה.
הפונקציה תקבל כפרמטרים את מערך הרשימות וגודלו וגם את מספר העמודות במטריצה.

על הפונקציה לשחזר את המטריצה כמערך דו-ממדי **דינאמי** שכל שורותיו באותו גודל.
הפונקציה תחזיר כתובת של המערך הדו-ממדי הדינאמי הבנוי.

**דוגמא:** (באיור: משמאל המטריצה `A`, מימין מערך הרשימות שלה)

בדוגמא הנ"ל הפונקציה תקבל את `A` כמערך רשימות, את גודל המערך, 4, וגם את מספר העמודות ב-`A`, 5.

יש להגדיר את הטיפוס של איברי הרשימה מעל הפונקציה.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.""" + CHOOSE

Q3_SOL = r"""```c
typedef struct element
{
    int data;
    int col;
    struct element* ptr_next;
} element;

int** lists_to_sparse_matrix(element** list_row, int rows, int cols)
{
    int** arr, i;
    element* ptr;
    arr = (int**)calloc(rows, sizeof(int*));
    for (i = 0; i < rows; i++)
        arr[i] = (int*)calloc(cols, sizeof(int));

    for (i = 0; i < rows; i++)
    {
        ptr = list_row[i];
        while (ptr)
        {
            arr[i][ptr->col] = ptr->data;
            ptr = ptr->ptr_next;
        }
    } // for i
    return arr;
}
```"""

# ---------------------------------------------------------------- Q4 (20 pts, four items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים הבאים (חובה לרשום את הבחירה והנימוק במחברת). שאלה 4, 20 נק' בסך הכול.\n"

Q4A_TEXT = Q4_INTRO + r"""מהו פלט (משמאל לימין) של התוכנית הבאה?
```c
#include <stdio.h>

int x;

void f() {
    static int x;
    printf("%d", x);
    printf("%d", ++x);
}

void main() {
    f();
    printf("%d", x);
    printf("%d", ++x);
    f();
}
```
(1) `010101`
(2) `000000`
(3) `000011`
(4) `010112`
(5) `011223`
(6) התוכנית אינה תקינה
(7) אף תשובה אינה נכונה"""

Q4A_SOL = r"""**התשובה:** (4) `010112`

**נימוק:**
כברירת מחדל ערך התחלתי של `static x` הוא 0. לכן בקריאה ראשונה של `f()` מדפיסים 0, מקדמים `x` ומדפיסים 1. אחרי זה מדפיסים ערך התחלתי של `x` גלובלי ששווה ל-0, מקדמים `x` גלובלי ומדפיסים 1. בקריאה שנייה של `f()` מדפיסים `static x` שערכו נשאר 1, מקדמים `x` ומדפיסים 2."""

Q4B_TEXT = Q4_INTRO + r"""כמה פעמים יודפס `Hi` עקב ביצוע התוכנית הבאה?
```c
#include <stdio.h>
void main() {
    int i = 64;
    for (; i; i >>= 1)
        printf("Hi \n");
}
```"""
Q4B_OPTS = opts("פעם אחת", "7 פעמים", "64 פעמים", "אף פעם", "תהיה לולאה אינסופית", "אף תשובה אינה נכונה")
Q4B_EXPL = r"""ייצוג בינארי של 64 הוא 1000000 (6 אפסים, 7 סיביות). כל פעולה `i >>= 1` מביאה להזזה של 1 בסיבית אחת ימינה. לכן תוך 7 בדיקות (6 הזזות) סיבית 1 תהיה עוד במספר `i`, ערך של `i` יהיה שונה מ-0 ותנאי המשך הלולאה יתקיים. אחרי הזזה שביעית 1 יצאה מייצוג בינארי של `i` אשר יהיה מורכב רק מאפסים, ולכן ערך עשרוני שלו יהיה 0 כך שתנאי המשך הלולאה בבדיקה שמינית לא יתקיים."""

Q4C_TEXT = Q4_INTRO + r"""נתון פוינטר ל-`int p` שמצביע למערך דינאמי. למה יצביע `p` אחרי ביצוע פעולת `p = (int*)realloc(p, 0);`?"""
Q4C_OPTS = opts("לאותו מערך", "לאיזשהו מקום חדש", "`p` יהיה שווה ל-`NULL`", "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4C_EXPL = r"""לפי כללי שפת C כאשר גודל חדש של בלוק זיכרון ב-`realloc` שווה ל-0, הפונקציה מחזירה `NULL`."""

Q4D_TEXT = Q4_INTRO + r"""בתוכנית בה `a` מוגדר כמשתנה מסוג `int` ו-`fptr1` ו-`fptr2` הם פוינטרים לקבצים בינאריים קיימות שתי השורות הבאות:
```c
fread(&a, sizeof(a), 1, fptr1);
fwrite(&a, sizeof(a), 1, fptr2);
```
מהי הטענה הנכונה?"""
Q4D_OPTS = opts("ברשימת פרמטרי `fread` בשורה הראשונה יש סימן `&` מיותר והשורה השנייה תקינה",
                "ברשימת פרמטרי `fwrite` בשורה השנייה יש סימן `&` מיותר והשורה הראשונה תקינה",
                "ברשימות פרמטרי `fread` ו-`fwrite` יש סימן `&` מיותר",
                "שתי השורות תקינות",
                "באחת מהשורות או בשתי השורות סימן `&` נמצא במקום לא נכון",
                "אף טענה אינה נכונה")
Q4D_EXPL = r"""גם `fread` וגם `fwrite` מקבלות כפרמטר מצביע לבלוק הזיכרון. לכן צריך להציב כתובת של המשתנה."""

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
void main()
{
    printf("%d",printf("%d%d",printf("%d",11),printf("%d",11)));
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:**
```
1111222
```
**נימוק:**
כל אחת מהפונקציות `printf("%d",11)` מדפיסה 11, סה"כ 1111. פונקציית `printf` מחזירה מספר בתים כתובים, לכן כל אחת מהפונקציות הנ"ל מחזירה 2. אז `printf` שלישית (מימין) מדפיסה 22 (שני תווים) ומחזירה 2. לכן `printf` חיצונית (רביעית מימין) מדפיסה 2."""

questions = [
    Q(1, "code", "files", Q1_TEXT, Q1_SOL, points=40,
      hold="official solution fails its own example (stray blank lines in outfile when the files differ in length); see ASK_ADIR 21B-B Q1",
      confidence="low"),
    Q(2, "code", "structs_unions", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "list_manipulation", Q3_TEXT, Q3_SOL, points=40, image="images/exams/21B-B-Q3.png"),
    Q(4, "code", "storage_classes", Q4A_TEXT, Q4A_SOL, part="א"),
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "bit_manipulation", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "b", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "dynamic_memory", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "c", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "files", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "d", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
    Q(5, "code", "c_basics_output", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "21B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"א, מועד ב'",
    "year": 2021,
    "examDate": "13.07.2021",
    "sourceFile": "21B-B exam",
    "solutionFile": "21B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
