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
  "built": "2026-10-17T13:48:35Z",
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
   "steps": 23
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
   "rubric": [
    {
     "text": "פונקציית עזר שבודקת אם כל איברי `L` נמצאים ברשימה אחרת: לכל איבר של `L` חיפוש ברשימה, והחזרת 0 כשאיבר חסר",
     "points": 14,
     "html": "פונקציית עזר שבודקת אם כל איברי <code class=\"tok\" dir=\"ltr\">L</code> נמצאים ברשימה אחרת: לכל איבר של <code class=\"tok\" dir=\"ltr\">L</code> חיפוש ברשימה, והחזרת 0 כשאיבר חסר"
    },
    {
     "text": "מעבר על כל `n` הרשימות במערך `A` וקריאה לפונקציית העזר עבור כל אחת",
     "points": 9,
     "html": "מעבר על כל <code class=\"tok\" dir=\"ltr\">n</code> הרשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> וקריאה לפונקציית העזר עבור כל אחת"
    },
    {
     "text": "יצירת איבר `Item` חדש עם האינדקס `i` בשדה `data` (הקצאה דינמית) והוספתו לרשימה החדשה",
     "points": 9,
     "html": "יצירת איבר <code class=\"tok\" dir=\"ltr\">Item</code> חדש עם האינדקס <code class=\"tok\" dir=\"ltr\">i</code> בשדה <code class=\"tok\" dir=\"ltr\">data</code> (הקצאה דינמית) והוספתו לרשימה החדשה"
    },
    {
     "text": "החזרת כתובת האיבר הראשון של הרשימה החדשה, ו-`NULL` כשאין אף רשימה מתאימה",
     "points": 8,
     "html": "החזרת כתובת האיבר הראשון של הרשימה החדשה, ו-<code class=\"tok\" dir=\"ltr\">NULL</code> כשאין אף רשימה מתאימה"
    }
   ],
   "rubricSource": "ai-verified",
   "pitfalls": [
    "לבדוק רק שאורך הרשימה ב-`A[i]` שווה לאורך `L` או שהאיבר הראשון זהה, במקום לחפש כל איבר של `L` ברשימה.",
    "להוסיף לרשימה החדשה את `A[i]` או כתובת של איבר קיים במקום ליצור איבר `Item` חדש שמחזיק את האינדקס `i`.",
    "החזרת ערך שלא אותחל כאשר לא נמצא אף איבר מתאים"
   ],
   "steps": [
    {
     "type": "numeric",
     "prompt": "בדוגמה (`L` היא `8,2,5`) כמה רשימות במערך `A` מכילות את כל איברי `L`? כלומר, מה אורך הרשימה החדשה?",
     "answer": 3,
     "tol": 0,
     "explain": "הרשימות באינדקסים 0, 3 ו-4 מכילות את `8`, `2` ו-`5`, ולכן האורך 3 (ריצה אמיתית: 3, הרשימה `0 3 4`).",
     "promptHtml": "בדוגמה (<code class=\"tok\" dir=\"ltr\">L</code> היא <code class=\"tok\" dir=\"ltr\">8,2,5</code>) כמה רשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> מכילות את כל איברי <code class=\"tok\" dir=\"ltr\">L</code>? כלומר, מה אורך הרשימה החדשה?",
     "explainHtml": "הרשימות באינדקסים 0, 3 ו-4 מכילות את <code class=\"tok\" dir=\"ltr\">8</code>, <code class=\"tok\" dir=\"ltr\">2</code> ו-<code class=\"tok\" dir=\"ltr\">5</code>, ולכן האורך 3 (ריצה אמיתית: 3, הרשימה <code class=\"tok\" dir=\"ltr\">0 3 4</code>)."
    },
    {
     "type": "choice",
     "prompt": "מה מחזירה פונקציית העזר `List1_elements_in_List2(L, A[2])`, כאשר `A[2]` היא הרשימה `5` בלבד?",
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "`0`",
       "html": "<code class=\"tok\" dir=\"ltr\">0</code>"
      },
      {
       "id": "b",
       "type": "text",
       "value": "`1`",
       "html": "<code class=\"tok\" dir=\"ltr\">1</code>"
      },
      {
       "id": "c",
       "type": "text",
       "value": "`NULL`",
       "html": "<code class=\"tok\" dir=\"ltr\">NULL</code>"
      },
      {
       "id": "d",
       "type": "text",
       "value": "`2`",
       "html": "<code class=\"tok\" dir=\"ltr\">2</code>"
      }
     ],
     "correctId": "a",
     "explain": "`A[2]` קצרה מ-`L`, ולכן הבדיקה הראשונה בפונקציה מחזירה 0 לפני החיפוש (ריצה אמיתית: 0). הפונקציה מחזירה 1 רק כשכל האיברים נמצאו.",
     "promptHtml": "מה מחזירה פונקציית העזר <code class=\"tok\" dir=\"ltr\">List1_elements_in_List2(L, A[2])</code>, כאשר <code class=\"tok\" dir=\"ltr\">A[2]</code> היא הרשימה <code class=\"tok\" dir=\"ltr\">5</code> בלבד?",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">A[2]</code> קצרה מ-<code class=\"tok\" dir=\"ltr\">L</code>, ולכן הבדיקה הראשונה בפונקציה מחזירה 0 לפני החיפוש (ריצה אמיתית: 0). הפונקציה מחזירה 1 רק כשכל האיברים נמצאו."
    },
    {
     "type": "fillblank",
     "prompt": "השלימו את השורה החסרה בפונקציה הראשית.",
     "code": true,
     "lines": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i >= 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "___",
      "    return ind_list;",
      "}"
     ],
     "blankIndex": 6,
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "insert_in_head(i, &ind_list);",
       "html": "insert_in_head(i, &amp;ind_list);"
      },
      {
       "id": "b",
       "type": "text",
       "value": "insert_in_head(A[i], &ind_list);",
       "html": "insert_in_head(A[i], &amp;ind_list);"
      },
      {
       "id": "c",
       "type": "text",
       "value": "insert_in_head(L->data, &ind_list);",
       "html": "insert_in_head(L-&gt;data, &amp;ind_list);"
      },
      {
       "id": "d",
       "type": "text",
       "value": "ind_list = A[i];",
       "html": "ind_list = A[i];"
      }
     ],
     "correctId": "a",
     "explain": "לרשימה החדשה מוסיפים איבר חדש שמחזיק את האינדקס `i` (ולא את `A[i]`), והכתובת המעודכנת של הראש נשמרת דרך `&ind_list`.",
     "promptHtml": "השלימו את השורה החסרה בפונקציה הראשית.",
     "explainHtml": "לרשימה החדשה מוסיפים איבר חדש שמחזיק את האינדקס <code class=\"tok\" dir=\"ltr\">i</code> (ולא את <code class=\"tok\" dir=\"ltr\">A[i]</code>), והכתובת המעודכנת של הראש נשמרת דרך <code class=\"tok\" dir=\"ltr\">&amp;ind_list</code>.",
     "linesHtml": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i &gt;= 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "___",
      "    return ind_list;",
      "}"
     ]
    },
    {
     "type": "order",
     "prompt": "סדרו את שורות הפונקציה `lists_with_given_elements`.",
     "code": true,
     "lines": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i >= 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "            insert_in_head(i, &ind_list);",
      "    return ind_list;",
      "}"
     ],
     "explain": "הכרזה על המשתנים, אתחול הרשימה החדשה ל-`NULL`, לולאה על האינדקסים, בדיקה והוספה, ובסוף החזרת הראש.",
     "promptHtml": "סדרו את שורות הפונקציה <code class=\"tok\" dir=\"ltr\">lists_with_given_elements</code>.",
     "explainHtml": "הכרזה על המשתנים, אתחול הרשימה החדשה ל-<code class=\"tok\" dir=\"ltr\">NULL</code>, לולאה על האינדקסים, בדיקה והוספה, ובסוף החזרת הראש.",
     "linesHtml": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i &gt;= 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "            insert_in_head(i, &amp;ind_list);",
      "    return ind_list;",
      "}"
     ]
    },
    {
     "type": "findbug",
     "prompt": "בגרסה הבאה שורה אחת שונתה. הפלט על הדוגמה הוא `3 4` במקום `0 3 4`. מצאו את השורה.",
     "code": true,
     "lines": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i > 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "            insert_in_head(i, &ind_list);",
      "    return ind_list;",
      "}"
     ],
     "bugIndex": 4,
     "explain": "`i > 0` במקום `i >= 0` מדלג על האינדקס 0, ולכן האינדקס 0 חסר (ריצה אמיתית: `3 4`).",
     "promptHtml": "בגרסה הבאה שורה אחת שונתה. הפלט על הדוגמה הוא <code class=\"tok\" dir=\"ltr\">3 4</code> במקום <code class=\"tok\" dir=\"ltr\">0 3 4</code>. מצאו את השורה.",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">i &gt; 0</code> במקום <code class=\"tok\" dir=\"ltr\">i &gt;= 0</code> מדלג על האינדקס 0, ולכן האינדקס 0 חסר (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">3 4</code>).",
     "linesHtml": [
      "Item *lists_with_given_elements(Item** A, int n, Item* L)",
      "{",
      "    int i;",
      "    Item *ind_list = NULL;",
      "    for (i = n - 1; i &gt; 0; i--)",
      "        if (List1_elements_in_List2(L, A[i]))",
      "            insert_in_head(i, &amp;ind_list);",
      "    return ind_list;",
      "}"
     ]
    }
   ],
   "stepsSource": "ai-verified",
   "id": "25B-B-Q1",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "רשימות מקושרות",
   "questionHtml": "נתונה הגדרה הבאה של הטיפוס:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct item\n{\n  int data;\n  struct item *next;\n} Item;</code></pre>כתבו פונקציה <code class=\"tok\" dir=\"ltr\">Item *lists_with_given_elements(Item **A, int n, Item *L)</code> אשר מקבלת מערך <code class=\"tok\" dir=\"ltr\">A</code> של רשימות מקושרות עם גודלו <code class=\"tok\" dir=\"ltr\">n</code> וגם רשימה מקושרת נפרדת <code class=\"tok\" dir=\"ltr\">L</code>. כל הרשימות מורכבות מאיברים מסוג <code class=\"tok\" dir=\"ltr\">Item</code>. שדות <code class=\"tok\" dir=\"ltr\">data</code> של איברי <code class=\"tok\" dir=\"ltr\">L</code> שונים זה מזה.<br>על הפונקציה לגלות את כל הרשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> שמכילות בתוכן את כל האיברים שמופיעים גם ב-<code class=\"tok\" dir=\"ltr\">L</code>.<br>יש ליצור רשימה חדשה (אשר גם היא תהיה מורכבת מאיברים מסוג <code class=\"tok\" dir=\"ltr\">Item</code>) שתכיל את האינדקסים במערך <code class=\"tok\" dir=\"ltr\">A</code> של כל הרשימות במערך שהן עומדות בדרישה הנ\"ל. אין חשיבות לסדר האיברים ברשימה החדשה.<br>הפונקציה תחזיר את כתובת האיבר הראשון של הרשימה החדשה. אם הרשימה החדשה תהיה ריקה, הפונקציה תחזיר <code class=\"tok\" dir=\"ltr\">NULL</code>.<br><br>ניתן להניח שיש בזיכרון מספיק מקום להקצאת איברי הרשימה החדשה.<br><br><strong>דוגמא:</strong> באיור, הרשימות במערך <code class=\"tok\" dir=\"ltr\">A</code> הן (לפי אינדקס) <code class=\"tok\" dir=\"ltr\">0: 2,6,5,1,8</code>, <code class=\"tok\" dir=\"ltr\">1: 8,3,5</code>, <code class=\"tok\" dir=\"ltr\">2: 5</code>, <code class=\"tok\" dir=\"ltr\">3: 1,2,8,5,3</code>, <code class=\"tok\" dir=\"ltr\">4: 8,5,2,8</code>, והרשימה <code class=\"tok\" dir=\"ltr\">L</code> היא <code class=\"tok\" dir=\"ltr\">8,2,5</code>. הרשימות שמכילות את כל איברי <code class=\"tok\" dir=\"ltr\">L</code> הן באינדקסים 0, 3 ו-4, ולכן הרשימה החדשה היא <code class=\"tok\" dir=\"ltr\">0,3,4</code>.",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>//Auxiliary function - checks whether all elements of L1 are in L2\nint List1_elements_in_List2(Item* L1, Item* L2)\n{\n    Item* ptr1 = L1, * ptr2 = L2;\n    int found;\n\n    /* whether L2 is not shorter L1*/\n    while (ptr1 &amp;&amp; ptr2)\n    {\n        ptr1 = ptr1-&gt;next;\n        ptr2 = ptr2-&gt;next;\n    }\n    if (ptr1 &amp;&amp; !ptr2)\n        return 0;\n    /*---------------------------------*/\n    /* searching each element of L1 in L2 */\n    ptr1 = L1;\n    while (ptr1)\n    {\n        found = 0;\n        ptr2 = L2;\n        while (ptr2)\n        {\n            if (ptr1-&gt;data == ptr2-&gt;data)\n            {\n                found = 1;\n                break;\n            }\n            ptr2 = ptr2-&gt;next;\n        } // while (ptr2)\n        if (!found)\n            return 0;\n        ptr1 = ptr1-&gt;next;\n    } // while (ptr1)\n    /*---------------------------------*/\n    return 1;\n}\n\n//Auxiliary function\nvoid insert_in_head(int x, Item **pl)\n{\n    Item *temp = (Item *)malloc(sizeof(Item));\n    temp-&gt;data = x;\n    temp-&gt;next = *pl;\n    *pl = temp;\n}\n\nItem *lists_with_given_elements(Item** A, int n, Item* L)\n{\n    int i;\n    Item *ind_list = NULL;\n    for (i = n - 1; i &gt;= 0; i--)\n        if (List1_elements_in_List2(L, A[i]))\n            insert_in_head(i, &amp;ind_list);\n    return ind_list;\n}</code></pre>",
   "pointsTotal": 40,
   "pitfallsHtml": [
    "לבדוק רק שאורך הרשימה ב-<code class=\"tok\" dir=\"ltr\">A[i]</code> שווה לאורך <code class=\"tok\" dir=\"ltr\">L</code> או שהאיבר הראשון זהה, במקום לחפש כל איבר של <code class=\"tok\" dir=\"ltr\">L</code> ברשימה.",
    "להוסיף לרשימה החדשה את <code class=\"tok\" dir=\"ltr\">A[i]</code> או כתובת של איבר קיים במקום ליצור איבר <code class=\"tok\" dir=\"ltr\">Item</code> חדש שמחזיק את האינדקס <code class=\"tok\" dir=\"ltr\">i</code>.",
    "החזרת ערך שלא אותחל כאשר לא נמצא אף איבר מתאים"
   ]
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
   "rubric": [
    {
     "text": "הקצאת מערך מצביעים בגודל `n+1` והקצאת כל שורה בגודל `n+1` עם איפוס (`calloc`) כך שהאלכסון הראשי 0",
     "points": 10,
     "html": "הקצאת מערך מצביעים בגודל <code class=\"tok\" dir=\"ltr\">n+1</code> והקצאת כל שורה בגודל <code class=\"tok\" dir=\"ltr\">n+1</code> עם איפוס (<code class=\"tok\" dir=\"ltr\">calloc</code>) כך שהאלכסון הראשי 0"
    },
    {
     "text": "העתקת המשולש התחתון: `A[i][j] = tr_low[i-1][j]` עבור `i` מ-1 עד `n` ו-`j < i`",
     "points": 12,
     "html": "העתקת המשולש התחתון: <code class=\"tok\" dir=\"ltr\">A[i][j] = tr_low[i-1][j]</code> עבור <code class=\"tok\" dir=\"ltr\">i</code> מ-1 עד <code class=\"tok\" dir=\"ltr\">n</code> ו-<code class=\"tok\" dir=\"ltr\">j &lt; i</code>"
    },
    {
     "text": "העתקת המשולש העליון עם הזזה: `A[i][j] = tr_up[i][j-i-1]` עבור `j` מ-`i+1` עד `n`",
     "points": 12,
     "html": "העתקת המשולש העליון עם הזזה: <code class=\"tok\" dir=\"ltr\">A[i][j] = tr_up[i][j-i-1]</code> עבור <code class=\"tok\" dir=\"ltr\">j</code> מ-<code class=\"tok\" dir=\"ltr\">i+1</code> עד <code class=\"tok\" dir=\"ltr\">n</code>"
    },
    {
     "text": "החזרת כתובת המערך",
     "points": 6,
     "html": "החזרת כתובת המערך"
    }
   ],
   "rubricSource": "ai-verified",
   "pitfalls": [
    "לשכוח שהמטריצה בגודל `(n+1)×(n+1)` ולהקצות `n×n`, או לא לאפס את האלכסון הראשי (שימוש ב-`malloc` במקום `calloc`).",
    "לגשת למשולש העליון ב-`tr_up[i][j]` במקום `tr_up[i][j-i-1]`, בלי להתחשב בכך ששורותיו מוזזות שמאלה בזיכרון.",
    "לחשב שורות של המשולש התחתון ב-`tr_low[i][j]` במקום `tr_low[i-1][j]`: ל-`tr_low` יש `n` שורות והראשונה מתאימה לשורה 1 של המטריצה."
   ],
   "steps": [
    {
     "type": "numeric",
     "prompt": "בדוגמה (`n = 3`), מה ערך `A[2][1]` בסוף הפונקציה? (תא מתחת לאלכסון הראשי)",
     "answer": 4,
     "tol": 0,
     "explain": "`A[2][1] = tr_low[1][1] = 4` (ריצה אמיתית: 4).",
     "promptHtml": "בדוגמה (<code class=\"tok\" dir=\"ltr\">n = 3</code>), מה ערך <code class=\"tok\" dir=\"ltr\">A[2][1]</code> בסוף הפונקציה? (תא מתחת לאלכסון הראשי)",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">A[2][1] = tr_low[1][1] = 4</code> (ריצה אמיתית: 4)."
    },
    {
     "type": "numeric",
     "prompt": "באותה דוגמה, מה ערך `A[1][3]`?",
     "answer": 42,
     "tol": 0,
     "explain": "`A[1][3] = tr_up[1][3-1-1] = tr_up[1][1] = 42` (ריצה אמיתית: 42).",
     "promptHtml": "באותה דוגמה, מה ערך <code class=\"tok\" dir=\"ltr\">A[1][3]</code>?",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">A[1][3] = tr_up[1][3-1-1] = tr_up[1][1] = 42</code> (ריצה אמיתית: 42)."
    },
    {
     "type": "choice",
     "prompt": "באיזה אינדקס בשורה `tr_up[i]` נמצא האיבר של `A[i][j]` (כש-`j > i`)?",
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "`j - i - 1`",
       "html": "<code class=\"tok\" dir=\"ltr\">j - i - 1</code>"
      },
      {
       "id": "b",
       "type": "text",
       "value": "`j`",
       "html": "<code class=\"tok\" dir=\"ltr\">j</code>"
      },
      {
       "id": "c",
       "type": "text",
       "value": "`j - i`",
       "html": "<code class=\"tok\" dir=\"ltr\">j - i</code>"
      },
      {
       "id": "d",
       "type": "text",
       "value": "`j + i`",
       "html": "<code class=\"tok\" dir=\"ltr\">j + i</code>"
      }
     ],
     "correctId": "a",
     "explain": "שורה `i` של המשולש העליון מתחילה באיבר `A[i][i+1]`, ולכן האינדקס הוא `j-i-1` (הדוגמה: `A[1][3]` נמצא באינדקס 1).",
     "promptHtml": "באיזה אינדקס בשורה <code class=\"tok\" dir=\"ltr\">tr_up[i]</code> נמצא האיבר של <code class=\"tok\" dir=\"ltr\">A[i][j]</code> (כש-<code class=\"tok\" dir=\"ltr\">j &gt; i</code>)?",
     "explainHtml": "שורה <code class=\"tok\" dir=\"ltr\">i</code> של המשולש העליון מתחילה באיבר <code class=\"tok\" dir=\"ltr\">A[i][i+1]</code>, ולכן האינדקס הוא <code class=\"tok\" dir=\"ltr\">j-i-1</code> (הדוגמה: <code class=\"tok\" dir=\"ltr\">A[1][3]</code> נמצא באינדקס 1)."
    },
    {
     "type": "fillblank",
     "prompt": "השלימו את השורה החסרה בפונקציה.",
     "code": true,
     "lines": [
      "int** triangles_to_matrix(int** tr_low, int** tr_up, int n)",
      "{",
      "    int i, j, ** A;",
      "    A = (int**)calloc(n + 1, sizeof(int*));",
      "    for (i = 0; i < n + 1; i++)",
      "        A[i] = (int*)calloc(n + 1, sizeof(int));",
      "    /* lower triangle */",
      "    for (i = 1; i < n + 1; i++)",
      "        for (j = 0; j < i; j++)",
      "            A[i][j] = tr_low[i - 1][j];",
      "    /* upper triangle */",
      "    for (i = 0; i < n; i++)",
      "        for (j = i + 1; j < n + 1; j++)",
      "___",
      "    return A;",
      "}"
     ],
     "blankIndex": 13,
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "A[i][j] = tr_up[i][j - i - 1];",
       "html": "A[i][j] = tr_up[i][j - i - 1];"
      },
      {
       "id": "b",
       "type": "text",
       "value": "A[i][j] = tr_up[i][j];",
       "html": "A[i][j] = tr_up[i][j];"
      },
      {
       "id": "c",
       "type": "text",
       "value": "A[i][j] = tr_up[i - 1][j];",
       "html": "A[i][j] = tr_up[i - 1][j];"
      },
      {
       "id": "d",
       "type": "text",
       "value": "A[i][j] = tr_low[i][j - i - 1];",
       "html": "A[i][j] = tr_low[i][j - i - 1];"
      }
     ],
     "correctId": "a",
     "explain": "שורות המשולש העליון מוזזות שמאלה, ולכן הגישה היא עם `j - i - 1`.",
     "promptHtml": "השלימו את השורה החסרה בפונקציה.",
     "explainHtml": "שורות המשולש העליון מוזזות שמאלה, ולכן הגישה היא עם <code class=\"tok\" dir=\"ltr\">j - i - 1</code>.",
     "linesHtml": [
      "int** triangles_to_matrix(int** tr_low, int** tr_up, int n)",
      "{",
      "    int i, j, ** A;",
      "    A = (int**)calloc(n + 1, sizeof(int*));",
      "    for (i = 0; i &lt; n + 1; i++)",
      "        A[i] = (int*)calloc(n + 1, sizeof(int));",
      "    /* lower triangle */",
      "    for (i = 1; i &lt; n + 1; i++)",
      "        for (j = 0; j &lt; i; j++)",
      "            A[i][j] = tr_low[i - 1][j];",
      "    /* upper triangle */",
      "    for (i = 0; i &lt; n; i++)",
      "        for (j = i + 1; j &lt; n + 1; j++)",
      "___",
      "    return A;",
      "}"
     ]
    },
    {
     "type": "findbug",
     "prompt": "בגרסה הבאה שורה אחת שונתה והעמודה האחרונה של המטריצה נשארת 0 במקום `13, 42, 60`. מצאו אותה.",
     "code": true,
     "lines": [
      "int** triangles_to_matrix(int** tr_low, int** tr_up, int n)",
      "{",
      "    int i, j, ** A;",
      "    A = (int**)calloc(n + 1, sizeof(int*));",
      "    for (i = 0; i < n + 1; i++)",
      "        A[i] = (int*)calloc(n + 1, sizeof(int));",
      "    /* lower triangle */",
      "    for (i = 1; i < n + 1; i++)",
      "        for (j = 0; j < i; j++)",
      "            A[i][j] = tr_low[i - 1][j];",
      "    /* upper triangle */",
      "    for (i = 0; i < n; i++)",
      "        for (j = i + 1; j < n; j++)",
      "            A[i][j] = tr_up[i][j - i - 1];",
      "    return A;",
      "}"
     ],
     "bugIndex": 12,
     "explain": "`j < n` במקום `j < n + 1` לא ממלא את העמודה האחרונה (ריצה אמיתית: `A[0][3]` יצא 0 במקום 13).",
     "promptHtml": "בגרסה הבאה שורה אחת שונתה והעמודה האחרונה של המטריצה נשארת 0 במקום <code class=\"tok\" dir=\"ltr\">13, 42, 60</code>. מצאו אותה.",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">j &lt; n</code> במקום <code class=\"tok\" dir=\"ltr\">j &lt; n + 1</code> לא ממלא את העמודה האחרונה (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">A[0][3]</code> יצא 0 במקום 13).",
     "linesHtml": [
      "int** triangles_to_matrix(int** tr_low, int** tr_up, int n)",
      "{",
      "    int i, j, ** A;",
      "    A = (int**)calloc(n + 1, sizeof(int*));",
      "    for (i = 0; i &lt; n + 1; i++)",
      "        A[i] = (int*)calloc(n + 1, sizeof(int));",
      "    /* lower triangle */",
      "    for (i = 1; i &lt; n + 1; i++)",
      "        for (j = 0; j &lt; i; j++)",
      "            A[i][j] = tr_low[i - 1][j];",
      "    /* upper triangle */",
      "    for (i = 0; i &lt; n; i++)",
      "        for (j = i + 1; j &lt; n; j++)",
      "            A[i][j] = tr_up[i][j - i - 1];",
      "    return A;",
      "}"
     ]
    }
   ],
   "stepsSource": "ai-verified",
   "id": "25B-B-Q2",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מערכים דינמיים דו-ממדיים",
   "questionHtml": "<strong>האלכסון הראשי</strong> של מטריצה ריבועית הוא האלכסון שמתחיל מהפינה השמאלית העליונה של המטריצה עד לפינה הימנית התחתונה.<br>כל איברי המטריצה הריבועית הנמצאים מתחת לאלכסון הראשי שלה מרכיבים את <strong>המשולש התחתון ממש</strong> של המטריצה.<br>כל איברי המטריצה הריבועית הנמצאים מעל האלכסון הראשי שלה מרכיבים את <strong>המשולש העליון ממש</strong> של המטריצה.<br><br>כתבו פונקציה <code class=\"tok\" dir=\"ltr\">int <strong>triangles_to_matrix(int </strong>tr_low, int **tr_up, int n)</code> אשר מקבלת שני <strong>מערכים דו-ממדיים דינאמיים</strong> של מספרים שלמים (בעלי <code class=\"tok\" dir=\"ltr\">n</code> שורות בגדלים שונים) המיישמים את המשולש התחתון ממש ואת המשולש העליון ממש בהתאמה.<br>על הפונקציה ליצור מטריצה ריבועית בגודל <code class=\"tok\" dir=\"ltr\">(n+1)×(n+1)</code> המבוססת על שני המשולשים הנ\"ל בה איברי האלכסון הראשי שווים ל-0. המטריצה מיושמת כ<strong>מערך דו-ממדי דינאמי</strong>. הפונקציה תחזיר את כתובת המערך.<br><br><strong>דוגמא:</strong><br>המטריצה:<pre class=\"code-block\" dir=\"ltr\"><code> 0   7  -3  13\n76   0   8  42\n98   4   0  60\n11  19  21   0</code></pre>המשולש העליון:<pre class=\"code-block\" dir=\"ltr\"><code>7  -3  13\n    8  42\n       60</code></pre>המשולש התחתון:<pre class=\"code-block\" dir=\"ltr\"><code>76\n98   4\n11  19  21</code></pre>גדלי השורות במערכים שהפונקציה מקבלת שווים לכמויות האיברים בשורות המתאימות של המשולשים. המשולש התחתון מוצג בזיכרון בצורתו הטבעית. שורות המשולש העליון בזיכרון מוזזות שמאלה בהשוואה לייצוג הטבעי שלהן.<br><br>למשל, המשולש התחתון והמשולש העליון של הדוגמא לעיל יוצגו בזיכרון באופן הבא (באיור).<br><br>ניתן להניח שיש בזיכרון מספיק מקום להקצאה.<br><br>*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>int** triangles_to_matrix(int** tr_low, int** tr_up, int n)\n{\n    int i, j, ** A;\n\n    A = (int**)calloc(n + 1, sizeof(int*));\n    for (i = 0; i &lt; n + 1; i++)\n        A[i] = (int*)calloc(n + 1, sizeof(int));\n\n    /* lower triangle */\n    for (i = 1; i &lt; n + 1; i++)\n        for (j = 0; j &lt; i; j++)\n            A[i][j] = tr_low[i - 1][j];\n\n    /* upper triangle */\n    for (i = 0; i &lt; n; i++)\n        for (j = i + 1; j &lt; n + 1; j++)\n            A[i][j] = tr_up[i][j - i - 1];\n\n    return A;\n}</code></pre>",
   "pointsTotal": 40,
   "pitfallsHtml": [
    "לשכוח שהמטריצה בגודל <code class=\"tok\" dir=\"ltr\">(n+1)×(n+1)</code> ולהקצות <code class=\"tok\" dir=\"ltr\">n×n</code>, או לא לאפס את האלכסון הראשי (שימוש ב-<code class=\"tok\" dir=\"ltr\">malloc</code> במקום <code class=\"tok\" dir=\"ltr\">calloc</code>).",
    "לגשת למשולש העליון ב-<code class=\"tok\" dir=\"ltr\">tr_up[i][j]</code> במקום <code class=\"tok\" dir=\"ltr\">tr_up[i][j-i-1]</code>, בלי להתחשב בכך ששורותיו מוזזות שמאלה בזיכרון.",
    "לחשב שורות של המשולש התחתון ב-<code class=\"tok\" dir=\"ltr\">tr_low[i][j]</code> במקום <code class=\"tok\" dir=\"ltr\">tr_low[i-1][j]</code>: ל-<code class=\"tok\" dir=\"ltr\">tr_low</code> יש <code class=\"tok\" dir=\"ltr\">n</code> שורות והראשונה מתאימה לשורה 1 של המטריצה."
   ]
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
   "rubric": [
    {
     "text": "פתיחת קובץ הטקסט לקריאה וקובץ הבינארי לכתיבה, ובדיקה שהפתיחה הצליחה",
     "points": 8,
     "html": "פתיחת קובץ הטקסט לקריאה וקובץ הבינארי לכתיבה, ובדיקה שהפתיחה הצליחה"
    },
    {
     "text": "קריאת שורה עם `fscanf` ובפורמט שמתאים לשדות: מחרוזת של עד 9 תווים, מחרוזת של עד 30 תווים ו-`double`",
     "points": 12,
     "html": "קריאת שורה עם <code class=\"tok\" dir=\"ltr\">fscanf</code> ובפורמט שמתאים לשדות: מחרוזת של עד 9 תווים, מחרוזת של עד 30 תווים ו-<code class=\"tok\" dir=\"ltr\">double</code>"
    },
    {
     "text": "כתיבת הרשומה לקובץ הבינארי עם `fwrite` בגודל `sizeof(clientData)` לכל שורה",
     "points": 12,
     "html": "כתיבת הרשומה לקובץ הבינארי עם <code class=\"tok\" dir=\"ltr\">fwrite</code> בגודל <code class=\"tok\" dir=\"ltr\">sizeof(clientData)</code> לכל שורה"
    },
    {
     "text": "לולאה שמסתיימת בסוף הקובץ ושלא מפספסת שורה, וסגירת שני הקבצים",
     "points": 8,
     "html": "לולאה שמסתיימת בסוף הקובץ ושלא מפספסת שורה, וסגירת שני הקבצים"
    }
   ],
   "rubricSource": "ai-verified",
   "pitfalls": [
    "לכתוב ל-`fwrite` גודל שגוי, למשל `sizeof(client.id)` במקום `sizeof(clientData)`, ולקבל רשומות חלקיות בקובץ הבינארי.",
    "לקלוט את השם עם `%s` ללא הגבלת רוחב (או `%10s` ל-`id`), ולכתוב מחוץ לגבולות המערך `char id[10]`.",
    "לבצע בדיקת `feof` לפני הקריאה הראשונה או רק אחרי הקריאה של השורה, ולכתוב רשומה אחת יותר או פחות מדי."
   ],
   "steps": [
    {
     "type": "numeric",
     "prompt": "מה `sizeof(clientData)` במחשב שעליו נבדק הקוד (`id[10]`, `name[31]`, `double total`)?",
     "answer": 56,
     "tol": 0,
     "explain": "10 + 31 = 41 בתים, אחריהם ריפוד עד 48 (היסט `total`), ועוד 8 בתים ל-`double`, בסך הכול 56 (במערכת 64 ביט) (ריצה אמיתית: 56 (במערכת 64 ביט)).",
     "promptHtml": "מה <code class=\"tok\" dir=\"ltr\">sizeof(clientData)</code> במחשב שעליו נבדק הקוד (<code class=\"tok\" dir=\"ltr\">id[10]</code>, <code class=\"tok\" dir=\"ltr\">name[31]</code>, <code class=\"tok\" dir=\"ltr\">double total</code>)?",
     "explainHtml": "10 + 31 = 41 בתים, אחריהם ריפוד עד 48 (היסט <code class=\"tok\" dir=\"ltr\">total</code>), ועוד 8 בתים ל-<code class=\"tok\" dir=\"ltr\">double</code>, בסך הכול 56 (במערכת 64 ביט) (ריצה אמיתית: 56 (במערכת 64 ביט))."
    },
    {
     "type": "numeric",
     "prompt": "קובץ הטקסט מהדוגמה (שלוש שורות, והשורה האחרונה מסתיימת בתו שורה חדשה) עבר המרה. מה גודל הקובץ הבינארי בבתים?",
     "answer": 168,
     "tol": 0,
     "explain": "שלוש רשומות של 56 (במערכת 64 ביט) בתים: 3 × 56 = 168 (ריצה אמיתית: 168 בתים, 3 רשומות).",
     "promptHtml": "קובץ הטקסט מהדוגמה (שלוש שורות, והשורה האחרונה מסתיימת בתו שורה חדשה) עבר המרה. מה גודל הקובץ הבינארי בבתים?",
     "explainHtml": "שלוש רשומות של 56 (במערכת 64 ביט) בתים: 3 × 56 = 168 (ריצה אמיתית: 168 בתים, 3 רשומות)."
    },
    {
     "type": "fillblank",
     "prompt": "השלימו את השורה החסרה בפונקציה: הקריאה הראשונה של לקוח.",
     "code": true,
     "lines": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "___",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&client, sizeof(clientData), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ],
     "blankIndex": 7,
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
       "html": "fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);"
      },
      {
       "id": "b",
       "type": "text",
       "value": "fscanf(fin, \"%10s%31s%lf\", client.id, client.name, &client.total);",
       "html": "fscanf(fin, \"%10s%31s%lf\", client.id, client.name, &amp;client.total);"
      },
      {
       "id": "c",
       "type": "text",
       "value": "fscanf(fin, \"%9s%30s%lf\", client.id, client.name, client.total);",
       "html": "fscanf(fin, \"%9s%30s%lf\", client.id, client.name, client.total);"
      },
      {
       "id": "d",
       "type": "text",
       "value": "fscanf(fin, \"%9s%30s%f\", client.id, client.name, &client.total);",
       "html": "fscanf(fin, \"%9s%30s%f\", client.id, client.name, &amp;client.total);"
      }
     ],
     "correctId": "a",
     "explain": "רוחב 9 ל-`id[10]` ו-30 ל-`name[31]` משאיר מקום לתו הסיום, ולקליטת `double` נדרש `%lf` עם כתובת `&client.total`. האפשרות ב' (`%10s%31s`) עובדת על קובץ הדוגמה, אך נכשלת כאשר מזהה בן 9 תווים נצמד ישירות לשם בן 30 תווים.",
     "promptHtml": "השלימו את השורה החסרה בפונקציה: הקריאה הראשונה של לקוח.",
     "explainHtml": "רוחב 9 ל-<code class=\"tok\" dir=\"ltr\">id[10]</code> ו-30 ל-<code class=\"tok\" dir=\"ltr\">name[31]</code> משאיר מקום לתו הסיום, ולקליטת <code class=\"tok\" dir=\"ltr\">double</code> נדרש <code class=\"tok\" dir=\"ltr\">%lf</code> עם כתובת <code class=\"tok\" dir=\"ltr\">&amp;client.total</code>. האפשרות ב' (<code class=\"tok\" dir=\"ltr\">%10s%31s</code>) עובדת על קובץ הדוגמה, אך נכשלת כאשר מזהה בן 9 תווים נצמד ישירות לשם בן 30 תווים.",
     "linesHtml": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "___",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&amp;client, sizeof(clientData), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ]
    },
    {
     "type": "order",
     "prompt": "סדרו את שורות הפונקציה `text_to_binary`.",
     "code": true,
     "lines": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&client, sizeof(clientData), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ],
     "explain": "פתיחת הקבצים ובדיקות, קריאה ראשונה, לולאה שכותבת וקוראת את הבאה, ובסוף סגירת הקבצים.",
     "promptHtml": "סדרו את שורות הפונקציה <code class=\"tok\" dir=\"ltr\">text_to_binary</code>.",
     "explainHtml": "פתיחת הקבצים ובדיקות, קריאה ראשונה, לולאה שכותבת וקוראת את הבאה, ובסוף סגירת הקבצים.",
     "linesHtml": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&amp;client, sizeof(clientData), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ]
    },
    {
     "type": "findbug",
     "prompt": "בגרסה הבאה שורה אחת שונתה, ובקובץ הבינארי יש רק 30 בתים במקום 168. מצאו אותה.",
     "code": true,
     "lines": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&client, sizeof(client.id), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ],
     "bugIndex": 10,
     "explain": "`sizeof(client.id)` הוא 10, ולכן נכתבים 10 בתים לכל לקוח במקום הרשומה כולה (ריצה אמיתית: 30 בתים לשלוש רשומות).",
     "promptHtml": "בגרסה הבאה שורה אחת שונתה, ובקובץ הבינארי יש רק 30 בתים במקום 168. מצאו אותה.",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">sizeof(client.id)</code> הוא 10, ולכן נכתבים 10 בתים לכל לקוח במקום הרשומה כולה (ריצה אמיתית: 30 בתים לשלוש רשומות).",
     "linesHtml": [
      "void text_to_binary(char* text_name, char* binary_name)",
      "{",
      "    clientData client;",
      "    FILE* fin = fopen(text_name, \"r\");",
      "    FILE* fout = fopen(binary_name, \"w\");",
      "    if (!fin)  exit(1);",
      "    if (!fout)  exit(1);",
      "    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);",
      "    while (!feof(fin))",
      "    {",
      "        fwrite(&amp;client, sizeof(client.id), 1, fout);",
      "        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);",
      "    }",
      "    fclose(fin);",
      "    fclose(fout);",
      "}"
     ]
    }
   ],
   "stepsSource": "ai-verified",
   "id": "25B-B-Q3",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "קבצי טקסט",
   "questionHtml": "כתבו פונקציה <code class=\"tok\" dir=\"ltr\">void text_to_binary(char *text_name, char *binary_name)</code> אשר מקבלת מחרוזות <code class=\"tok\" dir=\"ltr\">text_name</code> ו-<code class=\"tok\" dir=\"ltr\">binary_name</code> המהוות שמות של <strong>קובץ טקסט</strong> ושל <strong>קובץ בינארי</strong> בהתאמה.<br><br>תוכן <strong>קובץ הטקסט</strong> מורכב משורות. בכל שורה נמצא מידע עבור לקוח בייצוג הבא:<br>- מס' ת.ז. (9 תווים),<br>- שם לקוח (30 תווים),<br>- סכום סה\"כ קניות (מספר מסוג <code class=\"tok\" dir=\"ltr\">double</code> שתופס 8 עמודות).<br><br><strong>דוגמא:</strong><pre class=\"code-block\" dir=\"ltr\"><code>06842151          Moshe    71.25\n330578795      Benjamin  1755.65\n20051546           Dina   560.10</code></pre>על הפונקציה ליצור <strong>קובץ בינארי</strong> בעל אותו מידע שיש ב<strong>קובץ הטקסט</strong>. כל שורה של <strong>קובץ הטקסט</strong> תהפוך לרשומה ב<strong>קובץ הבינארי</strong>. הפורמט של כל רשומה יהיה מתאים למבנה <code class=\"tok\" dir=\"ltr\">clientData</code> הבא:<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>typedef struct {\n    char id[10];\n    char name[31];\n    double total;\n} clientData;</code></pre>כך ש-<br>- <code class=\"tok\" dir=\"ltr\">id</code> - מס' ת.ז.,<br>- <code class=\"tok\" dir=\"ltr\">name</code> - שם לקוח,<br>- <code class=\"tok\" dir=\"ltr\">total</code> - סכום סה\"כ קניות.<br><br><strong>שימו לב:</strong> פונקציה <code class=\"tok\" dir=\"ltr\">fscanf</code> אשר ניתן להשתמש במהלך סריקת <strong>קובץ הטקסט</strong> מתעלמת מהרווחים השמאליים של המחרוזת הנקלטת ומתחילה את הקלט מהתו הראשון שאחריהם.<br><br>*בחלק זה יש לענות על שאלה אחת מתוך שתיים (שאלה 2 או שאלה 3).*",
   "solutionHtml": "<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>void text_to_binary(char* text_name, char* binary_name)\n{\n    clientData client;\n\n    FILE* fin = fopen(text_name, \"r\");\n    FILE* fout = fopen(binary_name, \"w\");\n    if (!fin)  exit(1);\n    if (!fout)  exit(1);\n\n    fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);\n    while (!feof(fin))\n    {\n        fwrite(&amp;client, sizeof(clientData), 1, fout);\n        fscanf(fin, \"%9s%30s%lf\", client.id, client.name, &amp;client.total);\n    }\n\n    fclose(fin);\n    fclose(fout);\n}</code></pre><br><strong>הערת מתמלל (לא חלק מהפתרון הרשמי):</strong> הפתרון הרשמי עובד על הדוגמה כאשר השורה האחרונה בקובץ מסתיימת בתו שורה חדשה. אם אין תו שורה חדשה אחרי השורה האחרונה, הקריאה האחרונה מגיעה ל-EOF כבר בקליטת <code class=\"tok\" dir=\"ltr\">total</code>, ו-<code class=\"tok\" dir=\"ltr\">feof</code> מחזיר אמת לפני כתיבת הרשומה האחרונה, כך שהיא אובדת. כמו כן הקובץ נפתח ב-<code class=\"tok\" dir=\"ltr\">\"w\"</code> ולא ב-<code class=\"tok\" dir=\"ltr\">\"wb\"</code>.",
   "pointsTotal": 40,
   "pitfallsHtml": [
    "לכתוב ל-<code class=\"tok\" dir=\"ltr\">fwrite</code> גודל שגוי, למשל <code class=\"tok\" dir=\"ltr\">sizeof(client.id)</code> במקום <code class=\"tok\" dir=\"ltr\">sizeof(clientData)</code>, ולקבל רשומות חלקיות בקובץ הבינארי.",
    "לקלוט את השם עם <code class=\"tok\" dir=\"ltr\">%s</code> ללא הגבלת רוחב (או <code class=\"tok\" dir=\"ltr\">%10s</code> ל-<code class=\"tok\" dir=\"ltr\">id</code>), ולכתוב מחוץ לגבולות המערך <code class=\"tok\" dir=\"ltr\">char id[10]</code>.",
    "לבצע בדיקת <code class=\"tok\" dir=\"ltr\">feof</code> לפני הקריאה הראשונה או רק אחרי הקריאה של השורה, ולכתוב רשומה אחת יותר או פחות מדי."
   ]
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
   "rubric": [
    {
     "text": "זיהוי ש-`y` ב-`f4` הוא `static` עם ערך התחלתי 0 ושהשינוי בו נשמר בין הקריאות, בעוד `x` מאותחל מחדש בכל קריאה",
     "points": 3,
     "html": "זיהוי ש-<code class=\"tok\" dir=\"ltr\">y</code> ב-<code class=\"tok\" dir=\"ltr\">f4</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> עם ערך התחלתי 0 ושהשינוי בו נשמר בין הקריאות, בעוד <code class=\"tok\" dir=\"ltr\">x</code> מאותחל מחדש בכל קריאה"
    },
    {
     "text": "שלוש השורות הראשונות נכונות: `1 1`, `1 2`, `1 3`",
     "points": 3,
     "html": "שלוש השורות הראשונות נכונות: <code class=\"tok\" dir=\"ltr\">1 1</code>, <code class=\"tok\" dir=\"ltr\">1 2</code>, <code class=\"tok\" dir=\"ltr\">1 3</code>"
    },
    {
     "text": "זיהוי ש-`f5` משתמשת במשתנה הגלובלי `y` (2, ואחר כך 3) ו-`main` מדפיסה את `y` המקומי (8)",
     "points": 2,
     "html": "זיהוי ש-<code class=\"tok\" dir=\"ltr\">f5</code> משתמשת במשתנה הגלובלי <code class=\"tok\" dir=\"ltr\">y</code> (2, ואחר כך 3) ו-<code class=\"tok\" dir=\"ltr\">main</code> מדפיסה את <code class=\"tok\" dir=\"ltr\">y</code> המקומי (8)"
    },
    {
     "text": "שתי השורות האחרונות נכונות: `2 8` ו-`3 8`",
     "points": 2,
     "html": "שתי השורות האחרונות נכונות: <code class=\"tok\" dir=\"ltr\">2 8</code> ו-<code class=\"tok\" dir=\"ltr\">3 8</code>"
    }
   ],
   "rubricSource": "ai-verified",
   "pitfalls": [
    "לחשוב ש-`y` הסטטי מאותחל מחדש בכל קריאה ל-`f4` ולהדפיס `1 1` בשלוש השורות.",
    "לבלבל בין שלושת ה-`y`: הגלובלי, הסטטי ב-`f4` והמקומי ב-`main`, ולכן להדפיס `5 8` או `2 5` ב-`f5`.",
    "לשכוח שאחרי הלולאה `y` של `main` שווה 8 (הלולאה יוצאת כש-`y <= 7` לא מתקיים) ולכתוב 7."
   ],
   "steps": [
    {
     "type": "choice",
     "prompt": "מה מדפיסה השורה השנייה של הפלט?",
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "`1 2`",
       "html": "<code class=\"tok\" dir=\"ltr\">1 2</code>"
      },
      {
       "id": "b",
       "type": "text",
       "value": "`1 1`",
       "html": "<code class=\"tok\" dir=\"ltr\">1 1</code>"
      },
      {
       "id": "c",
       "type": "text",
       "value": "`2 2`",
       "html": "<code class=\"tok\" dir=\"ltr\">2 2</code>"
      },
      {
       "id": "d",
       "type": "text",
       "value": "`2 1`",
       "html": "<code class=\"tok\" dir=\"ltr\">2 1</code>"
      }
     ],
     "correctId": "a",
     "explain": "בקריאה השנייה `x = 0` ו-`y` הסטטי שווה 1, לכן נקראות `f1` ו-`f2` (ריצה אמיתית: `1 2`).",
     "promptHtml": "מה מדפיסה השורה השנייה של הפלט?",
     "explainHtml": "בקריאה השנייה <code class=\"tok\" dir=\"ltr\">x = 0</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> הסטטי שווה 1, לכן נקראות <code class=\"tok\" dir=\"ltr\">f1</code> ו-<code class=\"tok\" dir=\"ltr\">f2</code> (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">1 2</code>)."
    },
    {
     "type": "choice",
     "prompt": "מה מדפיסה השורה השלישית של הפלט?",
     "options": [
      {
       "id": "a",
       "type": "text",
       "value": "`1 3`",
       "html": "<code class=\"tok\" dir=\"ltr\">1 3</code>"
      },
      {
       "id": "b",
       "type": "text",
       "value": "`1 2`",
       "html": "<code class=\"tok\" dir=\"ltr\">1 2</code>"
      },
      {
       "id": "c",
       "type": "text",
       "value": "`3 3`",
       "html": "<code class=\"tok\" dir=\"ltr\">3 3</code>"
      },
      {
       "id": "d",
       "type": "text",
       "value": "`1 1`",
       "html": "<code class=\"tok\" dir=\"ltr\">1 1</code>"
      }
     ],
     "correctId": "a",
     "explain": "בקריאה השלישית ה-`y` הסטטי שווה 2, לכן נקראות `f1` ו-`f3` (ריצה אמיתית: `1 3`).",
     "promptHtml": "מה מדפיסה השורה השלישית של הפלט?",
     "explainHtml": "בקריאה השלישית ה-<code class=\"tok\" dir=\"ltr\">y</code> הסטטי שווה 2, לכן נקראות <code class=\"tok\" dir=\"ltr\">f1</code> ו-<code class=\"tok\" dir=\"ltr\">f3</code> (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">1 3</code>)."
    },
    {
     "type": "numeric",
     "prompt": "מה הערך של `y` של `main` שמודפס אחרי הקריאה הראשונה ל-`f5`?",
     "answer": 8,
     "tol": 0,
     "explain": "הלולאה מסתיימת כש-`y` הופך ל-8 (ריצה אמיתית: השורה `2 8`). `f5` משנה רק את הגלובלי.",
     "promptHtml": "מה הערך של <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code> שמודפס אחרי הקריאה הראשונה ל-<code class=\"tok\" dir=\"ltr\">f5</code>?",
     "explainHtml": "הלולאה מסתיימת כש-<code class=\"tok\" dir=\"ltr\">y</code> הופך ל-8 (ריצה אמיתית: השורה <code class=\"tok\" dir=\"ltr\">2 8</code>). <code class=\"tok\" dir=\"ltr\">f5</code> משנה רק את הגלובלי."
    },
    {
     "type": "order",
     "prompt": "סדרו את שורות הפלט של התוכנית, מהראשונה לאחרונה.",
     "code": true,
     "lines": [
      "1 1",
      "1 2",
      "1 3",
      "2 8",
      "3 8"
     ],
     "explain": "שלוש קריאות ל-`f4`, ואז שתי קריאות ל-`f5` עם ההדפסה של `y` המקומי (ריצה אמיתית: אותן חמש שורות).",
     "promptHtml": "סדרו את שורות הפלט של התוכנית, מהראשונה לאחרונה.",
     "explainHtml": "שלוש קריאות ל-<code class=\"tok\" dir=\"ltr\">f4</code>, ואז שתי קריאות ל-<code class=\"tok\" dir=\"ltr\">f5</code> עם ההדפסה של <code class=\"tok\" dir=\"ltr\">y</code> המקומי (ריצה אמיתית: אותן חמש שורות).",
     "linesHtml": [
      "1 1",
      "1 2",
      "1 3",
      "2 8",
      "3 8"
     ]
    }
   ],
   "stepsSource": "ai-verified",
   "id": "25B-B-Q4",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "static, const ו-scope",
   "questionHtml": "מהו הפלט של התוכנית הבאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#include &lt;stdio.h&gt;\n\nint y = 2;\n\nvoid f1() {\n    printf(\"1 \");\n}\n\nvoid f2() {\n    printf(\"2 \");\n}\n\nvoid f3() {\n    printf(\"3 \");\n}\n\nvoid f4() {\n    int x = 0;\n    static int y;\n    void (*p[3])() = {f1, f2, f3};\n\n    p[x]();\n    p[y]();\n    x++;\n    y++;\n}\n\nvoid f5() {\n    printf(\"%d \", y);\n    y++;\n}\n\nvoid main() {\n    int y;\n\n    for (y = 5; y &lt;= 7; y++) {\n        f4();\n        printf(\"\\n\");\n    }\n    f5();\n    printf(\"%d\\n\", y);\n    f5();\n    printf(\"%d\\n\", y);\n}</code></pre>יש לנמק את התשובה.",
   "solutionHtml": "<strong>הפלט:</strong><pre class=\"code-block\" dir=\"ltr\"><code>1 1\n1 2\n1 3\n2 8\n3 8</code></pre><strong>נימוק:</strong><br>פונקציה <code class=\"tok\" dir=\"ltr\">f4</code> בלולאה של <code class=\"tok\" dir=\"ltr\">main</code> נקראת שלוש פעמים.<br><code class=\"tok\" dir=\"ltr\">p</code> ב-פונקציה <code class=\"tok\" dir=\"ltr\">f4</code> הוא מערך של שלושה מצביעים לפונקציות אשר מאותחל לפונקציות <code class=\"tok\" dir=\"ltr\">f1</code>, <code class=\"tok\" dir=\"ltr\">f2</code>, <code class=\"tok\" dir=\"ltr\">f3</code>.<br>משתנה <code class=\"tok\" dir=\"ltr\">x</code> מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן ערך התחלתי שלו 0 כברירת מחדל.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיבר <code class=\"tok\" dir=\"ltr\">p[0]</code>, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1. לכן הפלט באיטרציה הראשונה הוא<br><code class=\"tok\" dir=\"ltr\">1 1</code><br>בסוף הפונקציה <code class=\"tok\" dir=\"ltr\">f4</code>, מתקדמים <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code>. בקריאה השנייה ל-<code class=\"tok\" dir=\"ltr\">f4</code>, משתנה <code class=\"tok\" dir=\"ltr\">x</code> שוב מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן השינוי שלו נשמר. אזי ערכי <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> הם 0 ו-1 בהתאמה.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיברי <code class=\"tok\" dir=\"ltr\">p[0]</code> ו-<code class=\"tok\" dir=\"ltr\">p[1]</code> בהתאמה, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1 ולפונקציה <code class=\"tok\" dir=\"ltr\">f2()</code> אשר מדפיסה 2. אזי הפלט באיטרציה השנייה הוא<br><code class=\"tok\" dir=\"ltr\">1 2</code><br>בסוף הפונקציה <code class=\"tok\" dir=\"ltr\">f4</code>, <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> מתקדמים שוב. בקריאה השלישית ל-<code class=\"tok\" dir=\"ltr\">f4</code>, משתנה <code class=\"tok\" dir=\"ltr\">x</code> שוב מאותחל ל-0. משתנה <code class=\"tok\" dir=\"ltr\">y</code> הוא <code class=\"tok\" dir=\"ltr\">static</code> ולכן השינוי שלו שוב נשמר. אזי ערכי <code class=\"tok\" dir=\"ltr\">x</code> ו-<code class=\"tok\" dir=\"ltr\">y</code> הם 0 ו-2 בהתאמה.<br>לכן <code class=\"tok\" dir=\"ltr\">p[x]</code> ו-<code class=\"tok\" dir=\"ltr\">p[y]</code> הם גישות לאיברי <code class=\"tok\" dir=\"ltr\">p[0]</code> ו-<code class=\"tok\" dir=\"ltr\">p[2]</code> בהתאמה, ז\"א קריאות לפונקציה <code class=\"tok\" dir=\"ltr\">f1()</code> אשר מדפיסה 1 ולפונקציה <code class=\"tok\" dir=\"ltr\">f3()</code> אשר מדפיסה 3. אזי הפלט באיטרציה השלישית הוא<br><code class=\"tok\" dir=\"ltr\">1 3</code><br>אחרי יציאה מהלולאה, נקראת פונקצית <code class=\"tok\" dir=\"ltr\">f5</code> אשר מדפיסה ערך משתנה גלובלי <code class=\"tok\" dir=\"ltr\">y</code> המאותחל ל-2 ומקדמת את <code class=\"tok\" dir=\"ltr\">y</code> לאחר מכאן. מיד אחרי יציאה מ-<code class=\"tok\" dir=\"ltr\">f5</code>, מודפס ערך <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code>, אשר אחרי יציאה מהלולאה שווה ל-8. לכן הפלט בשורה הרביעית הוא<br><code class=\"tok\" dir=\"ltr\">2 8</code><br>אחר כך, שוב נקראת פונקצית <code class=\"tok\" dir=\"ltr\">f5</code> אשר מדפיסה ערך משתנה גלובלי <code class=\"tok\" dir=\"ltr\">y</code> אשר אחרי השינוי בקריאה הקודמת שווה ל-3. מיד אחרי יציאה מ-<code class=\"tok\" dir=\"ltr\">f5</code>, מודפס ערך <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code>, אשר עדיין שווה ל-8. לכן הפלט בשורה החמישית הוא<br><code class=\"tok\" dir=\"ltr\">3 8</code>",
   "pointsTotal": 10,
   "pitfallsHtml": [
    "לחשוב ש-<code class=\"tok\" dir=\"ltr\">y</code> הסטטי מאותחל מחדש בכל קריאה ל-<code class=\"tok\" dir=\"ltr\">f4</code> ולהדפיס <code class=\"tok\" dir=\"ltr\">1 1</code> בשלוש השורות.",
    "לבלבל בין שלושת ה-<code class=\"tok\" dir=\"ltr\">y</code>: הגלובלי, הסטטי ב-<code class=\"tok\" dir=\"ltr\">f4</code> והמקומי ב-<code class=\"tok\" dir=\"ltr\">main</code>, ולכן להדפיס <code class=\"tok\" dir=\"ltr\">5 8</code> או <code class=\"tok\" dir=\"ltr\">2 5</code> ב-<code class=\"tok\" dir=\"ltr\">f5</code>.",
    "לשכוח שאחרי הלולאה <code class=\"tok\" dir=\"ltr\">y</code> של <code class=\"tok\" dir=\"ltr\">main</code> שווה 8 (הלולאה יוצאת כש-<code class=\"tok\" dir=\"ltr\">y &lt;= 7</code> לא מתקיים) ולכתוב 7."
   ]
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
   "pitfalls": [
    "לחשוב שמצביע למבנה לא יכול להיות שדה של אותו מבנה: זה המקרה של `struct item *next` ברשימה מקושרת, והוא מתקמפל (ריצה אמיתית). רק שדה מאותו מבנה עצמו (`struct s inner;`) נכשל בקומפילציה עם `field has incomplete type`."
   ],
   "id": "25B-B-Q5a",
   "partKey": "a",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מבנים ואיחודים",
   "questionHtml": "בחרו את התשובה הנכונה <strong>ונמקו</strong> בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).<br>מהי הטענה הלא נכונה?",
   "explanationHtml": "אם המבנה יתבסס על עצמו זו תהיה הגדרה אינסופית. והזיכרון הדרוש לא יהיה ידוע במהלך ההגדרה.",
   "pointsTotal": 0,
   "pitfallsHtml": [
    "לחשוב שמצביע למבנה לא יכול להיות שדה של אותו מבנה: זה המקרה של <code class=\"tok\" dir=\"ltr\">struct item *next</code> ברשימה מקושרת, והוא מתקמפל (ריצה אמיתית). רק שדה מאותו מבנה עצמו (<code class=\"tok\" dir=\"ltr\">struct s inner;</code>) נכשל בקומפילציה עם <code class=\"tok\" dir=\"ltr\">field has incomplete type</code>."
   ]
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
   "pitfalls": [
    "לחשוב ש-`==` על שני שמות של מחרוזות משווה תוכן: הוא משווה כתובות. בריצה אמיתית `str1 == str2` נותן 0 והטקסט `yes` לא מודפס (`strcmp` היא ההשוואה של התוכן)."
   ],
   "id": "25B-B-Q5b",
   "partKey": "b",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מחרוזות",
   "questionHtml": "בחרו את התשובה הנכונה <strong>ונמקו</strong> בכל אחד מהסעיפים הבאים (שאלה 5, 10 נק' בסך הכול).<br>מה עושים בקטע הבא?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>char str1[] = \"hello\", *str2 = \"hello\";\nif (str1 == str2)   printf(\"yes\");</code></pre>",
   "explanationHtml": "גם <code class=\"tok\" dir=\"ltr\">str1</code> וגם <code class=\"tok\" dir=\"ltr\">str2</code> הם כתובות (כי <code class=\"tok\" dir=\"ltr\">str1</code> הוא מערך ו-<code class=\"tok\" dir=\"ltr\">str2</code> הוא מצביע במפורש).",
   "pointsTotal": 0,
   "pitfallsHtml": [
    "לחשוב ש-<code class=\"tok\" dir=\"ltr\">==</code> על שני שמות של מחרוזות משווה תוכן: הוא משווה כתובות. בריצה אמיתית <code class=\"tok\" dir=\"ltr\">str1 == str2</code> נותן 0 והטקסט <code class=\"tok\" dir=\"ltr\">yes</code> לא מודפס (<code class=\"tok\" dir=\"ltr\">strcmp</code> היא ההשוואה של התוכן)."
   ]
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
   "rubric": [
    {
     "text": "חישוב ערכי איברי המערך: `s[0] = '/'` (47), `s[1] = '/' / '/' = 1`, `s[2] = 0`",
     "points": 4,
     "html": "חישוב ערכי איברי המערך: <code class=\"tok\" dir=\"ltr\">s[0] = '/'</code> (47), <code class=\"tok\" dir=\"ltr\">s[1] = '/' / '/' = 1</code>, <code class=\"tok\" dir=\"ltr\">s[2] = 0</code>"
    },
    {
     "text": "זיהוי שהלולאה נעצרת באיבר 0 (`s[2]`), כך שרצים רק על שני האיברים הראשונים",
     "points": 2,
     "html": "זיהוי שהלולאה נעצרת באיבר 0 (<code class=\"tok\" dir=\"ltr\">s[2]</code>), כך שרצים רק על שני האיברים הראשונים"
    },
    {
     "text": "הדפסת `s[i] / '/'` בכל איטרציה: 1 ואחר כך 0",
     "points": 3,
     "html": "הדפסת <code class=\"tok\" dir=\"ltr\">s[i] / '/'</code> בכל איטרציה: 1 ואחר כך 0"
    },
    {
     "text": "הפלט הסופי `10` (רצף ללא רווחים)",
     "points": 1,
     "html": "הפלט הסופי <code class=\"tok\" dir=\"ltr\">10</code> (רצף ללא רווחים)"
    }
   ],
   "rubricSource": "ai-verified",
   "pitfalls": [
    "לקרוא את המערך כארבעה תווי `/` ולהדפיס `1111`: האופרטור `/` בתוך הסוגריים המסולסלים הוא חילוק של קודי ASCII.",
    "לשכוח שחילוק שלם של 1 ב-47 נותן 0, ושהלולאה נעצרת באיבר שערכו 0 ולא ממשיכה לאיבר `s[3]`."
   ],
   "steps": [
    {
     "type": "numeric",
     "prompt": "מה ערך האיבר `s[1]`, כלומר `'/' / '/'`?",
     "answer": 1,
     "tol": 0,
     "explain": "חילוק של קוד ASCII בעצמו נותן 1 (ריצה אמיתית: `s[1] = 1`).",
     "promptHtml": "מה ערך האיבר <code class=\"tok\" dir=\"ltr\">s[1]</code>, כלומר <code class=\"tok\" dir=\"ltr\">'/' / '/'</code>?",
     "explainHtml": "חילוק של קוד ASCII בעצמו נותן 1 (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">s[1] = 1</code>)."
    },
    {
     "type": "numeric",
     "prompt": "מה ערך האיבר `s[2]`, כלומר `'/' / '/' / '/'`?",
     "answer": 0,
     "tol": 0,
     "explain": "`(47/47)/47 = 1/47 = 0` בחילוק שלם (ריצה אמיתית: `s[2] = 0`).",
     "promptHtml": "מה ערך האיבר <code class=\"tok\" dir=\"ltr\">s[2]</code>, כלומר <code class=\"tok\" dir=\"ltr\">'/' / '/' / '/'</code>?",
     "explainHtml": "<code class=\"tok\" dir=\"ltr\">(47/47)/47 = 1/47 = 0</code> בחילוק שלם (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">s[2] = 0</code>)."
    },
    {
     "type": "numeric",
     "prompt": "כמה איטרציות מבצעת הלולאה `for (i=0; s[i]; i++)`?",
     "answer": 2,
     "tol": 0,
     "explain": "הלולאה נעצרת ב-`s[2] = 0` (ריצה אמיתית: הודפסו הערכים של `i = 0` ו-`i = 1` בלבד).",
     "promptHtml": "כמה איטרציות מבצעת הלולאה <code class=\"tok\" dir=\"ltr\">for (i=0; s[i]; i++)</code>?",
     "explainHtml": "הלולאה נעצרת ב-<code class=\"tok\" dir=\"ltr\">s[2] = 0</code> (ריצה אמיתית: הודפסו הערכים של <code class=\"tok\" dir=\"ltr\">i = 0</code> ו-<code class=\"tok\" dir=\"ltr\">i = 1</code> בלבד)."
    },
    {
     "type": "text",
     "prompt": "מה הפלט של התוכנית? (רצף ספרות, ללא רווחים)",
     "accept": [
      "10"
     ],
     "normalize": "none",
     "explain": "האיטרציות מדפיסות `1` ואחר כך `0` (ריצה אמיתית: `10`).",
     "promptHtml": "מה הפלט של התוכנית? (רצף ספרות, ללא רווחים)",
     "explainHtml": "האיטרציות מדפיסות <code class=\"tok\" dir=\"ltr\">1</code> ואחר כך <code class=\"tok\" dir=\"ltr\">0</code> (ריצה אמיתית: <code class=\"tok\" dir=\"ltr\">10</code>)."
    }
   ],
   "stepsSource": "ai-verified",
   "id": "25B-B-Q6",
   "partKey": "",
   "examCode": "25B-B",
   "examLabel": "סדנה מתקדמת בתכנות 61108, סמסטר ב' תשפ\"ה, מועד ב'",
   "year": 2025,
   "source": "exam",
   "topicLabel": "מלכודות C",
   "questionHtml": "מהו הפלט של התוכנית הבאה?<pre class=\"code-block\" dir=\"ltr\" data-lang=\"c\"><code>#include &lt;stdio.h&gt;\n\nvoid main()\n{\n     char s[]={'/','/'/'/','/'/'/'/'/','/'};\n     int i;\n     for (i=0;s[i];i++) printf(\"%d\",s[i]/'/');\n}</code></pre>יש לנמק את התשובה.",
   "solutionHtml": "<strong>הפלט:</strong> <code class=\"tok\" dir=\"ltr\">10</code><br><br><strong>נימוק:</strong><br>איבר מס' 0 ב-<code class=\"tok\" dir=\"ltr\">s</code> שווה ל-<code class=\"tok\" dir=\"ltr\">'/'</code>. איבר מס' 1 ב-<code class=\"tok\" dir=\"ltr\">s</code> שווה ל-<code class=\"tok\" dir=\"ltr\">'/' / '/'</code>, ז\"א, ל-1. איבר מס' 2 הוא <code class=\"tok\" dir=\"ltr\">'/' / '/' / '/'</code> ששווה ל-0 (קוד ASCII של <code class=\"tok\" dir=\"ltr\">'/'</code> גדול מ-1 ולכן <code class=\"tok\" dir=\"ltr\">'/' / 1</code> שווה ל-0).<br>בלולאה סורקים את המערך מאיבר מס' 0. מכיוון שאיבר מס' 2 הוא 0, מטפלים רק באיברי מס' 0 ומס' 1. באיטרציה הראשונה מדפיסים ערך של <code class=\"tok\" dir=\"ltr\">'/' / '/'</code>, ז\"א <strong>1</strong>. באיטרציה השנייה מדפיסים ערך של <code class=\"tok\" dir=\"ltr\">'/' / 1</code>, ז\"א <strong>0</strong>. לכן הפלט יהיה<br><code class=\"tok\" dir=\"ltr\">10</code>",
   "pointsTotal": 10,
   "pitfallsHtml": [
    "לקרוא את המערך כארבעה תווי <code class=\"tok\" dir=\"ltr\">/</code> ולהדפיס <code class=\"tok\" dir=\"ltr\">1111</code>: האופרטור <code class=\"tok\" dir=\"ltr\">/</code> בתוך הסוגריים המסולסלים הוא חילוק של קודי ASCII.",
    "לשכוח שחילוק שלם של 1 ב-47 נותן 0, ושהלולאה נעצרת באיבר שערכו 0 ולא ממשיכה לאיבר <code class=\"tok\" dir=\"ltr\">s[3]</code>."
   ]
  }
 ]
};
