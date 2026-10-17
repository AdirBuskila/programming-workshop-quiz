# מיזוג, השוואה והמרה של רשימות

## מה המבחן שואל
זו שאלה 1 (40 נקודות) בגרסאות הקשות יותר: לא רק מעבר או מחיקה, אלא שילוב של כמה רשימות או הצגה של מבנה אחר על רשימה. הדפוסים הידועים:
- **רשימת ספרות כמספר**: השוואת שני מספרים בלי להמיר ל-`int` (`24B-A-Q1`), והוספת מספר לרשימה (`22B-A-Q2`).
- **צבירה לפי חזקה**: רשימת מונומים של פולינום, איחוד אותן חזקות, והחזרת רשימה ממוינת, בעזרת מערך עזר שגודלו לפי החזקה המקסימלית (`23B-A-Q1`).
- **מעגלית**: הוצאת כל איבר `m` מרשימה מעגלית לרשימה חדשה (בעיית יוספוס, `23B-B-Q1`), ואיחוד שתי מעגליות (`21B-A-Q2`).
- **מערך מצביעים לרשימות**: חלוקת מערך מספרים לרשימות לפי מספר הספרות (`24B-B-Q1`).

## הרעיונות המרכזיים
- יש לשלוט בפעולות הבסיס ב-[[linked_lists]]: מעבר, הכנסה לראש, חיבור מחדש.
- **השוואת מספרים בייצוג ספרות**: מספר ארוך יותר גדול יותר (אם אין אפסים מובילים). בשווי אורכים, ההבדל הראשון משמאל מכריע.
- **צבירה**: במקום לחפש כל פעם ברשימה, ממפים חזקה לתא במערך עזר: `coef[power] += c`. עוברים פעם אחת על הרשימה ופעם על המערך.
- **ספירת ספרות**: `digits(n)` לאחר `abs`, ומקרה `0` שבו יש ספרה אחת.
- **רשימה מעגלית וספירה**: מקדמים מצביע `m-2` צעדים כדי לעמוד על האיבר שלפני האיבר שמוציאים (כך מנתקים אותו בלי עוד סריקה).
- **מערך של רשימות**: `L[k]` הוא ראש רשימה, והכתובת `L + k` מסוג `Item**` מועברת לפונקציית ההכנסה.

## השוואת מספרים ברשימות (`24B-A-Q1`)
```c
typedef struct item
{
    int digit;
    struct item *next;
} Item;

/* -1, 0, 1 : compares the numbers represented by the lists (no leading zeros) */
int num_list_cmp(const Item *L1, const Item *L2)
{
    const Item *p = L1, *q = L2;
    while (p && q)                    /* walk together: which list is longer? */
    {
        p = p->next;
        q = q->next;
    }
    if (p == NULL && q != NULL)
        return -1;                    /* L1 is shorter */
    if (p != NULL && q == NULL)
        return 1;
    for (; L1; L1 = L1->next, L2 = L2->next)   /* equal length: first difference */
    {
        if (L1->digit < L2->digit)
            return -1;
        if (L1->digit > L2->digit)
            return 1;
    }
    return 0;
}
```

## הוספת מספר לרשימת ספרות במקום (`22B-A-Q2`)
```c
int count_digits(int n)
{
    int c = 0;
    while (n)
    {
        c++;
        n /= 10;
    }
    return c;
}

/* head is the most significant digit; the list is updated in place */
void list_num_add(Item *head, int N)
{
    int size = 0, number = 0, i, newSize, digits[12];
    Item *p, *last = head;
    for (p = head; p; p = p->next)         /* list -> number */
    {
        number = number * 10 + p->digit;
        size++;
        last = p;
    }
    number += N;
    newSize = count_digits(number);
    for (i = size; i < newSize; i++)       /* extend at the tail */
    {
        last->next = (Item *)calloc(1, sizeof(Item));
        last = last->next;
    }
    for (i = newSize - 1; i >= 0; i--)     /* number -> digits array, least significant first */
    {
        digits[i] = number % 10;
        number /= 10;
    }
    for (p = head, i = 0; i < newSize; i++, p = p->next)
        p->digit = digits[i];
}
```
השיטה הזו משתמשת בהמרה למספר `int`, ולכן מתאימה לרשימות קצרות (עד 9 ספרות). זו גם השיטה בפתרון הרשמי. הרשימה לא נוצרת מחדש: מוסיפים איברים רק בסוף ורק כשצריך.

## צבירת מונומים (`23B-A-Q1`)
```c
typedef struct
{
    double coefficient;
    int power;
} Monom;

typedef struct node
{
    Monom mon;
    struct node *next;
} Node;

/* sums equal powers; result sorted so the highest power is first */
Node *create_polynom(const Node *L)
{
    const Node *p;
    Node *P = NULL, *t;
    int maxPower = 0, power;
    double *coef;
    for (p = L; p; p = p->next)
        if (p->mon.power > maxPower)
            maxPower = p->mon.power;
    coef = (double *)calloc(maxPower + 1, sizeof(double));
    for (p = L; p; p = p->next)
        coef[p->mon.power] += p->mon.coefficient;
    for (power = 0; power <= maxPower; power++)     /* ascending + head insertion = descending list */
        if (coef[power] != 0)
        {
            t = (Node *)malloc(sizeof(Node));
            t->mon.coefficient = coef[power];
            t->mon.power = power;
            t->next = P;
            P = t;
        }
    free(coef);
    return P;
}
```

## בעיית יוספוס על רשימה מעגלית (`23B-B-Q1`)
```c
typedef struct jnode
{
    int value;
    struct jnode *next;
} jnode;

/* moves every m-th element of the circular list to a new NULL-terminated list */
jnode *josephus(jnode *lst, int m)
{
    jnode *head = NULL, *tail = NULL, *dead;
    int i;
    while (lst != NULL)
    {
        for (i = 0; i < m - 2; i++)        /* stop on the node BEFORE the m-th */
            lst = lst->next;
        dead = lst->next;                  /* the m-th */
        if (dead == lst)                   /* the last remaining node */
            lst = NULL;
        else
        {
            lst->next = dead->next;        /* unlink from the circle */
            lst = lst->next;               /* counting restarts after dead */
        }
        dead->next = NULL;
        if (head == NULL)
            head = tail = dead;
        else
        {
            tail->next = dead;
            tail = dead;
        }
    }
    return head;
}

int main()
{
    jnode n[8], *r;
    int i;
    for (i = 0; i < 8; i++)
    {
        n[i].value = i + 1;
        n[i].next = &n[(i + 1) % 8];
    }
    for (r = josephus(&n[0], 3); r; r = r->next)
        printf("%d ", r->value);           /* 3 6 1 5 2 8 4 7 */
    printf("\n");
    return 0;
}
```
(הדוגמה משתמשת במערך מקומי של איברים, ולכן אין בה `free`. ברשימה שהוקצתה דינמית האיברים עוברים לרשימה החדשה ושם משחררים אותם.)

## איחוד שתי רשימות מעגליות עם ערך משותף (`21B-A-Q2`)
הרעיון: מוצאים באחת את האיבר `a` עם הערך המשותף ואת קודמו `pa`, ובשנייה את האיבר `b` עם אותו ערך ואת קודמו `pb`. מכניסים את שאר איברי הרשימה השנייה (מ-`b->next` עד `pb`) בין `pa` ל-`a`, ומשחררים את `b`.
```c
typedef struct citem
{
    int data;
    struct citem *next;
} CItem;

/* returns the node with value val in the circle L and sets *pred to its predecessor; NULL if absent */
CItem *find_with_pred(CItem *L, int val, CItem **pred)
{
    CItem *p = L;
    do
    {
        if (p->next->data == val)
        {
            *pred = p;
            return p->next;
        }
        p = p->next;
    } while (p != L);
    return NULL;
}

CItem *cyclic_lists_combining(CItem *L1, CItem *L2)
{
    CItem *p = L1, *a = NULL, *b = NULL, *pa = NULL, *pb = NULL;
    do                                       /* the common value: first x of L1 found in L2 */
    {
        b = find_with_pred(L2, p->data, &pb);
        if (b != NULL)
        {
            a = find_with_pred(L1, p->data, &pa);
            break;
        }
        p = p->next;
    } while (p != L1);
    if (b->next == b)                        /* L2 has only the common node */
    {
        free(b);
        return a;
    }
    pa->next = b->next;                      /* L1 up to pa, then L2 without b */
    pb->next = a;                            /* ... then the common node a */
    free(b);
    return a;
}
```
זו אותה בעיה כמו בשאלה המקורית, בפתרון קצר יותר: מנתקים חלק אחד, חוסכים סריקות כפולות ותופסים את מקרה הקצה של איבר יחיד.

## מערך של רשימות לפי כמות ספרות (`24B-B-Q1`)
```c
typedef struct nitem
{
    int number;
    struct nitem *next;
} NItem;

int digits_number(int num)
{
    int count = 1, a = abs(num);
    while (a > 9)
    {
        count++;
        a /= 10;
    }
    return count;
}

void head_insert(NItem **plst, int key)
{
    NItem *t = (NItem *)malloc(sizeof(NItem));
    t->number = key;
    t->next = *plst;
    *plst = t;
}

NItem **num_separation(const int *A, int sz, int *p_size)
{
    int i, maxd = 1, *d = (int *)calloc(sz, sizeof(int));
    NItem **L;
    for (i = 0; i < sz; i++)
    {
        d[i] = digits_number(A[i]);
        if (d[i] > maxd)
            maxd = d[i];
    }
    L = (NItem **)calloc(maxd, sizeof(NItem *));   /* all NULL */
    for (i = sz - 1; i >= 0; i--)
        head_insert(L + d[i] - 1, A[i]);           /* L + k is &L[k] */
    free(d);
    *p_size = maxd;
    return L;
}
```

## מתכון לפתרון
1. כתבו את הרעיון במשפט אחד לפני הקוד ("עוברים על שתי הרשימות יחד", "מערך עזר לפי חזקה", "מקדמים m-2 צעדים").
2. בהוראות כמו "הפתרון של המרה למספר אינו מתקבל" (`24B-A-Q1`) אסור להמיר, גם אם זה היה קצר יותר.
3. בהוראות כמו "השתמש במערך עזר" (`23B-A-Q1`) השימוש חובה.
4. בהוראות כמו "יש לכתוב ולהשתמש בפונקציית עזר" כתבו אותה בנפרד, עם החתימה שניתנה, וקראו לה.
5. בדקו מקרי קצה: רשימה ריקה (בפולינום: המספר 0), איבר יחיד, רשימות באורכים שונים, סכום מקדמים שמתאפס (לא נכנס לתוצאה).

## מלכודות
> 🪤 השוואת אורכים של רשימות ספרות נכונה רק בלי אפסים מובילים. השאלה מבטיחה זאת.

> 🪤 במערך מצביעים `calloc` מאפס ל-`NULL`, ולכן רשימות ריקות מתחילות נכון. עם `malloc` צריך לאפס ידנית.

> 🪤 מקדם `0.0` שהתקבל מסכום (למשל `3 + (-3)`) לא נכנס לרשימה. `coef[power] != 0` מטפל בזה.

> 🪤 ביוספוס, אחרי הוצאת איבר מתחילים לספור מהבא אחריו (`lst = lst->next`), ובסוף כשנשאר איבר אחד הוא קודם לעצמו.

> 🪤 הגדרת הטיפוס של איברי הרשימה צריכה להופיע מעל הפונקציה כשהשאלה אומרת כך (`22B-A-Q2`, `22B-B-Q3`).
