# דף עזר: C לסדנה

> 🔑 **דף אחד לפני המבחן.** מבנה המבחן, כללי הזהב לכל נושא, חתימות של פונקציות הספרייה ושלדי קוד. הפירוט בכל פרק; כאן רק מה שצריך לזכור.

## מבנה המבחן (2023 עד 2025, ומועדים קודמים לפי אותו דפוס)
| חלק | תוכן | נקודות | הערה |
|---|---|---|---|
| שאלה 1 | רשימה מקושרת, כולל מעגלית ומערך רשימות | 40 | חובה. [[linked_lists]], [[list_manipulation]] |
| שאלה 2 או 3 | מערך דו-ממדי דינמי (משולשים, דחוס, מסגרת) | 40 | [[dynamic_arrays_2d]] |
| שאלה 2 או 3 | קובץ טקסט או בינארי, או טיפול במילים ומחרוזות | 40 | [[files]], [[strings]] |
| שאלה 4 | מה מודפס (מבנה, איחוד, `static`, מצביעים) עם נימוק | 10 | [[structs_unions]], [[storage_classes]], [[pointers]] |
| שאלה 5 | שתי טענות אמריקאיות עם נימוק | 10 | [[c_traps_mcq]] |
| שאלה 6 (בונוס) | מה מודפס: `fgetc`, סיביות, `sizeof`, `strcmp` | 10 | [[bit_manipulation]], [[c_basics_output]] |

במועדים 2019 עד 2022 החלק האמריקאי היה גדול יותר (חמש טענות, 20 נקודות, עם אפשרות "אף תשובה אינה נכונה").

תכנון זמן (3 שעות): 10 דקות סקירה, 45 דקות לשאלה 1, 40 דקות לשאלה שבחרתם, 30 דקות לשאלות 4 עד 6, ו-20 דקות לבדיקה. כל שאלה נבחנת גם על דוגמת הקלט שבשאלה: הריצו אותה בראש על הקוד שכתבתם.

## כללי זהב
1. **גודל הקצאה**: `n * sizeof(T)`, ולמחרוזת `strlen + 1`. שורות מטריצה: `calloc(cols, sizeof(int))`. מערך מצביעים: `calloc(rows, sizeof(int*))`.
2. **by reference**: מוסיפים `*` אחד לטיפוס. מערך שנוצר בפנים: `int **out`. ראש רשימה שעשוי להשתנות: `Item **head`. מטריצה: `int ***out`. סוגריים: `(*out)[i]`, `(*size)++`.
3. **ריק**: אם אין תוצאה מחזירים `NULL`, ומעבירים 0 לגודל.
4. **אל תשכחו**: בדיקת `fopen`, `fclose`, `free` למה שהוקצה זמנית, `'\0'` בסוף מחרוזת, `+1` לאורך.
5. **קלט**: קוראים כל רשומה/תו/שורה לפי `fread == 1`, `fgets != NULL`, `fscanf == מספר שדות`, `(c = fgetc(f)) != EOF` עם `int c`.

## הקצאה
| פונקציה | מה היא עושה |
|---|---|
| `malloc(bytes)` | מקצה, לא מאפס |
| `calloc(count, size)` | מקצה ומאפס |
| `realloc(p, bytes)` | משנה גודל, עשויה להזיז, הישן משוחרר. `realloc(NULL, n)` כמו `malloc(n)` |
| `free(p)` | משחררת. אסור על סטטי, אסור פעמיים. `free(NULL)` בסדר |

## מחרוזות (`string.h`, `ctype.h`)
| פונקציה | פעולה |
|---|---|
| `strlen(s)` | אורך בלי `'\0'` |
| `strcpy(d, s)` / `strcat(d, s)` | העתקה / שרשור (היעד חייב להיות מספיק גדול) |
| `strcmp(a, b)` | 0 אם שווים, שלילי אם `a` קטן, חיובי אחרת |
| `strchr(s, c)` / `strstr(s, t)` | כתובת המופע הראשון או `NULL`. `strchr(s, '\0')` אינה `NULL` |
| `isalpha` `isdigit` `islower` `isupper` `tolower` `toupper` | מיון ותרגום תווים |
| `c - 'a'` | אינדקס אות (0 עד 25) |

## קבצים
| פונקציה | פעולה |
|---|---|
| `fopen(name, "r" / "w" / "a" / "rb" / "wb")` | פתיחה, `NULL` אם נכשלה |
| `fscanf(f, "%d", &x)` / `fscanf(f, "%9s", buf)` | קריאה, מחזירה מספר שדות שנקראו |
| `fgets(buf, n, f)` | קוראת עד `n-1` תווים או שורה (עם `'\n'`) |
| `fgetc(f)` / `fputc(c, f)` | תו אחד. `fgetc` מחזירה `int` |
| `fprintf(f, ...)` / `fputs(s, f)` | כתיבה. `fputs` ללא `'\n'` |
| `fread(&r, sizeof(r), 1, f)` / `fwrite(...)` | רשומה בינארית |
| `ftell(f)` / `fseek(f, off, SEEK_SET)` / `rewind(f)` | מיקום וקפיצה |
| `feof(f)` | אמת רק **אחרי** ניסיון לקרוא מעבר לסוף |

## מצביעים
- חוקי: מצביע + מספר, מצביע - מספר, מצביע - מצביע, השוואה. לא חוקי: מצביע + מצביע.
- `a[i]` שקול ל-`*(a+i)`. שם מערך הוא כתובת, מערך סטטי לא מושמים ולא משחררים.
- שם פונקציה הוא כתובתה: `f(k)` זהה ל-`(*f)(k)`.
- `sizeof(מצביע)` קבוע (4 או 8).

## מבנים, איחוד ו-static
- `p2 = p1`: מערכים בתוך המבנה מועתקים, מצביעים משתפים יעד. איחוד: זיכרון משותף, האחרון שנכתב גובר.
- `static` מקומי: מאותחל פעם אחת, זוכר ערך. גלובלי ו-`static` מאופסים. מקומי רגיל הוא זבל.
- שם בהיקף פנימי מסתיר שם חיצוני.

## סיביות והדפסה
- `&`, `|`, `^`, `~`, `<<` (כפל ב-2), `>>` (חילוק ב-2, מילוי אפסים במספר חיובי).
- `x ^ x = 0`, `x ^ 1` הופך סיבית אחרונה, `(x & 1) == 0` בדיקת זוגיות. סוגריים סביב `&` לפני `==`.
- תו הוא מספר: `'0'` הוא 48, `'A'` 65, `'a'` 97, `'\0'` 0. `/` בין שלמים חותך. `printf("%d")` על תו מדפיס קוד.
- מחרוזת קבועה בביטוי היא כתובת: `"puts" + 1` היא `"uts"`, ו-`sizeof"ab"` הוא 3.

## שלדים

רשימה (הכנסה לראש, מעבר, מחיקה):
```c
typedef struct item
{
    int data;
    struct item *next;
} Item;

void push(Item **head, int d)
{
    Item *t = (Item *)malloc(sizeof(Item));
    t->data = d;
    t->next = *head;
    *head = t;
}

void remove_value(Item **head, int v)
{
    Item **pp = head;
    while (*pp)
    {
        if ((*pp)->data == v)
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

מערך דינמי מסונן וגודלו בפרמטר:
```c
int *filter_positive(const int *a, int n, int *size)
{
    int i, k = 0, *res = (int *)calloc(n, sizeof(int));
    for (i = 0; i < n; i++)
        if (a[i] > 0)
            res[k++] = a[i];
    *size = k;
    return (int *)realloc(res, k * sizeof(int));
}
```

מטריצה משונה (משולש תחתון) ושחרורה:
```c
int **lower(int n)
{
    int i, **m = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
        m[i] = (int *)calloc(i + 1, sizeof(int));
    return m;
}

void free2(int **m, int rows)
{
    int i;
    for (i = 0; i < rows; i++)
        free(m[i]);
    free(m);
}
```

קריאת רשומות מקובץ בינארי וסינון:
```c
typedef struct
{
    char name[20];
    int price;
} rec;

rec *cheap(const char *fn, int max, int *cnt)
{
    FILE *f = fopen(fn, "rb");
    rec r, *res;
    int n = 0, i = 0;
    *cnt = 0;
    if (!f)
        return NULL;
    while (fread(&r, sizeof(rec), 1, f) == 1)
        if (r.price <= max)
            n++;
    if (n == 0)
    {
        fclose(f);
        return NULL;
    }
    res = (rec *)calloc(n, sizeof(rec));
    rewind(f);
    while (fread(&r, sizeof(rec), 1, f) == 1)
        if (r.price <= max)
            res[i++] = r;
    fclose(f);
    *cnt = n;
    return res;
}
```
