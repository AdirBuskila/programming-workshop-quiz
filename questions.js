window.OPEN_BANK = {
 "meta": {
  "course": {
   "slug": "programming-workshop",
   "title": "סדנה מתקדמת בתכנות",
   "description": "תרגול מבחנים - סדנה מתקדמת בתכנות",
   "accent": "#facc15",
   "accent2": "#7c3aed",
   "storePrefix": "programming-workshop",
   "needHelp": [
    {
     "id": "linked_lists",
     "titleHe": "רשימות מקושרות",
     "icon": "🔗",
     "topic": "linked_lists",
     "entryLabelHe": "צריך עזרה ברשימות מקושרות?"
    },
    {
     "id": "dyn_2d",
     "titleHe": "מערכים דינמיים ודו-ממדיים",
     "icon": "🧱",
     "topic": "dynamic_arrays_2d",
     "entryLabelHe": "צריך עזרה במערכים דינמיים ודו-ממדיים?"
    },
    {
     "id": "files_strings",
     "titleHe": "קבצים ומחרוזות",
     "icon": "📄",
     "topic": "files",
     "entryLabelHe": "צריך עזרה בקבצים ובמחרוזות?"
    },
    {
     "id": "c_traps",
     "titleHe": "מלכודות C",
     "icon": "🪤",
     "topic": "c_traps_mcq",
     "entryLabelHe": "צריך עזרה במלכודות C?"
    }
   ]
  },
  "topics": [
   {
    "key": "c_basics_output",
    "label": "ערכים, אופרטורים ופלט"
   },
   {
    "key": "strings",
    "label": "מחרוזות"
   },
   {
    "key": "arrays_static",
    "label": "מערכים סטטיים ודו-ממדיים"
   },
   {
    "key": "pointers",
    "label": "מצביעים וכתובות"
   },
   {
    "key": "pointer_to_pointer",
    "label": "מצביע למצביע"
   },
   {
    "key": "dynamic_memory",
    "label": "הקצאה דינמית"
   },
   {
    "key": "dynamic_arrays_2d",
    "label": "מערכים דינמיים דו-ממדיים"
   },
   {
    "key": "structs_unions",
    "label": "מבנים ואיחודים"
   },
   {
    "key": "files",
    "label": "קבצי טקסט"
   },
   {
    "key": "linked_lists",
    "label": "רשימות מקושרות"
   },
   {
    "key": "list_manipulation",
    "label": "מיזוג והמרת רשימות"
   },
   {
    "key": "storage_classes",
    "label": "static, const ו-scope"
   },
   {
    "key": "bit_manipulation",
    "label": "פעולות סיביות"
   },
   {
    "key": "c_traps_mcq",
    "label": "מלכודות C"
   }
  ],
  "kinds": [
   "code",
   "mcq"
  ],
  "built": "2026-10-17T13:40:42Z",
  "exams": [
   {
    "examCode": "25B-B",
    "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
    "year": 2025,
    "source": "exam",
    "examDate": "29.07.2025"
   }
  ],
  "counts": {
   "total": 7,
   "contexts": 0,
   "math": 0,
   "steps": 0
  }
 },
 "contexts": {},
 "questions": [
  {
   "num": 1,
   "kind": "code",
   "topic": "linked_lists",
   "question": "נתונה הגדרה הבאה של הטיפוס:\n```c\ntypedef struct item\n{\n  int data;\n  struct item *next;\n} Item;\n```\nכתבו פונקציה `Item *lists_with_given_elements(Item **A, int n, Item *L)` אשר מקבלת מערך `A` של רשימות מקושרות עם גודלו `n` וגם רשימה מקושרת נפרדת `L`. כל הרשימות מורכבות מאיברים מסוג `Item`. שדות `data` של איברי `L` שונים זה מזה.\nעל הפונקציה לגלות את כל הרשימות במערך `A` שמכילות בתוכן את כל האיברים שמופיעים גם ב-`L`.\nיש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג `Item`) שתכיל את האינדקסים במערך `A` של כל הרשימות במערך שהן עומדות בדרישה הנ\"ל. אין חשיבות לסדר האיברים ברשימה החדשה.\nהפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר `NULL`.\n\nניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.\n\n**דוגמא:** באיור, הרשימות במערך `A` הן (לפי אינדקס) `0: 2,6,5,1,8`, `1: 8,3,5`, `2: 5`, `3: 1,2,8,5,3`, `4: 8,5,2,8`, והרשימה `L` היא `8,2,5`. הרשימות שמכילות את כל איברי `L` הן באינדקסים 0, 3 ו-4, ולכן הרשימה החדשה היא `0,3,4`.",
   "solution": "```c\n//Auxiliary function - checks whether all elements of L1 are in L2\nint List1_elements_in_List2(Item* L1, Item* L2)\n{\n    Item* ptr1 = L1, * ptr2 = L2;\n    int found;\n\n    /* whether L2 is not shorter L1*/\n    while (ptr1 && ptr2)\n    {\n        ptr1 = ptr1->next;\n        ptr2 = ptr2->next;\n    }\n    if (ptr1 && !ptr2)\n        return 0;\n    /*---------------------------------*/\n    /* searching each element of L1 in L2 */\n    ptr1 = L1;\n    while (ptr1)\n    {\n        found = 0;\n        ptr2 = L2;\n        while (ptr2)\n        {\n            if (ptr1->data == ptr2->data)\n            {\n                found = 1;\n                break;\n            }\n            ptr2 = ptr2->next;\n        } // while (ptr2)\n        if (!found)\n            return 0;\n        ptr1 = ptr1->next;\n    } // while (ptr1)\n    /*---------------------------------*/\n    return 1;\n}\n\n//Auxiliary function\nvoid insert_in_head(int x, Item **pl)\n{\n    Item *temp = (Item *)malloc(sizeof(Item));\n    temp->data = x;\n    temp->next = *pl;\n    *pl = temp;\n}\n\nItem *lists_with_given_elements(Item** A, int n, Item* L)\n{\n    int i;\n    Item *ind_list = NULL;\n    for (i = n - 1; i >= 0; i--)\n        if (List1_elements_in_List2(L, A[i]))\n            insert_in_head(i, &ind_list);\n    return ind_list;\n}\n```",
   "solutionSource": "official-pdf",
   "official": true,
   "confidence": "high",
   "points": 40,
   "image": "images/exams/25B-B-Q1.png",
   "id": "25B-B-Q1",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "רשימות מקושרות",
   "questionHtml": "נתונה הגדרה הבאה של הטיפוס:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct item\n{\n  int data;\n  struct item *next;\n} Item;</code></pre>כתבו פונקציה <code class=\"tok\" dir=\"ltr\">Item *lists_with_given_elements(Item **A, int n, Item *L)</code> אשר מקבלת מערך <code class=\"tok\" dir=\"ltr\">A</code> של רשימות מקושרות עם גודלו <code class=\"tok\" dir=\"ltr\">n</code> וגם רשימה מקושרת נפרדת <code class=\"tok\" dir=\"ltr\">L</code>. כל הרשימות מורכבות מאיברים מסוג <code class=\"tok\" dir=\"ltr\">Item</code>. שדות <code class=\"tok\" dir=\"ltr\">data</code> של איברי <code class=\"tok\" dir=\"ltr\">L</code> שונים זה מזה.<br>על הפונקציה לגלות את כל הרשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> שמכילות בתוכן את כל האיברים שמופיעים גם ב-<code class=\"tok\" dir=\"ltr\">L</code>.<br>יש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג <code class=\"tok\" dir=\"ltr\">Item</code>) שתכיל את האינדקסים במערך <code class=\"tok\" dir=\"ltr\">A</code> של כל הרשימות במערך שהן עומדות בדרישה הנ\"ל. אין חשיבות לסדר האיברים ברשימה החדשה.<br>הפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר <code class=\"tok\" dir=\"ltr\">NULL</code>.<br><br>ניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.<br><br><strong>דוגמא:</strong> באיור, הרשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> הן (לפי אינדקס) <code class=\"tok\" dir=\"ltr\">0: 2,6,5,1,8</code>, <code class=\"tok\" dir=\"ltr\">1: 8,3,5</code>, <code class=\"tok\" dir=\"ltr\">2: 5</code>, <code class=\"tok\" dir=\"ltr\">3: 1,2,8,5,3</code>, <code class=\"tok\" dir=\"ltr\">4: 8,5,2,8</code>, והרשימה <code class=\"tok\" dir=\"ltr\">L</code> היא <code class=\"tok\" dir=\"ltr\">8,2,5</code>. הרשימות שמכילות את כל איברי <code class=\"tok\" dir=\"ltr\">L</code> הן באינדקסים 0, 3 ו-4, ולכן הרשימה החדשה היא <code class=\"tok\" dir=\"ltr\">0,3,4</code>.",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>//Auxiliary function - checks whether all elements of L1 are in L2\nint List1_elements_in_List2(Item* L1, Item* L2)\n{\n    Item* ptr1 = L1, * ptr2 = L2;\n    int found;\n\n    /* whether L2 is not shorter L1*/\n    while (ptr1 &amp;&amp; ptr2)\n    {\n        ptr1 = ptr1-&gt;next;\n        ptr2 = ptr2-&gt;next;\n    }\n    if (ptr1 &amp;&amp; !ptr2)\n        return 0;\n    /*---------------------------------*/\n    /* searching each element of L1 in L2 */\n    ptr1 = L1;\n    while (ptr1)\n    {\n        found = 0;\n        ptr2 = L2;\n        while (ptr2)\n        {\n            if (ptr1-&gt;data == ptr2-&gt;data)\n            {\n                found = 1;\n                break;\n            }\n            ptr2 = ptr2-&gt;next;\n        } // while (ptr2)\n        if (!found)\n            return 0;\n        ptr1 = ptr1-&gt;next;\n    } // while (ptr1)\n    /*---------------------------------*/\n    return 1;\n}\n\n//Auxiliary function\nvoid insert_in_head(int x, Item **pl)\n{\n    Item *temp = (Item *)malloc(sizeof(Item));\n    temp-&gt;data = x;\n    temp-&gt;next = *pl;\n    *pl = temp;\n}\n\nItem *lists_with_given_elements(Item** A, int n, Item* L)\n{\n    int i;\n    Item *ind_list = NULL;\n    for (i = n - 1; i &gt;= 0; i--)\n        if (List1_elements_in_List2(L, A[i]))\n            insert_in_head(i, &amp;ind_list);\n    return ind_list;\n}</code></pre>",
   "pointsTotal": 40
  },
  {
   "num": 2,
   "kind": "code",
   "topic": "dynamic_arrays_2d",
   "question": "**האלכסון הראשי** של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית העליונה של המטריצה עד לפינה הימנית התחתונה.\nכל איברי המטריצה הריבועית הנמצאים מתחת לאלכסון הראשי שלה מרכיבים את **המשולש התחתון ממש** של המטריצה.\nכל איברי המטריצה הריבועית הנמצאים מעל האלכסון הראשי שלה מרכיבים את **המשולש העליון ממש** של המטריצה.\n\nכתבו פונקציה `int **triangles_to_matrix(int **tr_low, int **tr_up, int n)` אשר מקבלת שני **מערכים דו-ממדיים דינאמיים** של מספרים שלמים (בעלי `n` שורות בגדלים שונים) המיישמים את המשולש התחתון ממש ואת המשולש העליון ממש בהתאמה.\nעל הפונקציה ליצור מטריצה ריבועית בגודל `(n+1)×(n+1)` המבוססת על שני המשולשים הנ\"ל בה איברי האלכסון הראשי שווים ל-0. המטריצה מיושמת כ**מערך דו-ממדי דינאמי**. הפונקציה תחזיר את כתובת המערך.\n\n**דוגמא:**\nהמטריצה:\n```\n 0   7  -3  13\n76   0   8  42\n98   4   0  60\n11  19  21   0\n```\nהמשולש העליון:\n```\n7  -3  13\n    8  42\n       60\n```\nהמשולש התחתון:\n```\n76\n98   4\n11  19  21\n```\nגדלי השורות במערכים שהפונקציה מקבלת שווים לכמויות האיברים בשורות המתאימות של המשולשים. המשולש התחתון מוצג בזיכרון בצורתו הטבעית. שורות המשולש העליון בזיכרון מוזזות שמאלה בהשוואה לייצוג הטבעי שלהן.\n\nלמשל, המשולש התחתון והמשולש העליון של הדוגמא לעיל יוצגו בזיכרון באופן הבא (באיור).\n\nניתן להניח שיש בזיכרון מספיק מקום להקצאה.\n\n*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solution": "```c\nint** triangles_to_matrix(int** tr_low, int** tr_up, int n)\n{\n    int i, j, ** A;\n\n    A = (int**)calloc(n + 1, sizeof(int*));\n    for (i = 0; i < n + 1; i++)\n        A[i] = (int*)calloc(n + 1, sizeof(int));\n\n    /* lower triangle */\n    for (i = 1; i < n + 1; i++)\n        for (j = 0; j < i; j++)\n            A[i][j] = tr_low[i - 1][j];\n\n    /* upper triangle */\n    for (i = 0; i < n; i++)\n        for (j = i + 1; j < n + 1; j++)\n            A[i][j] = tr_up[i][j - i - 1];\n\n    return A;\n}\n```",
   "solutionSource": "official-pdf",
   "official": true,
   "confidence": "high",
   "points": 40,
   "image": "images/exams/25B-B-Q2.png",
   "id": "25B-B-Q2",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מערכים דינמיים דו-ממדיים",
   "questionHtml": "<strong>האלכסון הראשי</strong> של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית העליונה של המטריצה עד לפינה הימנית התחתונה.<br>כל איברי המטריצה הריבועית הנמצאים מתחת לאלכסון הראשי שלה מרכיבים את <strong>המשולש התחתון ממש</strong> של המטריצה.<br>כל איברי המטריצה הריבועית הנמצאים מעל האלכסון הראשי שלה מרכיבים את <strong>המשולש העליון ממש</strong> של המטריצה.<br><br>כתבו פונקציה <code class=\"tok\" dir=\"ltr\">int <strong>triangles_to_matrix(int </strong>tr_low, int **tr_up, int n)</code> אשר מקבלת שני <strong>מערכים דו-ממדיים דינאמיים</strong> של מספרים שלמים (בעלי <code class=\"tok\" dir=\"ltr\">n</code> שורות בגדלים שונים) המיישמים את המשולש התחתון ממש ואת המשולש העליון ממש בהתאמה.<br>על הפונקציה ליצור מטריצה ריבועית בגודל <code class=\"tok\" dir=\"ltr\">(n+1)×(n+1)</code> המבוססת על שני המשולשים הנ\"ל בה איברי האלכסון הראשי שווים ל-0. המטריצה מיושמת כ<strong>מערך דו-ממדי דינאמי</strong>. הפונקציה תחזיר את כתובת המערך.<br><br><strong>דוגמא:</strong><br>המטריצה:<pre class=\"code-block\" dir=\"ltr\"><code> 0   7  -3  13\n76   0   8  42\n98   4   0  60\n11  19  21   0</code></pre>המשולש העליון:<pre class=\"code-block\" dir=\"ltr\"><code>7  -3  13\n    8  42\n       60</code></pre>המשולש התחתון:<pre class=\"code-block\" dir=\"ltr\"><code>76\n98   4\n11  19  21</code></pre>גדלי השורות במערכים שהפונקציה מקבלת שווים לכמויות האיברים בשורות המתאימות של המשולשים. המשולש התחתון מוצג בזיכרון בצורתו הטבעית. שורות המשולש העליון בזיכרון מוזזות שמאלה בהשוואה לייצוג הטבעי שלהן.<br><br>למשל, המשולש התחתון והמשולש העליון של הדוגמא לעיל יוצגו בזיכרון באופן הבא (באיור).<br><br>ניתן להניח שיש בזיכרון מספיק מקום להקצאה.<br><br>*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int** triangles_to_matrix(int** tr_low, int** tr_up, int n)\n{\n    int i, j, ** A;\n\n    A = (int**)calloc(n + 1, sizeof(int*));\n    for (i = 0; i &lt; n + 1; i++)\n        A[i] = (int*)calloc(n + 1, sizeof(int));\n\n    /* lower triangle */\n    for (i = 1; i &lt; n + 1; i++)\n        for (j = 0; j &lt; i; j++)\n            A[i][j] = tr_low[i - 1][j];\n\n    /* upper triangle */\n    for (i = 0; i &lt; n; i++)\n        for (j = i + 1; j &lt; n + 1; j++)\n            A[i][j] = tr_up[i][j - i - 1];\n\n    return A;\n}</code></pre>",
   "pointsTotal": 40
  },
  {
   "num": 3,
   "kind": "code",
   "topic": "files",
   "question": "כתבו פונקציה `void text_to_binary(char *text_name, char *binary_name)` אשר מקבלת מחרוזות `text_name` ו-`binary_name` המהוות שמות של **קובץ טקסט** ושל **קובץ בינארי** בהתאמה.\n\nתוכן **קובץ הטקסט** מורכב משורות. בכל שורה נמצא מידע עבור לקוח בייצוג הבא:\n- מס' ת.ז. (9 תווים),\n- שם לקוח (30 תווים),\n- סכום סה\"כ קניות (מספר מסוג `double` שתופס 8 עמודות).\n\n**דוגמא:**\n```\n06842151          Moshe    71.25\n330578795      Benjamin  1755.65\n20051546           Dina   560.10\n```\nעל הפונקציה ליצור **קובץ בינארי** בעל אותו מידע שיש ב**קובץ הטקסט**. כל שורה של **קובץ הטקסט** תהפוך לרשומה ב**קובץ הבינארי**. הפורמט של כל רשומה יהיה מתאים למבנה `clientData` הבא:\n```c\ntypedef struct {\n    char id[10];\n    char name[31];\n    double total;\n} clientData;\n```\nכך ש-\n- `id` - מס' ת.ז.,\n- `name` - שם לקוח,\n- `total` - סכום סה\"כ קניות.\n\n**שימו לב:** פונקציה `fscanf` אשר ניתן להשתמש במהלך סריקת **קובץ הטקסט** מתעלמת מהרווחים השמאליים של המחרוזת הנקלטת ומתחילה את הקלט מהתו הראשון שאחריהם.\n\n*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solution": "```c\nvoid text_to_binary(char* text_name, char* binary_name)\n{\n    clientData client;\n\n    FILE* fin = fopen(text_name, \"r\");\n    FILE* fout = fopen(binary_name, \"w\");\n    if (!fin)  exit(1);\n    if (!fout)  exit(1);\n\n    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);\n    while (!feof(fin))\n    {\n        fwrite(&client, sizeof(clientData), 1, fout);\n        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);\n    }\n\n    fclose(fin);\n    fclose(fout);\n}\n```\n\n**הערת מתמלל (לא חלק מהפתרון הרשמי):** הפתרון הרשמי עובד על הדוגמה כאשר השורה האחרונה בקובץ מסתיימת בתו שורה חדשה. אם אין תו שורה חדשה אחרי השורה האחרונה, הקריאה האחרונה מגיעה ל-EOF כבר בקליטת `total`, ו-`feof` מחזיר אמת לפני כתיבת הרשומה האחרונה, כך שהיא אובדת. כמו כן הקובץ נפתח ב-`\"w\"` ולא ב-`\"wb\"`.",
   "solutionSource": "official-pdf",
   "official": true,
   "confidence": "high",
   "points": 40,
   "id": "25B-B-Q3",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "קבצי טקסט",
   "questionHtml": "כתבו פונקציה <code class=\"tok\" dir=\"ltr\">void text_to_binary(char *text_name, char *binary_name)</code> אשר מקבלת מחרוזות <code class=\"tok\" dir=\"ltr\">text_name</code> ו-<code class=\"tok\" dir=\"ltr\">binary_name</code> המהוות שמות של <strong>קובץ טקסט</strong> ושל <strong>קובץ בינארי</strong> בהתאמה.<br><br>תוכן <strong>קובץ הטקסט</strong> מורכב משורות. בכל שורה נמצא מידע עבור לקוח בייצוג הבא:<br>- מס' ת.ז. (9 תווים),<br>- שם לקוח (30 תווים),<br>- סכום סה\"כ קניות (מספר מסוג <code class=\"tok\" dir=\"ltr\">double</code> שתופס 8 עמודות).<br><br><strong>דוגמא:</strong><pre class=\"code-block\" dir=\"ltr\"><code>06842151          Moshe    71.25\n330578795      Benjamin  1755.65\n20051546           Dina   560.10</code></pre>על הפונקציה ליצור <strong>קובץ בינארי</strong> בעל אותו מידע שיש ב<strong>קובץ הטקסט</strong>. כל שורה של <strong>קובץ הטקסט</strong> תהפוך לרשומה ב<strong>קובץ הבינארי</strong>. הפורמט של כל רשומה יהיה מתאים למבנה <code class=\"tok\" dir=\"ltr\">clientData</code> הבא:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct {\n    char id[10];\n    char name[31];\n    double total;\n} clientData;</code></pre>כך ש-<br>- <code class=\"tok\" dir=\"ltr\">id</code> - מס' ת.ז.,<br>- <code class=\"tok\" dir=\"ltr\">name</code> - שם לקוח,<br>- <code class=\"tok\" dir=\"ltr\">total</code> - סכום סה\"כ קניות.<br><br><strong>שימו לב:</strong> פונקציה <code class=\"tok\" dir=\"ltr\">fscanf</code> אשר ניתן להשתמש במהלך סריקת <strong>קובץ הטקסט</strong> מתעלמת מהרווחים השמאליים של המחרוזת הנקלטת ומתחילה את הקלט מהתו הראשון שאחריהם.<br><br>*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void text_to_binary(char* text_name, char* binary_name)\n{\n    clientData client;\n\n    FILE* fin = fopen(text_name, \"r\");\n    FILE* fout = fopen(binary_name, \"w\");\n    if (!fin)  exit(1);\n    if (!fout)  exit(1);\n\n    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);\n    while (!feof(fin))\n    {\n        fwrite(&amp;client, sizeof(clientData), 1, fout);\n        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);\n    }\n\n    fclose(fin);\n    fclose(fout);\n}</code></pre><br><strong>הערת מתמלל (לא חלק מהפתרון הרשמי):</strong> הפתרון הרשמי עובד על הדוגמה כאשר השורה האחרונה בקובץ מסתיימת בתו שורה חדשה. אם אין תו שורה חדשה אחרי השורה האחרונה, הקריאה האחרונה מגיעה ל-EOF כבר בקליטת <code class=\"tok\" dir=\"ltr\">total</code>, ו-<code class=\"tok\" dir=\"ltr\">feof</code> מחזיר אמת לפני כתיבת הרשומה האחרונה, כך שהיא אובדת. כמו כן הקובץ נפתח ב-<code class=\"tok\" dir=\"ltr\">\"w\"</code> ולא ב-<code class=\"tok\" dir=\"ltr\">\"wb\"</code>.",
   "pointsTotal": 40
  },
  {
   "num": 4,
   "kind": "code",
   "topic": "storage_classes",
   "question": "מהו הפלט של התוכנית הבאה?\n```c\n#include <stdio.h>\n\nint y = 2;\n\nvoid f1() {\n    printf(\"1 \");\n}\n\nvoid f2() {\n    printf(\"2 \");\n}\n\nvoid f3() {\n    printf(\"3 \");\n}\n\nvoid f4() {\n    int x = 0;\n    static int y;\n    void (*p[3])() = {f1, f2, f3};\n\n    p[x]();\n    p[y]();\n    x++;\n    y++;\n}\n\nvoid f5() {\n    printf(\"%d \", y);\n    y++;\n}\n\nvoid main() {\n    int y;\n\n    for (y = 5; y <= 7; y++) {\n        f4();\n        printf(\"\\n\");\n    }\n    f5();\n    printf(\"%d\\n\", y);\n    f5();\n    printf(\"%d\\n\", y);\n}\n```\nיש לנמק את התשובה.",
   "solution": "**הפלט:**\n```\n1 1\n1 2\n1 3\n2 8\n3 8\n```\n**נימוק:**\nפונקציה `f4` בלולאה של `main` נקראת שלוש פעמים.\n`p` ב-פונקציה `f4` הוא מערך של שלושה מצביעים לפונקציות אשר מאותחל לפונקציות `f1`, `f2`, `f3`.\nמשתנה `x` מאותחל ל-0. משתנה `y` הוא `static` ולכן ערך התחלתי שלו 0 כברירת מחדל.\nלכן `p[x]` ו-`p[y]` הם גישות לאיבר `p[0]`, ז\"א קריאות לפונקציה `f1()` אשר מדפיסה 1. לכן הפלט באיטרציה הראשונה הוא\n`1 1`\nבסוף הפונקציה `f4`, מתקדמים `x` ו-`y`. בקריאה השנייה ל-`f4`, משתנה `x` שוב מאותחל ל-0. משתנה `y` הוא `static` ולכן השינוי שלו נשמר. אזי ערכי `x` ו-`y` הם 0 ו-1 בהתאמה.\nלכן `p[x]` ו-`p[y]` הם גישות לאיברי `p[0]` ו-`p[1]` בהתאמה, ז\"א קריאות לפונקציה `f1()` אשר מדפיסה 1 ולפונקציה `f2()` אשר מדפיסה 2. אזי הפלט באיטרציה השנייה הוא\n`1 2`\nבסוף הפונקציה `f4`, `x` ו-`y` מתקדמים שוב. בקריאה השלישית ל-`f4`, משתנה `x` שוב מאותחל ל-0. משתנה `y` הוא `static` ולכן השינוי שלו שוב נשמר. אזי ערכי `x` ו-`y` הם 0 ו-2 בהתאמה.\nלכן `p[x]` ו-`p[y]` הם גישות לאיברי `p[0]` ו-`p[2]` בהתאמה, ז\"א קריאות לפונקציה `f1()` אשר מדפיסה 1 ולפונקציה `f3()` אשר מדפיסה 3. אזי הפלט באיטרציה השלישית הוא\n`1 3`\nאחרי יציאה מהלולאה, נקראת פונקצית `f5` אשר מדפיסה ערך משתנה גלובלי `y` המאותחל ל-2 ומקדמת את `y` לאחר מכאן. מיד אחרי יציאה מ-`f5`, מודפס ערך `y` של `main`, אשר אחרי יציאה מהלולאה שווה ל-8. לכן הפלט בשורה הרביעית הוא\n`2 8`\nאחר כך, שוב נקראת פונקצית `f5` אשר מדפיסה ערך משתנה גלובלי `y` אשר אחרי השינוי בקריאה הקודמת שווה ל-3. מיד אחרי יציאה מ-`f5`, מודפס ערך `y` של `main`, אשר עדיין שווה ל-8. לכן הפלט בשורה החמישית הוא\n`3 8`",
   "solutionSource": "official-pdf",
   "official": true,
   "confidence": "high",
   "points": 10,
   "id": "25B-B-Q4",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "static, const ו-scope",
   "questionHtml": "מהו הפלט של התוכנית הבאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#include &lt;stdio.h&gt;\n\nint y = 2;\n\nvoid f1() {\n    printf(\"1 \");\n}\n\nvoid f2() {\n    printf(\"2 \");\n}\n\nvoid f3() {\n    printf(\"3 \");\n}\n\nvoid f4() {\n    int x = 0;\n    static int y;\n    void (*p[3])() = {f1, f2, f3};\n\n    p[x]();\n    p[y]();\n    x++;\n    y++;\n}\n\nvoid f5() {\n    printf(\"%d \", y);\n    y++;\n}\n\nvoid main() {\n    int y;\n\n    for (y = 5; y &lt;= 7; y++) {\n        f4();\n        printf(\"\\n\");\n    }\n    f5();\n    printf(\"%d\\n\", y);\n    f5();\n    printf(\"%d\\n\", y);\n}</code></pre>יש לנמק את התשובה.",
   "solutionHtml": "<strong>הפלט:</strong><pre class=\"code-block\" dir=\"ltr\"><code>1 1\n1 2\n1 3\n2 8\n3 8</code></pre><strong>נימוק:</strong><br>פונקציה <code class=\"tok\" dir=\"ltr\">f4</code> בלולאה של <code class=\"tok\" dir=\"ltr\">main</code> נקראת שלוש פעמים.<br><code class=\"tok\" dir=\"ltr\">p</code> ב-פונקציה <code class=\"tok\" dir=\"ltr\">f4</code> הוא מערך של שלושה מצביעים לפונקציות אשר מאותחל לפונקציות <code class=\"tok\" dir=\"ltr\">f1</code>, <code class=\"tok\" dir=\"ltr\">f2</code>, <code class=\"tok\" dir=\"ltr\">f3</code>.<br>משתנה <code class=\"tok\" dir=\"ltr\">x</code> מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן ערך התחלתי שלו 0 כברירת מחדל.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיבר <code class=\"tok\" dir=\"ltr\">p[0]</code>, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1. לכן הפלט באיטרציה הראשונה הוא<br><code class=\"tok\" dir=\"ltr\">1 1</code><br>בסוף הפונקציה <code class=\"tok\" dir=\"ltr\">f4</code>, מתקדמים <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code>. בקריאה השנייה ל-<code class=\"tok\" dir=\"ltr\">f4</code>, משתנה <code class=\"tok\" dir=\"ltr\">x</code> שוב מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן השינוי שלו נשמר. אזי ערכי <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> הם 0 ו-1 בהתאמה.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיברי <code class=\"tok\" dir=\"ltr\">p[0]</code> ו-<code class=\"tok\" dir=\"ltr\">p[1]</code> בהתאמה, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1 ולפונקציה <code class=\"tok\" dir=\"ltr\">f2()</code> אשר מדפיסה 2. אזי הפלט באיטרציה השנייה הוא<br><code class=\"tok\" dir=\"ltr\">1 2</code><br>בסוף הפונקציה <code class=\"tok\" dir=\"ltr\">f4</code>, <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> מתקדמים שוב. בקריאה השלישית ל-<code class=\"tok\" dir=\"ltr\">f4</code>, משתנה <code class=\"tok\" dir=\"ltr\">x</code> שוב מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן השינוי שלו שוב נשמר. אזי ערכי <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> הם 0 ו-2 בהתאמה.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיברי <code class=\"tok\" dir=\"ltr\">p[0]</code> ו-<code class=\"tok\" dir=\"ltr\">p[2]</code> בהתאמה, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1 ולפונקציה <code class=\"tok\" dir=\"ltr\">f3()</code> אשר מדפיסה 3. אזי הפלט באיטרציה השלישית הוא<br><code class=\"tok\" dir=\"ltr\">1 3</code><br>אחרי יציאה מהלולאה, נקראת פונקצית <code class=\"tok\" dir=\"ltr\">f5</code> אשר מדפיסה ערך משתנה גלובלי <code class=\"tok\" dir=\"ltr\">y</code> המאותחל ל-2 ומקדמת את <code class=\"tok\" dir=\"ltr\">y</code> לאחר מכאן. מיד אחרי יציאה מ-<code class=\"tok\" dir=\"ltr\">f5</code>, מודפס ערך <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code>, אשר אחרי יציאה מהלולאה שווה ל-8. לכן הפלט בשורה הרביעית הוא<br><code class=\"tok\" dir=\"ltr\">2 8</code><br>אחר כך, שוב נקראת פונקצית <code class=\"tok\" dir=\"ltr\">f5</code> אשר מדפיסה ערך משתנה גלובלי <code class=\"tok\" dir=\"ltr\">y</code> אשר אחרי השינוי בקריאה הקודמת שווה ל-3. מיד אחרי יציאה מ-<code class=\"tok\" dir=\"ltr\">f5</code>, מודפס ערך <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code>, אשר עדיין שווה ל-8. לכן הפלט בשורה החמישית הוא<br><code class=\"tok\" dir=\"ltr\">3 8</code>",
   "pointsTotal": 10
  },
  {
   "num": 5,
   "part": "א",
   "kind": "mcq",
   "topic": "structs_unions",
   "question": "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\nמהי הטענה הלא נכונה?",
   "options": [
    {
     "id": "a",
     "type": "text",
     "value": "מבנה יכול להיות שדה של מבנה אחר",
     "html": "מבנה יכול להיות שדה של מבנה אחר"
    },
    {
     "id": "b",
     "type": "text",
     "value": "מצביע למבנה יכול להיות שדה של מבנה אחר",
     "html": "מצביע למבנה יכול להיות שדה של מבנה אחר"
    },
    {
     "id": "c",
     "type": "text",
     "value": "מבנה יכול להיות שדה של אותו מבנה",
     "html": "מבנה יכול להיות שדה של אותו מבנה"
    },
    {
     "id": "d",
     "type": "text",
     "value": "מצביע למבנה יכול להיות שדה של אותו מבנה",
     "html": "מצביע למבנה יכול להיות שדה של אותו מבנה"
    },
    {
     "id": "e",
     "type": "text",
     "value": "כל הטענות לעיל הן נכונות",
     "html": "כל הטענות לעיל הן נכונות"
    }
   ],
   "correctId": "c",
   "explanation": "אם המבנה יתבסס על עצמו זו תהיה הגדרה אינסופית. והזיכרון הדרוש לא יהיה ידוע במהלך ההגדרה.",
   "official": true,
   "confidence": "high",
   "id": "25B-B-Q5a",
   "partKey": "a",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מבנים ואיחודים",
   "questionHtml": "בחרו את התשובה הנכונה <strong>ונמקו</strong> בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).<br>מהי הטענה הלא נכונה?",
   "explanationHtml": "אם המבנה יתבסס על עצמו זו תהיה הגדרה אינסופית. והזיכרון הדרוש לא יהיה ידוע במהלך ההגדרה.",
   "pointsTotal": 0
  },
  {
   "num": 5,
   "part": "ב",
   "kind": "mcq",
   "topic": "strings",
   "question": "בחרו את התשובה הנכונה **ונמקו** בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).\nמה עושים בקטע הבא?\n```c\nchar str1[] = \"hello\", *str2 = \"hello\";\nif (str1 == str2)   printf(\"yes\");\n```",
   "options": [
    {
     "id": "a",
     "type": "text",
     "value": "משווים את כתובות המחרוזות",
     "html": "משווים את כתובות המחרוזות"
    },
    {
     "id": "b",
     "type": "text",
     "value": "משווים את תכני המחרוזות",
     "html": "משווים את תכני המחרוזות"
    },
    {
     "id": "c",
     "type": "text",
     "value": "משווים את אורכי המחרוזות",
     "html": "משווים את אורכי המחרוזות"
    },
    {
     "id": "d",
     "type": "text",
     "value": "משווים תווים ראשונים של המחרוזות",
     "html": "משווים תווים ראשונים של המחרוזות"
    },
    {
     "id": "e",
     "type": "text",
     "value": "הקטע שגוי ויגרום לשגיאת קומפילציה",
     "html": "הקטע שגוי ויגרום לשגיאת קומפילציה"
    },
    {
     "id": "f",
     "type": "text",
     "value": "אף תשובה אינה נכונה",
     "html": "אף תשובה אינה נכונה"
    }
   ],
   "correctId": "a",
   "explanation": "גם `str1` וגם `str2` הם כתובות (כי `str1` הוא מערך ו-`str2` הוא מצביע במפורש).",
   "official": true,
   "confidence": "high",
   "id": "25B-B-Q5b",
   "partKey": "b",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מחרוזות",
   "questionHtml": "בחרו את התשובה הנכונה <strong>ונמקו</strong> בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).<br>מה עושים בקטע הבא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char str1[] = \"hello\", *str2 = \"hello\";\nif (str1 == str2)   printf(\"yes\");</code></pre>",
   "explanationHtml": "גם <code class=\"tok\" dir=\"ltr\">str1</code> וגם <code class=\"tok\" dir=\"ltr\">str2</code> הם כתובות (כי <code class=\"tok\" dir=\"ltr\">str1</code> הוא מערך ו-<code class=\"tok\" dir=\"ltr\">str2</code> הוא מצביע במפורש).",
   "pointsTotal": 0
  },
  {
   "num": 6,
   "kind": "code",
   "topic": "c_traps_mcq",
   "question": "מהו הפלט של התוכנית הבאה?\n```c\n#include <stdio.h>\n\nvoid main()\n{\n     char s[]={'/','/'/'/','/'/'/'/'/','/'};\n     int i;\n     for (i=0;s[i];i++) printf(\"%d\",s[i]/'/');\n}\n```\nיש לנמק את התשובה.",
   "solution": "**הפלט:** `10`\n\n**נימוק:**\nאיבר מס' 0 ב-`s` שווה ל-`'/'`. איבר מס' 1 ב-`s` שווה ל-`'/' / '/'`, ז\"א, ל-1. איבר מס' 2 הוא `'/' / '/' / '/'` ששווה ל-0 (קוד ASCII של `'/'` גדול מ-1 ולכן `'/' / 1` שווה ל-0).\nבלולאה סורקים את המערך מאיבר מס' 0. מכיוון שאיבר מס' 2 הוא 0, מטפלים רק באיברי מס' 0 ומס' 1. באיטרציה הראשונה מדפיסים ערך של `'/' / '/'`, ז\"א **1**. באיטרציה השנייה מדפיסים ערך של `'/' / 1`, ז\"א **0**. לכן הפלט יהיה\n`10`",
   "solutionSource": "official-pdf",
   "official": true,
   "confidence": "high",
   "points": 10,
   "id": "25B-B-Q6",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מלכודות C",
   "questionHtml": "מהו הפלט של התוכנית הבאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#include &lt;stdio.h&gt;\n\nvoid main()\n{\n     char s[]={'/','/'/'/','/'/'/'/'/','/'};\n     int i;\n     for (i=0;s[i];i++) printf(\"%d\",s[i]/'/');\n}</code></pre>יש לנמק את התשובה.",
   "solutionHtml": "<strong>הפלט:</strong> <code class=\"tok\" dir=\"ltr\">10</code><br><br><strong>נימוק:</strong><br>איבר מס' 0 ב-<code class=\"tok\" dir=\"ltr\">s</code> שווה ל-<code class=\"tok\" dir=\"ltr\">'/'</code>. איבר מס' 1 ב-<code class=\"tok\" dir=\"ltr\">s</code> שווה ל-<code class=\"tok\" dir=\"ltr\">'/' / '/'</code>, ז\"א, ל-1. איבר מס' 2 הוא <code class=\"tok\" dir=\"ltr\">'/' / '/' / '/'</code> ששווה ל-0 (קוד ASCII של <code class=\"tok\" dir=\"ltr\">'/'</code> גדול מ-1 ולכן <code class=\"tok\" dir=\"ltr\">'/' / 1</code> שווה ל-0).<br>בלולאה סורקים את המערך מאיבר מס' 0. מכיוון שאיבר מס' 2 הוא 0, מטפלים רק באיברי מס' 0 ומס' 1. באיטרציה הראשונה מדפיסים ערך של <code class=\"tok\" dir=\"ltr\">'/' / '/'</code>, ז\"א <strong>1</strong>. באיטרציה השנייה מדפיסים ערך של <code class=\"tok\" dir=\"ltr\">'/' / 1</code>, ז\"א <strong>0</strong>. לכן הפלט יהיה<br><code class=\"tok\" dir=\"ltr\">10</code>",
   "pointsTotal": 10
  }
 ]
};
