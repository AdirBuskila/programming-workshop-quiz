# מחרוזות

## מה המבחן שואל
מחרוזת היא נושא של שאלה בת 40 נקודות כמעט בכל מועד, או חלק ממנה (`21B-A-Q1`, `22B-A-Q1`, `22B-B-Q1`, `23B-A-Q3a`, `23B-A-Q3c`, `23B-B-Q3`). בנוסף יש שאלות אמריקאיות על ההבדל בין מערך תווים למצביע (`22B-A-Q4d`, `22B-B-Q4d`, `25B-B-Q5b`). הדפוסים החוזרים:
- בדיקת סדר לפי שדות `char[]` במבנה (`21B-A-Q1`).
- בניית מחרוזת דינמית חדשה משרשור (`22B-A-Q1`).
- ספירת סוגי תווים במחצית של מחרוזת (`22B-B-Q1`).
- פירוק משפט למילים לפי מערך מפרידים, ללא `strtok` (`23B-A-Q3a`, `23B-B-Q3`).

## הרעיונות המרכזיים
- מחרוזת היא מערך `char` שנגמר ב-`'\0'`. אורכה לא כולל אותו, וגודל המערך הדרוש כולל אותו: `strlen(s) + 1`.
- `char s[] = "hello"` יוצר מערך שאפשר לשנות. `char *p = "hello"` יוצר מצביע למחרוזת קבועה: מותר להזיז את `p`, **אסור** לשנות את התווים (שגיאת ריצה).
- `s1 == s2` משווה **כתובות**. להשוואת תוכן: `strcmp(a, b)` (0 אם שווים, שלילי אם `a` לפני `b`, חיובי אחרת).
- מערך לא מושמים: `s = "abc"` על `char s[10]` לא מתקמפל. מעתיקים עם `strcpy`.
- פונקציות `string.h`: `strlen`, `strcpy`, `strncpy`, `strcat`, `strcmp`, `strchr` (חיפוש תו), `strstr` (חיפוש תת-מחרוזת), `strtok` (אסורה בשאלות שאומרות זאת).
- `ctype.h`: `isalpha`, `isdigit`, `islower`, `isupper`, `isspace`, `tolower`, `toupper`.
- מונה לכל אות: `int cnt[26] = {0}; cnt[tolower(c) - 'a']++;`.

## תבניות C מדויקות
פירוק מילה מתחילת משפט (בטוח מול סוף המחרוזת):
```c
/* strchr(sep, '\0') returns non-NULL, so test s[i] first */
char *next_word(char *s, const char *sep, char *word)
{
    int i = 0;
    while (s[i] && !strchr(sep, s[i]))
    {
        word[i] = s[i];
        i++;
    }
    word[i] = '\0';
    while (s[i] && strchr(sep, s[i]))
        i++;
    return s[i] ? s + i : NULL;
}
```
בניית מחרוזת דינמית משרשור (`22B-A-Q1`):
```c
char *duplicate_string(const char *base, const char *middle, int times)
{
    /* times copies of base, times-1 copies of middle, one '\0' */
    size_t len = times * strlen(base) + (times - 1) * strlen(middle) + 1;
    char *res = (char *)calloc(len, sizeof(char)); /* calloc: starts as "" */
    int i;
    for (i = 1; i < times; i++)
    {
        strcat(res, base);
        strcat(res, middle);
    }
    strcat(res, base);
    return res;
}
```
הפיכת מחרוזת במקום, ובדיקת אותיות שונות (`24B-B-Q3` משתמשת בשתיהן, ראו [[files]]):
```c
void reverse_string(char *s)
{
    int i = 0, j = (int)strlen(s) - 1;
    for (; i < j; i++, j--)
    {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
}

int has_unique_letters(const char *s)
{
    int seen[26] = {0}, i;
    for (i = 0; s[i]; i++)
    {
        if (!isalpha((unsigned char)s[i]))
            return 0;
        if (seen[tolower((unsigned char)s[i]) - 'a']++)
            return 0;
    }
    return 1;
}
```

## מתכון לפתרון
1. סרקו עם אינדקס `i` עד `s[i] != '\0'`. אל תקראו ל-`strlen` בתנאי הלולאה כשאפשר בלי (זה איטי, וב"פונקציה יעילה" זה יורד נקודות).
2. אם צריך מחרוזת חדשה: חשבו אורך מדויק, הוסיפו 1, הקצו עם `calloc`/`malloc`, וזכרו להשלים `'\0'`.
3. את תוצאות הספירה מחזירים by reference (`int *count1`), ומאפסים אותן בתחילת הפונקציה.
4. חצאי מחרוזת (`22B-B-Q1`): באורך `len` החצי הראשון הוא `[0, len/2)`. החצי השני מתחיל ב-`(len+1)/2` (באורך אי-זוגי מדלגים על התו האמצעי `s[len/2]`).
5. סדר לקסיקוגרפי עולה: `strcmp(a[i], a[i-1]) >= 0` לכל `i`. מספיק זוג אחד שמפר כדי להסיק "לא ממוין לפי השדה הזה".

## דוגמה פתורה
`22B-B-Q1`: סופרים אותיות קטנות במחצית הראשונה וגדולות בשנייה.
```c
int nums_in_halves(const char *str, int *lower, int *upper)
{
    int len = (int)strlen(str), i;
    *lower = *upper = 0;
    for (i = 0; i < len / 2; i++)
        if (islower((unsigned char)str[i]))
            (*lower)++;
    for (i = (len + 1) / 2; str[i]; i++)
        if (isupper((unsigned char)str[i]))
            (*upper)++;
    if (len % 2 == 0)
        return 0;
    return isdigit((unsigned char)str[len / 2]) ? 1 : -1;
}
```
בדיקה: ל-`"t&u5Y%as3k#R"` (אורך 12) המחצית הראשונה `t&u5Y%` מכילה 2 קטנות, והשנייה `as3k#R` מכילה 1 גדולה. הפונקציה מחזירה 0.

## מלכודות
> 🚧 `strchr(sep, '\0')` מחזירה כתובת (סוף המחרוזת עצמה), לא `NULL`. לכן בלולאה על מחרוזת בודקים קודם `s[i]`.

> 🚧 שוכחים `+1` ל-`'\0'` בהקצאה, ואז `strcat` או `strcpy` כותבים מעבר לסוף.

> 🚧 `malloc` לא מאפס. לפני `strcat` על מחרוזת חדשה צריך `res[0] = '\0'` או `calloc`.

> 🚧 `char *str = "hello"; str[0] = 'x';` זו שגיאת ריצה (`22B-B-Q4d`). `str = "good-bye";` לעומת זה חוקי ומשנה רק את המצביע (`22B-A-Q4d`).

> 🚧 `s1 == s2` על שתי מחרוזות משווה כתובות (`25B-B-Q5b`), ולכן כמעט תמיד 0.

> 🚧 `word[i++] = sentence[i]` (כפי שמופיע בפתרון הרשמי של `23B-A-Q3a`) תלוי בסדר חישוב שאינו מובטח. כתבו `word[i] = sentence[i]; i++;` בשתי פקודות.

> 🚧 `fgets` משאירה `'\n'` בסוף השורה. מורידים אותו לפני בדיקות (`24B-B-Q3`).
