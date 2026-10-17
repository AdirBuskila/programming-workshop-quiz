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

# ---- rubric / pitfalls / steps (ai-draft). Every expected value comes from a real clang run: tools/verify/22B-B/steps_check.py
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
F1 = func_lines(Q1_SOL, "int nums_in_halves")
b1, i1 = swap(F1, "for (i = 0; i < len / 2; i++)", "for (i = 0; i <= len / 2; i++)")
f1, j1 = blank(F1, "for (i = (len + 1) / 2; str[i] != '\\0'; i++)")
Q1_BODY = ["int len = strlen(str), i; *num1 = *num2 = 0;",
           "for (i = 0; i < len / 2; i++) if (islower(str[i])) (*num1)++; for (i = (len + 1) / 2; str[i] != '\\0'; i++) if (isupper(str[i])) (*num2)++;",
           "if (len % 2 == 0) return 0;",
           "if (isdigit(str[len / 2])) return 1;",
           "return -1;"]
add(1,
    rubric=rub(("חישוב האורך `len` ואיפוס שני המונים שמועברים by reference", 6),
               ("מעבר על המחצית הראשונה (`i < len/2`) וספירת אותיות קטנות עם `islower`", 10),
               ("מעבר על המחצית השנייה, שמתחילה ב-`(len+1)/2` (בלי התו האמצעי באורך אי-זוגי), וספירת אותיות גדולות עם `isupper`", 12),
               ("ערך ההחזרה: 0 לאורך זוגי, 1 כשהתו האמצעי ספרה, ו-1- בכל מקרה אחר", 12)),
    rubricSource="ai-draft",
    pitfalls=["להתחיל את המחצית השנייה ב-`len/2`: באורך אי-זוגי זה כולל את התו האמצעי, שאינו שייך לאף מחצית.",
              "לבדוק את התו האמצעי בלי לבדוק קודם שהאורך אי-זוגי, ולהחזיר 1 למחרוזת באורך זוגי.",
              "לשכוח לאפס את `*num1` ו-`*num2` לפני הספירה."],
    steps=[
        {"type": "numeric",
         "prompt": r"המחרוזת `t&u5Y%4as3k\$R` באורך 13. באיזה אינדקס מתחילה המחצית השנייה בקוד, כלומר מה ערך `(len + 1) / 2`?",
         "answer": 7, "tol": 0,
         "explain": "(13 + 1) / 2 = 7. התו באינדקס 6 הוא `4`, התו האמצעי, והוא לא נספר באף מחצית (ריצה אמיתית: 7)."},
        {"type": "choice",
         "prompt": r"מה מחזירה הפונקציה עבור `t&u5Y%&as3k\$R` (אורך אי-זוגי, והתו האמצעי הוא `&`)?",
         "options": opts("`-1`", "`0`", "`1`", "`2`"), "correctId": "a",
         "explain": "האורך אי-זוגי, והתו האמצעי `&` אינו ספרה, ולכן הפונקציה מחזירה -1 (ריצה אמיתית: -1)."},
        {"type": "fillblank", "prompt": "השלימו את כותרת הלולאה שעוברת על המחצית השנייה.", "code": True,
         "lines": f1, "blankIndex": j1,
         "options": opts("for (i = (len + 1) / 2; str[i] != '\\0'; i++)", "for (i = len / 2; str[i] != '\\0'; i++)",
                         "for (i = len / 2 + 1; str[i] != '\\0'; i++)", "for (i = (len - 1) / 2; str[i] != '\\0'; i++)"),
         "correctId": "a",
         "explain": "`(len+1)/2` נותן את תחילת המחצית השנייה גם באורך זוגי וגם באי-זוגי. החלופות האחרות כוללות את התו האמצעי או מדלגות על תו, ונכשלות על מחרוזות מתאימות (ריצה אמיתית)."},
        {"type": "order", "prompt": "סדרו את גוף הפונקציה `nums_in_halves`. כל שורה היא בלוק לוגי אחד.", "code": True,
         "lines": Q1_BODY,
         "explain": "אתחול, ספירה בשתי המחציות, ואז שלוש בדיקות לפי הסדר: אורך זוגי, ספרה באמצע, וברירת המחדל. החלפת שני בלוקים משנה את הפלט או שוברת את הקומפילציה (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": r"בגרסה הבאה שורה אחת שונתה, ועבור `t&u5Y%as3k\$R` נספרות 3 אותיות קטנות במחצית הראשונה במקום 2. מצאו אותה.",
         "code": True, "lines": b1, "bugIndex": i1,
         "explain": "`i <= len/2` כולל גם את התו הראשון של המחצית השנייה (`a`), ולכן הוא נספר פעם נוספת (ריצה אמיתית: 3)."},
    ],
    stepsSource="ai-draft")

# Q2
F2 = func_lines(Q2_SOL, "pair* indirect_friends")
b2, i2 = swap(F2, "if (M[i][j] == 0)", "if (M[i][j] == 1)")
f2, j2 = blank(F2, "if (M[i][k] == 1 && M[k][j] == 1)")
add(2,
    rubric=rub(("הגדרת מבנה `pair` של שני אינדקסים, והקצאת מערך בגודל החסם העליון `N(N-1)/2`", 8),
               ("מעבר על כל זוג `i > j` פעם אחת, והתחשבות רק בזוגות שאינם חברים ישירים (`M[i][j] == 0`)", 10),
               ("חיפוש חבר משותף `k` (`M[i][k] == 1` וגם `M[k][j] == 1`) ורישום הזוג פעם אחת בלבד (`break`)", 14),
               ("עדכון הגודל האמיתי ב-`*new_size`, כיווץ המערך עם `realloc` והחזרתו (`NULL` ו-0 כשאין זוגות)", 8)),
    rubricSource="ai-draft",
    pitfalls=["לספור גם חברים ישירים שיש להם חבר משותף: צריך לבדוק `M[i][j] == 0`.",
              "לרשום את אותו זוג כמה פעמים (בגלל כמה חברים משותפים), או גם כ-`{i,j}` וגם כ-`{j,i}`. הלולאה על `j < i` והפקודה `break` מונעות זאת.",
              "להקצות מערך בגודל `N*N` ולא לכווץ אותו, ולהחזיר גודל שגוי ב-`*new_size`."],
    steps=[
        {"type": "numeric",
         "prompt": "במטריצת הדוגמה (8 אנשים), כמה זוגות של חברים עקיפים יש?",
         "answer": 15, "tol": 0,
         "explain": "זוגות `i > j` שאינם חברים ישירים ויש להם חבר משותף, למשל `{4,1}` (חבר משותף 2) ו-`{2,0}` (חבר משותף 1). ספירה ישירה על המטריצה וגם הרצת הפתרון נותנות 15 זוגות."},
        {"type": "numeric",
         "prompt": "מהו החסם העליון על מספר הזוגות, `(size*size - size)/2`, עבור `size = 8`?",
         "answer": 28, "tol": 0,
         "explain": "(64 - 8) / 2 = 28: כל זוג `i > j` פעם אחת (ריצה אמיתית: 28)."},
        {"type": "fillblank", "prompt": "השלימו את תנאי החבר המשותף `k`.", "code": True,
         "lines": f2, "blankIndex": j2,
         "options": opts("if (M[i][k] == 1 && M[k][j] == 1)", "if (M[i][k] == 1 || M[k][j] == 1)",
                         "if (M[i][k] == 1 && M[k][k] == 1)", "if (M[i][k] + M[k][j] == 1)"),
         "correctId": "a",
         "explain": "`k` הוא חבר משותף רק אם הוא חבר ישיר של `i` וגם של `j`. `||` ו-`+ == 1` נותנים יותר מדי זוגות, ו-`M[k][k]` תמיד 0 ולכן לא נמצא אף זוג (ריצה אמיתית)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה 0 זוגות על מטריצת הדוגמה אף שיש בה זוגות עקיפים (למשל 4 ו-1). מצאו אותה.",
         "code": True, "lines": b2, "bugIndex": i2,
         "explain": "הבדיקה `M[i][j] == 1` משאירה רק זוגות שהם חברים ישירים, ובדוגמה אין חברים ישירים עם חבר משותף (ריצה אמיתית: 0 זוגות, אבל על משולש של שלושה חברים היא מחזירה 3 זוגות)."},
    ],
    stepsSource="ai-draft")

# Q3
F3 = func_lines(Q3_SOL, "Item* appropriateCar")
b3, i3 = swap(F3, "if (strcmp(unit.model, desired_model) == 0 && unit.price <= max_price && unit.year >= min_year)",
              "if (strcmp(unit.model, desired_model) == 0 && unit.price <= max_price && unit.year <= min_year)")
f3, j3 = blank(F3, "curr = curr->next;")
add(3,
    rubric=rub(("פתיחת הקובץ בבינארי והחזרת `NULL` כשהפתיחה נכשלת", 6),
               ("קריאת רשומות עם `fread` ולולאה עד סוף הקובץ (קריאה ראשונה לפני `feof`)", 8),
               ("בדיקת שלושת התנאים: `strcmp(...) == 0`, `price <= max_price`, `year >= min_year`", 10),
               ("יצירת איבר חדש בסוף הרשימה והעתקת מחיר ושנה אליו, בלי לאבד את סדר הקובץ", 10),
               ("סיום הרשימה ב-`NULL`, הסרת האיבר הפיקטיבי, סגירת הקובץ והחזרת הראש", 6)),
    rubricSource="ai-draft",
    pitfalls=["להשוות מחרוזות עם `==` או `desired_model == unit.model` במקום `strcmp`.",
              "לבדוק `year <= min_year` במקום `year >= min_year`, או `price < max_price` במקום `<=`.",
              "לא להסיר את האיבר הפיקטיבי, או לשכוח לסיים את הרשימה ב-`NULL`."],
    steps=[
        {"type": "numeric",
         "prompt": "בקובץ הדוגמה קוראים עם `desired_model = \"Subaru\"`, `max_price = 100,000` ו-`min_year = 2005`. כמה איברים יהיו ברשימה?",
         "answer": 3, "tol": 0,
         "explain": "שלוש מכוניות Subaru עומדות בתנאים: 90,000 (2019), 10,000 (2009) ו-25,000 (2012). ה-Mazda וה-Toyota נפסלות לפי הדגם (ריצה אמיתית: 3)."},
        {"type": "numeric",
         "prompt": "באותה קריאה, מה המחיר באיבר השני של הרשימה?",
         "answer": 10000, "tol": 0,
         "explain": "האיברים נוספים בסוף הרשימה לפי סדר הרשומות בקובץ, ולכן השני הוא 10,000 (ריצה אמיתית: 10000)."},
        {"type": "fillblank", "prompt": "השלימו את השורה החסרה אחרי יצירת האיבר החדש.", "code": True,
         "lines": f3, "blankIndex": j3,
         "options": opts("curr = curr->next;", "curr = lst;", "curr->next = NULL;", "lst = curr;"),
         "correctId": "a",
         "explain": "`curr` צריך לעבור לאיבר החדש כדי שהמחיר והשנה ייכתבו בו והאיבר הבא יתחבר אחריו. בכל חלופה אחרת הרשימה מתרוקנת או נשברת (ריצה אמיתית: `NULL`)."},
        {"type": "findbug",
         "prompt": "בגרסה הבאה שורה אחת שונתה, ועבור הדוגמה (`min_year = 2010`) מתקבל איבר אחד בלבד, `[10,000 | 2009]`, במקום שני האיברים הצפויים. מצאו אותה.",
         "code": True, "lines": b3, "bugIndex": i3,
         "explain": "`year <= min_year` מקבל מכוניות ישנות במקום מכוניות מ-`min_year` ואילך (ריצה אמיתית: `[10000 | 2009]`)."},
    ],
    stepsSource="ai-draft")

# Q5 (bonus; every intermediate value checked with a probe program; strcmp is -1 on the course toolchain, as in the official solution)
add(5,
    rubric=rub(("`strcmp(\"&\",\"&&\")` שלילית (-1), כי המחרוזת הראשונה קצרה והיא קודמת לקסיקוגרפית", 2),
               ("`&` על סיביות בין שני ערכים שווים נותן את אותו ערך, כלומר -1", 2),
               ("`&&` בין שתי מחרוזות קבועות (כתובות שונות מ-`NULL`) נותן 1", 3),
               ("`-1 | 1` נותן -1 (כל הסיביות דולקות), ולכן הפלט `-1`", 3)),
    rubricSource="ai-draft",
    pitfalls=["להתבלבל בין `&` (על סיביות) ל-`&&` (לוגי), ולחשב `-1 & -1` כ-1 או 0.",
              "לחשוב ש-`\"strcmp(&,&&)\" && \"strcmp(&,&&)\"` משווה מחרוזות. זה AND לוגי על שתי כתובות, והתוצאה 1.",
              "לחשוב ש-`-1 | 1` שווה 1 (או 0) ולא להתייחס לייצוג המשלים ל-2 של -1."],
    steps=[
        {"type": "choice", "prompt": "מה סימן התוצאה של `strcmp(\"&\", \"&&\")`?",
         "options": opts("שלילי: `\"&\"` קודמת ל-`\"&&\"` ולכן קטנה ממנה", "אפס: שתי המחרוזות מתחילות באותו תו",
                         "חיובי: `\"&\"` קצרה יותר", "לא מוגדר: תלוי באורך המחרוזות"), "correctId": "a",
         "explain": "מחרוזת שהיא תחילית של אחרת קטנה ממנה (ריצה אמיתית: הערך שלילי, -1)."},
        {"type": "numeric", "prompt": "מה הערך של `(\"strcmp(&,&&)\"&&\"strcmp(&,&&)\")`?", "answer": 1, "tol": 0,
         "explain": "AND לוגי של שתי כתובות שאינן `NULL` נותן 1 (ריצה אמיתית: 1)."},
        {"type": "numeric", "prompt": "בהנחה ש-`strcmp(\"&\",\"&&\")` מחזירה -1 (כמו בפתרון הרשמי), מה מדפיסה התוכנית כולה?",
         "answer": -1, "tol": 0,
         "explain": "`-1 & -1 = -1`, ואז `-1 | 1 = -1` (ריצה אמיתית: -1)."},
    ],
    stepsSource="ai-draft")


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
