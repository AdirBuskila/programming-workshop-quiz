# -*- coding: utf-8 -*-
"""Generator for tools/raw/23B-B.json -- programming-workshop (C), semester B 2023, moed B (29.06.2023).
Part 1: Q1 (40). Part 2: Q2/Q3 (40 each, answer one). Part 3: Q4 (10), Q5 a/b (10 total). Part 4: Q6 bonus (10).
Solutions and keys transcribed from the official solution PDF (typed answers in the answer boxes).
Code solutions compiled and run with clang: tools/verify/23B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_23B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "23B-B.json"
IDS = "abcdef"


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

Q5A_TEXT = Q5_INTRO + r"""איזה פעולה לא תיתן פלט `0`?
```c
(1) printf("%d\n", 0);
(2) printf("%.0lf\n", 0.0);
(3) printf("%d\n", NULL);
(4) printf("%d\n", '0');
(5) printf("%d\n", '\0');
(6) printf("%d\n", EOF + 1);
(7) כל הפעולות לעיל יתנו פלט 0
```"""

Q5A_SOL = r"""**התשובה:** (4) `printf("%d\n", '0');`

**נימוק:**
(1) מדפיסים מספר שלם 0.
(2) מדפיסים מספר ממשי 0.0 עם אפס ספרות אחרי הנקודה, ז"א מדפיסים רק 0.
(3) `NULL` הוא שם של קבוע 0. לכן מדפיסים 0.
(4) קוד ASCII של תו `'0'` הוא המספר ששונה מ-0. לכן מדפיסים לא 0.
(5) קוד ASCII של תו `'\0'` הוא 0. לכן מדפיסים 0.
(6) קוד ASCII של תו `EOF` הוא -1. לכן מדפיסים ערך של 1+1-, ז"א 0."""

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
    # Q5 part a has seven options (the mcq engine allows at most six), so it is a "code" item with the key in the solution.
    Q(5, "code", "c_traps_mcq", Q5A_TEXT, Q5A_SOL, part="א"),
    {"num": 5, "part": "ב", "kind": "mcq", "topic": "pointers", "question": Q5B_TEXT,
     "options": Q5B_OPTS, "correctId": "f", "explanation": Q5B_EXPL, "official": True, "confidence": "high"},
    Q(6, "code", "bit_manipulation", Q6_TEXT, Q6_SOL, points=10),
]

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
