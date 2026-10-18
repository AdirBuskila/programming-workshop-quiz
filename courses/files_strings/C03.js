/* files_strings, level 3 - C03 */
COURSE_LEVEL("files_strings", {
  "id": "C03",
  "order": 3,
  "icon": "🔤",
  "title": "תו אחר תו ושורה אחר שורה",
  "goal": "אחרי השלב הזה אפשר לקרוא קובץ בתווים עם fgetc ובשורות עם fgets ולהסיר את תו השורה החדשה.",
  "boss": false,
  "source": "ai-verified",
  "lesson": {
    "html": "<h3>fgetc: תו אחד</h3><p><code>fgetc(f)</code> מחזירה את התו הבא, או <code>EOF</code> כשהקובץ נגמר. הערך <code>EOF</code> אינו תו חוקי, ולכן התוצאה נשמרת ב-<code>int</code> ולא ב-<code>char</code>.</p><pre><code>int ch;\nwhile ((ch = fgetc(f)) != EOF)\n    putchar(ch);</code></pre><div class=\"lesson-rule\">🔑 מצהירים <code>int ch</code>. ב-<code>char</code> הלולאה עלולה לא להיעצר לעולם (כש-<code>char</code> ללא סימן) או להיעצר מוקדם מדי, וההתנהגות תלויה במערכת.</div><p>הסוגריים סביב ההשמה חשובים: <code>ch = fgetc(f) != EOF</code> משווה קודם ושומרת ב-<code>ch</code> את 0 או 1.</p><h3>fgets: שורה</h3><p><code>fgets(buf, n, f)</code> קוראת עד <b>n-1 תווים</b> או עד סוף השורה, מה שבא קודם. היא:</p><ul><li><b>משאירה</b> את <code>'\\n'</code> בסוף המחרוזת אם הוא נקרא;</li><li>מוסיפה <code>'\\0'</code> בסוף;</li><li>מחזירה <code>NULL</code> כשאין מה לקרוא, ולכן <code>while (fgets(buf, n, f))</code> היא לולאת קריאה בטוחה.</li></ul><pre><code>char line[101];\nwhile (fgets(line, 101, f))\n{\n    size_t len = strlen(line);\n    if (len &gt; 0 &amp;&amp; line[len - 1] == '\\n')\n        line[len - 1] = '\\0';      /* remove the newline */\n    puts(line);\n}</code></pre><div class=\"lesson-ex\">דוגמה: שורה <code>ab</code> בקובץ נקראת כ-<code>\"ab\\n\"</code> (אורך 3). אחרי ההסרה נשאר <code>ab</code> (אורך 2). שורה ריקה בקובץ נקראת כ-<code>\"\\n\"</code>, ובכל זאת <code>fgets</code> מחזירה בשבילה מחרוזת תקינה.</div><div class=\"lesson-trap\">⚠️ <code>fgets(buf, 4, f)</code> על שורה ארוכה קוראת רק 3 תווים. את שאר השורה תקרא הקריאה הבאה.</div>"
  },
  "questions": [
    {
      "id": "C03-Q1",
      "step": {
        "type": "numeric",
        "answer": 8,
        "tol": 0,
        "prompt": "הקובץ מכיל ארבע שורות: `a`, אחר כך `bb`, אחר כך שורה ריקה, אחר כך `c`, וכל שורה מסתיימת ב-`'\\n'`. מה ערך `n` בסוף?\n```c\nint ch, n = 0;\nwhile ((ch = fgetc(f)) != EOF)\n    n++;\n```",
        "explain": "הלולאה סופרת כל תו, כולל תווי השורה החדשה: $1+1+2+1+1+1+1=8$ (`a`, שורה, `bb`, שורה, שורה, `c`, שורה)."
      },
      "recap": "`fgetc` מחזירה גם את `'\\n'` כתו רגיל."
    },
    {
      "id": "C03-Q2",
      "step": {
        "type": "numeric",
        "answer": 4,
        "tol": 0,
        "prompt": "אותו קובץ כמו בשאלה הקודמת (`a`, `bb`, שורה ריקה, `c`, כל שורה מסתיימת ב-`'\\n'`). מה ערך `n` בסוף?\n```c\nchar line[20];\nint n = 0;\nwhile (fgets(line, 20, f))\n    n++;\n```",
        "explain": "`fgets` מחזירה מחרוזת לכל אחת מארבע השורות, גם לשורה הריקה (היא מחזירה `\"\\n\"`). `NULL` מוחזר רק בסוף הקובץ, לכן $n=4$."
      },
      "recap": "`fgets` מחזירה `NULL` רק בסוף הקובץ, גם שורה ריקה נקראת."
    },
    {
      "id": "C03-Q3",
      "question": "איזו הצהרה נכונה למשתנה `ch` בלולאה `while ((ch = fgetc(f)) != EOF)` ?",
      "options": [
        {
          "id": "a",
          "value": "`int ch;`"
        },
        {
          "id": "b",
          "value": "`char ch;`"
        },
        {
          "id": "c",
          "value": "`unsigned char ch;`"
        },
        {
          "id": "d",
          "value": "כל אחד מהטיפוסים האלה נכון באותה מידה"
        }
      ],
      "correctId": "a",
      "explanation": "`fgetc` מחזירה `int`: ערך של תו, או `EOF` שאינו תו. רק ב-`int` אפשר להבדיל ביניהם תמיד. ב-`unsigned char` ההשוואה ל-`EOF` (שלילי) אף פעם לא נכונה והלולאה לא נגמרת. ב-`char` תלוי אם הוא עם סימן: או שהלולאה נעצרת באמצע הקובץ בתו עם הערך 255, או שהיא אינסופית. לכן הטיפוסים לא שווים.",
      "recap": "תוצאת `fgetc` נשמרת ב-`int`."
    },
    {
      "id": "C03-Q4",
      "step": {
        "type": "numeric",
        "answer": 3,
        "tol": 0,
        "prompt": "הקובץ מתחיל בשורה `ab` (ואחריה `'\\n'`) ובשורה נוספת. מה ידפיס הקוד?\n```c\nchar buf[10];\nfgets(buf, 10, f);\nprintf(\"%d\", (int)strlen(buf));\n```",
        "explain": "`fgets` קוראת את `a`, `b` ואת `'\\n'` ומשאירה אותו במחרוזת: האורך הוא 3."
      },
      "recap": "`fgets` משאירה את `'\\n'` במחרוזת."
    },
    {
      "id": "C03-Q5",
      "step": {
        "type": "numeric",
        "answer": 3,
        "tol": 0,
        "prompt": "הקובץ מכיל שורה אחת `abcdefgh`. מה ידפיס הקוד?\n```c\nchar buf[10];\nfgets(buf, 4, f);\nprintf(\"%d\", (int)strlen(buf));\n```",
        "explain": "עם `n = 4` נקראים לכל היותר $4-1=3$ תווים (`abc`), והמקום הרביעי שמור ל-`'\\0'`. האורך הוא 3."
      },
      "recap": "`fgets(buf, n, f)` קוראת לכל היותר `n-1` תווים."
    },
    {
      "id": "C03-Q6",
      "step": {
        "type": "fillblank",
        "code": true,
        "prompt": "השלימו את הסרת `'\\n'` מסוף השורה (השורה היא `hi` ואחריה `'\\n'`, והאורך אחרי ההסרה צריך להיות 2).",
        "lines": [
          "size_t len = strlen(line);",
          "if (len > 0 && line[len - 1] == '\\n')",
          "    line[___] = '\\0';"
        ],
        "blankIndex": 2,
        "options": [
          {
            "id": "a",
            "value": "len - 1"
          },
          {
            "id": "b",
            "value": "len"
          },
          {
            "id": "c",
            "value": "0"
          },
          {
            "id": "d",
            "value": "1"
          }
        ],
        "correctId": "a",
        "explain": "התו `'\\n'` נמצא במקום $len-1$, ולכן שם שמים `'\\0'`. עם `len` מחליפים את ה-`'\\0'` הקיים ב-`'\\0'` ושום דבר לא משתנה. עם `0` המחרוזת הופכת לריקה, ועם `1` היא מתקצרת לתו אחד (נבדק עם clang)."
      },
      "recap": "מוחקים את `'\\n'` ב-`line[len - 1] = '\\0'`."
    }
  ]
});
