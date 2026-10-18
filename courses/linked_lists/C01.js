/* linked_lists, level 1 - the node, the head, NULL and the first traversal. */
COURSE_LEVEL("linked_lists", {
  id: "C01", order: 1, icon: "🔗", title: "איבר, ראש ומעבר ראשון",
  goal: "אחרי השלב הזה אפשר להגדיר איבר ברשימה מקושרת, להסביר מה זה ראש ו-NULL, ולעבור על כל האיברים בלולאה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p><b>רשימה מקושרת</b> היא סדרה של איברים שמוקצים כל אחד לחוד בזיכרון. כל איבר מחזיק נתון וגם כתובת של האיבר הבא. כך אין צורך בבלוק רציף אחד כמו במערך.</p>
    <p>האיבר מוגדר כמבנה (struct) שמצביע על מבנה מאותו סוג:</p>
    <pre><code>typedef struct item
{
    int data;
    struct item *next;
} Item;</code></pre>
    <div class="lesson-rule">🔑 בתוך ההגדרה השם <code>Item</code> עדיין לא קיים (הוא נוצר רק בסוף ה-typedef), ולכן שדה ההמשך נכתב <code>struct item *next</code>. לכן חשוב לתת למבנה שם, כאן <code>item</code>.</div>
    <h3>הראש וסוף הרשימה</h3>
    <ul>
      <li>הרשימה כולה מיוצגת על ידי <b>מצביע לאיבר הראשון</b>, שנקרא ראש (<code>head</code>).</li>
      <li>האיבר האחרון מצביע ל-<code>NULL</code>. אין אורך שמור בשום מקום, ולכן הסוף מזוהה רק לפי NULL.</li>
      <li>רשימה ריקה היא <code>head == NULL</code>.</li>
      <li>לשדה של איבר שמצביעים עליו ניגשים עם החץ: <code>p-&gt;data</code> ו-<code>p-&gt;next</code>.</li>
    </ul>
    <h3>מעבר על הרשימה</h3>
    <pre><code>Item *p;
for (p = head; p; p = p-&gt;next)
    printf("%d ", p-&gt;data);</code></pre>
    <p>התנאי <code>p</code> הוא קיצור של <code>p != NULL</code>. הלולאה מסתיימת כש-<code>p</code> הגיע ל-NULL, כלומר אחרי האיבר האחרון.</p>
    <div class="lesson-ex">דוגמה: הרשימה <code>3 → 5 → 2</code>. אחרי <code>p = head</code> מתקבל <code>p-&gt;data == 3</code>. אחרי <code>p = p-&gt;next</code> מתקבל 5, אחר כך 2, ואז <code>p == NULL</code> והלולאה נעצרת. הביטוי <code>head-&gt;next-&gt;data</code> הוא 5.</div>
    <div class="lesson-trap">⚠️ רשימה ריקה: אסור לכתוב <code>head-&gt;data</code> כש-<code>head == NULL</code>, זו גישה ל-NULL וקריסה. לולאת <code>for (p = head; p; ...)</code> בטוחה, כי היא בכלל לא נכנסת.</div>` },
  questions: [
    { id: "C01-Q1",
      question: "מגדירים:\n```c\ntypedef struct {\n    int data;\n    Item *next;\n} Item;\n```\nמה קורה בהידור?",
      options: [
        { id: "a", value: "שגיאת הידור: השם `Item` עדיין לא מוכר בתוך ההגדרה" },
        { id: "b", value: "ההידור תקין והרשימה תעבוד כרגיל" },
        { id: "c", value: "ההידור תקין, אבל `next` תמיד יהיה `NULL`" },
        { id: "d", value: "אזהרה בלבד, והמבנה יתפוס זיכרון אינסופי" } ],
      correctId: "a",
      explanation: "השם `Item` נוצר רק אחרי שה-typedef נגמר, ולכן בתוך המבנה הוא לא מוכר והקומפיילר מדווח על שגיאה (נבדק עם clang). הפתרון: לתת למבנה שם ולכתוב `struct item *next`. שאר התשובות מניחות שההידור עובר, וזה לא קורה.",
      recap: "בתוך המבנה כותבים `struct item *next`, לא `Item *next`." },
    { id: "C01-Q2",
      step: { type: "numeric",
        prompt: "הרשימה היא `3 → 5 → 2 → 4` ו-`head` מצביע על האיבר הראשון. מה ידפיס הקוד?\n```c\nint s = 0;\nItem *p;\nfor (p = head; p; p = p->next)\n    s += p->data;\nprintf(\"%d\", s);\n```",
        answer: 14, tol: 0,
        explain: "הלולאה עוברת על כל ארבעת האיברים וסוכמת: $3+5+2+4=14$." },
      recap: "הלולאה `for (p = head; p; p = p->next)` מבקרת בכל איבר פעם אחת." },
    { id: "C01-Q3",
      question: "הרשימה היא `3 → 5 → 2 → 4` ו-`head` מצביע על האיבר הראשון. מה הערך של `head->next->next->data` ?",
      options: [
        { id: "a", value: "`2`" }, { id: "b", value: "`3`" }, { id: "c", value: "`5`" }, { id: "d", value: "`4`" } ],
      correctId: "a",
      explanation: "`head` הוא האיבר 3, `head->next` הוא 5, `head->next->next` הוא 2, ולכן התוצאה 2. התשובה 5 היא `head->next->data`, והתשובה 3 היא `head->data`. התשובה 4 היא האיבר הרביעי, שדורש חץ נוסף.",
      recap: "כל חץ `->next` מתקדם איבר אחד." },
    { id: "C01-Q4",
      step: { type: "numeric",
        prompt: "הרשימה ריקה (`head == NULL`). כמה פעמים ירוץ גוף הלולאה `for (p = head; p; p = p->next)` ?",
        answer: 0, tol: 0,
        explain: "כבר בבדיקה הראשונה `p` הוא NULL, ולכן הלולאה לא נכנסת אף פעם. לכן לולאה כזו בטוחה גם על רשימה ריקה." },
      recap: "לולאת מעבר עם תנאי `p` בטוחה על רשימה ריקה." },
    { id: "C01-Q5",
      question: "מה הערך של `p` מיד אחרי שהלולאה הבאה מסתיימת, על רשימה לא ריקה?\n```c\nfor (p = head; p; p = p->next)\n    ;\n```",
      options: [
        { id: "a", value: "`NULL`" },
        { id: "b", value: "הכתובת של האיבר האחרון" },
        { id: "c", value: "הכתובת של האיבר הראשון" },
        { id: "d", value: "ערך לא מוגדר" } ],
      correctId: "a",
      explanation: "הלולאה נעצרת רק כשהתנאי `p` שקר, כלומר כש-`p == NULL`. לכן `p` לא מצביע על האיבר האחרון אלא אחריו. אם צריך את האחרון, עוצרים מוקדם יותר עם התנאי `p->next`. הערך מוגדר היטב, ולכן לא התשובה האחרונה.",
      recap: "אחרי לולאה עד `p == NULL`, המצביע `p` הוא NULL ולא האיבר האחרון." },
  ],
});
