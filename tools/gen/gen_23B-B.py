# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- programming-workshop (C), semester B 2023, moed B (29.06.2023).
Part 1: Q1 (40). Part 2: Q2/Q3 (40 each, answer one). Part 3: Q4 (10), Q5 a/b (10 total). Part 4: Q6 bonus (10).
Solutions and keys transcribed from the official solution PDF (typed answers in the answer boxes).
Code solutions compiled and run with clang: tools/verify/23B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_23B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"
IDS = "abcdefgh"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


PART2 = "\n\n*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""נגדיר מבנה המייצג איבר ברשימה מקושרת:
```c
typedef struct node {
    int value;
    struct node* next;
} node;
```
כתבו את הפונקציה `node* JosephusPermutation(node* lst, int m)` אשר מממשת את **בעיית יוספוס** המתוארת להלן.
הפונקציה מקבלת פוינטר `lst` שמצביע על אחד מהאיברים מטיפוס `node` ברשימה מקושרת חד-כיוונית **מעגלית**, ואת הערך `m > 1`.
על הפונקציה לנתק כל איבר שבמקום `m` (`lst` מצביע על האיבר הראשון שממנו מתחילה הספירה) מתוך הרשימה המעגלית ולחבר אותו לרשימה חדשה חד-כיוונית **לא מעגלית**. ההעברה מסתיימת כאשר כל האיברים מרשימת המקור עוברים לרשימת היעד. סדר האיברים ברשימה החדשה יהיה לפי סדר ההוצאה.
הפונקציה תחזיר את הכתובת של הרשימה החדשה, או `NULL` אם הרשימה המקורית הייתה ריקה.

**לדוגמא:**
עבור הרשימה המעגלית `lst` הבאה (באיור) ו-`m = 3` הפונקציה תחזיר את הרשימה הבאה:
```
3 -> 6 -> 1 -> 5 -> 2 -> 8 -> 4 -> 7 -> NULL
```
**ההסבר:** יש לנתק ולהעביר לרשימה החדשה כל איבר שלישי. בהתאם, קודם עוברים האיברים 3, 6 ו-1. בשלב זה, האיברים שנשארים ברשימה המעגלית הם 2,4,5,7,8 (משמאל לימין). לכן, האיברים שעוברים אחר כך הם 5, 2 ו-8 והאיברים שנותרו הם 4,7 (משמאל לימין). לאחר מכן, מבקרים באיברים 4, 7 ושוב 4, ואיבר 4 עובר לרשימה החדשה. בשלב האחרון מבקרים באיבר 7 שלוש פעמים ברצף והוא גם מצטרף לרשימה החדשה.

**שימו לב:** הפונקציה אינה מקצה איברים חדשים, היא מנתקת את האיברים הקיימים ומעבירה אותם לרשימה החדשה."""

Q1_SOL = r"""```c
node* JosephusPermutation(node* lst, int m)
{
    int i;
    node* head = NULL;
    node* tail = NULL;
    node* tmp;
    while (lst != NULL)
    {
        for (i = 0; i < m - 2; i++)
            lst = lst->next;
        tmp = lst->next;
        lst->next = tmp->next;
        tmp->next = NULL;
        if (head == NULL)
            head = tail = tmp;
        else
        {
            tail->next = tmp;
            tail = tail->next;
        }
        lst = lst->next;
    }
    return head;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרת המבנה הבאה:
```c
typedef struct {
    char film_code[10];
    int copies;
    int year;
} film;
```
המתארת מידע על סרט במאגר, כאשר:
- `film_code` - קוד הסרט,
- `copies` - מספר העותקים של סרט מסוים,
- `year` - שנת הפקת הסרט.

כתבו פונקציה עם החתימה
```c
film * appropriateFilm(char * fileName, int copies_limit,
                       int last_year, int * size)
```
אשר מקבלת מחרוזת המהווה שם של **קובץ בינארי**. הקובץ מורכב מרשומות הנתונים שהפורמט של כל אחת מהן מתאים למבנה `film`.
על הפונקציה ליצור מערך דינאמי של מבני `film`. המערך יכיל את נתוני כל הסרטים הנדירים הישנים של הקובץ כך שמספר העותקים של כל אחד מהם אינו עולה על `copies_limit` ושנת ההפקה לא אחרי `last_year`. הפונקציה תחזיר את כתובת תחילת המערך ותעביר (`by reference`) את גודלו.
אם אף סרט בקובץ לא מתאים לתנאים לעיל או הקובץ לא נפתח, הפונקציה תחזיר `NULL` ותעביר 0.

לדוגמא, עבור הקובץ הבא (הרשומות משמאל לימין):
```
film_code   A346-f   D8120-fx   S516-t   R11-v   G555-xx
copies      2        4          1        2       3
year        1967     1960       1970     1972    2010
```
ו-`copies_limit=2`, `last_year=1970` הפונקציה תיצור את המערך
```
film_code   A346-f   S516-t
copies      2        1
year        1967     1970
```
ותעביר 2.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת המערך.""" + PART2

Q2_SOL = r"""```c
film* appropriateFilm(char* fileName, int copies_limit, int last_year, int* size)
{
    int i = 0;
    FILE* fptr = fopen(fileName, "rb");
    film* approp_film_units, unit;
    *size = 0;
    if (!fptr)
        return NULL;

    /* Estimation of array size */
    fread(&unit, sizeof(film), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.copies <= copies_limit && unit.year <= last_year)
            (*size)++;
        fread(&unit, sizeof(film), 1, fptr);
    }

    if (*size == 0)
    {
        fclose(fptr);
        return NULL;
    }

    approp_film_units = (film*)calloc(*size, sizeof(film)); //array allocation

    /* Filling of array */
    rewind(fptr);
    fread(&unit, sizeof(film), 1, fptr);
    while (!feof(fptr))
    {
        if (unit.copies <= copies_limit && unit.year <= last_year)
            approp_film_units[i++] = unit;
        fread(&unit, sizeof(film), 1, fptr);
    }

    fclose(fptr);
    return approp_film_units;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""נגדיר כמה תווים מסוימים כ**מפרידים**. במיוחד, תווי פסיק, נקודה, רווח, סימן קריאה, סימן שאלה, נקודתיים וכו' ניתן להגדיר כמפרידים.
**מילה** היא רצף של תווים שאינם מפרידים.
**משפט** הוא מחרוזת המכילה שרשור של מילים ומפרידים. המילים יכולות להיות מופרדות ע"י מפריד אחד או יותר. מפרידים יכולים להופיע גם בתחילת משפט ובסופו. משפט יכול להיות ריק.

כתבו פונקציה עם החתימה
```c
char * my_strtok(char * sentence, char * separators)
```
אשר מקבלת מחרוזת `sentence` המהווה את המשפט ומחרוזת `separators` המורכבת מכל המפרידים שעשויים להופיע במשפט.
הפונקציה תבחר ברצף מילים ממשפט באופן הבא.
הקריאה הראשונה מכילה את המשפט כארגומנט הראשון. הפונקציה תיצור מחרוזת דינאמית חדשה עם התוכן זהה למילה הראשונה (השמאלית) של המשפט ותחזיר אותה.
קריאות עוקבות מכילות `NULL` כארגומנט הראשון. הפונקציה תיצור ותחזיר מחרוזות זהות למילים הבאות של המשפט בהתאמה.
אם אין יותר מילים, כאשר הפונקציה נקראת היא תחזיר `NULL`.
הפונקציה לא תשנה את תוכן המשפט המקורי!

**אסור להשתמש** בפונקציה סטנדרטית `strtok` אשר מממשת את האלגוריתם הדומה להנ"ל!

**דוגמא:**
`sentence = “   Why?! That’s why.”` ו-`separators = “? !.”`.
הקריאה הראשונה תהיה `my_strtok(sentence, separators)`. הפונקציה תחזיר “Why”.
הקריאה השנייה תהיה `my_strtok(NULL, separators)`. הפונקציה תחזיר “That’s”.
הקריאה השלישית תהיה `my_strtok(NULL, separators)`. הפונקציה תחזיר “why”.
הקריאה הרביעית תהיה `my_strtok(NULL, separators)`. הפונקציה תחזיר `NULL`.

**רמז:**
יש להשתמש במשתנה `static`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.""" + PART2

Q3_SOL = r"""```c
char* my_strtok(char* sentence, char* separators)
{
    int i = 0;
    char* word;
    static char* start;
    if (sentence != NULL)
        start = sentence;
    word = (char*)malloc(strlen(start) + 1);
    while (*start && strchr(separators, *start)) // scan separators
        start++;
    while (*start && !strchr(separators, *start)) // scan word
    {
        word[i++] = *start;
        start++;
    }
    if (i > 0) // word was found
    {
        word[i] = '\0';
        word = (char*)realloc(word, i + 1);
        return word;
    }
    free(word);
    return NULL;
}
```"""

# ---------------------------------------------------------------- Q4
Q4_TEXT = r"""מהו הפלט של התוכנית הבאה?
```c
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <malloc.h>

#define SIZE 4

struct TsT {
    int val1;
    char val2[SIZE];
    char* val3;
};

void func1(struct TsT myTsT) {
    myTsT.val3[1] = 'Y';
    myTsT.val2[1] = 'Y';
    myTsT.val1 = 444;
};

void func2(struct TsT* myTsT) {
    myTsT->val3[1] = 'X';
    myTsT->val2[1] = 'X';
    myTsT->val1 = 222;
};

void main() {
    struct TsT p1, p2;

    p1.val3 = (char*)malloc(4);
    strcpy(p1.val3, "aaa");
    p1.val1 = 20;
    strcpy(p1.val2, "bbb");

    p2 = p1;
    printf("p1 Print1: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
    printf("p2 Print1: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);

    p2.val2[0] = 'Z';
    p2.val3[0] = 'Z';
    printf("p1 Print2: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
    printf("p2 Print2: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);

    func1(p1);
    func2(&p2);
    printf("p1 Print3: %d, %s, %s \n", p1.val1, p1.val2, p1.val3);
    printf("p2 Print3: %d, %s, %s \n", p2.val1, p2.val2, p2.val3);
}
```
יש לנמק את התשובה."""

Q4_SOL = r"""**הפלט:**
```
p1 Print1: 20, bbb, aaa
p2 Print1: 20, bbb, aaa
p1 Print2: 20, bbb, Zaa
p2 Print2: 20, Zbb, Zaa
p1 Print3: 20, bbb, ZXa
p2 Print3: 222, ZXb, ZXa
```
**נימוק:**
אחרי ביצוע `p2 = p1` כל שדה של מבנה `p1` מועתק לשדה התואם של מבנה `p2`. בהתאם, 20 מועתק ל-`p2.val1` ו-"bbb" מועתקת ל-`p2.val2`. אחרי העתקת `p1.val3` ל-`p2.val3` מקבלים שני פוינטרים אשר מצביעים לאותה מחרוזת "aaa".
לכן הפלט הראשון יהיה:
```
p1 Print1: 20, bbb, aaa
p2 Print1: 20, bbb, aaa
```
תו מס' 0 של `p2.val2` משתנה ל-'Z'. מצד שני, `p1.val3` ו-`p2.val3` הם שני שמות של אותה מחרוזת ובכך שינוי של `p2.val3[0]` ל-'Z' אומר גם שינוי של `p1.val3[0]` ל-'Z'.
לכן הפלט השני יהיה:
```
p1 Print2: 20, bbb, Zaa
p2 Print2: 20, Zbb, Zaa
```
מבנה `p1` מועבר `by value` לפונקציה `func1`. כל השדות שלו מועתקים לשדות המתאימים של מבנה `TsT`. שינויים בשדות `val1` ו-`val2` של העתק לא משפיעים על השדות של המקור. אבל `myTsT.val3` הוא פוינטר. לכן שינוי של תו מס' 1 של מחרוזת עליה הוא מצביע הוא למעשה שינוי של תו מס' 1 של המחרוזת עליה מצביעים `p1.val3` ו-`p2.val3`.
מבנה `p2` מועבר `by reference` לפונקציה `func2`. ז"א כל השינויים בשדות עלייהם מצביע פוינטר `myTsT` הם למעשה שינויים בשדות המבנה `p2`. בזאת, תו מס' 1 של המחרוזת עליה מצביעים `p1.val3` ו-`p2.val3`, משתנה שוב הפעם ל-'X'. בהתאם, תו `p2.val2[1]` משתנה ל-'X' ושדה `p2.val1` משתנה ל-222.
לכן הפלט השלישי יהיה:
```
p1 Print3: 20, bbb, ZXa
p2 Print3: 222, ZXb, ZXa
```"""

# ---------------------------------------------------------------- Q5
Q5_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\n"

Q5A_TEXT = Q5_INTRO + r"""איזה פעולה לא תיתן פלט `0`?"""
Q5A_OPTS = opts(r"""`printf("%d\n", 0);`""",
                r"""`printf("%.0lf\n", 0.0);`""",
                r"""`printf("%d\n", NULL);`""",
                r"""`printf("%d\n", '0');`""",
                r"""`printf("%d\n", '\0');`""",
                r"""`printf("%d\n", EOF + 1);`""",
                "כל הפעולות לעיל יתנו פלט 0")


Q5A_EXPL = r"""(1) מדפיסים מספר שלם 0.
(2) מדפיסים מספר ממשי 0.0 עם אפס ספרות אחרי הנקודה, ז"א מדפיסים רק 0.
(3) `NULL` הוא קבוע מצביע ריק (בדרך כלל `((void*)0)`), לא מספר שלם. העברתו ל-`%d` היא התנהגות לא מוגדרת (UB) בשפת C; בפועל במימושים נפוצים (למשל clang על x64) מודפס 0.
(4) קוד ASCII של תו `'0'` הוא המספר ששונה מ-0. לכן מדפיסים לא 0.
(5) קוד ASCII של תו `'\0'` הוא 0. לכן מדפיסים 0.
(6) `EOF` אינו קוד ASCII של תו: זהו קבוע שלם שלילי (מוגדר במימוש, בדרך כלל -1) שנבחר כך שלא יתבלבל עם אף תו. לכן `EOF + 1` הוא 0.

הערה: לפי תקן C ההדפסה ב-(3) היא התנהגות לא מוגדרת, אבל בפועל מודפס בה 0. התשובה הנכונה היא (4): רק `'0'` נותן ערך שונה מ-0 (קוד ASCII 48)."""

Q5B_TEXT = Q5_INTRO + r"""נתונה התוכנית הבאה:
```c
#include <stdio.h>

int f(int n) {
    int m = 2 * n;
    return m;
}

void main() {
    int k = 3;
    printf("%d\n", f(k));     // 1
    printf("%d\n", (*f)(k));  // 2
}
```
מה ההבדל בין הפעולה המסומנת ב-1 לפעולה המסומנת ב-2?"""
Q5B_OPTS = opts("פעולה 1 תציג ערך של משתנה לוקלי `m` ואילו פעולה 2 תציג את הכתובת של `m`",
                "פעולה 1 תציג ערך המוחזר ע\"י הקריאה `f(k)` ואילו פעולה 2 תציג את הערך מוכפל בעצמו",
                "פעולה 1 תציג ערך המוחזר ע\"י הקריאה `f(k)` ואילו פעולה 2 תציג את הערך מוכפל ב-`k`",
                "פעולה 2 בנוסף למה שמבצעת פעולה 1 גם משנה את הערך של `k`",
                "פעולה 2 פשוט לא תקינה",
                "פעולות 1 ו-2 שקולות")
Q5B_EXPL = "שם של פונקציה הוא למעשה שם הפוינטר שמצביע לתחילת הפונקציה. לכן `f` הוא פוינטר שמצביע לתחילת הפונקציה שלנו. ובכך, בפעולה 2 פונים לאותה פונקציה כמו בפעולה 1 אך במפורש דרך הפוינטר."

# ---------------------------------------------------------------- Q6
Q6_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
    char s[]={'^','^','^'^'^','^'};
    printf("%s",s);
}
```
יש לנמק את התשובה."""

Q6_SOL = r"""**הפלט:** `^^`

**נימוק:**
איבר מס' 0 ואיבר מס' 1 ב-`s` שווים ל-`'^'`. איבר מס' 2 הוא `'^' ^ '^'`, ז"א ערך של פעולת XOR על סיביות קודי ASCII של תו `'^'`. פעולת XOR על ערכים שווים נותנת 0. לכן הערך מורכב רק מסיביות 0, ז"א שווה ל-0 אשר מהווה קוד ASCII של `'\0'`. פונקציה `printf` מדפיסה מחרוזת עד `'\0'` הראשון.
לכן יודפסו שני התווים הראשונים: `^^`."""

questions = [
    Q(1, "code", "list_manipulation", Q1_TEXT, Q1_SOL, points=40, image="images/exams/23B-B-Q1.png"),
    Q(2, "code", "files", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "strings", Q3_TEXT, Q3_SOL, points=40),
    Q(4, "code", "structs_unions", Q4_TEXT, Q4_SOL, points=10),
    {"num": 5, "part": "א", "kind": "mcq", "topic": "c_traps_mcq", "question": Q5A_TEXT,
     "options": Q5A_OPTS, "correctId": "d", "explanation": Q5A_EXPL, "official": True, "confidence": "high"},
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "pointers", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "f", "explanation": Q5B_EXPL, "official": True, "confidence": "high"},
    Q(6, "code", "bit_manipulation", Q6_TEXT, Q6_SOL, points=10),
]

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run: tools/verify/23B-B/steps_check.py
# (probes + order/fillblank/findbug checks through verify/step_lib.py). Lines of order/findbug/fillblank come from the stored solutions.
def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip() and not ln.startswith("```")]


def func_lines(src, header_start):
    """The code lines of the function whose header line starts with header_start, to its closing brace."""
    ls = lines_of(src)
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
F1 = func_lines(Q1_SOL, "node* JosephusPermutation")
b1, i1 = swap(F1, "for (i = 0; i < m - 2; i++)", "for (i = 0; i < m - 1; i++)")
f1, j1 = blank(F1, "lst->next = tmp->next;")
add(1,
    rubric=rub(("לולאה חיצונית שרצה כל עוד הרשימה המעגלית אינה ריקה (`lst != NULL`)", 6),
               ("התקדמות של `m-2` צעדים, כך ש-`lst` מצביע על האיבר שלפני האיבר ה-`m` בספירה", 10),
               ("ניתוק האיבר מהרשימה המעגלית (`lst->next = tmp->next`) ואיפוס `tmp->next = NULL`, בלי להקצות איברים חדשים", 12),
               ("הוספה לסוף הרשימה החדשה: טיפול באיבר הראשון (`head`) ועדכון `tail`", 8),
               ("המשך הספירה מהאיבר שאחרי המנותק (`lst = lst->next`) והחזרת `head`", 4)),
    rubricSource="ai-verified",
    pitfalls=["להתקדם `m` צעדים (או `m-1`) במקום `m-2`: `lst` חייב לעצור על האיבר שלפני האיבר שמנתקים, כי כך אפשר לעדכן את `next` שלו.",
              "לשכוח `tmp->next = NULL`, ואז הרשימה החדשה נשארת מחוברת לשאר האיברים של הרשימה המעגלית.",
              "לא לטפל באיבר הראשון של הרשימה החדשה (`head == NULL`) ולכתוב ל-`tail->next` כשה-`tail` עדיין `NULL`."],
    steps=[
        {"type": "numeric",
         "prompt": "הרשימה המעגלית היא `1,2,...,8` והספירה מתחילה ב-`1`. עבור `m = 2`, מהו הערך של האיבר האחרון שעובר לרשימה החדשה?",
         "answer": 1, "tol": 0,
         "explain": "סדר ההוצאה הוא `2 4 6 8 3 7 5 1`, ולכן האחרון הוא 1 (ריצה אמיתית: 1)."},
        {"type": "choice",
         "prompt": "הרשימה היא `1,2,...,8`, `m = 3`, והספירה מתחילה ב-`1`. על איזה איבר מצביע `lst` מיד אחרי הלולאה `for (i = 0; i < m - 2; i++)`?",
         "options": opts("על האיבר שלפני האיבר שמנתקים (הערך 2)", "על האיבר שמנתקים (הערך 3)",
                         "על האיבר שאחרי האיבר שמנתקים (הערך 4)", "על האיבר שהספירה התחילה בו (הערך 1)"), "correctId": "a",
         "explain": "הלולאה מתקדמת צעד אחד, ולכן `lst` מצביע על 2 ו-`tmp = lst->next` הוא 3 (ריצה אמיתית: `lst->value = 2`, `tmp->value = 3`)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה שמנתקת את `tmp` מהרשימה המעגלית.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": opts("lst->next = tmp->next;", "lst->next = tmp;", "tmp->next = lst->next;", "lst = tmp->next;"),
         "correctId": "a",
         "explain": "האיבר שלפני `tmp` צריך לדלג עליו ולהצביע על האיבר שאחריו. בכל אחת מהחלופות האחרות האיבר נשאר ברשימה או שהרשימה נשברת, והפלט שונה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ועבור `1,...,8` ו-`m = 3` מתקבל סדר הוצאה שונה מ-`3 6 1 5 2 8 4 7`. מצאו אותה.",
         "code": True, "lines": b1, "bugIndex": i1,
         "explain": "`m - 1` צעדים במקום `m - 2` גורמים לניתוק האיבר הלא נכון (ריצה אמיתית: הפלט שונה מהמצופה)."},
    ],
    stepsSource="ai-verified")

# Q2
F2 = func_lines(Q2_SOL, "film* appropriateFilm")
b2, i2 = swap(F2, "if (unit.copies <= copies_limit && unit.year <= last_year)",
              "if (unit.copies < copies_limit && unit.year <= last_year)", nth=1)
f2, j2 = blank(F2, "rewind(fptr);")
add(2,
    rubric=rub(("פתיחת הקובץ בבינארי (`\"rb\"`), איפוס `*size` והחזרת `NULL` כשהפתיחה נכשלת", 8),
               ("מעבר ראשון על הקובץ שסופר את הרשומות שעומדות בשני התנאים (`copies <= copies_limit` ו-`year <= last_year`)", 10),
               ("החזרת `NULL` כשאין רשומה מתאימה, אחרת הקצאת מערך בגודל המדויק `*size`", 10),
               ("חזרה לתחילת הקובץ (`rewind`) ומעבר שני שמעתיק את הרשומות המתאימות, סגירת הקובץ והחזרת המערך", 12)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב `<` במקום `<=` (או `>=` לשנה): הסרט עם בדיוק `copies_limit` עותקים או בדיוק `last_year` חייב להיכלל.",
              "לשכוח `rewind` (או `fseek`) בין שני המעברים, ואז המעבר השני לא קורא אף רשומה והמערך נשאר אפסים.",
              "לבדוק `feof` לפני הקריאה הראשונה, ואז הרשומה האחרונה נספרת פעמיים."],
    steps=[
        {"type": "numeric",
         "prompt": "בקובץ הדוגמה (חמש הרשומות) קוראים לפונקציה עם `copies_limit = 3` ו-`last_year = 1972`. כמה רשומות יעמדו בשני התנאים?",
         "answer": 3, "tol": 0,
         "explain": "מתאימות `A346-f`, `S516-t` ו-`R11-v`. `D8120-fx` נפסל בגלל 4 עותקים, ו-`G555-xx` בגלל שנת 2010 (ריצה אמיתית: 3)."},
        {"type": "numeric",
         "prompt": "כל רשומה מטיפוס `film` תופסת 20 בתים (כולל ריפוד). מה גודל קובץ הדוגמה בבתים (חמש רשומות)?",
         "answer": 100, "tol": 0,
         "explain": "5 × 20 = 100 (ריצה אמיתית: `sizeof(film) = 20` וגודל הקובץ 100 בתים)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה שבין שני המעברים על הקובץ.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": opts("rewind(fptr);", "fseek(fptr, 0, SEEK_END);", "fseek(fptr, sizeof(film), SEEK_SET);", "*size = 0;"),
         "correctId": "a",
         "explain": "המעבר השני חייב להתחיל מהרשומה הראשונה. בכל חלופה אחרת הוא מדלג על רשומות או לא קורא אותן, והפלט שונה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה. בדוגמה (`copies_limit = 2`, `last_year = 1970`) הרשומה `A346-f` חסרה בתוצאה ובמקומה יש רשומה ריקה בסוף. מצאו את השורה.",
         "code": True, "lines": b2, "bugIndex": i2,
         "explain": "במעבר השני נכתב `<` במקום `<=`, ולכן הרשומה עם 2 עותקים לא מועתקת אף שנספרה במעבר הראשון (ריצה אמיתית)."},
    ],
    stepsSource="ai-verified")

# Q3
F3 = func_lines(Q3_SOL, "char* my_strtok")
b3, i3 = swap(F3, "word[i] = '\\0';", "word[i - 1] = '\\0';")
f3, j3 = blank(F3, "start = sentence;")
Q3_BODY = ["int i = 0; char* word; static char* start;",
           "if (sentence != NULL) start = sentence; word = (char*)malloc(strlen(start) + 1);",
           "while (*start && strchr(separators, *start)) start++;",
           "while (*start && !strchr(separators, *start)) { word[i++] = *start; start++; }",
           "if (i > 0) { word[i] = '\\0'; word = (char*)realloc(word, i + 1); return word; }",
           "free(word); return NULL;"]
add(3,
    rubric=rub(("משתנה `static` ששומר את המיקום בין הקריאות, ואיתחול שלו מהמשפט רק כשהארגומנט אינו `NULL`", 10),
               ("דילוג על מפרידים לפני המילה (עם בדיקת `*start` כדי לא לעבור את סוף המחרוזת)", 8),
               ("העתקת תווי המילה למחרוזת דינמית חדשה (בלי לשנות את המשפט) וסיום ב-`'\\0'`", 12),
               ("החזרת `NULL` (ושחרור הזיכרון) כשאין עוד מילים", 10)),
    rubricSource="ai-verified",
    pitfalls=["לא להשתמש ב-`static` ולאבד את המיקום בין הקריאות, או לשנות את המשפט המקורי (כמו ש-`strtok` עושה).",
              "לשכוח את בדיקת `*start` ב-`strchr(separators, *start)`: `strchr` מוצאת גם את תו הסיום `'\\0'`, ולכן הלולאה תעבור את סוף המחרוזת.",
              "לא לסיים את המילה ב-`'\\0'` או להחזיר מחרוזת ריקה במקום `NULL` כשאין עוד מילים."],
    steps=[
        {"type": "numeric",
         "prompt": "קוראים ל-`my_strtok` עם המשפט `\"a,,b,c,\"` והמפריד `\",\"`, ואחר כך שוב ושוב עם `NULL` עד לקבלת `NULL`. כמה מילים מוחזרות?",
         "answer": 3, "tol": 0,
         "explain": "המילים הן `a`, `b`, `c`. הפסיקים הכפולים והפסיק בסוף לא יוצרים מילים ריקות (ריצה אמיתית: 3)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה: מה קורה בקריאה הראשונה?", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": opts("start = sentence;", "sentence = start;", "start = sentence + 1;", "start = NULL;"),
         "correctId": "a",
         "explain": "בקריאה הראשונה `start` מקבל את תחילת המשפט. כל חלופה אחרת קורסת או מדלגת על התו הראשון, ולכן הפלט שונה (ריצה אמיתית)."},
        {"type": "order", "prompt": "סדרו את גוף הפונקציה `my_strtok`. כל שורה היא בלוק לוגי אחד.", "code": True,
         "lines": Q3_BODY,
         "explain": "הצהרות, אתחול `start` והקצאה, דילוג על מפרידים, קריאת המילה, החזרתה אם נמצאה, ואחרת שחרור והחזרת `NULL`. כל החלפה של שני בלוקים משנה את הפלט או שוברת את הקומפילציה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ועבור `\"   Why?! That's why.\"` כל מילה מוחזרת בלי התו האחרון שלה (`Wh` במקום `Why`). מצאו אותה.",
         "code": True, "lines": b3, "bugIndex": i3,
         "explain": "סיום המחרוזת ב-`word[i - 1]` חותך את התו האחרון של כל מילה (ריצה אמיתית: `Wh`)."},
    ],
    stepsSource="ai-verified")

# Q4 (output verified by running the program from the question)
Q4_LINES = ["p1 Print1: 20, bbb, aaa", "p2 Print1: 20, bbb, aaa", "p1 Print2: 20, bbb, Zaa",
            "p2 Print2: 20, Zbb, Zaa", "p1 Print3: 20, bbb, ZXa", "p2 Print3: 222, ZXb, ZXa"]
add(4,
    rubric=rub(("שורות `Print1`: `p2 = p1` מעתיקה את כל השדות, כולל הכתובת שנשמרת ב-`val3`", 2),
               ("שורות `Print2`: `val2` של `p2` הוא עותק נפרד (רק `p2` משתנה), ו-`val3` משותף לשני המבנים (שניהם משתנים)", 3),
               ("שורות `Print3`: `func1` מקבלת עותק, ולכן `val1` ו-`val2` של `p1` לא משתנים, אבל `val3[1]` משתנה דרך המצביע המשותף", 3),
               ("`func2` מקבלת כתובת ומשנה את `p2` עצמו: `val1 = 222`, `val2[1] = 'X'`, ואת `val3[1] = 'X'`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`p2 = p1` מעתיקה גם את המחרוזת ש-`val3` מצביע עליה, ולכתוב ש-`p1.val3` נשאר `aaa` אחרי השינוי דרך `p2`.",
              "לחשוב ש-`func1` (העברה by value) משנה את `p1.val1` ל-444 או את `p1.val2`, כשהיא משנה רק את התו המשותף בזיכרון הדינמי.",
              "לשכוח ש-`val3[1]` נכתב פעמיים (`'Y'` ב-`func1` ואחר כך `'X'` ב-`func2`), והערך הסופי הוא `'X'`."],
    steps=[
        {"type": "choice", "prompt": "מה מודפס בשורה `p1 Print2`?",
         "options": opts("`p1 Print2: 20, bbb, Zaa`", "`p1 Print2: 20, bbb, aaa`", "`p1 Print2: 20, Zbb, Zaa`", "`p1 Print2: 20, Zbb, aaa`"),
         "correctId": "a",
         "explain": "`val2` הוא מערך בתוך המבנה והועתק, ולכן `p1.val2` נשאר `bbb`. `val3` הוא מצביע משותף, ולכן התו הראשון שונה ל-`Z` גם ב-`p1` (ריצה אמיתית: `20, bbb, Zaa`)."},
        {"type": "choice", "prompt": "למה `p1.val3` השתנה ל-`Zaa` למרות שהשינוי בוצע דרך `p2`?",
         "options": opts("`p2 = p1` מעתיקה את הכתובת שב-`val3` ולא את המחרוזת, ולכן שני המצביעים מצביעים לאותו מקום בזיכרון",
                         "`p2 = p1` מעתיקה את המחרוזת ש-`val3` מצביע עליה, אבל `printf` מעדכנת את `p1` לפי `p2`",
                         "המערך `val2` משותף בין `p1` ל-`p2` ולכן `p1.val2` אמור היה להשתנות גם הוא",
                         "הפונקציה `malloc` מקצה זיכרון שמשותף אוטומטית לכל המבנים בתוכנית"),
         "correctId": "a",
         "explain": "העתקת מבנה היא העתקה של כל שדה. מצביע מועתק ככתובת בלבד. `p1.val2` נשאר `bbb` ולכן המערך לא משותף (ריצה אמיתית)."},
        {"type": "choice", "prompt": "מה מודפס בשורה `p1 Print3`?",
         "options": opts("`p1 Print3: 20, bbb, ZXa`", "`p1 Print3: 444, bbb, ZYa`", "`p1 Print3: 20, bYb, ZYa`", "`p1 Print3: 222, bbb, ZXa`"),
         "correctId": "a",
         "explain": "`func1` מקבלת עותק ולכן `val1` ו-`val2` של `p1` לא משתנים. `val3[1]` נכתב `'Y'` ואחר כך `'X'` על אותה מחרוזת (ריצה אמיתית: `20, bbb, ZXa`)."},
        {"type": "order", "prompt": "סדרו את ששת שורות הפלט של התוכנית, מהראשונה לאחרונה.", "code": True,
         "lines": Q4_LINES,
         "explain": "שני `printf` אחרי ההעתקה, שניים אחרי השינוי של `p2`, ושניים אחרי הקריאות לפונקציות (ריצה אמיתית: אותן שש שורות)."},
    ],
    stepsSource="ai-verified")

# Q6 (values checked with a probe program)
add(6,
    rubric=rub(("חישוב איברי המערך: שני תווי `'^'` ראשונים, והאיבר השלישי הוא `'^' ^ '^'` (XOR) ולא תו נוסף", 4),
               ("XOR של שני ערכים שווים הוא 0, שהוא `'\\0'` (תו סיום המחרוזת)", 3),
               ("`printf` עם `%s` מדפיסה עד ה-`'\\0'` הראשון, ולכן הפלט הוא `^^`", 3)),
    rubricSource="ai-verified",
    pitfalls=["לקרוא את הסוגריים כחמישה תווי `^` ולהדפיס `^^^^^`, כשהביטוי `'^'^'^'` הוא פעולת XOR אחת שנותנת איבר אחד.",
              "לחשוב שהתו האחרון `'^'` מודפס גם הוא, אף שהוא נמצא אחרי ה-`'\\0'`."],
    steps=[
        {"type": "numeric", "prompt": "כמה איברים יש במערך `s`? (`sizeof(s)`)", "answer": 4, "tol": 0,
         "explain": "האיברים: `'^'`, `'^'`, `'^'^'^'`, `'^'` (ריצה אמיתית: 4)."},
        {"type": "numeric", "prompt": "מה הערך של `s[2]`, כלומר של `'^' ^ '^'`?", "answer": 0, "tol": 0,
         "explain": "XOR של ערכים שווים נותן 0 (ריצה אמיתית: 0)."},
        {"type": "text", "prompt": "מה מודפס? (כתבו את התווים בלבד)", "accept": ["^^"], "normalize": "none",
         "explain": "`printf(\"%s\", s)` עוצרת ב-`s[2] = 0`, ולכן מודפסים רק `s[0]` ו-`s[1]` (ריצה אמיתית: `^^`)."},
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "23B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ג, מועד ב'",
    "year": 2023,
    "examDate": "29.06.2023",
    "sourceFile": "23B-B exam",
    "solutionFile": "23B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
