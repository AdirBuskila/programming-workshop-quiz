/* files_strings, level 7 - C07 */
COURSE_LEVEL("files_strings", {
  "id": "C07",
  "order": 7,
  "icon": "🧩",
  "title": "תבניות מהמבחן: מילה שלמה, סינון שורות, טקסט לבינארי",
  "goal": "אחרי השלב הזה אפשר לכתוב את שלושת סוגי הפונקציות שחוזרות במבחנים: ספירת מילה שלמה, סינון שורות לקובץ חדש והמרת טקסט לרשומות.",
  "boss": false,
  "source": "ai-verified",
  "lesson": {
    "html": "<h3>1. ספירת מילה שלמה</h3><p>קוראים מילה אחר מילה עם <code>fscanf(f, \"%100s\", buf)</code> (הרוחב מונע גלישה) ומשווים ב-<code>strcmp</code> שבודקת שוויון מלא.</p><pre><code>int count = 0;\nchar buf[101];\nwhile (fscanf(f, \"%100s\", buf) == 1)\n    if (strcmp(buf, word) == 0)\n        count++;</code></pre><div class=\"lesson-rule\">🔑 <code>strstr(buf, word)</code> בודקת אם <code>word</code> <b>מוכלת</b> בתוך המילה, ולכן סופרת גם <code>lives</code> ו-<code>alive</code> עבור <code>live</code>. לשוויון מלא משתמשים ב-<code>strcmp(...) == 0</code>.</div><h3>2. סינון שורות לקובץ חדש</h3><pre><code>FILE *in = fopen(src, \"r\"), *out = fopen(dst, \"w\");\nchar line[101];\nif (!in || !out)\n    return;\nwhile (fgets(line, 101, in))\n{\n    size_t len = strlen(line);\n    if (len &gt; 0 &amp;&amp; line[len - 1] == '\\n')\n        line[len - 1] = '\\0';\n    if (strlen(line) &gt; 3)              /* the condition */\n        fprintf(out, \"%s\\n\", line);    /* write the line back */\n}\nfclose(in);\nfclose(out);</code></pre><p>מסירים את <code>'\\n'</code> לפני הבדיקות, וכותבים אותו מחדש עם <code>\"%s\\n\"</code>. גודל המערך הוא אורך השורה המקסימלי + 1 לתו <code>'\\0'</code> + 1 לתו <code>'\\n'</code>.</p><h3>עיבוד של שורה: אותיות שונות</h3><p>כדי לבדוק שכל התווים אותיות שונות זו מזו (בלי הבדל בין גדולה לקטנה) מחזיקים מערך מונים של 26 אותיות ומשתמשים ב-<code>isalpha</code> וב-<code>tolower</code> מ-<code>ctype.h</code>:</p><pre><code>int has_unique_letters(const char *s)\n{\n    int seen[26] = {0}, i, k;\n    for (i = 0; s[i]; i++)\n    {\n        if (!isalpha((unsigned char)s[i]))\n            return 0;                       /* not a letter */\n        k = tolower((unsigned char)s[i]) - 'a';\n        if (seen[k])\n            return 0;                       /* repeated letter */\n        seen[k] = 1;\n    }\n    return 1;\n}</code></pre><p>הפיכת מחרוזת במקום: שני אינדקסים, <code>i</code> מההתחלה ו-<code>j</code> מהסוף, מחליפים ומתקדמים עד שהם נפגשים.</p><h3>3. מטקסט לרשומות בינאריות</h3><pre><code>typedef struct\n{\n    char id[10];\n    char name[31];\n    double total;\n} clientData;\n\nwhile (fscanf(in, \"%9s%30s%lf\", c.id, c.name, &amp;c.total) == 3)\n    fwrite(&amp;c, sizeof(clientData), 1, out);</code></pre><p>הרוחב קטן ב-1 מגודל המערך: <code>%9s</code> ל-<code>char id[10]</code>, כדי שיישאר מקום ל-<code>'\\0'</code>. וכותבים את הרשומה כולה: <code>sizeof(clientData)</code>.</p><div class=\"lesson-trap\">⚠️ בלי הגבלת רוחב, <code>%s</code> שקורא מילה ארוכה כותב מעבר לגבולות המערך.</div>"
  },
  "questions": [
    {
      "id": "C07-Q1",
      "step": {
        "type": "numeric",
        "answer": 4,
        "tol": 0,
        "prompt": "הקובץ מכיל בשורה אחת `live lives alive live`. מה ידפיס הקוד?\n```c\nchar buf[101];\nint count = 0;\nwhile (fscanf(f, \"%100s\", buf) == 1)\n    if (strstr(buf, \"live\"))\n        count++;\nprintf(\"%d\", count);\n```",
        "explain": "`strstr` מצליחה בכל מילה שמכילה את `live`: `live`, `lives`, `alive`, `live`. התוצאה היא 4, בעוד ש-`strcmp(buf, \"live\") == 0` הייתה סופרת רק 2 מילים שלמות."
      },
      "recap": "מילה שלמה: `strcmp == 0`, לא `strstr`."
    },
    {
      "id": "C07-Q2",
      "step": {
        "type": "text",
        "accept": [
          "123456789"
        ],
        "normalize": "none",
        "prompt": "הקובץ מכיל `1234567890123`. מה יודפס?\n```c\nchar id[10];\nfscanf(f, \"%9s\", id);\nprintf(\"%s\", id);\n```",
        "explain": "`%9s` קוראת לכל היותר 9 תווים: `123456789`, ושומרת את המקום העשירי ל-`'\\0'`. שאר הספרות נשארות בקובץ לקריאה הבאה."
      },
      "recap": "רוחב הקריאה קטן ב-1 מגודל המערך."
    },
    {
      "id": "C07-Q3",
      "question": "איזו מהמחרוזות הבאות מקבלת 1 מהפונקציה `has_unique_letters` שבשיעור (רק אותיות, כולן שונות, גדולה וקטנה נחשבות אותה אות) ?",
      "options": [
        {
          "id": "a",
          "value": "`Table`"
        },
        {
          "id": "b",
          "value": "`Alisa`"
        },
        {
          "id": "c",
          "value": "`ab#c`"
        },
        {
          "id": "d",
          "value": "`Noon`"
        }
      ],
      "correctId": "a",
      "explanation": "ב-`Table` כל חמש האותיות שונות (נבדק עם clang). ב-`Alisa` יש `A` ו-`a`, שנחשבות לאותה אות. ב-`ab#c` יש תו שאינו אות. ב-`Noon` האות `n` חוזרת פעמיים (`N` ו-`n`).",
      "recap": "מערך מונים של 26 אותיות עם `tolower` בודק שכל אות מופיעה פעם אחת."
    },
    {
      "id": "C07-Q4",
      "step": {
        "type": "numeric",
        "answer": 2,
        "tol": 0,
        "prompt": "קובץ הקלט מכיל ארבע שורות: `abcd`, `ab`, `abcde` ו-`x` (כל אחת מסתיימת ב-`'\\n'`). הפונקציה מהשיעור מעתיקה לקובץ הפלט רק שורות שאורכן (בלי `'\\n'`) גדול מ-3. כמה שורות יהיו בקובץ הפלט?",
        "explain": "האורכים הם 4, 2, 5 ו-1. רק `abcd` ו-`abcde` עומדות בתנאי, ולכן בקובץ הפלט שתי שורות."
      },
      "recap": "מסירים את `'\\n'` לפני שבודקים אורך."
    },
    {
      "id": "C07-Q5",
      "step": {
        "type": "findbug",
        "code": true,
        "prompt": "הפונקציה אמורה להמיר כל שורה בקובץ הטקסט לרשומה בינארית שלמה, אבל הקובץ הבינארי יוצא קטן מדי ורשומות נקראות ממנו בצורה שבורה. איזו שורה שגויה?",
        "lines": [
          "clientData c;",
          "FILE *in = fopen(text_name, \"r\");",
          "FILE *out = fopen(binary_name, \"wb\");",
          "if (!in || !out) exit(1);",
          "while (fscanf(in, \"%9s%30s%lf\", c.id, c.name, &c.total) == 3)",
          "    fwrite(&c, sizeof(c.id), 1, out);",
          "fclose(in);",
          "fclose(out);"
        ],
        "bugIndex": 5,
        "explain": "`sizeof(c.id)` הוא גודל השדה הראשון בלבד. כל רשומה חייבת להיכתב בשלמותה עם `sizeof(clientData)`."
      },
      "recap": "כותבים רשומה שלמה: `sizeof` של המבנה, לא של שדה."
    },
    {
      "id": "C07-Q6",
      "step": {
        "type": "order",
        "code": true,
        "prompt": "סדרו את הפונקציה שמעתיקה את כל השורות מקובץ טקסט אחד לאחר (כל פקודה היא בלוק לוגי אחד).",
        "lines": [
          "FILE *in = fopen(src, \"r\"), *out = fopen(dst, \"w\");",
          "if (!in || !out) return;",
          "while (fgets(line, 101, in))",
          "    fputs(line, out);",
          "fclose(in); fclose(out);"
        ],
        "explain": "פותחים את שני הקבצים, בודקים אותם, מעתיקים שורה אחר שורה (`fgets` משאירה את `'\\n'` ולכן `fputs` מספיקה) וסוגרים."
      },
      "recap": "העתקת שורות: `while (fgets(...)) fputs(...)`."
    }
  ]
});
