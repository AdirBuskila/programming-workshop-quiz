# רשימות מקושרות חד-כיווניות

## מה המבחן שואל
שאלה 1 (40 נקודות, חובה) היא כמעט תמיד על רשימה מקושרת. הדוגמאות בנושא הזה:
- `25B-A-Q1`: מחיקת רווחים מיותרים מרשימת תווים (`node** head`, שחרור איברים).
- `25B-B-Q1`: מערך של רשימות ורשימה `L`: להחזיר רשימה חדשה של אינדקסי הרשימות שמכילות את כל איברי `L`.
- `21B-A-Q2`: איחוד שתי רשימות מעגליות שיש להן ערך משותף אחד.
- `22B-A-Q2`: רשימת ספרות המייצגת מספר, והוספת מספר לרשימה במקום (ראו גם [[list_manipulation]]).

תנאים שחוזרים: "אל תקצה איברים חדשים" (מחברים מחדש מצביעים), "עדכן את הרשימה המקורית", "שחרר איברים שהוסרו".

## הרעיונות המרכזיים
- איבר: מבנה עם נתון ומצביע לבא. ההגדרה חייבת שם למבנה כדי שיוכל להצביע על עצמו:
  `typedef struct item { int data; struct item *next; } Item;`
- הרשימה מיוצגת על ידי מצביע לאיבר הראשון (ראש, head). רשימה ריקה היא `head == NULL`. האיבר האחרון מצביע ל-`NULL`.
- מעבר: `for (p = head; p; p = p->next)`. אחרי השורה `p = p->next` הקודם אבד. אם צריך אותו, שומרים `prev`.
- הכנסה לראש: O(1). הכנסה לסוף: O(n) אלא אם שומרים מצביע לאחרון (`tail`).
- מחיקה דורשת **את האיבר שלפני** המחיק (`prev->next = curr->next`), או מצביע למצביע שמצביע לאיבר.
- כל שינוי שעשוי לשנות את הראש מחייב להעביר את הראש by reference (`Item **head`, ראו [[pointer_to_pointer]]).
- ברשימה מעגלית האיבר האחרון מצביע לראשון, ואין `NULL`. הלולאה היא `do { ... p = p->next; } while (p != start);`. רשימה בת איבר אחד מצביעה לעצמה.
- איבר שמנתקים מהרשימה ולא עושים לו `free` הוא דליפה (אלא אם שאלה מבקשת להעביר אותו לרשימה אחרת).

## תבניות C
```c
typedef struct item
{
    int data;
    struct item *next;
} Item;

Item *new_item(int data, Item *next)
{
    Item *t = (Item *)malloc(sizeof(Item));
    t->data = data;
    t->next = next;
    return t;
}

void insert_head(Item **head, int data)
{
    *head = new_item(data, *head);
}

Item *from_array(const int *a, int n)       /* helper for tests */
{
    Item *head = NULL;
    int i;
    for (i = n - 1; i >= 0; i--)
        insert_head(&head, a[i]);
    return head;
}

void print_list(const Item *p)
{
    for (; p; p = p->next)
        printf("%d ", p->data);
    printf("\n");
}

void free_list(Item *p)
{
    while (p)
    {
        Item *next = p->next;               /* save before free */
        free(p);
        p = next;
    }
}
```

הכנסה לסוף עם מצביע לאחרון, בלי לסרוק:
```c
void append(Item **head, Item **tail, int data)
{
    Item *t = new_item(data, NULL);
    if (*head == NULL)
        *head = *tail = t;
    else
    {
        (*tail)->next = t;
        *tail = t;
    }
}
```

מחיקת כל האיברים עם ערך נתון, ראש משתנה (שתי צורות):
```c
void delete_value(Item **head, int val)
{
    Item *curr = *head, *prev = NULL;
    while (curr)
    {
        Item *next = curr->next;
        if (curr->data == val)
        {
            if (prev == NULL)
                *head = next;               /* deleting the head */
            else
                prev->next = next;
            free(curr);
        }
        else
            prev = curr;
        curr = next;
    }
}

/* the same with a pointer to the link that points to curr */
void delete_value2(Item **head, int val)
{
    Item **pp = head;
    while (*pp)
    {
        if ((*pp)->data == val)
        {
            Item *dead = *pp;
            *pp = dead->next;
            free(dead);
        }
        else
            pp = &(*pp)->next;
    }
}
```

הכנסה של איבר דמה (dummy) בתחילת הבנייה פותרת את בעיית "הראשון שונה":
```c
/* copies the even values, in order, into a new list */
Item *evens(const Item *src)
{
    Item dummy, *tail = &dummy;
    dummy.next = NULL;
    for (; src; src = src->next)
        if (src->data % 2 == 0)
        {
            tail->next = new_item(src->data, NULL);
            tail = tail->next;
        }
    return dummy.next;                  /* real head; the dummy is a local variable */
}
```

## מתכון לפתרון
1. שרטטו רשימה של 4-5 איברים עם חצים, כולל הראש והסוף. סמנו איזה מצביע משתנה בכל שלב.
2. הגדירו את המצביעים הקבועים לפני הלולאה: `prev`, `curr`, `next` (שמרו `next` לפני שמשנים את `curr->next` או משחררים).
3. כתבו את תנאי העצירה: `curr != NULL` (רגילה), `curr->next != NULL` (כשצריך את האחרון), או חזרה להתחלה (מעגלית).
4. בדקו את מקרי הקצה: רשימה ריקה, איבר אחד, ראש משתנה, מחיקת האחרון, כל הרשימה נמחקת.
5. שימו לב לסדר פעולות בחיבור מחדש: קודם שומרים, אחר כך מחברים, ורק בסוף משחררים.
6. כשצריך רשימה חדשה בסדר מקורי ללא `tail`: מכניסים לראש ועוברים על הקלט **מהסוף להתחלה** (כמו `from_array`).

## דוגמה פתורה: אילו רשימות במערך מכילות את כל איברי `L` (`25B-B-Q1`)
```c
/* 1 if every value of sub appears somewhere in list */
int contains_all(const Item *sub, const Item *list)
{
    for (; sub; sub = sub->next)
    {
        const Item *p = list;
        while (p && p->data != sub->data)
            p = p->next;
        if (p == NULL)
            return 0;               /* this value of sub was not found */
    }
    return 1;
}

Item *lists_with_given_elements(Item **A, int n, Item *L)
{
    Item *res = NULL;
    int i;
    for (i = n - 1; i >= 0; i--)    /* backwards: head insertion keeps ascending order */
        if (contains_all(L, A[i]))
            insert_head(&res, i);   /* a NEW Item that holds the index i */
    return res;
}

int main()
{
    int a0[] = {2, 6, 5, 1, 8}, a1[] = {8, 3, 5}, a2[] = {5}, a3[] = {1, 2, 8, 5, 3}, a4[] = {8, 5, 2, 8};
    int l[] = {8, 2, 5};
    Item *A[5], *L = from_array(l, 3), *r;
    A[0] = from_array(a0, 5);
    A[1] = from_array(a1, 3);
    A[2] = from_array(a2, 1);
    A[3] = from_array(a3, 5);
    A[4] = from_array(a4, 4);
    r = lists_with_given_elements(A, 5, L);
    print_list(r);                  /* 0 3 4 */
    return 0;
}
```
אין צורך לדעת את אורך הרשימות, ולא אפשר להסתפק בהשוואת אורכים או איבר ראשון: צריך לחפש **כל** איבר של `L` בתוך כל `A[i]`.

## מלכודות
> 🪤 `curr = curr->next` אחרי `free(curr)`: קריאה מזיכרון משוחרר. שמרו `next` קודם.

> 🪤 מחיקת הראש בלי `Item **`: הקורא ממשיך להחזיק בכתובת הישנה.

> 🪤 שכחו לסיים את הרשימה החדשה ב-`NULL` (הרשימה "מתארכת" לזבל).

> 🪤 בהכנסה לראש של רשימה חדשה הסדר מתהפך. כדי לשמור סדר: עוברים על הקלט מהסוף, או שומרים `tail`.

> 🪤 ברשימה מעגלית, `while (p != start)` שמתחיל ב-`p = start` לא ירוץ אף פעם. משתמשים ב-`do ... while`.

> 🪤 הפונקציה "לא תקצה זיכרון": מחברים מחדש את `next` של האיברים הקיימים, אין `malloc`. לעומת זאת "ליצור רשימה חדשה" מחייב איברים חדשים (גם כשהם מחזיקים אינדקסים).
