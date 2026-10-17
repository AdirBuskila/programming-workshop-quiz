# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-A.json -- programming-workshop (C), semester B 2022, moed A (23.06.22).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of the three), Part 2: Q4 a-d (20 pts, MCQ with justification),
Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/22B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_22B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-A.json"
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
Q1_TEXT = r"""כתבו פונקציה בשם `duplicateString` אשר מקבלת מחרוזת בסיס `base`, מחרוזת אמצע `middle` ומספר שלם `times`.

על הפונקציה ליצור ולהחזיר מחרוזת דינאמית חדשה המהווה שרשור של מחרוזת הבסיס עם מחרוזת האמצע לסירוגין.
מחרוזת הבסיס תופיע `times` פעמים כתת-מחרוזת במחרוזת החדשה. מחרוזת האמצע לא תהיה בתחילת ובסוף המחרוזת החדשה ותופיע כתת-מחרוזת רק בין מחרוזת הבסיס.

**לדוגמא,** עבור `times = 3` המחרוזת החדשה תיראה כך:
```
base | middle | base | middle | base
```
ניתן להניח שיש בזיכרון מספיק מקום להקצאת המחרוזת.""" + PART1

Q1_SOL = r"""```c
char* duplicateString(char* base, char* middle, int times)
{
    // zeroed dynamic array
    char* str = calloc(times * strlen(base) + (times - 1) * strlen(middle) + 1,
        sizeof(char));
    int i;

    for (i = 1; i <= times - 1; i++)
    {
        strcat(str, base);
        strcat(str, middle);
    }
    strcat(str, base);
    return str;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתון מספר חיובי שלם `M` המיוצג באמצעות רשימה מקושרת `L`, כך שכל איבר ברשימה מכיל ספרה אחת של המספר (הספרה המשמעותית ביותר של `M` - באיבר הראשון של `L`, ..., הספרה הכי פחות משמעותית של `M` - באיבר האחרון של `L`).

כתבו פונקציה `void` בשם `List_num_add` המקבלת מצביע לראש הרשימה `L` ומספר חיובי שלם `N`.
על הפונקציה להגדיל ב-`N` את המספר `M` המיוצג ע"י `L` (כלומר להפוך `L` לרשימה מקושרת שתייצג את המספר `M+N`). במידת הצורך להאריך את הרשימה (במקרה זה ניתן להניח שיש בזיכרון מספיק מקום להקצאה).

**שימו לב.** אין ליצור רשימה חדשה אלא רק לעדכן את הרשימה המקורית.

**דוגמא:**
המספר 9994 ירשם כמתואר להלן, כך שהספרה הראשונה מופיעה בראש הרשימה והאחרונה בזנבה. לאחר הוספת הערך 18, הרשימה תראה כך (באיור).

יש להגדיר את הטיפוס של איברי הרשימה מעל הפונקציה.""" + PART1

Q2_SOL = r"""```c
typedef struct item {
    int data;
    struct item* next;
}Item;

/* Auxiliary function: estimation of the size of a number */
int countDigit(int number)
{
    int j = 0;
    while (number)
    {
        ++j;
        number /= 10;
    }
    return j;
}
```
**גרסה 1:**
```c
void List_num_add_1(Item* head, int N)
{
    int i, p, k, new_size, number = 0;
    Item* node = head;

    /* Creating a number from the list */
    while (node)
    {
        number = number * 10 + node->data;
        node = node->next;
    }

    number += N; //new number
    new_size = countDigit(number); //the size of a new number

    /* List transformation for a new number */
    p = (int)pow(10, new_size);
    node = head;
    for (i = 0; i < new_size; ++i)
    {
        p /= 10;
        k = number / p;
        node->data = k;
        number = number - k * p;
        if (!node->next && i < new_size - 1)  //additional element
            node->next = (Item*)calloc(1, sizeof(Item));
        node = node->next;
    } //for
}
```
**גרסה 2:**
```c
void List_num_add(Item* head, int N)
{
    int i, p, k, size = 0, new_size, number = 0, diff;
    Item* node = head;

    /* Creating a number from the list */
    while (node)
    {
        number = number * 10 + node->data;
        node = node->next;
        size++;
    }

    number += N; //new number
    new_size = countDigit(number); //the size of a new number
    diff = new_size - size;

    /* Addition of new elements for a new number */
    if (diff > 0)
    {
        node = head;
        while (node->next) //search of a last element
            node = node->next;
        for (i = 1; i <= diff; i++) //diff new elements
        {
            node->next = (Item*)malloc(sizeof(Item));
            node = node->next;
        }
        node->next = NULL;
    }

    /* List filling for a new number */
    p = (int)pow(10, new_size);
    node = head;
    while (node)
    {
        p /= 10;
        k = number / p % 10;
        node->data = k;
        node = node->next;
    }
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""נתונה הגדרת המבנה הבאה:
```c
typedef struct {
    char address[30];
    int rooms;
    int price;
} apartment;
```
המתארת מידע על דירה למכירה במשרד תיווך, כאשר:
- `address` - הכתובת של הדירה למכירה,
- `rooms` - מספר החדרים בדירה,
- `price` - מחיר הדירה.

כתבו פונקציה בשם `appropriateAppartment` אשר מקבלת מחרוזת `fileName` המהווה שם של **קובץ בינארי**. הקובץ מורכב מרשומות הנתונים שהפורמט של כל אחת מהן מתאים למבנה `apartment`. כמו כן, הפונקציה מקבלת כפרמטרים את מספר החדרים הרצוי לקונה (מספר שלם `room_number`) ואת המחיר המקסימאלי שהקונה מוכן לשלם (מספר שלם `max_price`).

על הפונקציה ליצור מערך דינאמי של מבני `apartment`. המערך יכיל את נתוני כל הדירות של הקובץ שמחירן אינו עולה על `max_price` ושמספר חדריהן שווה ל-`room_number`.
הפונקציה תחזיר את כתובת תחילת המערך ותעביר (`by reference`) את גודלו.
אם אף דירה בקובץ לא מתאימה לתנאים לעיל או הקובץ לא נפתח, הפונקציה תחזיר `NULL` ותעביר 0.

**דוגמא:**
עבור הקובץ הבא (הרשומות משמאל לימין):
```
address   Begin 7   Reznik 4   Ben-Gurion 27   Dubnov 13   Cohen 66
rooms     3         4          5               3           3
price     700,000   1,000,000  4,000,000       1,100,000   900,000
```
ו-`room_number=3`, `max_price=1,000,000` הפונקציה תיצור את המערך
```
address   Begin 7   Cohen 66
rooms     3         3
price     700,000   900,000
```
ותעביר 2.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת המערך.""" + PART1

Q3_SOL = r"""```c
apartment* appropriateAppartment(char* fileName, int room_number, int max_price,
    int* count)
{
    int i=0;
    FILE* fptr = fopen(fileName, "rb");
    apartment* approp_apart_units, unit;
    *count = 0;
    if (!fptr)
        return NULL;

    /* Estimation of array size */
    fread(&unit, sizeof(apartment), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.rooms == room_number && unit.price <= max_price)
            (*count)++;
        fread(&unit, sizeof(apartment), 1, fptr);
    }

    if (*count == 0)
    {
        fclose(fptr);
        return NULL;
    }

    approp_apart_units = (apartment*)calloc(*count, sizeof(apartment)); //array allocation

    /* Filling of array */
    rewind(fptr);
    fread(&unit, sizeof(apartment), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.rooms == room_number && unit.price <= max_price)
            approp_apart_units[i++] = unit;
        fread(&unit, sizeof(apartment), 1, fptr);
    }

    fclose(fptr);
    return approp_apart_units;
}
```"""

# ---------------------------------------------------------------- Q4 (a-d, MCQ with justification)
Q4_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 4, 20 נק' בסך הכול; חובה לרשום את הבחירה והנימוק במחברת).\n"

Q4A_TEXT = Q4_INTRO + r"""נתון קובץ טקסט בעל התוכן הבא: `1 2 3 4 5` (משמאל לימין). אחרי כל אחד מחמישה המספרים (גם אחרי 5) יש רווח. מיד אחרי הפתיחה המוצלחת של הקובץ באמצעות מצביע `fptr` מופיע הקטע הבא בתוכנית (`x` הוא משתנה מסוג `int`):
```c
while (!feof(fptr)) {
    fscanf(fptr, "%d", &x);
    printf("%d ", x);
}
```
כמה פעמים מבוצע גוף הלולאה?"""
Q4A_OPTS = opts("5 פעמים", "4 פעמים", "מספר אינסופי פעמים", "פעם אחת", "אף תשובה אינה נכונה")
Q4A_EXPL = "הקוד מאורגן בצורה לא תקינה - ללא קלט לפני בדיקת סוף הקובץ. כתוצאה אחרי טיפול בחמישה המספרים השמורים נכנס לתוך הלולאה גם בפעם השישי כאשר נהיה כבר בסוף הקובץ."

Q4B_TEXT = Q4_INTRO + r"""נתונה ההצהרה:
```c
double (**q) ();
```
על מה מצביע פוינטר `q`?"""
Q4B_OPTS = opts("על פוינטר ל-`double`", "על פונקציה", "על פוינטר לפונקציה", "על פוינטר לפוינטר ל-`double`",
                "`q` זה לא פוינטר אלא פונקציה", "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי תחביר שפת C, `q` זה פוינטר לפוינטר לפונקציה ללא פרמטרים אשר מחזירה `double`. ז\"א, `q` מצביע על פוינטר לפונקליה."

Q4C_TEXT = Q4_INTRO + r"""נתון פוינטר ל-`int` בשם `p`. בחרו מה יקרה אחרי ביצוע פעולת
```c
p = (int*)malloc(0);
```"""
Q4C_OPTS = opts("`malloc` תקצה ביית אחד בעל אינדקס 0", "`p` יצביע על איזשהו מקום", "`p` יהיה שווה ל-`NULL`",
                "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4C_EXPL = "במידה והפרמטר של `malloc` שווה ל-0 , הפונקציה לא מקצה זיכרון אבל לא מחזירה `NULL`."

Q4D_TEXT = Q4_INTRO + r"""בתוכנית נתונה ההצהרה הבאה:
```c
char *str = "hello";
```
בחרו מה יקרה אחרי ביצוע פעולת
```c
str = "good-bye";
```"""
Q4D_OPTS = opts("ישתנה ערך של מצביע `str`", "תוכן המערך `str` ישתנה ל-\"good-bye\"", "תוכן המערך `str` ישתנה ל-\"good-\"",
                "תוכן המערך `str` ישתנה ל-\"good-byehello\"", "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4D_EXPL = "לא מוגדר פה מערך ו-`str` הוא מצביע. עבור הגדרה זו של `str` המחשב מקצה שטח זיכרון ל-`str` ולמחרוזת \"hello\" ומציב ל-`str` את כתובת התו הראשון של המחרוזת."

# ---------------------------------------------------------------- Q5
Q5_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <math.h>

void main()
{
    int z='z'-1;
    putchar(z-(int)pow((z^1)-z,z<<1));
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:** `x`

**נימוק:**
בשורה הראשונה משתנה `z` מקבל ערך שקטן ב-1 מקוד ASCII של `'z'`, ז"א קוד ASCII של `'y'`. ייצוג בינארי של 1 מורכב מאפסים וסיבית 1 בסוף. לפי כללי פעולת `^` (XOR), `a^0=a`, `a^1=ā`. לכן `z^1` שונה מ-`z` רק בסיבית ימנית ולכן הפרש ביניהם הוא 1 או -1. אחרי הזזת שמאלה סיביות של `z`, הסיבית הימנית של `z` תהיה 0 ולכן זה מספר זוגי. לכן `z^1` בחזקת `z<<1` שווה ל-1. `z` שווה לקוד ASCII של `'y'` ואז `z-1` שווה לקוד ASCII של `'x'`. לכן הפלט הוא `x`.

**הערת מתמלל (לא חלק מהפתרון הרשמי):** בקוד עצמו בסיס החזקה הוא `(z^1)-z`, וערכו -1 (`z` אי-זוגי ולכן `z^1 = z-1`), והמעריך `z<<1` זוגי, ולכן החזקה שווה ל-1. הנימוק הרשמי מקצר את הביטוי. הפלט נבדק בהרצה: `x`."""

questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/22B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    {"num": 4, "part": "א", "kind": "mcq", "topic": "files", "question": Q4A_TEXT,
     "options": Q4A_OPTS, "correctId": "e", "explanation": Q4A_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "pointers", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "c", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "dynamic_memory", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "b", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "strings", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "a", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
    Q(5, "code", "bit_manipulation", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "22B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ב, מועד א'",
    "year": 2022,
    "examDate": "23.06.2022",
    "sourceFile": "22B-A exam",
    "solutionFile": "22B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
