# מצביע למצביע והעברה by reference

## מה המבחן שואל
כמעט כל שאלת קוד בת 40 נקודות דורשת להחזיר יותר מערך אחד מהפונקציה, והדרך היחידה ב-C היא כתובת של מה שרוצים לעדכן. אם מה שמעדכנים הוא עצמו מצביע (מערך שהוקצה בפנים, ראש רשימה שמשתנה), צריך **מצביע למצביע**. דוגמאות אמיתיות:
- `25B-A-Q1`: `void removeExtraSpaces(node** head)` — ראש הרשימה יכול להימחק.
- `25B-A-Q2`: `int ***tr_low, int ***tr_up` — מערך דו-ממדי דינמי מוחזר דרך פרמטר.
- `23B-A-Q2`: `int **ar_s_rows, int *num_s_rows` — מערך דינמי וגודלו מוחזרים דרך פרמטרים.
- `21B-A-Q3`: `int **S, int *rows` — מערך דינמי וגודלו, בנוסף לערך מוחזר.
- `24B-B-Q1`: `Item **L` — מערך של מצביעים לראשי רשימות, והכנסה לראש דרך `L + k`.

## הרעיון המרכזי
פרמטרים ב-C מועברים by value: הפונקציה מקבלת **עותק**. כדי שהפונקציה תשנה משתנה של הקורא, מעבירים את **כתובתו**, ובפונקציה כותבים דרכה עם `*`.

| רוצים לעדכן | מעבירים | כותבים בפונקציה | הקורא קורא |
|---|---|---|---|
| `int n` | `int *p` | `*p = 5;` | `f(&n)` |
| `int *arr` (מערך שהוקצה בפנים) | `int **p` | `*p = calloc(...)` | `f(&arr)` |
| `Item *head` (ראש רשימה) | `Item **p` | `*p = newNode;` | `f(&head)` |
| `int **mat` (מטריצה דינמית) | `int ***p` | `*p = rows;` | `f(&mat)` |

כלל אצבע: מוסיפים `*` אחד לטיפוס עבור כל רמה של "by reference".

## תבניות C
החזרת מערך דינמי וגודלו בפרמטרים:
```c
/* fills *out with a new array of the even numbers, *size with their count */
void evens(const int *a, int n, int **out, int *size)
{
    int i, k = 0;
    *size = 0;
    for (i = 0; i < n; i++)
        if (a[i] % 2 == 0)
            (*size)++;
    if (*size == 0)
    {
        *out = NULL;
        return;
    }
    *out = (int *)calloc(*size, sizeof(int));
    for (i = 0; i < n; i++)
        if (a[i] % 2 == 0)
            (*out)[k++] = a[i];
}
```
שימו לב לסוגריים: `(*out)[k]` ו-`(*size)++`. בלי הסוגריים `*out[k]` ו-`*size++` אומרים משהו אחר (`[]` ו-`++` חזקים מ-`*`).

מחיקת ראש רשימה ושינוי הראש:
```c
typedef struct node
{
    char value;
    struct node *next;
} node;

void delete_head(node **head)
{
    node *tmp = *head;
    *head = tmp->next;
    free(tmp);
}

void push_front(node **head, char c)
{
    node *n = (node *)malloc(sizeof(node));
    n->value = c;
    n->next = *head;
    *head = n;
}
```
מערך של רשימות והכנסה לראש הרשימה ה-`k` (`24B-B-Q1`):
```c
typedef struct item
{
    int number;
    struct item *next;
} Item;

void head_insert(Item **plst, int key)
{
    Item *t = (Item *)malloc(sizeof(Item));
    t->number = key;
    t->next = *plst;
    *plst = t;
}

/* L is Item*[]; L + k is the address of L[k], i.e. an Item** */
void put(Item **L, int k, int key)
{
    head_insert(L + k, key);      /* same as head_insert(&L[k], key) */
}
```
החזרת מטריצה משולשית דרך `int ***` (`25B-A-Q2`):
```c
void make_low(int n, int ***out)
{
    int i, j;
    int **low = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        low[i] = (int *)calloc(i + 1, sizeof(int));
        for (j = 0; j <= i; j++)
            low[i][j] = i * 10 + j;
    }
    *out = low;          /* one assignment at the end */
}
```
הקריאה: `int **m; make_low(4, &m);`.

## מתכון לפתרון
1. מהי התוצאה? אם ערך מספרי: `int *`. מצביע/מערך שנוצר בפנים: `T **`. מטריצה שנוצרה בפנים: `T ***`.
2. בנו את התוצאה במשתנה מקומי (`low`, `res`), ורק בסוף כתבו `*out = low;`. כך נמנעים מערבוב רמות הכוכביות.
3. כשמעדכנים ראש רשימה, בדקו שהקריאה שולחת `&head`.
4. סימון ריק: כתבו `*out = NULL; *size = 0;` (שאלות רבות דורשות זאת במפורש).
5. אחרי שכתבתם, בדקו כל `*`: האם הוא פותח כתובת אחת בלבד, והאם יש סוגריים סביב `*p` לפני `[i]` או `->`.

## דוגמה פתורה
`25B-A-Q1`: ברשימת תווים להשאיר רק רווח יחיד בין מילים ולהסיר רווחים בתחילה ובסוף.
```c
void remove_extra_spaces(node **head)
{
    node *prev, *curr;
    while (*head && (*head)->value == ' ')     /* leading spaces */
        delete_head(head);
    if (*head == NULL)
        return;
    prev = *head;
    curr = prev->next;
    while (curr)
    {
        if (curr->value == ' ' && (curr->next == NULL || curr->next->value == ' '))
        {
            prev->next = curr->next;           /* skip and free curr */
            free(curr);
        }
        else
            prev = curr;
        curr = prev->next;
    }
}
```
אפשר למחוק רווח אם הבא אחריו רווח אחר או סוף רשימה. כך נשאר מכל רצף הרווח האחרון בלבד, ורווח בסוף הרשימה נמחק.

## מלכודות
> 🚧 `void f(int *arr) { arr = malloc(...); }` משנה רק עותק של המצביע. הקורא נשאר עם המצביע הישן. צריך `int **`.

> 🚧 `*size++` מקדם את **המצביע** `size`, לא את הערך. כתבו `(*size)++`.

> 🚧 `*out[k]` אינו `(*out)[k]`. הראשון קורא מערך של מצביעים.

> 🚧 שכחו לכתוב את התוצאה (`*out = ...`) בכל נתיבי היציאה, כולל המקרה הריק.

> 🚧 הקורא מעביר `head` במקום `&head`: התוכנית מתקמפלת (עם אזהרה) ונופלת בריצה.
