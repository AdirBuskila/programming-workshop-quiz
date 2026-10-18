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
Q4C_EXPL = "במידה והפרמטר של `malloc` שווה ל-0 , הפונקציה לא מקצה זיכרון אבל לא מחזירה `NULL`.\n\nהערה: לפי תקן C, התנהגות `malloc(0)` מוגדרת במימוש: היא עשויה להחזיר `NULL` או מצביע ייחודי שאסור לפנות דרכו. התשובה הרשמית (ב) נכונה במימושים הנפוצים (glibc, MSVC, clang על Windows), שמחזירים מצביע שאינו `NULL`, אבל אינה מובטחת על ידי התקן."

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

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run: tools/verify/22B-A/steps_check.py
# (probes + order/fillblank/findbug checks through verify/step_lib.py). Lines of order/findbug/fillblank come from the stored solutions.
def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip() and not ln.startswith("```")]


def clean(lines):
    """Drop comment-only lines and trailing // comments (they are not part of the logic being asked about)."""
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("/*") or s.startswith("//"):
            continue
        if "//" in ln:
            ln = ln[:ln.index("//")].rstrip()
        out.append(ln)
    return out


def func_lines(src, header_start):
    """The code lines of the function whose header line starts with header_start, to its closing brace."""
    ls = clean(lines_of(src))
    i0 = [i for i, ln in enumerate(ls) if ln.startswith(header_start)]
    assert len(i0) == 1, header_start
    i1 = next(i for i in range(i0[0], len(ls)) if ls[i] == "}")
    return ls[i0[0]:i1 + 1]


def swap(lines, old, new, nth=0):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == old.strip()]
    assert len(idx) > nth and (nth > 0 or len(idx) == 1), old
    out = list(lines)
    out[idx[nth]] = out[idx[nth]].replace(old.strip(), new.strip())
    return out, idx[nth]


def blank(lines, target, nth=0):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == target]
    assert len(idx) > nth and (nth > 0 or len(idx) == 1), target
    return [("___" if i == idx[nth] else ln) for i, ln in enumerate(lines)], idx[nth]


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            q.update(kw)
            return
    raise KeyError(num)


# Q1
F1 = func_lines(Q1_SOL, "char* duplicateString")
k1 = next(i for i, ln in enumerate(F1) if ln.strip().startswith("char* str = calloc("))
F1[k1] = F1[k1].rstrip() + " " + F1[k1 + 1].strip()  # the allocation line, joined
del F1[k1 + 1]
b1, i1 = swap(F1, "strcat(str, base);", "strcat(str, middle);", nth=1)
f1, j1 = blank(F1, "for (i = 1; i <= times - 1; i++)")
Q1_BODY = ["char* str = calloc(times * strlen(base) + (times - 1) * strlen(middle) + 1, sizeof(char)); int i;",
           "for (i = 1; i <= times - 1; i++) { strcat(str, base); strcat(str, middle); }",
           "strcat(str, base);",
           "return str;"]
add(1,
    rubric=rub(("הקצאת מחרוזת בגודל `times*strlen(base) + (times-1)*strlen(middle) + 1`, כולל מקום לתו הסיום", 12),
               ("איפוס הזיכרון (`calloc`), כדי שה-`strcat` הראשון יתחיל ממחרוזת ריקה", 6),
               ("לולאה של `times-1` צירופים: מחרוזת הבסיס ואחריה מחרוזת האמצע", 12),
               ("צירוף מחרוזת הבסיס האחרונה בלי אמצע אחריה, והחזרת המחרוזת החדשה", 10)),
    rubricSource="ai-verified",
    pitfalls=["לשכוח את ה-`+1` לתו הסיום בגודל ההקצאה, או לספור `times` פעמים את מחרוזת האמצע במקום `times-1`.",
              "להשתמש ב-`malloc` בלי לאפס את התא הראשון: `strcat` מחפשת את תו הסיום של היעד, והוא לא מובטח.",
              "לצרף את מחרוזת האמצע גם אחרי הבסיס האחרון (לולאה של `times` צירופים)."],
    steps=[
        {"type": "numeric",
         "prompt": "קוראים ל-`duplicateString(\"ab\", \"-\", 3)`. מה אורך המחרוזת שמוחזרת (`strlen`)?",
         "answer": 8, "tol": 0,
         "explain": "התוצאה היא `ab-ab-ab`: שלושה בסיסים ושתי מחרוזות אמצע, 3·2 + 2·1 = 8 (ריצה אמיתית: 8)."},
        {"type": "numeric",
         "prompt": "כמה בתים מקצה `calloc` באותה קריאה (`times = 3`, `base = \"ab\"`, `middle = \"-\"`)?",
         "answer": 9, "tol": 0,
         "explain": "3·2 + (3-1)·1 + 1 = 9, כולל תו הסיום (ריצה אמיתית: 9)."},
        {"type": "fillblank", "prompt": "השלימו את כותרת הלולאה שמצרפת את הזוגות (בסיס + אמצע).", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": opts("for (i = 1; i <= times - 1; i++)", "for (i = 1; i < times - 1; i++)",
                         "for (i = 0; i <= times - 1; i++)", "for (i = 1; i <= times; i++)"),
         "correctId": "a",
         "explain": "מצרפים `times-1` זוגות ואחריהם בסיס אחד אחרון. חלופה ב' מצרפת זוג אחד פחות, וחלופות ג' ו-ד' זוג אחד יותר (ריצה אמיתית: הפלט שונה)."},
        {"type": "order", "prompt": "סדרו את גוף הפונקציה `duplicateString`. כל שורה היא בלוק לוגי אחד.", "code": True,
         "lines": Q1_BODY,
         "explain": "הקצאה והצהרה, זוגות בסיס+אמצע, הבסיס האחרון, והחזרה. החלפת שני בלוקים משנה את הפלט או שוברת את הקומפילציה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ועבור `(\"ab\", \"-\", 3)` מתקבל `ab-ab--` במקום `ab-ab-ab`. מצאו אותה.",
         "code": True, "lines": b1, "bugIndex": i1,
         "explain": "הצירוף האחרון הוא של מחרוזת האמצע במקום הבסיס (ריצה אמיתית: `ab-ab--`)."},
    ],
    stepsSource="ai-verified")

# Q2
F2 = func_lines(Q2_SOL, "void List_num_add(Item* head")
b2, i2 = swap(F2, "p = (int)pow(10, new_size);", "p = (int)pow(10, size);")
f2, j2 = blank(F2, "k = number / p % 10;")
Q2_BODY = ["int i, p, k, size = 0, new_size, number = 0, diff; Item* node = head;",
           "while (node) { number = number * 10 + node->data; node = node->next; size++; }",
           "number += N; new_size = countDigit(number); diff = new_size - size;",
           "if (diff > 0) { node = head; while (node->next) node = node->next; for (i = 1; i <= diff; i++) { node->next = (Item*)malloc(sizeof(Item)); node = node->next; } node->next = NULL; }",
           "p = (int)pow(10, new_size); node = head; while (node) { p /= 10; k = number / p % 10; node->data = k; node = node->next; }"]
add(2,
    rubric=rub(("בניית המספר `M` מספרות הרשימה (`number = number*10 + node->data`) וספירת האיברים", 10),
               ("חישוב `M+N` ומספר הספרות החדש, וההפרש מגודל הרשימה", 8),
               ("הוספת האיברים החסרים בסוף הרשימה הקיימת, בלי ליצור רשימה חדשה", 10),
               ("כתיבת הספרות מחדש מהמשמעותית ביותר לפחות משמעותית באמצעות חזקות של 10", 12)),
    rubricSource="ai-verified",
    pitfalls=["ליצור רשימה חדשה במקום לעדכן את הקיימת, או להוסיף איבר בראש הרשימה: הפונקציה מקבלת את `head` by value, ולכן הקורא לא יראה ראש חדש.",
              "לשכוח שמספר הספרות יכול לגדול (`9994 + 18 = 10012`) ולא להאריך את הרשימה.",
              "לכתוב את הספרות מהקטנה לגדולה, או לשכוח את `% 10` ולכתוב מספר שלם בכל איבר."],
    steps=[
        {"type": "numeric",
         "prompt": "הרשימה מייצגת את `9994` ו-`N = 18`. כמה איברים צריך להוסיף לרשימה?",
         "answer": 1, "tol": 0,
         "explain": "9994 + 18 = 10012 מכיל 5 ספרות, ובראשונה 4, ולכן מוסיפים איבר אחד (ריצה אמיתית: `countDigit(10012) - countDigit(9994) = 1`)."},
        {"type": "choice",
         "prompt": "היכן מוסיפים את האיברים החסרים, ומה עושים אחר כך?",
         "options": opts("בסוף הרשימה, ואז כותבים מחדש את כל הספרות מהראשונה לאחרונה",
                         "בראש הרשימה, ומחזירים לקורא את הראש החדש דרך הפרמטר `head`",
                         "בסוף הרשימה, ומשאירים את הספרות הישנות בלי לשנות אותן",
                         "לא מוסיפים איברים, אלא כותבים באיבר הראשון מספר בן כמה ספרות"),
         "correctId": "a",
         "explain": "`head` מועבר by value, ולכן שינוי שלו לא מגיע לקורא (ריצה אמיתית: הרשימה של הקורא נשארה `9994`). אחרי ההארכה כל הספרות משתנות (10012 אחרי 9994), ולכן כותבים את כולן מחדש."},
        {"type": "fillblank", "prompt": "השלימו את השורה שמחשבת את הספרה שנכתבת באיבר הנוכחי.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": opts("k = number / p % 10;", "k = number / p;", "k = number % p;", "k = number % 10;"),
         "correctId": "a",
         "explain": "`number / p` מוריד את הספרות הימניות, ו-`% 10` משאיר את הספרה האחרונה שנשארה. בלעדיו נכתב מספר בן כמה ספרות, ועם `number % 10` נכתבת אותה ספרה בכל האיברים (ריצה אמיתית)."},
        {"type": "order", "prompt": "סדרו את גוף הפונקציה `List_num_add`. כל שורה היא בלוק לוגי אחד.", "code": True,
         "lines": Q2_BODY,
         "explain": "הצהרות, קריאת המספר מהרשימה, חישוב הסכום וגודלו, הארכת הרשימה, וכתיבת הספרות. החלפת שני בלוקים שוברת את הקומפילציה או משנה את הרשימה שמתקבלת (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, והתוכנית קורסת (חלוקה באפס) כשמוסיפים 18 ל-`9994`. מצאו אותה.",
         "code": True, "lines": b2, "bugIndex": i2,
         "explain": "החזקה צריכה להתאים למספר הספרות החדש (`new_size`) ולא לישן (`size`). עם `size` החזקה קטנה בספרה אחת, ובאיבר האחרון `p` מתאפס ו-`number / p` מחלק באפס (ריצה אמיתית: קריסה)."},
    ],
    stepsSource="ai-verified")

# Q3
F3 = func_lines(Q3_SOL, "apartment* appropriateAppartment")
b3, i3 = swap(F3, "if (unit.rooms == room_number && unit.price <= max_price)",
              "if (unit.rooms == room_number && unit.price < max_price)", nth=1)
f3, j3 = blank(F3, "rewind(fptr);")
add(3,
    rubric=rub(("פתיחת הקובץ בבינארי (`\"rb\"`), איפוס `*count` והחזרת `NULL` כשהפתיחה נכשלת", 8),
               ("מעבר ראשון שסופר את הדירות עם `rooms == room_number` ו-`price <= max_price`", 10),
               ("החזרת `NULL` כשאין דירה מתאימה, אחרת הקצאת מערך בגודל `*count`", 10),
               ("`rewind` ומעבר שני שמעתיק את הדירות המתאימות, סגירת הקובץ והחזרת המערך", 12)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב `<` במקום `<=` במחיר: דירה שמחירה בדיוק `max_price` צריכה להיכלל.",
              "לא לחזור לתחילת הקובץ לפני המעבר השני, והמערך נשאר אפסים.",
              "לבדוק `feof` לפני הקריאה הראשונה, ואז הרשומה האחרונה נספרת פעמיים."],
    steps=[
        {"type": "numeric",
         "prompt": "בקובץ הדוגמה (חמש הרשומות) קוראים לפונקציה עם `room_number = 3` ו-`max_price = 1,100,000`. כמה דירות יעמדו בתנאים?",
         "answer": 3, "tol": 0,
         "explain": "מתאימות `Begin 7`, `Dubnov 13` (מחיר בדיוק 1,100,000) ו-`Cohen 66`. הדירות עם 4 ו-5 חדרים נפסלות (ריצה אמיתית: 3)."},
        {"type": "numeric",
         "prompt": "מה הערך של `sizeof(apartment)` (30 בתים לכתובת, ושני `int`, כולל ריפוד)?",
         "answer": 40, "tol": 0,
         "explain": "30 בתים, ריפוד של 2 עד היסט 32, ועוד 4 + 4: סך הכול 40 (ריצה אמיתית: 40)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה שבין שני המעברים על הקובץ.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": opts("rewind(fptr);", "fseek(fptr, 0, SEEK_END);", "fseek(fptr, sizeof(apartment), SEEK_SET);", "*count = 0;"),
         "correctId": "a",
         "explain": "המעבר השני חייב להתחיל מהרשומה הראשונה. בכל חלופה אחרת הוא מדלג על רשומות או לא קורא אותן, והפלט שונה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה. כשיש דירה שמחירה שווה בדיוק ל-`max_price`, היא חסרה בתוצאה ובסוף המערך יש רשומה ריקה. מצאו את השורה.",
         "code": True, "lines": b3, "bugIndex": i3,
         "explain": "במעבר השני נכתב `<` במקום `<=`, ולכן הדירה שנספרה במעבר הראשון לא מועתקת (ריצה אמיתית)."},
    ],
    stepsSource="ai-verified")

# Q5 (bonus; every intermediate value checked with a probe program)
add(5,
    rubric=rub(("`z = 'z' - 1` הוא הקוד של `'y'`, כלומר 121", 2),
               ("`(z^1) - z` שווה -1, כי `z` אי-זוגי ו-XOR עם 1 מוריד אותו ב-1", 3),
               ("המעריך `z<<1` זוגי, ולכן `(-1)` בחזקתו שווה 1", 3),
               ("`z - 1` הוא הקוד של `'x'`, ולכן הפלט `x`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא את `^` כחזקה ולא כ-XOR: אז `(z^1)-z` הוא `121-121 = 0`, החזקה היא 0, והפלט שגוי: התו `y` במקום `x` (נבדק בהרצה).",
              "לפסול את החזקה כ-`-1` ולהדפיס את התו `z`, אף שהמעריך `z<<1` תמיד זוגי."],
    steps=[
        {"type": "numeric", "prompt": "מה הערך של `z` אחרי `int z='z'-1;`?", "answer": 121, "tol": 0,
         "explain": "קוד ה-ASCII של `'z'` הוא 122, ולכן `z = 121`, קוד של `'y'` (ריצה אמיתית: 121)."},
        {"type": "numeric", "prompt": "מה הערך של הביטוי `(z^1)-z`?", "answer": -1, "tol": 0,
         "explain": "`z` אי-זוגי, ולכן `z^1 = z-1 = 120` (ריצה אמיתית: -1)."},
        {"type": "numeric", "prompt": "מה הערך של `(int)pow((z^1)-z, z<<1)`?", "answer": 1, "tol": 0,
         "explain": "הבסיס -1 והמעריך 242 זוגי, לכן התוצאה 1 (ריצה אמיתית: 1)."},
        {"type": "text", "prompt": "מה מודפס? (תו אחד)", "accept": ["x"], "normalize": "none",
         "explain": "`putchar(121 - 1)` מדפיסה את התו שקודו 120, כלומר `x` (ריצה אמיתית: `x`)."},
    ],
    stepsSource="ai-verified")


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
