# מערכים דינמיים דו-ממדיים

## מה המבחן שואל
זו השאלה השנייה בת 40 הנקודות (בחירה בין שאלה 2 לשאלה 3) כמעט בכל מועד. קלט: מטריצה סטטית או דינמית. פלט: מבנה דינמי חדש שמוחזר ו/או מועבר by reference. הדפוסים בבנק:
- `25B-A-Q2`: ממטריצה סטטית `A[][N]` לשני משולשים דינמיים (שורות באורכים שונים), דרך `int ***`.
- `25B-B-Q2`: ההפך: משני משולשים (שורה `i` מוזזת) למטריצה `(n+1)×(n+1)` עם אלכסון אפס.
- `24B-B-Q2`: הקפת מטריצה דינמית במסגרת אפסים ושחרור המקור.
- `24B-A-Q2`: מערך דינמי של `struct {int size; int *ptr;}`, שורה `i` מכילה את המתחלקים ב-`i+2`.
- `23B-A-Q2`: איזה שורות ממוינות ואיזה עמודות, שני מערכים חד-ממדיים בתוצאה.
- `22B-B-Q2`: מערך של זוגות `{i, j}` (מבנה) מתוך מטריצת חברויות, עם `realloc` בסוף.
- `21B-A-Q3`: שחזור מטריצה מקובץ דחוס (ראו [[files]]).

## הרעיון המרכזי
מטריצה דינמית היא **מערך של מצביעים**, שכל אחד מהם מצביע על שורה שהוקצתה בנפרד:
```
M ──► [ M[0] ][ M[1] ][ M[2] ]    (int**: an array of row pointers)
         │        │        └──► [ . . . . ]  row 2
         │        └─────────► [ . . . . ]    row 1
         └──────────────────► [ . . . . ]    row 0
```
שורות יכולות להיות באורכים שונים (מערך משונן, jagged), וזה מה שהמבחן אוהב: משולשים, דחוס, מערך של רשימות.

## תבניות C
הקצאה ושחרור של מטריצה `rows×cols` מאופסת:
```c
int **alloc_matrix(int rows, int cols)
{
    int i;
    int **m = (int **)calloc(rows, sizeof(int *));
    for (i = 0; i < rows; i++)
        m[i] = (int *)calloc(cols, sizeof(int));
    return m;
}

void free_matrix(int **m, int rows)
{
    int i;
    for (i = 0; i < rows; i++)
        free(m[i]);
    free(m);
}
```
משולש שמאלי תחתון (שורה `i` באורך `i+1`) ממטריצה סטטית (`25B-A-Q2`):
```c
#define N 4

void low_triangle(int A[][N], int n, int ***out)
{
    int i, j;
    int **low = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        low[i] = (int *)calloc(i + 1, sizeof(int));
        for (j = 0; j <= i; j++)
            low[i][j] = A[i][j];
    }
    *out = low;
}
```
שני משולשים חזרה למטריצה (`25B-B-Q2`). `tr_low` בעל `n` שורות: שורה `k` שלו היא שורה `k+1` במטריצה. `tr_up` בעל `n` שורות: שורה `i` שלו מתחילה בעמודה `i+1`, ולכן עמודה `j` במטריצה היא אינדקס `j-i-1` בו:
```c
int **triangles_to_matrix(int **tr_low, int **tr_up, int n)
{
    int i, j;
    int **A = (int **)calloc(n + 1, sizeof(int *));
    for (i = 0; i <= n; i++)
        A[i] = (int *)calloc(n + 1, sizeof(int));   /* zeros: main diagonal */
    for (i = 1; i <= n; i++)
        for (j = 0; j < i; j++)
            A[i][j] = tr_low[i - 1][j];
    for (i = 0; i < n; i++)
        for (j = i + 1; j <= n; j++)
            A[i][j] = tr_up[i][j - i - 1];
    return A;
}
```
מסגרת סביב מטריצה ושחרור המקור (`24B-B-Q2`):
```c
int **matrix_to_frame(int **M, int rows, int cols)
{
    int i, j;
    int **F = alloc_matrix(rows + 2, cols + 2);   /* all zeros */
    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++)
            F[i + 1][j + 1] = M[i][j];
    free_matrix(M, rows);
    return F;
}
```
מערך של מבנים שכל אחד מחזיק מערך דינמי וגודלו (`24B-A-Q2`):
```c
typedef struct
{
    int size;
    int *ptr;
} dyn_array;

dyn_array *div_numbers(const int *A, int sz, int n)
{
    int i, j, k;
    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array)); /* size 0, ptr NULL */
    for (i = 2; i <= n; i++)
    {
        int *tmp = (int *)calloc(sz, sizeof(int));
        k = 0;
        for (j = 0; j < sz; j++)
            if (A[j] % i == 0)
                tmp[k++] = A[j];
        if (k > 0)
        {
            B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));
            B[i - 2].size = k;
        }
        else
            free(tmp);
    }
    return B;
}
```
`calloc` של מערך המבנים נותן בחינם `size = 0` ו-`ptr = NULL` לשורות שנשארות ריקות, וזה בדיוק מה שהשאלה דורשת.

## מתכון לפתרון
1. שרטטו את הקלט והפלט עם דוגמה קטנה (3×3). כתבו ליד כל שורת פלט מה אורכה ומאיפה מגיע כל איבר.
2. רשמו נוסחה: אינדקס בקלט כנגד אינדקס בפלט (`j` מול `j - i - 1`, `i` מול `i + 1`, `i` מול `i + 1` במסגרת).
3. הקצו קודם את מערך המצביעים, ואז כל שורה בלולאה. השתמשו ב-`calloc` כשצריך אפסים.
4. מלאו בלולאה כפולה. בדקו את גבולות הלולאה על המקרה הקטן ביותר (`n = 1`).
5. אם צריך להחזיר שני דברים, אחד מוחזר ב-`return` והשני דרך מצביע. לגודל: `int *size`.
6. אם מבקשים לשחרר את הקלט, עשו זאת **אחרי** ההעתקה, שורה אחר שורה ואז המערך החיצוני.

## דוגמה פתורה
הפיכת מטריצה ריבועית סטטית למשולש עליון ממש (מערך משונן): שורה `i` מכילה את האיברים `A[i][i+1..n-1]`, כלומר `n-1-i` איברים.
```c
#define N 4

int **strict_upper(int A[][N], int n)
{
    int i, j;
    int **up = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        up[i] = (int *)calloc(n - 1 - i, sizeof(int));   /* last row: 0 elements */
        for (j = i + 1; j < n; j++)
            up[i][j - i - 1] = A[i][j];
    }
    return up;
}
```
בשורה האחרונה האורך 0, כלומר `calloc(0, ...)`. ההתנהגות תלויה במימוש, ולכן בשאלה אמיתית קראו היטב כמה איברים יש בכל שורה.

## מלכודות
> 🪤 `calloc(rows, sizeof(int))` במקום `sizeof(int*)` למערך המצביעים: בגרסת 64 סיביות מקצים חצי ממה שצריך.

> 🪤 מטריצה בגודל `n+1` ולא `n` (`25B-B-Q2`). וגם `tr_low[i-1][j]` ולא `tr_low[i][j]`.

> 🪤 שחרור שורות אחרי שחרור המערך החיצוני (איבדתם את הכתובות).

> 🪤 מערך סטטי שהועבר בפרמטר ונעשה עליו `free`: אסור (המערך אינו דינמי).

> 🪤 `malloc` במקום `calloc` כשהתוצאה צריכה אפסים (אלכסון, מסגרת): ערכי זבל נשארים.

> 🪤 `int **M` ו-`int M[][N]` אינם אותו טיפוס. את הראשון מקבלים מ-`malloc` והשני מהצהרה סטטית; לא מעבירים אחד במקום השני.
