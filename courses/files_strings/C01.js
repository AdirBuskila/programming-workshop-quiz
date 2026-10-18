/* files_strings, level 1 - C01 */
COURSE_LEVEL("files_strings", {
  "id": "C01",
  "order": 1,
  "icon": "📂",
  "title": "פתיחה, מצבים וכתיבה",
  "goal": "אחרי השלב הזה אפשר לפתוח קובץ במצב הנכון, לבדוק שהפתיחה הצליחה, לכתוב אליו ולסגור אותו.",
  "boss": false,
  "source": "ai-verified",
  "lesson": {
    "html": "<p>קובץ בתוכנית מיוצג על ידי מצביע מטיפוס <code>FILE *</code>. מקבלים אותו מהפונקציה <code>fopen(name, mode)</code> ובסוף משחררים אותו עם <code>fclose(f)</code>.</p><pre><code>FILE *f = fopen(\"data.txt\", \"w\");\nif (!f)\n    return 1;          /* the open failed */\nfprintf(f, \"%d\", 5);\nfclose(f);</code></pre><div class=\"lesson-rule\">🔑 <code>fopen</code> מחזירה <code>NULL</code> כשהפתיחה נכשלה (למשל קובץ שלא קיים בקריאה). תמיד בודקים <code>NULL</code> לפני שמשתמשים במצביע, אחרת התוכנית קורסת.</div><h3>מצבי פתיחה</h3><table><tr><th>מצב</th><th>משמעות</th></tr><tr><td><code>\"r\"</code></td><td>קריאה. הקובץ חייב להיות קיים, אחרת מתקבל NULL</td></tr><tr><td><code>\"w\"</code></td><td>כתיבה. אם הקובץ קיים, <b>התוכן שלו נמחק</b>. אם לא, הוא נוצר</td></tr><tr><td><code>\"a\"</code></td><td>הוספה בסוף הקובץ. התוכן הקיים נשמר</td></tr><tr><td><code>\"r+\"</code>, <code>\"w+\"</code></td><td>גם קריאה וגם כתיבה (ב-<code>\"w+\"</code> הקובץ מתאפס בפתיחה)</td></tr><tr><td><code>\"rb\"</code>, <code>\"wb\"</code></td><td>אותם מצבים לקבצים בינאריים (האות b)</td></tr></table><h3>פונקציות כתיבה</h3><ul><li><code>fprintf(f, \"%d,%d\", 7, 8)</code> כמו <code>printf</code> אבל לקובץ.</li><li><code>fputs(str, f)</code> כותבת מחרוזת <b>בלי</b> לשרשר תו שורה חדשה.</li><li><code>fputc(ch, f)</code> כותבת תו אחד.</li><li><code>puts(str)</code> כותבת למסך <b>ומוסיפה</b> <code>'\\n'</code> בסוף. <code>fputs(str, stdout)</code> לא מוסיפה.</li></ul><div class=\"lesson-ex\">דוגמה: אם הקובץ מכיל <code>AB</code> ופותחים אותו ב-<code>\"a\"</code> וכותבים <code>fputs(\"C\", f)</code>, התוכן הופך ל-<code>ABC</code>. אם פותחים אותו ב-<code>\"w\"</code> וכותבים אותו דבר, התוכן הוא <code>C</code> בלבד.</div><div class=\"lesson-trap\">⚠️ <code>\"w\"</code> מוחק קובץ קיים כבר ברגע הפתיחה, עוד לפני שכתבתם משהו. כשרוצים להוסיף משתמשים ב-<code>\"a\"</code>.</div>"
  },
  "questions": [
    {
      "id": "C01-Q1",
      "question": "מה מחזירה `fopen(\"nope.txt\", \"r\")` כשהקובץ `nope.txt` לא קיים בתיקייה?",
      "options": [
        {
          "id": "a",
          "value": "`NULL`"
        },
        {
          "id": "b",
          "value": "מצביע תקין לקובץ ריק"
        },
        {
          "id": "c",
          "value": "התוכנית קורסת כבר בתוך `fopen`"
        },
        {
          "id": "d",
          "value": "מצביע ל-`stdin`"
        }
      ],
      "correctId": "a",
      "explanation": "במצב קריאה קובץ שלא קיים לא נוצר, ו-`fopen` מחזירה `NULL` (נבדק עם clang). לכן בודקים `if (!f)` מיד אחרי הפתיחה. מצביע תקין לקובץ ריק היה קורה במצב כתיבה. הקריסה מתרחשת רק אם משתמשים במצביע ה-`NULL`, לא בפתיחה עצמה. `stdin` הוא קובץ סטנדרטי אחר שאינו קשור.",
      "recap": "`fopen` נכשלת עם `NULL`, ותמיד בודקים אותה."
    },
    {
      "id": "C01-Q2",
      "question": "הקובץ `t.txt` מכיל `AB`. התוכנית מריצה:\n```c\nFILE *f = fopen(\"t.txt\", \"w\");\nfputs(\"C\", f);\nfclose(f);\n```\nמה תוכן הקובץ אחרי הריצה?",
      "options": [
        {
          "id": "a",
          "value": "`C`"
        },
        {
          "id": "b",
          "value": "`ABC`"
        },
        {
          "id": "c",
          "value": "`AB`"
        },
        {
          "id": "d",
          "value": "`CB`"
        }
      ],
      "correctId": "a",
      "explanation": "מצב `\"w\"` מוחק את התוכן הקיים בפתיחה, ולכן נשאר רק `C` (נבדק עם clang). `ABC` היה מתקבל במצב `\"a\"`. `AB` היה נשאר לו הכתיבה לא התבצעה. `CB` היה מתקבל רק אם `C` היה דורס את התו הראשון, וזה לא מה ש-`\"w\"` עושה.",
      "recap": "`\"w\"` מוחק את התוכן הקיים, `\"a\"` מוסיף בסוף."
    },
    {
      "id": "C01-Q3",
      "step": {
        "type": "text",
        "accept": [
          "x125"
        ],
        "normalize": "none",
        "prompt": "הקובץ `t.txt` מכיל `x1`. מה יהיה תוכנו (בלי רווחים) אחרי הקוד?\n```c\nFILE *f = fopen(\"t.txt\", \"a\");\nfprintf(f, \"%d\", 25);\nfclose(f);\n```",
        "explain": "מצב `\"a\"` שומר את `x1` וכותב אחריו את `25`, ולכן התוכן `x125`."
      },
      "recap": "במצב `\"a\"` הכתיבה נעשית אחרי התוכן הקיים."
    },
    {
      "id": "C01-Q4",
      "step": {
        "type": "numeric",
        "answer": 7,
        "tol": 0,
        "prompt": "הקובץ נפתח חדש בכתיבה, ואז מתבצע הקוד הבא. כמה תווים יש בקובץ בסוף?\n```c\nfputs(\"ab\", f);\nfputc('c', f);\nfprintf(f, \"%d-%d\", 12, 3);\n```",
        "explain": "נכתבים `ab` (2 תווים), `c` (תו אחד) ו-`12-3` (4 תווים): $2+1+4=7$, כלומר `abc12-3`."
      },
      "recap": "כל פונקציית כתיבה מוסיפה את התווים שלה בלבד, בלי תו שורה חדשה אוטומטי."
    },
    {
      "id": "C01-Q5",
      "step": {
        "type": "numeric",
        "answer": 2,
        "tol": 0,
        "prompt": "כמה שורות יוצגו על המסך?\n```c\nputs(\"a\");\nfputs(\"b\", stdout);\nputs(\"c\");\n```",
        "explain": "`puts(\"a\")` מדפיסה `a` ותו שורה חדשה. `fputs(\"b\", stdout)` מדפיסה `b` בלי שורה חדשה, ולכן `puts(\"c\")` ממשיכה באותה שורה: `bc`. בסך הכול שתי שורות: `a` ו-`bc`."
      },
      "recap": "`puts` מוסיפה `'\\n'`, `fputs` לא."
    },
    {
      "id": "C01-Q6",
      "step": {
        "type": "order",
        "code": true,
        "prompt": "סדרו את השלבים של כתיבת המספר 5 לקובץ בצורה נכונה ובטוחה.",
        "lines": [
          "FILE *f = fopen(\"out.txt\", \"w\");",
          "if (!f) return 1;",
          "fprintf(f, \"%d\", 5);",
          "fclose(f);"
        ],
        "explain": "קודם פותחים, אחר כך בודקים שהפתיחה הצליחה, רק אז כותבים, ובסוף סוגרים."
      },
      "recap": "פותחים, בודקים `NULL`, משתמשים, סוגרים."
    }
  ]
});
