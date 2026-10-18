# קבצי טקסט וקבצים בינאריים

## מה המבחן שואל
כמעט בכל מועד, אחת משתי השאלות החלופיות בנות 40 הנקודות (שאלה 2 או 3) עוסקת בקובץ, ויש עוד שאלות קצרות על `feof`, `fgets` ו-`fgetc`. הדפוסים:
- **קובץ בינארי של רשומות**: לסנן לפי תנאי ולבנות מערך דינמי (`22B-A-Q3` דירות, `23B-B-Q2` סרטים) או רשימה מקושרת (`22B-B-Q3` מכוניות). 
- **קובץ טקסט מובנה**: לשחזר מטריצה מקובץ דחוס (`21B-A-Q3`), להמיר שורות טקסט לרשומות בינאריות (`25B-B-Q3`), לסנן שורות ולכתוב קובץ חדש (`24B-B-Q3`).
- **חיפוש בקובץ בלי לטעון אותו**: משחק boggle עם `fseek`/`ftell` (`24B-A-Q3`), ספירת מופעי מילה שלמה (`25B-A-Q3`), כתיבת מילים בשורות נפרדות (`23B-A-Q3b`).
- **פלט של קטע קוד על קובץ**: `24B-A-Q6` (`fgets` בלולאה), `22B-A-Q4a` (כמה פעמים מבוצעת הלולאה עם `feof`), `22B-B-Q4c` (מצבי פתיחה), `23B-A-Q5a` (`puts` מול `fputs`).

## הרעיונות המרכזיים
- `FILE *f = fopen(name, mode);` מחזיר `NULL` אם נכשל. תמיד בודקים. בסוף `fclose(f)`.
- מצבי פתיחה: `"r"` קריאה, `"w"` כתיבה (מוחק קיים), `"a"` הוספה בסוף. עם `+` (`"r+"`, `"w+"`) גם קריאה וגם כתיבה. קבצים בינאריים: `"rb"`, `"wb"`.
- קריאה בטקסט: `fscanf(f, "%d", &x)` (מחזיר כמה ערכים נקראו, או `EOF`), `fgets(buf, size, f)` (קורא שורה כולל `'\n'`, מחזיר `NULL` בסוף הקובץ), `fgetc(f)` (תו או `EOF`).
- כתיבה: `fprintf(f, ...)`, `fputs(str, f)` (בלי `'\n'` אוטומטי), `fputc(c, f)`. `puts(s)` מוסיפה `'\n'` ו-`fputs(s, stdout)` לא.
- `fread(&rec, sizeof(rec), 1, f)` קורא רשומה אחת (מחזיר כמה רשומות נקראו). `fwrite` כותב באותו אופן. בבינארי אין הפרדה לשורות; הגודל קבוע.
- מיקום בקובץ: `ftell(f)` נותן את המיקום הנוכחי, `fseek(f, offset, SEEK_SET | SEEK_CUR | SEEK_END)` קופץ, `rewind(f)` חוזר להתחלה.
- ל-`%s` ב-`fscanf` דילוג אוטומטי על רווחים לפני, ועצירה ברווח. `%9s` מגביל את מספר התווים, ובכך מונע גלישה.
- `feof(f)` נעשה אמת **רק אחרי** שניסו לקרוא מעבר לסוף. לכן לא בודקים אותו לפני הקריאה הראשונה.

## לולאות קריאה בטוחות
```c
/* text: ints separated by whitespace */
void read_ints(const char *name)
{
    FILE *f = fopen(name, "r");
    int x;
    if (!f)
        return;
    while (fscanf(f, "%d", &x) == 1)       /* stop when a read fails */
        printf("%d ", x);
    fclose(f);
}

/* text: line by line, with the '\n' removed */
void read_lines(const char *name)
{
    FILE *f = fopen(name, "r");
    char line[101];
    if (!f)
        return;
    while (fgets(line, 101, f))
    {
        size_t len = strlen(line);
        if (len > 0 && line[len - 1] == '\n')
            line[len - 1] = '\0';
        puts(line);
    }
    fclose(f);
}

/* binary: records, read until fread fails */
typedef struct
{
    char address[30];
    int rooms;
    int price;
} apartment;

int count_matching(const char *name, int rooms, int max_price)
{
    FILE *f = fopen(name, "rb");
    apartment a;
    int count = 0;
    if (!f)
        return -1;
    while (fread(&a, sizeof(apartment), 1, f) == 1)
        if (a.rooms == rooms && a.price <= max_price)
            count++;
    fclose(f);
    return count;
}
```
הפתרונות הרשמיים משתמשים בצורה `fread(...); while (!feof(f)) { ...; fread(...); }`. היא עובדת, אבל שימו לב שהקריאה חייבת להיות גם **לפני הלולאה** וגם **בסופה**.

## הדפוס הנפוץ: שני מעברים על הקובץ
כשיוצרים מערך מתוך הקובץ וצריך לדעת את הגודל: מונים בקריאה אחת, `rewind(f)`, מקצים, וממלאים בקריאה שנייה.
```c
apartment *matching(const char *name, int rooms, int max_price, int *count)
{
    FILE *f = fopen(name, "rb");
    apartment a, *arr;
    int i = 0;
    *count = 0;
    if (!f)
        return NULL;
    while (fread(&a, sizeof(apartment), 1, f) == 1)    /* pass 1 */
        if (a.rooms == rooms && a.price <= max_price)
            (*count)++;
    if (*count == 0)
    {
        fclose(f);
        return NULL;
    }
    arr = (apartment *)calloc(*count, sizeof(apartment));
    rewind(f);
    while (fread(&a, sizeof(apartment), 1, f) == 1)    /* pass 2 */
        if (a.rooms == rooms && a.price <= max_price)
            arr[i++] = a;
    fclose(f);
    return arr;
}
```

## ספירת מילה שלמה (`25B-A-Q3`)
```c
int word_appearance_num(const char *file_name, const char *word)
{
    FILE *f = fopen(file_name, "r");
    char buf[101];
    int count = 0;
    if (!f)
        return -1;
    while (fscanf(f, "%100s", buf) == 1)    /* one whitespace-separated word */
        if (strcmp(buf, word) == 0)
            count++;
    fclose(f);
    return count;
}
```
`fscanf` עם `%s` מדלג על רווחים ושורות חדשות, ולכן "מילה" כהגדרת השאלה (רצף תווים שאינם רווח או `'\n'`) נקראת בדיוק. `strcmp` בודק שוויון **מלא**, ולכן "lives" ו-"alive" לא נספרות עבור "live".

## שורות טקסט לרשומות בינאריות (`25B-B-Q3`)
```c
typedef struct
{
    char id[10];
    char name[31];
    double total;
} clientData;

void text_to_binary(const char *text_name, const char *binary_name)
{
    clientData c;
    FILE *in = fopen(text_name, "r");
    FILE *out = fopen(binary_name, "wb");
    if (!in || !out)
        exit(1);
    while (fscanf(in, "%9s%30s%lf", c.id, c.name, &c.total) == 3)
        fwrite(&c, sizeof(clientData), 1, out);
    fclose(in);
    fclose(out);
}
```
המגבלות `%9s` ו-`%30s` שומרות על מקום ל-`'\0'` בשדות `char id[10]` ו-`char name[31]`. בלעדיהן הקלט שורף זיכרון.

## מתכון לפתרון
1. פתחו את הקובץ במצב המתאים (טקסט או בינארי, קריאה או כתיבה), ובדקו `NULL`. בכל שאלה: מה מחזירים אם הקובץ לא נפתח?
2. החליטו את צורת הקריאה לפי המבנה: מספרים (`fscanf %d`), מילים (`fscanf %s`), שורות (`fgets`), תווים (`fgetc`), רשומות (`fread`).
3. אם נדרש מערך או רשימה בגודל לא ידוע: שני מעברים עם `rewind`, או רשימה מקושרת (אין צורך בגודל). 
4. אם מותר לקרוא רק "בלי לטעון את כל הקובץ" (boggle), השתמשו ב-`fgetc`, `ftell` ו-`fseek(f, -1, SEEK_CUR)` כדי לחזור אחורה.
5. סגרו את הקובץ בכל מסלול יציאה.
6. בשאלות פלט ("מה מודפס"), רשמו את מיקום הסמן ואת התוכן שאחריו אחרי כל קריאה.

## דוגמה פתורה: שחזור שורות מקובץ דחוס (`21B-A-Q3`)
כל שורה בקובץ היא זוגות "ערך כמות". מונים כמה שורות יש (מספר ה-`'\n'`), ולכל שורה מחשבים את אורכה במעבר ראשון ומשחזרים במעבר שני אחרי `fseek` לתחילת השורה.
```c
#include <stdio.h>
#include <stdlib.h>

int **decode(const char *filename, int **S, int *rows)
{
    int **A, i, j, k, num, size, start;
    int ch;
    FILE *f = fopen(filename, "r");
    if (!f)
        exit(1);
    *rows = 0;
    while ((ch = fgetc(f)) != EOF)
        if (ch == '\n')
            (*rows)++;
    A = (int **)calloc(*rows, sizeof(int *));
    *S = (int *)calloc(*rows, sizeof(int));
    rewind(f);
    for (i = 0; i < *rows; i++)
    {
        start = (int)ftell(f);
        do                                       /* pass 1: row length */
        {
            fscanf(f, "%d%d", &num, &size);
            (*S)[i] += size;
        } while ((ch = fgetc(f)) != '\n');
        A[i] = (int *)calloc((*S)[i], sizeof(int));
        fseek(f, start, SEEK_SET);               /* back to the row start */
        k = 0;
        do                                       /* pass 2: fill */
        {
            fscanf(f, "%d%d", &num, &size);
            for (j = 0; j < size; j++)
                A[i][k++] = num;
        } while ((ch = fgetc(f)) != '\n');
    }
    fclose(f);
    return A;
}

int main()
{
    int *S, rows, i, j;
    int **A;
    FILE *f = fopen("demo_rle.txt", "w");
    fputs("4 2 7 4 3 3\n2 6 1 2\n", f);
    fclose(f);
    A = decode("demo_rle.txt", &S, &rows);
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < S[i]; j++)
            printf("%d ", A[i][j]);
        printf("| %d\n", S[i]);
    }
    return 0;
}
```
הפלט: `4 4 7 7 7 7 3 3 3 | 9` ואחריו `2 2 2 2 2 2 1 1 | 8`. אחרי הזוג האחרון בשורה `fgetc` קורא את ה-`'\n'` ויוצא מהלולאה.

## מלכודות
> 🚧 `while (!feof(f)) { fscanf(...); printf(...); }` רץ **פעם אחת יותר** מדי: ב-`22B-A-Q4a` קובץ `1 2 3 4 5 ` (רווח אחרי ה-5) מכניס את הלולאה 6 פעמים, כי ה-EOF מזוהה רק בניסיון הקריאה השישי. התשובה הנכונה שם: "אף תשובה אינה נכונה".

> 🚧 `char c = fgetc(f)` ואז `c != EOF`: `char` לא יכול להחזיק את `EOF` באופן אמין. מצהירים `int c`. ובלי סוגריים, `c = fgetc(f) != EOF` שם בתוך `c` את הערך 0 או 1 (`25B-A-Q6` מדפיס `111`).

> 🚧 `fgets(st, 2, f)` קוראת **תו אחד** (נשאר מקום ל-`'\0'`). ב-`24B-A-Q6` לקובץ `1234` הלולאה קוראת "1" (בתנאי), "2" (ל-`fputs`), "3", "4" ומדפיסה `24`.

> 🚧 `fputs` לא מוסיפה `'\n'`, `puts` כן (`23B-A-Q5a`: `puts("abc")` שקולה ל-`fputs("abc\n", stdout)`).

> 🚧 `"r+"` ו-`"w+"` מאפשרים גם קריאה וגם כתיבה (`22B-B-Q4c`). כל ארבעת הטענות שם נכונות.

> 🚧 קובץ בינארי נפתח ב-`"rb"` / `"wb"`, וכותבים רשומה שלמה: `sizeof(clientData)`, לא `sizeof(c.id)`.

> 🚧 `fgets` משאירה את `'\n'`. מורידים אותו לפני השוואות או בדיקות (`24B-B-Q3`).

> 🚧 `%s` ב-`fscanf` בלי הגבלת רוחב על `char id[10]` יכול לכתוב מעבר לגבולות המערך.

## קובץ בינארי בעורך טקסט, והעתקה בין קבצים בינאריים (`20B-B-Q4d`, `21B-B-Q4d`)
- `fwrite(&a, sizeof(a), 1, f)` כותבת את **הבתים של הזיכרון** כמו שהם, ולא את הספרות. המספר 1000 נשמר בארבעה בתים `E8 03 00 00` (נבדק עם clang). עורך טקסט יציג על זה ג'יבריש, ולכן הערך אינו קריא לבני אדם, אבל `fread` מחזירה בדיוק את אותו מספר.
- לעומת זאת תווי טקסט (`char`) נשמרים כקוד ASCII, ולכן מחרוזת בקובץ בינארי כן נראית בעורך טקסט.
- הזוג `fread(&a, sizeof(a), 1, fptr1)` ואחריו `fwrite(&a, sizeof(a), 1, fptr2)` מעתיק מספר אחד בשלמותו מקובץ בינארי אחד לאחר, בלי המרה לטקסט ובלי שינוי הערך. הסימן `&` בשתי הקריאות נכון ונדרש, כי שתי הפונקציות מקבלות כתובת של המשתנה.
