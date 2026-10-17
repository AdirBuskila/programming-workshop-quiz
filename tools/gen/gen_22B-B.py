# -*- coding: utf-8 -*-
"""Generator for tools/raw/22B-B.json -- programming-workshop (C), semester B 2022, moed B (25.07.22).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of the three), Part 2: Q4 a-d (20 pts, MCQ with justification),
Part 3: Q5 bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + marked options).
Code solutions compiled and run with clang: tools/verify/22B-B/. Run: PYTHONUTF8=1 py tools/gen/gen_22B-B.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "22B-B.json"
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
Q1_TEXT = r"""במחרוזת בעלת **אורך זוגי** (`2n`) **המחצית הראשונה** מורכבת מהתווים במקומות מס' 0 עד מס' `n-1` ו**המחצית השנייה** מורכבת מהתווים במקומות מס' `n` עד מס' `2n-1`.
במחרוזת בעלת **אורך אי-זוגי** (`2n+1`) **המחצית הראשונה** מורכבת מהתווים במקומות מס' 0 עד מס' `n-1` ו**המחצית השנייה** מורכבת מהתווים במקומות מס' `n+1` עד מס' `2n`. **התו האמצעי** (מס' `n`) לא שייך לאף מחצית.

כתבו פונקציה אשר מקבלת מחרוזת וסופרת מספר אותיות קטנות במחצית הראשונה ומספר אותיות גדולות במחצית השנייה. על הפונקציה להעביר את התוצאות `by reference`.
אם אורך המחרוזת הוא זוגי, הפונקציה תחזיר 0.
אם אורך המחרוזת הוא אי זוגי אז הפונקציה תחזיר 1 במקרה שהתו האמצעי הוא ספרה ו-1- בכל מקרה אחר.

**דוגמאות** (יש לקרוא את המחרוזות משמאל לימין):

עבור המחרוזת `"t&u5Y%as3k\$R"` (האורך הוא זוגי) הפונקציה תעביר 2 (מספר האותיות הקטנות במחצית הראשונה) ו-1 (מספר האותיות הגדולות במחצית השנייה) ותחזיר 0.

עבור המחרוזת `"t&u5Y%4as3k\$R"` (האורך הוא אי זוגי) הפונקציה תעביר 2 (מספר האותיות הקטנות במחצית הראשונה) ו-1 (מספר האותיות הגדולות במחצית השנייה) ותחזיר 1.

עבור המחרוזת `"t&u5Y%&as3k\$R"` (האורך הוא אי זוגי) הפונקציה תעביר 2 (מספר האותיות הקטנות במחצית הראשונה) ו-1 (מספר האותיות הגדולות במחצית השנייה) ותחזיר 1-.""" + PART1

Q1_SOL = r"""```c
int nums_in_halves(char* str, int* num1, int* num2)
{
    int len = strlen(str), i;
    *num1 = *num2 = 0;
    for (i = 0; i < len / 2; i++)
        if ( islower(str[i]) )
            (*num1)++;
    for (i = (len + 1) / 2; str[i] != '\0'; i++)
        if ( isupper(str[i]) )
            (*num2)++;
    if (len % 2 == 0)
        return 0;
    if ( isdigit(str[len / 2]) )
        return 1;
    return -1;
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""**מטריצת חברויות** `M` של `N` אנשים היא מטריצה ריבועית **סימטרית** בגודל `N` בה כל האיברים שווים ל-0 או 1 בלבד.
במטריצה זו נגדיר אנשים `I,J` שהם **חברים ישירים** אם `M[I][J]=1` (בהתאם ליחס סימטרי בהכרח גם `M[J][I]=1`).
נגדיר **חברים עקיפים** כזוג אנשים שיש להם חבר משותף. כלומר `I,J` הם חברים עקיפים אם קיים `K` כך ש-`M[I][K]=1` וגם `M[J][K]=1` כאשר `I,J` אינם חברים ישירים (`M[I][J]=0`).

**דוגמא:**
עבור המטריצה הבאה האנשים 1 ו-4 הם חברים עקיפים כי 1 חבר של 2 ו-4 חבר של 2. אין חברות ישירה של 1 ו-4.
```
Index  0  1  2  3  4  5  6  7
  0    0  1  0  0  0  1  0  0
  1    1  0  1  0  0  0  1  0
  2    0  1  0  0  1  0  0  1
  3    0  0  0  0  0  1  0  1
  4    0  0  1  0  0  1  0  0
  5    1  0  0  1  1  0  1  0
  6    0  1  0  0  0  1  0  1
  7    0  0  1  1  0  0  1  0
```
כתבו פונקציה המקבלת מטריצת חברויות המיושמת כמערך דו-ממדי **דינאמי** וגודלה. על הפונקציה ליצור מערך של כל זוגות החברים העקיפים שבמטריצה.
הפונקציה תחזיר את כתובת תחילת המערך החדש ותעביר (`by reference`) את גודלו. אם אין במטריצה אף זוג חברים עקיפים, הפונקציה מחזירה `NULL` ומעבירה 0.

יש להגדיר מעל הפונקציה את **זוג החברים העקיפים** כ**מבנה** שמורכב משני המספרים המהווים אינדקסים של החברים.

**שימו לב.** חברים ישירים אינם נחשבים לחברים עקיפים, אפילו אם אפשר למצוא גם קשר עקיף ביניהם.
**שימו לב.** על כל זוג חברים עקיפים להופיע פעם אחת בלבד במערך החדש. למשל, אם הזוג `{1,4}` יופיע במערך אז המערך לא יכיל את הזוג `{4,1}`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת המערך החדש.""" + PART1

Q2_SOL = r"""```c
typedef struct
{
    int i, j;
} pair;

pair* indirect_friends(int** M, int size, int* new_size)
{
    int i, j, k, count = 0;
    pair* arr;
    *new_size = (size * size - size) / 2; //upper bound of possible number of pairs
    arr = (pair*)calloc(*new_size, sizeof(pair));
    for (i = 0; i < size; i++)
        for (j = 0; j < i; j++)
            if (M[i][j] == 0)
                for (k = 0; k < size; k++)
                    if (M[i][k] == 1 && M[k][j] == 1)
                    {
                        arr[count].i = i;
                        arr[count++].j = j;
                        break; //search for common friends of i and j has been terminated
                    }
    *new_size = count;
    arr = (pair*)realloc(arr, *new_size * sizeof(pair));
    return arr;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""נתונה הגדרת המבנה הבאה:
```c
typedef struct {
    char model[20];
    int price;
    int year;
} car;
```
המתאר את הנתונים על מכונית בחברת מכירות, כאשר:
- `model` - שם הדגם,
- `price` - מחיר המכונית,
- `year` - שנת היצור.

כתבו פונקציה בשם `appropriateCar` אשר מקבלת מחרוזת `fileName` המהווה שם של **קובץ בינארי**. הקובץ מורכב מרשומות הנתונים שהפורמט של כל אחת מהן מתאים למבנה `car`. כמו כן, הפונקציה מקבלת כפרמטרים את הדגם המבוקש ע"י הלקוח (מחרוזת `desired_model`), את המחיר המירבי שהקונה מוכן לשלם (מספר שלם `max_price`) ואת שנת היצור המינימלי (מספר שלם `min_year`).

על הפונקציה למצוא את כל המכוניות של הדגם `desired_model` מהקובץ בעלות מחיר שאינו עולה על `max_price` ושנת יצור לא לפני `min_year`.
הפונקציה תיצור רשימה מקושרת למחירים ושנות יצור של כל המכוניות המתאימות לתנאים לעיל. בזאת איברי הרשימה יהיו מורכבים משלושת השדות הבאים: מחיר, שנת יצור, ומצביע לאיבר הבא.
הפונקציה תחזיר את כתובת תחילת הרשימה. אם אף מכונית בקובץ לא מתאימה לתנאים לעיל או הקובץ לא נפתח, הפונקציה תחזיר `NULL`.
יש להגדיר את הטיפוס של איברי הרשימה מעל הפונקציה.

ניתן להניח שיש בזיכרון מספיק מקום להקצאת הרשימה.

**דוגמא:**
עבור הקובץ הבא (הרשומות משמאל לימין):
```
model   Subaru   Mazda    Subaru   Toyota    Subaru
price   90,000   95,000   10,000   200,000   25,000
year    2019     2020     2009     2022      2012
```
ו-`desired_model="Subaru"`, `max_price=100,000`, `min_year=2010` הפונקציה תיצור את הרשימה הבאה:
```
[90,000 | 2019] -> [25,000 | 2012]
```""" + PART1

Q3_SOL = r"""```c
typedef struct item {
    int price;
    int year;
    struct item* next;
} Item;

Item* appropriateCar(char* fileName, char* desired_model, int max_price, int min_year)
{
    FILE* fptr = fopen(fileName, "rb");
    car unit;
    Item* lst, * curr;
    if (!fptr)
        return NULL;
    curr = lst = (Item*)malloc(sizeof(Item)); //dummy item
    fread(&unit, sizeof(car), 1, fptr);
    while (!feof(fptr))
    {
        if (strcmp(unit.model, desired_model) == 0 && unit.price <= max_price && unit.year >= min_year)
        {
            curr->next = (Item*)malloc(sizeof(Item));
            curr = curr->next;
            curr->price = unit.price;
            curr->year = unit.year;
        }
        fread(&unit, sizeof(car), 1, fptr);
    }
    curr->next = NULL;
    /* Deleting dummy */
    curr = lst;
    lst = lst->next;
    free(curr);
    fclose(fptr);
    return lst;
}
```"""

# ---------------------------------------------------------------- Q4 (a-d, MCQ with justification)
Q4_INTRO = "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 4, 20 נק' בסך הכול; חובה לרשום את הבחירה והנימוק במחברת).\n"

Q4A_TEXT = Q4_INTRO + "איזו מהמילים הבאות אינה מילה שמורה של שפת C?"
Q4A_OPTS = opts("`static`", "`global`", "`extern`", "`auto`", "כל המילים לעיל הן מילים שמורות של שפת C")
Q4A_EXPL = "אין מילה `global` בשפת C. כדי לעשות משתנה גלובלי צריך פשוט להצהיר עליו מעל כל הפונקציות."

Q4B_TEXT = Q4_INTRO + r"""מהו פלט (משמאל לימין) של התוכנית הבאה?
```c
#include <stdio.h>
void main() {
    int a[3][3] = { {1,2,3},{4,5,6},{7,8,9} }, i;
    for (i = 0; i < 3; i++)
        printf("%d %d ", *a[i], *(*(a + i) + i));
}
```"""
Q4B_OPTS = opts("`1 2 4 5 7 8`", "`1 9 4 5 7 1`", "`1 1 2 5 3 9`", "`1 1 4 5 7 9`",
                "התוכנית אינה תקינה והפעלתה תגרום לשגיאת קומפילציה או לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4B_EXPL = "`*a[i]` שקול ל-`a[i][0]` ו-`*(*(a + i) + i)` שקול ל-`a[i][i]`."

Q4C_TEXT = Q4_INTRO + "מהי הטענה הלא נכונה?"
Q4C_OPTS = opts("קובץ טקסט שנפתח באופן `\"r\"` מיועד לקריאה ולא מיועד לכתיבה",
                "קובץ טקסט שנפתח באופן `\"w\"` מיועד לכתיבה ולא מיועד לקריאה",
                "קובץ טקסט שנפתח באופן `\"r+\"` מיועד גם לקריאה וגם לכתיבה",
                "קובץ טקסט שנפתח באופן `\"w+\"` מיועד גם לקריאה וגם לכתיבה",
                "כל הטענות לעיל הן נכונות")
Q4C_EXPL = "לפי כללי שפת C."

Q4D_TEXT = Q4_INTRO + r"""בתוכנית נתונה ההצהרה הבאה:
```c
char *str = "hello";
```
בחרו מה יקרה אחרי ביצוע פעולת
```c
str[0] = str[4] = '\0';
```"""
Q4D_OPTS = opts("ישתנה ערך של מצביע `str`", "תוכן המחרוזת `str` ישתנה ל-\"hell\"", "המחרוזת `str` תהפוך למחרוזת ריקה",
                "הפעולה תגרום לשגיאת ריצה", "אף תשובה אינה נכונה")
Q4D_EXPL = "ניסיון לשנות תוכן של מחרוזת קבועה גורם לשגיאת ריצה."

# ---------------------------------------------------------------- Q5
Q5_TEXT = r"""**שאלת בונוס.** מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>
#include <string.h>

void main()
{
  printf("%d",strcmp("&","&&")&strcmp("&","&&")|("strcmp(&,&&)"&&"strcmp(&,&&)"));
}
```
יש לנמק את התשובה."""

Q5_SOL = r"""**הפלט:** `-1`

**נימוק:**
המחרוזת `"&"` קטנה מילולית מהמחרוזת `"&&"`. לכן `strcmp("&","&&")` מחזירה -1.
פעולת `&` (and) על סיביות שוות נותנת אותה סיבית. לכן `-1 & -1` שווה ל-1-.
מצד ימין מבצעים פעולה בוליאנית `&&` על שתי המחרוזות, ז"א על כתובות שלהן אשר שונות מ-`NULL`. הפירוש הלוגי של כל מה ששונה מאפס הוא `true` ולכן ערך מספרי של תוצאת הפעולה הוא 1.
בסוף מבצעים את הפעולה `-1 | 1`. ייצוג בינארי של -1 הוא `111…1` וייצוג בינארי של 1 הוא `000…001` (פעולת `|` - or) על סיביות 1 ו-0 וגם על סיביות 1 ו-1 נותנת סיבית 1. לכן ייצוג בינארי של התוצאה הוא `111…1`, ז"א -1."""

questions = [
    Q(1, "code", "strings", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "dynamic_arrays_2d", Q2_TEXT, Q2_SOL, points=40),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40),
    {"num": 4, "part": "א", "kind": "mcq", "topic": "storage_classes", "question": Q4A_TEXT,
     "options": Q4A_OPTS, "correctId": "b", "explanation": Q4A_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ב", "kind": "mcq", "topic": "arrays_static", "question": Q4B_TEXT,
     "options": Q4B_OPTS, "correctId": "d", "explanation": Q4B_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ג", "kind": "mcq", "topic": "files", "question": Q4C_TEXT,
     "options": Q4C_OPTS, "correctId": "e", "explanation": Q4C_EXPL, "official": True, "confidence": "high"},
    {"num": 4, "part": "ד", "kind": "mcq", "topic": "strings", "question": Q4D_TEXT,
     "options": Q4D_OPTS, "correctId": "d", "explanation": Q4D_EXPL, "official": True, "confidence": "high"},
    Q(5, "code", "c_traps_mcq", Q5_TEXT, Q5_SOL, points=10),
]

exam = {
    "examCode": "22B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ב, מועד ב'",
    "year": 2022,
    "examDate": "25.07.2022",
    "sourceFile": "22B-B exam",
    "solutionFile": "22B-B official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
