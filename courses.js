window.COURSES = {
 "c_traps": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🔤",
    "title": "תווים הם מספרים",
    "goal": "אחרי השלב הזה אפשר לחשב מה מדפיסה printf כשמעבירים לה תו, ולהבדיל בין התו '0' לבין המספר 0.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>ב-C תו בגרשיים בודדים, כמו <code>'a'</code>, הוא <b>מספר שלם</b>: קוד ה-ASCII שלו. כמה קודים שכדאי לזכור:</p>\n    <table><thead><tr><th>תו</th><th>קוד</th></tr></thead>\n    <tbody><tr><td><code>'\\0'</code></td><td>0</td></tr><tr><td><code>'0'</code></td><td>48</td></tr><tr><td><code>'A'</code></td><td>65</td></tr><tr><td><code>'a'</code></td><td>97</td></tr></tbody></table>\n    <p>הספרות <code>'0'</code> עד <code>'9'</code> רצופות, והאותיות הגדולות והקטנות רצופות גם הן. לכן <code>'a' + 1</code> הוא 98, ו-<code>c - '0'</code> ממיר תו ספרה לערך שלו.</p>\n    <p>ההדפסה תלויה בתבנית: <code>%d</code> מדפיסה את המספר, ו-<code>%c</code> מדפיסה את התו שהמספר מייצג.</p>\n    <pre><code>printf(\"%d\", 'A');      /* 65 */\nprintf(\"%c\", 65);       /* A  */\nprintf(\"%c\", 'A' + 1);  /* B  */</code></pre>\n    <div class=\"lesson-rule\">🔑 התו <code>'0'</code> (קוד 48) אינו המספר 0. רק <code>'\\0'</code> שווה ל-0.</div>\n    <div class=\"lesson-ex\">דוגמה: <code>'7' - '0'</code> הוא <code>55 - 48 = 7</code>, ו-<code>'a' - 'A'</code> הוא <code>97 - 65 = 32</code>.</div>\n    <div class=\"lesson-trap\">⚠️ <code>\"0\"</code> במרכאות כפולות היא מחרוזת, ו-<code>'0'</code> בגרשיים הוא תו. הם לא אותו דבר.</div>"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "question": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", '0');\n```",
      "options": [
       {
        "id": "a",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       },
       {
        "id": "b",
        "value": "`48`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">48</code>"
       },
       {
        "id": "c",
        "value": "`'0'`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">'0'</code>"
       },
       {
        "id": "d",
        "value": "שגיאת הידור",
        "type": "text",
        "html": "שגיאת הידור"
       }
      ],
      "correctId": "b",
      "explanation": "`'0'` הוא תו הספרה אפס, וקוד ה-ASCII שלו הוא 48. התבנית `%d` מדפיסה את הקוד כמספר. התשובה `0` נכונה רק עבור `'\\0'`, והתבנית `%d` אינה מדפיסה גרשיים.",
      "recap": "התו '0' שווה 48, לא 0.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", '0');</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">'0'</code> הוא תו הספרה אפס, וקוד ה-ASCII שלו הוא 48. התבנית <code class=\"tok\" dir=\"ltr\">%d</code> מדפיסה את הקוד כמספר. התשובה <code class=\"tok\" dir=\"ltr\">0</code> נכונה רק עבור <code class=\"tok\" dir=\"ltr\">'\\0'</code>, והתבנית <code class=\"tok\" dir=\"ltr\">%d</code> אינה מדפיסה גרשיים.",
      "recapHtml": "התו '0' שווה 48, לא 0."
     },
     {
      "id": "C01-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", '7' - '0');\n```",
       "answer": 7,
       "tol": 0,
       "explain": "`'7'` הוא 55 ו-`'0'` הוא 48, ולכן ההפרש הוא 7. כך ממירים תו ספרה לערכו.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", '7' - '0');</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">'7'</code> הוא 55 ו-<code class=\"tok\" dir=\"ltr\">'0'</code> הוא 48, ולכן ההפרש הוא 7. כך ממירים תו ספרה לערכו."
      },
      "recap": "c - '0' נותן את ערך הספרה.",
      "recapHtml": "c - '0' נותן את ערך הספרה."
     },
     {
      "id": "C01-Q3",
      "question": "מה מדפיס הקוד?\n```c\nprintf(\"%c%c%c\", 'a' + 1, 'A' + 2, '0' + 3);\n```",
      "options": [
       {
        "id": "a",
        "value": "`bC3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">bC3</code>"
       },
       {
        "id": "b",
        "value": "`98 67 51`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">98 67 51</code>"
       },
       {
        "id": "c",
        "value": "`aA0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">aA0</code>"
       },
       {
        "id": "d",
        "value": "`b C 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">b C 3</code>"
       }
      ],
      "correctId": "a",
      "explanation": "התבנית `%c` מדפיסה את התו שמייצג הקוד: 98 הוא `b`, 67 הוא `C`, ו-51 הוא `3`. התשובה `98 67 51` הייתה נכונה עם `%d`, ובתבנית אין רווחים ולכן אין רווחים בפלט.",
      "recap": "%c מדפיסה תו, %d מדפיסה את הקוד.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%c%c%c\", 'a' + 1, 'A' + 2, '0' + 3);</code></pre>",
      "explanationHtml": "התבנית <code class=\"tok\" dir=\"ltr\">%c</code> מדפיסה את התו שמייצג הקוד: 98 הוא <code class=\"tok\" dir=\"ltr\">b</code>, 67 הוא <code class=\"tok\" dir=\"ltr\">C</code>, ו-51 הוא <code class=\"tok\" dir=\"ltr\">3</code>. התשובה <code class=\"tok\" dir=\"ltr\">98 67 51</code> הייתה נכונה עם <code class=\"tok\" dir=\"ltr\">%d</code>, ובתבנית אין רווחים ולכן אין רווחים בפלט.",
      "recapHtml": "%c מדפיסה תו, %d מדפיסה את הקוד."
     },
     {
      "id": "C01-Q4",
      "question": "איזו מההוראות הבאות **לא** מדפיסה 0?",
      "options": [
       {
        "id": "a",
        "value": "`printf(\"%d\", '\\0');`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">printf(\"%d\", '\\0');</code>"
       },
       {
        "id": "b",
        "value": "`printf(\"%d\", '0');`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">printf(\"%d\", '0');</code>"
       },
       {
        "id": "c",
        "value": "`printf(\"%d\", '0' - '0');`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">printf(\"%d\", '0' - '0');</code>"
       },
       {
        "id": "d",
        "value": "`printf(\"%d\", 'a' - 'a');`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">printf(\"%d\", 'a' - 'a');</code>"
       }
      ],
      "correctId": "b",
      "explanation": "`'0'` שווה 48. `'\\0'` שווה 0, וההפרש של תו עם עצמו (`'0' - '0'` או `'a' - 'a'`) הוא 0.",
      "recap": "רק '\\0' הוא אפס; '0' הוא 48.",
      "questionHtml": "איזו מההוראות הבאות <strong>לא</strong> מדפיסה 0?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">'0'</code> שווה 48. <code class=\"tok\" dir=\"ltr\">'\\0'</code> שווה 0, וההפרש של תו עם עצמו (<code class=\"tok\" dir=\"ltr\">'0' - '0'</code> או <code class=\"tok\" dir=\"ltr\">'a' - 'a'</code>) הוא 0.",
      "recapHtml": "רק '\\0' הוא אפס; '0' הוא 48."
     },
     {
      "id": "C01-Q5",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nchar c = 'x';\nc = c - 'a' + 'A';\nprintf(\"%d\", c);\n```",
       "answer": 88,
       "tol": 0,
       "explain": "`'x'` הוא 120, `'a'` הוא 97 ו-`'A'` הוא 65. מקבלים $120 - 97 + 65 = 88$, וזה קוד התו `'X'`. כך ממירים אות קטנה לגדולה.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char c = 'x';\nc = c - 'a' + 'A';\nprintf(\"%d\", c);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">'x'</code> הוא 120, <code class=\"tok\" dir=\"ltr\">'a'</code> הוא 97 ו-<code class=\"tok\" dir=\"ltr\">'A'</code> הוא 65. מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>120</mn><mo>−</mo><mn>97</mn><mo>+</mo><mn>65</mn><mo>=</mo><mn>88</mn></mrow><annotation encoding=\"application/x-tex\">120 - 97 + 65 = 88</annotation></semantics></math></span>, וזה קוד התו <code class=\"tok\" dir=\"ltr\">'X'</code>. כך ממירים אות קטנה לגדולה."
      },
      "recap": "c - 'a' + 'A' הופך אות קטנה לגדולה.",
      "recapHtml": "c - 'a' + 'A' הופך אות קטנה לגדולה."
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "➗",
    "title": "חילוק שלם ושארית",
    "goal": "אחרי השלב הזה אפשר לחשב חילוק ושארית של מספרים שלמים (גם שליליים), ולהבחין מתי החילוק הוא שלם ומתי ממשי.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>כששני האופרנדים של <code>/</code> הם מספרים שלמים, התוצאה היא מספר שלם: החלק השלם של המנה, <b>בלי עיגול</b>. ב-C הביטוי 5 / 2 הוא 2, לא 2.5.</p>\n    <ul>\n      <li><code>7 / 2</code> הוא 3 ו-<code>-7 / 2</code> הוא -3 (החילוק קוטם לכיוון אפס).</li>\n      <li><code>%</code> נותן את השארית, והיא מקבלת את סימן המחולק: <code>7 % 2</code> הוא 1 ו-<code>-7 % 2</code> הוא -1.</li>\n      <li>החילוק ממשי רק אם לפחות אופרנד אחד הוא <code>double</code>: <code>5 / 2.0</code> הוא 2.5.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 סדר החישוב קובע. ב-<code>1 / 2 + 1 / 2.0</code> החילוק הראשון שלם (0) והשני ממשי (0.5).</div>\n    <div class=\"lesson-ex\">דוגמה: <code>10 / 4 * 4</code> מחושב משמאל לימין: <code>(10 / 4) * 4 = 2 * 4 = 8</code>, ולא 10.</div>\n    <div class=\"lesson-trap\">⚠️ המרה שמתבצעת אחרי חילוק שלם לא מחזירה את מה שאבד: <code>(double)(7 / 2)</code> הוא 3.0, ואילו <code>(double)7 / 2</code> הוא 3.5.</div>\n    <h3>לולאה שנעצרת באפס</h3>\n    <p>בלולאה <code>for (i = 0; s[i]; i++)</code> התנאי הוא הערך <code>s[i]</code> עצמו. הלולאה נעצרת באיבר הראשון ששווה 0, והאיברים שאחריו לא נקראים. כך גם בחילוק שלם: <code>5 / 5 / 5</code> הוא <code>1 / 5</code>, כלומר 0.</p>"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "question": "מה מדפיס הקוד?\n```c\nprintf(\"%d %d\", 7 / 2, -7 / 2);\n```",
      "options": [
       {
        "id": "a",
        "value": "`3 -3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 -3</code>"
       },
       {
        "id": "b",
        "value": "`3.5 -3.5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3.5 -3.5</code>"
       },
       {
        "id": "c",
        "value": "`3 -4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 -4</code>"
       },
       {
        "id": "d",
        "value": "`4 -4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 -4</code>"
       }
      ],
      "correctId": "a",
      "explanation": "חילוק שלם קוטם לכיוון אפס: 7/2 הוא 3 ו-(-7)/2 הוא -3. התשובה `-4` מניחה עיגול כלפי מטה, ו-`3.5` מניחה חילוק ממשי. אף אחד מהם אינו נכון ב-C.",
      "recap": "חילוק שלם קוטם לכיוון אפס.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d %d\", 7 / 2, -7 / 2);</code></pre>",
      "explanationHtml": "חילוק שלם קוטם לכיוון אפס: 7/2 הוא 3 ו-(-7)/2 הוא -3. התשובה <code class=\"tok\" dir=\"ltr\">-4</code> מניחה עיגול כלפי מטה, ו-<code class=\"tok\" dir=\"ltr\">3.5</code> מניחה חילוק ממשי. אף אחד מהם אינו נכון ב-C.",
      "recapHtml": "חילוק שלם קוטם לכיוון אפס."
     },
     {
      "id": "C02-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", -7 % 3);\n```",
       "answer": -1,
       "tol": 0,
       "explain": "$-7 = (-2)\\cdot 3 + (-1)$. החילוק קוטם ל-(-2) והשארית מקבלת את סימן המחולק, ולכן התוצאה היא -1.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", -7 % 3);</code></pre>",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>−</mo><mn>7</mn><mo>=</mo><mo stretchy=\"false\">(</mo><mo>−</mo><mn>2</mn><mo stretchy=\"false\">)</mo><mo>⋅</mo><mn>3</mn><mo>+</mo><mo stretchy=\"false\">(</mo><mo>−</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">-7 = (-2)\\cdot 3 + (-1)</annotation></semantics></math></span>. החילוק קוטם ל-(-2) והשארית מקבלת את סימן המחולק, ולכן התוצאה היא -1."
      },
      "recap": "לשארית יש סימן של המחולק.",
      "recapHtml": "לשארית יש סימן של המחולק."
     },
     {
      "id": "C02-Q3",
      "question": "מה מדפיס הקוד?\n```c\ndouble x = 5 / 2;\nprintf(\"%.1f\", x);\n```",
      "options": [
       {
        "id": "a",
        "value": "`2.5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2.5</code>"
       },
       {
        "id": "b",
        "value": "`2.0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2.0</code>"
       },
       {
        "id": "c",
        "value": "`3.0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3.0</code>"
       },
       {
        "id": "d",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       }
      ],
      "correctId": "b",
      "explanation": "הביטוי `5 / 2` מחושב קודם, והוא חילוק שלם ששווה 2. רק אחר כך הערך 2 מומר ל-`double`. ההשמה ל-`double` לא הופכת את החילוק לממשי, ולכן התוצאה 2.0 ולא 2.5. התבנית `%.1f` מדפיסה ספרה אחת אחרי הנקודה, ולכן לא `2`.",
      "recap": "ההשמה ל-double באה אחרי החילוק השלם.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>double x = 5 / 2;\nprintf(\"%.1f\", x);</code></pre>",
      "explanationHtml": "הביטוי <code class=\"tok\" dir=\"ltr\">5 / 2</code> מחושב קודם, והוא חילוק שלם ששווה 2. רק אחר כך הערך 2 מומר ל-<code class=\"tok\" dir=\"ltr\">double</code>. ההשמה ל-<code class=\"tok\" dir=\"ltr\">double</code> לא הופכת את החילוק לממשי, ולכן התוצאה 2.0 ולא 2.5. התבנית <code class=\"tok\" dir=\"ltr\">%.1f</code> מדפיסה ספרה אחת אחרי הנקודה, ולכן לא <code class=\"tok\" dir=\"ltr\">2</code>.",
      "recapHtml": "ההשמה ל-double באה אחרי החילוק השלם."
     },
     {
      "id": "C02-Q4",
      "question": "מה מדפיס הקוד?\n```c\ndouble y = 1 / 2 + 1 / 2.0;\nprintf(\"%.1f\", y);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1.0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1.0</code>"
       },
       {
        "id": "b",
        "value": "`0.0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0.0</code>"
       },
       {
        "id": "c",
        "value": "`0.5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0.5</code>"
       },
       {
        "id": "d",
        "value": "`1.5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1.5</code>"
       }
      ],
      "correctId": "c",
      "explanation": "`1 / 2` הוא חילוק שלם ושווה 0, ו-`1 / 2.0` הוא חילוק ממשי ושווה 0.5. הסכום הוא 0.5. התשובה 1.0 מניחה ששני החילוקים ממשיים.",
      "recap": "כל חילוק נבחן בנפרד: שלם או ממשי.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>double y = 1 / 2 + 1 / 2.0;\nprintf(\"%.1f\", y);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">1 / 2</code> הוא חילוק שלם ושווה 0, ו-<code class=\"tok\" dir=\"ltr\">1 / 2.0</code> הוא חילוק ממשי ושווה 0.5. הסכום הוא 0.5. התשובה 1.0 מניחה ששני החילוקים ממשיים.",
      "recapHtml": "כל חילוק נבחן בנפרד: שלם או ממשי."
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 10 / 4 * 4);\n```",
       "answer": 8,
       "tol": 0,
       "explain": "האופרטורים `/` ו-`*` באותה רמה ומחושבים משמאל לימין: $(10/4)\\cdot 4 = 2\\cdot 4 = 8$.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", 10 / 4 * 4);</code></pre>",
       "explainHtml": "האופרטורים <code class=\"tok\" dir=\"ltr\">/</code> ו-<code class=\"tok\" dir=\"ltr\">*</code> באותה רמה ומחושבים משמאל לימין: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mn>10</mn><mi mathvariant=\"normal\">/</mi><mn>4</mn><mo stretchy=\"false\">)</mo><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>2</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>8</mn></mrow><annotation encoding=\"application/x-tex\">(10/4)\\cdot 4 = 2\\cdot 4 = 8</annotation></semantics></math></span>."
      },
      "recap": "משמאל לימין: קודם החילוק השלם.",
      "recapHtml": "משמאל לימין: קודם החילוק השלם."
     },
     {
      "id": "C02-Q6",
      "question": "מה מדפיס הקוד?\n```c\nint s[] = {5, 5 / 5, 5 / 5 / 5, 7};\nint i;\nfor (i = 0; s[i]; i++)\n    printf(\"%d\", s[i]);\n```",
      "options": [
       {
        "id": "a",
        "value": "`5107`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5107</code>"
       },
       {
        "id": "b",
        "value": "`51`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">51</code>"
       },
       {
        "id": "c",
        "value": "`517`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">517</code>"
       },
       {
        "id": "d",
        "value": "`5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5</code>"
       }
      ],
      "correctId": "b",
      "explanation": "האיברים הם 5, 1 (שווה ל-5/5), 0 (שווה ל-1/5 בחילוק שלם) ו-7. הלולאה נעצרת באיבר השלישי כי הוא 0, ולכן מודפסים רק 5 ו-1: `51`. התשובות עם 7 מניחות שהלולאה ממשיכה אחרי האפס.",
      "recap": "הלולאה נעצרת באיבר הראשון ששווה 0.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int s[] = {5, 5 / 5, 5 / 5 / 5, 7};\nint i;\nfor (i = 0; s[i]; i++)\n    printf(\"%d\", s[i]);</code></pre>",
      "explanationHtml": "האיברים הם 5, 1 (שווה ל-5/5), 0 (שווה ל-1/5 בחילוק שלם) ו-7. הלולאה נעצרת באיבר השלישי כי הוא 0, ולכן מודפסים רק 5 ו-1: <code class=\"tok\" dir=\"ltr\">51</code>. התשובות עם 7 מניחות שהלולאה ממשיכה אחרי האפס.",
      "recapHtml": "הלולאה נעצרת באיבר הראשון ששווה 0."
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "⚖️",
    "title": "קדימויות והשמה",
    "goal": "אחרי השלב הזה אפשר להבחין בין = ל-==, בין פעולות סיביות ללוגיות, ולחשב ביטויים שבהם סדר החישוב מפתיע.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>סדר החישוב נקבע לפי <b>קדימות</b> האופרטורים. מהחזק לחלש, בקצרה:</p>\n    <table><thead><tr><th>רמה</th><th>אופרטורים</th></tr></thead>\n    <tbody>\n    <tr><td>1</td><td><code>!</code> ו-<code>++</code> ו-<code>--</code> (יחידיים)</td></tr>\n    <tr><td>2</td><td><code>*</code> <code>/</code> <code>%</code>, אחר כך <code>+</code> <code>-</code></td></tr>\n    <tr><td>3</td><td><code>&lt;&lt;</code> <code>&gt;&gt;</code></td></tr>\n    <tr><td>4</td><td><code>&lt;</code> <code>&gt;</code> <code>&lt;=</code> <code>&gt;=</code>, אחר כך <code>==</code> <code>!=</code></td></tr>\n    <tr><td>5</td><td><code>&amp;</code>, אחר כך <code>^</code>, אחר כך <code>|</code></td></tr>\n    <tr><td>6</td><td><code>&amp;&amp;</code>, אחר כך <code>||</code></td></tr>\n    <tr><td>7</td><td><code>=</code> (הכי חלש)</td></tr>\n    </tbody></table>\n    <ul>\n      <li><code>=</code> היא השמה והערך שלה הוא הערך שהושם. <code>==</code> היא השוואה.</li>\n      <li>השוואה (<code>==</code>) חזקה מ-<code>&amp;</code>, ולכן <code>4 &amp; 3 == 3</code> הוא <code>4 &amp; (3 == 3)</code>, כלומר <code>4 &amp; 1</code>, כלומר 0.</li>\n      <li><code>^</code> היא XOR של סיביות ולא חזקה: <code>3 ^ 2</code> הוא 1. ו-<code>1 &lt;&lt; k</code> הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mn>2</mn><mi>k</mi></msup></mrow><annotation encoding=\"application/x-tex\">2^k</annotation></semantics></math></span>.</li>\n      <li>השוואות משורשרות מחושבות משמאל לימין, וכל השוואה נותנת 0 או 1: <code>5 &gt; 3 &gt; 1</code> הוא <code>1 &gt; 1</code>, כלומר 0.</li>\n      <li><code>&amp;&amp;</code> ו-<code>||</code> מחשבים משמאל לימין ו<b>עוצרים</b> ברגע שהתוצאה ידועה: הצד הימני של <code>&amp;&amp;</code> לא מחושב אם הצד השמאלי שקרי.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 בספק, שמים סוגריים. ובתנאי <code>if</code> כותבים <code>==</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: <code>2 + 3 * 4 % 5</code>. קודם <code>3 * 4 = 12</code>, אחר כך <code>12 % 5 = 2</code> (אותה רמה, משמאל לימין), ולבסוף <code>2 + 2 = 4</code>.</div>\n    <div class=\"lesson-trap\">⚠️ <code>if (x = 0)</code> מבצעת השמה, והערך של התנאי הוא 0, כלומר שקר. הקוד מתקמפל, והמשתנה כבר איבד את ערכו.</div>"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "question": "מה מדפיס הקוד?\n```c\nint x = 5;\nif (x = 0)\n    printf(\"A\");\nelse\n    printf(\"B\");\nprintf(\"%d\", x);\n```",
      "options": [
       {
        "id": "a",
        "value": "`B0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">B0</code>"
       },
       {
        "id": "b",
        "value": "`A0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">A0</code>"
       },
       {
        "id": "c",
        "value": "`B5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">B5</code>"
       },
       {
        "id": "d",
        "value": "`A5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">A5</code>"
       }
      ],
      "correctId": "a",
      "explanation": "התנאי הוא השמה: `x` מקבל 0 וערך הביטוי הוא 0, כלומר שקר, ולכן מדפיסים `B`. אחרי ההשמה `x` שווה 0 ולא 5. התשובות `A` מניחות שהתנאי אמת, והתשובות עם 5 מניחות ש-`x` לא השתנה.",
      "recap": "if (x = 0) משנה את x והתנאי שקרי.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x = 5;\nif (x = 0)\n    printf(\"A\");\nelse\n    printf(\"B\");\nprintf(\"%d\", x);</code></pre>",
      "explanationHtml": "התנאי הוא השמה: <code class=\"tok\" dir=\"ltr\">x</code> מקבל 0 וערך הביטוי הוא 0, כלומר שקר, ולכן מדפיסים <code class=\"tok\" dir=\"ltr\">B</code>. אחרי ההשמה <code class=\"tok\" dir=\"ltr\">x</code> שווה 0 ולא 5. התשובות <code class=\"tok\" dir=\"ltr\">A</code> מניחות שהתנאי אמת, והתשובות עם 5 מניחות ש-<code class=\"tok\" dir=\"ltr\">x</code> לא השתנה.",
      "recapHtml": "if (x = 0) משנה את x והתנאי שקרי."
     },
     {
      "id": "C03-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 4 & 3 == 3);\n```",
       "answer": 0,
       "tol": 0,
       "explain": "`==` חזק מ-`&`, ולכן הביטוי הוא `4 & (3 == 3)`, כלומר `4 & 1`. ב-4 הסיבית הנמוכה כבויה, ולכן התוצאה 0. אילו `&` היה קודם, הייתה התוצאה `(4 & 3) == 3` כלומר 0 == 3, וגם היא 0, אבל מסיבה אחרת.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", 4 &amp; 3 == 3);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">==</code> חזק מ-<code class=\"tok\" dir=\"ltr\">&amp;</code>, ולכן הביטוי הוא <code class=\"tok\" dir=\"ltr\">4 &amp; (3 == 3)</code>, כלומר <code class=\"tok\" dir=\"ltr\">4 &amp; 1</code>. ב-4 הסיבית הנמוכה כבויה, ולכן התוצאה 0. אילו <code class=\"tok\" dir=\"ltr\">&amp;</code> היה קודם, הייתה התוצאה <code class=\"tok\" dir=\"ltr\">(4 &amp; 3) == 3</code> כלומר 0 == 3, וגם היא 0, אבל מסיבה אחרת."
      },
      "recap": "השוואה חזקה מ-& ו-|.",
      "recapHtml": "השוואה חזקה מ-&amp; ו-|."
     },
     {
      "id": "C03-Q3",
      "question": "מה מדפיס הקוד?\n```c\nprintf(\"%d %d\", 3 ^ 2, 1 << 4);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1 16`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 16</code>"
       },
       {
        "id": "b",
        "value": "`9 16`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 16</code>"
       },
       {
        "id": "c",
        "value": "`1 4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 4</code>"
       },
       {
        "id": "d",
        "value": "`9 4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 4</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`^` היא XOR של סיביות: `011 ^ 010 = 001`, כלומר 1, ולא העלאה בחזקה (9). `1 << 4` מזיז את הסיבית ארבע מקומות ונותן $2^4 = 16$, ולא 4.",
      "recap": "^ היא XOR, לא חזקה.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d %d\", 3 ^ 2, 1 &lt;&lt; 4);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">^</code> היא XOR של סיביות: <code class=\"tok\" dir=\"ltr\">011 ^ 010 = 001</code>, כלומר 1, ולא העלאה בחזקה (9). <code class=\"tok\" dir=\"ltr\">1 &lt;&lt; 4</code> מזיז את הסיבית ארבע מקומות ונותן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><msup><mn>2</mn><mn>4</mn></msup><mo>=</mo><mn>16</mn></mrow><annotation encoding=\"application/x-tex\">2^4 = 16</annotation></semantics></math></span>, ולא 4.",
      "recapHtml": "^ היא XOR, לא חזקה."
     },
     {
      "id": "C03-Q4",
      "question": "מה מדפיס הקוד?\n```c\nint i = 0, j = 0;\nif (i++ && j++)\n    ;\nprintf(\"%d %d\", i, j);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1 0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 0</code>"
       },
       {
        "id": "b",
        "value": "`1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 1</code>"
       },
       {
        "id": "c",
        "value": "`0 0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 0</code>"
       },
       {
        "id": "d",
        "value": "`0 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`i++` נותן את הערך הישן 0 (שקר) ו-`i` נעשה 1. מכיוון שהצד השמאלי של `&&` שקרי, הצד הימני `j++` לא מחושב, ולכן `j` נשאר 0.",
      "recap": "&& לא מחשב את הצד הימני אחרי שמאל שקרי.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int i = 0, j = 0;\nif (i++ &amp;&amp; j++)\n    ;\nprintf(\"%d %d\", i, j);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">i++</code> נותן את הערך הישן 0 (שקר) ו-<code class=\"tok\" dir=\"ltr\">i</code> נעשה 1. מכיוון שהצד השמאלי של <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> שקרי, הצד הימני <code class=\"tok\" dir=\"ltr\">j++</code> לא מחושב, ולכן <code class=\"tok\" dir=\"ltr\">j</code> נשאר 0.",
      "recapHtml": "&amp;&amp; לא מחשב את הצד הימני אחרי שמאל שקרי."
     },
     {
      "id": "C03-Q5",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 5 > 3 > 1);\n```",
       "answer": 0,
       "tol": 0,
       "explain": "מחשבים משמאל לימין: `5 > 3` נותן 1, ואז `1 > 1` שקרי ונותן 0. הביטוי אינו בודק ש-3 גדול מ-1.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", 5 &gt; 3 &gt; 1);</code></pre>",
       "explainHtml": "מחשבים משמאל לימין: <code class=\"tok\" dir=\"ltr\">5 &gt; 3</code> נותן 1, ואז <code class=\"tok\" dir=\"ltr\">1 &gt; 1</code> שקרי ונותן 0. הביטוי אינו בודק ש-3 גדול מ-1."
      },
      "recap": "השוואות משורשרות נותנות 0 או 1 בכל שלב.",
      "recapHtml": "השוואות משורשרות נותנות 0 או 1 בכל שלב."
     },
     {
      "id": "C03-Q6",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 2 + 3 * 4 % 5);\n```",
       "answer": 4,
       "tol": 0,
       "explain": "`3 * 4` הוא 12, אחר כך `12 % 5` הוא 2, ולבסוף `2 + 2` הוא 4. הכפל והשארית באותה רמה וחזקים מהחיבור.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", 2 + 3 * 4 % 5);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">3 * 4</code> הוא 12, אחר כך <code class=\"tok\" dir=\"ltr\">12 % 5</code> הוא 2, ולבסוף <code class=\"tok\" dir=\"ltr\">2 + 2</code> הוא 4. הכפל והשארית באותה רמה וחזקים מהחיבור."
      },
      "recap": "כפל, חילוק ושארית לפני חיבור וחיסור.",
      "recapHtml": "כפל, חילוק ושארית לפני חיבור וחיסור."
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "📏",
    "title": "sizeof",
    "goal": "אחרי השלב הזה אפשר לחשב sizeof של מערכים ושל מחרוזות קבועות, ולהבחין בינו לבין strlen.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p><code>sizeof</code> הוא אופרטור (לא פונקציה) שמחשב בזמן ההידור את גודל הטיפוס או הביטוי בבתים. הערך שלו מטיפוס <code>size_t</code> (מספר שלם חיובי), ולכן מדפיסים אותו עם המרה: <code>printf(\"%d\", (int)sizeof x)</code>.</p>\n    <ul>\n      <li><b>מערך</b>: <code>sizeof a</code> הוא מספר האיברים כפול גודל איבר. לכן <code>sizeof a / sizeof a[0]</code> הוא מספר האיברים.</li>\n      <li><b>מחרוזת קבועה</b>: <code>sizeof \"hello\"</code> הוא 6, כי הגודל כולל את <code>'\\0'</code> הסופי. לעומת זאת <code>strlen(\"hello\")</code> הוא 5, והוא סופר רק עד התו האפס.</li>\n      <li>מערך <code>char s[10] = \"abc\"</code>: ה-<code>sizeof</code> הוא 10 (גודל המערך) וה-<code>strlen</code> הוא 3 (אורך הטקסט).</li>\n      <li><code>sizeof</code> <b>לא מריץ</b> את הביטוי שלו: ב-<code>sizeof(i++)</code> המשתנה <code>i</code> לא משתנה.</li>\n      <li>האינדקס <code>[ ]</code> חזק מ-<code>sizeof</code>, ולכן <code>sizeof \"abc\"[1]</code> הוא הגודל של התו <code>\"abc\"[1]</code>, כלומר 1.</li>\n      <li>התו <code>'a'</code> ב-C הוא מטיפוס <code>int</code>, לכן <code>sizeof('a') == sizeof(int)</code>.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 פרמטר מערך של פונקציה (<code>void f(int a[])</code>) הוא בעצם מצביע. בתוך הפונקציה <code>sizeof a</code> הוא גודל מצביע ולא גודל המערך, ולכן אי אפשר לחשב שם את מספר האיברים כך.</div>\n    <div class=\"lesson-ex\">דוגמה: <code>int a[10]</code>. מקבלים <code>sizeof a / sizeof a[0]</code>, שזה 10 איברים, בלי קשר לגודל של <code>int</code> במחשב.</div>\n    <div class=\"lesson-trap\">⚠️ גודל של מצביע תלוי במחשב (4 או 8 בתים). בשאלה שתלויה בו חייבים לכתוב את ההנחה, ואם אפשר מעדיפים לא להסתמך עליו.</div>"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", (int)sizeof \"hello\");\n```",
       "answer": 6,
       "tol": 0,
       "explain": "המחרוזת הקבועה כוללת 5 תווים ועוד `'\\0'` סופי, ולכן הגודל הוא 6. הערך 5 היה `strlen`.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", (int)sizeof \"hello\");</code></pre>",
       "explainHtml": "המחרוזת הקבועה כוללת 5 תווים ועוד <code class=\"tok\" dir=\"ltr\">'\\0'</code> סופי, ולכן הגודל הוא 6. הערך 5 היה <code class=\"tok\" dir=\"ltr\">strlen</code>."
      },
      "recap": "sizeof של מחרוזת כולל את '\\0'.",
      "recapHtml": "sizeof של מחרוזת כולל את '\\0'."
     },
     {
      "id": "C04-Q2",
      "question": "מה מדפיס הקוד?\n```c\nchar s[10] = \"abc\";\nprintf(\"%d %d\", (int)sizeof s, (int)strlen(s));\n```",
      "options": [
       {
        "id": "a",
        "value": "`10 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">10 3</code>"
       },
       {
        "id": "b",
        "value": "`4 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 3</code>"
       },
       {
        "id": "c",
        "value": "`3 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 3</code>"
       },
       {
        "id": "d",
        "value": "`10 10`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">10 10</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`sizeof s` הוא גודל המערך כולו, 10 בתים. `strlen(s)` סופר עד התו האפס הראשון, כלומר 3. הערך 4 היה נכון אילו המערך הוגדר `char s[] = \"abc\"`.",
      "recap": "sizeof הוא גודל המערך; strlen הוא אורך הטקסט.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char s[10] = \"abc\";\nprintf(\"%d %d\", (int)sizeof s, (int)strlen(s));</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">sizeof s</code> הוא גודל המערך כולו, 10 בתים. <code class=\"tok\" dir=\"ltr\">strlen(s)</code> סופר עד התו האפס הראשון, כלומר 3. הערך 4 היה נכון אילו המערך הוגדר <code class=\"tok\" dir=\"ltr\">char s[] = \"abc\"</code>.",
      "recapHtml": "sizeof הוא גודל המערך; strlen הוא אורך הטקסט."
     },
     {
      "id": "C04-Q3",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד (המספר שמודפס אינו תלוי בגודל של `int`)?\n```c\nint a[10];\nprintf(\"%d\", (int)(sizeof a / sizeof a[0]));\n```",
       "answer": 10,
       "tol": 0,
       "explain": "`sizeof a` הוא 10 איברים כפול גודל איבר, ו-`sizeof a[0]` הוא גודל איבר אחד. המנה היא מספר האיברים, 10.",
       "promptHtml": "מה מדפיס הקוד (המספר שמודפס אינו תלוי בגודל של <code class=\"tok\" dir=\"ltr\">int</code>)?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int a[10];\nprintf(\"%d\", (int)(sizeof a / sizeof a[0]));</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">sizeof a</code> הוא 10 איברים כפול גודל איבר, ו-<code class=\"tok\" dir=\"ltr\">sizeof a[0]</code> הוא גודל איבר אחד. המנה היא מספר האיברים, 10."
      },
      "recap": "sizeof a / sizeof a[0] הוא מספר האיברים.",
      "recapHtml": "sizeof a / sizeof a[0] הוא מספר האיברים."
     },
     {
      "id": "C04-Q4",
      "question": "מה מדפיס הקוד?\n```c\nint i = 5;\nint n = sizeof(i++);\nprintf(\"%d\", i);\n```",
      "options": [
       {
        "id": "a",
        "value": "`5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5</code>"
       },
       {
        "id": "b",
        "value": "`6`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">6</code>"
       },
       {
        "id": "c",
        "value": "`4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4</code>"
       },
       {
        "id": "d",
        "value": "`n`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">n</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`sizeof` מחשב רק את הטיפוס של הביטוי ולא מריץ אותו, ולכן `i++` לא מתבצע ו-`i` נשאר 5. התשובה 6 מניחה שההגדלה התבצעה.",
      "recap": "sizeof לא מריץ את הביטוי.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int i = 5;\nint n = sizeof(i++);\nprintf(\"%d\", i);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">sizeof</code> מחשב רק את הטיפוס של הביטוי ולא מריץ אותו, ולכן <code class=\"tok\" dir=\"ltr\">i++</code> לא מתבצע ו-<code class=\"tok\" dir=\"ltr\">i</code> נשאר 5. התשובה 6 מניחה שההגדלה התבצעה.",
      "recapHtml": "sizeof לא מריץ את הביטוי."
     },
     {
      "id": "C04-Q5",
      "question": "הפונקציה:\n```c\nvoid f(int a[])\n{\n    int n = sizeof a / sizeof a[0];\n}\n```\nנקראת עם מערך של 10 איברים. איזו טענה נכונה?",
      "options": [
       {
        "id": "a",
        "value": "`sizeof a` בתוך `f` הוא גודל של מצביע, ולכן `n` אינו מספר האיברים של המערך",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sizeof a</code> בתוך <code class=\"tok\" dir=\"ltr\">f</code> הוא גודל של מצביע, ולכן <code class=\"tok\" dir=\"ltr\">n</code> אינו מספר האיברים של המערך"
       },
       {
        "id": "b",
        "value": "`n` שווה תמיד ל-10",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">n</code> שווה תמיד ל-10"
       },
       {
        "id": "c",
        "value": "הקוד לא מתקמפל כי אי אפשר להשתמש ב-`sizeof` על פרמטר",
        "type": "text",
        "html": "הקוד לא מתקמפל כי אי אפשר להשתמש ב-<code class=\"tok\" dir=\"ltr\">sizeof</code> על פרמטר"
       },
       {
        "id": "d",
        "value": "`sizeof a` הוא גודל כל המערך שהועבר",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sizeof a</code> הוא גודל כל המערך שהועבר"
       }
      ],
      "correctId": "a",
      "explanation": "פרמטר שנכתב כמערך הוא מצביע לאיבר הראשון. לכן `sizeof a` הוא גודל מצביע ו-`n` אינו מספר האיברים. הקוד מתקמפל, ו-`n` לא שווה בהכרח ל-10.",
      "recap": "פרמטר מערך הוא מצביע; sizeof שלו הוא גודל מצביע.",
      "questionHtml": "הפונקציה:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void f(int a[])\n{\n    int n = sizeof a / sizeof a[0];\n}</code></pre>נקראת עם מערך של 10 איברים. איזו טענה נכונה?",
      "explanationHtml": "פרמטר שנכתב כמערך הוא מצביע לאיבר הראשון. לכן <code class=\"tok\" dir=\"ltr\">sizeof a</code> הוא גודל מצביע ו-<code class=\"tok\" dir=\"ltr\">n</code> אינו מספר האיברים. הקוד מתקמפל, ו-<code class=\"tok\" dir=\"ltr\">n</code> לא שווה בהכרח ל-10.",
      "recapHtml": "פרמטר מערך הוא מצביע; sizeof שלו הוא גודל מצביע."
     },
     {
      "id": "C04-Q6",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nprintf(\"%d\", (int)sizeof \"abc\"[1]);\n```",
       "answer": 1,
       "tol": 0,
       "explain": "האינדקס `[ ]` חזק מ-`sizeof`, ולכן מחשבים את הגודל של האיבר `\"abc\"[1]`, שהוא תו מטיפוס `char`. הגודל הוא 1. אילו `sizeof` חל על המחרוזת כולה, התוצאה הייתה 4.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%d\", (int)sizeof \"abc\"[1]);</code></pre>",
       "explainHtml": "האינדקס <code class=\"tok\" dir=\"ltr\">[ ]</code> חזק מ-<code class=\"tok\" dir=\"ltr\">sizeof</code>, ולכן מחשבים את הגודל של האיבר <code class=\"tok\" dir=\"ltr\">\"abc\"[1]</code>, שהוא תו מטיפוס <code class=\"tok\" dir=\"ltr\">char</code>. הגודל הוא 1. אילו <code class=\"tok\" dir=\"ltr\">sizeof</code> חל על המחרוזת כולה, התוצאה הייתה 4."
      },
      "recap": "[ ] חזק מ-sizeof.",
      "recapHtml": "[ ] חזק מ-sizeof."
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "🧵",
    "title": "מחרוזות ומצביעים",
    "goal": "אחרי השלב הזה אפשר להבדיל בין מערך תווים למצביע למחרוזת קבועה, להשוות מחרוזות נכון, ולזהות כתיבה אסורה למחרוזת קבועה.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>מחרוזת היא מערך תווים שנגמר ב-<code>'\\0'</code>.</p>\n    <ul>\n      <li><code>char a[] = \"hi\";</code> יוצר <b>מערך</b> משלו (3 בתים) שאפשר לשנות.</li>\n      <li><code>char *p = \"hi\";</code> יוצר <b>מצביע</b> למחרוזת קבועה. כתיבה דרכו (<code>p[0] = 'H'</code>) היא התנהגות לא מוגדרת לפי תקן C: ייתכן שהתוכנית תקרוס, וייתכן שלא.</li>\n      <li><code>a == b</code> על שני מערכים או מצביעים משווה <b>כתובות</b>, לא תוכן. שני מערכים נפרדים תמיד בכתובות שונות, ולכן <code>==</code> נותן 0 גם כשהתוכן זהה.</li>\n      <li><code>strcmp(a, b)</code> משווה תוכן ומחזירה <b>0 כשהמחרוזות שוות</b>, מספר שלילי כש-<code>a</code> קודמת ל-<code>b</code>, וחיובי אחרת.</li>\n      <li>מחרוזת קבועה היא כתובת של התו הראשון, ולכן <code>\"hello\" + 2</code> היא המחרוזת <code>\"llo\"</code>.</li>\n      <li>איברים שלא אותחלו במפורש במערך שיש לו אתחול מקבלים 0: ב-<code>char s[6] = \"ab\"</code> האיברים <code>s[2]</code> עד <code>s[5]</code> הם <code>'\\0'</code>.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 משווים תוכן עם <code>strcmp</code> והתנאי \"שווה\" הוא <code>strcmp(a, b) == 0</code>, כלומר <code>!strcmp(a, b)</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: אחרי <code>char s[] = \"hello\"; s[2] = '\\0';</code> המחרוזת מסתיימת באינדקס 2, ולכן <code>strlen(s)</code> הוא 2 ו-<code>printf(\"%s\", s)</code> מדפיס <code>he</code>.</div>\n    <div class=\"lesson-trap\">⚠️ <code>if (strcmp(a, b))</code> מתקיים כשהמחרוזות <b>שונות</b>, כי הערך אינו אפס.</div>"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "question": "מה מדפיס הקוד?\n```c\nchar a[] = \"hi\";\nchar b[] = \"hi\";\nprintf(\"%d\", a == b);\n```",
      "options": [
       {
        "id": "a",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       },
       {
        "id": "b",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "c",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       },
       {
        "id": "d",
        "value": "שגיאת הידור",
        "type": "text",
        "html": "שגיאת הידור"
       }
      ],
      "correctId": "a",
      "explanation": "`a == b` משווה את הכתובות של שני מערכים נפרדים, והן תמיד שונות, ולכן התוצאה 0 למרות שהתוכן זהה. להשוואת תוכן משתמשים ב-`strcmp`.",
      "recap": "== על מחרוזות משווה כתובות.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char a[] = \"hi\";\nchar b[] = \"hi\";\nprintf(\"%d\", a == b);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">a == b</code> משווה את הכתובות של שני מערכים נפרדים, והן תמיד שונות, ולכן התוצאה 0 למרות שהתוכן זהה. להשוואת תוכן משתמשים ב-<code class=\"tok\" dir=\"ltr\">strcmp</code>.",
      "recapHtml": "== על מחרוזות משווה כתובות."
     },
     {
      "id": "C05-Q2",
      "question": "מה מדפיס הקוד?\n```c\nprintf(\"%s\", \"hello\" + 2);\n```",
      "options": [
       {
        "id": "a",
        "value": "`llo`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">llo</code>"
       },
       {
        "id": "b",
        "value": "`hello2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">hello2</code>"
       },
       {
        "id": "c",
        "value": "`ello`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">ello</code>"
       },
       {
        "id": "d",
        "value": "`he`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">he</code>"
       }
      ],
      "correctId": "a",
      "explanation": "המחרוזת הקבועה היא כתובת של התו הראשון, והוספת 2 מזיזה לתו באינדקס 2. מודפס כל מה שנשאר עד `'\\0'`: `llo`. התשובה `ello` נכונה להוספת 1.",
      "recap": "s + k מצביע לתו באינדקס k.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>printf(\"%s\", \"hello\" + 2);</code></pre>",
      "explanationHtml": "המחרוזת הקבועה היא כתובת של התו הראשון, והוספת 2 מזיזה לתו באינדקס 2. מודפס כל מה שנשאר עד <code class=\"tok\" dir=\"ltr\">'\\0'</code>: <code class=\"tok\" dir=\"ltr\">llo</code>. התשובה <code class=\"tok\" dir=\"ltr\">ello</code> נכונה להוספת 1.",
      "recapHtml": "s + k מצביע לתו באינדקס k."
     },
     {
      "id": "C05-Q3",
      "question": "מה מדפיס הקוד?\n```c\nchar s[] = \"hello\";\ns[2] = '\\0';\nprintf(\"%d %s\", (int)strlen(s), s);\n```",
      "options": [
       {
        "id": "a",
        "value": "`2 he`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 he</code>"
       },
       {
        "id": "b",
        "value": "`5 hello`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5 hello</code>"
       },
       {
        "id": "c",
        "value": "`3 hel`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 hel</code>"
       },
       {
        "id": "d",
        "value": "`2 llo`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 llo</code>"
       }
      ],
      "correctId": "a",
      "explanation": "הכתיבה של `'\\0'` לאינדקס 2 מסיימת את המחרוזת שם. `strlen` סופר 2 תווים (`he`), ו-`%s` מדפיס עד התו האפס. המערך עצמו עדיין באורך 6, אבל המחרוזת הקצרה יותר.",
      "recap": "'\\0' באמצע מקצר את המחרוזת.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char s[] = \"hello\";\ns[2] = '\\0';\nprintf(\"%d %s\", (int)strlen(s), s);</code></pre>",
      "explanationHtml": "הכתיבה של <code class=\"tok\" dir=\"ltr\">'\\0'</code> לאינדקס 2 מסיימת את המחרוזת שם. <code class=\"tok\" dir=\"ltr\">strlen</code> סופר 2 תווים (<code class=\"tok\" dir=\"ltr\">he</code>), ו-<code class=\"tok\" dir=\"ltr\">%s</code> מדפיס עד התו האפס. המערך עצמו עדיין באורך 6, אבל המחרוזת הקצרה יותר.",
      "recapHtml": "'\\0' באמצע מקצר את המחרוזת."
     },
     {
      "id": "C05-Q4",
      "question": "מה מדפיס הקוד?\n```c\nchar *a = \"x\";\nchar *b = \"x\";\nif (strcmp(a, b))\n    printf(\"diff\");\nelse\n    printf(\"same\");\n```",
      "options": [
       {
        "id": "a",
        "value": "`same`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">same</code>"
       },
       {
        "id": "b",
        "value": "`diff`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">diff</code>"
       },
       {
        "id": "c",
        "value": "`diffsame`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">diffsame</code>"
       },
       {
        "id": "d",
        "value": "אין פלט",
        "type": "text",
        "html": "אין פלט"
       }
      ],
      "correctId": "a",
      "explanation": "`strcmp` מחזירה 0 כשהמחרוזות שוות, ו-0 הוא שקר, ולכן נבחר ה-`else` ומודפס `same`. התנאי `if (strcmp(a, b))` מתקיים רק כשהמחרוזות שונות.",
      "recap": "strcmp מחזירה 0 כשהמחרוזות שוות.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char *a = \"x\";\nchar *b = \"x\";\nif (strcmp(a, b))\n    printf(\"diff\");\nelse\n    printf(\"same\");</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">strcmp</code> מחזירה 0 כשהמחרוזות שוות, ו-0 הוא שקר, ולכן נבחר ה-<code class=\"tok\" dir=\"ltr\">else</code> ומודפס <code class=\"tok\" dir=\"ltr\">same</code>. התנאי <code class=\"tok\" dir=\"ltr\">if (strcmp(a, b))</code> מתקיים רק כשהמחרוזות שונות.",
      "recapHtml": "strcmp מחזירה 0 כשהמחרוזות שוות."
     },
     {
      "id": "C05-Q5",
      "question": "מה קורה בקוד הבא לפי תקן שפת C?\n```c\nchar *s = \"hi\";\ns[0] = 'H';\n```",
      "options": [
       {
        "id": "a",
        "value": "התנהגות לא מוגדרת: כתיבה למחרוזת קבועה",
        "type": "text",
        "html": "התנהגות לא מוגדרת: כתיבה למחרוזת קבועה"
       },
       {
        "id": "b",
        "value": "שגיאת הידור, כי `s` מצביע לקבוע",
        "type": "text",
        "html": "שגיאת הידור, כי <code class=\"tok\" dir=\"ltr\">s</code> מצביע לקבוע"
       },
       {
        "id": "c",
        "value": "`s` הופך להיות `\"Hi\"`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">s</code> הופך להיות <code class=\"tok\" dir=\"ltr\">\"Hi\"</code>"
       },
       {
        "id": "d",
        "value": "נוצר עותק של המחרוזת וה-`H` נכתב אליו",
        "type": "text",
        "html": "נוצר עותק של המחרוזת וה-<code class=\"tok\" dir=\"ltr\">H</code> נכתב אליו"
       }
      ],
      "correctId": "a",
      "explanation": "הקוד מתקמפל, אבל התקן קובע שניסיון לשנות מחרוזת קבועה הוא התנהגות לא מוגדרת. בפועל בדרך כלל הוא קורס בזמן הריצה, אך לא מובטח שיקרה משהו מסוים. כדי שאפשר יהיה לשנות כותבים `char s[] = \"hi\";`.",
      "recap": "כתיבה למחרוזת קבועה: התנהגות לא מוגדרת.",
      "questionHtml": "מה קורה בקוד הבא לפי תקן שפת C?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char *s = \"hi\";\ns[0] = 'H';</code></pre>",
      "explanationHtml": "הקוד מתקמפל, אבל התקן קובע שניסיון לשנות מחרוזת קבועה הוא התנהגות לא מוגדרת. בפועל בדרך כלל הוא קורס בזמן הריצה, אך לא מובטח שיקרה משהו מסוים. כדי שאפשר יהיה לשנות כותבים <code class=\"tok\" dir=\"ltr\">char s[] = \"hi\";</code>.",
      "recapHtml": "כתיבה למחרוזת קבועה: התנהגות לא מוגדרת."
     },
     {
      "id": "C05-Q6",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nchar s[6] = \"ab\";\nprintf(\"%d\", s[4]);\n```",
       "answer": 0,
       "tol": 0,
       "explain": "במערך עם אתחול, האיברים שלא אותחלו במפורש מקבלים 0. לכן `s[4]` הוא `'\\0'` ומודפס 0.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char s[6] = \"ab\";\nprintf(\"%d\", s[4]);</code></pre>",
       "explainHtml": "במערך עם אתחול, האיברים שלא אותחלו במפורש מקבלים 0. לכן <code class=\"tok\" dir=\"ltr\">s[4]</code> הוא <code class=\"tok\" dir=\"ltr\">'\\0'</code> ומודפס 0."
      },
      "recap": "שאר האיברים במערך מאותחל הם 0.",
      "recapHtml": "שאר האיברים במערך מאותחל הם 0."
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "📂",
    "title": "קריאה מקבצים",
    "goal": "אחרי השלב הזה אפשר לחשב מה מדפיסה לולאת קריאה מקובץ, ולזהות את המלכודות של EOF, של feof ושל fgets.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>הפונקציות לקריאה מקובץ מקבלות מצביע <code>FILE *f</code>. כל אחת מהן היא <b>הכללה</b> של פונקציית הקלט הרגילה: היא עובדת על קובץ שנבחר, והרגילה עובדת על המקלדת. <code>fprintf(stdout, ...)</code> שווה ל-<code>printf(...)</code>, <code>fscanf(stdin, ...)</code> שווה ל-<code>scanf(...)</code> ו-<code>fgetc(stdin)</code> שווה ל-<code>getchar()</code>.</p>\n    <ul>\n      <li><code>fgetc(f)</code> מחזירה את התו הבא כמספר, או את הקבוע <code>EOF</code> (בדרך כלל -1) בסוף הקובץ. לכן שומרים את התוצאה ב-<code>int</code>.</li>\n      <li><code>fscanf(f, ...)</code> מחזירה כמה ערכים נקראו בפועל (אפשר גם <code>EOF</code>). כשהקריאה נכשלת היא לא נוגעת במשתנה.</li>\n      <li><code>fgets(st, n, f)</code> קוראת עד <code>n-1</code> תווים, או עד סוף השורה, וכוללת את <code>'\\n'</code> במחרוזת. אם <code>n</code> הוא 2 היא קוראת תו אחד. זה שונה מ-<code>gets</code> שלא מקבלת גודל וזורקת את סוף השורה, ולכן <code>fgets</code> אינה הכללה של <code>gets</code>.</li>\n      <li><code>feof(f)</code> נעשית אמת רק <b>אחרי</b> שניסינו לקרוא מעבר לסוף הקובץ ולא הצלחנו.</li>\n      <li><code>fopen</code> מחזירה <code>NULL</code> אם הפתיחה נכשלה.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 הלולאה הנכונה: <code>int c; while ((c = fgetc(f)) != EOF) ...</code>. הסוגריים סביב ההשמה הכרחיים.</div>\n    <div class=\"lesson-ex\">דוגמה: בקובץ <code>abc</code>, הלולאה שלמעלה מקבלת 97, 98 ו-99 ונעצרת כש-<code>fgetc</code> מחזירה <code>EOF</code>.</div>\n    <div class=\"lesson-trap\">⚠️ <code>while (c = fgetc(f) != EOF)</code> מחושב כ-<code>c = (fgetc(f) != EOF)</code>, כי <code>!=</code> חזק מ-<code>=</code>. המשתנה <code>c</code> הוא 1 בכל תו, והלולאה מדפיסה 1 פעם אחת לכל תו בקובץ.</div>"
    },
    "questions": [
     {
      "id": "C06-Q1",
      "question": "הקובץ `data.txt` מכיל את הטקסט `abc` (בלי שורה חדשה בסוף). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint c;\nwhile ((c = fgetc(f)) != EOF)\n    printf(\"%d \", c);\nfclose(f);\n```",
      "options": [
       {
        "id": "a",
        "value": "`97 98 99`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">97 98 99</code>"
       },
       {
        "id": "b",
        "value": "`a b c`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">a b c</code>"
       },
       {
        "id": "c",
        "value": "`1 1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 1 1</code>"
       },
       {
        "id": "d",
        "value": "`97 98 99 -1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">97 98 99 -1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`fgetc` מחזירה קודים: 97, 98, 99, ואחריהם `EOF` שעוצר את הלולאה בלי להדפיס. התבנית `%d` מדפיסה מספרים ולא תווים. התוצאה `1 1 1` שייכת לגרסה בלי הסוגריים, והערך `-1` לא מודפס כי הוא סיבת העצירה.",
      "recap": "(c = fgetc(f)) != EOF, עם סוגריים.",
      "questionHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">data.txt</code> מכיל את הטקסט <code class=\"tok\" dir=\"ltr\">abc</code> (בלי שורה חדשה בסוף). מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"data.txt\", \"r\");\nint c;\nwhile ((c = fgetc(f)) != EOF)\n    printf(\"%d \", c);\nfclose(f);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fgetc</code> מחזירה קודים: 97, 98, 99, ואחריהם <code class=\"tok\" dir=\"ltr\">EOF</code> שעוצר את הלולאה בלי להדפיס. התבנית <code class=\"tok\" dir=\"ltr\">%d</code> מדפיסה מספרים ולא תווים. התוצאה <code class=\"tok\" dir=\"ltr\">1 1 1</code> שייכת לגרסה בלי הסוגריים, והערך <code class=\"tok\" dir=\"ltr\">-1</code> לא מודפס כי הוא סיבת העצירה.",
      "recapHtml": "(c = fgetc(f)) != EOF, עם סוגריים."
     },
     {
      "id": "C06-Q2",
      "question": "הקובץ `data.txt` מכיל את הטקסט `hi` (בלי שורה חדשה בסוף). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nchar ch;\nwhile (ch = fgetc(f) != EOF)\n    printf(\"%d\", ch);\nfclose(f);\n```",
      "options": [
       {
        "id": "a",
        "value": "`11`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">11</code>"
       },
       {
        "id": "b",
        "value": "`104105`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">104105</code>"
       },
       {
        "id": "c",
        "value": "`hi`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">hi</code>"
       },
       {
        "id": "d",
        "value": "`00`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">00</code>"
       }
      ],
      "correctId": "a",
      "explanation": "בלי סוגריים, `!=` חזק מ-`=`, ולכן `ch` מקבל את תוצאת ההשוואה `fgetc(f) != EOF`, כלומר 1 כל עוד יש תו. שני תווים נותנים `11`. הקודים 104 ו-105 היו מודפסים אילו ההשמה הייתה בסוגריים.",
      "recap": "!= חזק מ-=, ולכן ch הוא 0 או 1.",
      "questionHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">data.txt</code> מכיל את הטקסט <code class=\"tok\" dir=\"ltr\">hi</code> (בלי שורה חדשה בסוף). מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"data.txt\", \"r\");\nchar ch;\nwhile (ch = fgetc(f) != EOF)\n    printf(\"%d\", ch);\nfclose(f);</code></pre>",
      "explanationHtml": "בלי סוגריים, <code class=\"tok\" dir=\"ltr\">!=</code> חזק מ-<code class=\"tok\" dir=\"ltr\">=</code>, ולכן <code class=\"tok\" dir=\"ltr\">ch</code> מקבל את תוצאת ההשוואה <code class=\"tok\" dir=\"ltr\">fgetc(f) != EOF</code>, כלומר 1 כל עוד יש תו. שני תווים נותנים <code class=\"tok\" dir=\"ltr\">11</code>. הקודים 104 ו-105 היו מודפסים אילו ההשמה הייתה בסוגריים.",
      "recapHtml": "!= חזק מ-=, ולכן ch הוא 0 או 1."
     },
     {
      "id": "C06-Q3",
      "question": "הקובץ `data.txt` מכיל `1 2 3` ואחריהם **תו שורה חדשה** (שלושה מספרים בשורה אחת). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &x);\n    printf(\"%d \", x);\n}\nfclose(f);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1 2 3 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3 3</code>"
       },
       {
        "id": "b",
        "value": "`1 2 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3</code>"
       },
       {
        "id": "c",
        "value": "`1 2 3 0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3 0</code>"
       },
       {
        "id": "d",
        "value": "`1 2 3 -1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3 -1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "אחרי קריאת 3, התו שנשאר הוא שורה חדשה, ו-`feof` עדיין שקרית. נכנסים לסיבוב רביעי: `fscanf` נכשלת בגלל סוף הקובץ ולא משנה את `x`, אז מודפס שוב 3, ורק עכשיו `feof` נעשית אמת. זה סיבוב אחד יותר ממספר הערכים.",
      "recap": "feof נעשית אמת רק אחרי קריאה שנכשלה.",
      "questionHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">data.txt</code> מכיל <code class=\"tok\" dir=\"ltr\">1 2 3</code> ואחריהם <strong>תו שורה חדשה</strong> (שלושה מספרים בשורה אחת). מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"data.txt\", \"r\");\nint x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &amp;x);\n    printf(\"%d \", x);\n}\nfclose(f);</code></pre>",
      "explanationHtml": "אחרי קריאת 3, התו שנשאר הוא שורה חדשה, ו-<code class=\"tok\" dir=\"ltr\">feof</code> עדיין שקרית. נכנסים לסיבוב רביעי: <code class=\"tok\" dir=\"ltr\">fscanf</code> נכשלת בגלל סוף הקובץ ולא משנה את <code class=\"tok\" dir=\"ltr\">x</code>, אז מודפס שוב 3, ורק עכשיו <code class=\"tok\" dir=\"ltr\">feof</code> נעשית אמת. זה סיבוב אחד יותר ממספר הערכים.",
      "recapHtml": "feof נעשית אמת רק אחרי קריאה שנכשלה."
     },
     {
      "id": "C06-Q4",
      "step": {
       "type": "numeric",
       "prompt": "הקובץ `data.txt` מכיל שתי שורות: `ab` ואחריה `cd`, וכל שורה נגמרת בתו שורה חדשה. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nchar st[10];\nfgets(st, 10, f);\nprintf(\"%d\", (int)strlen(st));\nfclose(f);\n```",
       "answer": 3,
       "tol": 0,
       "explain": "`fgets` קוראת עד סוף השורה וכוללת את `'\\n'`: המחרוזת היא `ab\\n`, כלומר 3 תווים. `gets` הייתה זורקת את סוף השורה.",
       "promptHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">data.txt</code> מכיל שתי שורות: <code class=\"tok\" dir=\"ltr\">ab</code> ואחריה <code class=\"tok\" dir=\"ltr\">cd</code>, וכל שורה נגמרת בתו שורה חדשה. מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"data.txt\", \"r\");\nchar st[10];\nfgets(st, 10, f);\nprintf(\"%d\", (int)strlen(st));\nfclose(f);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">fgets</code> קוראת עד סוף השורה וכוללת את <code class=\"tok\" dir=\"ltr\">'\\n'</code>: המחרוזת היא <code class=\"tok\" dir=\"ltr\">ab\\n</code>, כלומר 3 תווים. <code class=\"tok\" dir=\"ltr\">gets</code> הייתה זורקת את סוף השורה."
      },
      "recap": "fgets שומרת את '\\n'.",
      "recapHtml": "fgets שומרת את '\\n'."
     },
     {
      "id": "C06-Q5",
      "step": {
       "type": "numeric",
       "prompt": "הקובץ `data.txt` מכיל את הטקסט `5 x`. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint a = 0, b = 0;\nint n = fscanf(f, \"%d %d\", &a, &b);\nprintf(\"%d\", n);\nfclose(f);\n```",
       "answer": 1,
       "tol": 0,
       "explain": "`fscanf` מחזירה את מספר הערכים שנקראו בהצלחה. הראשון (5) נקרא, והשני נכשל כי `x` אינו מספר, ולכן הערך המוחזר הוא 1.",
       "promptHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">data.txt</code> מכיל את הטקסט <code class=\"tok\" dir=\"ltr\">5 x</code>. מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"data.txt\", \"r\");\nint a = 0, b = 0;\nint n = fscanf(f, \"%d %d\", &amp;a, &amp;b);\nprintf(\"%d\", n);\nfclose(f);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">fscanf</code> מחזירה את מספר הערכים שנקראו בהצלחה. הראשון (5) נקרא, והשני נכשל כי <code class=\"tok\" dir=\"ltr\">x</code> אינו מספר, ולכן הערך המוחזר הוא 1."
      },
      "recap": "fscanf מחזירה כמה ערכים נקראו.",
      "recapHtml": "fscanf מחזירה כמה ערכים נקראו."
     },
     {
      "id": "C06-Q6",
      "question": "הקובץ `nope.txt` **לא קיים**. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"nope.txt\", \"r\");\nprintf(\"%d\", f == NULL);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "b",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       },
       {
        "id": "c",
        "value": "הקוד קורס בשורת ה-`fopen`",
        "type": "text",
        "html": "הקוד קורס בשורת ה-<code class=\"tok\" dir=\"ltr\">fopen</code>"
       },
       {
        "id": "d",
        "value": "`-1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">-1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`fopen` על קובץ שלא קיים לקריאה אינה קורסת: היא מחזירה `NULL`. ההשוואה `f == NULL` נותנת 1. התקלה מתרחשת רק אם משתמשים ב-`f` בלי לבדוק אותו.",
      "recap": "fopen מחזירה NULL כשנכשלה.",
      "questionHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">nope.txt</code> <strong>לא קיים</strong>. מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"nope.txt\", \"r\");\nprintf(\"%d\", f == NULL);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fopen</code> על קובץ שלא קיים לקריאה אינה קורסת: היא מחזירה <code class=\"tok\" dir=\"ltr\">NULL</code>. ההשוואה <code class=\"tok\" dir=\"ltr\">f == NULL</code> נותנת 1. התקלה מתרחשת רק אם משתמשים ב-<code class=\"tok\" dir=\"ltr\">f</code> בלי לבדוק אותו.",
      "recapHtml": "fopen מחזירה NULL כשנכשלה."
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "🧠",
    "title": "אתחול והקצאה",
    "goal": "אחרי השלב הזה אפשר לדעת מה הערך ההתחלתי של כל סוג משתנה, ולהבדיל בין malloc, calloc ו-realloc.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>מה הערך ההתחלתי של משתנה שלא אותחל במפורש?</p>\n    <table><thead><tr><th>סוג</th><th>ערך התחלתי</th></tr></thead>\n    <tbody>\n    <tr><td>משתנה גלובלי או <code>static</code></td><td>0</td></tr>\n    <tr><td>משתנה מקומי רגיל</td><td>לא מוגדר (זבל)</td></tr>\n    <tr><td>איברי מערך עם אתחול חלקי (<code>int a[5] = {1, 2}</code>)</td><td>0 לשאר האיברים, גם במערך מקומי</td></tr>\n    <tr><td>זיכרון מ-<code>malloc</code></td><td>לא מוגדר</td></tr>\n    <tr><td>זיכרון מ-<code>calloc</code></td><td>0</td></tr>\n    </tbody></table>\n    <ul>\n      <li><code>malloc(n)</code> מקצה <code>n</code> בתים בלי לאפס. <code>calloc(k, size)</code> מקצה <code>k * size</code> בתים ומאפסת.</li>\n      <li><code>realloc(p, n)</code> משנה את הגודל ושומרת את התוכן הקיים. הכתובת עשויה להשתנות, ולכן משימים את התוצאה ב-<code>p</code>.</li>\n      <li><code>free(p)</code> מותרת רק על כתובת שהוחזרה מ-<code>malloc</code>, <code>calloc</code> או <code>realloc</code> (או על <code>NULL</code>). שחרור מערך רגיל הוא התנהגות לא מוגדרת.</li>\n      <li>משתנה <code>static</code> בתוך פונקציה מאותחל פעם אחת ושומר את ערכו בין קריאות.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 קריאה של ערך שלא אותחל (מקומי או מ-<code>malloc</code>) נותנת ערך לא מוגדר. אין להסתמך עליו, ושאלה טובה לא תבנה עליו תשובה.</div>\n    <div class=\"lesson-ex\">דוגמה: פונקציה עם <code>static int n = 0; n++;</code> שנקראת שלוש פעמים מדפיסה 1, אחר כך 2, אחר כך 3. בלי <code>static</code> היא הייתה מדפיסה 1 שלוש פעמים.</div>\n    <div class=\"lesson-trap\">⚠️ <code>malloc</code> לא מאפסת. זיכרון ש\"נראה\" נקי בהרצה אחת הוא מקרה.</div>"
    },
    "questions": [
     {
      "id": "C07-Q1",
      "question": "מה מדפיס הקוד?\n```c\nint g;\nstatic int s;\nint main(void)\n{\n    int a[5] = {1, 2};\n    printf(\"%d %d %d %d %d\", g, s, a[0], a[2], a[4]);\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`0 0 1 0 0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 0 1 0 0</code>"
       },
       {
        "id": "b",
        "value": "`0 0 1 2 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 0 1 2 2</code>"
       },
       {
        "id": "c",
        "value": "ערכי זבל לא ידועים",
        "type": "text",
        "html": "ערכי זבל לא ידועים"
       },
       {
        "id": "d",
        "value": "`0 0 1 1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 0 1 1 1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "משתנים גלובליים ו-`static` מאותחלים ל-0. במערך עם אתחול חלקי, כל האיברים שלא נכתבו מקבלים 0 (גם במערך מקומי). לכן `a[2]` ו-`a[4]` הם 0, ו-`a[0]` הוא 1.",
      "recap": "גלובלי/static ואתחול חלקי: אפסים.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int g;\nstatic int s;\nint main(void)\n{\n    int a[5] = {1, 2};\n    printf(\"%d %d %d %d %d\", g, s, a[0], a[2], a[4]);\n    return 0;\n}</code></pre>",
      "explanationHtml": "משתנים גלובליים ו-<code class=\"tok\" dir=\"ltr\">static</code> מאותחלים ל-0. במערך עם אתחול חלקי, כל האיברים שלא נכתבו מקבלים 0 (גם במערך מקומי). לכן <code class=\"tok\" dir=\"ltr\">a[2]</code> ו-<code class=\"tok\" dir=\"ltr\">a[4]</code> הם 0, ו-<code class=\"tok\" dir=\"ltr\">a[0]</code> הוא 1.",
      "recapHtml": "גלובלי/static ואתחול חלקי: אפסים."
     },
     {
      "id": "C07-Q2",
      "question": "מה מדפיס הקוד?\n```c\nint *p = (int *)calloc(3, sizeof(int));\nprintf(\"%d%d%d\", p[0], p[1], p[2]);\n```",
      "options": [
       {
        "id": "a",
        "value": "`000`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">000</code>"
       },
       {
        "id": "b",
        "value": "`123`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">123</code>"
       },
       {
        "id": "c",
        "value": "ערכי זבל לא ידועים",
        "type": "text",
        "html": "ערכי זבל לא ידועים"
       },
       {
        "id": "d",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`calloc` מאפסת את הזיכרון שהקצתה, ולכן שלושת האיברים הם 0. אילו הקצינו עם `malloc`, הערכים היו לא מוגדרים.",
      "recap": "calloc מאפסת; malloc לא.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int *p = (int *)calloc(3, sizeof(int));\nprintf(\"%d%d%d\", p[0], p[1], p[2]);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">calloc</code> מאפסת את הזיכרון שהקצתה, ולכן שלושת האיברים הם 0. אילו הקצינו עם <code class=\"tok\" dir=\"ltr\">malloc</code>, הערכים היו לא מוגדרים.",
      "recapHtml": "calloc מאפסת; malloc לא."
     },
     {
      "id": "C07-Q3",
      "question": "מה הערך של `p[0]` מיד אחרי ההקצאה?\n```c\nint *p = (int *)malloc(sizeof(int));\n```",
      "options": [
       {
        "id": "a",
        "value": "לא מוגדר: `malloc` לא מאתחלת",
        "type": "text",
        "html": "לא מוגדר: <code class=\"tok\" dir=\"ltr\">malloc</code> לא מאתחלת"
       },
       {
        "id": "b",
        "value": "תמיד 0",
        "type": "text",
        "html": "תמיד 0"
       },
       {
        "id": "c",
        "value": "תמיד `NULL`",
        "type": "text",
        "html": "תמיד <code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "d",
        "value": "תמיד -1",
        "type": "text",
        "html": "תמיד -1"
       }
      ],
      "correctId": "a",
      "explanation": "`malloc` מחזירה זיכרון בלי לאתחל אותו, ולכן הערך לא מוגדר. הערך 0 מובטח רק ב-`calloc`. `NULL` הוא ערך של מצביע ולא של `int`, ו-`malloc` לא מציבה את -1.",
      "recap": "זיכרון של malloc אינו מאותחל.",
      "questionHtml": "מה הערך של <code class=\"tok\" dir=\"ltr\">p[0]</code> מיד אחרי ההקצאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int *p = (int *)malloc(sizeof(int));</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">malloc</code> מחזירה זיכרון בלי לאתחל אותו, ולכן הערך לא מוגדר. הערך 0 מובטח רק ב-<code class=\"tok\" dir=\"ltr\">calloc</code>. <code class=\"tok\" dir=\"ltr\">NULL</code> הוא ערך של מצביע ולא של <code class=\"tok\" dir=\"ltr\">int</code>, ו-<code class=\"tok\" dir=\"ltr\">malloc</code> לא מציבה את -1.",
      "recapHtml": "זיכרון של malloc אינו מאותחל."
     },
     {
      "id": "C07-Q4",
      "question": "מה מדפיס הקוד?\n```c\nvoid f(void)\n{\n    static int n = 0;\n    n++;\n    printf(\"%d\", n);\n}\nint main(void)\n{\n    f(); f(); f();\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`123`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">123</code>"
       },
       {
        "id": "b",
        "value": "`111`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">111</code>"
       },
       {
        "id": "c",
        "value": "`012`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">012</code>"
       },
       {
        "id": "d",
        "value": "`000`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">000</code>"
       }
      ],
      "correctId": "a",
      "explanation": "המשתנה `static` מאותחל פעם אחת בלבד ושומר את ערכו בין קריאות, ולכן מודפסים 1, 2, 3. התשובה `111` הייתה נכונה אילו `n` היה משתנה מקומי רגיל.",
      "recap": "static מקומי זוכר את ערכו.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void f(void)\n{\n    static int n = 0;\n    n++;\n    printf(\"%d\", n);\n}\nint main(void)\n{\n    f(); f(); f();\n    return 0;\n}</code></pre>",
      "explanationHtml": "המשתנה <code class=\"tok\" dir=\"ltr\">static</code> מאותחל פעם אחת בלבד ושומר את ערכו בין קריאות, ולכן מודפסים 1, 2, 3. התשובה <code class=\"tok\" dir=\"ltr\">111</code> הייתה נכונה אילו <code class=\"tok\" dir=\"ltr\">n</code> היה משתנה מקומי רגיל.",
      "recapHtml": "static מקומי זוכר את ערכו."
     },
     {
      "id": "C07-Q5",
      "question": "מה נכון לגבי הקוד הבא?\n```c\nint a[3];\nfree(a);\n```",
      "options": [
       {
        "id": "a",
        "value": "התנהגות לא מוגדרת: `a` לא הוקצה בהקצאה דינמית",
        "type": "text",
        "html": "התנהגות לא מוגדרת: <code class=\"tok\" dir=\"ltr\">a</code> לא הוקצה בהקצאה דינמית"
       },
       {
        "id": "b",
        "value": "`free` משחררת את המערך ללא בעיה",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">free</code> משחררת את המערך ללא בעיה"
       },
       {
        "id": "c",
        "value": "שגיאת הידור",
        "type": "text",
        "html": "שגיאת הידור"
       },
       {
        "id": "d",
        "value": "`free` לא עושה כלום כי המערך קטן",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">free</code> לא עושה כלום כי המערך קטן"
       }
      ],
      "correctId": "a",
      "explanation": "`free` מותרת רק על כתובת שהתקבלה מ-`malloc`, `calloc` או `realloc`. מערך רגיל שייך למחסנית, ולכן שחרורו הוא התנהגות לא מוגדרת. הקוד כן מתקמפל.",
      "recap": "free על מערך רגיל: התנהגות לא מוגדרת.",
      "questionHtml": "מה נכון לגבי הקוד הבא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int a[3];\nfree(a);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">free</code> מותרת רק על כתובת שהתקבלה מ-<code class=\"tok\" dir=\"ltr\">malloc</code>, <code class=\"tok\" dir=\"ltr\">calloc</code> או <code class=\"tok\" dir=\"ltr\">realloc</code>. מערך רגיל שייך למחסנית, ולכן שחרורו הוא התנהגות לא מוגדרת. הקוד כן מתקמפל.",
      "recapHtml": "free על מערך רגיל: התנהגות לא מוגדרת."
     },
     {
      "id": "C07-Q6",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nint *p = (int *)malloc(3 * sizeof(int));\np[0] = 7;\np = (int *)realloc(p, 6 * sizeof(int));\nprintf(\"%d\", p[0]);\n```",
       "answer": 7,
       "tol": 0,
       "explain": "`realloc` שומרת את התוכן הקיים (גם אם היא מעבירה אותו לכתובת חדשה), ולכן `p[0]` נשאר 7. רק האיברים החדשים אינם מאותחלים.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int *p = (int *)malloc(3 * sizeof(int));\np[0] = 7;\np = (int *)realloc(p, 6 * sizeof(int));\nprintf(\"%d\", p[0]);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">realloc</code> שומרת את התוכן הקיים (גם אם היא מעבירה אותו לכתובת חדשה), ולכן <code class=\"tok\" dir=\"ltr\">p[0]</code> נשאר 7. רק האיברים החדשים אינם מאותחלים."
      },
      "recap": "realloc שומרת את התוכן הקיים.",
      "recapHtml": "realloc שומרת את התוכן הקיים."
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🧩",
    "title": "מבנים, איחוד וטווח",
    "goal": "אחרי השלב הזה אפשר לחשב מה קורה בהעתקת מבנה, בכתיבה לאיחוד, ובהסתרת משתנה גלובלי, ולהכיר מהן הנחיות קדם-מעבד.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p><b>העתקת מבנה</b> (<code>s2 = s1</code>) מעתיקה את כל השדות ערך אחר ערך. שדה מערך מועתק במלואו (העתק נפרד), ושדה מצביע מועתק ככתובת בלבד: שני המבנים מצביעים לאותו מקום.</p>\n    <pre><code>struct S { int a; int *p; };</code></pre>\n    <p><b>איחוד</b> (<code>union</code>) מחזיק את כל השדות באותו זיכרון. הכתיבה האחרונה קובעת את הערך שנקרא. באיחוד ששני שדותיו מאותו טיפוס, הכתיבה לשדה אחד משנה את השני.</p>\n    <p><b>טווח (scope)</b>: פרמטר או משתנה מקומי באותו שם כמו משתנה גלובלי <b>מסתיר</b> אותו בתוך הפונקציה או הבלוק. הפרמטר הוא עותק (העברה לפי ערך), ושינויו לא משפיע על הקורא.</p>\n    <p><b>הנחיות קדם-מעבד</b> הן שורות שמתחילות ב-<code>#</code> ומעובדות לפני ההידור: <code>#include</code>, <code>#define</code>, <code>#undef</code>, <code>#ifdef</code>, <code>#ifndef</code>, <code>#if</code>, <code>#endif</code>. המילה <code>typedef</code> אינה הנחיית קדם-מעבד: היא הצהרה רגילה של השפה.</p>\n    <div class=\"lesson-rule\">🔑 העתקת מבנה היא שטוחה: מצביעים מועתקים כתובת, מערכים בתוך המבנה מועתקים תוכן.</div>\n    <div class=\"lesson-ex\">דוגמה: ב-<code>struct T { int v[2]; }</code>, אחרי <code>t2 = t1; t2.v[0] = 9;</code> המערך של <code>t1</code> לא השתנה, כי <code>t2.v</code> הוא עותק.</div>\n    <div class=\"lesson-trap\">⚠️ שינוי של <code>*s2.p</code> משנה את הערך ש-<code>s1.p</code> מצביע אליו, כי שני המצביעים מכילים אותה כתובת.</div>"
    },
    "questions": [
     {
      "id": "C08-Q1",
      "question": "מה מדפיס הקוד?\n```c\nstruct S { int a; int *p; };\nint x = 1;\nstruct S s1 = {5, &x};\nstruct S s2 = s1;\ns2.a = 9;\n*s2.p = 7;\nprintf(\"%d %d %d\", s1.a, *s1.p, x);\n```",
      "options": [
       {
        "id": "a",
        "value": "`5 7 7`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5 7 7</code>"
       },
       {
        "id": "b",
        "value": "`9 7 7`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 7 7</code>"
       },
       {
        "id": "c",
        "value": "`5 1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5 1 1</code>"
       },
       {
        "id": "d",
        "value": "`9 1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 1 1</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`s2.a` הוא עותק, ולכן `s1.a` נשאר 5. `s2.p` ו-`s1.p` מכילים אותה כתובת (של `x`), ולכן הכתיבה `*s2.p = 7` משנה את `x` ונראית דרך שניהם.",
      "recap": "העתקת מבנה: שדה רגיל עותק, מצביע משותף.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>struct S { int a; int *p; };\nint x = 1;\nstruct S s1 = {5, &amp;x};\nstruct S s2 = s1;\ns2.a = 9;\n*s2.p = 7;\nprintf(\"%d %d %d\", s1.a, *s1.p, x);</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">s2.a</code> הוא עותק, ולכן <code class=\"tok\" dir=\"ltr\">s1.a</code> נשאר 5. <code class=\"tok\" dir=\"ltr\">s2.p</code> ו-<code class=\"tok\" dir=\"ltr\">s1.p</code> מכילים אותה כתובת (של <code class=\"tok\" dir=\"ltr\">x</code>), ולכן הכתיבה <code class=\"tok\" dir=\"ltr\">*s2.p = 7</code> משנה את <code class=\"tok\" dir=\"ltr\">x</code> ונראית דרך שניהם.",
      "recapHtml": "העתקת מבנה: שדה רגיל עותק, מצביע משותף."
     },
     {
      "id": "C08-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nstruct T { int v[2]; };\nstruct T t1 = {{1, 2}};\nstruct T t2 = t1;\nt2.v[0] = 9;\nprintf(\"%d\", t1.v[0]);\n```",
       "answer": 1,
       "tol": 0,
       "explain": "מערך בתוך מבנה מועתק במלואו, ולכן `t2.v` הוא עותק נפרד. שינוי בו לא משפיע על `t1.v[0]`, שנשאר 1.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>struct T { int v[2]; };\nstruct T t1 = {{1, 2}};\nstruct T t2 = t1;\nt2.v[0] = 9;\nprintf(\"%d\", t1.v[0]);</code></pre>",
       "explainHtml": "מערך בתוך מבנה מועתק במלואו, ולכן <code class=\"tok\" dir=\"ltr\">t2.v</code> הוא עותק נפרד. שינוי בו לא משפיע על <code class=\"tok\" dir=\"ltr\">t1.v[0]</code>, שנשאר 1."
      },
      "recap": "מערך בתוך מבנה מועתק במלואו.",
      "recapHtml": "מערך בתוך מבנה מועתק במלואו."
     },
     {
      "id": "C08-Q3",
      "question": "מה מדפיס הקוד?\n```c\nunion U { int a; int b; } u;\nu.a = 5;\nu.b = 8;\nprintf(\"%d\", u.a);\n```",
      "options": [
       {
        "id": "a",
        "value": "`8`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">8</code>"
       },
       {
        "id": "b",
        "value": "`5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5</code>"
       },
       {
        "id": "c",
        "value": "`13`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">13</code>"
       },
       {
        "id": "d",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       }
      ],
      "correctId": "a",
      "explanation": "שדות האיחוד חולקים את אותו זיכרון, והכתיבה האחרונה (`u.b = 8`) דורסת את הקודמת. לכן קוראים 8 גם דרך `u.a`.",
      "recap": "באיחוד הכתיבה האחרונה קובעת.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>union U { int a; int b; } u;\nu.a = 5;\nu.b = 8;\nprintf(\"%d\", u.a);</code></pre>",
      "explanationHtml": "שדות האיחוד חולקים את אותו זיכרון, והכתיבה האחרונה (<code class=\"tok\" dir=\"ltr\">u.b = 8</code>) דורסת את הקודמת. לכן קוראים 8 גם דרך <code class=\"tok\" dir=\"ltr\">u.a</code>.",
      "recapHtml": "באיחוד הכתיבה האחרונה קובעת."
     },
     {
      "id": "C08-Q4",
      "question": "מה מדפיס הקוד?\n```c\nint x = 10;\nvoid f(int x)\n{\n    x = x + 1;\n    printf(\"%d \", x);\n}\nint main(void)\n{\n    f(1);\n    printf(\"%d\", x);\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`2 10`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 10</code>"
       },
       {
        "id": "b",
        "value": "`11 11`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">11 11</code>"
       },
       {
        "id": "c",
        "value": "`2 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 2</code>"
       },
       {
        "id": "d",
        "value": "`11 10`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">11 10</code>"
       }
      ],
      "correctId": "a",
      "explanation": "הפרמטר `x` מסתיר את הגלובלי בתוך `f`: הוא מקבל 1, גדל ל-2 ומודפס. הגלובלי לא נגע, ולכן ב-`main` מודפס 10.",
      "recap": "פרמטר באותו שם מסתיר את הגלובלי.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x = 10;\nvoid f(int x)\n{\n    x = x + 1;\n    printf(\"%d \", x);\n}\nint main(void)\n{\n    f(1);\n    printf(\"%d\", x);\n    return 0;\n}</code></pre>",
      "explanationHtml": "הפרמטר <code class=\"tok\" dir=\"ltr\">x</code> מסתיר את הגלובלי בתוך <code class=\"tok\" dir=\"ltr\">f</code>: הוא מקבל 1, גדל ל-2 ומודפס. הגלובלי לא נגע, ולכן ב-<code class=\"tok\" dir=\"ltr\">main</code> מודפס 10.",
      "recapHtml": "פרמטר באותו שם מסתיר את הגלובלי."
     },
     {
      "id": "C08-Q5",
      "question": "מה מדפיס הקוד?\n```c\nint x = 1;\n{\n    int x = 2;\n    x++;\n}\nprintf(\"%d\", x);\n```",
      "options": [
       {
        "id": "a",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "b",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       },
       {
        "id": "c",
        "value": "`3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3</code>"
       },
       {
        "id": "d",
        "value": "שגיאת הידור",
        "type": "text",
        "html": "שגיאת הידור"
       }
      ],
      "correctId": "a",
      "explanation": "בתוך הבלוק `x` הוא משתנה חדש שמסתיר את החיצוני, וה-`x++` משנה אותו בלבד. אחרי הבלוק הוא נעלם, והחיצוני נשאר 1. הצהרה באותו שם בבלוק פנימי מותרת.",
      "recap": "משתנה בבלוק פנימי מסתיר ולא משנה את החיצוני.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x = 1;\n{\n    int x = 2;\n    x++;\n}\nprintf(\"%d\", x);</code></pre>",
      "explanationHtml": "בתוך הבלוק <code class=\"tok\" dir=\"ltr\">x</code> הוא משתנה חדש שמסתיר את החיצוני, וה-<code class=\"tok\" dir=\"ltr\">x++</code> משנה אותו בלבד. אחרי הבלוק הוא נעלם, והחיצוני נשאר 1. הצהרה באותו שם בבלוק פנימי מותרת.",
      "recapHtml": "משתנה בבלוק פנימי מסתיר ולא משנה את החיצוני."
     },
     {
      "id": "C08-Q6",
      "question": "מה מהבאים **אינו** חלק מהנחיית קדם-מעבד?",
      "options": [
       {
        "id": "a",
        "value": "`typedef`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">typedef</code>"
       },
       {
        "id": "b",
        "value": "`define`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">define</code>"
       },
       {
        "id": "c",
        "value": "`ifndef`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">ifndef</code>"
       },
       {
        "id": "d",
        "value": "`include`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">include</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`define`, `ifndef` ו-`include` הן הנחיות קדם-מעבד שנכתבות אחרי `#`. `typedef` היא הצהרה רגילה של שפת C שמעובדת בהידור עצמו.",
      "recap": "typedef אינה הנחיית קדם-מעבד.",
      "questionHtml": "מה מהבאים <strong>אינו</strong> חלק מהנחיית קדם-מעבד?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">define</code>, <code class=\"tok\" dir=\"ltr\">ifndef</code> ו-<code class=\"tok\" dir=\"ltr\">include</code> הן הנחיות קדם-מעבד שנכתבות אחרי <code class=\"tok\" dir=\"ltr\">#</code>. <code class=\"tok\" dir=\"ltr\">typedef</code> היא הצהרה רגילה של שפת C שמעובדת בהידור עצמו.",
      "recapHtml": "typedef אינה הנחיית קדם-מעבד."
     }
    ]
   },
   {
    "id": "C09",
    "order": 9,
    "icon": "🏆",
    "title": "אתגר המלכודות",
    "goal": "אחרי השלב הזה אפשר לפתור שאלות מלכודת אמיתיות מהמבחנים: סיווג הנחיות, הכללה בין פונקציות קלט, sizeof של מחרוזת, לולאת fgetc וחילוק תווים.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "\n    <p>אתגר סיום: חמש שאלות אמיתיות מבחנים קודמים. לפני שפותרים, הפעילו את הכללים מהשלבים הקודמים.</p>\n    <ul>\n      <li>תו הוא מספר, והחילוק בין תווים הוא חילוק שלם; לולאה על מערך נעצרת באיבר 0.</li>\n      <li><code>sizeof</code> של מחרוזת קבועה כולל את <code>'\\0'</code>, והאינדקס חזק מ-<code>sizeof</code>.</li>\n      <li><code>!=</code> חזק מ-<code>=</code>, ולכן בלי סוגריים ההשמה מקבלת 0 או 1.</li>\n      <li><code>fgets</code> שונה מ-<code>gets</code>; הצורות שמתחילות ב-<code>f</code> הן הכללות של הצורות הרגילות רק כשהן מתנהגות אותו דבר על <code>stdin</code>.</li>\n      <li><code>typedef</code> אינה הנחיית קדם-מעבד.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 בכל שאלה כתבו את הכלל שעליו הסתמכתם לפני שאתם בוחרים תשובה.</div>"
    },
    "questions": [
     {
      "bankId": "19S-A-Q4d",
      "recap": "typedef אינה הנחיית קדם-מעבד.",
      "recapHtml": "typedef אינה הנחיית קדם-מעבד."
     },
     {
      "bankId": "20B-A-Q4a",
      "recap": "fgets אינה הכללה של gets.",
      "recapHtml": "fgets אינה הכללה של gets."
     },
     {
      "bankId": "19B-A-Q5",
      "recap": "[ ] חזק מ-sizeof, והגודל הוא של תו.",
      "recapHtml": "[ ] חזק מ-sizeof, והגודל הוא של תו."
     },
     {
      "bankId": "25B-A-Q6",
      "recap": "!= חזק מ-=, ולכן c הוא 1.",
      "recapHtml": "!= חזק מ-=, ולכן c הוא 1."
     },
     {
      "bankId": "25B-B-Q6",
      "recap": "חילוק תווים שלם והלולאה נעצרת באפס.",
      "recapHtml": "חילוק תווים שלם והלולאה נעצרת באפס."
     }
    ]
   }
  ]
 },
 "dyn_2d": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🧱",
    "title": "מערך של מצביעים: int **",
    "goal": "אחרי השלב הזה אפשר להסביר מה מטריצה דינמית היא בזיכרון, מה הטיפוס של m, של m[i] ושל m[i][j], וכמה הקצאות היא דורשת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>מטריצה דינמית אינה בלוק אחד. היא <b>מערך של מצביעים</b>, וכל מצביע מראה על שורה שהוקצתה בנפרד. את המערך החיצוני מחזיקים במצביע מסוג <code>int **</code>.</p>\n    <pre><code>m ──► [ m[0] ][ m[1] ][ m[2] ]     (int **)\n         │        │        └──► [ . . . . ]   row 2\n         │        └───────────► [ . . . . ]   row 1\n         └────────────────────► [ . . . . ]   row 0</code></pre>\n    <ul>\n      <li><code>m[i]</code> הוא מצביע <code>int *</code> לשורה <code>i</code>.</li>\n      <li><code>m[i][j]</code> הוא האיבר בשורה <code>i</code> ובעמודה <code>j</code>, מסוג <code>int</code>. זה שקול ל-<code>*(*(m + i) + j)</code>.</li>\n      <li>ב-64 סיביות <code>sizeof(int *)</code> הוא 8 בתים, ו-<code>sizeof(int)</code> הוא 4.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 אינדקס אחד על <code>int **</code> נותן שורה. שני אינדקסים נותנים איבר. ומטריצה עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi></mrow><annotation encoding=\"application/x-tex\">r</annotation></semantics></math></span> שורות דורשת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">r+1</annotation></semantics></math></span> הקצאות: אחת למערך המצביעים ועוד אחת לכל שורה.</div>\n    <div class=\"lesson-ex\">דוגמה: אחרי הבנייה של מטריצה 2×3 עם <code>m[i][j] = i * 10 + j</code> מתקבל <code>m[0] = {0, 1, 2}</code> ו-<code>m[1] = {10, 11, 12}</code>. אז <code>m[1][2]</code> הוא 12, וגם <code>*(*m + 1)</code> הוא <code>m[0][1]</code>, כלומר 1.</div>\n    <div class=\"lesson-trap\">⚠️ <code>m[j][i]</code> במקום <code>m[i][j]</code> מדפיס את המטריצה המשוחלפת, ובמטריצה לא ריבועית גם קורא מחוץ לגבולות.</div>"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "question": "מגדירים `int **m;` ו-`m` מצביע על מערך מצביעים שהוקצה. מהו הטיפוס של הביטוי `m[1]`?",
      "options": [
       {
        "id": "a",
        "value": "`int`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">int</code>"
       },
       {
        "id": "b",
        "value": "`int *`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">int *</code>"
       },
       {
        "id": "c",
        "value": "`int **`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">int **</code>"
       },
       {
        "id": "d",
        "value": "`int ***`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">int ***</code>"
       }
      ],
      "correctId": "b",
      "explanation": "`m` הוא `int **`, ו-`m[1]` הוא איבר אחד במערך המצביעים, כלומר `int *`: כתובת של שורה שלמה. `int` הוא רק `m[1][j]`, אחרי שני אינדקסים. `int **` הוא `m` עצמו, ו-`int ***` הוא `&m`.",
      "recap": "אינדקס אחד על `int **` נותן שורה (`int *`), שני אינדקסים נותנים איבר (`int`).",
      "questionHtml": "מגדירים <code class=\"tok\" dir=\"ltr\">int **m;</code> ו-<code class=\"tok\" dir=\"ltr\">m</code> מצביע על מערך מצביעים שהוקצה. מהו הטיפוס של הביטוי <code class=\"tok\" dir=\"ltr\">m[1]</code>?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">m</code> הוא <code class=\"tok\" dir=\"ltr\">int <strong></code>, ו-<code class=\"tok\" dir=\"ltr\">m[1]</code> הוא איבר אחד במערך המצביעים, כלומר <code class=\"tok\" dir=\"ltr\">int *</code>: כתובת של שורה שלמה. <code class=\"tok\" dir=\"ltr\">int</code> הוא רק <code class=\"tok\" dir=\"ltr\">m[1][j]</code>, אחרי שני אינדקסים. <code class=\"tok\" dir=\"ltr\">int </strong></code> הוא <code class=\"tok\" dir=\"ltr\">m</code> עצמו, ו-<code class=\"tok\" dir=\"ltr\">int ***</code> הוא <code class=\"tok\" dir=\"ltr\">&amp;m</code>.",
      "recapHtml": "אינדקס אחד על <code class=\"tok\" dir=\"ltr\">int **</code> נותן שורה (<code class=\"tok\" dir=\"ltr\">int *</code>), שני אינדקסים נותנים איבר (<code class=\"tok\" dir=\"ltr\">int</code>)."
     },
     {
      "id": "C01-Q2",
      "question": "מה מדפיס הקוד? (כל ההקצאות מצליחות)\n```c\nint main(void)\n{\n    int **m = (int **)calloc(2, sizeof(int *));\n    int i, j;\n    for (i = 0; i < 2; i++)\n    {\n        m[i] = (int *)calloc(3, sizeof(int));\n        for (j = 0; j < 3; j++)\n            m[i][j] = i * 10 + j;\n    }\n    printf(\"%d %d\", m[1][2], *(*m + 1));\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`12 10`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">12 10</code>"
       },
       {
        "id": "b",
        "value": "`12 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">12 1</code>"
       },
       {
        "id": "c",
        "value": "`2 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 1</code>"
       },
       {
        "id": "d",
        "value": "`21 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">21 1</code>"
       }
      ],
      "correctId": "b",
      "explanation": "האיבר בשורה 1 ובעמודה 2 הוא `1 * 10 + 2 = 12`. הביטוי `*m` הוא `m[0]`, כלומר שורה 0, ו-`*(*m + 1)` הוא `m[0][1] = 0 * 10 + 1 = 1`. הפלט `12 10` מתעלם מכך ש-`m[0][1]` הוא 1 ולא 10. `2 1` ו-`21 1` מחליפים ספרות או אינדקסים.",
      "recap": "`m[i][j]` שווה ל-`*(*(m + i) + j)`.",
      "questionHtml": "מה מדפיס הקוד? (כל ההקצאות מצליחות)<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int main(void)\n{\n    int **m = (int **)calloc(2, sizeof(int *));\n    int i, j;\n    for (i = 0; i &lt; 2; i++)\n    {\n        m[i] = (int *)calloc(3, sizeof(int));\n        for (j = 0; j &lt; 3; j++)\n            m[i][j] = i * 10 + j;\n    }\n    printf(\"%d %d\", m[1][2], *(*m + 1));\n    return 0;\n}</code></pre>",
      "explanationHtml": "האיבר בשורה 1 ובעמודה 2 הוא <code class=\"tok\" dir=\"ltr\">1 * 10 + 2 = 12</code>. הביטוי <code class=\"tok\" dir=\"ltr\">*m</code> הוא <code class=\"tok\" dir=\"ltr\">m[0]</code>, כלומר שורה 0, ו-<code class=\"tok\" dir=\"ltr\">*(*m + 1)</code> הוא <code class=\"tok\" dir=\"ltr\">m[0][1] = 0 * 10 + 1 = 1</code>. הפלט <code class=\"tok\" dir=\"ltr\">12 10</code> מתעלם מכך ש-<code class=\"tok\" dir=\"ltr\">m[0][1]</code> הוא 1 ולא 10. <code class=\"tok\" dir=\"ltr\">2 1</code> ו-<code class=\"tok\" dir=\"ltr\">21 1</code> מחליפים ספרות או אינדקסים.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">m[i][j]</code> שווה ל-<code class=\"tok\" dir=\"ltr\">*(*(m + i) + j)</code>."
     },
     {
      "id": "C01-Q3",
      "step": {
       "type": "numeric",
       "prompt": "כמה קריאות להקצאה (`calloc`) נדרשות כדי לבנות מטריצה דינמית עם 4 שורות ו-5 עמודות?",
       "answer": 5,
       "tol": 0,
       "explain": "קריאה אחת למערך המצביעים ועוד קריאה לכל שורה: $1 + 4 = 5$. אין קריאה אחת לכל התאים.",
       "promptHtml": "כמה קריאות להקצאה (<code class=\"tok\" dir=\"ltr\">calloc</code>) נדרשות כדי לבנות מטריצה דינמית עם 4 שורות ו-5 עמודות?",
       "explainHtml": "קריאה אחת למערך המצביעים ועוד קריאה לכל שורה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>5</mn></mrow><annotation encoding=\"application/x-tex\">1 + 4 = 5</annotation></semantics></math></span>. אין קריאה אחת לכל התאים."
      },
      "recap": "מטריצה עם $r$ שורות = $r + 1$ הקצאות.",
      "recapHtml": "מטריצה עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi></mrow><annotation encoding=\"application/x-tex\">r</annotation></semantics></math></span> שורות = <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">r + 1</annotation></semantics></math></span> הקצאות."
     },
     {
      "id": "C01-Q4",
      "question": "בהידור ל-64 סיביות, כמה בתים תופס מצביע, כלומר מהו `sizeof(int *)`?",
      "options": [
       {
        "id": "a",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       },
       {
        "id": "b",
        "value": "`4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4</code>"
       },
       {
        "id": "c",
        "value": "`8`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">8</code>"
       },
       {
        "id": "d",
        "value": "`16`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">16</code>"
       }
      ],
      "correctId": "c",
      "explanation": "במחשב 64 סיביות כל כתובת היא 8 בתים. הערך 4 הוא `sizeof(int)` ולא גודל מצביע. לכן מערך של $r$ מצביעים דורש $8r$ בתים, ולא $4r$.",
      "recap": "מצביע = 8 בתים ב-64 סיביות; `int` = 4 בתים.",
      "questionHtml": "בהידור ל-64 סיביות, כמה בתים תופס מצביע, כלומר מהו <code class=\"tok\" dir=\"ltr\">sizeof(int *)</code>?",
      "explanationHtml": "במחשב 64 סיביות כל כתובת היא 8 בתים. הערך 4 הוא <code class=\"tok\" dir=\"ltr\">sizeof(int)</code> ולא גודל מצביע. לכן מערך של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi></mrow><annotation encoding=\"application/x-tex\">r</annotation></semantics></math></span> מצביעים דורש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>8</mn><mi>r</mi></mrow><annotation encoding=\"application/x-tex\">8r</annotation></semantics></math></span> בתים, ולא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mi>r</mi></mrow><annotation encoding=\"application/x-tex\">4r</annotation></semantics></math></span>.",
      "recapHtml": "מצביע = 8 בתים ב-64 סיביות; <code class=\"tok\" dir=\"ltr\">int</code> = 4 בתים."
     },
     {
      "id": "C01-Q5",
      "step": {
       "type": "findbug",
       "prompt": "הקוד אמור להדפיס את המטריצה שורה אחר שורה: `0 1 2` ואז `3 4 5` ואז `6 7 8`. מצאו את השורה השגויה.",
       "code": true,
       "lines": [
        "int **m = (int **)calloc(3, sizeof(int *));",
        "int i, j;",
        "for (i = 0; i < 3; i++)",
        "{",
        "    m[i] = (int *)calloc(3, sizeof(int));",
        "    for (j = 0; j < 3; j++)",
        "        m[i][j] = i * 3 + j;",
        "}",
        "for (i = 0; i < 3; i++)",
        "{",
        "    for (j = 0; j < 3; j++)",
        "        printf(\"%d \", m[j][i]);",
        "    printf(\"\\n\");",
        "}"
       ],
       "bugIndex": 11,
       "explain": "האינדקס הראשון הוא השורה והשני העמודה. `m[j][i]` מחליף ביניהם, ולכן מודפסת המטריצה המשוחלפת (`0 3 6` בשורה הראשונה).",
       "promptHtml": "הקוד אמור להדפיס את המטריצה שורה אחר שורה: <code class=\"tok\" dir=\"ltr\">0 1 2</code> ואז <code class=\"tok\" dir=\"ltr\">3 4 5</code> ואז <code class=\"tok\" dir=\"ltr\">6 7 8</code>. מצאו את השורה השגויה.",
       "explainHtml": "האינדקס הראשון הוא השורה והשני העמודה. <code class=\"tok\" dir=\"ltr\">m[j][i]</code> מחליף ביניהם, ולכן מודפסת המטריצה המשוחלפת (<code class=\"tok\" dir=\"ltr\">0 3 6</code> בשורה הראשונה).",
       "linesHtml": [
        "int **m = (int **)calloc(3, sizeof(int *));",
        "int i, j;",
        "for (i = 0; i &lt; 3; i++)",
        "{",
        "    m[i] = (int *)calloc(3, sizeof(int));",
        "    for (j = 0; j &lt; 3; j++)",
        "        m[i][j] = i * 3 + j;",
        "}",
        "for (i = 0; i &lt; 3; i++)",
        "{",
        "    for (j = 0; j &lt; 3; j++)",
        "        printf(\"%d \", m[j][i]);",
        "    printf(\"\\n\");",
        "}"
       ]
      },
      "recap": "`m[i][j]`: קודם שורה (`i`), אחר כך עמודה (`j`).",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">m[i][j]</code>: קודם שורה (<code class=\"tok\" dir=\"ltr\">i</code>), אחר כך עמודה (<code class=\"tok\" dir=\"ltr\">j</code>)."
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "🏗️",
    "title": "הקצאת מטריצה rows × cols",
    "goal": "אחרי השלב הזה אפשר לכתוב פונקציה שמקצה מטריצה דינמית מאופסת, ולחשב כמה בתים היא תופסת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>בונים מטריצה <code>rows × cols</code> בשני שלבים: קודם <b>מערך המצביעים</b>, ואז <b>כל שורה בנפרד</b> בלולאה.</p>\n    <pre><code>int **alloc_matrix(int rows, int cols)\n{\n    int i;\n    int **m = (int **)calloc(rows, sizeof(int *));\n    for (i = 0; i &lt; rows; i++)\n        m[i] = (int *)calloc(cols, sizeof(int));\n    return m;\n}</code></pre>\n    <ul>\n      <li><code>calloc(n, size)</code> מקצה <code>n</code> איברים בגודל <code>size</code> ומאפס אותם. <code>malloc</code> לא מאפס, והתאים מכילים זבל.</li>\n      <li>גודל איבר במערך המצביעים: <code>sizeof(int *)</code> (8 בתים). גודל איבר בשורה: <code>sizeof(int)</code> (4 בתים).</li>\n      <li>סך הבתים הוא <code>n * size</code> של כל קריאה: למטריצה 3×4 מקבלים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>8</mn><mo>+</mo><mn>3</mn><mo>⋅</mo><mn>4</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>72</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 8 + 3 \\cdot 4 \\cdot 4 = 72</annotation></semantics></math></span>.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 מערך המצביעים: <code>rows</code> איברים של <code>sizeof(int *)</code>. כל שורה: <code>cols</code> איברים של <code>sizeof(int)</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: <code>alloc_matrix(2, 3)</code> קורא ל-<code>calloc(2, 8)</code> ואז פעמיים ל-<code>calloc(3, 4)</code>. כל התאים מתחילים באפס.</div>\n    <div class=\"lesson-trap\">⚠️ <code>calloc(rows, sizeof(int))</code> למערך המצביעים מקצה חצי ממה שצריך ב-64 סיביות. ו-<code>malloc</code> במקום <code>calloc</code> משאיר ערכי זבל כשהמטריצה אמורה להתחיל באפסים.</div>"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "step": {
       "type": "order",
       "prompt": "הפונקציה `alloc_matrix` כבר כתובה. סדרו את הפקודות ב-`main` כך שתוקצה מטריצה, יוכנס 7 לשורה 1 עמודה 2, והערך יודפס.",
       "code": true,
       "lines": [
        "int **m = alloc_matrix(2, 3);",
        "m[1][2] = 7;",
        "printf(\"%d\", m[1][2]);",
        "return 0;"
       ],
       "explain": "קודם מקצים (בלי מטריצה אין לאן לכתוב), אחר כך כותבים, אחר כך קוראים ומדפיסים, ורק בסוף `return`.",
       "promptHtml": "הפונקציה <code class=\"tok\" dir=\"ltr\">alloc_matrix</code> כבר כתובה. סדרו את הפקודות ב-<code class=\"tok\" dir=\"ltr\">main</code> כך שתוקצה מטריצה, יוכנס 7 לשורה 1 עמודה 2, והערך יודפס.",
       "explainHtml": "קודם מקצים (בלי מטריצה אין לאן לכתוב), אחר כך כותבים, אחר כך קוראים ומדפיסים, ורק בסוף <code class=\"tok\" dir=\"ltr\">return</code>.",
       "linesHtml": [
        "int **m = alloc_matrix(2, 3);",
        "m[1][2] = 7;",
        "printf(\"%d\", m[1][2]);",
        "return 0;"
       ]
      },
      "recap": "הקצאה, כתיבה, שימוש, ואז `return`.",
      "recapHtml": "הקצאה, כתיבה, שימוש, ואז <code class=\"tok\" dir=\"ltr\">return</code>."
     },
     {
      "id": "C02-Q2",
      "question": "צריך להקצות את מערך המצביעים של מטריצה עם 3 שורות ו-4 עמודות, ב-64 סיביות, בגודל של בדיוק מצביע אחד לכל שורה. איזו קריאה מבקשת בדיוק את הכמות הזאת?",
      "options": [
       {
        "id": "a",
        "value": "`calloc(3, sizeof(int *))`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">calloc(3, sizeof(int *))</code>"
       },
       {
        "id": "b",
        "value": "`calloc(3, sizeof(int))`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">calloc(3, sizeof(int))</code>"
       },
       {
        "id": "c",
        "value": "`calloc(4, sizeof(int))`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">calloc(4, sizeof(int))</code>"
       },
       {
        "id": "d",
        "value": "`calloc(3, 3 * sizeof(int *))`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">calloc(3, 3 * sizeof(int *))</code>"
       }
      ],
      "correctId": "a",
      "explanation": "שלוש שורות = שלושה מצביעים = $3 \\cdot 8 = 24$ בתים, וזה `calloc(3, sizeof(int *))`. `calloc(3, sizeof(int))` מבקשת $3 \\cdot 4 = 12$ בתים, `calloc(4, sizeof(int))` מבקשת $4 \\cdot 4 = 16$, ו-`calloc(3, 3 * sizeof(int *))` מבקשת $3 \\cdot 24 = 72$. רק הראשונה מבקשת בדיוק 24 (נבדק עם מקצה מתעד).",
      "recap": "למערך המצביעים: מספר השורות כפול `sizeof(int *)`.",
      "questionHtml": "צריך להקצות את מערך המצביעים של מטריצה עם 3 שורות ו-4 עמודות, ב-64 סיביות, בגודל של בדיוק מצביע אחד לכל שורה. איזו קריאה מבקשת בדיוק את הכמות הזאת?",
      "explanationHtml": "שלוש שורות = שלושה מצביעים = <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>8</mn><mo>=</mo><mn>24</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 8 = 24</annotation></semantics></math></span> בתים, וזה <code class=\"tok\" dir=\"ltr\">calloc(3, sizeof(int *))</code>. <code class=\"tok\" dir=\"ltr\">calloc(3, sizeof(int))</code> מבקשת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 4 = 12</annotation></semantics></math></span> בתים, <code class=\"tok\" dir=\"ltr\">calloc(4, sizeof(int))</code> מבקשת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>16</mn></mrow><annotation encoding=\"application/x-tex\">4 \\cdot 4 = 16</annotation></semantics></math></span>, ו-<code class=\"tok\" dir=\"ltr\">calloc(3, 3 * sizeof(int *))</code> מבקשת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>24</mn><mo>=</mo><mn>72</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 24 = 72</annotation></semantics></math></span>. רק הראשונה מבקשת בדיוק 24 (נבדק עם מקצה מתעד).",
      "recapHtml": "למערך המצביעים: מספר השורות כפול <code class=\"tok\" dir=\"ltr\">sizeof(int *)</code>."
     },
     {
      "id": "C02-Q3",
      "step": {
       "type": "fillblank",
       "prompt": "השלימו את גודל האיבר בהקצאת מערך המצביעים.",
       "code": true,
       "lines": [
        "int **alloc_matrix(int rows, int cols)",
        "{",
        "    int i;",
        "    int **m = (int **)calloc(rows, ___);",
        "    for (i = 0; i < rows; i++)",
        "        m[i] = (int *)calloc(cols, sizeof(int));",
        "    return m;",
        "}"
       ],
       "blankIndex": 3,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "sizeof(int *)",
         "html": "sizeof(int *)"
        },
        {
         "id": "b",
         "type": "text",
         "value": "sizeof(int)",
         "html": "sizeof(int)"
        },
        {
         "id": "c",
         "type": "text",
         "value": "cols * sizeof(int)",
         "html": "cols * sizeof(int)"
        },
        {
         "id": "d",
         "type": "text",
         "value": "rows",
         "html": "rows"
        }
       ],
       "correctId": "a",
       "explain": "איבר במערך המצביעים הוא `int *`, ולכן גודלו `sizeof(int *)`. כל אחת מהאפשרויות האחרות מבקשת גודל איבר שאינו 8 בתים.",
       "promptHtml": "השלימו את גודל האיבר בהקצאת מערך המצביעים.",
       "explainHtml": "איבר במערך המצביעים הוא <code class=\"tok\" dir=\"ltr\">int *</code>, ולכן גודלו <code class=\"tok\" dir=\"ltr\">sizeof(int *)</code>. כל אחת מהאפשרויות האחרות מבקשת גודל איבר שאינו 8 בתים.",
       "linesHtml": [
        "int **alloc_matrix(int rows, int cols)",
        "{",
        "    int i;",
        "    int **m = (int **)calloc(rows, ___);",
        "    for (i = 0; i &lt; rows; i++)",
        "        m[i] = (int *)calloc(cols, sizeof(int));",
        "    return m;",
        "}"
       ]
      },
      "recap": "גודל איבר במערך השורות: `sizeof(int *)`.",
      "recapHtml": "גודל איבר במערך השורות: <code class=\"tok\" dir=\"ltr\">sizeof(int *)</code>."
     },
     {
      "id": "C02-Q4",
      "step": {
       "type": "numeric",
       "prompt": "כמה בתים בסך הכל מקצה הקריאה `alloc_matrix(3, 4)` ב-64 סיביות, כולל מערך המצביעים?",
       "answer": 72,
       "tol": 0,
       "explain": "מערך המצביעים: $3 \\cdot 8 = 24$ בתים. שלוש שורות של 4 מספרים: $3 \\cdot 4 \\cdot 4 = 48$ בתים. סך הכל $24 + 48 = 72$.",
       "promptHtml": "כמה בתים בסך הכל מקצה הקריאה <code class=\"tok\" dir=\"ltr\">alloc_matrix(3, 4)</code> ב-64 סיביות, כולל מערך המצביעים?",
       "explainHtml": "מערך המצביעים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>8</mn><mo>=</mo><mn>24</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 8 = 24</annotation></semantics></math></span> בתים. שלוש שורות של 4 מספרים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>⋅</mo><mn>4</mn><mo>⋅</mo><mn>4</mn><mo>=</mo><mn>48</mn></mrow><annotation encoding=\"application/x-tex\">3 \\cdot 4 \\cdot 4 = 48</annotation></semantics></math></span> בתים. סך הכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>24</mn><mo>+</mo><mn>48</mn><mo>=</mo><mn>72</mn></mrow><annotation encoding=\"application/x-tex\">24 + 48 = 72</annotation></semantics></math></span>."
      },
      "recap": "בתים = שורות$\\cdot 8$ + שורות$\\cdot$עמודות$\\cdot 4$.",
      "recapHtml": "בתים = שורות<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>⋅</mo><mn>8</mn></mrow><annotation encoding=\"application/x-tex\">\\cdot 8</annotation></semantics></math></span> + שורות<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>⋅</mo></mrow><annotation encoding=\"application/x-tex\">\\cdot</annotation></semantics></math></span>עמודות<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo>⋅</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">\\cdot 4</annotation></semantics></math></span>."
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "findbug",
       "prompt": "הפונקציה אמורה להקצות מטריצה `rows` על `cols`, אבל במטריצה 2 על 3 השורות קצרות מדי. מצאו את השורה השגויה.",
       "code": true,
       "lines": [
        "int **alloc_matrix(int rows, int cols)",
        "{",
        "    int i;",
        "    int **m = (int **)calloc(rows, sizeof(int *));",
        "    for (i = 0; i < rows; i++)",
        "        m[i] = (int *)calloc(rows, sizeof(int));",
        "    return m;",
        "}"
       ],
       "bugIndex": 5,
       "explain": "אורך כל שורה הוא מספר העמודות. `calloc(rows, ...)` מקצה שורות באורך `rows`, ובמטריצה לא ריבועית זה קטן (או גדול) מדי.",
       "promptHtml": "הפונקציה אמורה להקצות מטריצה <code class=\"tok\" dir=\"ltr\">rows</code> על <code class=\"tok\" dir=\"ltr\">cols</code>, אבל במטריצה 2 על 3 השורות קצרות מדי. מצאו את השורה השגויה.",
       "explainHtml": "אורך כל שורה הוא מספר העמודות. <code class=\"tok\" dir=\"ltr\">calloc(rows, ...)</code> מקצה שורות באורך <code class=\"tok\" dir=\"ltr\">rows</code>, ובמטריצה לא ריבועית זה קטן (או גדול) מדי.",
       "linesHtml": [
        "int **alloc_matrix(int rows, int cols)",
        "{",
        "    int i;",
        "    int **m = (int **)calloc(rows, sizeof(int *));",
        "    for (i = 0; i &lt; rows; i++)",
        "        m[i] = (int *)calloc(rows, sizeof(int));",
        "    return m;",
        "}"
       ]
      },
      "recap": "אורך שורה = `cols`, מספר השורות = `rows`.",
      "recapHtml": "אורך שורה = <code class=\"tok\" dir=\"ltr\">cols</code>, מספר השורות = <code class=\"tok\" dir=\"ltr\">rows</code>."
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "🧹",
    "title": "שחרור: שורות ואז המערך החיצוני",
    "goal": "אחרי השלב הזה אפשר לשחרר מטריצה דינמית נכון, לספור את השחרורים הנדרשים ולזהות דליפות.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>כל <code>calloc</code> צריך <code>free</code> אחד. במטריצה דינמית יש <b><span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">r + 1</annotation></semantics></math></span> בלוקים נפרדים</b>, ולכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">r + 1</annotation></semantics></math></span> שחרורים.</p>\n    <pre><code>void free_matrix(int **m, int rows)\n{\n    int i;\n    for (i = 0; i &lt; rows; i++)\n        free(m[i]);\n    free(m);\n}</code></pre>\n    <ul>\n      <li><b>קודם השורות, אחר כך מערך המצביעים.</b> השורות מוכרות רק דרך <code>m[i]</code>; אחרי <code>free(m)</code> הכתובות האלה אבדו.</li>\n      <li><code>free(m)</code> לבד משחרר רק את מערך המצביעים, והשורות דולפות (דליפת זיכרון).</li>\n      <li><code>free(NULL)</code> בטוח ולא עושה כלום. אבל <code>free</code> פעמיים על אותה כתובת אמיתית הוא באג.</li>\n      <li>מערך סטטי (<code>int A[3][3]</code>) לא הוקצה ב-<code>calloc</code>, ולכן אסור לעשות לו <code>free</code>.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 שחרור מטריצה: לולאה על כל השורות עם <code>free(m[i])</code>, ורק אחריה <code>free(m)</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: עבור מטריצה עם 3 שורות מבצעים <code>free(m[0])</code>, <code>free(m[1])</code>, <code>free(m[2])</code> ואז <code>free(m)</code>: ארבעה שחרורים לארבע הקצאות.</div>\n    <div class=\"lesson-trap\">⚠️ לולאת שחרור שמתחילה מ-<code>i = 1</code>, או שמסתיימת מוקדם מדי, משאירה שורה בלי שחרור. ולולאה עם <code>i &lt;= rows</code> קוראת את <code>m[rows]</code> שאינו קיים.</div>"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "step": {
       "type": "numeric",
       "prompt": "כמה קריאות ל-`free` נדרשות כדי לשחרר מטריצה דינמית עם 5 שורות?",
       "answer": 6,
       "tol": 0,
       "explain": "כל שורה משוחררת בנפרד (5 קריאות) ועוד מערך המצביעים עצמו: $5 + 1 = 6$, בדיוק כמספר ההקצאות.",
       "promptHtml": "כמה קריאות ל-<code class=\"tok\" dir=\"ltr\">free</code> נדרשות כדי לשחרר מטריצה דינמית עם 5 שורות?",
       "explainHtml": "כל שורה משוחררת בנפרד (5 קריאות) ועוד מערך המצביעים עצמו: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>5</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">5 + 1 = 6</annotation></semantics></math></span>, בדיוק כמספר ההקצאות."
      },
      "recap": "כל `calloc` מקבל `free`: $r + 1$ שחרורים.",
      "recapHtml": "כל <code class=\"tok\" dir=\"ltr\">calloc</code> מקבל <code class=\"tok\" dir=\"ltr\">free</code>: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>r</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">r + 1</annotation></semantics></math></span> שחרורים."
     },
     {
      "id": "C03-Q2",
      "step": {
       "type": "order",
       "prompt": "סדרו את הפקודות כך שהמטריצה תשוחרר נכון: קודם השורות ואחר כך מערך המצביעים.",
       "code": true,
       "lines": [
        "int i, **m = alloc_matrix(3, 2);",
        "for (i = 0; i < 3; i++)\n        free(m[i]);",
        "free(m);"
       ],
       "explain": "אם משחררים את `m` לפני השורות, כתובות השורות (`m[i]`) אבדו ואי אפשר לשחרר אותן אחרי כן באופן חוקי. הסדר הנכון הוא שורות ואז `m`.",
       "promptHtml": "סדרו את הפקודות כך שהמטריצה תשוחרר נכון: קודם השורות ואחר כך מערך המצביעים.",
       "explainHtml": "אם משחררים את <code class=\"tok\" dir=\"ltr\">m</code> לפני השורות, כתובות השורות (<code class=\"tok\" dir=\"ltr\">m[i]</code>) אבדו ואי אפשר לשחרר אותן אחרי כן באופן חוקי. הסדר הנכון הוא שורות ואז <code class=\"tok\" dir=\"ltr\">m</code>.",
       "linesHtml": [
        "int i, **m = alloc_matrix(3, 2);",
        "for (i = 0; i &lt; 3; i++)\n        free(m[i]);",
        "free(m);"
       ]
      },
      "recap": "קודם השורות, אחר כך המערך החיצוני.",
      "recapHtml": "קודם השורות, אחר כך המערך החיצוני."
     },
     {
      "id": "C03-Q3",
      "question": "בסוף התוכנית הבאה, כמה בלוקים שהוקצו נשארו בלי שחרור (דליפה)?\n```c\nint **alloc_matrix(int rows, int cols)\n{\n    int i;\n    int **m = (int **)calloc(rows, sizeof(int *));\n    for (i = 0; i < rows; i++)\n        m[i] = (int *)calloc(cols, sizeof(int));\n    return m;\n}\n\nint main(void)\n{\n    int **m = alloc_matrix(3, 4);\n    free(m);\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       },
       {
        "id": "b",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "c",
        "value": "`3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3</code>"
       },
       {
        "id": "d",
        "value": "`4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4</code>"
       }
      ],
      "correctId": "c",
      "explanation": "הוקצו 4 בלוקים: מערך המצביעים ו-3 שורות. שוחרר רק מערך המצביעים, ולכן 3 שורות דלפו. התשובה 4 שוכחת שאחד מהם שוחרר, ו-1 סופרת רק את המערך החיצוני.",
      "recap": "`free(m)` לבד משחרר רק את מערך המצביעים; השורות דולפות.",
      "questionHtml": "בסוף התוכנית הבאה, כמה בלוקים שהוקצו נשארו בלי שחרור (דליפה)?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int **alloc_matrix(int rows, int cols)\n{\n    int i;\n    int **m = (int **)calloc(rows, sizeof(int *));\n    for (i = 0; i &lt; rows; i++)\n        m[i] = (int *)calloc(cols, sizeof(int));\n    return m;\n}\n\nint main(void)\n{\n    int **m = alloc_matrix(3, 4);\n    free(m);\n    return 0;\n}</code></pre>",
      "explanationHtml": "הוקצו 4 בלוקים: מערך המצביעים ו-3 שורות. שוחרר רק מערך המצביעים, ולכן 3 שורות דלפו. התשובה 4 שוכחת שאחד מהם שוחרר, ו-1 סופרת רק את המערך החיצוני.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">free(m)</code> לבד משחרר רק את מערך המצביעים; השורות דולפות."
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "findbug",
       "prompt": "הפונקציה אמורה לשחרר את כל המטריצה בלי דליפות, אבל שורה אחת נשארת. מצאו את השורה השגויה.",
       "code": true,
       "lines": [
        "void free_matrix(int **m, int rows)",
        "{",
        "    int i;",
        "    for (i = 1; i < rows; i++)",
        "        free(m[i]);",
        "    free(m);",
        "}"
       ],
       "bugIndex": 3,
       "explain": "הלולאה מתחילה מ-`i = 1` ולכן שורה 0 לא משוחררת. אינדקסים בלולאה על שורות מתחילים מ-0.",
       "promptHtml": "הפונקציה אמורה לשחרר את כל המטריצה בלי דליפות, אבל שורה אחת נשארת. מצאו את השורה השגויה.",
       "explainHtml": "הלולאה מתחילה מ-<code class=\"tok\" dir=\"ltr\">i = 1</code> ולכן שורה 0 לא משוחררת. אינדקסים בלולאה על שורות מתחילים מ-0.",
       "linesHtml": [
        "void free_matrix(int **m, int rows)",
        "{",
        "    int i;",
        "    for (i = 1; i &lt; rows; i++)",
        "        free(m[i]);",
        "    free(m);",
        "}"
       ]
      },
      "recap": "לולאה על שורות: `i` מ-0 עד `rows - 1`.",
      "recapHtml": "לולאה על שורות: <code class=\"tok\" dir=\"ltr\">i</code> מ-0 עד <code class=\"tok\" dir=\"ltr\">rows - 1</code>."
     },
     {
      "id": "C03-Q5",
      "question": "מה קורה בקוד הבא?\n```c\nint main(void)\n{\n    int *p = NULL;\n    free(p);\n    printf(\"A\");\n    free(p);\n    printf(\"B\");\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`AB`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">AB</code>"
       },
       {
        "id": "b",
        "value": "`A`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">A</code>"
       },
       {
        "id": "c",
        "value": "קריסה לפני כל פלט",
        "type": "text",
        "html": "קריסה לפני כל פלט"
       },
       {
        "id": "d",
        "value": "שגיאת הידור",
        "type": "text",
        "html": "שגיאת הידור"
       }
      ],
      "correctId": "a",
      "explanation": "`free(NULL)` מוגדר היטב ולא עושה כלום, גם פעמיים. לכן מודפס `AB`. לא קורסים ולא מקבלים שגיאת הידור. (`free` כפול על כתובת שאינה NULL הוא כבר באג.)",
      "recap": "`free(NULL)` בטוח ולא עושה כלום.",
      "questionHtml": "מה קורה בקוד הבא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int main(void)\n{\n    int *p = NULL;\n    free(p);\n    printf(\"A\");\n    free(p);\n    printf(\"B\");\n    return 0;\n}</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">free(NULL)</code> מוגדר היטב ולא עושה כלום, גם פעמיים. לכן מודפס <code class=\"tok\" dir=\"ltr\">AB</code>. לא קורסים ולא מקבלים שגיאת הידור. (<code class=\"tok\" dir=\"ltr\">free</code> כפול על כתובת שאינה NULL הוא כבר באג.)",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">free(NULL)</code> בטוח ולא עושה כלום."
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "📋",
    "title": "מטריצה סטטית לדינמית",
    "goal": "אחרי השלב הזה אפשר להעתיק מטריצה סטטית A[][N] למטריצה דינמית חדשה ולהבחין בין int A[][N] ל-int **.",
    "source": "ai-verified",
    "boss": false,
    "goalHtml": "אחרי השלב הזה אפשר להעתיק מטריצה סטטית A[][N] למטריצה דינמית חדשה ולהבחין בין int A[][N] ל-int **.",
    "lesson": {
     "html": "\n    <p>במבחן הקלט הוא לעיתים מטריצה <b>סטטית</b> והפלט מבנה <b>דינמי</b>. הפרמטר הסטטי נכתב עם קבוע עמודות:</p>\n    <pre><code>#define N 3\nint **copy_matrix(int A[][N], int n);</code></pre>\n    <ul>\n      <li><code>int A[][N]</code> הוא מצביע לשורה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>N</mi></mrow><annotation encoding=\"application/x-tex\">N</annotation></semantics></math></span> מספרים. מעבירים לו מערך כמו <code>int S[3][3]</code>.</li>\n      <li><code>int **m</code> הוא מערך מצביעים, <b>טיפוס אחר</b>: לא מעבירים אחד במקום השני.</li>\n      <li>הפלט הדינמי נבנה בנפרד (<code>calloc</code>), מועתק מהקלט, ומוחזר ב-<code>return</code>. ההעתק עצמאי מהמקור.</li>\n      <li>תא שלא כותבים אליו נשאר 0, כי <code>calloc</code> מאפס.</li>\n    </ul>\n    <pre><code>#define N 3\nint **copy_matrix(int A[][N], int n)\n{\n    int i, j;\n    int **B = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i &lt; n; i++)\n    {\n        B[i] = (int *)calloc(n, sizeof(int));\n        for (j = 0; j &lt; n; j++)\n            B[i][j] = A[i][j];\n    }\n    return B;\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 העתקה: מקצים מטריצה חדשה בגודל המתאים, ואז <code>B[i][j] = A[i][j]</code> בלולאה כפולה.</div>\n    <div class=\"lesson-ex\">דוגמה: אחרי <code>B = copy_matrix(A, 3)</code>, השינוי <code>B[0][0] = 9</code> לא משנה את <code>A[0][0]</code>.</div>\n    <div class=\"lesson-trap\">⚠️ מערך סטטי שהועבר לפונקציה לא משחררים עם <code>free</code>: הוא לא הוקצה ב-<code>calloc</code>.</div>"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "question": "הפונקציה `int sum(int A[][N], int n)` מקבלת מטריצה סטטית (`N` קבוע). יש `int S[3][3]` ו-`int **m` (מטריצה דינמית). איזו קריאה תקינה?",
      "options": [
       {
        "id": "a",
        "value": "`sum(S, 3)`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sum(S, 3)</code>"
       },
       {
        "id": "b",
        "value": "`sum(m, 3)`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sum(m, 3)</code>"
       },
       {
        "id": "c",
        "value": "`sum(&m, 3)`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sum(&amp;m, 3)</code>"
       },
       {
        "id": "d",
        "value": "`sum(*m, 3)`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">sum(*m, 3)</code>"
       }
      ],
      "correctId": "a",
      "explanation": "הפרמטר `int A[][N]` הוא מצביע לשורה של $N$ מספרים, וזה מה שמתקבל משם של מערך דו-ממדי סטטי. `int **m` הוא מערך מצביעים, טיפוס אחר: ההידור נכשל או מתקבלת אזהרה, ואם מריצים, הקריאה מפרשת מצביעים כמספרים. גם `&m` וגם `*m` אינם מצביע-לשורה.",
      "recap": "`int A[][N]` לא שווה ל-`int **`. סטטי ודינמי אינם ניתנים להחלפה.",
      "questionHtml": "הפונקציה <code class=\"tok\" dir=\"ltr\">int sum(int A[][N], int n)</code> מקבלת מטריצה סטטית (<code class=\"tok\" dir=\"ltr\">N</code> קבוע). יש <code class=\"tok\" dir=\"ltr\">int S[3][3]</code> ו-<code class=\"tok\" dir=\"ltr\">int **m</code> (מטריצה דינמית). איזו קריאה תקינה?",
      "explanationHtml": "הפרמטר <code class=\"tok\" dir=\"ltr\">int A[][N]</code> הוא מצביע לשורה של <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>N</mi></mrow><annotation encoding=\"application/x-tex\">N</annotation></semantics></math></span> מספרים, וזה מה שמתקבל משם של מערך דו-ממדי סטטי. <code class=\"tok\" dir=\"ltr\">int **m</code> הוא מערך מצביעים, טיפוס אחר: ההידור נכשל או מתקבלת אזהרה, ואם מריצים, הקריאה מפרשת מצביעים כמספרים. גם <code class=\"tok\" dir=\"ltr\">&amp;m</code> וגם <code class=\"tok\" dir=\"ltr\">*m</code> אינם מצביע-לשורה.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">int A[][N]</code> לא שווה ל-<code class=\"tok\" dir=\"ltr\">int **</code>. סטטי ודינמי אינם ניתנים להחלפה."
     },
     {
      "id": "C04-Q2",
      "question": "מה מדפיס הקוד?\n```c\n#define N 2\nint **copy_matrix(int A[][N], int n)\n{\n    int i, j;\n    int **B = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i < n; i++)\n    {\n        B[i] = (int *)calloc(n, sizeof(int));\n        for (j = 0; j < n; j++)\n            B[i][j] = A[i][j];\n    }\n    return B;\n}\n\nint main(void)\n{\n    int A[2][2] = {{1, 2}, {3, 4}};\n    int **B = copy_matrix(A, 2);\n    B[0][0] = 9;\n    printf(\"%d %d\", A[0][0], B[0][0]);\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`9 9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 9</code>"
       },
       {
        "id": "b",
        "value": "`1 9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 9</code>"
       },
       {
        "id": "c",
        "value": "`1 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 1</code>"
       },
       {
        "id": "d",
        "value": "`9 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 1</code>"
       }
      ],
      "correctId": "b",
      "explanation": "`copy_matrix` בונה מטריצה דינמית חדשה ומעתיקה אליה ערכים. שינוי `B[0][0]` משנה רק את ההעתק, ולכן `A[0][0]` נשאר 1 ו-`B[0][0]` הוא 9. תשובות אחרות מניחות שהמטריצות חולקות זיכרון.",
      "recap": "ההעתק עצמאי: שינוי בו לא משנה את המקור.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#define N 2\nint **copy_matrix(int A[][N], int n)\n{\n    int i, j;\n    int **B = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i &lt; n; i++)\n    {\n        B[i] = (int *)calloc(n, sizeof(int));\n        for (j = 0; j &lt; n; j++)\n            B[i][j] = A[i][j];\n    }\n    return B;\n}\n\nint main(void)\n{\n    int A[2][2] = {{1, 2}, {3, 4}};\n    int **B = copy_matrix(A, 2);\n    B[0][0] = 9;\n    printf(\"%d %d\", A[0][0], B[0][0]);\n    return 0;\n}</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">copy_matrix</code> בונה מטריצה דינמית חדשה ומעתיקה אליה ערכים. שינוי <code class=\"tok\" dir=\"ltr\">B[0][0]</code> משנה רק את ההעתק, ולכן <code class=\"tok\" dir=\"ltr\">A[0][0]</code> נשאר 1 ו-<code class=\"tok\" dir=\"ltr\">B[0][0]</code> הוא 9. תשובות אחרות מניחות שהמטריצות חולקות זיכרון.",
      "recapHtml": "ההעתק עצמאי: שינוי בו לא משנה את המקור."
     },
     {
      "id": "C04-Q3",
      "step": {
       "type": "fillblank",
       "prompt": "השלימו את השורה שמעתיקה איבר מהמטריצה הסטטית `A` להעתק `B`, כך ש-`B` זהה ל-`A`.",
       "code": true,
       "lines": [
        "int **copy_matrix(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **B = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i < n; i++)",
        "    {",
        "        B[i] = (int *)calloc(n, sizeof(int));",
        "        for (j = 0; j < n; j++)",
        "            B[i][j] = ___;",
        "    }",
        "    return B;",
        "}"
       ],
       "blankIndex": 8,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "A[i][j]",
         "html": "A[i][j]"
        },
        {
         "id": "b",
         "type": "text",
         "value": "A[j][i]",
         "html": "A[j][i]"
        },
        {
         "id": "c",
         "type": "text",
         "value": "A[i][j] * 2",
         "html": "A[i][j] * 2"
        },
        {
         "id": "d",
         "type": "text",
         "value": "A[i][j] + i",
         "html": "A[i][j] + i"
        }
       ],
       "correctId": "a",
       "explain": "ההעתק זהה למקור כשכל תא מועתק מאותו מקום: `A[i][j]`. `A[j][i]` משחלף, והאחרות משנות את הערך.",
       "promptHtml": "השלימו את השורה שמעתיקה איבר מהמטריצה הסטטית <code class=\"tok\" dir=\"ltr\">A</code> להעתק <code class=\"tok\" dir=\"ltr\">B</code>, כך ש-<code class=\"tok\" dir=\"ltr\">B</code> זהה ל-<code class=\"tok\" dir=\"ltr\">A</code>.",
       "explainHtml": "ההעתק זהה למקור כשכל תא מועתק מאותו מקום: <code class=\"tok\" dir=\"ltr\">A[i][j]</code>. <code class=\"tok\" dir=\"ltr\">A[j][i]</code> משחלף, והאחרות משנות את הערך.",
       "linesHtml": [
        "int **copy_matrix(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **B = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i &lt; n; i++)",
        "    {",
        "        B[i] = (int *)calloc(n, sizeof(int));",
        "        for (j = 0; j &lt; n; j++)",
        "            B[i][j] = ___;",
        "    }",
        "    return B;",
        "}"
       ]
      },
      "recap": "העתקה: `B[i][j] = A[i][j]`.",
      "recapHtml": "העתקה: <code class=\"tok\" dir=\"ltr\">B[i][j] = A[i][j]</code>."
     },
     {
      "id": "C04-Q4",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד הבא?\n```c\nint main(void)\n{\n    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    int **B = (int **)calloc(3, sizeof(int *));\n    int i, j, s = 0;\n    for (i = 0; i < 3; i++)\n    {\n        B[i] = (int *)calloc(3, sizeof(int));\n        for (j = 0; j <= i; j++)\n            B[i][j] = A[i][j];\n    }\n    for (i = 0; i < 3; i++)\n        for (j = 0; j < 3; j++)\n            s += B[i][j];\n    printf(\"%d\", s);\n    return 0;\n}\n```",
       "answer": 34,
       "tol": 0,
       "explain": "רק התאים עם $j \\le i$ מועתקים, והשאר נשארים אפס (`calloc`): $1 + 4 + 5 + 7 + 8 + 9 = 34$. האיברים $2, 3, 6$ מעל האלכסון לא נכנסים.",
       "promptHtml": "מה מדפיס הקוד הבא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int main(void)\n{\n    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    int **B = (int **)calloc(3, sizeof(int *));\n    int i, j, s = 0;\n    for (i = 0; i &lt; 3; i++)\n    {\n        B[i] = (int *)calloc(3, sizeof(int));\n        for (j = 0; j &lt;= i; j++)\n            B[i][j] = A[i][j];\n    }\n    for (i = 0; i &lt; 3; i++)\n        for (j = 0; j &lt; 3; j++)\n            s += B[i][j];\n    printf(\"%d\", s);\n    return 0;\n}</code></pre>",
       "explainHtml": "רק התאים עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi><mo>≤</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">j \\le i</annotation></semantics></math></span> מועתקים, והשאר נשארים אפס (<code class=\"tok\" dir=\"ltr\">calloc</code>): <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>7</mn><mo>+</mo><mn>8</mn><mo>+</mo><mn>9</mn><mo>=</mo><mn>34</mn></mrow><annotation encoding=\"application/x-tex\">1 + 4 + 5 + 7 + 8 + 9 = 34</annotation></semantics></math></span>. האיברים <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo separator=\"true\">,</mo><mn>3</mn><mo separator=\"true\">,</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">2, 3, 6</annotation></semantics></math></span> מעל האלכסון לא נכנסים."
      },
      "recap": "תא שלא הועתק נשאר 0.",
      "recapHtml": "תא שלא הועתק נשאר 0."
     },
     {
      "id": "C04-Q5",
      "step": {
       "type": "order",
       "prompt": "סדרו את גוף `copy_matrix`, שמשתמשת ב-`alloc_matrix` שכבר כתובה: להקצות, להעתיק, להחזיר.",
       "code": true,
       "lines": [
        "int **B = alloc_matrix(n, n);",
        "for (i = 0; i < n; i++) for (j = 0; j < n; j++) B[i][j] = A[i][j];",
        "return B;"
       ],
       "explain": "קודם מקצים את `B` (אחרת אין לאן להעתיק), אחר כך מעתיקים, ורק אז מחזירים. `return` לפני ההעתקה מחזיר מטריצה מאופסת.",
       "promptHtml": "סדרו את גוף <code class=\"tok\" dir=\"ltr\">copy_matrix</code>, שמשתמשת ב-<code class=\"tok\" dir=\"ltr\">alloc_matrix</code> שכבר כתובה: להקצות, להעתיק, להחזיר.",
       "explainHtml": "קודם מקצים את <code class=\"tok\" dir=\"ltr\">B</code> (אחרת אין לאן להעתיק), אחר כך מעתיקים, ורק אז מחזירים. <code class=\"tok\" dir=\"ltr\">return</code> לפני ההעתקה מחזיר מטריצה מאופסת.",
       "linesHtml": [
        "int **B = alloc_matrix(n, n);",
        "for (i = 0; i &lt; n; i++) for (j = 0; j &lt; n; j++) B[i][j] = A[i][j];",
        "return B;"
       ]
      },
      "recap": "הקצאה, העתקה, `return`.",
      "recapHtml": "הקצאה, העתקה, <code class=\"tok\" dir=\"ltr\">return</code>."
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "📐",
    "title": "מערך משונן: משולשים",
    "goal": "אחרי השלב הזה אפשר להקצות משולש תחתון או עליון עם שורות באורכים שונים ולחשב אורכי שורות ואינדקסים.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>שורות המטריצה הדינמית יכולות להיות <b>באורכים שונים</b>: מערך משונן (jagged). כך חוסכים זיכרון כשצריך רק חלק מהמטריצה, והמבחן אוהב את זה.</p>\n    <pre><code>#define N 4\nint **low_triangle(int A[][N], int n)\n{\n    int i, j;\n    int **low = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i &lt; n; i++)\n    {\n        low[i] = (int *)calloc(i + 1, sizeof(int));\n        for (j = 0; j &lt;= i; j++)\n            low[i][j] = A[i][j];\n    }\n    return low;\n}</code></pre>\n    <ul>\n      <li><b>משולש תחתון</b> (כולל האלכסון): שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> מכילה את <code>A[i][0..i]</code>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">i+1</annotation></semantics></math></span> איברים. סך הכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mi>n</mi><mo stretchy=\"false\">(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{n(n+1)}{2}</annotation></semantics></math></span>.</li>\n      <li><b>משולש עליון ממש</b> (בלי האלכסון): שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> מכילה את <code>A[i][i+1..n-1]</code>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">n-1-i</annotation></semantics></math></span> איברים. הערך <code>A[i][j]</code> נשמר באינדקס <code>j - i - 1</code>.</li>\n      <li>השורה האחרונה במשולש העליון ריקה (אורך 0), ו-<code>calloc(0, ...)</code> תלוי במימוש. בשאלה אמיתית קראו כמה איברים יש בכל שורה.</li>\n    </ul>\n    <pre><code>#define N 4\nint **strict_upper(int A[][N], int n)\n{\n    int i, j;\n    int **up = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i &lt; n; i++)\n    {\n        up[i] = (int *)calloc(n - 1 - i, sizeof(int));\n        for (j = i + 1; j &lt; n; j++)\n            up[i][j - i - 1] = A[i][j];\n    }\n    return up;\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 לפני שכותבים קוד: רשמו אורך כל שורה ונוסחה של אינדקס מקור מול אינדקס יעד. אחר כך הקצו שורה בגודל הנכון והעתיקו.</div>\n    <div class=\"lesson-ex\">דוגמה: עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">n = 4</annotation></semantics></math></span> אורכי השורות במשולש העליון הם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo separator=\"true\">,</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">3, 2, 1, 0</annotation></semantics></math></span>. האיבר <code>A[1][3]</code> נשמר ב-<code>up[1][1]</code> כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>−</mo><mn>1</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">3 - 1 - 1 = 1</annotation></semantics></math></span>.</div>\n    <div class=\"lesson-trap\">⚠️ <code>up[i][j]</code> במקום <code>up[i][j - i - 1]</code> כותב מחוץ לגבולות השורה הקצרה.</div>"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "step": {
       "type": "numeric",
       "prompt": "כמה איברים נשמרים בסך הכל במשולש התחתון (כולל האלכסון) של מטריצה 6 על 6, כששורה $i$ מקבלת $i+1$ איברים?",
       "answer": 21,
       "tol": 0,
       "explain": "$1 + 2 + 3 + 4 + 5 + 6 = 21$, כלומר $\\frac{6 \\cdot 7}{2}$. זה חצי ממטריצה מלאה (36), בלי מקום מבוזבז.",
       "promptHtml": "כמה איברים נשמרים בסך הכל במשולש התחתון (כולל האלכסון) של מטריצה 6 על 6, כששורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> מקבלת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">i+1</annotation></semantics></math></span> איברים?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>6</mn><mo>=</mo><mn>21</mn></mrow><annotation encoding=\"application/x-tex\">1 + 2 + 3 + 4 + 5 + 6 = 21</annotation></semantics></math></span>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mn>6</mn><mo>⋅</mo><mn>7</mn></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{6 \\cdot 7}{2}</annotation></semantics></math></span>. זה חצי ממטריצה מלאה (36), בלי מקום מבוזבז."
      },
      "recap": "משולש עם $n$ שורות: $\\frac{n(n+1)}{2}$ איברים.",
      "recapHtml": "משולש עם <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> שורות: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mfrac><mrow><mi>n</mi><mo stretchy=\"false\">(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><mn>2</mn></mfrac></mrow><annotation encoding=\"application/x-tex\">\\frac{n(n+1)}{2}</annotation></semantics></math></span> איברים."
     },
     {
      "id": "C05-Q2",
      "question": "ב-`strict_upper` למטריצה 4 על 4 (המשולש שמעל האלכסון, בלי האלכסון), מה אורכי השורות `up[0]` עד `up[3]`?",
      "options": [
       {
        "id": "a",
        "value": "`3 2 1 0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 2 1 0</code>"
       },
       {
        "id": "b",
        "value": "`4 3 2 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 3 2 1</code>"
       },
       {
        "id": "c",
        "value": "`3 3 3 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 3 3 3</code>"
       },
       {
        "id": "d",
        "value": "`1 2 3 4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3 4</code>"
       }
      ],
      "correctId": "a",
      "explanation": "שורה $i$ מכילה את `A[i][i+1..n-1]`, כלומר $n-1-i$ איברים: $3, 2, 1, 0$. הרצף `4 3 2 1` כולל את האלכסון, `1 2 3 4` הפוך, ו-`3 3 3 3` שומר מקום מבוזבז.",
      "recap": "משולש עליון ממש: שורה $i$ באורך $n-1-i$.",
      "questionHtml": "ב-<code class=\"tok\" dir=\"ltr\">strict_upper</code> למטריצה 4 על 4 (המשולש שמעל האלכסון, בלי האלכסון), מה אורכי השורות <code class=\"tok\" dir=\"ltr\">up[0]</code> עד <code class=\"tok\" dir=\"ltr\">up[3]</code>?",
      "explanationHtml": "שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> מכילה את <code class=\"tok\" dir=\"ltr\">A[i][i+1..n-1]</code>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">n-1-i</annotation></semantics></math></span> איברים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo separator=\"true\">,</mo><mn>2</mn><mo separator=\"true\">,</mo><mn>1</mn><mo separator=\"true\">,</mo><mn>0</mn></mrow><annotation encoding=\"application/x-tex\">3, 2, 1, 0</annotation></semantics></math></span>. הרצף <code class=\"tok\" dir=\"ltr\">4 3 2 1</code> כולל את האלכסון, <code class=\"tok\" dir=\"ltr\">1 2 3 4</code> הפוך, ו-<code class=\"tok\" dir=\"ltr\">3 3 3 3</code> שומר מקום מבוזבז.",
      "recapHtml": "משולש עליון ממש: שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> באורך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">n-1-i</annotation></semantics></math></span>."
     },
     {
      "id": "C05-Q3",
      "step": {
       "type": "numeric",
       "prompt": "ב-`strict_upper` נשמר האיבר `A[i][j]` (עבור $j > i$) בתא `up[i][j - i - 1]`. באיזה אינדקס בתוך `up[1]` נשמר `A[1][3]`?",
       "answer": 1,
       "tol": 0,
       "explain": "$j - i - 1 = 3 - 1 - 1 = 1$. השורה `up[1]` מחזיקה את `A[1][2]` באינדקס 0 ואת `A[1][3]` באינדקס 1.",
       "promptHtml": "ב-<code class=\"tok\" dir=\"ltr\">strict_upper</code> נשמר האיבר <code class=\"tok\" dir=\"ltr\">A[i][j]</code> (עבור <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi><mo>&gt;</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">j &gt; i</annotation></semantics></math></span>) בתא <code class=\"tok\" dir=\"ltr\">up[i][j - i - 1]</code>. באיזה אינדקס בתוך <code class=\"tok\" dir=\"ltr\">up[1]</code> נשמר <code class=\"tok\" dir=\"ltr\">A[1][3]</code>?",
       "explainHtml": "<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi><mo>−</mo><mi>i</mi><mo>−</mo><mn>1</mn><mo>=</mo><mn>3</mn><mo>−</mo><mn>1</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">j - i - 1 = 3 - 1 - 1 = 1</annotation></semantics></math></span>. השורה <code class=\"tok\" dir=\"ltr\">up[1]</code> מחזיקה את <code class=\"tok\" dir=\"ltr\">A[1][2]</code> באינדקס 0 ואת <code class=\"tok\" dir=\"ltr\">A[1][3]</code> באינדקס 1."
      },
      "recap": "אינדקס בתוך שורת המשולש העליון: $j - i - 1$.",
      "recapHtml": "אינדקס בתוך שורת המשולש העליון: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi><mo>−</mo><mi>i</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">j - i - 1</annotation></semantics></math></span>."
     },
     {
      "id": "C05-Q4",
      "step": {
       "type": "fillblank",
       "prompt": "השלימו את אורך השורה `i` במשולש התחתון (עם האלכסון).",
       "code": true,
       "lines": [
        "#define N 4",
        "int **low_triangle(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **low = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i < n; i++)",
        "    {",
        "        low[i] = (int *)calloc(___, sizeof(int));",
        "        for (j = 0; j <= i; j++)",
        "            low[i][j] = A[i][j];",
        "    }",
        "    return low;",
        "}"
       ],
       "blankIndex": 7,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "i + 1",
         "html": "i + 1"
        },
        {
         "id": "b",
         "type": "text",
         "value": "i",
         "html": "i"
        },
        {
         "id": "c",
         "type": "text",
         "value": "n",
         "html": "n"
        },
        {
         "id": "d",
         "type": "text",
         "value": "n - i",
         "html": "n - i"
        }
       ],
       "correctId": "a",
       "explain": "שורה $i$ מכילה את `A[i][0..i]`, כלומר $i+1$ איברים. עם `i` הלולאה `j <= i` כותבת איבר אחד מעבר לסוף. עם `n` כל השורות ארוכות (בזבוז), ועם `n - i` המשולש הפוך.",
       "promptHtml": "השלימו את אורך השורה <code class=\"tok\" dir=\"ltr\">i</code> במשולש התחתון (עם האלכסון).",
       "explainHtml": "שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> מכילה את <code class=\"tok\" dir=\"ltr\">A[i][0..i]</code>, כלומר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">i+1</annotation></semantics></math></span> איברים. עם <code class=\"tok\" dir=\"ltr\">i</code> הלולאה <code class=\"tok\" dir=\"ltr\">j &lt;= i</code> כותבת איבר אחד מעבר לסוף. עם <code class=\"tok\" dir=\"ltr\">n</code> כל השורות ארוכות (בזבוז), ועם <code class=\"tok\" dir=\"ltr\">n - i</code> המשולש הפוך.",
       "linesHtml": [
        "#define N 4",
        "int **low_triangle(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **low = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i &lt; n; i++)",
        "    {",
        "        low[i] = (int *)calloc(___, sizeof(int));",
        "        for (j = 0; j &lt;= i; j++)",
        "            low[i][j] = A[i][j];",
        "    }",
        "    return low;",
        "}"
       ]
      },
      "recap": "משולש תחתון: שורה $i$ באורך $i+1$.",
      "recapHtml": "משולש תחתון: שורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> באורך <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi><mo>+</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">i+1</annotation></semantics></math></span>."
     },
     {
      "id": "C05-Q5",
      "step": {
       "type": "findbug",
       "prompt": "הפונקציה אמורה לשמור בשורה $i$ את `A[i][i+1..n-1]` החל מאינדקס 0, אבל התוצאה שגויה. מצאו את השורה השגויה.",
       "code": true,
       "lines": [
        "#define N 4",
        "int **strict_upper(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **up = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i < n; i++)",
        "    {",
        "        up[i] = (int *)calloc(n - 1 - i, sizeof(int));",
        "        for (j = i + 1; j < n; j++)",
        "            up[i][j] = A[i][j];",
        "    }",
        "    return up;",
        "}"
       ],
       "bugIndex": 9,
       "explain": "השורה `up[i]` קצרה ($n-1-i$ איברים), ואינדקס `j` הולך עד $n-1$. הכתיבה ל-`up[i][j]` חורגת מהגבולות ומשאירה את התא הראשון ריק. האינדקס הנכון הוא `j - i - 1`.",
       "promptHtml": "הפונקציה אמורה לשמור בשורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> את <code class=\"tok\" dir=\"ltr\">A[i][i+1..n-1]</code> החל מאינדקס 0, אבל התוצאה שגויה. מצאו את השורה השגויה.",
       "explainHtml": "השורה <code class=\"tok\" dir=\"ltr\">up[i]</code> קצרה (<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">n-1-i</annotation></semantics></math></span> איברים), ואינדקס <code class=\"tok\" dir=\"ltr\">j</code> הולך עד <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">n-1</annotation></semantics></math></span>. הכתיבה ל-<code class=\"tok\" dir=\"ltr\">up[i][j]</code> חורגת מהגבולות ומשאירה את התא הראשון ריק. האינדקס הנכון הוא <code class=\"tok\" dir=\"ltr\">j - i - 1</code>.",
       "linesHtml": [
        "#define N 4",
        "int **strict_upper(int A[][N], int n)",
        "{",
        "    int i, j;",
        "    int **up = (int **)calloc(n, sizeof(int *));",
        "    for (i = 0; i &lt; n; i++)",
        "    {",
        "        up[i] = (int *)calloc(n - 1 - i, sizeof(int));",
        "        for (j = i + 1; j &lt; n; j++)",
        "            up[i][j] = A[i][j];",
        "    }",
        "    return up;",
        "}"
       ]
      },
      "recap": "מקור בעמודה $j$ הולך ליעד $j - i - 1$.",
      "recapHtml": "מקור בעמודה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi></mrow><annotation encoding=\"application/x-tex\">j</annotation></semantics></math></span> הולך ליעד <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>j</mi><mo>−</mo><mi>i</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">j - i - 1</annotation></semantics></math></span>."
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "🔁",
    "title": "החזרה by reference: ***out ו-*size",
    "goal": "אחרי השלב הזה אפשר להחזיר מערך או מטריצה וגם גודל דרך פרמטרים, עם הכתובות והסוגריים הנכונים.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>פונקציה יכולה להחזיר ב-<code>return</code> רק דבר אחד. כשצריך שניים (מבנה וגם גודל), את השני מעבירים <b>by reference</b>: הקורא שולח <b>כתובת</b> של משתנה, והפונקציה כותבת דרכה.</p>\n    <ul>\n      <li>כדי להחזיר מערך (<code>int *</code>) דרך פרמטר, הפרמטר הוא <code>int **out</code> והקריאה שולחת <code>&amp;a</code>. כדי להחזיר מטריצה (<code>int **</code>) הפרמטר הוא <code>int ***out</code>.</li>\n      <li>כותבים <code>*out = ...</code> כדי לשנות את המשתנה של הקורא. <code>out = ...</code> משנה רק עותק מקומי.</li>\n      <li>איבר במערך המוחזר: <code>(*out)[k]</code>. הסוגריים חובה: <code>*out[k]</code> פירושו <code>*(out[k])</code>.</li>\n      <li>גודל: <code>int *cnt</code>, והעלאה כ-<code>(*cnt)++</code> (בלי סוגריים, <code>*cnt++</code> מקדם את המצביע עצמו).</li>\n    </ul>\n    <pre><code>void evens(int *A, int n, int **out, int *cnt)\n{\n    int i, k;\n    *cnt = 0;\n    for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;\n    *out = (int *)calloc(*cnt, sizeof(int));\n    k = 0;\n    for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 פרמטר פלט מסוג <code>T</code> מוגדר <code>T *p</code>, נכתב <code>*p = ...</code>, ומועבר בקריאה כ-<code>&amp;x</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: הקורא כותב <code>int *a; int c; evens(A, 5, &amp;a, &amp;c);</code>. אחרי הקריאה <code>a</code> מצביע על המערך החדש ו-<code>c</code> מחזיק את אורכו.</div>\n    <div class=\"lesson-trap\">⚠️ <code>*cnt++</code> במקום <code>(*cnt)++</code>, ו-<code>*out[k]</code> במקום <code>(*out)[k]</code>: שתי טעויות סוגריים נפוצות.</div>"
    },
    "questions": [
     {
      "id": "C06-Q1",
      "question": "הפונקציה מחזירה את המשולש התחתון דרך הפרמטר `int ***out` (הקורא מעביר `&T` כש-`T` הוא `int **`). איזו פקודה במקום `___` מוסרת את התוצאה לקורא?\n```c\n#define N 3\nvoid low_triangle(int A[][N], int n, int ***out)\n{\n    int i, j;\n    int **low = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i < n; i++)\n    {\n        low[i] = (int *)calloc(i + 1, sizeof(int));\n        for (j = 0; j <= i; j++)\n            low[i][j] = A[i][j];\n    }\n    ___\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`*out = low;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">*out = low;</code>"
       },
       {
        "id": "b",
        "value": "`out = low;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">out = low;</code>"
       },
       {
        "id": "c",
        "value": "`**out = low;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">**out = low;</code>"
       },
       {
        "id": "d",
        "value": "`out[0] = *low;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">out[0] = *low;</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`out` הוא כתובת של משתנה `int **` אצל הקורא. כדי לשנות את אותו משתנה כותבים דרך הכתובת: `*out = low`. `out = low` משנה רק את העותק המקומי של הפרמטר (וגם הטיפוס לא תואם), ו-`**out = low` ו-`out[0] = *low` מערבבים רמות הפניה: ההידור נכשל.",
      "recap": "מחזירים דרך פרמטר `X *p` בכתיבה `*p = ...`. כאן `X` הוא `int **`.",
      "questionHtml": "הפונקציה מחזירה את המשולש התחתון דרך הפרמטר <code class=\"tok\" dir=\"ltr\">int <strong>*out</code> (הקורא מעביר <code class=\"tok\" dir=\"ltr\">&amp;T</code> כש-<code class=\"tok\" dir=\"ltr\">T</code> הוא <code class=\"tok\" dir=\"ltr\">int </strong></code>). איזו פקודה במקום <code class=\"tok\" dir=\"ltr\">___</code> מוסרת את התוצאה לקורא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#define N 3\nvoid low_triangle(int A[][N], int n, int ***out)\n{\n    int i, j;\n    int **low = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i &lt; n; i++)\n    {\n        low[i] = (int *)calloc(i + 1, sizeof(int));\n        for (j = 0; j &lt;= i; j++)\n            low[i][j] = A[i][j];\n    }\n    ___\n}</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">out</code> הוא כתובת של משתנה <code class=\"tok\" dir=\"ltr\">int <strong></code> אצל הקורא. כדי לשנות את אותו משתנה כותבים דרך הכתובת: <code class=\"tok\" dir=\"ltr\">*out = low</code>. <code class=\"tok\" dir=\"ltr\">out = low</code> משנה רק את העותק המקומי של הפרמטר (וגם הטיפוס לא תואם), ו-<code class=\"tok\" dir=\"ltr\"></strong>out = low</code> ו-<code class=\"tok\" dir=\"ltr\">out[0] = *low</code> מערבבים רמות הפניה: ההידור נכשל.",
      "recapHtml": "מחזירים דרך פרמטר <code class=\"tok\" dir=\"ltr\">X *p</code> בכתיבה <code class=\"tok\" dir=\"ltr\">*p = ...</code>. כאן <code class=\"tok\" dir=\"ltr\">X</code> הוא <code class=\"tok\" dir=\"ltr\">int **</code>."
     },
     {
      "id": "C06-Q2",
      "question": "מה מדפיס הקוד?\n```c\nvoid fill(int **out, int *cnt)\n{\n    *out = (int *)calloc(3, sizeof(int));\n    (*out)[0] = 4;\n    (*out)[2] = 9;\n    *cnt = 3;\n}\n\nint main(void)\n{\n    int *a;\n    int c;\n    fill(&a, &c);\n    printf(\"%d %d\", a[2], c);\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`9 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 3</code>"
       },
       {
        "id": "b",
        "value": "`4 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 3</code>"
       },
       {
        "id": "c",
        "value": "`9 9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 9</code>"
       },
       {
        "id": "d",
        "value": "`3 9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 9</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`fill` כותבת דרך `out` אל `a`, וגם דרך `cnt` אל `c`. אחרי הקריאה `a` מצביע על מערך `{4, 0, 9}` ו-`c` הוא 3, ולכן `a[2]` הוא 9 והפלט `9 3`. ב-`4 3` נבחר האיבר הראשון, ושתי האפשרויות האחרות מחליפות ערכים.",
      "recap": "`*out` הוא המצביע של הקורא; `(*out)[k]` הוא האיבר ה-`k` במערך שלו.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void fill(int **out, int *cnt)\n{\n    *out = (int *)calloc(3, sizeof(int));\n    (*out)[0] = 4;\n    (*out)[2] = 9;\n    *cnt = 3;\n}\n\nint main(void)\n{\n    int *a;\n    int c;\n    fill(&amp;a, &amp;c);\n    printf(\"%d %d\", a[2], c);\n    return 0;\n}</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fill</code> כותבת דרך <code class=\"tok\" dir=\"ltr\">out</code> אל <code class=\"tok\" dir=\"ltr\">a</code>, וגם דרך <code class=\"tok\" dir=\"ltr\">cnt</code> אל <code class=\"tok\" dir=\"ltr\">c</code>. אחרי הקריאה <code class=\"tok\" dir=\"ltr\">a</code> מצביע על מערך <code class=\"tok\" dir=\"ltr\">{4, 0, 9}</code> ו-<code class=\"tok\" dir=\"ltr\">c</code> הוא 3, ולכן <code class=\"tok\" dir=\"ltr\">a[2]</code> הוא 9 והפלט <code class=\"tok\" dir=\"ltr\">9 3</code>. ב-<code class=\"tok\" dir=\"ltr\">4 3</code> נבחר האיבר הראשון, ושתי האפשרויות האחרות מחליפות ערכים.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">*out</code> הוא המצביע של הקורא; <code class=\"tok\" dir=\"ltr\">(*out)[k]</code> הוא האיבר ה-<code class=\"tok\" dir=\"ltr\">k</code> במערך שלו."
     },
     {
      "id": "C06-Q3",
      "step": {
       "type": "numeric",
       "prompt": "מה מדפיס הקוד?\n```c\nvoid evens(int *A, int n, int **out, int *cnt)\n{\n    int i, k;\n    *cnt = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;\n    *out = (int *)calloc(*cnt, sizeof(int));\n    k = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];\n}\n\nint main(void)\n{\n    int A[5] = {3, 4, 8, 5, 6};\n    int *a = NULL;\n    int c = 77;\n    evens(A, 5, &a, &c);\n    printf(\"%d\", c);\n    return 0;\n}\n```",
       "answer": 3,
       "tol": 0,
       "explain": "`evens` סופרת את הזוגיים (4, 8, 6) ושומרת 3 ב-`*cnt`. הערך ההתחלתי 77 נדרס בפקודה `*cnt = 0` בתחילת הפונקציה.",
       "promptHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void evens(int *A, int n, int **out, int *cnt)\n{\n    int i, k;\n    *cnt = 0;\n    for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;\n    *out = (int *)calloc(*cnt, sizeof(int));\n    k = 0;\n    for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];\n}\n\nint main(void)\n{\n    int A[5] = {3, 4, 8, 5, 6};\n    int *a = NULL;\n    int c = 77;\n    evens(A, 5, &amp;a, &amp;c);\n    printf(\"%d\", c);\n    return 0;\n}</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">evens</code> סופרת את הזוגיים (4, 8, 6) ושומרת 3 ב-<code class=\"tok\" dir=\"ltr\">*cnt</code>. הערך ההתחלתי 77 נדרס בפקודה <code class=\"tok\" dir=\"ltr\">*cnt = 0</code> בתחילת הפונקציה."
      },
      "recap": "ערך שמוחזר בפרמטר נקבע בתוך הפונקציה (`*cnt = ...`).",
      "recapHtml": "ערך שמוחזר בפרמטר נקבע בתוך הפונקציה (<code class=\"tok\" dir=\"ltr\">*cnt = ...</code>)."
     },
     {
      "id": "C06-Q4",
      "step": {
       "type": "order",
       "prompt": "סדרו את גוף `evens`: לאפס מונה, לספור זוגיים, להקצות בדיוק לפי המונה, ולמלא.",
       "code": true,
       "lines": [
        "*cnt = 0;",
        "for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;",
        "*out = (int *)calloc(*cnt, sizeof(int));",
        "k = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];"
       ],
       "explain": "המונה מתאפס קודם, אחר כך נספרים הזוגיים, רק אחר כך מקצים `*cnt` תאים (כך מקצים בדיוק), ובסוף ממלאים. מילוי לפני הקצאה כותב ל-NULL, והקצאה לפני הספירה מקצה לפי הערך הישן.",
       "promptHtml": "סדרו את גוף <code class=\"tok\" dir=\"ltr\">evens</code>: לאפס מונה, לספור זוגיים, להקצות בדיוק לפי המונה, ולמלא.",
       "explainHtml": "המונה מתאפס קודם, אחר כך נספרים הזוגיים, רק אחר כך מקצים <code class=\"tok\" dir=\"ltr\">*cnt</code> תאים (כך מקצים בדיוק), ובסוף ממלאים. מילוי לפני הקצאה כותב ל-NULL, והקצאה לפני הספירה מקצה לפי הערך הישן.",
       "linesHtml": [
        "*cnt = 0;",
        "for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;",
        "*out = (int *)calloc(*cnt, sizeof(int));",
        "k = 0;\n    for (i = 0; i &lt; n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];"
       ]
      },
      "recap": "מאפסים, סופרים, מקצים, ממלאים.",
      "recapHtml": "מאפסים, סופרים, מקצים, ממלאים."
     },
     {
      "id": "C06-Q5",
      "question": "הפונקציה `evens(int *A, int n, int **out, int *cnt)` מחזירה מערך דרך `out` וגודלו דרך `cnt`. הקורא הצהיר `int A[5]; int *a; int c;`. איזו קריאה נכונה?",
      "options": [
       {
        "id": "a",
        "value": "`evens(A, 5, &a, &c);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">evens(A, 5, &amp;a, &amp;c);</code>"
       },
       {
        "id": "b",
        "value": "`evens(A, 5, a, c);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">evens(A, 5, a, c);</code>"
       },
       {
        "id": "c",
        "value": "`evens(A, 5, &a, c);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">evens(A, 5, &amp;a, c);</code>"
       },
       {
        "id": "d",
        "value": "`evens(A, 5, *a, *c);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">evens(A, 5, *a, *c);</code>"
       }
      ],
      "correctId": "a",
      "explanation": "כדי שהפונקציה תשנה את `a` ואת `c` מעבירים את הכתובות שלהם: `&a` (מסוג `int **`) ו-`&c` (מסוג `int *`). העברת `a` ו-`c` עצמם, או `&a` עם `c`, או `*a` ו-`*c`, לא מתאימה לטיפוסים ולא משנה דבר אצל הקורא.",
      "recap": "פרמטר פלט: מעבירים `&משתנה`.",
      "questionHtml": "הפונקציה <code class=\"tok\" dir=\"ltr\">evens(int *A, int n, int **out, int *cnt)</code> מחזירה מערך דרך <code class=\"tok\" dir=\"ltr\">out</code> וגודלו דרך <code class=\"tok\" dir=\"ltr\">cnt</code>. הקורא הצהיר <code class=\"tok\" dir=\"ltr\">int A[5]; int *a; int c;</code>. איזו קריאה נכונה?",
      "explanationHtml": "כדי שהפונקציה תשנה את <code class=\"tok\" dir=\"ltr\">a</code> ואת <code class=\"tok\" dir=\"ltr\">c</code> מעבירים את הכתובות שלהם: <code class=\"tok\" dir=\"ltr\">&amp;a</code> (מסוג <code class=\"tok\" dir=\"ltr\">int **</code>) ו-<code class=\"tok\" dir=\"ltr\">&amp;c</code> (מסוג <code class=\"tok\" dir=\"ltr\">int *</code>). העברת <code class=\"tok\" dir=\"ltr\">a</code> ו-<code class=\"tok\" dir=\"ltr\">c</code> עצמם, או <code class=\"tok\" dir=\"ltr\">&amp;a</code> עם <code class=\"tok\" dir=\"ltr\">c</code>, או <code class=\"tok\" dir=\"ltr\">*a</code> ו-<code class=\"tok\" dir=\"ltr\">*c</code>, לא מתאימה לטיפוסים ולא משנה דבר אצל הקורא.",
      "recapHtml": "פרמטר פלט: מעבירים <code class=\"tok\" dir=\"ltr\">&amp;משתנה</code>."
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "🧮",
    "title": "מערך של מבנים ו-realloc",
    "goal": "אחרי השלב הזה אפשר לבנות מערך של struct {size, ptr}, למלא כל שורה ולהקטין אותה עם realloc.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>לפעמים כל שורה היא <b>מבנה</b> שמחזיק גם מערך דינמי וגם את גודלו, ומחזירים מערך של מבנים:</p>\n    <pre><code>typedef struct\n{\n    int size;\n    int *ptr;\n} dyn_array;</code></pre>\n    <ul>\n      <li><code>calloc(n, sizeof(dyn_array))</code> נותן לכל איבר <code>size = 0</code> ו-<code>ptr = NULL</code>, וזה מתאים לשורה ריקה.</li>\n      <li>גישה לשדות באיבר של מערך: <code>B[i].size</code> ו-<code>B[i].ptr[j]</code> (נקודה, כי <code>B[i]</code> הוא מבנה ולא מצביע).</li>\n      <li>גודל המבנה ב-64 סיביות הוא 16 בתים: <code>int</code> (4) + ריפוד (4) + מצביע (8).</li>\n      <li><b>הקטנה עם <code>realloc</code></b>: מקצים מערך זמני בגודל המרבי, ממלאים ומחשבים <code>k</code>, ואז <code>p = realloc(p, k * sizeof(int))</code>. הגודל בבתים.</li>\n      <li>אם <code>k == 0</code>, התנהגות <code>realloc(p, 0)</code> תלויה במימוש: עדיף <code>free(p)</code> ולהשאיר <code>NULL</code>.</li>\n    </ul>\n    <pre><code>dyn_array *div_numbers(const int *A, int sz, int n)\n{\n    int i, j, k = 0;\n    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));\n    for (i = 2; i &lt;= n; i++)\n    {\n        int *tmp = (int *)calloc(sz, sizeof(int));\n        for (j = 0, k = 0; j &lt; sz; j++)\n            if (A[j] % i == 0)\n                tmp[k++] = A[j];\n        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));\n        B[i - 2].size = k;\n    }\n    return B;\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 מערך מבנים: מקצים עם <code>calloc</code>, ממלאים כל איבר בנפרד, ומקטינים כל מערך פנימי עם <code>realloc</code> בגודל <code>k * sizeof(int)</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: עבור <code>A = {4, 6, 8, 9, 10, 12}</code> ו-<code>n = 4</code>: <code>B[0]</code> מחזיק את הזוגיים (5 איברים), <code>B[1]</code> את המתחלקים ב-3, ו-<code>B[2]</code> את המתחלקים ב-4.</div>\n    <div class=\"lesson-trap\">⚠️ <code>realloc(tmp, k)</code> בלי <code>sizeof</code> מקצה <code>k</code> בתים ולא <code>k</code> מספרים. ו-<code>malloc</code> במקום <code>calloc</code> משאיר <code>size</code> ו-<code>ptr</code> עם זבל בשורות שלא מילאתם.</div>"
    },
    "questions": [
     {
      "id": "C07-Q1",
      "question": "מה מדפיס הקוד?\n```c\ntypedef struct\n{\n    int size;\n    int *ptr;\n} dyn_array;\n\nint main(void)\n{\n    dyn_array *B = (dyn_array *)calloc(3, sizeof(dyn_array));\n    printf(\"%d %s\", B[1].size, B[1].ptr ? \"ptr\" : \"NULL\");\n    return 0;\n}\n```",
      "options": [
       {
        "id": "a",
        "value": "`0 NULL`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 NULL</code>"
       },
       {
        "id": "b",
        "value": "`0 ptr`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0 ptr</code>"
       },
       {
        "id": "c",
        "value": "`3 NULL`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 NULL</code>"
       },
       {
        "id": "d",
        "value": "ערכי זבל, התוצאה אינה צפויה",
        "type": "text",
        "html": "ערכי זבל, התוצאה אינה צפויה"
       }
      ],
      "correctId": "a",
      "explanation": "`calloc` מאפס את כל הבתים, ולכן בכל איבר `size` הוא 0 ו-`ptr` הוא `NULL`. זה בדיוק מה שמתאים לשורות ריקות. זבל היה מתקבל רק מ-`malloc`.",
      "recap": "מערך מבנים מ-`calloc`: `size = 0` ו-`ptr = NULL` בכל איבר.",
      "questionHtml": "מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct\n{\n    int size;\n    int *ptr;\n} dyn_array;\n\nint main(void)\n{\n    dyn_array *B = (dyn_array *)calloc(3, sizeof(dyn_array));\n    printf(\"%d %s\", B[1].size, B[1].ptr ? \"ptr\" : \"NULL\");\n    return 0;\n}</code></pre>",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">calloc</code> מאפס את כל הבתים, ולכן בכל איבר <code class=\"tok\" dir=\"ltr\">size</code> הוא 0 ו-<code class=\"tok\" dir=\"ltr\">ptr</code> הוא <code class=\"tok\" dir=\"ltr\">NULL</code>. זה בדיוק מה שמתאים לשורות ריקות. זבל היה מתקבל רק מ-<code class=\"tok\" dir=\"ltr\">malloc</code>.",
      "recapHtml": "מערך מבנים מ-<code class=\"tok\" dir=\"ltr\">calloc</code>: <code class=\"tok\" dir=\"ltr\">size = 0</code> ו-<code class=\"tok\" dir=\"ltr\">ptr = NULL</code> בכל איבר."
     },
     {
      "id": "C07-Q2",
      "step": {
       "type": "numeric",
       "prompt": "ב-64 סיביות, מה `sizeof(dyn_array)` של המבנה מהשיעור (`int size; int *ptr;`)?",
       "answer": 16,
       "tol": 0,
       "explain": "`int` תופס 4 בתים, ואחריו 4 בתים ריפוד כדי שהמצביע (8 בתים) יתחיל בכתובת שמתחלקת ב-8. סך הכל $4 + 4 + 8 = 16$.",
       "promptHtml": "ב-64 סיביות, מה <code class=\"tok\" dir=\"ltr\">sizeof(dyn_array)</code> של המבנה מהשיעור (<code class=\"tok\" dir=\"ltr\">int size; int *ptr;</code>)?",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">int</code> תופס 4 בתים, ואחריו 4 בתים ריפוד כדי שהמצביע (8 בתים) יתחיל בכתובת שמתחלקת ב-8. סך הכל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>+</mo><mn>4</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>16</mn></mrow><annotation encoding=\"application/x-tex\">4 + 4 + 8 = 16</annotation></semantics></math></span>."
      },
      "recap": "גודל מבנה כולל ריפוד לפי השדה הרחב ביותר.",
      "recapHtml": "גודל מבנה כולל ריפוד לפי השדה הרחב ביותר."
     },
     {
      "id": "C07-Q3",
      "step": {
       "type": "fillblank",
       "prompt": "השלימו את גודל ההקטנה של `tmp` למספר האיברים שנמצאו בפועל (`k`).",
       "code": true,
       "lines": [
        "dyn_array *div_numbers(const int *A, int sz, int n)",
        "{",
        "    int i, j, k = 0;",
        "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));",
        "    for (i = 2; i <= n; i++)",
        "    {",
        "        int *tmp = (int *)calloc(sz, sizeof(int));",
        "        for (j = 0, k = 0; j < sz; j++)",
        "            if (A[j] % i == 0)",
        "                tmp[k++] = A[j];",
        "        B[i - 2].ptr = (int *)realloc(tmp, ___);",
        "        B[i - 2].size = k;",
        "    }",
        "    return B;",
        "}"
       ],
       "blankIndex": 10,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "k * sizeof(int)",
         "html": "k * sizeof(int)"
        },
        {
         "id": "b",
         "type": "text",
         "value": "k",
         "html": "k"
        },
        {
         "id": "c",
         "type": "text",
         "value": "sz * sizeof(int)",
         "html": "sz * sizeof(int)"
        },
        {
         "id": "d",
         "type": "text",
         "value": "sizeof(int)",
         "html": "sizeof(int)"
        }
       ],
       "correctId": "a",
       "explain": "`realloc` מקבל גודל בבתים, כלומר `k` איברים כפול `sizeof(int)`. `k` לבד הוא `k` בתים בלבד, `sz * sizeof(int)` לא מקטין כלום, ו-`sizeof(int)` משאיר איבר אחד.",
       "promptHtml": "השלימו את גודל ההקטנה של <code class=\"tok\" dir=\"ltr\">tmp</code> למספר האיברים שנמצאו בפועל (<code class=\"tok\" dir=\"ltr\">k</code>).",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">realloc</code> מקבל גודל בבתים, כלומר <code class=\"tok\" dir=\"ltr\">k</code> איברים כפול <code class=\"tok\" dir=\"ltr\">sizeof(int)</code>. <code class=\"tok\" dir=\"ltr\">k</code> לבד הוא <code class=\"tok\" dir=\"ltr\">k</code> בתים בלבד, <code class=\"tok\" dir=\"ltr\">sz * sizeof(int)</code> לא מקטין כלום, ו-<code class=\"tok\" dir=\"ltr\">sizeof(int)</code> משאיר איבר אחד.",
       "linesHtml": [
        "dyn_array *div_numbers(const int *A, int sz, int n)",
        "{",
        "    int i, j, k = 0;",
        "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));",
        "    for (i = 2; i &lt;= n; i++)",
        "    {",
        "        int *tmp = (int *)calloc(sz, sizeof(int));",
        "        for (j = 0, k = 0; j &lt; sz; j++)",
        "            if (A[j] % i == 0)",
        "                tmp[k++] = A[j];",
        "        B[i - 2].ptr = (int *)realloc(tmp, ___);",
        "        B[i - 2].size = k;",
        "    }",
        "    return B;",
        "}"
       ]
      },
      "recap": "`realloc(p, k * sizeof(int))`: הגודל בבתים.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">realloc(p, k * sizeof(int))</code>: הגודל בבתים."
     },
     {
      "id": "C07-Q4",
      "step": {
       "type": "order",
       "prompt": "סדרו את גוף הלולאה של `div_numbers` עבור מחלק `i`: להקצות מערך זמני, למלא אותו, ולהקטין ולשמור.",
       "code": true,
       "lines": [
        "int *tmp = (int *)calloc(sz, sizeof(int));",
        "for (j = 0, k = 0; j < sz; j++)\n            if (A[j] % i == 0)\n                tmp[k++] = A[j];",
        "B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));\n        B[i - 2].size = k;"
       ],
       "explain": "קודם מקצים `tmp` בגודל המרבי, אחר כך ממלאים ומחשבים את `k`, ורק אז מקטינים ל-`k` איברים ושומרים את הגודל. הקטנה לפני המילוי משתמשת ב-`k` שעדיין לא חושב.",
       "promptHtml": "סדרו את גוף הלולאה של <code class=\"tok\" dir=\"ltr\">div_numbers</code> עבור מחלק <code class=\"tok\" dir=\"ltr\">i</code>: להקצות מערך זמני, למלא אותו, ולהקטין ולשמור.",
       "explainHtml": "קודם מקצים <code class=\"tok\" dir=\"ltr\">tmp</code> בגודל המרבי, אחר כך ממלאים ומחשבים את <code class=\"tok\" dir=\"ltr\">k</code>, ורק אז מקטינים ל-<code class=\"tok\" dir=\"ltr\">k</code> איברים ושומרים את הגודל. הקטנה לפני המילוי משתמשת ב-<code class=\"tok\" dir=\"ltr\">k</code> שעדיין לא חושב.",
       "linesHtml": [
        "int *tmp = (int *)calloc(sz, sizeof(int));",
        "for (j = 0, k = 0; j &lt; sz; j++)\n            if (A[j] % i == 0)\n                tmp[k++] = A[j];",
        "B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));\n        B[i - 2].size = k;"
       ]
      },
      "recap": "מקצים מקסימום, ממלאים, מקטינים ושומרים.",
      "recapHtml": "מקצים מקסימום, ממלאים, מקטינים ושומרים."
     },
     {
      "id": "C07-Q5",
      "step": {
       "type": "findbug",
       "prompt": "בשורה $i$ של התוצאה אמורים להיכנס המספרים מ-`A` שמתחלקים ב-`i`. התוצאה שגויה. מצאו את השורה השגויה.",
       "code": true,
       "lines": [
        "dyn_array *div_numbers(const int *A, int sz, int n)",
        "{",
        "    int i, j, k = 0;",
        "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));",
        "    for (i = 2; i <= n; i++)",
        "    {",
        "        int *tmp = (int *)calloc(sz, sizeof(int));",
        "        for (j = 0, k = 0; j < sz; j++)",
        "            if (i % A[j] == 0)",
        "                tmp[k++] = A[j];",
        "        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));",
        "        B[i - 2].size = k;",
        "    }",
        "    return B;",
        "}"
       ],
       "bugIndex": 8,
       "explain": "התנאי הוא ש-`A[j]` מתחלק ב-`i`: `A[j] % i == 0`. הגרסה `i % A[j] == 0` שואלת את ההפך (האם `i` מתחלק ב-`A[j]`), ולכן אף מספר גדול מ-`i` לא נכנס.",
       "promptHtml": "בשורה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>i</mi></mrow><annotation encoding=\"application/x-tex\">i</annotation></semantics></math></span> של התוצאה אמורים להיכנס המספרים מ-<code class=\"tok\" dir=\"ltr\">A</code> שמתחלקים ב-<code class=\"tok\" dir=\"ltr\">i</code>. התוצאה שגויה. מצאו את השורה השגויה.",
       "explainHtml": "התנאי הוא ש-<code class=\"tok\" dir=\"ltr\">A[j]</code> מתחלק ב-<code class=\"tok\" dir=\"ltr\">i</code>: <code class=\"tok\" dir=\"ltr\">A[j] % i == 0</code>. הגרסה <code class=\"tok\" dir=\"ltr\">i % A[j] == 0</code> שואלת את ההפך (האם <code class=\"tok\" dir=\"ltr\">i</code> מתחלק ב-<code class=\"tok\" dir=\"ltr\">A[j]</code>), ולכן אף מספר גדול מ-<code class=\"tok\" dir=\"ltr\">i</code> לא נכנס.",
       "linesHtml": [
        "dyn_array *div_numbers(const int *A, int sz, int n)",
        "{",
        "    int i, j, k = 0;",
        "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));",
        "    for (i = 2; i &lt;= n; i++)",
        "    {",
        "        int *tmp = (int *)calloc(sz, sizeof(int));",
        "        for (j = 0, k = 0; j &lt; sz; j++)",
        "            if (i % A[j] == 0)",
        "                tmp[k++] = A[j];",
        "        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));",
        "        B[i - 2].size = k;",
        "    }",
        "    return B;",
        "}"
       ]
      },
      "recap": "`x % d == 0`: `x` מתחלק ב-`d`.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">x % d == 0</code>: <code class=\"tok\" dir=\"ltr\">x</code> מתחלק ב-<code class=\"tok\" dir=\"ltr\">d</code>."
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🏆",
    "title": "אלוף: שאלות אמיתיות ממבחנים",
    "goal": "אחרי השלב הזה אפשר לפתור שאלות אמיתיות על מטריצות דינמיות, משולשים ומערכי מבנים.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "\n    <p>זה שלב האלוף: שאלות אמיתיות ממבחנים קודמים. בכל אחת מהן אותו שלד:</p>\n    <ul>\n      <li>שרטטו קלט ופלט עם דוגמה 3×3, וכתבו אורך כל שורה ונוסחת אינדקס (מקור מול יעד).</li>\n      <li>הקצו קודם את מערך המצביעים, ואז כל שורה בלולאה. <code>calloc</code> כשצריך אפסים.</li>\n      <li>החזרה: ב-<code>return</code> או דרך <code>int ***out</code> / <code>int *size</code>, עם <code>*out = ...</code> ו-<code>(*out)[k]</code>.</li>\n      <li>שחרור: קודם השורות ואז המערך החיצוני, ורק אחרי שהעתקתם.</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 בדקו תמיד מקרה קטן (למשל <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">n = 1</annotation></semantics></math></span>) ואת כל הקצאה: האם יש לה שחרור, והאם הגודל הוא <code>sizeof</code> של הטיפוס הנכון.</div>"
    },
    "questions": [
     {
      "bankId": "24B-B-Q2",
      "recap": "מסגרת סביב מטריצה: `calloc` לאפסים, העתקה עם היסט 1, ושחרור המקור אחרי ההעתקה.",
      "recapHtml": "מסגרת סביב מטריצה: <code class=\"tok\" dir=\"ltr\">calloc</code> לאפסים, העתקה עם היסט 1, ושחרור המקור אחרי ההעתקה."
     },
     {
      "bankId": "24B-A-Q2",
      "recap": "מערך של מבנים: `calloc` נותן `size = 0` ו-`ptr = NULL`, ו-`realloc` מקטין לגודל הסופי.",
      "recapHtml": "מערך של מבנים: <code class=\"tok\" dir=\"ltr\">calloc</code> נותן <code class=\"tok\" dir=\"ltr\">size = 0</code> ו-<code class=\"tok\" dir=\"ltr\">ptr = NULL</code>, ו-<code class=\"tok\" dir=\"ltr\">realloc</code> מקטין לגודל הסופי."
     },
     {
      "bankId": "25B-A-Q2",
      "recap": "ממטריצה סטטית לשני משולשים משוננים דרך `int ***`.",
      "recapHtml": "ממטריצה סטטית לשני משולשים משוננים דרך <code class=\"tok\" dir=\"ltr\">int ***</code>."
     },
     {
      "bankId": "25B-B-Q2",
      "recap": "משני משולשים למטריצה $(n+1) \\times (n+1)$ עם אלכסון אפס: נוסחאות אינדקס.",
      "recapHtml": "משני משולשים למטריצה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mo stretchy=\"false\">(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo><mo>×</mo><mo stretchy=\"false\">(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">(n+1) \\times (n+1)</annotation></semantics></math></span> עם אלכסון אפס: נוסחאות אינדקס."
     },
     {
      "bankId": "23B-A-Q2",
      "recap": "שני מערכי פלט דרך פרמטרים, אורך מקסימלי ואז `realloc`.",
      "recapHtml": "שני מערכי פלט דרך פרמטרים, אורך מקסימלי ואז <code class=\"tok\" dir=\"ltr\">realloc</code>."
     }
    ]
   }
  ]
 },
 "files_strings": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "📂",
    "title": "פתיחה, מצבים וכתיבה",
    "goal": "אחרי השלב הזה אפשר לפתוח קובץ במצב הנכון, לבדוק שהפתיחה הצליחה, לכתוב אליו ולסגור אותו.",
    "source": "ai-verified",
    "boss": false,
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
        "value": "`NULL`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "b",
        "value": "מצביע תקין לקובץ ריק",
        "type": "text",
        "html": "מצביע תקין לקובץ ריק"
       },
       {
        "id": "c",
        "value": "התוכנית קורסת כבר בתוך `fopen`",
        "type": "text",
        "html": "התוכנית קורסת כבר בתוך <code class=\"tok\" dir=\"ltr\">fopen</code>"
       },
       {
        "id": "d",
        "value": "מצביע ל-`stdin`",
        "type": "text",
        "html": "מצביע ל-<code class=\"tok\" dir=\"ltr\">stdin</code>"
       }
      ],
      "correctId": "a",
      "explanation": "במצב קריאה קובץ שלא קיים לא נוצר, ו-`fopen` מחזירה `NULL` (נבדק עם clang). לכן בודקים `if (!f)` מיד אחרי הפתיחה. מצביע תקין לקובץ ריק היה קורה במצב כתיבה. הקריסה מתרחשת רק אם משתמשים במצביע ה-`NULL`, לא בפתיחה עצמה. `stdin` הוא קובץ סטנדרטי אחר שאינו קשור.",
      "recap": "`fopen` נכשלת עם `NULL`, ותמיד בודקים אותה.",
      "questionHtml": "מה מחזירה <code class=\"tok\" dir=\"ltr\">fopen(\"nope.txt\", \"r\")</code> כשהקובץ <code class=\"tok\" dir=\"ltr\">nope.txt</code> לא קיים בתיקייה?",
      "explanationHtml": "במצב קריאה קובץ שלא קיים לא נוצר, ו-<code class=\"tok\" dir=\"ltr\">fopen</code> מחזירה <code class=\"tok\" dir=\"ltr\">NULL</code> (נבדק עם clang). לכן בודקים <code class=\"tok\" dir=\"ltr\">if (!f)</code> מיד אחרי הפתיחה. מצביע תקין לקובץ ריק היה קורה במצב כתיבה. הקריסה מתרחשת רק אם משתמשים במצביע ה-<code class=\"tok\" dir=\"ltr\">NULL</code>, לא בפתיחה עצמה. <code class=\"tok\" dir=\"ltr\">stdin</code> הוא קובץ סטנדרטי אחר שאינו קשור.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fopen</code> נכשלת עם <code class=\"tok\" dir=\"ltr\">NULL</code>, ותמיד בודקים אותה."
     },
     {
      "id": "C01-Q2",
      "question": "הקובץ `t.txt` מכיל `AB`. התוכנית מריצה:\n```c\nFILE *f = fopen(\"t.txt\", \"w\");\nfputs(\"C\", f);\nfclose(f);\n```\nמה תוכן הקובץ אחרי הריצה?",
      "options": [
       {
        "id": "a",
        "value": "`C`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">C</code>"
       },
       {
        "id": "b",
        "value": "`ABC`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">ABC</code>"
       },
       {
        "id": "c",
        "value": "`AB`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">AB</code>"
       },
       {
        "id": "d",
        "value": "`CB`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">CB</code>"
       }
      ],
      "correctId": "a",
      "explanation": "מצב `\"w\"` מוחק את התוכן הקיים בפתיחה, ולכן נשאר רק `C` (נבדק עם clang). `ABC` היה מתקבל במצב `\"a\"`. `AB` היה נשאר לו הכתיבה לא התבצעה. `CB` היה מתקבל רק אם `C` היה דורס את התו הראשון, וזה לא מה ש-`\"w\"` עושה.",
      "recap": "`\"w\"` מוחק את התוכן הקיים, `\"a\"` מוסיף בסוף.",
      "questionHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">t.txt</code> מכיל <code class=\"tok\" dir=\"ltr\">AB</code>. התוכנית מריצה:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"t.txt\", \"w\");\nfputs(\"C\", f);\nfclose(f);</code></pre>מה תוכן הקובץ אחרי הריצה?",
      "explanationHtml": "מצב <code class=\"tok\" dir=\"ltr\">\"w\"</code> מוחק את התוכן הקיים בפתיחה, ולכן נשאר רק <code class=\"tok\" dir=\"ltr\">C</code> (נבדק עם clang). <code class=\"tok\" dir=\"ltr\">ABC</code> היה מתקבל במצב <code class=\"tok\" dir=\"ltr\">\"a\"</code>. <code class=\"tok\" dir=\"ltr\">AB</code> היה נשאר לו הכתיבה לא התבצעה. <code class=\"tok\" dir=\"ltr\">CB</code> היה מתקבל רק אם <code class=\"tok\" dir=\"ltr\">C</code> היה דורס את התו הראשון, וזה לא מה ש-<code class=\"tok\" dir=\"ltr\">\"w\"</code> עושה.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">\"w\"</code> מוחק את התוכן הקיים, <code class=\"tok\" dir=\"ltr\">\"a\"</code> מוסיף בסוף."
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
       "explain": "מצב `\"a\"` שומר את `x1` וכותב אחריו את `25`, ולכן התוכן `x125`.",
       "promptHtml": "הקובץ <code class=\"tok\" dir=\"ltr\">t.txt</code> מכיל <code class=\"tok\" dir=\"ltr\">x1</code>. מה יהיה תוכנו (בלי רווחים) אחרי הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>FILE *f = fopen(\"t.txt\", \"a\");\nfprintf(f, \"%d\", 25);\nfclose(f);</code></pre>",
       "explainHtml": "מצב <code class=\"tok\" dir=\"ltr\">\"a\"</code> שומר את <code class=\"tok\" dir=\"ltr\">x1</code> וכותב אחריו את <code class=\"tok\" dir=\"ltr\">25</code>, ולכן התוכן <code class=\"tok\" dir=\"ltr\">x125</code>."
      },
      "recap": "במצב `\"a\"` הכתיבה נעשית אחרי התוכן הקיים.",
      "recapHtml": "במצב <code class=\"tok\" dir=\"ltr\">\"a\"</code> הכתיבה נעשית אחרי התוכן הקיים."
     },
     {
      "id": "C01-Q4",
      "step": {
       "type": "numeric",
       "answer": 7,
       "tol": 0,
       "prompt": "הקובץ נפתח חדש בכתיבה, ואז מתבצע הקוד הבא. כמה תווים יש בקובץ בסוף?\n```c\nfputs(\"ab\", f);\nfputc('c', f);\nfprintf(f, \"%d-%d\", 12, 3);\n```",
       "explain": "נכתבים `ab` (2 תווים), `c` (תו אחד) ו-`12-3` (4 תווים): $2+1+4=7$, כלומר `abc12-3`.",
       "promptHtml": "הקובץ נפתח חדש בכתיבה, ואז מתבצע הקוד הבא. כמה תווים יש בקובץ בסוף?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>fputs(\"ab\", f);\nfputc('c', f);\nfprintf(f, \"%d-%d\", 12, 3);</code></pre>",
       "explainHtml": "נכתבים <code class=\"tok\" dir=\"ltr\">ab</code> (2 תווים), <code class=\"tok\" dir=\"ltr\">c</code> (תו אחד) ו-<code class=\"tok\" dir=\"ltr\">12-3</code> (4 תווים): <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>7</mn></mrow><annotation encoding=\"application/x-tex\">2+1+4=7</annotation></semantics></math></span>, כלומר <code class=\"tok\" dir=\"ltr\">abc12-3</code>."
      },
      "recap": "כל פונקציית כתיבה מוסיפה את התווים שלה בלבד, בלי תו שורה חדשה אוטומטי.",
      "recapHtml": "כל פונקציית כתיבה מוסיפה את התווים שלה בלבד, בלי תו שורה חדשה אוטומטי."
     },
     {
      "id": "C01-Q5",
      "step": {
       "type": "numeric",
       "answer": 2,
       "tol": 0,
       "prompt": "כמה שורות יוצגו על המסך?\n```c\nputs(\"a\");\nfputs(\"b\", stdout);\nputs(\"c\");\n```",
       "explain": "`puts(\"a\")` מדפיסה `a` ותו שורה חדשה. `fputs(\"b\", stdout)` מדפיסה `b` בלי שורה חדשה, ולכן `puts(\"c\")` ממשיכה באותה שורה: `bc`. בסך הכול שתי שורות: `a` ו-`bc`.",
       "promptHtml": "כמה שורות יוצגו על המסך?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>puts(\"a\");\nfputs(\"b\", stdout);\nputs(\"c\");</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">puts(\"a\")</code> מדפיסה <code class=\"tok\" dir=\"ltr\">a</code> ותו שורה חדשה. <code class=\"tok\" dir=\"ltr\">fputs(\"b\", stdout)</code> מדפיסה <code class=\"tok\" dir=\"ltr\">b</code> בלי שורה חדשה, ולכן <code class=\"tok\" dir=\"ltr\">puts(\"c\")</code> ממשיכה באותה שורה: <code class=\"tok\" dir=\"ltr\">bc</code>. בסך הכול שתי שורות: <code class=\"tok\" dir=\"ltr\">a</code> ו-<code class=\"tok\" dir=\"ltr\">bc</code>."
      },
      "recap": "`puts` מוסיפה `'\\n'`, `fputs` לא.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">puts</code> מוסיפה <code class=\"tok\" dir=\"ltr\">'\\n'</code>, <code class=\"tok\" dir=\"ltr\">fputs</code> לא."
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
       "explain": "קודם פותחים, אחר כך בודקים שהפתיחה הצליחה, רק אז כותבים, ובסוף סוגרים.",
       "promptHtml": "סדרו את השלבים של כתיבת המספר 5 לקובץ בצורה נכונה ובטוחה.",
       "explainHtml": "קודם פותחים, אחר כך בודקים שהפתיחה הצליחה, רק אז כותבים, ובסוף סוגרים.",
       "linesHtml": [
        "FILE *f = fopen(\"out.txt\", \"w\");",
        "if (!f) return 1;",
        "fprintf(f, \"%d\", 5);",
        "fclose(f);"
       ]
      },
      "recap": "פותחים, בודקים `NULL`, משתמשים, סוגרים.",
      "recapHtml": "פותחים, בודקים <code class=\"tok\" dir=\"ltr\">NULL</code>, משתמשים, סוגרים."
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "🔢",
    "title": "קריאת מספרים ומילים עם fscanf",
    "goal": "אחרי השלב הזה אפשר לקרוא מקובץ טקסט מספרים ומילים בלולאה שנעצרת בדיוק בסוף הקלט.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "<p><code>fscanf(f, format, ...)</code> עובדת כמו <code>scanf</code> אבל קוראת מהקובץ <code>f</code>. היא <b>מחזירה כמה ערכים נקראו בהצלחה</b>.</p><ul><li>קריאה מוצלחת של ערך אחד מחזירה <code>1</code>.</li><li>אם הטקסט לא מתאים לפורמט (למשל <code>abc</code> כשמבקשים <code>%d</code>) היא מחזירה <code>0</code>.</li><li>אם הקלט נגמר לפני שנקרא משהו היא מחזירה <code>EOF</code> (ערך שלילי, בפועל <code>-1</code>).</li></ul><p>הלולאה הרגילה לקריאת מספרים עד הסוף:</p><pre><code>int x, sum = 0;\nwhile (fscanf(f, \"%d\", &amp;x) == 1)   /* stop on EOF or on a mismatch */\n    sum += x;</code></pre><div class=\"lesson-rule\">🔑 תנאי הלולאה הוא <code>fscanf(...) == 1</code> (כמספר הערכים שביקשתם). כך הלולאה נעצרת גם בסוף הקובץ וגם כשהטקסט לא מתאים.</div><h3>רווחים ומילים</h3><ul><li><code>%d</code> ו-<code>%s</code> מדלגים אוטומטית על רווחים, טאבים ושורות חדשות שלפני הערך.</li><li><code>%s</code> קוראת <b>מילה</b>: רצף תווים עד הרווח או השורה החדשה הבאה. היא מוסיפה <code>'\\0'</code> בסוף.</li><li><code>%3s</code> מגביל את הקריאה ל-3 תווים לכל היותר (בלי ה-<code>'\\0'</code>). את הרצף שנשאר קוראת הקריאה הבאה.</li></ul><div class=\"lesson-ex\">דוגמה: בקובץ <code>4 10 -3</code> הלולאה קוראת 4, 10, -3 ואז הקריאה הרביעית מחזירה <code>EOF</code>, והסכום הוא 11. בקובץ <code>12 abc 5</code> הלולאה קוראת 12, ואז נכשלת על <code>abc</code> (מחזירה 0) ונעצרת: ה-5 לא נקרא לעולם.</div><div class=\"lesson-trap\">⚠️ לא שוכחים את ה-<code>&amp;</code> לפני משתנה מספרי. ל-<code>%s</code> לא צריך <code>&amp;</code> כי שם מערך הוא כבר כתובת.</div>"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "step": {
       "type": "numeric",
       "answer": 19,
       "tol": 0,
       "prompt": "הקובץ מכיל את השורה `4 10 -3` ואחריה השורה `8`. מה יודפס?\n```c\nint x, sum = 0;\nwhile (fscanf(f, \"%d\", &x) == 1)\n    sum += x;\nprintf(\"%d\", sum);\n```",
       "explain": "`fscanf` מדלגת על ירידת השורה וקוראת את כל ארבעת המספרים: $4+10-3+8=19$.",
       "promptHtml": "הקובץ מכיל את השורה <code class=\"tok\" dir=\"ltr\">4 10 -3</code> ואחריה השורה <code class=\"tok\" dir=\"ltr\">8</code>. מה יודפס?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x, sum = 0;\nwhile (fscanf(f, \"%d\", &amp;x) == 1)\n    sum += x;\nprintf(\"%d\", sum);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">fscanf</code> מדלגת על ירידת השורה וקוראת את כל ארבעת המספרים: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>+</mo><mn>10</mn><mo>−</mo><mn>3</mn><mo>+</mo><mn>8</mn><mo>=</mo><mn>19</mn></mrow><annotation encoding=\"application/x-tex\">4+10-3+8=19</annotation></semantics></math></span>."
      },
      "recap": "`fscanf` עם `%d` מדלגת על רווחים ושורות חדשות.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fscanf</code> עם <code class=\"tok\" dir=\"ltr\">%d</code> מדלגת על רווחים ושורות חדשות."
     },
     {
      "id": "C02-Q2",
      "question": "מה מחזירה `fscanf(f, \"%d\", &x)` כשכל הקלט כבר נקרא וכבר אין בקובץ מה לקרוא?",
      "options": [
       {
        "id": "a",
        "value": "`EOF`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">EOF</code>"
       },
       {
        "id": "b",
        "value": "`0`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
       },
       {
        "id": "c",
        "value": "`NULL`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "d",
        "value": "הערך האחרון שנקרא",
        "type": "text",
        "html": "הערך האחרון שנקרא"
       }
      ],
      "correctId": "a",
      "explanation": "כשהקלט נגמר לפני שנקרא משהו, `fscanf` מחזירה `EOF` (נבדק עם clang). הערך `0` מוחזר כשיש טקסט שלא מתאים לפורמט (למשל אותיות במקום מספר). `NULL` הוא ערך של מצביע ש-`fscanf` לא מחזירה, והמשתנה `x` נשאר עם ערכו הקודם ואינו ערך ההחזרה.",
      "recap": "בסוף הקלט `fscanf` מחזירה `EOF`, ועל אי-התאמה היא מחזירה `0`.",
      "questionHtml": "מה מחזירה <code class=\"tok\" dir=\"ltr\">fscanf(f, \"%d\", &amp;x)</code> כשכל הקלט כבר נקרא וכבר אין בקובץ מה לקרוא?",
      "explanationHtml": "כשהקלט נגמר לפני שנקרא משהו, <code class=\"tok\" dir=\"ltr\">fscanf</code> מחזירה <code class=\"tok\" dir=\"ltr\">EOF</code> (נבדק עם clang). הערך <code class=\"tok\" dir=\"ltr\">0</code> מוחזר כשיש טקסט שלא מתאים לפורמט (למשל אותיות במקום מספר). <code class=\"tok\" dir=\"ltr\">NULL</code> הוא ערך של מצביע ש-<code class=\"tok\" dir=\"ltr\">fscanf</code> לא מחזירה, והמשתנה <code class=\"tok\" dir=\"ltr\">x</code> נשאר עם ערכו הקודם ואינו ערך ההחזרה.",
      "recapHtml": "בסוף הקלט <code class=\"tok\" dir=\"ltr\">fscanf</code> מחזירה <code class=\"tok\" dir=\"ltr\">EOF</code>, ועל אי-התאמה היא מחזירה <code class=\"tok\" dir=\"ltr\">0</code>."
     },
     {
      "id": "C02-Q3",
      "step": {
       "type": "numeric",
       "answer": 1,
       "tol": 0,
       "prompt": "הקובץ מכיל `12 abc 5`. כמה פעמים יתבצע גוף הלולאה?\n```c\nint x, n = 0;\nwhile (fscanf(f, \"%d\", &x) == 1)\n    n++;\n```",
       "explain": "הקריאה הראשונה קוראת 12 ומחזירה 1. הקריאה השנייה נתקלת ב-`abc`, שאינו מספר, ומחזירה 0, ולכן הלולאה נעצרת. הגוף רץ פעם אחת.",
       "promptHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">12 abc 5</code>. כמה פעמים יתבצע גוף הלולאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x, n = 0;\nwhile (fscanf(f, \"%d\", &amp;x) == 1)\n    n++;</code></pre>",
       "explainHtml": "הקריאה הראשונה קוראת 12 ומחזירה 1. הקריאה השנייה נתקלת ב-<code class=\"tok\" dir=\"ltr\">abc</code>, שאינו מספר, ומחזירה 0, ולכן הלולאה נעצרת. הגוף רץ פעם אחת."
      },
      "recap": "אי-התאמה בפורמט עוצרת את הלולאה, כי `fscanf` מחזירה `0`.",
      "recapHtml": "אי-התאמה בפורמט עוצרת את הלולאה, כי <code class=\"tok\" dir=\"ltr\">fscanf</code> מחזירה <code class=\"tok\" dir=\"ltr\">0</code>."
     },
     {
      "id": "C02-Q4",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "הקובץ מכיל בשורה הראשונה `red  green` (שני רווחים בין המילים) ובשורה השנייה `blue`. כמה מילים נקראות?\n```c\nchar w[20];\nint n = 0;\nwhile (fscanf(f, \"%19s\", w) == 1)\n    n++;\n```",
       "explain": "`%s` מדלגת על כל הרווחים ועל השורה החדשה וקוראת `red`, `green` ו-`blue`: שלוש מילים.",
       "promptHtml": "הקובץ מכיל בשורה הראשונה <code class=\"tok\" dir=\"ltr\">red  green</code> (שני רווחים בין המילים) ובשורה השנייה <code class=\"tok\" dir=\"ltr\">blue</code>. כמה מילים נקראות?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char w[20];\nint n = 0;\nwhile (fscanf(f, \"%19s\", w) == 1)\n    n++;</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">%s</code> מדלגת על כל הרווחים ועל השורה החדשה וקוראת <code class=\"tok\" dir=\"ltr\">red</code>, <code class=\"tok\" dir=\"ltr\">green</code> ו-<code class=\"tok\" dir=\"ltr\">blue</code>: שלוש מילים."
      },
      "recap": "`%s` קוראת מילה אחת בכל פעם ומדלגת על רווחים ושורות חדשות.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">%s</code> קוראת מילה אחת בכל פעם ומדלגת על רווחים ושורות חדשות."
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את תנאי הלולאה שמסכמת את כל המספרים בקובץ (התוצאה הנכונה לקובץ `4 10 -3 8` היא 19).",
       "lines": [
        "int sum = 0, x;",
        "while (fscanf(f, \"%d\", &x) ___ 1)",
        "    sum += x;"
       ],
       "blankIndex": 1,
       "options": [
        {
         "id": "a",
         "value": "==",
         "type": "text",
         "html": "=="
        },
        {
         "id": "b",
         "value": "!=",
         "type": "text",
         "html": "!="
        },
        {
         "id": "c",
         "value": "<",
         "type": "text",
         "html": "&lt;"
        },
        {
         "id": "d",
         "value": ">",
         "type": "text",
         "html": "&gt;"
        }
       ],
       "correctId": "a",
       "explain": "הלולאה צריכה לרוץ כל עוד נקרא ערך אחד בהצלחה, כלומר `== 1`. עם `!=`, `<` או `>` התנאי שקר כבר בקריאה הראשונה והסכום נשאר 0 (נבדק עם clang).",
       "promptHtml": "השלימו את תנאי הלולאה שמסכמת את כל המספרים בקובץ (התוצאה הנכונה לקובץ <code class=\"tok\" dir=\"ltr\">4 10 -3 8</code> היא 19).",
       "explainHtml": "הלולאה צריכה לרוץ כל עוד נקרא ערך אחד בהצלחה, כלומר <code class=\"tok\" dir=\"ltr\">== 1</code>. עם <code class=\"tok\" dir=\"ltr\">!=</code>, <code class=\"tok\" dir=\"ltr\">&lt;</code> או <code class=\"tok\" dir=\"ltr\">&gt;</code> התנאי שקר כבר בקריאה הראשונה והסכום נשאר 0 (נבדק עם clang).",
       "linesHtml": [
        "int sum = 0, x;",
        "while (fscanf(f, \"%d\", &amp;x) ___ 1)",
        "    sum += x;"
       ]
      },
      "recap": "לולאת קריאה: `while (fscanf(...) == מספר הערכים)`.",
      "recapHtml": "לולאת קריאה: <code class=\"tok\" dir=\"ltr\">while (fscanf(...) == מספר הערכים)</code>."
     },
     {
      "id": "C02-Q6",
      "step": {
       "type": "text",
       "accept": [
        "abc|def|g|hi|"
       ],
       "normalize": "none",
       "prompt": "הקובץ מכיל `abcdefg hi`. מה יודפס (בלי רווחים)?\n```c\nchar w[4];\nwhile (fscanf(f, \"%3s\", w) == 1)\n    printf(\"%s|\", w);\n```",
       "explain": "כל קריאה לוקחת עד 3 תווים: `abc`, אחר כך `def`, אחר כך `g` (המילה נגמרת ברווח), ולבסוף `hi`. הפלט `abc|def|g|hi|`.",
       "promptHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">abcdefg hi</code>. מה יודפס (בלי רווחים)?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char w[4];\nwhile (fscanf(f, \"%3s\", w) == 1)\n    printf(\"%s|\", w);</code></pre>",
       "explainHtml": "כל קריאה לוקחת עד 3 תווים: <code class=\"tok\" dir=\"ltr\">abc</code>, אחר כך <code class=\"tok\" dir=\"ltr\">def</code>, אחר כך <code class=\"tok\" dir=\"ltr\">g</code> (המילה נגמרת ברווח), ולבסוף <code class=\"tok\" dir=\"ltr\">hi</code>. הפלט <code class=\"tok\" dir=\"ltr\">abc|def|g|hi|</code>."
      },
      "recap": "`%3s` קוראת עד 3 תווים, והשאר נשאר לקריאה הבאה.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">%3s</code> קוראת עד 3 תווים, והשאר נשאר לקריאה הבאה."
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "🔤",
    "title": "תו אחר תו ושורה אחר שורה",
    "goal": "אחרי השלב הזה אפשר לקרוא קובץ בתווים עם fgetc ובשורות עם fgets ולהסיר את תו השורה החדשה.",
    "source": "ai-verified",
    "boss": false,
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
       "explain": "הלולאה סופרת כל תו, כולל תווי השורה החדשה: $1+1+2+1+1+1+1=8$ (`a`, שורה, `bb`, שורה, שורה, `c`, שורה).",
       "promptHtml": "הקובץ מכיל ארבע שורות: <code class=\"tok\" dir=\"ltr\">a</code>, אחר כך <code class=\"tok\" dir=\"ltr\">bb</code>, אחר כך שורה ריקה, אחר כך <code class=\"tok\" dir=\"ltr\">c</code>, וכל שורה מסתיימת ב-<code class=\"tok\" dir=\"ltr\">'\\n'</code>. מה ערך <code class=\"tok\" dir=\"ltr\">n</code> בסוף?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int ch, n = 0;\nwhile ((ch = fgetc(f)) != EOF)\n    n++;</code></pre>",
       "explainHtml": "הלולאה סופרת כל תו, כולל תווי השורה החדשה: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>1</mn><mo>=</mo><mn>8</mn></mrow><annotation encoding=\"application/x-tex\">1+1+2+1+1+1+1=8</annotation></semantics></math></span> (<code class=\"tok\" dir=\"ltr\">a</code>, שורה, <code class=\"tok\" dir=\"ltr\">bb</code>, שורה, שורה, <code class=\"tok\" dir=\"ltr\">c</code>, שורה)."
      },
      "recap": "`fgetc` מחזירה גם את `'\\n'` כתו רגיל.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fgetc</code> מחזירה גם את <code class=\"tok\" dir=\"ltr\">'\\n'</code> כתו רגיל."
     },
     {
      "id": "C03-Q2",
      "step": {
       "type": "numeric",
       "answer": 4,
       "tol": 0,
       "prompt": "אותו קובץ כמו בשאלה הקודמת (`a`, `bb`, שורה ריקה, `c`, כל שורה מסתיימת ב-`'\\n'`). מה ערך `n` בסוף?\n```c\nchar line[20];\nint n = 0;\nwhile (fgets(line, 20, f))\n    n++;\n```",
       "explain": "`fgets` מחזירה מחרוזת לכל אחת מארבע השורות, גם לשורה הריקה (היא מחזירה `\"\\n\"`). `NULL` מוחזר רק בסוף הקובץ, לכן $n=4$.",
       "promptHtml": "אותו קובץ כמו בשאלה הקודמת (<code class=\"tok\" dir=\"ltr\">a</code>, <code class=\"tok\" dir=\"ltr\">bb</code>, שורה ריקה, <code class=\"tok\" dir=\"ltr\">c</code>, כל שורה מסתיימת ב-<code class=\"tok\" dir=\"ltr\">'\\n'</code>). מה ערך <code class=\"tok\" dir=\"ltr\">n</code> בסוף?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char line[20];\nint n = 0;\nwhile (fgets(line, 20, f))\n    n++;</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">fgets</code> מחזירה מחרוזת לכל אחת מארבע השורות, גם לשורה הריקה (היא מחזירה <code class=\"tok\" dir=\"ltr\">\"\\n\"</code>). <code class=\"tok\" dir=\"ltr\">NULL</code> מוחזר רק בסוף הקובץ, לכן <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>=</mo><mn>4</mn></mrow><annotation encoding=\"application/x-tex\">n=4</annotation></semantics></math></span>."
      },
      "recap": "`fgets` מחזירה `NULL` רק בסוף הקובץ, גם שורה ריקה נקראת.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fgets</code> מחזירה <code class=\"tok\" dir=\"ltr\">NULL</code> רק בסוף הקובץ, גם שורה ריקה נקראת."
     },
     {
      "id": "C03-Q3",
      "question": "איזו הצהרה נכונה למשתנה `ch` בלולאה `while ((ch = fgetc(f)) != EOF)` ?",
      "options": [
       {
        "id": "a",
        "value": "`int ch;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">int ch;</code>"
       },
       {
        "id": "b",
        "value": "`char ch;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">char ch;</code>"
       },
       {
        "id": "c",
        "value": "`unsigned char ch;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">unsigned char ch;</code>"
       },
       {
        "id": "d",
        "value": "כל אחד מהטיפוסים האלה נכון באותה מידה",
        "type": "text",
        "html": "כל אחד מהטיפוסים האלה נכון באותה מידה"
       }
      ],
      "correctId": "a",
      "explanation": "`fgetc` מחזירה `int`: ערך של תו, או `EOF` שאינו תו. רק ב-`int` אפשר להבדיל ביניהם תמיד. ב-`unsigned char` ההשוואה ל-`EOF` (שלילי) אף פעם לא נכונה והלולאה לא נגמרת. ב-`char` תלוי אם הוא עם סימן: או שהלולאה נעצרת באמצע הקובץ בתו עם הערך 255, או שהיא אינסופית. לכן הטיפוסים לא שווים.",
      "recap": "תוצאת `fgetc` נשמרת ב-`int`.",
      "questionHtml": "איזו הצהרה נכונה למשתנה <code class=\"tok\" dir=\"ltr\">ch</code> בלולאה <code class=\"tok\" dir=\"ltr\">while ((ch = fgetc(f)) != EOF)</code> ?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fgetc</code> מחזירה <code class=\"tok\" dir=\"ltr\">int</code>: ערך של תו, או <code class=\"tok\" dir=\"ltr\">EOF</code> שאינו תו. רק ב-<code class=\"tok\" dir=\"ltr\">int</code> אפשר להבדיל ביניהם תמיד. ב-<code class=\"tok\" dir=\"ltr\">unsigned char</code> ההשוואה ל-<code class=\"tok\" dir=\"ltr\">EOF</code> (שלילי) אף פעם לא נכונה והלולאה לא נגמרת. ב-<code class=\"tok\" dir=\"ltr\">char</code> תלוי אם הוא עם סימן: או שהלולאה נעצרת באמצע הקובץ בתו עם הערך 255, או שהיא אינסופית. לכן הטיפוסים לא שווים.",
      "recapHtml": "תוצאת <code class=\"tok\" dir=\"ltr\">fgetc</code> נשמרת ב-<code class=\"tok\" dir=\"ltr\">int</code>."
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "הקובץ מתחיל בשורה `ab` (ואחריה `'\\n'`) ובשורה נוספת. מה ידפיס הקוד?\n```c\nchar buf[10];\nfgets(buf, 10, f);\nprintf(\"%d\", (int)strlen(buf));\n```",
       "explain": "`fgets` קוראת את `a`, `b` ואת `'\\n'` ומשאירה אותו במחרוזת: האורך הוא 3.",
       "promptHtml": "הקובץ מתחיל בשורה <code class=\"tok\" dir=\"ltr\">ab</code> (ואחריה <code class=\"tok\" dir=\"ltr\">'\\n'</code>) ובשורה נוספת. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char buf[10];\nfgets(buf, 10, f);\nprintf(\"%d\", (int)strlen(buf));</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">fgets</code> קוראת את <code class=\"tok\" dir=\"ltr\">a</code>, <code class=\"tok\" dir=\"ltr\">b</code> ואת <code class=\"tok\" dir=\"ltr\">'\\n'</code> ומשאירה אותו במחרוזת: האורך הוא 3."
      },
      "recap": "`fgets` משאירה את `'\\n'` במחרוזת.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fgets</code> משאירה את <code class=\"tok\" dir=\"ltr\">'\\n'</code> במחרוזת."
     },
     {
      "id": "C03-Q5",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "הקובץ מכיל שורה אחת `abcdefgh`. מה ידפיס הקוד?\n```c\nchar buf[10];\nfgets(buf, 4, f);\nprintf(\"%d\", (int)strlen(buf));\n```",
       "explain": "עם `n = 4` נקראים לכל היותר $4-1=3$ תווים (`abc`), והמקום הרביעי שמור ל-`'\\0'`. האורך הוא 3.",
       "promptHtml": "הקובץ מכיל שורה אחת <code class=\"tok\" dir=\"ltr\">abcdefgh</code>. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char buf[10];\nfgets(buf, 4, f);\nprintf(\"%d\", (int)strlen(buf));</code></pre>",
       "explainHtml": "עם <code class=\"tok\" dir=\"ltr\">n = 4</code> נקראים לכל היותר <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>4</mn><mo>−</mo><mn>1</mn><mo>=</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">4-1=3</annotation></semantics></math></span> תווים (<code class=\"tok\" dir=\"ltr\">abc</code>), והמקום הרביעי שמור ל-<code class=\"tok\" dir=\"ltr\">'\\0'</code>. האורך הוא 3."
      },
      "recap": "`fgets(buf, n, f)` קוראת לכל היותר `n-1` תווים.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fgets(buf, n, f)</code> קוראת לכל היותר <code class=\"tok\" dir=\"ltr\">n-1</code> תווים."
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
         "value": "len - 1",
         "type": "text",
         "html": "len - 1"
        },
        {
         "id": "b",
         "value": "len",
         "type": "text",
         "html": "len"
        },
        {
         "id": "c",
         "value": "0",
         "type": "text",
         "html": "0"
        },
        {
         "id": "d",
         "value": "1",
         "type": "text",
         "html": "1"
        }
       ],
       "correctId": "a",
       "explain": "התו `'\\n'` נמצא במקום $len-1$, ולכן שם שמים `'\\0'`. עם `len` מחליפים את ה-`'\\0'` הקיים ב-`'\\0'` ושום דבר לא משתנה. עם `0` המחרוזת הופכת לריקה, ועם `1` היא מתקצרת לתו אחד (נבדק עם clang).",
       "promptHtml": "השלימו את הסרת <code class=\"tok\" dir=\"ltr\">'\\n'</code> מסוף השורה (השורה היא <code class=\"tok\" dir=\"ltr\">hi</code> ואחריה <code class=\"tok\" dir=\"ltr\">'\\n'</code>, והאורך אחרי ההסרה צריך להיות 2).",
       "explainHtml": "התו <code class=\"tok\" dir=\"ltr\">'\\n'</code> נמצא במקום <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>l</mi><mi>e</mi><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">len-1</annotation></semantics></math></span>, ולכן שם שמים <code class=\"tok\" dir=\"ltr\">'\\0'</code>. עם <code class=\"tok\" dir=\"ltr\">len</code> מחליפים את ה-<code class=\"tok\" dir=\"ltr\">'\\0'</code> הקיים ב-<code class=\"tok\" dir=\"ltr\">'\\0'</code> ושום דבר לא משתנה. עם <code class=\"tok\" dir=\"ltr\">0</code> המחרוזת הופכת לריקה, ועם <code class=\"tok\" dir=\"ltr\">1</code> היא מתקצרת לתו אחד (נבדק עם clang).",
       "linesHtml": [
        "size_t len = strlen(line);",
        "if (len &gt; 0 &amp;&amp; line[len - 1] == '\\n')",
        "    line[___] = '\\0';"
       ]
      },
      "recap": "מוחקים את `'\\n'` ב-`line[len - 1] = '\\0'`.",
      "recapHtml": "מוחקים את <code class=\"tok\" dir=\"ltr\">'\\n'</code> ב-<code class=\"tok\" dir=\"ltr\">line[len - 1] = '\\0'</code>."
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "🚧",
    "title": "feof ולולאות קריאה נכונות",
    "goal": "אחרי השלב הזה אפשר להסביר מתי feof נהיית אמת ולכתוב לולאת קריאה שלא רצה פעם אחת יותר מדי.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "<p><code>feof(f)</code> מחזירה ערך שונה מאפס <b>רק אחרי שניסו לקרוא מעבר לסוף הקובץ</b> וזה נכשל. היא לא מזהה מראש שהקובץ עומד להיגמר.</p><div class=\"lesson-rule\">🔑 קוראים קודם, ורק אז בודקים אם הקריאה הצליחה. הבדיקה הנכונה היא ערך ההחזרה של הקריאה עצמה: <code>fscanf(...) == 1</code>, <code>fgets(...) != NULL</code>, <code>fgetc(f) != EOF</code>.</div><h3>הלולאה השגויה</h3><pre><code>while (!feof(f))\n{\n    fscanf(f, \"%d\", &amp;x);\n    printf(\"%d \", x);\n}</code></pre><p>בקובץ <code>1 2 3</code> ואחריו <b>רווח</b>: אחרי שנקרא 3, הקובץ עוד לא נגמר (נשאר הרווח), ולכן <code>feof</code> עדיין שקר והלולאה נכנסת פעם נוספת. הקריאה הזו נכשלת, <code>x</code> נשאר 3, והמספר 3 מודפס פעמיים.</p><p>בקובץ <code>1 2 3</code> <b>בלי</b> רווח בסוף, הקריאה של 3 כבר מגיעה לסוף הקובץ בזמן שהיא בודקת אם המספר ממשיך, ולכן <code>feof</code> נהיית אמת מיד והלולאה רצה 3 פעמים בלבד. התוצאה תלויה בתו האחרון בקובץ, ולכן אי אפשר לסמוך על השיטה.</p><p>אותה בעיה ב-<code>fgets</code>: בקובץ עם שתי שורות <code>a</code> ו-<code>b</code> אחרי השורה השנייה <code>feof</code> עוד שקר. הקריאה השלישית מחזירה <code>NULL</code> ולא נוגעת במחרוזת, ולכן השורה <code>b</code> מודפסת שוב.</p><h3>הצורה שמופיעה בפתרונות הרשמיים</h3><p>קוראים פעם אחת <b>לפני</b> הלולאה, ופעם נוספת <b>בסוף כל איטרציה</b>:</p><pre><code>int ch = fgetc(f);\nwhile (ch != EOF)\n{\n    putchar(ch);\n    ch = fgetc(f);       /* refresh at the end of the body */\n}</code></pre><div class=\"lesson-trap\">⚠️ <code>while (!feof(f))</code> עם קריאה בתוך הגוף ועיבוד מיד אחריה, בלי לבדוק את ערך ההחזרה, היא הטעות הנפוצה במבחנים.</div>"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "step": {
       "type": "numeric",
       "answer": 4,
       "tol": 0,
       "prompt": "הקובץ מכיל `1 2 3` ואחרי ה-3 רווח אחד. כמה פעמים יתבצע גוף הלולאה?\n```c\nint x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &x);\n    printf(\"%d \", x);\n}\n```",
       "explain": "אחרי שנקרא 3, נשאר רווח בקובץ ו-`feof` עוד שקר, לכן הלולאה נכנסת פעם רביעית. הקריאה נכשלת בסוף הקובץ, והמשתנה `x` נשאר 3. הגוף רץ 4 פעמים והפלט `1 2 3 3`.",
       "promptHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">1 2 3</code> ואחרי ה-3 רווח אחד. כמה פעמים יתבצע גוף הלולאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &amp;x);\n    printf(\"%d \", x);\n}</code></pre>",
       "explainHtml": "אחרי שנקרא 3, נשאר רווח בקובץ ו-<code class=\"tok\" dir=\"ltr\">feof</code> עוד שקר, לכן הלולאה נכנסת פעם רביעית. הקריאה נכשלת בסוף הקובץ, והמשתנה <code class=\"tok\" dir=\"ltr\">x</code> נשאר 3. הגוף רץ 4 פעמים והפלט <code class=\"tok\" dir=\"ltr\">1 2 3 3</code>."
      },
      "recap": "`feof` נהיית אמת רק אחרי שהקריאה נכשלה.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">feof</code> נהיית אמת רק אחרי שהקריאה נכשלה."
     },
     {
      "id": "C04-Q2",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "אותה לולאה כמו בשאלה הקודמת, אבל הקובץ מכיל `1 2 3` **בלי** תו נוסף אחרי ה-3. כמה פעמים יתבצע הגוף?\n```c\nint x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &x);\n    printf(\"%d \", x);\n}\n```",
       "explain": "הקריאה של 3 מגיעה לסוף הקובץ בזמן שהיא בודקת אם המספר ממשיך, ולכן `feof` נהיית אמת מיד אחריה. הגוף רץ 3 פעמים. אותה לולאה, והתוצאה תלויה בתו האחרון בקובץ.",
       "promptHtml": "אותה לולאה כמו בשאלה הקודמת, אבל הקובץ מכיל <code class=\"tok\" dir=\"ltr\">1 2 3</code> <strong>בלי</strong> תו נוסף אחרי ה-3. כמה פעמים יתבצע הגוף?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &amp;x);\n    printf(\"%d \", x);\n}</code></pre>",
       "explainHtml": "הקריאה של 3 מגיעה לסוף הקובץ בזמן שהיא בודקת אם המספר ממשיך, ולכן <code class=\"tok\" dir=\"ltr\">feof</code> נהיית אמת מיד אחריה. הגוף רץ 3 פעמים. אותה לולאה, והתוצאה תלויה בתו האחרון בקובץ."
      },
      "recap": "התנהגות `while (!feof(f))` תלויה בתו האחרון, ולכן לא משתמשים בה.",
      "recapHtml": "התנהגות <code class=\"tok\" dir=\"ltr\">while (!feof(f))</code> תלויה בתו האחרון, ולכן לא משתמשים בה."
     },
     {
      "id": "C04-Q3",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "הקובץ מכיל שתי שורות: `a` ו-`b`, וכל אחת מסתיימת ב-`'\\n'`. כמה שורות יודפסו?\n```c\nchar line[10];\nwhile (!feof(f))\n{\n    fgets(line, 10, f);\n    fputs(line, stdout);\n}\n```",
       "explain": "אחרי הקריאה השנייה הקובץ עוד לא סומן כנגמר. הקריאה השלישית מחזירה `NULL` ואינה משנה את `line`, שעדיין מכיל `b\\n`, ולכן השורה `b` מודפסת פעם נוספת. הפלט הוא `a`, `b`, `b`: שלוש שורות.",
       "promptHtml": "הקובץ מכיל שתי שורות: <code class=\"tok\" dir=\"ltr\">a</code> ו-<code class=\"tok\" dir=\"ltr\">b</code>, וכל אחת מסתיימת ב-<code class=\"tok\" dir=\"ltr\">'\\n'</code>. כמה שורות יודפסו?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char line[10];\nwhile (!feof(f))\n{\n    fgets(line, 10, f);\n    fputs(line, stdout);\n}</code></pre>",
       "explainHtml": "אחרי הקריאה השנייה הקובץ עוד לא סומן כנגמר. הקריאה השלישית מחזירה <code class=\"tok\" dir=\"ltr\">NULL</code> ואינה משנה את <code class=\"tok\" dir=\"ltr\">line</code>, שעדיין מכיל <code class=\"tok\" dir=\"ltr\">b\\n</code>, ולכן השורה <code class=\"tok\" dir=\"ltr\">b</code> מודפסת פעם נוספת. הפלט הוא <code class=\"tok\" dir=\"ltr\">a</code>, <code class=\"tok\" dir=\"ltr\">b</code>, <code class=\"tok\" dir=\"ltr\">b</code>: שלוש שורות."
      },
      "recap": "קריאה שנכשלה משאירה את המחרוזת כפי שהייתה.",
      "recapHtml": "קריאה שנכשלה משאירה את המחרוזת כפי שהייתה."
     },
     {
      "id": "C04-Q4",
      "question": "הקובץ מכיל `ab`. מתבצעות שתי קריאות `fgetc(f)` (נקראים `a` ו-`b`). מה מחזירה `feof(f)` מיד אחריהן?",
      "options": [
       {
        "id": "a",
        "value": "ערך שקר (0), כי עוד לא ניסו לקרוא מעבר לסוף",
        "type": "text",
        "html": "ערך שקר (0), כי עוד לא ניסו לקרוא מעבר לסוף"
       },
       {
        "id": "b",
        "value": "ערך אמת, כי כל התווים כבר נקראו",
        "type": "text",
        "html": "ערך אמת, כי כל התווים כבר נקראו"
       },
       {
        "id": "c",
        "value": "ערך אמת, כי המצביע בסוף הקובץ",
        "type": "text",
        "html": "ערך אמת, כי המצביע בסוף הקובץ"
       },
       {
        "id": "d",
        "value": "ערך לא מוגדר",
        "type": "text",
        "html": "ערך לא מוגדר"
       }
      ],
      "correctId": "a",
      "explanation": "`feof` נהיית אמת רק אחרי קריאה שהגיעה מעבר לסוף. שתי הקריאות הצליחו, ולכן `feof` עדיין 0 (נבדק עם clang). רק הקריאה השלישית תחזיר `EOF` ותדליק את הדגל. בגלל זה הטענות על כך שהיא כבר אמת, בגלל שהכול נקרא או בגלל המיקום, שגויות. הערך מוגדר היטב.",
      "recap": "`feof` נהיית אמת אחרי קריאה שנכשלה, לא לפניה.",
      "questionHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">ab</code>. מתבצעות שתי קריאות <code class=\"tok\" dir=\"ltr\">fgetc(f)</code> (נקראים <code class=\"tok\" dir=\"ltr\">a</code> ו-<code class=\"tok\" dir=\"ltr\">b</code>). מה מחזירה <code class=\"tok\" dir=\"ltr\">feof(f)</code> מיד אחריהן?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">feof</code> נהיית אמת רק אחרי קריאה שהגיעה מעבר לסוף. שתי הקריאות הצליחו, ולכן <code class=\"tok\" dir=\"ltr\">feof</code> עדיין 0 (נבדק עם clang). רק הקריאה השלישית תחזיר <code class=\"tok\" dir=\"ltr\">EOF</code> ותדליק את הדגל. בגלל זה הטענות על כך שהיא כבר אמת, בגלל שהכול נקרא או בגלל המיקום, שגויות. הערך מוגדר היטב.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">feof</code> נהיית אמת אחרי קריאה שנכשלה, לא לפניה."
     },
     {
      "id": "C04-Q5",
      "question": "הקובץ מכיל `1 2 3` ואחרי ה-3 רווח. איזו לולאה מדפיסה כל מספר פעם אחת בדיוק (`1 2 3`) ?",
      "options": [
       {
        "id": "a",
        "value": "`while (fscanf(f, \"%d\", &x) == 1) printf(\"%d \", x);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">while (fscanf(f, \"%d\", &amp;x) == 1) printf(\"%d \", x);</code>"
       },
       {
        "id": "b",
        "value": "`while (!feof(f)) { fscanf(f, \"%d\", &x); printf(\"%d \", x); }`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">while (!feof(f)) { fscanf(f, \"%d\", &amp;x); printf(\"%d \", x); }</code>"
       },
       {
        "id": "c",
        "value": "`do { fscanf(f, \"%d\", &x); printf(\"%d \", x); } while (!feof(f));`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">do { fscanf(f, \"%d\", &amp;x); printf(\"%d \", x); } while (!feof(f));</code>"
       },
       {
        "id": "d",
        "value": "`while (feof(f) == 0) { fscanf(f, \"%d\", &x); printf(\"%d \", x); }`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">while (feof(f) == 0) { fscanf(f, \"%d\", &amp;x); printf(\"%d \", x); }</code>"
       }
      ],
      "correctId": "a",
      "explanation": "רק הראשונה בודקת את ערך ההחזרה של `fscanf`, ולכן נעצרת מיד כשהקריאה נכשלת. שלוש האחרות מדפיסות `1 2 3 3` (נבדק עם clang): השנייה והרביעית שקולות, והשלישית מדפיסה לפני שהיא בודקת כלום.",
      "recap": "בודקים את ערך ההחזרה של הקריאה, לא את `feof`.",
      "questionHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">1 2 3</code> ואחרי ה-3 רווח. איזו לולאה מדפיסה כל מספר פעם אחת בדיוק (<code class=\"tok\" dir=\"ltr\">1 2 3</code>) ?",
      "explanationHtml": "רק הראשונה בודקת את ערך ההחזרה של <code class=\"tok\" dir=\"ltr\">fscanf</code>, ולכן נעצרת מיד כשהקריאה נכשלת. שלוש האחרות מדפיסות <code class=\"tok\" dir=\"ltr\">1 2 3 3</code> (נבדק עם clang): השנייה והרביעית שקולות, והשלישית מדפיסה לפני שהיא בודקת כלום.",
      "recapHtml": "בודקים את ערך ההחזרה של הקריאה, לא את <code class=\"tok\" dir=\"ltr\">feof</code>."
     },
     {
      "id": "C04-Q6",
      "step": {
       "type": "order",
       "code": true,
       "prompt": "סדרו את לולאת ההעתקה של הקובץ למסך בצורה של קריאה לפני הלולאה (הגוף כולל את שתי השורות האחרונות).",
       "lines": [
        "int ch = fgetc(f);",
        "while (ch != EOF)",
        "putchar(ch);",
        "ch = fgetc(f);"
       ],
       "explain": "קוראים את התו הראשון, בודקים אותו בתנאי הלולאה, מדפיסים אותו, ורק אז קוראים את הבא. אם הקריאה הבאה הייתה לפני `putchar`, התו הנוכחי היה אובד.",
       "promptHtml": "סדרו את לולאת ההעתקה של הקובץ למסך בצורה של קריאה לפני הלולאה (הגוף כולל את שתי השורות האחרונות).",
       "explainHtml": "קוראים את התו הראשון, בודקים אותו בתנאי הלולאה, מדפיסים אותו, ורק אז קוראים את הבא. אם הקריאה הבאה הייתה לפני <code class=\"tok\" dir=\"ltr\">putchar</code>, התו הנוכחי היה אובד.",
       "linesHtml": [
        "int ch = fgetc(f);",
        "while (ch != EOF)",
        "putchar(ch);",
        "ch = fgetc(f);"
       ]
      },
      "recap": "קוראים לפני הלולאה, מעבדים, וקוראים שוב בסוף הגוף.",
      "recapHtml": "קוראים לפני הלולאה, מעבדים, וקוראים שוב בסוף הגוף."
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "💾",
    "title": "קבצים בינאריים: רשומות עם fwrite ו-fread",
    "goal": "אחרי השלב הזה אפשר לכתוב רשומות לקובץ בינארי, לקרוא אותן בלולאה ולסנן לפי תנאי.",
    "source": "ai-verified",
    "boss": false,
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
        "value": "`fwrite(&r, sizeof(r), 1, f);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fwrite(&amp;r, sizeof(r), 1, f);</code>"
       },
       {
        "id": "b",
        "value": "`fwrite(r, sizeof(r), 1, f);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fwrite(r, sizeof(r), 1, f);</code>"
       },
       {
        "id": "c",
        "value": "`fwrite(&r, sizeof(r.id), 1, f);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fwrite(&amp;r, sizeof(r.id), 1, f);</code>"
       },
       {
        "id": "d",
        "value": "`fprintf(f, \"%d %d\", r.id, r.score);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fprintf(f, \"%d %d\", r.id, r.score);</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`fwrite` מקבלת כתובת, ולכן `&r` נכון. התשובה בלי `&` לא עוברת הידור (מבנה במקום כתובת). התשובה עם `sizeof(r.id)` כותבת רק את השדה הראשון. `fprintf` כותבת טקסט באורך משתנה ולא רשומה בגודל קבוע.",
      "recap": "`fwrite(&r, sizeof(r), 1, f)` כותבת רשומה שלמה.",
      "questionHtml": "המשתנה <code class=\"tok\" dir=\"ltr\">r</code> הוא רשומה מטיפוס <code class=\"tok\" dir=\"ltr\">rec</code> (עם <code class=\"tok\" dir=\"ltr\">id</code> ו-<code class=\"tok\" dir=\"ltr\">score</code>). איזו שורה כותבת את הרשומה כולה כגוש בינארי אחד לקובץ שנפתח ב-<code class=\"tok\" dir=\"ltr\">\"wb\"</code> ?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fwrite</code> מקבלת כתובת, ולכן <code class=\"tok\" dir=\"ltr\">&amp;r</code> נכון. התשובה בלי <code class=\"tok\" dir=\"ltr\">&amp;</code> לא עוברת הידור (מבנה במקום כתובת). התשובה עם <code class=\"tok\" dir=\"ltr\">sizeof(r.id)</code> כותבת רק את השדה הראשון. <code class=\"tok\" dir=\"ltr\">fprintf</code> כותבת טקסט באורך משתנה ולא רשומה בגודל קבוע.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fwrite(&amp;r, sizeof(r), 1, f)</code> כותבת רשומה שלמה."
     },
     {
      "id": "C05-Q2",
      "step": {
       "type": "numeric",
       "answer": 3,
       "tol": 0,
       "prompt": "בקובץ בינארי חמש רשומות עם הציונים 50, 90, 70, 95, 60 (לפי הסדר). מה ערך `count` בסוף?\n```c\nrec a;\nint count = 0;\nwhile (fread(&a, sizeof(a), 1, f) == 1)\n    if (a.score >= 70)\n        count++;\n```",
       "explain": "הציונים שלפחות 70 הם 90, 70 ו-95: שלוש רשומות.",
       "promptHtml": "בקובץ בינארי חמש רשומות עם הציונים 50, 90, 70, 95, 60 (לפי הסדר). מה ערך <code class=\"tok\" dir=\"ltr\">count</code> בסוף?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>rec a;\nint count = 0;\nwhile (fread(&amp;a, sizeof(a), 1, f) == 1)\n    if (a.score &gt;= 70)\n        count++;</code></pre>",
       "explainHtml": "הציונים שלפחות 70 הם 90, 70 ו-95: שלוש רשומות."
      },
      "recap": "לולאת `fread` עוברת על כל הרשומות, והתנאי מסנן.",
      "recapHtml": "לולאת <code class=\"tok\" dir=\"ltr\">fread</code> עוברת על כל הרשומות, והתנאי מסנן."
     },
     {
      "id": "C05-Q3",
      "step": {
       "type": "numeric",
       "answer": 0,
       "tol": 0,
       "prompt": "בקובץ בינארי שתי רשומות בלבד. הקוד קורא שלוש פעמים ברצף `n = fread(&a, sizeof(a), 1, f);`. מה ערך `n` בקריאה השלישית?",
       "explain": "שתי הקריאות הראשונות מחזירות 1. אחרי הרשומה השנייה אין מה לקרוא, ולכן השלישית קוראת 0 רשומות ומחזירה 0.",
       "promptHtml": "בקובץ בינארי שתי רשומות בלבד. הקוד קורא שלוש פעמים ברצף <code class=\"tok\" dir=\"ltr\">n = fread(&amp;a, sizeof(a), 1, f);</code>. מה ערך <code class=\"tok\" dir=\"ltr\">n</code> בקריאה השלישית?",
       "explainHtml": "שתי הקריאות הראשונות מחזירות 1. אחרי הרשומה השנייה אין מה לקרוא, ולכן השלישית קוראת 0 רשומות ומחזירה 0."
      },
      "recap": "`fread` מחזירה 0 בסוף הקובץ.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fread</code> מחזירה 0 בסוף הקובץ."
     },
     {
      "id": "C05-Q4",
      "question": "כותבים קודם את הערך 7 ואחר כך את הערך 1234567 (כל אחד לקובץ חדש). מה נכון?",
      "options": [
       {
        "id": "a",
        "value": "ב-`fwrite(&x, sizeof(int), 1, f)` שני הקבצים באותו גודל, וב-`fprintf(f, \"%d\", x)` הקובץ של 1234567 גדול יותר",
        "type": "text",
        "html": "ב-<code class=\"tok\" dir=\"ltr\">fwrite(&amp;x, sizeof(int), 1, f)</code> שני הקבצים באותו גודל, וב-<code class=\"tok\" dir=\"ltr\">fprintf(f, \"%d\", x)</code> הקובץ של 1234567 גדול יותר"
       },
       {
        "id": "b",
        "value": "ב-`fprintf(f, \"%d\", x)` שני הקבצים באותו גודל, וב-`fwrite` הקובץ של 1234567 גדול יותר",
        "type": "text",
        "html": "ב-<code class=\"tok\" dir=\"ltr\">fprintf(f, \"%d\", x)</code> שני הקבצים באותו גודל, וב-<code class=\"tok\" dir=\"ltr\">fwrite</code> הקובץ של 1234567 גדול יותר"
       },
       {
        "id": "c",
        "value": "בשתי השיטות שני הקבצים באותו גודל",
        "type": "text",
        "html": "בשתי השיטות שני הקבצים באותו גודל"
       },
       {
        "id": "d",
        "value": "בשתי השיטות הקובץ של 1234567 גדול יותר",
        "type": "text",
        "html": "בשתי השיטות הקובץ של 1234567 גדול יותר"
       }
      ],
      "correctId": "a",
      "explanation": "`fwrite` כותבת תמיד `sizeof(int)` בתים, בלי קשר לערך. `fprintf` כותבת את הספרות כתווים, ולכן 7 הוא תו אחד ו-1234567 הוא שבעה תווים (נבדק עם clang). שתי התשובות האחרונות אינן מתאימות לאף אחת מהשיטות, והשנייה הפוכה.",
      "recap": "ב-`fwrite` הגודל קבוע, בטקסט הוא תלוי במספר הספרות.",
      "questionHtml": "כותבים קודם את הערך 7 ואחר כך את הערך 1234567 (כל אחד לקובץ חדש). מה נכון?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">fwrite</code> כותבת תמיד <code class=\"tok\" dir=\"ltr\">sizeof(int)</code> בתים, בלי קשר לערך. <code class=\"tok\" dir=\"ltr\">fprintf</code> כותבת את הספרות כתווים, ולכן 7 הוא תו אחד ו-1234567 הוא שבעה תווים (נבדק עם clang). שתי התשובות האחרונות אינן מתאימות לאף אחת מהשיטות, והשנייה הפוכה.",
      "recapHtml": "ב-<code class=\"tok\" dir=\"ltr\">fwrite</code> הגודל קבוע, בטקסט הוא תלוי במספר הספרות."
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
       "explain": "התנאי צריך להיות `&&`: שני התנאים חייבים להתקיים. עם `||` מספיק שאחד מהם מתקיים וכל ארבע הדירות נספרות.",
       "promptHtml": "הפונקציה אמורה לספור דירות עם <code class=\"tok\" dir=\"ltr\">rooms</code> חדרים ומחיר של לכל היותר <code class=\"tok\" dir=\"ltr\">max_price</code>. בקובץ ארבע דירות: (3 חדרים, 500), (2, 400), (3, 900), (4, 300). הקריאה <code class=\"tok\" dir=\"ltr\">count_matching(name, 3, 600)</code> צריכה להחזיר 1 אבל מחזירה 4. איזו שורה שגויה?",
       "explainHtml": "התנאי צריך להיות <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code>: שני התנאים חייבים להתקיים. עם <code class=\"tok\" dir=\"ltr\">||</code> מספיק שאחד מהם מתקיים וכל ארבע הדירות נספרות.",
       "linesHtml": [
        "FILE *f = fopen(name, \"rb\");",
        "apartment a;",
        "int count = 0;",
        "if (!f) return -1;",
        "while (fread(&amp;a, sizeof(apartment), 1, f) == 1)",
        "    if (a.rooms == rooms || a.price &lt;= max_price)",
        "        count++;",
        "fclose(f);",
        "return count;"
       ]
      },
      "recap": "סינון לפי שני תנאים משתמש ב-`&&`.",
      "recapHtml": "סינון לפי שני תנאים משתמש ב-<code class=\"tok\" dir=\"ltr\">&amp;&amp;</code>."
     },
     {
      "id": "C05-Q6",
      "step": {
       "type": "order",
       "code": true,
       "prompt": "סדרו את הפונקציה שמדפיסה את ה-`id` של כל הרשומות בקובץ הבינארי.",
       "lines": [
        "rec a; FILE *f = fopen(\"recs.bin\", \"rb\");",
        "if (!f) return;",
        "while (fread(&a, sizeof(a), 1, f) == 1)",
        "    printf(\"%d\\n\", a.id);",
        "fclose(f);"
       ],
       "explain": "מצהירים ופותחים, בודקים, קוראים בלולאה ואז סוגרים. הגוף של הלולאה בא מיד אחרי תנאי הלולאה.",
       "promptHtml": "סדרו את הפונקציה שמדפיסה את ה-<code class=\"tok\" dir=\"ltr\">id</code> של כל הרשומות בקובץ הבינארי.",
       "explainHtml": "מצהירים ופותחים, בודקים, קוראים בלולאה ואז סוגרים. הגוף של הלולאה בא מיד אחרי תנאי הלולאה.",
       "linesHtml": [
        "rec a; FILE *f = fopen(\"recs.bin\", \"rb\");",
        "if (!f) return;",
        "while (fread(&amp;a, sizeof(a), 1, f) == 1)",
        "    printf(\"%d\\n\", a.id);",
        "fclose(f);"
       ]
      },
      "recap": "קריאה בינארית: פותחים עם `\"rb\"`, בודקים, לולאת `fread`, סוגרים.",
      "recapHtml": "קריאה בינארית: פותחים עם <code class=\"tok\" dir=\"ltr\">\"rb\"</code>, בודקים, לולאת <code class=\"tok\" dir=\"ltr\">fread</code>, סוגרים."
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "🧭",
    "title": "מיקום בקובץ: ftell, fseek ו-rewind",
    "goal": "אחרי השלב הזה אפשר לדעת איפה הסמן בקובץ, לקפוץ למקום מסוים, לחזור להתחלה ולחשב גודל קובץ.",
    "source": "ai-verified",
    "boss": false,
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
       "explain": "כל `fgetc` מקדמת את הסמן בבית אחד. אחרי שלוש קריאות הסמן במקום 3.",
       "promptHtml": "הקובץ (נפתח כבינארי) מכיל <code class=\"tok\" dir=\"ltr\">ABCDEFGH</code>. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>fgetc(f);\nfgetc(f);\nfgetc(f);\nprintf(\"%ld\", ftell(f));</code></pre>",
       "explainHtml": "כל <code class=\"tok\" dir=\"ltr\">fgetc</code> מקדמת את הסמן בבית אחד. אחרי שלוש קריאות הסמן במקום 3."
      },
      "recap": "`ftell` שווה למספר הבתים שכבר עברנו.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">ftell</code> שווה למספר הבתים שכבר עברנו."
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
       "explain": "המיקומים מתחילים ב-0: `A` ב-0, `B` ב-1, `C` ב-2. אחרי `fseek(f, 2, SEEK_SET)` הקריאה מחזירה `C`.",
       "promptHtml": "הקובץ (בינארי) מכיל <code class=\"tok\" dir=\"ltr\">ABCDEFGH</code>. איזה תו יודפס?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>fseek(f, 2, SEEK_SET);\nputchar(fgetc(f));</code></pre>",
       "explainHtml": "המיקומים מתחילים ב-0: <code class=\"tok\" dir=\"ltr\">A</code> ב-0, <code class=\"tok\" dir=\"ltr\">B</code> ב-1, <code class=\"tok\" dir=\"ltr\">C</code> ב-2. אחרי <code class=\"tok\" dir=\"ltr\">fseek(f, 2, SEEK_SET)</code> הקריאה מחזירה <code class=\"tok\" dir=\"ltr\">C</code>."
      },
      "recap": "`SEEK_SET` סופר מההתחלה, והתו הראשון במקום 0.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">SEEK_SET</code> סופר מההתחלה, והתו הראשון במקום 0."
     },
     {
      "id": "C06-Q3",
      "step": {
       "type": "numeric",
       "answer": 8,
       "tol": 0,
       "prompt": "הקובץ (בינארי) מכיל `ABCDEFGH`. מה ידפיס הקוד?\n```c\nfseek(f, 0, SEEK_END);\nprintf(\"%ld\", ftell(f));\n```",
       "explain": "הקפיצה לסוף מציבה את הסמן במקום שאחרי התו האחרון, והוא שווה לגודל הקובץ בבתים: 8.",
       "promptHtml": "הקובץ (בינארי) מכיל <code class=\"tok\" dir=\"ltr\">ABCDEFGH</code>. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>fseek(f, 0, SEEK_END);\nprintf(\"%ld\", ftell(f));</code></pre>",
       "explainHtml": "הקפיצה לסוף מציבה את הסמן במקום שאחרי התו האחרון, והוא שווה לגודל הקובץ בבתים: 8."
      },
      "recap": "גודל קובץ: `fseek(f, 0, SEEK_END)` ואז `ftell`.",
      "recapHtml": "גודל קובץ: <code class=\"tok\" dir=\"ltr\">fseek(f, 0, SEEK_END)</code> ואז <code class=\"tok\" dir=\"ltr\">ftell</code>."
     },
     {
      "id": "C06-Q4",
      "question": "הקובץ בינארי והוא מכיל רשומות מטיפוס `rec` ברצף. איזו שורה מציבה את הסמן בתחילת הרשומה שמספרה `i` (הראשונה היא 0) ?",
      "options": [
       {
        "id": "a",
        "value": "`fseek(f, i * sizeof(rec), SEEK_SET);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fseek(f, i * sizeof(rec), SEEK_SET);</code>"
       },
       {
        "id": "b",
        "value": "`fseek(f, (i + 1) * sizeof(rec), SEEK_SET);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fseek(f, (i + 1) * sizeof(rec), SEEK_SET);</code>"
       },
       {
        "id": "c",
        "value": "`fseek(f, i + sizeof(rec), SEEK_SET);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fseek(f, i + sizeof(rec), SEEK_SET);</code>"
       },
       {
        "id": "d",
        "value": "`fseek(f, i, SEEK_SET);`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">fseek(f, i, SEEK_SET);</code>"
       }
      ],
      "correctId": "a",
      "explanation": "לפני רשומה `i` יש `i` רשומות, שכל אחת מהן `sizeof(rec)` בתים, ולכן ההיסט הוא `i * sizeof(rec)` (נבדק עם clang, רשומה 2 מתוך ארבע נקראה נכון). עם `i + 1` מגיעים לרשומה הבאה. עם חיבור או עם `i` בלבד מגיעים לאמצע רשומה.",
      "recap": "רשומה `i` נמצאת בהיסט `i * sizeof(rec)`.",
      "questionHtml": "הקובץ בינארי והוא מכיל רשומות מטיפוס <code class=\"tok\" dir=\"ltr\">rec</code> ברצף. איזו שורה מציבה את הסמן בתחילת הרשומה שמספרה <code class=\"tok\" dir=\"ltr\">i</code> (הראשונה היא 0) ?",
      "explanationHtml": "לפני רשומה <code class=\"tok\" dir=\"ltr\">i</code> יש <code class=\"tok\" dir=\"ltr\">i</code> רשומות, שכל אחת מהן <code class=\"tok\" dir=\"ltr\">sizeof(rec)</code> בתים, ולכן ההיסט הוא <code class=\"tok\" dir=\"ltr\">i * sizeof(rec)</code> (נבדק עם clang, רשומה 2 מתוך ארבע נקראה נכון). עם <code class=\"tok\" dir=\"ltr\">i + 1</code> מגיעים לרשומה הבאה. עם חיבור או עם <code class=\"tok\" dir=\"ltr\">i</code> בלבד מגיעים לאמצע רשומה.",
      "recapHtml": "רשומה <code class=\"tok\" dir=\"ltr\">i</code> נמצאת בהיסט <code class=\"tok\" dir=\"ltr\">i * sizeof(rec)</code>."
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
       "explain": "אחרי שתי קריאות הסמן במקום 2. `SEEK_CUR` עם 1 מזיז אותו למקום 3, והתו שם הוא `D`.",
       "promptHtml": "הקובץ (בינארי) מכיל <code class=\"tok\" dir=\"ltr\">ABCDEFGH</code>. איזה תו יודפס?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>fgetc(f);\nfgetc(f);\nfseek(f, 1, SEEK_CUR);\nputchar(fgetc(f));</code></pre>",
       "explainHtml": "אחרי שתי קריאות הסמן במקום 2. <code class=\"tok\" dir=\"ltr\">SEEK_CUR</code> עם 1 מזיז אותו למקום 3, והתו שם הוא <code class=\"tok\" dir=\"ltr\">D</code>."
      },
      "recap": "`SEEK_CUR` זז יחסית למקום הנוכחי.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">SEEK_CUR</code> זז יחסית למקום הנוכחי."
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
       "explain": "אחרי המעבר הראשון הסמן בסוף הקובץ. כדי שהמעבר השני יקרא את הרשומות צריך להחזיר אותו להתחלה עם `rewind(f)`. הקפיצה לסוף משאירה אותו שם והמעבר השני לא קורא כלום.",
       "promptHtml": "הקוד אמור לטעון את כל הרשומות של קובץ בינארי למערך, אבל כל איברי המערך נשארים אפסים. איזו שורה שגויה?",
       "explainHtml": "אחרי המעבר הראשון הסמן בסוף הקובץ. כדי שהמעבר השני יקרא את הרשומות צריך להחזיר אותו להתחלה עם <code class=\"tok\" dir=\"ltr\">rewind(f)</code>. הקפיצה לסוף משאירה אותו שם והמעבר השני לא קורא כלום.",
       "linesHtml": [
        "FILE *f = fopen(name, \"rb\");",
        "rec a, *arr;",
        "int n = 0, i = 0;",
        "while (fread(&amp;a, sizeof(a), 1, f) == 1)",
        "    n++;",
        "fseek(f, 0, SEEK_END);",
        "arr = (rec *)calloc(n, sizeof(rec));",
        "while (fread(&amp;a, sizeof(a), 1, f) == 1)",
        "    arr[i++] = a;"
       ]
      },
      "recap": "בין שני מעברים על הקובץ מחזירים את הסמן להתחלה עם `rewind`.",
      "recapHtml": "בין שני מעברים על הקובץ מחזירים את הסמן להתחלה עם <code class=\"tok\" dir=\"ltr\">rewind</code>."
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "🧩",
    "title": "תבניות מהמבחן: מילה שלמה, סינון שורות, טקסט לבינארי",
    "goal": "אחרי השלב הזה אפשר לכתוב את שלושת סוגי הפונקציות שחוזרות במבחנים: ספירת מילה שלמה, סינון שורות לקובץ חדש והמרת טקסט לרשומות.",
    "source": "ai-verified",
    "boss": false,
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
       "explain": "`strstr` מצליחה בכל מילה שמכילה את `live`: `live`, `lives`, `alive`, `live`. התוצאה היא 4, בעוד ש-`strcmp(buf, \"live\") == 0` הייתה סופרת רק 2 מילים שלמות.",
       "promptHtml": "הקובץ מכיל בשורה אחת <code class=\"tok\" dir=\"ltr\">live lives alive live</code>. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char buf[101];\nint count = 0;\nwhile (fscanf(f, \"%100s\", buf) == 1)\n    if (strstr(buf, \"live\"))\n        count++;\nprintf(\"%d\", count);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">strstr</code> מצליחה בכל מילה שמכילה את <code class=\"tok\" dir=\"ltr\">live</code>: <code class=\"tok\" dir=\"ltr\">live</code>, <code class=\"tok\" dir=\"ltr\">lives</code>, <code class=\"tok\" dir=\"ltr\">alive</code>, <code class=\"tok\" dir=\"ltr\">live</code>. התוצאה היא 4, בעוד ש-<code class=\"tok\" dir=\"ltr\">strcmp(buf, \"live\") == 0</code> הייתה סופרת רק 2 מילים שלמות."
      },
      "recap": "מילה שלמה: `strcmp == 0`, לא `strstr`.",
      "recapHtml": "מילה שלמה: <code class=\"tok\" dir=\"ltr\">strcmp == 0</code>, לא <code class=\"tok\" dir=\"ltr\">strstr</code>."
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
       "explain": "`%9s` קוראת לכל היותר 9 תווים: `123456789`, ושומרת את המקום העשירי ל-`'\\0'`. שאר הספרות נשארות בקובץ לקריאה הבאה.",
       "promptHtml": "הקובץ מכיל <code class=\"tok\" dir=\"ltr\">1234567890123</code>. מה יודפס?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char id[10];\nfscanf(f, \"%9s\", id);\nprintf(\"%s\", id);</code></pre>",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">%9s</code> קוראת לכל היותר 9 תווים: <code class=\"tok\" dir=\"ltr\">123456789</code>, ושומרת את המקום העשירי ל-<code class=\"tok\" dir=\"ltr\">'\\0'</code>. שאר הספרות נשארות בקובץ לקריאה הבאה."
      },
      "recap": "רוחב הקריאה קטן ב-1 מגודל המערך.",
      "recapHtml": "רוחב הקריאה קטן ב-1 מגודל המערך."
     },
     {
      "id": "C07-Q3",
      "question": "איזו מהמחרוזות הבאות מקבלת 1 מהפונקציה `has_unique_letters` שבשיעור (רק אותיות, כולן שונות, גדולה וקטנה נחשבות אותה אות) ?",
      "options": [
       {
        "id": "a",
        "value": "`Table`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">Table</code>"
       },
       {
        "id": "b",
        "value": "`Alisa`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">Alisa</code>"
       },
       {
        "id": "c",
        "value": "`ab#c`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">ab#c</code>"
       },
       {
        "id": "d",
        "value": "`Noon`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">Noon</code>"
       }
      ],
      "correctId": "a",
      "explanation": "ב-`Table` כל חמש האותיות שונות (נבדק עם clang). ב-`Alisa` יש `A` ו-`a`, שנחשבות לאותה אות. ב-`ab#c` יש תו שאינו אות. ב-`Noon` האות `n` חוזרת פעמיים (`N` ו-`n`).",
      "recap": "מערך מונים של 26 אותיות עם `tolower` בודק שכל אות מופיעה פעם אחת.",
      "questionHtml": "איזו מהמחרוזות הבאות מקבלת 1 מהפונקציה <code class=\"tok\" dir=\"ltr\">has_unique_letters</code> שבשיעור (רק אותיות, כולן שונות, גדולה וקטנה נחשבות אותה אות) ?",
      "explanationHtml": "ב-<code class=\"tok\" dir=\"ltr\">Table</code> כל חמש האותיות שונות (נבדק עם clang). ב-<code class=\"tok\" dir=\"ltr\">Alisa</code> יש <code class=\"tok\" dir=\"ltr\">A</code> ו-<code class=\"tok\" dir=\"ltr\">a</code>, שנחשבות לאותה אות. ב-<code class=\"tok\" dir=\"ltr\">ab#c</code> יש תו שאינו אות. ב-<code class=\"tok\" dir=\"ltr\">Noon</code> האות <code class=\"tok\" dir=\"ltr\">n</code> חוזרת פעמיים (<code class=\"tok\" dir=\"ltr\">N</code> ו-<code class=\"tok\" dir=\"ltr\">n</code>).",
      "recapHtml": "מערך מונים של 26 אותיות עם <code class=\"tok\" dir=\"ltr\">tolower</code> בודק שכל אות מופיעה פעם אחת."
     },
     {
      "id": "C07-Q4",
      "step": {
       "type": "numeric",
       "answer": 2,
       "tol": 0,
       "prompt": "קובץ הקלט מכיל ארבע שורות: `abcd`, `ab`, `abcde` ו-`x` (כל אחת מסתיימת ב-`'\\n'`). הפונקציה מהשיעור מעתיקה לקובץ הפלט רק שורות שאורכן (בלי `'\\n'`) גדול מ-3. כמה שורות יהיו בקובץ הפלט?",
       "explain": "האורכים הם 4, 2, 5 ו-1. רק `abcd` ו-`abcde` עומדות בתנאי, ולכן בקובץ הפלט שתי שורות.",
       "promptHtml": "קובץ הקלט מכיל ארבע שורות: <code class=\"tok\" dir=\"ltr\">abcd</code>, <code class=\"tok\" dir=\"ltr\">ab</code>, <code class=\"tok\" dir=\"ltr\">abcde</code> ו-<code class=\"tok\" dir=\"ltr\">x</code> (כל אחת מסתיימת ב-<code class=\"tok\" dir=\"ltr\">'\\n'</code>). הפונקציה מהשיעור מעתיקה לקובץ הפלט רק שורות שאורכן (בלי <code class=\"tok\" dir=\"ltr\">'\\n'</code>) גדול מ-3. כמה שורות יהיו בקובץ הפלט?",
       "explainHtml": "האורכים הם 4, 2, 5 ו-1. רק <code class=\"tok\" dir=\"ltr\">abcd</code> ו-<code class=\"tok\" dir=\"ltr\">abcde</code> עומדות בתנאי, ולכן בקובץ הפלט שתי שורות."
      },
      "recap": "מסירים את `'\\n'` לפני שבודקים אורך.",
      "recapHtml": "מסירים את <code class=\"tok\" dir=\"ltr\">'\\n'</code> לפני שבודקים אורך."
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
       "explain": "`sizeof(c.id)` הוא גודל השדה הראשון בלבד. כל רשומה חייבת להיכתב בשלמותה עם `sizeof(clientData)`.",
       "promptHtml": "הפונקציה אמורה להמיר כל שורה בקובץ הטקסט לרשומה בינארית שלמה, אבל הקובץ הבינארי יוצא קטן מדי ורשומות נקראות ממנו בצורה שבורה. איזו שורה שגויה?",
       "explainHtml": "<code class=\"tok\" dir=\"ltr\">sizeof(c.id)</code> הוא גודל השדה הראשון בלבד. כל רשומה חייבת להיכתב בשלמותה עם <code class=\"tok\" dir=\"ltr\">sizeof(clientData)</code>.",
       "linesHtml": [
        "clientData c;",
        "FILE *in = fopen(text_name, \"r\");",
        "FILE *out = fopen(binary_name, \"wb\");",
        "if (!in || !out) exit(1);",
        "while (fscanf(in, \"%9s%30s%lf\", c.id, c.name, &amp;c.total) == 3)",
        "    fwrite(&amp;c, sizeof(c.id), 1, out);",
        "fclose(in);",
        "fclose(out);"
       ]
      },
      "recap": "כותבים רשומה שלמה: `sizeof` של המבנה, לא של שדה.",
      "recapHtml": "כותבים רשומה שלמה: <code class=\"tok\" dir=\"ltr\">sizeof</code> של המבנה, לא של שדה."
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
       "explain": "פותחים את שני הקבצים, בודקים אותם, מעתיקים שורה אחר שורה (`fgets` משאירה את `'\\n'` ולכן `fputs` מספיקה) וסוגרים.",
       "promptHtml": "סדרו את הפונקציה שמעתיקה את כל השורות מקובץ טקסט אחד לאחר (כל פקודה היא בלוק לוגי אחד).",
       "explainHtml": "פותחים את שני הקבצים, בודקים אותם, מעתיקים שורה אחר שורה (<code class=\"tok\" dir=\"ltr\">fgets</code> משאירה את <code class=\"tok\" dir=\"ltr\">'\\n'</code> ולכן <code class=\"tok\" dir=\"ltr\">fputs</code> מספיקה) וסוגרים.",
       "linesHtml": [
        "FILE *in = fopen(src, \"r\"), *out = fopen(dst, \"w\");",
        "if (!in || !out) return;",
        "while (fgets(line, 101, in))",
        "    fputs(line, out);",
        "fclose(in); fclose(out);"
       ]
      },
      "recap": "העתקת שורות: `while (fgets(...)) fputs(...)`.",
      "recapHtml": "העתקת שורות: <code class=\"tok\" dir=\"ltr\">while (fgets(...)) fputs(...)</code>."
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🏆",
    "title": "מבחן גמר: שאלות מהמבחן",
    "goal": "אחרי השלב הזה אפשר לפתור שאלות קבצים בגודל של שאלת מבחן אמיתית.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "<p>ארבע שאלות אמיתיות מהמבחנים, חלקן עם צעדים מודרכים. לפני שכותבים קוד, עוברים על הרשימה:</p><ul><li>איזה סוג קובץ זה (טקסט או בינארי) ואיזו קריאה מתאימה: <code>fscanf</code> למילים ומספרים, <code>fgets</code> לשורות, <code>fgetc</code> לתווים, <code>fread</code> לרשומות?</li><li>מה מחזירים אם הקובץ לא נפתח?</li><li>האם צריך את <code>'\\n'</code>: מורידים אחרי <code>fgets</code>, וכותבים אותו חזרה עם <code>\"%s\\n\"</code>?</li><li>בשאלות פלט: רושמים אחרי כל קריאה מה נקרא ואיפה הסמן, ולא סומכים על <code>feof</code>.</li><li>סוגרים את כל הקבצים בכל מסלול יציאה.</li></ul><div class=\"lesson-rule\">🔑 בודקים את ערך ההחזרה של הקריאה עצמה, ולא את <code>feof</code>: <code>fscanf == 1</code>, <code>fgets != NULL</code>, <code>fread == 1</code>.</div>"
    },
    "questions": [
     {
      "bankId": "24B-A-Q6",
      "recap": "`fgets(st, 2, f)` קוראת תו אחד בכל קריאה, והקריאה הפנימית בלולאה צורכת את התו הבא.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">fgets(st, 2, f)</code> קוראת תו אחד בכל קריאה, והקריאה הפנימית בלולאה צורכת את התו הבא."
     },
     {
      "bankId": "25B-A-Q3",
      "recap": "מילה שלמה: `fscanf` עם `%100s` ו-`strcmp`, כשמחזירים `-1` אם הקובץ לא נפתח.",
      "recapHtml": "מילה שלמה: <code class=\"tok\" dir=\"ltr\">fscanf</code> עם <code class=\"tok\" dir=\"ltr\">%100s</code> ו-<code class=\"tok\" dir=\"ltr\">strcmp</code>, כשמחזירים <code class=\"tok\" dir=\"ltr\">-1</code> אם הקובץ לא נפתח."
     },
     {
      "bankId": "25B-B-Q3",
      "recap": "טקסט לבינארי: `fscanf` עם `%9s%30s%lf` והכתיבה של הרשומה כולה עם `fwrite`.",
      "recapHtml": "טקסט לבינארי: <code class=\"tok\" dir=\"ltr\">fscanf</code> עם <code class=\"tok\" dir=\"ltr\">%9s%30s%lf</code> והכתיבה של הרשומה כולה עם <code class=\"tok\" dir=\"ltr\">fwrite</code>."
     },
     {
      "bankId": "24B-B-Q3",
      "recap": "סינון שורות: הסרת `'\\n'`, פונקציית עזר לאותיות שונות, ושורות הפוכות לקובץ הפלט.",
      "recapHtml": "סינון שורות: הסרת <code class=\"tok\" dir=\"ltr\">'\\n'</code>, פונקציית עזר לאותיות שונות, ושורות הפוכות לקובץ הפלט."
     }
    ]
   }
  ]
 },
 "linked_lists": {
  "levels": [
   {
    "id": "C01",
    "order": 1,
    "icon": "🔗",
    "title": "איבר, ראש ומעבר ראשון",
    "goal": "אחרי השלב הזה אפשר להגדיר איבר ברשימה מקושרת, להסביר מה זה ראש ו-NULL, ולעבור על כל האיברים בלולאה.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p><b>רשימה מקושרת</b> היא סדרה של איברים שמוקצים כל אחד לחוד בזיכרון. כל איבר מחזיק נתון וגם כתובת של האיבר הבא. כך אין צורך בבלוק רציף אחד כמו במערך.</p>\n    <p>האיבר מוגדר כמבנה (struct) שמצביע על מבנה מאותו סוג:</p>\n    <pre><code>typedef struct item\n{\n    int data;\n    struct item *next;\n} Item;</code></pre>\n    <div class=\"lesson-rule\">🔑 בתוך ההגדרה השם <code>Item</code> עדיין לא קיים (הוא נוצר רק בסוף ה-typedef), ולכן שדה ההמשך נכתב <code>struct item *next</code>. לכן חשוב לתת למבנה שם, כאן <code>item</code>.</div>\n    <h3>הראש וסוף הרשימה</h3>\n    <ul>\n      <li>הרשימה כולה מיוצגת על ידי <b>מצביע לאיבר הראשון</b>, שנקרא ראש (<code>head</code>).</li>\n      <li>האיבר האחרון מצביע ל-<code>NULL</code>. אין אורך שמור בשום מקום, ולכן הסוף מזוהה רק לפי NULL.</li>\n      <li>רשימה ריקה היא <code>head == NULL</code>.</li>\n      <li>לשדה של איבר שמצביעים עליו ניגשים עם החץ: <code>p-&gt;data</code> ו-<code>p-&gt;next</code>.</li>\n    </ul>\n    <h3>מעבר על הרשימה</h3>\n    <pre><code>Item *p;\nfor (p = head; p; p = p-&gt;next)\n    printf(\"%d \", p-&gt;data);</code></pre>\n    <p>התנאי <code>p</code> הוא קיצור של <code>p != NULL</code>. הלולאה מסתיימת כש-<code>p</code> הגיע ל-NULL, כלומר אחרי האיבר האחרון.</p>\n    <div class=\"lesson-ex\">דוגמה: הרשימה <code>3 → 5 → 2</code>. אחרי <code>p = head</code> מתקבל <code>p-&gt;data == 3</code>. אחרי <code>p = p-&gt;next</code> מתקבל 5, אחר כך 2, ואז <code>p == NULL</code> והלולאה נעצרת. הביטוי <code>head-&gt;next-&gt;data</code> הוא 5.</div>\n    <div class=\"lesson-trap\">⚠️ רשימה ריקה: אסור לכתוב <code>head-&gt;data</code> כש-<code>head == NULL</code>, זו גישה ל-NULL וקריסה. לולאת <code>for (p = head; p; ...)</code> בטוחה, כי היא בכלל לא נכנסת.</div>"
    },
    "questions": [
     {
      "id": "C01-Q1",
      "question": "מגדירים:\n```c\ntypedef struct {\n    int data;\n    Item *next;\n} Item;\n```\nמה קורה בהידור?",
      "options": [
       {
        "id": "a",
        "value": "שגיאת הידור: השם `Item` עדיין לא מוכר בתוך ההגדרה",
        "type": "text",
        "html": "שגיאת הידור: השם <code class=\"tok\" dir=\"ltr\">Item</code> עדיין לא מוכר בתוך ההגדרה"
       },
       {
        "id": "b",
        "value": "ההידור תקין והרשימה תעבוד כרגיל",
        "type": "text",
        "html": "ההידור תקין והרשימה תעבוד כרגיל"
       },
       {
        "id": "c",
        "value": "ההידור תקין, אבל `next` תמיד יהיה `NULL`",
        "type": "text",
        "html": "ההידור תקין, אבל <code class=\"tok\" dir=\"ltr\">next</code> תמיד יהיה <code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "d",
        "value": "אזהרה בלבד, והמבנה יתפוס זיכרון אינסופי",
        "type": "text",
        "html": "אזהרה בלבד, והמבנה יתפוס זיכרון אינסופי"
       }
      ],
      "correctId": "a",
      "explanation": "השם `Item` נוצר רק אחרי שה-typedef נגמר, ולכן בתוך המבנה הוא לא מוכר והקומפיילר מדווח על שגיאה (נבדק עם clang). הפתרון: לתת למבנה שם ולכתוב `struct item *next`. שאר התשובות מניחות שההידור עובר, וזה לא קורה.",
      "recap": "בתוך המבנה כותבים `struct item *next`, לא `Item *next`.",
      "questionHtml": "מגדירים:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct {\n    int data;\n    Item *next;\n} Item;</code></pre>מה קורה בהידור?",
      "explanationHtml": "השם <code class=\"tok\" dir=\"ltr\">Item</code> נוצר רק אחרי שה-typedef נגמר, ולכן בתוך המבנה הוא לא מוכר והקומפיילר מדווח על שגיאה (נבדק עם clang). הפתרון: לתת למבנה שם ולכתוב <code class=\"tok\" dir=\"ltr\">struct item *next</code>. שאר התשובות מניחות שההידור עובר, וזה לא קורה.",
      "recapHtml": "בתוך המבנה כותבים <code class=\"tok\" dir=\"ltr\">struct item *next</code>, לא <code class=\"tok\" dir=\"ltr\">Item *next</code>."
     },
     {
      "id": "C01-Q2",
      "step": {
       "type": "numeric",
       "prompt": "הרשימה היא `3 → 5 → 2 → 4` ו-`head` מצביע על האיבר הראשון. מה ידפיס הקוד?\n```c\nint s = 0;\nItem *p;\nfor (p = head; p; p = p->next)\n    s += p->data;\nprintf(\"%d\", s);\n```",
       "answer": 14,
       "tol": 0,
       "explain": "הלולאה עוברת על כל ארבעת האיברים וסוכמת: $3+5+2+4=14$.",
       "promptHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">3 → 5 → 2 → 4</code> ו-<code class=\"tok\" dir=\"ltr\">head</code> מצביע על האיבר הראשון. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int s = 0;\nItem *p;\nfor (p = head; p; p = p-&gt;next)\n    s += p-&gt;data;\nprintf(\"%d\", s);</code></pre>",
       "explainHtml": "הלולאה עוברת על כל ארבעת האיברים וסוכמת: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>3</mn><mo>+</mo><mn>5</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>14</mn></mrow><annotation encoding=\"application/x-tex\">3+5+2+4=14</annotation></semantics></math></span>."
      },
      "recap": "הלולאה `for (p = head; p; p = p->next)` מבקרת בכל איבר פעם אחת.",
      "recapHtml": "הלולאה <code class=\"tok\" dir=\"ltr\">for (p = head; p; p = p-&gt;next)</code> מבקרת בכל איבר פעם אחת."
     },
     {
      "id": "C01-Q3",
      "question": "הרשימה היא `3 → 5 → 2 → 4` ו-`head` מצביע על האיבר הראשון. מה הערך של `head->next->next->data` ?",
      "options": [
       {
        "id": "a",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       },
       {
        "id": "b",
        "value": "`3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3</code>"
       },
       {
        "id": "c",
        "value": "`5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">5</code>"
       },
       {
        "id": "d",
        "value": "`4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4</code>"
       }
      ],
      "correctId": "a",
      "explanation": "`head` הוא האיבר 3, `head->next` הוא 5, `head->next->next` הוא 2, ולכן התוצאה 2. התשובה 5 היא `head->next->data`, והתשובה 3 היא `head->data`. התשובה 4 היא האיבר הרביעי, שדורש חץ נוסף.",
      "recap": "כל חץ `->next` מתקדם איבר אחד.",
      "questionHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">3 → 5 → 2 → 4</code> ו-<code class=\"tok\" dir=\"ltr\">head</code> מצביע על האיבר הראשון. מה הערך של <code class=\"tok\" dir=\"ltr\">head-&gt;next-&gt;next-&gt;data</code> ?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">head</code> הוא האיבר 3, <code class=\"tok\" dir=\"ltr\">head-&gt;next</code> הוא 5, <code class=\"tok\" dir=\"ltr\">head-&gt;next-&gt;next</code> הוא 2, ולכן התוצאה 2. התשובה 5 היא <code class=\"tok\" dir=\"ltr\">head-&gt;next-&gt;data</code>, והתשובה 3 היא <code class=\"tok\" dir=\"ltr\">head-&gt;data</code>. התשובה 4 היא האיבר הרביעי, שדורש חץ נוסף.",
      "recapHtml": "כל חץ <code class=\"tok\" dir=\"ltr\">-&gt;next</code> מתקדם איבר אחד."
     },
     {
      "id": "C01-Q4",
      "step": {
       "type": "numeric",
       "prompt": "הרשימה ריקה (`head == NULL`). כמה פעמים ירוץ גוף הלולאה `for (p = head; p; p = p->next)` ?",
       "answer": 0,
       "tol": 0,
       "explain": "כבר בבדיקה הראשונה `p` הוא NULL, ולכן הלולאה לא נכנסת אף פעם. לכן לולאה כזו בטוחה גם על רשימה ריקה.",
       "promptHtml": "הרשימה ריקה (<code class=\"tok\" dir=\"ltr\">head == NULL</code>). כמה פעמים ירוץ גוף הלולאה <code class=\"tok\" dir=\"ltr\">for (p = head; p; p = p-&gt;next)</code> ?",
       "explainHtml": "כבר בבדיקה הראשונה <code class=\"tok\" dir=\"ltr\">p</code> הוא NULL, ולכן הלולאה לא נכנסת אף פעם. לכן לולאה כזו בטוחה גם על רשימה ריקה."
      },
      "recap": "לולאת מעבר עם תנאי `p` בטוחה על רשימה ריקה.",
      "recapHtml": "לולאת מעבר עם תנאי <code class=\"tok\" dir=\"ltr\">p</code> בטוחה על רשימה ריקה."
     },
     {
      "id": "C01-Q5",
      "question": "מה הערך של `p` מיד אחרי שהלולאה הבאה מסתיימת, על רשימה לא ריקה?\n```c\nfor (p = head; p; p = p->next)\n    ;\n```",
      "options": [
       {
        "id": "a",
        "value": "`NULL`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "b",
        "value": "הכתובת של האיבר האחרון",
        "type": "text",
        "html": "הכתובת של האיבר האחרון"
       },
       {
        "id": "c",
        "value": "הכתובת של האיבר הראשון",
        "type": "text",
        "html": "הכתובת של האיבר הראשון"
       },
       {
        "id": "d",
        "value": "ערך לא מוגדר",
        "type": "text",
        "html": "ערך לא מוגדר"
       }
      ],
      "correctId": "a",
      "explanation": "הלולאה נעצרת רק כשהתנאי `p` שקר, כלומר כש-`p == NULL`. לכן `p` לא מצביע על האיבר האחרון אלא אחריו. אם צריך את האחרון, עוצרים מוקדם יותר עם התנאי `p->next`. הערך מוגדר היטב, ולכן לא התשובה האחרונה.",
      "recap": "אחרי לולאה עד `p == NULL`, המצביע `p` הוא NULL ולא האיבר האחרון.",
      "questionHtml": "מה הערך של <code class=\"tok\" dir=\"ltr\">p</code> מיד אחרי שהלולאה הבאה מסתיימת, על רשימה לא ריקה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>for (p = head; p; p = p-&gt;next)\n    ;</code></pre>",
      "explanationHtml": "הלולאה נעצרת רק כשהתנאי <code class=\"tok\" dir=\"ltr\">p</code> שקר, כלומר כש-<code class=\"tok\" dir=\"ltr\">p == NULL</code>. לכן <code class=\"tok\" dir=\"ltr\">p</code> לא מצביע על האיבר האחרון אלא אחריו. אם צריך את האחרון, עוצרים מוקדם יותר עם התנאי <code class=\"tok\" dir=\"ltr\">p-&gt;next</code>. הערך מוגדר היטב, ולכן לא התשובה האחרונה.",
      "recapHtml": "אחרי לולאה עד <code class=\"tok\" dir=\"ltr\">p == NULL</code>, המצביע <code class=\"tok\" dir=\"ltr\">p</code> הוא NULL ולא האיבר האחרון."
     }
    ]
   },
   {
    "id": "C02",
    "order": 2,
    "icon": "➕",
    "title": "הכנסה לראש ולסוף",
    "goal": "אחרי השלב הזה אפשר ליצור איבר, להכניס אותו לראש או לסוף הרשימה, ולהסביר למה פונקציית הכנסה מקבלת Item**.",
    "source": "ai-verified",
    "boss": false,
    "goalHtml": "אחרי השלב הזה אפשר ליצור איבר, להכניס אותו לראש או לסוף הרשימה, ולהסביר למה פונקציית הכנסה מקבלת Item**.",
    "lesson": {
     "html": "\n    <p>איבר חדש נוצר עם <code>malloc</code>. נכתוב פונקציית עזר שיוצרת איבר ומחברת אותו לפני איבר אחר:</p>\n    <pre><code>Item *new_item(int data, Item *next)\n{\n    Item *t = (Item *)malloc(sizeof(Item));\n    t-&gt;data = data;\n    t-&gt;next = next;\n    return t;\n}</code></pre>\n    <h3>הכנסה לראש</h3>\n    <pre><code>void insert_head(Item **head, int data)\n{\n    *head = new_item(data, *head);\n}</code></pre>\n    <p>האיבר החדש מצביע על הראש הישן, ואז הוא הופך להיות הראש. הראש משתנה, ולכן הפונקציה מקבלת <b>כתובת של המצביע</b> <code>Item **head</code> וקוראים לה כך: <code>insert_head(&amp;h, 7)</code>.</p>\n    <div class=\"lesson-rule\">🔑 כשפונקציה צריכה לשנות את הראש, מעבירים אליה <code>&amp;head</code>. אם מעבירים רק <code>Item *head</code>, הפונקציה משנה עותק מקומי והקורא לא מושפע.</div>\n    <div class=\"lesson-ex\">דוגמה: מתחילים מרשימה ריקה ומכניסים 1, אחר כך 2, אחר כך 3 לראש. התוצאה היא <code>3 → 2 → 1</code>: כל איבר חדש נכנס <b>לפני</b> הקודמים, ולכן הסדר מתהפך.</div>\n    <h3>הכנסה לסוף</h3>\n    <p>בלי מצביע לאחרון צריך לעבור על כל הרשימה עד האיבר האחרון (<code>while (p-&gt;next) p = p-&gt;next;</code>), כלומר O(n) לכל הכנסה. מי שמחזיק גם מצביע <code>tail</code> לאחרון מכניס בזמן O(1):</p>\n    <pre><code>void append(Item **head, Item **tail, int data)\n{\n    Item *t = new_item(data, NULL);\n    if (*head == NULL)\n        *head = *tail = t;\n    else\n    {\n        (*tail)-&gt;next = t;\n        *tail = t;\n    }\n}</code></pre>\n    <div class=\"lesson-trap\">⚠️ ברשימה ריקה אין אחרון. לכן הכנסה לסוף חייבת טיפול נפרד במקרה <code>*head == NULL</code>.</div>"
    },
    "questions": [
     {
      "id": "C02-Q1",
      "question": "מתחילים עם `Item *h = NULL;` ומריצים:\n```c\ninsert_head(&h, 1);\ninsert_head(&h, 2);\ninsert_head(&h, 3);\n```\nמה מדפיסה מעבר על הרשימה מהראש?",
      "options": [
       {
        "id": "a",
        "value": "`3 2 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 2 1</code>"
       },
       {
        "id": "b",
        "value": "`1 2 3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3</code>"
       },
       {
        "id": "c",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "d",
        "value": "`3`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3</code>"
       }
      ],
      "correctId": "a",
      "explanation": "כל הכנסה לראש מציבה את האיבר החדש לפני כל הקודמים, ולכן הסדר הפוך לסדר ההכנסה: `3 2 1`. התשובה `1 2 3` נכונה רק להכנסה לסוף.",
      "recap": "הכנסה לראש הופכת את סדר ההכנסה.",
      "questionHtml": "מתחילים עם <code class=\"tok\" dir=\"ltr\">Item *h = NULL;</code> ומריצים:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>insert_head(&amp;h, 1);\ninsert_head(&amp;h, 2);\ninsert_head(&amp;h, 3);</code></pre>מה מדפיסה מעבר על הרשימה מהראש?",
      "explanationHtml": "כל הכנסה לראש מציבה את האיבר החדש לפני כל הקודמים, ולכן הסדר הפוך לסדר ההכנסה: <code class=\"tok\" dir=\"ltr\">3 2 1</code>. התשובה <code class=\"tok\" dir=\"ltr\">1 2 3</code> נכונה רק להכנסה לסוף.",
      "recapHtml": "הכנסה לראש הופכת את סדר ההכנסה."
     },
     {
      "id": "C02-Q2",
      "step": {
       "type": "numeric",
       "prompt": "ברשימה יש 8 איברים, ומכניסים איבר חדש לסוף בלי מצביע `tail`, בעזרת:\n```c\nItem *p = head;\nwhile (p->next)\n    p = p->next;\n```\nכמה פעמים מתבצעת ההוראה `p = p->next` ?",
       "answer": 7,
       "tol": 0,
       "explain": "מתחילים באיבר הראשון ויש להגיע לאיבר השמיני, כלומר 7 התקדמויות. בכלל, ברשימה בת $n$ איברים יש $n-1$ התקדמויות, ולכן ההכנסה לסוף היא O(n).",
       "promptHtml": "ברשימה יש 8 איברים, ומכניסים איבר חדש לסוף בלי מצביע <code class=\"tok\" dir=\"ltr\">tail</code>, בעזרת:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>Item *p = head;\nwhile (p-&gt;next)\n    p = p-&gt;next;</code></pre>כמה פעמים מתבצעת ההוראה <code class=\"tok\" dir=\"ltr\">p = p-&gt;next</code> ?",
       "explainHtml": "מתחילים באיבר הראשון ויש להגיע לאיבר השמיני, כלומר 7 התקדמויות. בכלל, ברשימה בת <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi></mrow><annotation encoding=\"application/x-tex\">n</annotation></semantics></math></span> איברים יש <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding=\"application/x-tex\">n-1</annotation></semantics></math></span> התקדמויות, ולכן ההכנסה לסוף היא O(n)."
      },
      "recap": "הכנסה לסוף בלי tail עולה n-1 צעדים.",
      "recapHtml": "הכנסה לסוף בלי tail עולה n-1 צעדים."
     },
     {
      "id": "C02-Q3",
      "question": "הרשימה `h` היא `3 → 5`. מגדירים:\n```c\nvoid add(Item *head, int x)\n{\n    head = new_item(x, head);\n}\n```\nאחרי הקריאה `add(h, 9)` מדפיסים את הרשימה דרך `h`. מה מודפס?",
      "options": [
       {
        "id": "a",
        "value": "`3 5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 5</code>"
       },
       {
        "id": "b",
        "value": "`9 3 5`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9 3 5</code>"
       },
       {
        "id": "c",
        "value": "`3 5 9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">3 5 9</code>"
       },
       {
        "id": "d",
        "value": "`9`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">9</code>"
       }
      ],
      "correctId": "a",
      "explanation": "הפרמטר `head` הוא עותק של `h`. ההשמה משנה את העותק בלבד, ולכן `h` ממשיך להצביע על 3 והרשימה לא השתנתה (ובנוסף האיבר החדש דלף). כדי לשנות את הראש צריך `Item **head` והקריאה `add(&h, 9)`.",
      "recap": "שינוי ראש מחייב להעביר `&head`.",
      "questionHtml": "הרשימה <code class=\"tok\" dir=\"ltr\">h</code> היא <code class=\"tok\" dir=\"ltr\">3 → 5</code>. מגדירים:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void add(Item *head, int x)\n{\n    head = new_item(x, head);\n}</code></pre>אחרי הקריאה <code class=\"tok\" dir=\"ltr\">add(h, 9)</code> מדפיסים את הרשימה דרך <code class=\"tok\" dir=\"ltr\">h</code>. מה מודפס?",
      "explanationHtml": "הפרמטר <code class=\"tok\" dir=\"ltr\">head</code> הוא עותק של <code class=\"tok\" dir=\"ltr\">h</code>. ההשמה משנה את העותק בלבד, ולכן <code class=\"tok\" dir=\"ltr\">h</code> ממשיך להצביע על 3 והרשימה לא השתנתה (ובנוסף האיבר החדש דלף). כדי לשנות את הראש צריך <code class=\"tok\" dir=\"ltr\">Item **head</code> והקריאה <code class=\"tok\" dir=\"ltr\">add(&amp;h, 9)</code>.",
      "recapHtml": "שינוי ראש מחייב להעביר <code class=\"tok\" dir=\"ltr\">&amp;head</code>."
     },
     {
      "id": "C02-Q4",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "הפונקציה אמורה להכניס איבר לראש. בגרסה הבאה שורה אחת שונתה, ואחרי `insert_head(&h, 3)` על הרשימה `2 → 1` מתקבלת הרשימה `3` בלבד. מצאו את השורה.",
       "lines": [
        "void insert_head(Item **head, int x)",
        "{",
        "    Item *t = (Item *)malloc(sizeof(Item));",
        "    t->data = x;",
        "    t->next = NULL;",
        "    *head = t;",
        "}"
       ],
       "bugIndex": 4,
       "explain": "השורה `t->next = NULL;` מנתקת את האיבר החדש מהרשימה הקיימת, ולכן האיברים הישנים אבדו. צריך `t->next = *head;` לפני שמעדכנים את הראש.",
       "promptHtml": "הפונקציה אמורה להכניס איבר לראש. בגרסה הבאה שורה אחת שונתה, ואחרי <code class=\"tok\" dir=\"ltr\">insert_head(&amp;h, 3)</code> על הרשימה <code class=\"tok\" dir=\"ltr\">2 → 1</code> מתקבלת הרשימה <code class=\"tok\" dir=\"ltr\">3</code> בלבד. מצאו את השורה.",
       "explainHtml": "השורה <code class=\"tok\" dir=\"ltr\">t-&gt;next = NULL;</code> מנתקת את האיבר החדש מהרשימה הקיימת, ולכן האיברים הישנים אבדו. צריך <code class=\"tok\" dir=\"ltr\">t-&gt;next = *head;</code> לפני שמעדכנים את הראש.",
       "linesHtml": [
        "void insert_head(Item **head, int x)",
        "{",
        "    Item *t = (Item *)malloc(sizeof(Item));",
        "    t-&gt;data = x;",
        "    t-&gt;next = NULL;",
        "    *head = t;",
        "}"
       ]
      },
      "recap": "האיבר החדש חייב להצביע על הראש הישן לפני שהראש מתעדכן.",
      "recapHtml": "האיבר החדש חייב להצביע על הראש הישן לפני שהראש מתעדכן."
     },
     {
      "id": "C02-Q5",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את פונקציית ההכנסה לסוף עם מצביע `tail`. אחרי ארבע הכנסות של 1, 2, 3, 4 הרשימה צריכה להיות `1 2 3 4`.",
       "lines": [
        "void append(Item **head, Item **tail, int x)",
        "{",
        "    Item *t = new_item(x, NULL);",
        "    if (*head == NULL)",
        "        *head = *tail = t;",
        "    else",
        "    {",
        "        ___",
        "        *tail = t;",
        "    }",
        "}"
       ],
       "blankIndex": 7,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "(*tail)->next = t;",
         "html": "(*tail)-&gt;next = t;"
        },
        {
         "id": "b",
         "type": "text",
         "value": "t->next = *tail;",
         "html": "t-&gt;next = *tail;"
        },
        {
         "id": "c",
         "type": "text",
         "value": "(*head)->next = t;",
         "html": "(*head)-&gt;next = t;"
        },
        {
         "id": "d",
         "type": "text",
         "value": "*head = t;",
         "html": "*head = t;"
        }
       ],
       "correctId": "a",
       "explain": "האחרון הנוכחי צריך להצביע על האיבר החדש: `(*tail)->next = t`, ורק אחר כך `*tail = t`. התשובה `t->next = *tail` הופכת את הכיוון (תוצאה `1`), התשובה `(*head)->next = t` מחברת תמיד לראש (תוצאה `1 4`), והתשובה `*head = t` מאבדת את כל האיברים הקודמים (תוצאה `4`).",
       "promptHtml": "השלימו את פונקציית ההכנסה לסוף עם מצביע <code class=\"tok\" dir=\"ltr\">tail</code>. אחרי ארבע הכנסות של 1, 2, 3, 4 הרשימה צריכה להיות <code class=\"tok\" dir=\"ltr\">1 2 3 4</code>.",
       "explainHtml": "האחרון הנוכחי צריך להצביע על האיבר החדש: <code class=\"tok\" dir=\"ltr\">(*tail)-&gt;next = t</code>, ורק אחר כך <code class=\"tok\" dir=\"ltr\">*tail = t</code>. התשובה <code class=\"tok\" dir=\"ltr\">t-&gt;next = *tail</code> הופכת את הכיוון (תוצאה <code class=\"tok\" dir=\"ltr\">1</code>), התשובה <code class=\"tok\" dir=\"ltr\">(*head)-&gt;next = t</code> מחברת תמיד לראש (תוצאה <code class=\"tok\" dir=\"ltr\">1 4</code>), והתשובה <code class=\"tok\" dir=\"ltr\">*head = t</code> מאבדת את כל האיברים הקודמים (תוצאה <code class=\"tok\" dir=\"ltr\">4</code>).",
       "linesHtml": [
        "void append(Item **head, Item **tail, int x)",
        "{",
        "    Item *t = new_item(x, NULL);",
        "    if (*head == NULL)",
        "        *head = *tail = t;",
        "    else",
        "    {",
        "        ___",
        "        *tail = t;",
        "    }",
        "}"
       ]
      },
      "recap": "הכנסה לסוף: `(*tail)->next = t; *tail = t;`.",
      "recapHtml": "הכנסה לסוף: <code class=\"tok\" dir=\"ltr\">(*tail)-&gt;next = t; *tail = t;</code>."
     }
    ]
   },
   {
    "id": "C03",
    "order": 3,
    "icon": "🔍",
    "title": "מעבר, ספירה וחיפוש",
    "goal": "אחרי השלב הזה אפשר לספור איברים לפי תנאי, להגיע לאיבר האחרון, לחפש ערך, ולכתוב תנאי עצירה בטוח.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>רוב השאלות על רשימות מתחילות בלולאת מעבר. יש שלוש צורות שכדאי להכיר:</p>\n    <ul>\n      <li><b>לכל איבר</b>: <code>for (p = head; p; p = p-&gt;next)</code>. מתאים לספירה, לסכום ולהדפסה. בסוף הלולאה <code>p == NULL</code>.</li>\n      <li><b>עד האיבר האחרון</b>: <code>while (p-&gt;next) p = p-&gt;next;</code>. בסוף <code>p</code> מצביע על האיבר האחרון עצמו. אבל <code>p</code> חייב להיות לא NULL לפני הלולאה, כלומר צריך לטפל ברשימה ריקה בנפרד.</li>\n      <li><b>חיפוש</b>: מתקדמים כל עוד לא מצאנו וגם לא נגמרה הרשימה.</li>\n    </ul>\n    <pre><code>Item *find(Item *head, int x)\n{\n    Item *p = head;\n    while (p &amp;&amp; p-&gt;data != x)\n        p = p-&gt;next;\n    return p;          /* the found item, or NULL */\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 בתנאי <code>p &amp;&amp; p-&gt;data != x</code> הסדר חשוב. האופרטור <code>&amp;&amp;</code> מעריך משמאל לימין ועוצר ברגע שהתוצאה ידועה, ולכן <code>p-&gt;data</code> נבדק רק אם <code>p</code> אינו NULL.</div>\n    <div class=\"lesson-ex\">דוגמה: חיפוש 9 ברשימה <code>4 → 9 → 1</code>. הלולאה מתקדמת פעם אחת, <code>p</code> מצביע על 9 והתנאי שקר, ולכן מוחזר האיבר 9. חיפוש 7 מתקדם עד NULL ומחזיר NULL.</div>\n    <div class=\"lesson-trap\">⚠️ אם כותבים <code>p-&gt;data != x &amp;&amp; p</code>, כשהערך לא ברשימה <code>p</code> מגיע ל-NULL ומיד אחר כך נקרא <code>p-&gt;data</code>. זו התנהגות לא מוגדרת (UB), בדרך כלל קריסה.</div>"
    },
    "questions": [
     {
      "id": "C03-Q1",
      "step": {
       "type": "numeric",
       "prompt": "הרשימה היא `5 → 1 → 4 → 3 → 8`. כמה איברים עם ערך גדול מ-3 מונה הקוד?\n```c\nint c = 0;\nfor (p = head; p; p = p->next)\n    if (p->data > 3)\n        c++;\n```",
       "answer": 3,
       "tol": 0,
       "explain": "הערכים 5, 4 ו-8 גדולים מ-3, והערכים 1 ו-3 לא. לכן c שווה 3.",
       "promptHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">5 → 1 → 4 → 3 → 8</code>. כמה איברים עם ערך גדול מ-3 מונה הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int c = 0;\nfor (p = head; p; p = p-&gt;next)\n    if (p-&gt;data &gt; 3)\n        c++;</code></pre>",
       "explainHtml": "הערכים 5, 4 ו-8 גדולים מ-3, והערכים 1 ו-3 לא. לכן c שווה 3."
      },
      "recap": "ספירה לפי תנאי: לולאה על כל האיברים עם `if` ו-`c++`.",
      "recapHtml": "ספירה לפי תנאי: לולאה על כל האיברים עם <code class=\"tok\" dir=\"ltr\">if</code> ו-<code class=\"tok\" dir=\"ltr\">c++</code>."
     },
     {
      "id": "C03-Q2",
      "question": "מריצים `while (p->next) p = p->next;` כש-`p` הוא `head` והרשימה ריקה (`head == NULL`). מה קורה?",
      "options": [
       {
        "id": "a",
        "value": "התנהגות לא מוגדרת (UB): קריאת `NULL->next`, בדרך כלל קריסה",
        "type": "text",
        "html": "התנהגות לא מוגדרת (UB): קריאת <code class=\"tok\" dir=\"ltr\">NULL-&gt;next</code>, בדרך כלל קריסה"
       },
       {
        "id": "b",
        "value": "הלולאה לא רצה ו-`p` נשאר `NULL`",
        "type": "text",
        "html": "הלולאה לא רצה ו-<code class=\"tok\" dir=\"ltr\">p</code> נשאר <code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "c",
        "value": "הלולאה רצה לנצח",
        "type": "text",
        "html": "הלולאה רצה לנצח"
       },
       {
        "id": "d",
        "value": "הלולאה מסתיימת מיד, כי רשימה ריקה נחשבת לבעלת איבר אחד",
        "type": "text",
        "html": "הלולאה מסתיימת מיד, כי רשימה ריקה נחשבת לבעלת איבר אחד"
       }
      ],
      "correctId": "a",
      "explanation": "כבר הבדיקה הראשונה קוראת `p->next` כש-`p` הוא NULL, ולכן זו גישה ל-NULL: התנהגות לא מוגדרת (UB). בדרך כלל התוכנית קורסת, אבל התקן לא מבטיח זאת, ולכן גם \"הלולאה לא רצה\" אינה תוצאה מובטחת. בלולאה `while (p)` אין בעיה כזו, אבל כאן הבדיקה נוגעת בשדה של `p`. מי שמשתמש ב-`p->next` חייב לוודא קודם ש-`head != NULL`.",
      "recap": "`p->next` בתנאי לולאה דורש `p != NULL` מראש.",
      "questionHtml": "מריצים <code class=\"tok\" dir=\"ltr\">while (p-&gt;next) p = p-&gt;next;</code> כש-<code class=\"tok\" dir=\"ltr\">p</code> הוא <code class=\"tok\" dir=\"ltr\">head</code> והרשימה ריקה (<code class=\"tok\" dir=\"ltr\">head == NULL</code>). מה קורה?",
      "explanationHtml": "כבר הבדיקה הראשונה קוראת <code class=\"tok\" dir=\"ltr\">p-&gt;next</code> כש-<code class=\"tok\" dir=\"ltr\">p</code> הוא NULL, ולכן זו גישה ל-NULL: התנהגות לא מוגדרת (UB). בדרך כלל התוכנית קורסת, אבל התקן לא מבטיח זאת, ולכן גם \"הלולאה לא רצה\" אינה תוצאה מובטחת. בלולאה <code class=\"tok\" dir=\"ltr\">while (p)</code> אין בעיה כזו, אבל כאן הבדיקה נוגעת בשדה של <code class=\"tok\" dir=\"ltr\">p</code>. מי שמשתמש ב-<code class=\"tok\" dir=\"ltr\">p-&gt;next</code> חייב לוודא קודם ש-<code class=\"tok\" dir=\"ltr\">head != NULL</code>.",
      "recapHtml": "<code class=\"tok\" dir=\"ltr\">p-&gt;next</code> בתנאי לולאה דורש <code class=\"tok\" dir=\"ltr\">p != NULL</code> מראש."
     },
     {
      "id": "C03-Q3",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "הפונקציה אמורה להחזיר את האיבר האחרון ברשימה לא ריקה. בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה `NULL`. מצאו את השורה.",
       "lines": [
        "Item *last(Item *head)",
        "{",
        "    Item *p = head;",
        "    while (p)",
        "        p = p->next;",
        "    return p;",
        "}"
       ],
       "bugIndex": 3,
       "explain": "התנאי `while (p)` ממשיך עד ש-`p` הוא NULL, ולכן מוחזר NULL. התנאי הנכון הוא `while (p && p->next)`, שעוצר על האיבר האחרון.",
       "promptHtml": "הפונקציה אמורה להחזיר את האיבר האחרון ברשימה לא ריקה. בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה <code class=\"tok\" dir=\"ltr\">NULL</code>. מצאו את השורה.",
       "explainHtml": "התנאי <code class=\"tok\" dir=\"ltr\">while (p)</code> ממשיך עד ש-<code class=\"tok\" dir=\"ltr\">p</code> הוא NULL, ולכן מוחזר NULL. התנאי הנכון הוא <code class=\"tok\" dir=\"ltr\">while (p &amp;&amp; p-&gt;next)</code>, שעוצר על האיבר האחרון.",
       "linesHtml": [
        "Item *last(Item *head)",
        "{",
        "    Item *p = head;",
        "    while (p)",
        "        p = p-&gt;next;",
        "    return p;",
        "}"
       ]
      },
      "recap": "כדי לעצור על האחרון משתמשים בתנאי `p->next`.",
      "recapHtml": "כדי לעצור על האחרון משתמשים בתנאי <code class=\"tok\" dir=\"ltr\">p-&gt;next</code>."
     },
     {
      "id": "C03-Q4",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את תנאי הלולאה בפונקציית החיפוש. היא צריכה להחזיר את האיבר הראשון עם הערך `x`, או `NULL` אם אין כזה.",
       "lines": [
        "Item *find(Item *head, int x)",
        "{",
        "    Item *p = head;",
        "    while (___)",
        "        p = p->next;",
        "    return p;",
        "}"
       ],
       "blankIndex": 3,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "p && p->data != x",
         "html": "p &amp;&amp; p-&gt;data != x"
        },
        {
         "id": "b",
         "type": "text",
         "value": "p && p->data == x",
         "html": "p &amp;&amp; p-&gt;data == x"
        },
        {
         "id": "c",
         "type": "text",
         "value": "p && p->data < x",
         "html": "p &amp;&amp; p-&gt;data &lt; x"
        },
        {
         "id": "d",
         "type": "text",
         "value": "p->next->data != x",
         "html": "p-&gt;next-&gt;data != x"
        }
       ],
       "correctId": "a",
       "explain": "ממשיכים להתקדם כל עוד לא נגמרה הרשימה והערך שונה מ-`x`. התנאי `p->data == x` עוצר דווקא על איברים לא נכונים, התנאי `p->data < x` תלוי בסדר ולא בשוויון, והתנאי `p->next->data != x` קורס בסוף הרשימה ומדלג על הראשון.",
       "promptHtml": "השלימו את תנאי הלולאה בפונקציית החיפוש. היא צריכה להחזיר את האיבר הראשון עם הערך <code class=\"tok\" dir=\"ltr\">x</code>, או <code class=\"tok\" dir=\"ltr\">NULL</code> אם אין כזה.",
       "explainHtml": "ממשיכים להתקדם כל עוד לא נגמרה הרשימה והערך שונה מ-<code class=\"tok\" dir=\"ltr\">x</code>. התנאי <code class=\"tok\" dir=\"ltr\">p-&gt;data == x</code> עוצר דווקא על איברים לא נכונים, התנאי <code class=\"tok\" dir=\"ltr\">p-&gt;data &lt; x</code> תלוי בסדר ולא בשוויון, והתנאי <code class=\"tok\" dir=\"ltr\">p-&gt;next-&gt;data != x</code> קורס בסוף הרשימה ומדלג על הראשון.",
       "linesHtml": [
        "Item *find(Item *head, int x)",
        "{",
        "    Item *p = head;",
        "    while (___)",
        "        p = p-&gt;next;",
        "    return p;",
        "}"
       ]
      },
      "recap": "חיפוש: `while (p && p->data != x)`.",
      "recapHtml": "חיפוש: <code class=\"tok\" dir=\"ltr\">while (p &amp;&amp; p-&gt;data != x)</code>."
     },
     {
      "id": "C03-Q5",
      "question": "מה הבעיה בתנאי הלולאה `while (p->data != x && p)` בחיפוש הערך `x` ברשימה?",
      "options": [
       {
        "id": "a",
        "value": "כש-`x` לא נמצא ברשימה, `p` מגיע ל-`NULL` ואז נקרא `p->data` לפני הבדיקה: UB / התנהגות לא מוגדרת, בדרך כלל קריסה",
        "type": "text",
        "html": "כש-<code class=\"tok\" dir=\"ltr\">x</code> לא נמצא ברשימה, <code class=\"tok\" dir=\"ltr\">p</code> מגיע ל-<code class=\"tok\" dir=\"ltr\">NULL</code> ואז נקרא <code class=\"tok\" dir=\"ltr\">p-&gt;data</code> לפני הבדיקה: UB / התנהגות לא מוגדרת, בדרך כלל קריסה"
       },
       {
        "id": "b",
        "value": "אין בעיה, כי האופרטור `&&` חילופי",
        "type": "text",
        "html": "אין בעיה, כי האופרטור <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> חילופי"
       },
       {
        "id": "c",
        "value": "שגיאת הידור, כי אי אפשר לכתוב מצביע בתוך תנאי",
        "type": "text",
        "html": "שגיאת הידור, כי אי אפשר לכתוב מצביע בתוך תנאי"
       },
       {
        "id": "d",
        "value": "הלולאה אף פעם לא מסתיימת כשהערך נמצא",
        "type": "text",
        "html": "הלולאה אף פעם לא מסתיימת כשהערך נמצא"
       }
      ],
      "correctId": "a",
      "explanation": "האופרטור `&&` מוערך משמאל לימין, ולכן `p->data` נקרא לפני שבדקנו אם `p` הוא NULL. כשהערך חסר, זו גישה ל-NULL: התנהגות לא מוגדרת (UB), שבדרך כלל מסתיימת בקריסה. כשהערך נמצא, הלולאה עוצרת לפני כן ואין בעיה (נבדק עם clang), ולכן התשובה האחרונה שגויה. `&&` לא חילופי כשיש תלות בין האגפים, והקוד מתקמפל.",
      "recap": "קודם `p`, אחר כך `p->data`.",
      "questionHtml": "מה הבעיה בתנאי הלולאה <code class=\"tok\" dir=\"ltr\">while (p-&gt;data != x &amp;&amp; p)</code> בחיפוש הערך <code class=\"tok\" dir=\"ltr\">x</code> ברשימה?",
      "explanationHtml": "האופרטור <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> מוערך משמאל לימין, ולכן <code class=\"tok\" dir=\"ltr\">p-&gt;data</code> נקרא לפני שבדקנו אם <code class=\"tok\" dir=\"ltr\">p</code> הוא NULL. כשהערך חסר, זו גישה ל-NULL: התנהגות לא מוגדרת (UB), שבדרך כלל מסתיימת בקריסה. כשהערך נמצא, הלולאה עוצרת לפני כן ואין בעיה (נבדק עם clang), ולכן התשובה האחרונה שגויה. <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> לא חילופי כשיש תלות בין האגפים, והקוד מתקמפל.",
      "recapHtml": "קודם <code class=\"tok\" dir=\"ltr\">p</code>, אחר כך <code class=\"tok\" dir=\"ltr\">p-&gt;data</code>."
     }
    ]
   },
   {
    "id": "C04",
    "order": 4,
    "icon": "✂️",
    "title": "מחיקת איברים",
    "goal": "אחרי השלב הזה אפשר למחוק איבר מהרשימה (כולל הראש) בלי לאבד את המשך הרשימה ובלי לגשת לזיכרון משוחרר.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>כדי להוציא איבר מהרשימה צריך לשנות את המצביע של <b>האיבר שלפניו</b> כך שידלג עליו. לכן במחיקה מחזיקים שני מצביעים: <code>curr</code> לאיבר הנבדק ו-<code>prev</code> לאיבר שלפניו.</p>\n    <pre><code>prev-&gt;next = curr-&gt;next;   /* unlink */\nfree(curr);                /* then release */</code></pre>\n    <div class=\"lesson-rule\">🔑 לא קוראים שדה של איבר אחרי <code>free</code> שלו. לכן שומרים <code>next</code> לפני המחיקה, ורק אז משחררים ומתקדמים.</div>\n    <h3>מחיקת הראש</h3>\n    <p>לראש אין איבר קודם (<code>prev == NULL</code>). המחיקה משנה את הראש עצמו: <code>*head = curr-&gt;next</code>, ולכן הפונקציה מקבלת <code>Item **head</code>.</p>\n    <pre><code>void delete_value(Item **head, int val)\n{\n    Item *curr = *head, *prev = NULL;\n    while (curr)\n    {\n        Item *next = curr-&gt;next;   /* save first */\n        if (curr-&gt;data == val)\n        {\n            if (prev == NULL)\n                *head = next;\n            else\n                prev-&gt;next = next;\n            free(curr);\n        }\n        else\n            prev = curr;            /* advance prev only when nothing was deleted */\n        curr = next;\n    }\n}</code></pre>\n    <p>שימו לב: אחרי מחיקה <code>prev</code> לא זז, כי האיבר שאחריו הוא עכשיו <code>next</code>.</p>\n    <div class=\"lesson-ex\">דוגמה: מוחקים את הערך 2 מ-<code>2 → 2 → 5</code>. האיבר הראשון נמחק (<code>*head</code> עובר לאיבר השני), גם הוא נמחק (<code>*head</code> עובר ל-5), ונשארת הרשימה <code>5</code>.</div>\n    <div class=\"lesson-trap\">⚠️ מי שמוחק את הראש בפונקציה שמקבלת <code>Item *head</code> רק משנה עותק. הקורא ממשיך להחזיק כתובת של איבר שהשתחרר.</div>\n    <p>צורה שקולה: מצביע למצביע <code>pp</code> שמחזיק את הכתובת של השדה שמצביע על <code>curr</code>. אז אין צורך במקרה מיוחד לראש:</p>\n    <pre><code>Item **pp = head;\nwhile (*pp)\n{\n    if ((*pp)-&gt;data == val)\n    {\n        Item *dead = *pp;\n        *pp = dead-&gt;next;      /* the pointer that pointed to dead now skips it */\n        free(dead);\n    }\n    else\n        pp = &amp;(*pp)-&gt;next;\n}</code></pre>"
    },
    "questions": [
     {
      "id": "C04-Q1",
      "question": "ברשימה `1 → 2 → 3` מצביע `prev` על 1 ומצביע `curr` על 2. רוצים להוציא את 2 מהרשימה כך שהמעבר מ-`head` ידפיס `1 3`, ואחר כך מבצעים `free(curr)`. איזו שורה מתאימה לפני ה-`free`?",
      "options": [
       {
        "id": "a",
        "value": "`prev->next = curr->next;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">prev-&gt;next = curr-&gt;next;</code>"
       },
       {
        "id": "b",
        "value": "`prev = curr->next;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">prev = curr-&gt;next;</code>"
       },
       {
        "id": "c",
        "value": "`curr->next = prev;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">curr-&gt;next = prev;</code>"
       },
       {
        "id": "d",
        "value": "`prev->next = curr;`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">prev-&gt;next = curr;</code>"
       }
      ],
      "correctId": "a",
      "explanation": "האיבר 1 צריך לדלג על 2 ולהצביע על 3, כלומר `prev->next = curr->next`. התשובה `prev = curr->next` משנה רק משתנה מקומי והרשימה נשארת `1 2 3`. התשובה `curr->next = prev` יוצרת מעגל בין 1 ל-2 והמעבר לא נגמר. התשובה `prev->next = curr` לא משנה כלום.",
      "recap": "מחיקה: `prev->next = curr->next;` ואז `free(curr);`.",
      "questionHtml": "ברשימה <code class=\"tok\" dir=\"ltr\">1 → 2 → 3</code> מצביע <code class=\"tok\" dir=\"ltr\">prev</code> על 1 ומצביע <code class=\"tok\" dir=\"ltr\">curr</code> על 2. רוצים להוציא את 2 מהרשימה כך שהמעבר מ-<code class=\"tok\" dir=\"ltr\">head</code> ידפיס <code class=\"tok\" dir=\"ltr\">1 3</code>, ואחר כך מבצעים <code class=\"tok\" dir=\"ltr\">free(curr)</code>. איזו שורה מתאימה לפני ה-<code class=\"tok\" dir=\"ltr\">free</code>?",
      "explanationHtml": "האיבר 1 צריך לדלג על 2 ולהצביע על 3, כלומר <code class=\"tok\" dir=\"ltr\">prev-&gt;next = curr-&gt;next</code>. התשובה <code class=\"tok\" dir=\"ltr\">prev = curr-&gt;next</code> משנה רק משתנה מקומי והרשימה נשארת <code class=\"tok\" dir=\"ltr\">1 2 3</code>. התשובה <code class=\"tok\" dir=\"ltr\">curr-&gt;next = prev</code> יוצרת מעגל בין 1 ל-2 והמעבר לא נגמר. התשובה <code class=\"tok\" dir=\"ltr\">prev-&gt;next = curr</code> לא משנה כלום.",
      "recapHtml": "מחיקה: <code class=\"tok\" dir=\"ltr\">prev-&gt;next = curr-&gt;next;</code> ואז <code class=\"tok\" dir=\"ltr\">free(curr);</code>."
     },
     {
      "id": "C04-Q2",
      "step": {
       "type": "numeric",
       "prompt": "מפעילים את `delete_value(&h, 2)` מהשיעור על הרשימה `2 → 2 → 5 → 2 → 7`. כמה קריאות `free` מתבצעות?",
       "answer": 3,
       "tol": 0,
       "explain": "שלושה איברים בעלי הערך 2 נמחקים, וכל אחד משוחרר בקריאה אחת. הרשימה שנשארת היא `5 → 7`.",
       "promptHtml": "מפעילים את <code class=\"tok\" dir=\"ltr\">delete_value(&amp;h, 2)</code> מהשיעור על הרשימה <code class=\"tok\" dir=\"ltr\">2 → 2 → 5 → 2 → 7</code>. כמה קריאות <code class=\"tok\" dir=\"ltr\">free</code> מתבצעות?",
       "explainHtml": "שלושה איברים בעלי הערך 2 נמחקים, וכל אחד משוחרר בקריאה אחת. הרשימה שנשארת היא <code class=\"tok\" dir=\"ltr\">5 → 7</code>."
      },
      "recap": "כל איבר שנמחק משוחרר פעם אחת.",
      "recapHtml": "כל איבר שנמחק משוחרר פעם אחת."
     },
     {
      "id": "C04-Q3",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "בגרסה הבאה של `delete_value` שורה אחת שונתה. התוכנית קורסת כשמוחקים את הראש. מצאו את השורה.",
       "lines": [
        "void delete_value(Item **head, int val)",
        "{",
        "    Item *curr = *head, *prev = NULL;",
        "    while (curr)",
        "    {",
        "        Item *next = curr->next;",
        "        if (curr->data == val)",
        "        {",
        "            if (prev != NULL)",
        "                *head = next;",
        "            else",
        "                prev->next = next;",
        "            free(curr);",
        "        }",
        "        else",
        "            prev = curr;",
        "        curr = next;",
        "    }",
        "}"
       ],
       "bugIndex": 8,
       "explain": "התנאי `prev != NULL` הפוך. כשמוחקים את הראש `prev` הוא NULL, והקוד נכנס לענף `prev->next = next` וניגש ל-NULL. התנאי הנכון הוא `prev == NULL` לשינוי הראש.",
       "promptHtml": "בגרסה הבאה של <code class=\"tok\" dir=\"ltr\">delete_value</code> שורה אחת שונתה. התוכנית קורסת כשמוחקים את הראש. מצאו את השורה.",
       "explainHtml": "התנאי <code class=\"tok\" dir=\"ltr\">prev != NULL</code> הפוך. כשמוחקים את הראש <code class=\"tok\" dir=\"ltr\">prev</code> הוא NULL, והקוד נכנס לענף <code class=\"tok\" dir=\"ltr\">prev-&gt;next = next</code> וניגש ל-NULL. התנאי הנכון הוא <code class=\"tok\" dir=\"ltr\">prev == NULL</code> לשינוי הראש.",
       "linesHtml": [
        "void delete_value(Item **head, int val)",
        "{",
        "    Item *curr = *head, *prev = NULL;",
        "    while (curr)",
        "    {",
        "        Item *next = curr-&gt;next;",
        "        if (curr-&gt;data == val)",
        "        {",
        "            if (prev != NULL)",
        "                *head = next;",
        "            else",
        "                prev-&gt;next = next;",
        "            free(curr);",
        "        }",
        "        else",
        "            prev = curr;",
        "        curr = next;",
        "    }",
        "}"
       ]
      },
      "recap": "ראש נמחק כש-`prev == NULL`, ואז משנים `*head`.",
      "recapHtml": "ראש נמחק כש-<code class=\"tok\" dir=\"ltr\">prev == NULL</code>, ואז משנים <code class=\"tok\" dir=\"ltr\">*head</code>."
     },
     {
      "id": "C04-Q4",
      "question": "הרשימה היא `4 → 4 → 1 → 4 → 4 → 2 → 4`. מפעילים `delete_value(&h, 4)` מהשיעור. מה מדפיס מעבר על `h` ?",
      "options": [
       {
        "id": "a",
        "value": "`1 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2</code>"
       },
       {
        "id": "b",
        "value": "`4 4 1 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 4 1 2</code>"
       },
       {
        "id": "c",
        "value": "`1 4 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 4 2</code>"
       },
       {
        "id": "d",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       }
      ],
      "correctId": "a",
      "explanation": "כל ההופעות של 4 נמחקות, גם הרצופות, כי `prev` לא זז אחרי מחיקה ו-`next` נשמר מראש. נשארים `1` ו-`2`.",
      "recap": "מחיקת ערך מחייבת לבדוק גם הופעות רצופות והופעות בראש ובסוף.",
      "questionHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">4 → 4 → 1 → 4 → 4 → 2 → 4</code>. מפעילים <code class=\"tok\" dir=\"ltr\">delete_value(&amp;h, 4)</code> מהשיעור. מה מדפיס מעבר על <code class=\"tok\" dir=\"ltr\">h</code> ?",
      "explanationHtml": "כל ההופעות של 4 נמחקות, גם הרצופות, כי <code class=\"tok\" dir=\"ltr\">prev</code> לא זז אחרי מחיקה ו-<code class=\"tok\" dir=\"ltr\">next</code> נשמר מראש. נשארים <code class=\"tok\" dir=\"ltr\">1</code> ו-<code class=\"tok\" dir=\"ltr\">2</code>.",
      "recapHtml": "מחיקת ערך מחייבת לבדוק גם הופעות רצופות והופעות בראש ובסוף."
     },
     {
      "id": "C04-Q5",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את הגרסה עם מצביע למצביע. היא צריכה למחוק את כל האיברים בעלי הערך `val`.",
       "lines": [
        "void delete_value2(Item **head, int val)",
        "{",
        "    Item **pp = head;",
        "    while (*pp)",
        "    {",
        "        if ((*pp)->data == val)",
        "        {",
        "            Item *dead = *pp;",
        "            ___",
        "            free(dead);",
        "        }",
        "        else",
        "            pp = &(*pp)->next;",
        "    }",
        "}"
       ],
       "blankIndex": 8,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "*pp = dead->next;",
         "html": "*pp = dead-&gt;next;"
        },
        {
         "id": "b",
         "type": "text",
         "value": "*pp = (*pp)->next->next;",
         "html": "*pp = (*pp)-&gt;next-&gt;next;"
        },
        {
         "id": "c",
         "type": "text",
         "value": "*pp = NULL;",
         "html": "*pp = NULL;"
        },
        {
         "id": "d",
         "type": "text",
         "value": "*head = dead->next;",
         "html": "*head = dead-&gt;next;"
        }
       ],
       "correctId": "a",
       "explain": "המצביע ש-`pp` מצביע עליו (ה-`next` של הקודם, או הראש) צריך לדלג על `dead`: `*pp = dead->next`. התשובה `(*pp)->next->next` מדלגת גם על איבר נוסף ומקריסה בסוף הרשימה, התשובה `*pp = NULL` חותכת את שאר הרשימה, והתשובה `*head = dead->next` תמיד משנה את הראש, גם כשהמחיקה באמצע.",
       "promptHtml": "השלימו את הגרסה עם מצביע למצביע. היא צריכה למחוק את כל האיברים בעלי הערך <code class=\"tok\" dir=\"ltr\">val</code>.",
       "explainHtml": "המצביע ש-<code class=\"tok\" dir=\"ltr\">pp</code> מצביע עליו (ה-<code class=\"tok\" dir=\"ltr\">next</code> של הקודם, או הראש) צריך לדלג על <code class=\"tok\" dir=\"ltr\">dead</code>: <code class=\"tok\" dir=\"ltr\">*pp = dead-&gt;next</code>. התשובה <code class=\"tok\" dir=\"ltr\">(*pp)-&gt;next-&gt;next</code> מדלגת גם על איבר נוסף ומקריסה בסוף הרשימה, התשובה <code class=\"tok\" dir=\"ltr\">*pp = NULL</code> חותכת את שאר הרשימה, והתשובה <code class=\"tok\" dir=\"ltr\">*head = dead-&gt;next</code> תמיד משנה את הראש, גם כשהמחיקה באמצע.",
       "linesHtml": [
        "void delete_value2(Item **head, int val)",
        "{",
        "    Item **pp = head;",
        "    while (*pp)",
        "    {",
        "        if ((*pp)-&gt;data == val)",
        "        {",
        "            Item *dead = *pp;",
        "            ___",
        "            free(dead);",
        "        }",
        "        else",
        "            pp = &amp;(*pp)-&gt;next;",
        "    }",
        "}"
       ]
      },
      "recap": "עם `Item **pp`: `*pp = dead->next;` ואין מקרה מיוחד לראש.",
      "recapHtml": "עם <code class=\"tok\" dir=\"ltr\">Item **pp</code>: <code class=\"tok\" dir=\"ltr\">*pp = dead-&gt;next;</code> ואין מקרה מיוחד לראש."
     }
    ]
   },
   {
    "id": "C05",
    "order": 5,
    "icon": "🏗️",
    "title": "בניית רשימה חדשה ושמירת סדר",
    "goal": "אחרי השלב הזה אפשר לבנות רשימה חדשה מתוך קלט, לשמור על הסדר המקורי, ולהבדיל בין 'חבר מחדש' ל'צור איברים חדשים'.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>הרבה שאלות מבקשות להחזיר <b>רשימה חדשה</b> שנבנית מתוך רשימה או מערך קיים. יש שלוש דרכים לשמור על הסדר המקורי:</p>\n    <ul>\n      <li>לעבור על הקלט <b>מהסוף להתחלה</b> ולהכניס כל ערך לראש (כך עובדת <code>from_array</code>).</li>\n      <li>להחזיק מצביע <code>tail</code> ולהכניס לסוף ב-O(1).</li>\n      <li>להשתמש ב<b>איבר דמה</b> (dummy): משתנה מקומי שה-<code>next</code> שלו הוא תחילת הרשימה החדשה. אין מקרה מיוחד ל\"האיבר הראשון\".</li>\n    </ul>\n    <pre><code>Item *from_array(const int *a, int n)\n{\n    Item *head = NULL;\n    int i;\n    for (i = n - 1; i &gt;= 0; i--)\n        insert_head(&amp;head, a[i]);\n    return head;\n}\n\n/* copies the even values, in order, into a new list */\nItem *evens(const Item *src)\n{\n    Item dummy, *tail = &amp;dummy;\n    dummy.next = NULL;\n    for (; src; src = src-&gt;next)\n        if (src-&gt;data % 2 == 0)\n        {\n            tail-&gt;next = new_item(src-&gt;data, NULL);\n            tail = tail-&gt;next;\n        }\n    return dummy.next;\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 שני ניסוחים שונים: \"<b>אל תקצה איברים חדשים</b>\" אומר לחבר מחדש את ה-<code>next</code> של האיברים הקיימים בלי <code>malloc</code>. \"<b>צור רשימה חדשה</b>\" אומר שכל איבר ברשימה החדשה הוא איבר חדש (<code>malloc</code>), גם כשהוא מחזיק רק אינדקס או עותק של ערך.</div>\n    <div class=\"lesson-ex\">דוגמה: <code>evens</code> על <code>1 → 2 → 3 → 4</code>: האיבר 2 נוסף אחרי הדמה, ואז 4 אחרי 2. הפונקציה מחזירה את <code>dummy.next</code>, כלומר <code>2 → 4</code>, ומבצעת <code>malloc</code> פעמיים.</div>\n    <div class=\"lesson-trap\">⚠️ הכנסה לראש תמיד הופכת סדר. אם עוברים על הקלט מההתחלה ומכניסים לראש, הרשימה החדשה יוצאת הפוכה.</div>"
    },
    "questions": [
     {
      "id": "C05-Q1",
      "question": "הרשימה היא `1 → 2 → 3 → 4 → 5 → 6`. לולאה עוברת עליה מההתחלה לסוף, ולכל ערך זוגי קוראת ל-`insert_head(&res, p->data)` כש-`res` מתחיל ב-`NULL`. מה הרשימה `res` בסוף?",
      "options": [
       {
        "id": "a",
        "value": "`6 4 2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">6 4 2</code>"
       },
       {
        "id": "b",
        "value": "`2 4 6`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 4 6</code>"
       },
       {
        "id": "c",
        "value": "`2`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
       },
       {
        "id": "d",
        "value": "`6`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">6</code>"
       }
      ],
      "correctId": "a",
      "explanation": "כל הכנסה לראש שמה את הערך לפני הקודמים. הערכים נכנסים בסדר 2, 4, 6 ולכן מתקבל `6 4 2`. כדי לקבל `2 4 6` צריך tail, איבר דמה או מעבר מהסוף.",
      "recap": "מעבר קדימה + הכנסה לראש = סדר הפוך.",
      "questionHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">1 → 2 → 3 → 4 → 5 → 6</code>. לולאה עוברת עליה מההתחלה לסוף, ולכל ערך זוגי קוראת ל-<code class=\"tok\" dir=\"ltr\">insert_head(&amp;res, p-&gt;data)</code> כש-<code class=\"tok\" dir=\"ltr\">res</code> מתחיל ב-<code class=\"tok\" dir=\"ltr\">NULL</code>. מה הרשימה <code class=\"tok\" dir=\"ltr\">res</code> בסוף?",
      "explanationHtml": "כל הכנסה לראש שמה את הערך לפני הקודמים. הערכים נכנסים בסדר 2, 4, 6 ולכן מתקבל <code class=\"tok\" dir=\"ltr\">6 4 2</code>. כדי לקבל <code class=\"tok\" dir=\"ltr\">2 4 6</code> צריך tail, איבר דמה או מעבר מהסוף.",
      "recapHtml": "מעבר קדימה + הכנסה לראש = סדר הפוך."
     },
     {
      "id": "C05-Q2",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את הפונקציה שמעתיקה את הערכים הזוגיים לרשימה חדשה בסדר המקורי. על `1 → 2 → 3 → 4` היא צריכה להחזיר `2 → 4`.",
       "lines": [
        "Item *evens(const Item *src)",
        "{",
        "    Item dummy, *tail = &dummy;",
        "    dummy.next = NULL;",
        "    for (; src; src = src->next)",
        "        if (src->data % 2 == 0)",
        "        {",
        "            tail->next = new_item(src->data, NULL);",
        "            ___",
        "        }",
        "    return dummy.next;",
        "}"
       ],
       "blankIndex": 8,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "tail = tail->next;",
         "html": "tail = tail-&gt;next;"
        },
        {
         "id": "b",
         "type": "text",
         "value": "tail = &dummy;",
         "html": "tail = &amp;dummy;"
        },
        {
         "id": "c",
         "type": "text",
         "value": "tail->next = NULL;",
         "html": "tail-&gt;next = NULL;"
        },
        {
         "id": "d",
         "type": "text",
         "value": "tail = src;",
         "html": "tail = src;"
        }
       ],
       "correctId": "a",
       "explain": "אחרי שהאיבר החדש חובר, `tail` צריך לעבור אליו: `tail = tail->next`. התשובה `tail = &dummy` תחבר כל איבר חדש לדמה ותשאיר רק את האחרון, `tail->next = NULL` מנתקת מיד את האיבר החדש והרשימה יוצאת ריקה, ו-`tail = src` מעבירה את `tail` לרשימת הקלט ופוגמת בה.",
       "promptHtml": "השלימו את הפונקציה שמעתיקה את הערכים הזוגיים לרשימה חדשה בסדר המקורי. על <code class=\"tok\" dir=\"ltr\">1 → 2 → 3 → 4</code> היא צריכה להחזיר <code class=\"tok\" dir=\"ltr\">2 → 4</code>.",
       "explainHtml": "אחרי שהאיבר החדש חובר, <code class=\"tok\" dir=\"ltr\">tail</code> צריך לעבור אליו: <code class=\"tok\" dir=\"ltr\">tail = tail-&gt;next</code>. התשובה <code class=\"tok\" dir=\"ltr\">tail = &amp;dummy</code> תחבר כל איבר חדש לדמה ותשאיר רק את האחרון, <code class=\"tok\" dir=\"ltr\">tail-&gt;next = NULL</code> מנתקת מיד את האיבר החדש והרשימה יוצאת ריקה, ו-<code class=\"tok\" dir=\"ltr\">tail = src</code> מעבירה את <code class=\"tok\" dir=\"ltr\">tail</code> לרשימת הקלט ופוגמת בה.",
       "linesHtml": [
        "Item *evens(const Item *src)",
        "{",
        "    Item dummy, *tail = &amp;dummy;",
        "    dummy.next = NULL;",
        "    for (; src; src = src-&gt;next)",
        "        if (src-&gt;data % 2 == 0)",
        "        {",
        "            tail-&gt;next = new_item(src-&gt;data, NULL);",
        "            ___",
        "        }",
        "    return dummy.next;",
        "}"
       ]
      },
      "recap": "עם dummy ו-tail: מחברים `tail->next` ואז מקדמים `tail = tail->next`.",
      "recapHtml": "עם dummy ו-tail: מחברים <code class=\"tok\" dir=\"ltr\">tail-&gt;next</code> ואז מקדמים <code class=\"tok\" dir=\"ltr\">tail = tail-&gt;next</code>."
     },
     {
      "id": "C05-Q3",
      "step": {
       "type": "numeric",
       "prompt": "כמה קריאות `malloc` מבצעת `evens` מהשיעור על הרשימה `1 → 2 → 3 → 4 → 5 → 6 → 7` ?",
       "answer": 3,
       "tol": 0,
       "explain": "הפונקציה מעתיקה את הערכים הזוגיים 2, 4 ו-6, ולכן יוצרת שלושה איברים חדשים. הדמה היא משתנה מקומי ולא מוקצית ב-`malloc`.",
       "promptHtml": "כמה קריאות <code class=\"tok\" dir=\"ltr\">malloc</code> מבצעת <code class=\"tok\" dir=\"ltr\">evens</code> מהשיעור על הרשימה <code class=\"tok\" dir=\"ltr\">1 → 2 → 3 → 4 → 5 → 6 → 7</code> ?",
       "explainHtml": "הפונקציה מעתיקה את הערכים הזוגיים 2, 4 ו-6, ולכן יוצרת שלושה איברים חדשים. הדמה היא משתנה מקומי ולא מוקצית ב-<code class=\"tok\" dir=\"ltr\">malloc</code>."
      },
      "recap": "רשימה חדשה = איבר חדש לכל ערך שמועתק.",
      "recapHtml": "רשימה חדשה = איבר חדש לכל ערך שמועתק."
     },
     {
      "id": "C05-Q4",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "הפונקציה אמורה להחזיר רשימה עם ערכי המערך בסדר המערך. בגרסה הבאה שורה אחת שונתה והרשימה יוצאת הפוכה: על `{1, 2, 3}` מתקבל `3 2 1`. מצאו את השורה.",
       "lines": [
        "Item *from_array(const int *a, int n)",
        "{",
        "    Item *head = NULL;",
        "    int i;",
        "    for (i = 0; i < n; i++)",
        "        insert_head(&head, a[i]);",
        "    return head;",
        "}"
       ],
       "bugIndex": 4,
       "explain": "מעבר מההתחלה עם הכנסה לראש הופך את הסדר. הלולאה הנכונה רצה מהסוף: `for (i = n - 1; i >= 0; i--)`.",
       "promptHtml": "הפונקציה אמורה להחזיר רשימה עם ערכי המערך בסדר המערך. בגרסה הבאה שורה אחת שונתה והרשימה יוצאת הפוכה: על <code class=\"tok\" dir=\"ltr\">{1, 2, 3}</code> מתקבל <code class=\"tok\" dir=\"ltr\">3 2 1</code>. מצאו את השורה.",
       "explainHtml": "מעבר מההתחלה עם הכנסה לראש הופך את הסדר. הלולאה הנכונה רצה מהסוף: <code class=\"tok\" dir=\"ltr\">for (i = n - 1; i &gt;= 0; i--)</code>.",
       "linesHtml": [
        "Item *from_array(const int *a, int n)",
        "{",
        "    Item *head = NULL;",
        "    int i;",
        "    for (i = 0; i &lt; n; i++)",
        "        insert_head(&amp;head, a[i]);",
        "    return head;",
        "}"
       ]
      },
      "recap": "כדי לשמור סדר עם הכנסה לראש עוברים על הקלט מהסוף.",
      "recapHtml": "כדי לשמור סדר עם הכנסה לראש עוברים על הקלט מהסוף."
     },
     {
      "id": "C05-Q5",
      "step": {
       "type": "numeric",
       "prompt": "בונים רשימה של 5 ערכים, ערך אחרי ערך, בלי `tail`: כל הכנסה לסוף סורקת מהראש בלולאה `while (p->next) p = p->next;` (ההכנסה הראשונה לרשימה ריקה לא סורקת). כמה פעמים מתבצעת ההוראה `p = p->next` בסך הכל, על פני חמש ההכנסות?",
       "answer": 6,
       "tol": 0,
       "explain": "ההכנסה הראשונה והשנייה סורקות 0 צעדים (ברשימה בת איבר אחד `p->next` כבר NULL), ואחריהן 1, 2 ו-3 צעדים. הסכום הוא $0+0+1+2+3=6$. בכלל זה $O(n^2)$, ו-`tail` מוריד זאת ל-$O(n)$.",
       "promptHtml": "בונים רשימה של 5 ערכים, ערך אחרי ערך, בלי <code class=\"tok\" dir=\"ltr\">tail</code>: כל הכנסה לסוף סורקת מהראש בלולאה <code class=\"tok\" dir=\"ltr\">while (p-&gt;next) p = p-&gt;next;</code> (ההכנסה הראשונה לרשימה ריקה לא סורקת). כמה פעמים מתבצעת ההוראה <code class=\"tok\" dir=\"ltr\">p = p-&gt;next</code> בסך הכל, על פני חמש ההכנסות?",
       "explainHtml": "ההכנסה הראשונה והשנייה סורקות 0 צעדים (ברשימה בת איבר אחד <code class=\"tok\" dir=\"ltr\">p-&gt;next</code> כבר NULL), ואחריהן 1, 2 ו-3 צעדים. הסכום הוא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>0</mn><mo>+</mo><mn>0</mn><mo>+</mo><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>=</mo><mn>6</mn></mrow><annotation encoding=\"application/x-tex\">0+0+1+2+3=6</annotation></semantics></math></span>. בכלל זה <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>O</mi><mo stretchy=\"false\">(</mo><msup><mi>n</mi><mn>2</mn></msup><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">O(n^2)</annotation></semantics></math></span>, ו-<code class=\"tok\" dir=\"ltr\">tail</code> מוריד זאת ל-<span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>O</mi><mo stretchy=\"false\">(</mo><mi>n</mi><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">O(n)</annotation></semantics></math></span>."
      },
      "recap": "הכנסה לסוף בלי tail n פעמים היא $O(n^2)$.",
      "recapHtml": "הכנסה לסוף בלי tail n פעמים היא <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mi>O</mi><mo stretchy=\"false\">(</mo><msup><mi>n</mi><mn>2</mn></msup><mo stretchy=\"false\">)</mo></mrow><annotation encoding=\"application/x-tex\">O(n^2)</annotation></semantics></math></span>."
     }
    ]
   },
   {
    "id": "C06",
    "order": 6,
    "icon": "🔄",
    "title": "רשימות מעגליות",
    "goal": "אחרי השלב הזה אפשר לעבור על רשימה מעגלית בלי לתקוע את התוכנית, ולמצוא בה את האיבר המקסימלי כשהיא ממוינת.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <p>ברשימה <b>מעגלית</b> האיבר האחרון מצביע על הראשון, ולכן <b>אין NULL</b> בשום מקום. רשימה בת איבר אחד מצביעה על עצמה: <code>p-&gt;next == p</code>.</p>\n    <div class=\"lesson-rule\">🔑 לולאה שמחכה ל-NULL לא תיגמר על רשימה מעגלית. עוצרים כשחוזרים לנקודת ההתחלה.</div>\n    <p>כדי לעבור על כל האיברים פעם אחת מתחילים ב-<code>start</code> ומשתמשים ב-<code>do ... while</code>. הגוף רץ לפחות פעם אחת, ורק אחר כך נבדק אם חזרנו להתחלה:</p>\n    <pre><code>Item *p = start;\ndo\n{\n    /* work on p */\n    p = p-&gt;next;\n} while (p != start);</code></pre>\n    <div class=\"lesson-trap\">⚠️ <code>p = start; while (p != start) { ... }</code> לא תרוץ אפילו פעם אחת, כי התנאי כבר שקר בהתחלה.</div>\n    <div class=\"lesson-ex\">דוגמה: ברשימה המעגלית <code>2 → 4 → 7 → 9 → (חוזר ל-2)</code> עם <code>start</code> על 7 סדר הביקור הוא 7, 9, 2, 4. אחרי 4 הצעד הבא מחזיר ל-7 והלולאה נעצרת.</div>\n    <h3>רשימה מעגלית ממוינת</h3>\n    <p>אם הערכים עולים ממש לאורך הרשימה, ורק האיבר האחרון (המקסימלי) מצביע חזרה על הקטן ביותר, אז האיבר המקסימלי הוא היחיד ש-<code>p-&gt;data</code> שלו <b>לא קטן</b> מזה של <code>p-&gt;next</code>. לכן הלולאה</p>\n    <pre><code>while (p-&gt;data &lt; p-&gt;next-&gt;data)\n    p = p-&gt;next;</code></pre>\n    <p>מתקדמת עד האיבר המקסימלי מכל נקודת התחלה. ברשימה בת איבר אחד התנאי שקר מיד, כי ערך אינו קטן מעצמו.</p>"
    },
    "questions": [
     {
      "id": "C06-Q1",
      "question": "הרשימה המעגלית היא `2 → 4 → 7 → 9` (אחרי 9 חוזרים ל-2), ו-`p` מצביע על 2. מה מדפיס הקוד?\n```c\nint n = 0;\nwhile (p->next && n < 100)\n{\n    p = p->next;\n    n++;\n}\nprintf(\"%d\", n);\n```",
      "options": [
       {
        "id": "a",
        "value": "100",
        "type": "text",
        "html": "100"
       },
       {
        "id": "b",
        "value": "3",
        "type": "text",
        "html": "3"
       },
       {
        "id": "c",
        "value": "4",
        "type": "text",
        "html": "4"
       },
       {
        "id": "d",
        "value": "0",
        "type": "text",
        "html": "0"
       }
      ],
      "correctId": "a",
      "explanation": "ברשימה מעגלית כל `next` מצביע על איבר אמיתי, ולכן התנאי `p->next` תמיד אמת ושום דבר לא עוצר את הלולאה חוץ מהחסם `n < 100`. היא רצה 100 פעמים ומדפיסה 100, ללא קשר לאורך הרשימה (נבדק עם clang). 3 היה מתקבל ברשימה רגילה בת 4 איברים שנגמרת ב-NULL, ו-4 הוא מספר האיברים, שהקוד לא סופר. בלי החסם הלולאה לא הייתה נגמרת.",
      "recap": "ברשימה מעגלית עוצרים בחזרה ל-`start`, לא ב-NULL.",
      "questionHtml": "הרשימה המעגלית היא <code class=\"tok\" dir=\"ltr\">2 → 4 → 7 → 9</code> (אחרי 9 חוזרים ל-2), ו-<code class=\"tok\" dir=\"ltr\">p</code> מצביע על 2. מה מדפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int n = 0;\nwhile (p-&gt;next &amp;&amp; n &lt; 100)\n{\n    p = p-&gt;next;\n    n++;\n}\nprintf(\"%d\", n);</code></pre>",
      "explanationHtml": "ברשימה מעגלית כל <code class=\"tok\" dir=\"ltr\">next</code> מצביע על איבר אמיתי, ולכן התנאי <code class=\"tok\" dir=\"ltr\">p-&gt;next</code> תמיד אמת ושום דבר לא עוצר את הלולאה חוץ מהחסם <code class=\"tok\" dir=\"ltr\">n &lt; 100</code>. היא רצה 100 פעמים ומדפיסה 100, ללא קשר לאורך הרשימה (נבדק עם clang). 3 היה מתקבל ברשימה רגילה בת 4 איברים שנגמרת ב-NULL, ו-4 הוא מספר האיברים, שהקוד לא סופר. בלי החסם הלולאה לא הייתה נגמרת.",
      "recapHtml": "ברשימה מעגלית עוצרים בחזרה ל-<code class=\"tok\" dir=\"ltr\">start</code>, לא ב-NULL."
     },
     {
      "id": "C06-Q2",
      "step": {
       "type": "numeric",
       "prompt": "הרשימה המעגלית היא `2 → 4 → 7 → 9` (אחרי 9 חוזרים ל-2), ו-`start` מצביע על 7. מה ידפיס הקוד?\n```c\nint s = 0;\nItem *p = start;\ndo\n{\n    s += p->data;\n    p = p->next;\n} while (p != start);\nprintf(\"%d\", s);\n```",
       "answer": 22,
       "tol": 0,
       "explain": "הלולאה מבקרת בכל ארבעת האיברים פעם אחת בסדר 7, 9, 2, 4: $7+9+2+4=22$, ללא תלות בנקודת ההתחלה.",
       "promptHtml": "הרשימה המעגלית היא <code class=\"tok\" dir=\"ltr\">2 → 4 → 7 → 9</code> (אחרי 9 חוזרים ל-2), ו-<code class=\"tok\" dir=\"ltr\">start</code> מצביע על 7. מה ידפיס הקוד?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int s = 0;\nItem *p = start;\ndo\n{\n    s += p-&gt;data;\n    p = p-&gt;next;\n} while (p != start);\nprintf(\"%d\", s);</code></pre>",
       "explainHtml": "הלולאה מבקרת בכל ארבעת האיברים פעם אחת בסדר 7, 9, 2, 4: <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>7</mn><mo>+</mo><mn>9</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>4</mn><mo>=</mo><mn>22</mn></mrow><annotation encoding=\"application/x-tex\">7+9+2+4=22</annotation></semantics></math></span>, ללא תלות בנקודת ההתחלה."
      },
      "recap": "do-while על מעגלית מבקר בכל איבר פעם אחת.",
      "recapHtml": "do-while על מעגלית מבקר בכל איבר פעם אחת."
     },
     {
      "id": "C06-Q3",
      "question": "ברשימה מעגלית ממוינת יש איבר אחד, `L`, ו-`L->next == L`. כמה פעמים רץ גוף הלולאה `while (L->data < L->next->data) L = L->next;` ?",
      "options": [
       {
        "id": "a",
        "value": "אף פעם",
        "type": "text",
        "html": "אף פעם"
       },
       {
        "id": "b",
        "value": "פעם אחת",
        "type": "text",
        "html": "פעם אחת"
       },
       {
        "id": "c",
        "value": "לנצח",
        "type": "text",
        "html": "לנצח"
       },
       {
        "id": "d",
        "value": "קריסה",
        "type": "text",
        "html": "קריסה"
       }
      ],
      "correctId": "a",
      "explanation": "`L->next` הוא `L` עצמו, ולכן התנאי הוא `L->data < L->data`, שתמיד שקר. הלולאה לא נכנסת וגם אין גישה לא חוקית, כי `L->next` הוא כתובת של איבר אמיתי (נבדק עם clang).",
      "recap": "איבר יחיד מצביע על עצמו, והתנאי `<` ממש מסתיים מיד.",
      "questionHtml": "ברשימה מעגלית ממוינת יש איבר אחד, <code class=\"tok\" dir=\"ltr\">L</code>, ו-<code class=\"tok\" dir=\"ltr\">L-&gt;next == L</code>. כמה פעמים רץ גוף הלולאה <code class=\"tok\" dir=\"ltr\">while (L-&gt;data &lt; L-&gt;next-&gt;data) L = L-&gt;next;</code> ?",
      "explanationHtml": "<code class=\"tok\" dir=\"ltr\">L-&gt;next</code> הוא <code class=\"tok\" dir=\"ltr\">L</code> עצמו, ולכן התנאי הוא <code class=\"tok\" dir=\"ltr\">L-&gt;data &lt; L-&gt;data</code>, שתמיד שקר. הלולאה לא נכנסת וגם אין גישה לא חוקית, כי <code class=\"tok\" dir=\"ltr\">L-&gt;next</code> הוא כתובת של איבר אמיתי (נבדק עם clang).",
      "recapHtml": "איבר יחיד מצביע על עצמו, והתנאי <code class=\"tok\" dir=\"ltr\">&lt;</code> ממש מסתיים מיד."
     },
     {
      "id": "C06-Q4",
      "step": {
       "type": "numeric",
       "prompt": "הרשימה המעגלית הממוינת היא `3 → 5 → 8 → 12` (אחרי 12 חוזרים ל-3), ו-`L` מצביע על 5. כמה פעמים ירוץ גוף הלולאה `while (L->data < L->next->data) L = L->next;` ?",
       "answer": 2,
       "tol": 0,
       "explain": "מ-5 עוברים ל-8 (כי $5<8$), מ-8 ל-12 (כי $8<12$), וב-12 התנאי $12<3$ שקר. הגוף רץ פעמיים ו-`L` מסיים על האיבר המקסימלי 12.",
       "promptHtml": "הרשימה המעגלית הממוינת היא <code class=\"tok\" dir=\"ltr\">3 → 5 → 8 → 12</code> (אחרי 12 חוזרים ל-3), ו-<code class=\"tok\" dir=\"ltr\">L</code> מצביע על 5. כמה פעמים ירוץ גוף הלולאה <code class=\"tok\" dir=\"ltr\">while (L-&gt;data &lt; L-&gt;next-&gt;data) L = L-&gt;next;</code> ?",
       "explainHtml": "מ-5 עוברים ל-8 (כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>5</mn><mo>&lt;</mo><mn>8</mn></mrow><annotation encoding=\"application/x-tex\">5&lt;8</annotation></semantics></math></span>), מ-8 ל-12 (כי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>8</mn><mo>&lt;</mo><mn>12</mn></mrow><annotation encoding=\"application/x-tex\">8&lt;12</annotation></semantics></math></span>), וב-12 התנאי <span class=\"math-inline\"><math dir=\"ltr\" xmlns=\"http://www.w3.org/1998/Math/MathML\"><semantics><mrow><mn>12</mn><mo>&lt;</mo><mn>3</mn></mrow><annotation encoding=\"application/x-tex\">12&lt;3</annotation></semantics></math></span> שקר. הגוף רץ פעמיים ו-<code class=\"tok\" dir=\"ltr\">L</code> מסיים על האיבר המקסימלי 12."
      },
      "recap": "הלולאה עוצרת באיבר המקסימלי, כי אחריו בא הקטן ביותר.",
      "recapHtml": "הלולאה עוצרת באיבר המקסימלי, כי אחריו בא הקטן ביותר."
     },
     {
      "id": "C06-Q5",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "הפונקציה אמורה לספור את האיברים ברשימה מעגלית. בגרסה הבאה שורה אחת שונתה, ועל רשימה בת 4 איברים מתקבל 3. מצאו את השורה.",
       "lines": [
        "int count(Item *start)",
        "{",
        "    Item *p = start;",
        "    int c = 0;",
        "    do",
        "    {",
        "        c++;",
        "        p = p->next;",
        "    } while (p->next != start);",
        "    return c;",
        "}"
       ],
       "bugIndex": 8,
       "explain": "התנאי `p->next != start` עוצר כשהאיבר הבא הוא `start`, כלומר כש-`p` הוא האחרון, לפני שספרנו אותו. התנאי הנכון הוא `p != start` אחרי ההתקדמות.",
       "promptHtml": "הפונקציה אמורה לספור את האיברים ברשימה מעגלית. בגרסה הבאה שורה אחת שונתה, ועל רשימה בת 4 איברים מתקבל 3. מצאו את השורה.",
       "explainHtml": "התנאי <code class=\"tok\" dir=\"ltr\">p-&gt;next != start</code> עוצר כשהאיבר הבא הוא <code class=\"tok\" dir=\"ltr\">start</code>, כלומר כש-<code class=\"tok\" dir=\"ltr\">p</code> הוא האחרון, לפני שספרנו אותו. התנאי הנכון הוא <code class=\"tok\" dir=\"ltr\">p != start</code> אחרי ההתקדמות.",
       "linesHtml": [
        "int count(Item *start)",
        "{",
        "    Item *p = start;",
        "    int c = 0;",
        "    do",
        "    {",
        "        c++;",
        "        p = p-&gt;next;",
        "    } while (p-&gt;next != start);",
        "    return c;",
        "}"
       ]
      },
      "recap": "תנאי העצירה במעגלית: `while (p != start)` אחרי `p = p->next`.",
      "recapHtml": "תנאי העצירה במעגלית: <code class=\"tok\" dir=\"ltr\">while (p != start)</code> אחרי <code class=\"tok\" dir=\"ltr\">p = p-&gt;next</code>."
     }
    ]
   },
   {
    "id": "C07",
    "order": 7,
    "icon": "🧩",
    "title": "היפוך, השוואה ופונקציות עזר",
    "goal": "אחרי השלב הזה אפשר להפוך רשימה במקום, להשוות שתי רשימות, ולפרק בעיה על מערך של רשימות לפונקציית עזר ולולאה חיצונית.",
    "source": "ai-verified",
    "boss": false,
    "lesson": {
     "html": "\n    <h3>היפוך במקום (בלי איברים חדשים)</h3>\n    <p>מחזיקים שלושה מצביעים: <code>prev</code> (כבר הפוך), <code>curr</code> (הנוכחי) ו-<code>next</code> (המשך שעוד לא נגענו בו). בכל צעד הופכים את החץ של <code>curr</code>:</p>\n    <pre><code>Item *reverse(Item *head)\n{\n    Item *prev = NULL, *curr = head;\n    while (curr)\n    {\n        Item *next = curr-&gt;next;   /* 1. save the rest */\n        curr-&gt;next = prev;         /* 2. flip the arrow */\n        prev = curr;               /* 3. advance prev */\n        curr = next;               /* 4. advance curr */\n    }\n    return prev;                   /* the new head */\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 הסדר כפוי: קודם שומרים את <code>next</code> (אחרת מאבדים את המשך הרשימה), אחר כך הופכים חץ, ורק אז מקדמים <code>prev</code> ואחריו <code>curr</code>. הראש החדש הוא <code>prev</code>.</div>\n    <div class=\"lesson-ex\">דוגמה: ברשימה <code>1 → 2 → 3</code>, אחרי הצעד הראשון האיבר 1 מצביע על NULL ו-<code>prev</code> עליו. המצביע <code>head</code> של הקורא עדיין מצביע על 1, שהוא עכשיו האיבר האחרון, ולכן מעבר דרך <code>head</code> ידפיס רק <code>1</code>.</div>\n    <h3>השוואה בין שתי רשימות</h3>\n    <p>עוברים בו זמנית על שתיהן. מחזירים 0 כשערכים שונים, ובסיום הלולאה בודקים <b>מי נגמר</b>: הרשימות שוות רק אם שתיהן נגמרו יחד.</p>\n    <pre><code>int equal(const Item *a, const Item *b)\n{\n    while (a &amp;&amp; b)\n    {\n        if (a-&gt;data != b-&gt;data)\n            return 0;\n        a = a-&gt;next;\n        b = b-&gt;next;\n    }\n    return a == NULL &amp;&amp; b == NULL;\n}</code></pre>\n    <h3>מערך של רשימות: פונקציית עזר ולולאה חיצונית</h3>\n    <p>כשצריך לבדוק כל רשימה במערך <code>A</code> של רשימות, כותבים פונקציית עזר ששואלת שאלה אחת על שתי רשימות, ולולאה על האינדקסים שקוראת לה. למשל, האם כל ערכי <code>sub</code> מופיעים ב-<code>list</code>:</p>\n    <pre><code>int contains_all(const Item *sub, const Item *list)\n{\n    for (; sub; sub = sub-&gt;next)\n    {\n        const Item *p = list;\n        while (p &amp;&amp; p-&gt;data != sub-&gt;data)\n            p = p-&gt;next;\n        if (p == NULL)\n            return 0;          /* this value was not found */\n    }\n    return 1;\n}</code></pre>\n    <div class=\"lesson-trap\">⚠️ בחיפוש מתחילים מחדש מראש <code>list</code> עבור כל ערך של <code>sub</code>, וה-<code>p &amp;&amp;</code> בתנאי הלולאה הפנימית הכרחי: בלעדיו ערך חסר גורם לקריסה.</div>"
    },
    "questions": [
     {
      "id": "C07-Q1",
      "step": {
       "type": "order",
       "code": true,
       "prompt": "סדרו את גוף הלולאה של היפוך הרשימה.",
       "lines": [
        "Item *next = curr->next;",
        "curr->next = prev;",
        "prev = curr;",
        "curr = next;"
       ],
       "explain": "קודם שומרים את `next`. אחר כך הופכים את החץ של `curr`. אז `prev` מתקדם אל `curr`, ולבסוף `curr` מתקדם אל `next`. כל שינוי סדר שובר את הרשימה או לא נגמר (נבדק עם clang על כל 24 הסדרים: רק זה הופך נכון).",
       "promptHtml": "סדרו את גוף הלולאה של היפוך הרשימה.",
       "explainHtml": "קודם שומרים את <code class=\"tok\" dir=\"ltr\">next</code>. אחר כך הופכים את החץ של <code class=\"tok\" dir=\"ltr\">curr</code>. אז <code class=\"tok\" dir=\"ltr\">prev</code> מתקדם אל <code class=\"tok\" dir=\"ltr\">curr</code>, ולבסוף <code class=\"tok\" dir=\"ltr\">curr</code> מתקדם אל <code class=\"tok\" dir=\"ltr\">next</code>. כל שינוי סדר שובר את הרשימה או לא נגמר (נבדק עם clang על כל 24 הסדרים: רק זה הופך נכון).",
       "linesHtml": [
        "Item *next = curr-&gt;next;",
        "curr-&gt;next = prev;",
        "prev = curr;",
        "curr = next;"
       ]
      },
      "recap": "היפוך: שמור next, הפוך חץ, קדם prev, קדם curr.",
      "recapHtml": "היפוך: שמור next, הפוך חץ, קדם prev, קדם curr."
     },
     {
      "id": "C07-Q2",
      "question": "הרשימה היא `1 → 2 → 3 → 4` ו-`head` מצביע על 1. מריצים את גוף לולאת ההיפוך (השיעור) פעם אחת בלבד, עם `curr = head` ו-`prev = NULL`. מה ידפיס מעבר על הרשימה דרך המשתנה `head` ?",
      "options": [
       {
        "id": "a",
        "value": "`1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
       },
       {
        "id": "b",
        "value": "`4 3 2 1`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">4 3 2 1</code>"
       },
       {
        "id": "c",
        "value": "`2 3 4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">2 3 4</code>"
       },
       {
        "id": "d",
        "value": "`1 2 3 4`",
        "type": "text",
        "html": "<code class=\"tok\" dir=\"ltr\">1 2 3 4</code>"
       }
      ],
      "correctId": "a",
      "explanation": "אחרי הצעד הראשון `1->next` הוא `NULL`. המשתנה `head` עדיין מצביע על 1, ולכן המעבר דרכו מדפיס רק `1`. הרשימה ההפוכה (`4 3 2 1`) מתקבלת רק אחרי כל הצעדים, ורק מהמצביע `prev` שהוחזר.",
      "recap": "אחרי היפוך מתחילים מהראש החדש, לא מ-`head` הישן.",
      "questionHtml": "הרשימה היא <code class=\"tok\" dir=\"ltr\">1 → 2 → 3 → 4</code> ו-<code class=\"tok\" dir=\"ltr\">head</code> מצביע על 1. מריצים את גוף לולאת ההיפוך (השיעור) פעם אחת בלבד, עם <code class=\"tok\" dir=\"ltr\">curr = head</code> ו-<code class=\"tok\" dir=\"ltr\">prev = NULL</code>. מה ידפיס מעבר על הרשימה דרך המשתנה <code class=\"tok\" dir=\"ltr\">head</code> ?",
      "explanationHtml": "אחרי הצעד הראשון <code class=\"tok\" dir=\"ltr\">1-&gt;next</code> הוא <code class=\"tok\" dir=\"ltr\">NULL</code>. המשתנה <code class=\"tok\" dir=\"ltr\">head</code> עדיין מצביע על 1, ולכן המעבר דרכו מדפיס רק <code class=\"tok\" dir=\"ltr\">1</code>. הרשימה ההפוכה (<code class=\"tok\" dir=\"ltr\">4 3 2 1</code>) מתקבלת רק אחרי כל הצעדים, ורק מהמצביע <code class=\"tok\" dir=\"ltr\">prev</code> שהוחזר.",
      "recapHtml": "אחרי היפוך מתחילים מהראש החדש, לא מ-<code class=\"tok\" dir=\"ltr\">head</code> הישן."
     },
     {
      "id": "C07-Q3",
      "step": {
       "type": "fillblank",
       "code": true,
       "prompt": "השלימו את ערך ההחזרה של פונקציית ההשוואה בין שתי רשימות. היא צריכה להחזיר 1 רק כששתי הרשימות זהות.",
       "lines": [
        "int equal(const Item *a, const Item *b)",
        "{",
        "    while (a && b)",
        "    {",
        "        if (a->data != b->data)",
        "            return 0;",
        "        a = a->next;",
        "        b = b->next;",
        "    }",
        "    ___",
        "}"
       ],
       "blankIndex": 9,
       "options": [
        {
         "id": "a",
         "type": "text",
         "value": "return a == NULL && b == NULL;",
         "html": "return a == NULL &amp;&amp; b == NULL;"
        },
        {
         "id": "b",
         "type": "text",
         "value": "return 1;",
         "html": "return 1;"
        },
        {
         "id": "c",
         "type": "text",
         "value": "return a == NULL;",
         "html": "return a == NULL;"
        },
        {
         "id": "d",
         "type": "text",
         "value": "return b == NULL;",
         "html": "return b == NULL;"
        }
       ],
       "correctId": "a",
       "explain": "אחרי הלולאה לפחות אחת מהרשימות נגמרה, והן זהות רק אם שתיהן נגמרו. `return 1` נכשל על `1 2` מול `1 2 3`, `return a == NULL` נכשל על אותו זוג (a נגמרה אבל b לא), ו-`return b == NULL` נכשל על הזוג ההפוך.",
       "promptHtml": "השלימו את ערך ההחזרה של פונקציית ההשוואה בין שתי רשימות. היא צריכה להחזיר 1 רק כששתי הרשימות זהות.",
       "explainHtml": "אחרי הלולאה לפחות אחת מהרשימות נגמרה, והן זהות רק אם שתיהן נגמרו. <code class=\"tok\" dir=\"ltr\">return 1</code> נכשל על <code class=\"tok\" dir=\"ltr\">1 2</code> מול <code class=\"tok\" dir=\"ltr\">1 2 3</code>, <code class=\"tok\" dir=\"ltr\">return a == NULL</code> נכשל על אותו זוג (a נגמרה אבל b לא), ו-<code class=\"tok\" dir=\"ltr\">return b == NULL</code> נכשל על הזוג ההפוך.",
       "linesHtml": [
        "int equal(const Item *a, const Item *b)",
        "{",
        "    while (a &amp;&amp; b)",
        "    {",
        "        if (a-&gt;data != b-&gt;data)",
        "            return 0;",
        "        a = a-&gt;next;",
        "        b = b-&gt;next;",
        "    }",
        "    ___",
        "}"
       ]
      },
      "recap": "השוואת רשימות: בסוף בודקים ששתיהן נגמרו.",
      "recapHtml": "השוואת רשימות: בסוף בודקים ששתיהן נגמרו."
     },
     {
      "id": "C07-Q4",
      "step": {
       "type": "findbug",
       "code": true,
       "prompt": "בגרסה הבאה של `contains_all` שורה אחת שונתה. התוכנית קורסת כשערך של `sub` לא נמצא ב-`list`. מצאו את השורה.",
       "lines": [
        "int contains_all(const Item *sub, const Item *list)",
        "{",
        "    for (; sub; sub = sub->next)",
        "    {",
        "        const Item *p = list;",
        "        while (p->data != sub->data)",
        "            p = p->next;",
        "        if (p == NULL)",
        "            return 0;",
        "    }",
        "    return 1;",
        "}"
       ],
       "bugIndex": 5,
       "explain": "בלי `p &&` הלולאה הפנימית ממשיכה אחרי האיבר האחרון, מגיעה ל-NULL וקוראת `p->data`. התנאי הנכון הוא `while (p && p->data != sub->data)`.",
       "promptHtml": "בגרסה הבאה של <code class=\"tok\" dir=\"ltr\">contains_all</code> שורה אחת שונתה. התוכנית קורסת כשערך של <code class=\"tok\" dir=\"ltr\">sub</code> לא נמצא ב-<code class=\"tok\" dir=\"ltr\">list</code>. מצאו את השורה.",
       "explainHtml": "בלי <code class=\"tok\" dir=\"ltr\">p &amp;&amp;</code> הלולאה הפנימית ממשיכה אחרי האיבר האחרון, מגיעה ל-NULL וקוראת <code class=\"tok\" dir=\"ltr\">p-&gt;data</code>. התנאי הנכון הוא <code class=\"tok\" dir=\"ltr\">while (p &amp;&amp; p-&gt;data != sub-&gt;data)</code>.",
       "linesHtml": [
        "int contains_all(const Item *sub, const Item *list)",
        "{",
        "    for (; sub; sub = sub-&gt;next)",
        "    {",
        "        const Item *p = list;",
        "        while (p-&gt;data != sub-&gt;data)",
        "            p = p-&gt;next;",
        "        if (p == NULL)",
        "            return 0;",
        "    }",
        "    return 1;",
        "}"
       ]
      },
      "recap": "חיפוש בתוך לולאה: תמיד `p &&` לפני `p->data`.",
      "recapHtml": "חיפוש בתוך לולאה: תמיד <code class=\"tok\" dir=\"ltr\">p &amp;&amp;</code> לפני <code class=\"tok\" dir=\"ltr\">p-&gt;data</code>."
     },
     {
      "id": "C07-Q5",
      "step": {
       "type": "numeric",
       "prompt": "המערך `A` מכיל ארבע רשימות: `1,2`, `2,1,3`, `3`, `1,2,3`, והרשימה `L` היא `1,2`. הלולאה החיצונית קוראת ל-`contains_all(L, A[i])` לכל `i`. בכמה רשימות מ-`A` היא מחזירה 1 ?",
       "answer": 3,
       "tol": 0,
       "explain": "הרשימות `1,2`, `2,1,3` ו-`1,2,3` מכילות את שני הערכים 1 ו-2 (הסדר לא משנה), והרשימה `3` לא. לכן 3.",
       "promptHtml": "המערך <code class=\"tok\" dir=\"ltr\">A</code> מכיל ארבע רשימות: <code class=\"tok\" dir=\"ltr\">1,2</code>, <code class=\"tok\" dir=\"ltr\">2,1,3</code>, <code class=\"tok\" dir=\"ltr\">3</code>, <code class=\"tok\" dir=\"ltr\">1,2,3</code>, והרשימה <code class=\"tok\" dir=\"ltr\">L</code> היא <code class=\"tok\" dir=\"ltr\">1,2</code>. הלולאה החיצונית קוראת ל-<code class=\"tok\" dir=\"ltr\">contains_all(L, A[i])</code> לכל <code class=\"tok\" dir=\"ltr\">i</code>. בכמה רשימות מ-<code class=\"tok\" dir=\"ltr\">A</code> היא מחזירה 1 ?",
       "explainHtml": "הרשימות <code class=\"tok\" dir=\"ltr\">1,2</code>, <code class=\"tok\" dir=\"ltr\">2,1,3</code> ו-<code class=\"tok\" dir=\"ltr\">1,2,3</code> מכילות את שני הערכים 1 ו-2 (הסדר לא משנה), והרשימה <code class=\"tok\" dir=\"ltr\">3</code> לא. לכן 3."
      },
      "recap": "contains_all לא מתחשבת בסדר, רק בקיום כל הערכים.",
      "recapHtml": "contains_all לא מתחשבת בסדר, רק בקיום כל הערכים."
     }
    ]
   },
   {
    "id": "C08",
    "order": 8,
    "icon": "🏆",
    "title": "מבחן גמר: שאלות מהמבחן",
    "goal": "אחרי השלב הזה אפשר לפתור שאלות רשימות מקושרות בגודל של שאלת מבחן אמיתית.",
    "source": "ai-verified",
    "boss": true,
    "lesson": {
     "html": "\n    <p>ארבע שאלות אמיתיות מהמבחנים, כולל צעדים מודרכים. לפני שכותבים קוד, עוברים על הרשימה הבאה:</p>\n    <ul>\n      <li>שרטטו רשימה של 4-5 איברים עם חצים, וסמנו את הראש.</li>\n      <li>החליטו אילו מצביעים צריך (<code>prev</code>, <code>curr</code>, <code>next</code>) ומה תנאי העצירה.</li>\n      <li>בדקו מקרי קצה: רשימה ריקה, איבר אחד, שינוי הראש, מחיקת האחרון.</li>\n      <li>שימו לב למילים \"אל תקצה איברים חדשים\" (מחברים מחדש), \"צור רשימה חדשה\" (<code>malloc</code> לכל איבר) ו\"שחרר\" (<code>free</code>).</li>\n    </ul>\n    <div class=\"lesson-rule\">🔑 סדר פעולות בחיבור מחדש: קודם שומרים מצביעים, אחר כך מחברים, ורק בסוף משחררים.</div>"
    },
    "questions": [
     {
      "bankId": "25B-A-Q1",
      "recap": "מחיקת רווחים: ראש משתנה (`Item **`), `prev` לאחר מחיקה לא זז, ו-`free` לכל איבר שהוסר.",
      "recapHtml": "מחיקת רווחים: ראש משתנה (<code class=\"tok\" dir=\"ltr\">Item **</code>), <code class=\"tok\" dir=\"ltr\">prev</code> לאחר מחיקה לא זז, ו-<code class=\"tok\" dir=\"ltr\">free</code> לכל איבר שהוסר."
     },
     {
      "bankId": "25B-B-Q1",
      "recap": "פונקציית עזר שבודקת רשימה אחת, ולולאה על המערך שבונה רשימה חדשה של אינדקסים.",
      "recapHtml": "פונקציית עזר שבודקת רשימה אחת, ולולאה על המערך שבונה רשימה חדשה של אינדקסים."
     },
     {
      "bankId": "20B-A-Q2",
      "recap": "רשימה מעגלית ממוינת: האיבר המקסימלי הוא האחרון שבו `data` לא קטן מה-`next`, והבא אחריו הוא המינימלי.",
      "recapHtml": "רשימה מעגלית ממוינת: האיבר המקסימלי הוא האחרון שבו <code class=\"tok\" dir=\"ltr\">data</code> לא קטן מה-<code class=\"tok\" dir=\"ltr\">next</code>, והבא אחריו הוא המינימלי."
     },
     {
      "bankId": "20B-B-Q2",
      "recap": "תחילית: מעבר מקביל על שתי רשימות, ובסיום בודקים ש-`L1` נגמרה.",
      "recapHtml": "תחילית: מעבר מקביל על שתי רשימות, ובסיום בודקים ש-<code class=\"tok\" dir=\"ltr\">L1</code> נגמרה."
     }
    ]
   }
  ]
 }
};
