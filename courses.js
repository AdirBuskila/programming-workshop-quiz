window.COURSES = {
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
     "html": "\n    <p>רוב השאלות על רשימות מתחילות בלולאת מעבר. יש שלוש צורות שכדאי להכיר:</p>\n    <ul>\n      <li><b>לכל איבר</b>: <code>for (p = head; p; p = p-&gt;next)</code>. מתאים לספירה, לסכום ולהדפסה. בסוף הלולאה <code>p == NULL</code>.</li>\n      <li><b>עד האיבר האחרון</b>: <code>while (p-&gt;next) p = p-&gt;next;</code>. בסוף <code>p</code> מצביע על האיבר האחרון עצמו. אבל <code>p</code> חייב להיות לא NULL לפני הלולאה, כלומר צריך לטפל ברשימה ריקה בנפרד.</li>\n      <li><b>חיפוש</b>: מתקדמים כל עוד לא מצאנו וגם לא נגמרה הרשימה.</li>\n    </ul>\n    <pre><code>Item *find(Item *head, int x)\n{\n    Item *p = head;\n    while (p &amp;&amp; p-&gt;data != x)\n        p = p-&gt;next;\n    return p;          /* the found item, or NULL */\n}</code></pre>\n    <div class=\"lesson-rule\">🔑 בתנאי <code>p &amp;&amp; p-&gt;data != x</code> הסדר חשוב. האופרטור <code>&amp;&amp;</code> מעריך משמאל לימין ועוצר ברגע שהתוצאה ידועה, ולכן <code>p-&gt;data</code> נבדק רק אם <code>p</code> אינו NULL.</div>\n    <div class=\"lesson-ex\">דוגמה: חיפוש 9 ברשימה <code>4 → 9 → 1</code>. הלולאה מתקדמת פעם אחת, <code>p</code> מצביע על 9 והתנאי שקר, ולכן מוחזר האיבר 9. חיפוש 7 מתקדם עד NULL ומחזיר NULL.</div>\n    <div class=\"lesson-trap\">⚠️ אם כותבים <code>p-&gt;data != x &amp;&amp; p</code>, כשהערך לא ברשימה <code>p</code> מגיע ל-NULL ומיד אחר כך נקרא <code>p-&gt;data</code>. זו קריסה.</div>"
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
        "value": "קריסה: גישה ל-`NULL->next`",
        "type": "text",
        "html": "קריסה: גישה ל-<code class=\"tok\" dir=\"ltr\">NULL-&gt;next</code>"
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
      "explanation": "כבר הבדיקה הראשונה קוראת `p->next` כש-`p` הוא NULL, ולכן התוכנית קורסת (נבדק עם clang). בלולאה `while (p)` אין בעיה כזו, אבל כאן הבדיקה נוגעת בשדה של `p`. מי שמשתמש ב-`p->next` חייב לוודא קודם ש-`head != NULL`.",
      "recap": "`p->next` בתנאי לולאה דורש `p != NULL` מראש.",
      "questionHtml": "מריצים <code class=\"tok\" dir=\"ltr\">while (p-&gt;next) p = p-&gt;next;</code> כש-<code class=\"tok\" dir=\"ltr\">p</code> הוא <code class=\"tok\" dir=\"ltr\">head</code> והרשימה ריקה (<code class=\"tok\" dir=\"ltr\">head == NULL</code>). מה קורה?",
      "explanationHtml": "כבר הבדיקה הראשונה קוראת <code class=\"tok\" dir=\"ltr\">p-&gt;next</code> כש-<code class=\"tok\" dir=\"ltr\">p</code> הוא NULL, ולכן התוכנית קורסת (נבדק עם clang). בלולאה <code class=\"tok\" dir=\"ltr\">while (p)</code> אין בעיה כזו, אבל כאן הבדיקה נוגעת בשדה של <code class=\"tok\" dir=\"ltr\">p</code>. מי שמשתמש ב-<code class=\"tok\" dir=\"ltr\">p-&gt;next</code> חייב לוודא קודם ש-<code class=\"tok\" dir=\"ltr\">head != NULL</code>.",
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
        "value": "כש-`x` לא נמצא ברשימה, `p` מגיע ל-`NULL` ואז נקרא `p->data` לפני הבדיקה: קריסה",
        "type": "text",
        "html": "כש-<code class=\"tok\" dir=\"ltr\">x</code> לא נמצא ברשימה, <code class=\"tok\" dir=\"ltr\">p</code> מגיע ל-<code class=\"tok\" dir=\"ltr\">NULL</code> ואז נקרא <code class=\"tok\" dir=\"ltr\">p-&gt;data</code> לפני הבדיקה: קריסה"
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
      "explanation": "האופרטור `&&` מוערך משמאל לימין, ולכן `p->data` נקרא לפני שבדקנו אם `p` הוא NULL. כשהערך חסר, זו גישה ל-NULL ותוכנית קורסת (נבדק עם clang). כשהערך נמצא, הלולאה עוצרת כרגיל ואין בעיה, ולכן התשובה האחרונה שגויה. `&&` לא חילופי כשיש תלות בין האגפים, והקוד מתקמפל.",
      "recap": "קודם `p`, אחר כך `p->data`.",
      "questionHtml": "מה הבעיה בתנאי הלולאה <code class=\"tok\" dir=\"ltr\">while (p-&gt;data != x &amp;&amp; p)</code> בחיפוש הערך <code class=\"tok\" dir=\"ltr\">x</code> ברשימה?",
      "explanationHtml": "האופרטור <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> מוערך משמאל לימין, ולכן <code class=\"tok\" dir=\"ltr\">p-&gt;data</code> נקרא לפני שבדקנו אם <code class=\"tok\" dir=\"ltr\">p</code> הוא NULL. כשהערך חסר, זו גישה ל-NULL ותוכנית קורסת (נבדק עם clang). כשהערך נמצא, הלולאה עוצרת כרגיל ואין בעיה, ולכן התשובה האחרונה שגויה. <code class=\"tok\" dir=\"ltr\">&amp;&amp;</code> לא חילופי כשיש תלות בין האגפים, והקוד מתקמפל.",
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
      "question": "מה קורה כשמריצים `while (p->next) p = p->next;` על רשימה מעגלית לא ריקה?",
      "options": [
       {
        "id": "a",
        "value": "הלולאה אינסופית, כי אין איבר ש-`next` שלו `NULL`",
        "type": "text",
        "html": "הלולאה אינסופית, כי אין איבר ש-<code class=\"tok\" dir=\"ltr\">next</code> שלו <code class=\"tok\" dir=\"ltr\">NULL</code>"
       },
       {
        "id": "b",
        "value": "הלולאה עוצרת באיבר האחרון",
        "type": "text",
        "html": "הלולאה עוצרת באיבר האחרון"
       },
       {
        "id": "c",
        "value": "הלולאה עוצרת כשהיא חוזרת להתחלה",
        "type": "text",
        "html": "הלולאה עוצרת כשהיא חוזרת להתחלה"
       },
       {
        "id": "d",
        "value": "קריסה מיידית",
        "type": "text",
        "html": "קריסה מיידית"
       }
      ],
      "correctId": "a",
      "explanation": "ברשימה מעגלית כל `next` מצביע על איבר אמיתי, ולכן התנאי תמיד אמת והלולאה לא נגמרת (נבדק עם clang). הלולאה לא יודעת מתי חזרנו להתחלה, אלא אם משווים ל-`start`. אין כאן גישה ל-NULL, ולכן אין קריסה.",
      "recap": "ברשימה מעגלית עוצרים בחזרה ל-`start`, לא ב-NULL.",
      "questionHtml": "מה קורה כשמריצים <code class=\"tok\" dir=\"ltr\">while (p-&gt;next) p = p-&gt;next;</code> על רשימה מעגלית לא ריקה?",
      "explanationHtml": "ברשימה מעגלית כל <code class=\"tok\" dir=\"ltr\">next</code> מצביע על איבר אמיתי, ולכן התנאי תמיד אמת והלולאה לא נגמרת (נבדק עם clang). הלולאה לא יודעת מתי חזרנו להתחלה, אלא אם משווים ל-<code class=\"tok\" dir=\"ltr\">start</code>. אין כאן גישה ל-NULL, ולכן אין קריסה.",
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
