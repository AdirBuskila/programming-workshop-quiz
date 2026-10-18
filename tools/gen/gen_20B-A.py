# -*- coding: utf-8 -*-
"""Generator for tools/raw/20B-A.json -- programming-workshop (C), semester B 2020, moed A (28.06.2020).
Part 1: Q1, Q2, Q3 (40 pts each, answer two of three). Part 2: Q4 (20 pts, six pick-and-justify items, a student gets four).
Part 3: bonus (10 pts). Solutions transcribed from the official solution PDF (typed code + yellow-marked options).
Code solutions compiled and run with clang: tools/verify/20B-A/. Run: PYTHONUTF8=1 py tools/gen/gen_20B-A.py"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "raw" / "20B-A.json"
IDS = "abcdef"


def opts(*vals):
    return [{"id": IDS[i], "type": "text", "value": v} for i, v in enumerate(vals)]


def Q(num, kind, topic, question, solution, **kw):
    q = {"num": num, "kind": kind, "topic": topic, "question": question, "solution": solution,
         "solutionSource": "official-pdf", "official": True, "confidence": "high"}
    q.update(kw)
    return q


CHOOSE = "\n\n*בחלק זה יש לענות על שתי שאלות מתוך שלוש.*"

# ---------------------------------------------------------------- Q1
Q1_TEXT = r"""כתוב פונקציה אשר מקבלת מערך דו-ממדי דינאמי `A` בעל `n` שורות וגם מערך `SIZE` המכיל את אורכי השורות של מערך `A` – כך שערך האיבר ה-`i` במערך `SIZE` מייצג את גודל השורה ה-`i` ב-`A`.

על הפונקציה לבצע את החלפת השורות ב-`A`, כך ששורה מס' `0` תוחלף עם שורה מס' `n-1`, שורה מס' `1` תוחלף עם שורה מס' `n-2`, שורה מס' `2` תוחלף עם שורה מס' `n-3` וכו'. אם `n` הוא מספר זוגי אז שורה מס' `n/2-1` תוחלף עם שורה מס' `n/2`, אחרת שורה מס' `(n-1)/2` לא תשתנה.
בנוסף, הפונקציה תעדכן את איברי `SIZE` בהתאם להיסט המחזורי שבוצע על `A`.

**דוגמא** (בתחילת כל שורה נמצא מספרה):
`A` לפני ההיסט:
```
0 5 12 6 9
1 0 3 1 29 101
2 13 14
3 2 20 4
```
`A` אחרי ההיסט:
```
0 2 20 4
1 13 14
2 0 3 1 29 101
3 5 12 6 9
```
`SIZE` לפני ההיסט (משמאל לימין): 4, 5, 2, 3.
`SIZE` אחרי ההיסט (משמאל לימין): 3, 2, 5, 4.

זמן ריצת הפונקציה יהיה תלוי רק בכמות שורות במערך הדו-ממדי `A` ולא יהיה תלוי בגדלי השורות!

על הפונקציה להיות אוניברסאלית כלפי טיפוס איברי המערך `A`, ז"א לבצע את ההיסט המחזורי על המערך בעל איברים של טיפוס שרירותי.

אפשר להשתמש במשתני עזר בודדים, אך לא במערכים מכל סוג שהוא.""" + CHOOSE

Q1_SOL = r"""```c
void point_swap(void **p, void **q) {
    void *temp = *p;
    *p = *q;
    *q = temp;
}

void swap(int *p, int *q) {
    int temp = *p;
    *p = *q;
    *q = temp;
}

void row_reverse(void **A, int n, int *SIZE) {
    int row1, row2;
    for (row1=0, row2=n-1; row1<row2; row1++, row2--) {
        point_swap(A + row1, A + row2);
        swap(SIZE + row1, SIZE + row2);
    }
}
```"""

# ---------------------------------------------------------------- Q2
Q2_TEXT = r"""נתונה הגדרה הבאה של הטיפוס:
```c
typedef struct item
{
  int data;
  struct item *next;
} Item;
```
**רשימה מעגלית ממוינת** מורכבת מאיברים מסוג `Item` אשר ממוינים בסדר עולה ממש לפי שדה `data`. שדה `next` של איבר עם `data` יותר קטן מצביע לאיבר עם `data` יותר גדול. שדה `next` של איבר עם `data` המקסימלי מצביע לאיבר עם `data` המינימלי. ברשימה בעלת איבר אחד שדה `next` שלו מצביע לאיבר עצמו.

כתוב פונקציה אשר מקבלת כתובת של אחד מהאיברים של רשימה מעגלית ממוינת `L`.
על הפונקציה "לחתוך" את הרשימה כך ששדה `next` של איבר עם `data` המקסימלי ישתנה ל-`NULL`.
הפונקציה תחזיר כתובת של האיבר עם `data` המינימלי.
אם `L` היא רשימה ריקה הפונקציה תקבל `NULL` ותחזיר `NULL`.

**דוגמא:** (באיור: `L` לפני עיבוד, עם הכתובת המתקבלת שמצביעה על האיבר 4, ו-`L` אחרי עיבוד עם הכתובת המוחזרת)""" + CHOOSE

Q2_SOL = r"""```c
Item *cut_cyclic_list(Item *L)
{
    Item *first;
    if (!L)
        return NULL;
    while (L->data < L->next->data)
        L = L->next;
    first = L->next;
    L->next = NULL;
    return first;
}
```"""

# ---------------------------------------------------------------- Q3
Q3_TEXT = r"""כתוב פונקציה שמקבלת מערך מחרוזות בשם `Infiles` עם גודלו `n`.
כל אחת מהמחרוזות מהווה שם של קובץ (טקסט או בינארי) עם נקודה וסיומת שם הקובץ בסוף. שם של קובץ בינארי מתחיל באות 'b' קטנה או באות 'B' גדולה. שם של קובץ טקסט מתחיל בכל תו אחר. תווים אחרונים משמאל לנקודה, בשם הקובץ הבינארי, הם ספרות אשר מייצגות גודל בבתים של רשומות הקובץ. בקבצי הטקסט תו של סוף השורה מופיע גם בסוף השורה האחרונה.

על הפונקציה לספור את כמות השורות בכל קובץ טקסט ואת כמות הרשומות בכל קובץ בינארי ולאחסן את התוצאות במערך דינאמי `Results` בגודל `n` של מבנים המוגדרים באופן הבא:
```c
typedef struct pair
{
  int num_text_rows;
  int num_bin_records;
} Pair;
```
אם מחרוזת מס' `i` ב-`Infiles` היא שם קובץ טקסט אז שדה `num_text_rows` באיבר מס' `i` של `Results` יהיה שווה למספר השורות בקובץ זה ושדה `num_bin_records` יקבל ערך `-1`.
אם המחרוזת היא שם קובץ בינארי אז בהתאם שדה `num_bin_records` באיבר מס' `i` יהיה שווה למספר הרשומות בקובץ ושדה `num_bin_records` יקבל `-1`.
אם הקובץ הנבחן לא נפתח יש להכניס ערך `0` לשדה המתאים.

הפונקציה תחזיר את הכתובת ההתחלתית של מערך `Results`.

ניתן להניח שיש בזיכרון מספיק מקום להקצאה.

**דוגמא:** שמות הקבצים ותוכנם (באיור): `MyFile.dat` (טקסט, שתי שורות: `Name: Moshe`, `Date: 24.05.2012`), `binFile120.doc` (בינארי), `Students.txt` (טקסט, שלוש שורות: `Amir Shai`, `Doron Levi`, `Tomer Cohen`), `B_Numbers68.xr` (בינארי), `Letters.dat`.
```
Infiles
MyFile.dat
binFile120.doc
Students.txt
B_Numbers68.xr
Letters.dat
```
`Results`:
```
num_text_rows   num_bin_records
 2              -1
-1               5
 3              -1
-1               4
 0              -1
```

**הערת מתמלל:** בנוסח המודפס, בפסקה על קובץ בינארי, מופיע `num_bin_records` גם בשדה שמקבל `-1`. מהדוגמה ברור שהכוונה לשדה `num_text_rows`.""" + CHOOSE

Q3_SOL = r"""```c
/* Counting number of rows in text file */
int NumOfRows(char *fname) {
    FILE *f = fopen(fname, "r");
    int count = 0;
    char c;
    if (!f) return 0;
    while ( (c=fgetc(f))!=EOF )
        if (c == '\n') count++;
    fclose(f);
    return count;
}

/* Counting number of records in binary file */
int NumOfRecords(char *fname, int rec_size) {
    char c;
    FILE *f = fopen(fname, "rb");
    int count = 0;
    if (!f) return 0;
    while (fread(&c, 1, 1, f)) //byte by byte input
        count++;               //number of bytes
    fclose(f);
    return count/rec_size;     //number of records
}

/* Extract a record size from a binary file name */
int getNumber(char *str) {
    int i = 0, dec = 1, num = 0;
    while (str[i] != '.') i++;
    i--; /*Scan of digits and deriving the number to the left of the point*/
    while (isdigit(str[i])) {
        num += (str[i--] - '0') * dec;
        dec *= 10;
    }
    return num;
}

Pair *numRowsRecords(char **Infiles, int n) {
    Pair *Results = (Pair *)malloc(n * sizeof(Pair));
    int i;
    for (i = 0; i < n; i++) {
        if (Infiles[i][0] == 'b' || Infiles[i][0] == 'B') {
            /* Processing of binary file */
            int rec = getNumber(Infiles[i]);
            Results[i].num_bin_records = NumOfRecords(Infiles[i], rec);
            Results[i].num_text_rows = -1;
        }
        else {
            /* Processing of text file */
            Results[i].num_text_rows = NumOfRows(Infiles[i]);
            Results[i].num_bin_records = -1;
        }
    } //for
    return Results;
}
```"""

# ---------------------------------------------------------------- Q4 (american items)
Q4_INTRO = "בחר את התשובה הנכונה **ונמק** בכל אחד מהסעיפים. **התשובה הנכונה ללא נימוק או עם נימוק לא נכון תזכה רק בנקודה אחת.** \"לפי כללי שפת C\" הינו גם יכול להיות נימוק מקובל. (שאלה 4, 20 נק' בסך הכול; סטודנט יקבל ארבע שאלות.)\n"

Q4A_TEXT = Q4_INTRO + r"""נגדיר כי פעולה `Y` היא **הכללה** של פעולה `X` אם `X` מוגדרת אך ורק לחלק מהמקרים שבהם מוגדרת `Y` ולכל המקרים שבהם מוגדרת `X` התנהגותה של `Y` זהה **לחלוטין** להתנהגותה של `X`.
מהי הטענה הלא נכונה?"""
Q4A_OPTS = opts("`fprintf` היא הכללה של `printf`", "`fscanf` היא הכללה של `scanf`", "`fgets` היא הכללה של `gets`",
                "`fgetc` היא הכללה של `getchar`", "כל הטענות לעיל הן נכונות")
Q4A_EXPL = r"""הצבת `stdout` או `stdin` (בהתאמה) ב-`fprintf`, `fscanf`, `fgetc` הופכת אותן מבחינת ההתנהגות ל-`printf`, `scanf`, `getchar` בהתאמה. `fgets` עם `stdin` לא זהה לחלוטין ל-`gets` כי ל-`fgets` יש עוד פרמטר למספר תווים מקסימלי ובנוסף היא קולטת גם `'\n'` לעומת `gets`."""

Q4B_TEXT = Q4_INTRO + "מה קורה בצד שמאל של מספר `int` שלילי לאחר ביצוע פעולת הזזת סיביות ימינה בתוכו?"
Q4B_OPTS = opts("מצד שמאל המספר מתמלא ב-0-ים", "מצד שמאל המספר מתמלא ב-1-ים",
                "מצד שמאל המספר מתמלא בסיביות שהלכו לאיבוד מצד ימין", "שיטת מילוי המספר מצד שמאל תלויה במערכת",
                "אף תשובה אינה נכונה")
Q4B_EXPL = "לפי כללי שפת C, הזזה ימינה של `int` שלילי היא מוגדרת-מימוש: חלק מהמערכות ממלאות מצד שמאל בסיבית הסימן (הזזה אריתמטית, ולכן ב-1-ים) וחלק ב-0-ים (הזזה לוגית). לכן שיטת המילוי תלויה במערכת. **הערה:** התשובה נכונה משום שהתקן משאיר את ההתנהגות להחלטת המימוש; במהדרים הנפוצים מתקבלת הזזה אריתמטית."

Q4C_TEXT = Q4_INTRO + r"""נתונה ההצהרה:
```c
const int **p;
```
מה הוא `p`?"""
Q4C_OPTS = opts("פוינטר לפוינטר קבוע שמצביע למשתנה", "פוינטר קבוע לפוינטר קבוע שמצביע למשתנה",
                "פוינטר קבוע לפוינטר שמצביע למשתנה", "פוינטר קבוע לפוינטר שמצביע לקבוע", "אף תשובה אינה נכונה")
Q4C_EXPL = "התשובה הנכונה: פוינטר לפוינטר שמצביע לקבוע."

Q4D_TEXT = Q4_INTRO + "מהי הטענה הנכונה?"
Q4D_OPTS = opts("משתנה מסוג `static` מוכר גם אחרי יציאה מהפונקציה בה הוא הוצהר",
                "משתנה מסוג `static` יכול להשתנות גם אחרי יציאה מהפונקציה בה הוא הוצהר",
                "משתנה מסוג `static` חייב להיות מאותחל באופן מפורש",
                "אחרי יציאה מהפונקציה בה הוצהר משתנה מסוג `static` ערך המשתנה נשמר בזיכרון ולא ניתן לשנות אותו",
                "שינוי משתנה מסוג `static` בשם `x` שהוצהר באחת מהפונקציות גורם לשינוי משתנה מסוג `static` בשם `x` שהוצהר בפונקציה אחרת",
                "אף טענה אינה נכונה")
Q4D_EXPL = "משתנה מסוג `static` לא מוכר אחרי יציאה מהפונקציה אבל נשמר בזיכרון. הפונקציה יכולה להחזיר כתובתו ודרכה אפשר לשנות את המשתנה גם אחרי יציאה מהפונקציה."

Q4E_TEXT = Q4_INTRO + "בתוכנית הוצהרו משתנה לוקאלי בשם `x` בתוך פונקציה `main` וגם משתנה גלובלי בשם `x` שמוכר בכל התוכנית. לאיזה משתנה ניגשים כאשר פונים ל-`x` בתוך `main`?"
Q4E_OPTS = opts("למשתנה לוקאלי", "למשתנה גלובלי",
                "אין משמעות בשאלה כי משתנה לוקאלי ומשתנה גלובלי בעלי אותו שם תופסים אותו מקום בזיכרון",
                "תלוי במערכת ובמהדר", "אף תשובה אינה נכונה כי המהדר ייתן הודעה על שגיאה")
Q4E_EXPL = "כללי הטווח: לקטעים מקוננים עם משתנים בעלי אותו שם עדיפות בגישה – למשתנה הפנימי ביותר."

Q4F_TEXT = Q4_INTRO + "עבור איזה משפט המהדר ייתן הודעה קשורה עם אי-התאמת טיפוסים?"
Q4F_OPTS = opts("`int n='a';`", "`char c=123;`", "`double x=38;`", "`int m=2000000000;`", "`float y=2.6;`",
                "כל המשפטים לעיל הם תקינים")
Q4F_EXPL = "מספר ממשי הוא בברירת מחדל `double`. לכן המהדר נותן את האזהרה: `truncation from 'double' to 'float'`. **הערה:** האזהרה תלויה במהדר: Visual C++ מדווח עליה כברירת מחדל (אזהרה C4305), ואילו מהדרים אחרים (למשל clang ו-gcc) לא מדווחים עליה בלי דגלי אזהרה נוספים כמו `-Wconversion`. לפי המפתח הרשמי זו התשובה הנכונה."

# ---------------------------------------------------------------- Q5 (bonus)
Q5_TEXT = r"""*שאלת בונוס (10 נק').*
מהו הפלט של התוכנית הבאה?
```c
#include <stdio.h>

void main()
{
  char C[]="C++", c;
  for (c=0; c<3; c++)
       C[c]+=!c?'+'-'+':'-'-'+';
  puts(C);
}
```
חובה לנמק את התשובה! התשובה ללא נימוק או עם נימוק לא נכון לא תזכה בנקודות."""

Q5_SOL = r"""**הפלט:**
```
C--
```
**נימוק:**
ל-`c==0` מתקיים `!c` ולכן מבצעים פעולות לפני ":" – ל-`C[0]` מחברים קוד ASCII של `'+'` ומחסירים קוד ASCII של `'+'`. לכן `C[0]` לא משתנה וערך שלו נשאר `'C'`.
ל-`c==1` ו-`c==2` לא מתקיים `!c` ולכן מבצעים פעולות אחרי ":" – ל-`C[1]` ו-`C[2]` מחברים קוד ASCII של `'-'` ומחסירים קוד ASCII של `'+'`. ערך של התווים הוא `'+'` ולכן אחרי חיסור `'+'` וחיבור `'-'` ערך שלהם משתנה ל-`'-'`."""


def M(part, topic, text, options, correct, expl):
    return {"num": 4, "part": part, "kind": "mcq", "topic": topic, "question": text, "options": options,
            "correctId": correct, "explanation": expl, "official": True, "confidence": "high"}


questions = [
    Q(1, "code", "pointer_to_pointer", Q1_TEXT, Q1_SOL, points=40),
    Q(2, "code", "linked_lists", Q2_TEXT, Q2_SOL, points=40, image="images/exams/20B-A-Q2.png"),
    Q(3, "code", "files", Q3_TEXT, Q3_SOL, points=40, image="images/exams/20B-A-Q3.png"),
    M("א", "c_traps_mcq", Q4A_TEXT, Q4A_OPTS, "c", Q4A_EXPL),
    M("ב", "bit_manipulation", Q4B_TEXT, Q4B_OPTS, "d", Q4B_EXPL),
    M("ג", "pointers", Q4C_TEXT, Q4C_OPTS, "e", Q4C_EXPL),
    M("ד", "storage_classes", Q4D_TEXT, Q4D_OPTS, "b", Q4D_EXPL),
    M("ה", "storage_classes", Q4E_TEXT, Q4E_OPTS, "a", Q4E_EXPL),
    M("ו", "c_traps_mcq", Q4F_TEXT, Q4F_OPTS, "e", Q4F_EXPL),
    Q(5, "code", "c_basics_output", Q5_TEXT, Q5_SOL, points=10),
]

# ---------------------------------------------------------------- steps / rubric / pitfalls (ai-draft)
# Every expected value below was produced by a real clang run: tools/verify/<CODE>/steps_check.py
import re


def rub(*items):
    return [{"text": t, "points": p} for t, p in items]


def code_of(sol, n=0):
    return re.findall(r"```c\n(.*?)\n```", sol, re.S)[n]


def lines_of(src):
    return [ln for ln in src.strip("\n").split("\n") if ln.strip()]


def ix(lines, text, nth=None):
    idx = [i for i, ln in enumerate(lines) if ln.strip() == text.strip()]
    if nth is None:
        assert len(idx) == 1, (text, idx)
        return idx[0]
    return idx[nth]


def blocks(lines, *starts):
    """Logical blocks: each start is the (unique) first line of a block; block 0 begins at line 0."""
    cuts = [0] + sorted(ix(lines, *(s if isinstance(s, tuple) else (s,))) for s in starts)
    assert len(set(cuts)) == len(cuts), starts
    return ["\n".join(lines[a:b]) for a, b in zip(cuts, cuts[1:] + [len(lines)])]


def swap1(lines, old, new):
    """The lines with exactly one line changed (asserted)."""
    i = ix(lines, old)
    out = list(lines)
    out[i] = out[i].replace(old.strip(), new.strip())
    assert out[i] != lines[i]
    return out, i


def blank(lines, target):
    i = ix(lines, target)
    out = list(lines)
    out[i] = out[i][:len(out[i]) - len(out[i].lstrip())] + "___"
    return out, i


def add(num, part=None, **kw):
    for q in questions:
        if q["num"] == num and q.get("part") == part:
            assert "hold" not in q and q["kind"] != "mcq", (num, part)
            q.update(kw)
            return
    raise KeyError((num, part))


def step(type_, **kw):
    s = {"type": type_}
    s.update(kw)
    return s

# ---- Q1: row_reverse
S1 = lines_of(code_of(Q1_SOL))
S1_bug, S1_bi = swap1(S1, "swap(SIZE + row1, SIZE + row2);", "swap(SIZE + row1, SIZE + row1);")
S1_fb, S1_bl = blank(S1, "for (row1=0, row2=n-1; row1<row2; row1++, row2--) {")

add(1,
    rubric=rub(("החלפת מצביעים לשורות (`A[i]` עם `A[n-1-i]`) ולא העתקת איברים, כך שזמן הריצה תלוי רק ב-`n`", 10),
               ("פונקציית עזר גנרית שמחליפה שני `void*` דרך כתובותיהם (`void **`), ולכן עובדת לכל טיפוס איברים", 8),
               ("לולאה עם שני אינדקסים משני הקצוות (`row1 < row2`) שעוצרת באמצע, כך שהשורה האמצעית ב-`n` אי-זוגי נשארת במקומה", 10),
               ("עדכון `SIZE` באותן החלפות בדיוק (החלפת `SIZE[row1]` עם `SIZE[row2]`)", 8),
               ("בלי מערכי עזר, רק משתני עזר בודדים", 4)),
    rubricSource="ai-verified",
    pitfalls=["להעתיק איברי שורות למערך עזר: זמן הריצה יהיה תלוי בגדלי השורות, וגם נאסר להשתמש במערכים.",
              "לרוץ עם `row1` על כל `n` (או על יותר מחצי): כל זוג מוחלף פעמיים והמערך חוזר למצבו ההתחלתי.",
              "לשכוח לעדכן את `SIZE`, או לכתוב פונקציית החלפה שמתאימה רק ל-`int*`/`int` ולא ל-`void**`."],
    steps=[
        step("numeric", prompt="כמה החלפות של שורות (קריאות ל-`point_swap`) מבצעת `row_reverse` עבור `n = 7`?",
             answer=3, tol=0,
             explain="הלולאה רצה כל עוד `row1 < row2`: (0,6), (1,5), (2,4), ואז `row1 = row2 = 3` והלולאה נעצרת. השורה האמצעית נשארת במקומה (ריצה אמיתית: 3)."),
        step("choice", prompt="במערך `A` של 4 שורות בגדלים `SIZE = 4, 5, 2, 3` (משמאל לימין), מה יהיה `SIZE` אחרי הקריאה ל-`row_reverse`?",
             options=opts("3, 2, 5, 4", "4, 5, 2, 3", "3, 5, 2, 4", "5, 4, 3, 2"), correctId="a",
             explain="`SIZE` עובר את אותן החלפות כמו השורות: (0,3) ו-(1,2), כלומר ההיפוך של הרצף (ריצה אמיתית: 3, 2, 5, 4). `4, 5, 2, 3` הוא מצב שבו `SIZE` לא עודכן, `3, 5, 2, 4` הוא החלפה של הקצוות בלבד, ו-`5, 4, 3, 2` הוא מיון."),
        step("fillblank", prompt="השלימו את שורת הלולאה: תנאי העצירה צריך להחליף כל זוג שורות פעם אחת בדיוק.",
             code=True, lines=S1_fb, blankIndex=S1_bl,
             options=opts("for (row1=0, row2=n-1; row1<row2; row1++, row2--) {", "for (row1=0, row2=n-1; row1<n; row1++, row2--) {",
                          "for (row1=0, row2=n-1; row1>row2; row1++, row2--) {", "for (row1=0, row2=n-1; row1<n/2+1; row1++, row2--) {"),
             correctId="a",
             explain="עם `row1<row2` כל זוג מוחלף פעם אחת. `row1<n` או `row1<n/2+1` ממשיכים אחרי האמצע ומחליפים חזרה זוגות שכבר הוחלפו (ב-`n = 4` הפלט שגוי), ו-`row1>row2` לא מבצע אף החלפה."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה: השורות הוחלפו אבל `SIZE` נשאר שגוי. מצאו אותה.",
             code=True, lines=S1_bug, bugIndex=S1_bi,
             explain="`swap(SIZE + row1, SIZE + row1)` מחליפה איבר עם עצמו, ולכן `SIZE` לא מתעדכן. צריך `SIZE + row2` כדי שגדלי השורות יתאימו לשורות שהוחלפו."),
    ],
    stepsSource="ai-verified")

# ---- Q2: cut_cyclic_list
S2 = lines_of(code_of(Q2_SOL))
S2_ord = blocks(S2, "if (!L)", "while (L->data < L->next->data)", "first = L->next;", "L->next = NULL;", "return first;")
S2_bug, S2_bi = swap1(S2, "first = L->next;", "first = L;")
S2_fb, S2_bl = blank(S2, "while (L->data < L->next->data)")

add(2,
    rubric=rub(("רשימה ריקה: אם `L == NULL` מחזירים `NULL`", 6),
               ("מעבר קדימה כל עוד `L->data < L->next->data` עד שמגיעים לאיבר המקסימלי (ברשימה בעלת איבר אחד התנאי שקרי מיד)", 14),
               ("שמירת האיבר המינימלי `first = L->next` לפני החיתוך", 8),
               ("חיתוך המעגל: `L->next = NULL` באיבר המקסימלי", 8),
               ("החזרת `first`", 4)),
    rubricSource="ai-verified",
    pitfalls=["לכתוב `<=` בתנאי הלולאה: ברשימה בעלת איבר אחד (שמצביע לעצמו) הלולאה אינסופית.",
              "לחתוך (`L->next = NULL`) לפני ששומרים את `L->next`, ואז לאבד את האיבר המינימלי.",
              "לשכוח את המקרה של רשימה ריקה ולגשת ל-`NULL->next`."],
    steps=[
        step("numeric", prompt="רשימה מעגלית ממוינת מכילה את הערכים $2, 4, 7, 9$ (אחרי $9$ בא $2$). הפונקציה מקבלת את כתובת האיבר $4$. כמה פעמים מתבצעת הפקודה `L = L->next` בלולאה?",
             answer=2, tol=0,
             explain="$4<7$ ומתקדמים, $7<9$ ומתקדמים, ואז $9<2$ שקרי והלולאה נעצרת באיבר המקסימלי (ריצה אמיתית: 2 התקדמויות)."),
        step("fillblank", prompt="השלימו את תנאי הלולאה שמגיעה לאיבר המקסימלי (גם כשברשימה איבר אחד שמצביע לעצמו).",
             code=True, lines=S2_fb, blankIndex=S2_bl,
             options=opts("while (L->data < L->next->data)", "while (L->data <= L->next->data)",
                          "while (L->data > L->next->data)", "while (L->next)"),
             correctId="a",
             explain="עם `<` הלולאה נעצרת באיבר שאחריו קטן ממנו (המקסימום), וברשימת איבר אחד נעצרת מיד. ב-`<=` הלולאה נעצרת במקסימום כשיש לפחות שני איברים (המקסימום גדול ממש מהאיבר שאחריו), אבל ברשימה בת איבר אחד `L->next == L` ו-`x <= x` תמיד אמת, ולכן היא נתקעת (ריצה אמיתית: תקיעה). `L->next` הוא תמיד אמת במעגל ולכן אינו נעצר לעולם, ו-`>` נעצר באיבר הראשון שאינו מקסימלי ומחזיר איבר שגוי."),
        step("order", prompt="סדרו את גושי הפונקציה `cut_cyclic_list`.",
             code=True, lines=S2_ord,
             explain="בודקים רשימה ריקה לפני כל גישה, מגיעים למקסימום, שומרים את המינימום (`L->next`) לפני שחותכים, חותכים, ומחזירים."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה והפונקציה מחזירה את האיבר הלא נכון. מצאו אותה.",
             code=True, lines=S2_bug, bugIndex=S2_bi,
             explain="`first = L;` שומרת את האיבר המקסימלי, בעוד שהפונקציה צריכה להחזיר את המינימלי, שהוא `L->next` של המקסימלי."),
    ],
    stepsSource="ai-verified")

# ---- Q3: numRowsRecords
S3 = lines_of(code_of(Q3_SOL))
S3_fb, S3_bl = blank(S3, "dec *= 10;")
S3_bug, S3_bi = swap1(S3, "return count/rec_size;     //number of records", "return count;")
_i0 = ix(S3, "int NumOfRecords(char *fname, int rec_size) {")
_i1 = ix(S3, "return count/rec_size;     //number of records") + 1
S3_ord = blocks(S3[_i0:_i1 + 1], "if (!f) return 0;", "while (fread(&c, 1, 1, f)) //byte by byte input", "fclose(f);")

add(3,
    rubric=rub(("הקצאת `Results` בגודל `n` מבנים `Pair` והחזרתו בסוף", 5),
               ("הבחנה בין קובץ בינארי לטקסט לפי התו הראשון בשם (`b` או `B`)", 6),
               ("קובץ טקסט: ספירת תווי `\\n`, החזרת `0` אם לא נפתח, ו-`-1` בשדה של הבינארי", 10),
               ("קובץ בינארי: הוצאת גודל הרשומה מהספרות משמאל לנקודה בשם הקובץ (הכפלה ב-10 בכל ספרה)", 10),
               ("קובץ בינארי: ספירת בתים בקובץ שנפתח ב-`\"rb\"`, חלוקה בגודל הרשומה, `0` אם לא נפתח ו-`-1` בשדה של הטקסט", 9)),
    rubricSource="ai-verified",
    pitfalls=["לפתוח קובץ בינארי במצב `\"r\"` ולא `\"rb\"`: על Windows התרגום של סוף שורה משנה את ספירת הבתים.",
              "לקרוא את ספרות גודל הרשומה משמאל לימין בלי שקלול ערך המקום (`120` יוצא `21`/`12` במקום `120`).",
              "לשכוח את הערך `-1` בשדה שאינו רלוונטי, או להחזיר ערך לא מוגדר במקום `0` כשהקובץ לא נפתח."],
    steps=[
        step("numeric", prompt="מה מחזירה הפונקציה `getNumber` עבור שם הקובץ `\"binFile120.doc\"`?",
             answer=120, tol=0,
             explain="הפונקציה מגיעה לנקודה, חוזרת תו אחד אחורה וקוראת ספרות מימין לשמאל: $0\\cdot1+2\\cdot10+1\\cdot100=120$ (ריצה אמיתית: 120)."),
        step("numeric", prompt="הקובץ הבינארי `binFile120.doc` גודלו 600 בתים. מה יהיה `num_bin_records` עבורו?",
             answer=5, tol=0,
             explain="`NumOfRecords` סופרת 600 בתים ומחלקת בגודל הרשומה 120, כלומר $600/120=5$ (ריצה אמיתית: 5)."),
        step("fillblank", prompt="השלימו את השורה שמעדכנת את ערך המקום בפונקציה `getNumber`.",
             code=True, lines=S3_fb, blankIndex=S3_bl,
             options=opts("dec *= 10;", "dec += 10;", "dec *= 2;", "dec = 10;"), correctId="a",
             explain="ערך המקום גדל פי 10 בכל ספרה: 1, 10, 100. עם `+= 10`, `*= 2` או `= 10` מתקבל מספר שגוי עבור `120` (ובהתאמה מספר רשומות שגוי)."),
        step("order", prompt="סדרו את גושי הפונקציה `NumOfRecords`.",
             code=True, lines=S3_ord,
             explain="פותחים את הקובץ ומצהירים, בודקים שנפתח, סופרים בתים, וסוגרים ומחשבים את מספר הרשומות."),
        step("findbug", prompt="בגרסה הבאה שורה אחת שונתה בפונקציה `NumOfRecords` והתוצאה שגויה. מצאו אותה.",
             code=True, lines=S3_bug, bugIndex=S3_bi,
             explain="`return count;` מחזירה את מספר הבתים (600) ולא את מספר הרשומות. צריך לחלק בגודל הרשומה."),
    ],
    stepsSource="ai-verified")

add(5,
    rubric=rub(("עבור `c == 0` מתקיים `!c`, ולכן מחשבים `'+'-'+'` שהוא `0` והתו `C[0]` נשאר `'C'`", 3),
               ("עבור `c == 1, 2` מחשבים `'-'-'+'`, כלומר מוסיפים `2` לתו", 3),
               ("התו `'+'` (קוד 43) ועוד 2 הוא קוד 45, כלומר `'-'`", 2),
               ("הפלט הוא `C--`", 2)),
    rubricSource="ai-verified",
    pitfalls=["לחשוב ש-`!c ? ... : ...` מתייחס לאורך המחרוזת או לתו עצמו ולא לאינדקס `c`.",
              "לטעות בפעולה `'-'-'+'` ולחשוב שהיא מחסירה 2 או שווה לתו, ולא שהיא מספר (2)."],
    steps=[
        step("numeric", prompt="מה ערך הביטוי `!c ? '+'-'+' : '-'-'+'` כאשר `c == 0`?", answer=0, tol=0,
             explain="`!0` שווה 1, ולכן בוחרים בענף הראשון: `'+'-'+'` שווה 0 (ריצה אמיתית: 0), ו-`C[0]` נשאר `'C'`."),
        step("numeric", prompt="מה ערך אותו ביטוי כאשר `c == 1`?", answer=2, tol=0,
             explain="`!1` שווה 0, ולכן בוחרים בענף השני: `'-'-'+'` הוא $45-43=2$ (ריצה אמיתית: 2)."),
        step("text", prompt="מה הפלט של התוכנית? (שלושה תווים)", accept=["C--"], normalize="none",
             explain="`C[0]` נשאר `C`, ו-`C[1]`, `C[2]` הם `'+'` (43) ועוד 2, כלומר 45 שהוא `'-'`: `C--` (ריצה אמיתית)."),
    ],
    stepsSource="ai-verified")


exam = {
    "examCode": "20B-A",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תש\"ף, מועד א'",
    "year": 2020,
    "examDate": "28.06.2020",
    "sourceFile": "20B-A exam",
    "solutionFile": "20B-A official solution",
    "contexts": {},
    "questions": questions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(exam, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.name}: {len(questions)} questions")
