/* files_strings, level 5 - C05 */
COURSE_LEVEL("files_strings", {
  "id": "C05",
  "order": 5,
  "icon": "💾",
  "title": "קבצים בינאריים: רשומות עם fwrite ו-fread",
  "goal": "אחרי השלב הזה אפשר לכתוב רשומות לקובץ בינארי, לקרוא אותן בלולאה ולסנן לפי תנאי.",
  "boss": false,
  "source": "ai-verified",
  "lesson": {
    "html": "<p>בקובץ טקסט שומרים תווים. בקובץ <b>בינארי</b> שומרים את הבתים של המבנה כמו שהם בזיכרון, רשומה אחרי רשומה, ולכל רשומה אותו גודל קבוע. אין שורות ואין רווחים, ופותחים עם <code>\"rb\"</code> או <code>\"wb\"</code>.</p><pre><code>typedef struct\n{\n    int id;\n    int score;\n} rec;</code></pre><ul><li>כתיבה: <code>fwrite(&amp;r, sizeof(r), 1, f)</code>. הפרמטרים: כתובת הרשומה, גודל רשומה אחת, כמה רשומות, הקובץ.</li><li>קריאה: <code>fread(&amp;r, sizeof(r), 1, f)</code>. <b>הערך המוחזר הוא מספר הרשומות שנקראו</b>, כאן 1 בהצלחה ו-0 בסוף הקובץ.</li></ul><pre><code>rec a;\nint count = 0;\nFILE *f = fopen(name, \"rb\");\nif (!f)\n    return -1;\nwhile (fread(&amp;a, sizeof(a), 1, f) == 1)    /* one record per iteration */\n    if (a.score &gt;= 70)\n        count++;\nfclose(f);</code></pre><div class=\"lesson-rule\">🔑 לולאת קריאה בינארית: <code>while (fread(&amp;a, sizeof(a), 1, f) == 1)</code>. כותבים <code>sizeof(a)</code> (או <code>sizeof(rec)</code>) כדי לכתוב ולקרוא את הרשומה כולה.</div><h3>מה שונה מטקסט</h3><ul><li>המספר 7 נכתב ב-<code>fprintf(f, \"%d\", 7)</code> כתו אחד. ב-<code>fwrite</code> הוא תופס תמיד <code>sizeof(int)</code> בתים, ולכן גם <code>1234567</code> תופס אותו גודל.</li><li>הגודל המדויק של מבנה תלוי במערכת ולכן תמיד כותבים <code>sizeof</code> ולא מספר קבוע.</li><li>בקובץ בינארי אין טעם לקרוא עם <code>fgets</code> או <code>fscanf</code>.</li></ul><div class=\"lesson-ex\">דוגמה: בקובץ עם חמש רשומות עם הציונים 50, 90, 70, 95, 60 הלולאה לעיל סופרת את 90, 70 ו-95, ולכן <code>count</code> הוא 3.</div><div class=\"lesson-trap\">⚠️ <code>fwrite(&amp;r, sizeof(r.id), 1, f)</code> כותבת רק את השדה הראשון, והרשומות בקובץ קטנות מדי. תמיד גודל של הרשומה כולה.</div>"
  },
  "questions": [
    {
      "id": "C05-Q1",
      "question": "המשתנה `r` הוא רשומה מטיפוס `rec` (עם `id` ו-`score`). איזו שורה כותבת את הרשומה כולה כגוש בינארי אחד לקובץ שנפתח ב-`\"wb\"` ?",
      "options": [
        {
          "id": "a",
          "value": "`fwrite(&r, sizeof(r), 1, f);`"
        },
        {
          "id": "b",
          "value": "`fwrite(r, sizeof(r), 1, f);`"
        },
        {
          "id": "c",
          "value": "`fwrite(&r, sizeof(r.id), 1, f);`"
        },
        {
          "id": "d",
          "value": "`fprintf(f, \"%d %d\", r.id, r.score);`"
        }
      ],
      "correctId": "a",
      "explanation": "`fwrite` מקבלת כתובת, ולכן `&r` נכון. התשובה בלי `&` לא עוברת הידור (מבנה במקום כתובת). התשובה עם `sizeof(r.id)` כותבת רק את השדה הראשון. `fprintf` כותבת טקסט באורך משתנה ולא רשומה בגודל קבוע.",
      "recap": "`fwrite(&r, sizeof(r), 1, f)` כותבת רשומה שלמה."
    },
    {
      "id": "C05-Q2",
      "step": {
        "type": "numeric",
        "answer": 3,
        "tol": 0,
        "prompt": "בקובץ בינארי חמש רשומות עם הציונים 50, 90, 70, 95, 60 (לפי הסדר). מה ערך `count` בסוף?\n```c\nrec a;\nint count = 0;\nwhile (fread(&a, sizeof(a), 1, f) == 1)\n    if (a.score >= 70)\n        count++;\n```",
        "explain": "הציונים שלפחות 70 הם 90, 70 ו-95: שלוש רשומות."
      },
      "recap": "לולאת `fread` עוברת על כל הרשומות, והתנאי מסנן."
    },
    {
      "id": "C05-Q3",
      "step": {
        "type": "numeric",
        "answer": 0,
        "tol": 0,
        "prompt": "בקובץ בינארי שתי רשומות בלבד. הקוד קורא שלוש פעמים ברצף `n = fread(&a, sizeof(a), 1, f);`. מה ערך `n` בקריאה השלישית?",
        "explain": "שתי הקריאות הראשונות מחזירות 1. אחרי הרשומה השנייה אין מה לקרוא, ולכן השלישית קוראת 0 רשומות ומחזירה 0."
      },
      "recap": "`fread` מחזירה 0 בסוף הקובץ."
    },
    {
      "id": "C05-Q4",
      "question": "כותבים קודם את הערך 7 ואחר כך את הערך 1234567 (כל אחד לקובץ חדש). מה נכון?",
      "options": [
        {
          "id": "a",
          "value": "ב-`fwrite(&x, sizeof(int), 1, f)` שני הקבצים באותו גודל, וב-`fprintf(f, \"%d\", x)` הקובץ של 1234567 גדול יותר"
        },
        {
          "id": "b",
          "value": "ב-`fprintf(f, \"%d\", x)` שני הקבצים באותו גודל, וב-`fwrite` הקובץ של 1234567 גדול יותר"
        },
        {
          "id": "c",
          "value": "בשתי השיטות שני הקבצים באותו גודל"
        },
        {
          "id": "d",
          "value": "בשתי השיטות הקובץ של 1234567 גדול יותר"
        }
      ],
      "correctId": "a",
      "explanation": "`fwrite` כותבת תמיד `sizeof(int)` בתים, בלי קשר לערך. `fprintf` כותבת את הספרות כתווים, ולכן 7 הוא תו אחד ו-1234567 הוא שבעה תווים (נבדק עם clang). שתי התשובות האחרונות אינן מתאימות לאף אחת מהשיטות, והשנייה הפוכה.",
      "recap": "ב-`fwrite` הגודל קבוע, בטקסט הוא תלוי במספר הספרות."
    },
    {
      "id": "C05-Q5",
      "step": {
        "type": "findbug",
        "code": true,
        "prompt": "הפונקציה אמורה לספור דירות עם `rooms` חדרים ומחיר של לכל היותר `max_price`. בקובץ ארבע דירות: (3 חדרים, 500), (2, 400), (3, 900), (4, 300). הקריאה `count_matching(name, 3, 600)` צריכה להחזיר 1 אבל מחזירה 4. איזו שורה שגויה?",
        "lines": [
          "FILE *f = fopen(name, \"rb\");",
          "apartment a;",
          "int count = 0;",
          "if (!f) return -1;",
          "while (fread(&a, sizeof(apartment), 1, f) == 1)",
          "    if (a.rooms == rooms || a.price <= max_price)",
          "        count++;",
          "fclose(f);",
          "return count;"
        ],
        "bugIndex": 5,
        "explain": "התנאי צריך להיות `&&`: שני התנאים חייבים להתקיים. עם `||` מספיק שאחד מהם מתקיים וכל ארבע הדירות נספרות."
      },
      "recap": "סינון לפי שני תנאים משתמש ב-`&&`."
    },
    {
      "id": "C05-Q6",
      "step": {
        "type": "order",
        "code": true,
        "prompt": "סדרו את הפונקציה שמדפיסה את ה-`id` של כל הרשומות בקובץ הבינארי.",
        "lines": [
          "rec a;",
          "FILE *f = fopen(\"recs.bin\", \"rb\");",
          "if (!f) return;",
          "while (fread(&a, sizeof(a), 1, f) == 1)",
          "    printf(\"%d\\n\", a.id);",
          "fclose(f);"
        ],
        "explain": "מצהירים על המשתנה, פותחים, בודקים, קוראים בלולאה ואז סוגרים. הגוף של הלולאה בא מיד אחרי תנאי הלולאה."
      },
      "recap": "קריאה בינארית: פותחים עם `\"rb\"`, בודקים, לולאת `fread`, סוגרים."
    }
  ]
});
