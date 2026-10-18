/* files_strings, level 6 - C06 */
COURSE_LEVEL("files_strings", {
  "id": "C06",
  "order": 6,
  "icon": "🧭",
  "title": "מיקום בקובץ: ftell, fseek ו-rewind",
  "goal": "אחרי השלב הזה אפשר לדעת איפה הסמן בקובץ, לקפוץ למקום מסוים, לחזור להתחלה ולחשב גודל קובץ.",
  "boss": false,
  "source": "ai-verified",
  "lesson": {
    "html": "<p>לכל קובץ פתוח יש <b>סמן</b>: המיקום בבתים מתחילת הקובץ. כל קריאה וכל כתיבה מקדמות אותו.</p><ul><li><code>ftell(f)</code> מחזירה את מיקום הסמן (בבתים מההתחלה, כשהראשון הוא 0).</li><li><code>fseek(f, offset, origin)</code> מזיזה את הסמן, כאשר ה-origin הוא <code>SEEK_SET</code> (מתחילת הקובץ), <code>SEEK_CUR</code> (מהמיקום הנוכחי) או <code>SEEK_END</code> (מסוף הקובץ).</li><li><code>rewind(f)</code> מחזירה את הסמן להתחלה, כמו <code>fseek(f, 0, SEEK_SET)</code>.</li></ul><div class=\"lesson-ex\">נניח שהקובץ (בינארי, <code>\"rb\"</code>) מכיל <code>ABCDEFGH</code>. אחרי קריאת שני תווים <code>ftell</code> היא 2. אחרי <code>fseek(f, 5, SEEK_SET)</code> הקריאה הבאה מחזירה <code>F</code>. אחרי <code>fseek(f, -1, SEEK_END)</code> הקריאה הבאה מחזירה <code>H</code>, התו האחרון.</div><h3>שלושה שימושים</h3><ul><li><b>גודל הקובץ:</b> <code>fseek(f, 0, SEEK_END); size = ftell(f);</code>. הערך הוא מספר הבתים, ואם הקובץ מורכב מרשומות, מספר הרשומות הוא <code>size / sizeof(rec)</code>.</li><li><b>רשומה במקום ידוע:</b> רשומה מספר <code>i</code> (הראשונה היא 0) נמצאת ב-<code>i * sizeof(rec)</code>, כלומר <code>fseek(f, i * sizeof(rec), SEEK_SET)</code> ואחר כך <code>fread</code>.</li><li><b>שני מעברים:</b> עוברים ומונים, <code>rewind(f)</code>, מקצים בגודל שנמנה, ועוברים שוב כדי למלא.</li></ul><pre><code>int n = 0, i = 0;\nrec a, *arr;\nwhile (fread(&amp;a, sizeof(a), 1, f) == 1)   /* pass 1: count */\n    n++;\nrewind(f);                                /* back to the start */\narr = (rec *)calloc(n, sizeof(rec));\nwhile (fread(&amp;a, sizeof(a), 1, f) == 1)   /* pass 2: fill */\n    arr[i++] = a;</code></pre><div class=\"lesson-trap\">⚠️ חישובי מיקום כמו גודל וקפיצה לפי בתים מדויקים בקובץ שנפתח כבינארי (<code>\"rb\"</code>). בקובץ טקסט משתמשים רק בערך ש-<code>ftell</code> החזירה ובקפיצה אליו עם <code>SEEK_SET</code>, ולא בחישובי בתים.</div>"
  },
  "questions": [
    {
      "id": "C06-Q1",
      "step": {
        "type": "numeric",
        "answer": 3,
        "tol": 0,
        "prompt": "הקובץ (נפתח כבינארי) מכיל `ABCDEFGH`. מה ידפיס הקוד?\n```c\nfgetc(f);\nfgetc(f);\nfgetc(f);\nprintf(\"%ld\", ftell(f));\n```",
        "explain": "כל `fgetc` מקדמת את הסמן בבית אחד. אחרי שלוש קריאות הסמן במקום 3."
      },
      "recap": "`ftell` שווה למספר הבתים שכבר עברנו."
    },
    {
      "id": "C06-Q2",
      "step": {
        "type": "text",
        "accept": [
          "C"
        ],
        "normalize": "none",
        "prompt": "הקובץ (בינארי) מכיל `ABCDEFGH`. איזה תו יודפס?\n```c\nfseek(f, 2, SEEK_SET);\nputchar(fgetc(f));\n```",
        "explain": "המיקומים מתחילים ב-0: `A` ב-0, `B` ב-1, `C` ב-2. אחרי `fseek(f, 2, SEEK_SET)` הקריאה מחזירה `C`."
      },
      "recap": "`SEEK_SET` סופר מההתחלה, והתו הראשון במקום 0."
    },
    {
      "id": "C06-Q3",
      "step": {
        "type": "numeric",
        "answer": 8,
        "tol": 0,
        "prompt": "הקובץ (בינארי) מכיל `ABCDEFGH`. מה ידפיס הקוד?\n```c\nfseek(f, 0, SEEK_END);\nprintf(\"%ld\", ftell(f));\n```",
        "explain": "הקפיצה לסוף מציבה את הסמן במקום שאחרי התו האחרון, והוא שווה לגודל הקובץ בבתים: 8."
      },
      "recap": "גודל קובץ: `fseek(f, 0, SEEK_END)` ואז `ftell`."
    },
    {
      "id": "C06-Q4",
      "question": "הקובץ בינארי והוא מכיל רשומות מטיפוס `rec` ברצף. איזו שורה מציבה את הסמן בתחילת הרשומה שמספרה `i` (הראשונה היא 0) ?",
      "options": [
        {
          "id": "a",
          "value": "`fseek(f, i * sizeof(rec), SEEK_SET);`"
        },
        {
          "id": "b",
          "value": "`fseek(f, (i + 1) * sizeof(rec), SEEK_SET);`"
        },
        {
          "id": "c",
          "value": "`fseek(f, i + sizeof(rec), SEEK_SET);`"
        },
        {
          "id": "d",
          "value": "`fseek(f, i, SEEK_SET);`"
        }
      ],
      "correctId": "a",
      "explanation": "לפני רשומה `i` יש `i` רשומות, שכל אחת מהן `sizeof(rec)` בתים, ולכן ההיסט הוא `i * sizeof(rec)` (נבדק עם clang, רשומה 2 מתוך ארבע נקראה נכון). עם `i + 1` מגיעים לרשומה הבאה. עם חיבור או עם `i` בלבד מגיעים לאמצע רשומה.",
      "recap": "רשומה `i` נמצאת בהיסט `i * sizeof(rec)`."
    },
    {
      "id": "C06-Q5",
      "step": {
        "type": "text",
        "accept": [
          "D"
        ],
        "normalize": "none",
        "prompt": "הקובץ (בינארי) מכיל `ABCDEFGH`. איזה תו יודפס?\n```c\nfgetc(f);\nfgetc(f);\nfseek(f, 1, SEEK_CUR);\nputchar(fgetc(f));\n```",
        "explain": "אחרי שתי קריאות הסמן במקום 2. `SEEK_CUR` עם 1 מזיז אותו למקום 3, והתו שם הוא `D`."
      },
      "recap": "`SEEK_CUR` זז יחסית למקום הנוכחי."
    },
    {
      "id": "C06-Q6",
      "step": {
        "type": "findbug",
        "code": true,
        "prompt": "הקוד אמור לטעון את כל הרשומות של קובץ בינארי למערך, אבל כל איברי המערך נשארים אפסים. איזו שורה שגויה?",
        "lines": [
          "FILE *f = fopen(name, \"rb\");",
          "rec a, *arr;",
          "int n = 0, i = 0;",
          "while (fread(&a, sizeof(a), 1, f) == 1)",
          "    n++;",
          "fseek(f, 0, SEEK_END);",
          "arr = (rec *)calloc(n, sizeof(rec));",
          "while (fread(&a, sizeof(a), 1, f) == 1)",
          "    arr[i++] = a;"
        ],
        "bugIndex": 5,
        "explain": "אחרי המעבר הראשון הסמן בסוף הקובץ. כדי שהמעבר השני יקרא את הרשומות צריך להחזיר אותו להתחלה עם `rewind(f)`. הקפיצה לסוף משאירה אותו שם והמעבר השני לא קורא כלום."
      },
      "recap": "בין שני מעברים על הקובץ מחזירים את הסמן להתחלה עם `rewind`."
    }
  ]
});
