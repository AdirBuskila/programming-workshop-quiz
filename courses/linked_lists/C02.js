/* linked_lists, level 2 - creating items and inserting at the head / tail. */
COURSE_LEVEL("linked_lists", {
  id: "C02", order: 2, icon: "➕", title: "הכנסה לראש ולסוף",
  goal: "אחרי השלב הזה אפשר ליצור איבר, להכניס אותו לראש או לסוף הרשימה, ולהסביר למה פונקציית הכנסה מקבלת Item**.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>איבר חדש נוצר עם <code>malloc</code>. נכתוב פונקציית עזר שיוצרת איבר ומחברת אותו לפני איבר אחר:</p>
    <pre><code>Item *new_item(int data, Item *next)
{
    Item *t = (Item *)malloc(sizeof(Item));
    t-&gt;data = data;
    t-&gt;next = next;
    return t;
}</code></pre>
    <h3>הכנסה לראש</h3>
    <pre><code>void insert_head(Item **head, int data)
{
    *head = new_item(data, *head);
}</code></pre>
    <p>האיבר החדש מצביע על הראש הישן, ואז הוא הופך להיות הראש. הראש משתנה, ולכן הפונקציה מקבלת <b>כתובת של המצביע</b> <code>Item **head</code> וקוראים לה כך: <code>insert_head(&amp;h, 7)</code>.</p>
    <div class="lesson-rule">🔑 כשפונקציה צריכה לשנות את הראש, מעבירים אליה <code>&amp;head</code>. אם מעבירים רק <code>Item *head</code>, הפונקציה משנה עותק מקומי והקורא לא מושפע.</div>
    <div class="lesson-ex">דוגמה: מתחילים מרשימה ריקה ומכניסים 1, אחר כך 2, אחר כך 3 לראש. התוצאה היא <code>3 → 2 → 1</code>: כל איבר חדש נכנס <b>לפני</b> הקודמים, ולכן הסדר מתהפך.</div>
    <h3>הכנסה לסוף</h3>
    <p>בלי מצביע לאחרון צריך לעבור על כל הרשימה עד האיבר האחרון (<code>while (p-&gt;next) p = p-&gt;next;</code>), כלומר O(n) לכל הכנסה. מי שמחזיק גם מצביע <code>tail</code> לאחרון מכניס בזמן O(1):</p>
    <pre><code>void append(Item **head, Item **tail, int data)
{
    Item *t = new_item(data, NULL);
    if (*head == NULL)
        *head = *tail = t;
    else
    {
        (*tail)-&gt;next = t;
        *tail = t;
    }
}</code></pre>
    <div class="lesson-trap">⚠️ ברשימה ריקה אין אחרון. לכן הכנסה לסוף חייבת טיפול נפרד במקרה <code>*head == NULL</code>.</div>` },
  questions: [
    { id: "C02-Q1",
      question: "מתחילים עם `Item *h = NULL;` ומריצים:\n```c\ninsert_head(&h, 1);\ninsert_head(&h, 2);\ninsert_head(&h, 3);\n```\nמה מדפיסה מעבר על הרשימה מהראש?",
      options: [
        { id: "a", value: "`3 2 1`" }, { id: "b", value: "`1 2 3`" }, { id: "c", value: "`1`" }, { id: "d", value: "`3`" } ],
      correctId: "a",
      explanation: "כל הכנסה לראש מציבה את האיבר החדש לפני כל הקודמים, ולכן הסדר הפוך לסדר ההכנסה: `3 2 1`. התשובה `1 2 3` נכונה רק להכנסה לסוף.",
      recap: "הכנסה לראש הופכת את סדר ההכנסה." },
    { id: "C02-Q2",
      step: { type: "numeric",
        prompt: "ברשימה יש 8 איברים, ומכניסים איבר חדש לסוף בלי מצביע `tail`, בעזרת:\n```c\nItem *p = head;\nwhile (p->next)\n    p = p->next;\n```\nכמה פעמים מתבצעת ההוראה `p = p->next` ?",
        answer: 7, tol: 0,
        explain: "מתחילים באיבר הראשון ויש להגיע לאיבר השמיני, כלומר 7 התקדמויות. בכלל, ברשימה בת $n$ איברים יש $n-1$ התקדמויות, ולכן ההכנסה לסוף היא O(n)." },
      recap: "הכנסה לסוף בלי tail עולה n-1 צעדים." },
    { id: "C02-Q3",
      question: "הרשימה `h` היא `3 → 5`. מגדירים:\n```c\nvoid add(Item *head, int x)\n{\n    head = new_item(x, head);\n}\n```\nאחרי הקריאה `add(h, 9)` מדפיסים את הרשימה דרך `h`. מה מודפס?",
      options: [
        { id: "a", value: "`3 5`" }, { id: "b", value: "`9 3 5`" }, { id: "c", value: "`3 5 9`" }, { id: "d", value: "`9`" } ],
      correctId: "a",
      explanation: "הפרמטר `head` הוא עותק של `h`. ההשמה משנה את העותק בלבד, ולכן `h` ממשיך להצביע על 3 והרשימה לא השתנתה (ובנוסף האיבר החדש דלף). כדי לשנות את הראש צריך `Item **head` והקריאה `add(&h, 9)`.",
      recap: "שינוי ראש מחייב להעביר `&head`." },
    { id: "C02-Q4",
      step: { type: "findbug", code: true,
        prompt: "הפונקציה אמורה להכניס איבר לראש. בגרסה הבאה שורה אחת שונתה, ואחרי `insert_head(&h, 3)` על הרשימה `2 → 1` מתקבלת הרשימה `3` בלבד. מצאו את השורה.",
        lines: [
          "void insert_head(Item **head, int x)",
          "{",
          "    Item *t = (Item *)malloc(sizeof(Item));",
          "    t->data = x;",
          "    t->next = NULL;",
          "    *head = t;",
          "}" ],
        bugIndex: 4,
        explain: "השורה `t->next = NULL;` מנתקת את האיבר החדש מהרשימה הקיימת, ולכן האיברים הישנים אבדו. צריך `t->next = *head;` לפני שמעדכנים את הראש." },
      recap: "האיבר החדש חייב להצביע על הראש הישן לפני שהראש מתעדכן." },
    { id: "C02-Q5",
      step: { type: "fillblank", code: true,
        prompt: "השלימו את פונקציית ההכנסה לסוף עם מצביע `tail`. אחרי ארבע הכנסות של 1, 2, 3, 4 הרשימה צריכה להיות `1 2 3 4`.",
        lines: [
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
          "}" ],
        blankIndex: 7,
        options: [
          { id: "a", type: "text", value: "(*tail)->next = t;" },
          { id: "b", type: "text", value: "t->next = *tail;" },
          { id: "c", type: "text", value: "(*head)->next = t;" },
          { id: "d", type: "text", value: "*head = t;" } ],
        correctId: "a",
        explain: "האחרון הנוכחי צריך להצביע על האיבר החדש: `(*tail)->next = t`, ורק אחר כך `*tail = t`. התשובה `t->next = *tail` הופכת את הכיוון (תוצאה `1`), התשובה `(*head)->next = t` מחברת תמיד לראש (תוצאה `1 4`), והתשובה `*head = t` מאבדת את כל האיברים הקודמים (תוצאה `4`)." },
      recap: "הכנסה לסוף: `(*tail)->next = t; *tail = t;`." },
  ],
});
