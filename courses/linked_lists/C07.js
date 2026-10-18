/* linked_lists, level 7 - reversal, comparing two lists, and helper functions over an array of lists. */
COURSE_LEVEL("linked_lists", {
  id: "C07", order: 7, icon: "🧩", title: "היפוך, השוואה ופונקציות עזר",
  goal: "אחרי השלב הזה אפשר להפוך רשימה במקום, להשוות שתי רשימות, ולפרק בעיה על מערך של רשימות לפונקציית עזר ולולאה חיצונית.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <h3>היפוך במקום (בלי איברים חדשים)</h3>
    <p>מחזיקים שלושה מצביעים: <code>prev</code> (כבר הפוך), <code>curr</code> (הנוכחי) ו-<code>next</code> (המשך שעוד לא נגענו בו). בכל צעד הופכים את החץ של <code>curr</code>:</p>
    <pre><code>Item *reverse(Item *head)
{
    Item *prev = NULL, *curr = head;
    while (curr)
    {
        Item *next = curr-&gt;next;   /* 1. save the rest */
        curr-&gt;next = prev;         /* 2. flip the arrow */
        prev = curr;               /* 3. advance prev */
        curr = next;               /* 4. advance curr */
    }
    return prev;                   /* the new head */
}</code></pre>
    <div class="lesson-rule">🔑 הסדר כפוי: קודם שומרים את <code>next</code> (אחרת מאבדים את המשך הרשימה), אחר כך הופכים חץ, ורק אז מקדמים <code>prev</code> ואחריו <code>curr</code>. הראש החדש הוא <code>prev</code>.</div>
    <div class="lesson-ex">דוגמה: ברשימה <code>1 → 2 → 3</code>, אחרי הצעד הראשון האיבר 1 מצביע על NULL ו-<code>prev</code> עליו. המצביע <code>head</code> של הקורא עדיין מצביע על 1, שהוא עכשיו האיבר האחרון, ולכן מעבר דרך <code>head</code> ידפיס רק <code>1</code>.</div>
    <h3>השוואה בין שתי רשימות</h3>
    <p>עוברים בו זמנית על שתיהן. מחזירים 0 כשערכים שונים, ובסיום הלולאה בודקים <b>מי נגמר</b>: הרשימות שוות רק אם שתיהן נגמרו יחד.</p>
    <pre><code>int equal(const Item *a, const Item *b)
{
    while (a &amp;&amp; b)
    {
        if (a-&gt;data != b-&gt;data)
            return 0;
        a = a-&gt;next;
        b = b-&gt;next;
    }
    return a == NULL &amp;&amp; b == NULL;
}</code></pre>
    <h3>מערך של רשימות: פונקציית עזר ולולאה חיצונית</h3>
    <p>כשצריך לבדוק כל רשימה במערך <code>A</code> של רשימות, כותבים פונקציית עזר ששואלת שאלה אחת על שתי רשימות, ולולאה על האינדקסים שקוראת לה. למשל, האם כל ערכי <code>sub</code> מופיעים ב-<code>list</code>:</p>
    <pre><code>int contains_all(const Item *sub, const Item *list)
{
    for (; sub; sub = sub-&gt;next)
    {
        const Item *p = list;
        while (p &amp;&amp; p-&gt;data != sub-&gt;data)
            p = p-&gt;next;
        if (p == NULL)
            return 0;          /* this value was not found */
    }
    return 1;
}</code></pre>
    <div class="lesson-trap">⚠️ בחיפוש מתחילים מחדש מראש <code>list</code> עבור כל ערך של <code>sub</code>, וה-<code>p &amp;&amp;</code> בתנאי הלולאה הפנימית הכרחי: בלעדיו ערך חסר גורם לקריסה.</div>` },
  questions: [
    { id: "C07-Q1",
      step: { type: "order", code: true,
        prompt: "סדרו את גוף הלולאה של היפוך הרשימה.",
        lines: [
          "Item *next = curr->next;",
          "curr->next = prev;",
          "prev = curr;",
          "curr = next;" ],
        explain: "קודם שומרים את `next`. אחר כך הופכים את החץ של `curr`. אז `prev` מתקדם אל `curr`, ולבסוף `curr` מתקדם אל `next`. כל שינוי סדר שובר את הרשימה או לא נגמר (נבדק עם clang על כל 24 הסדרים: רק זה הופך נכון)." },
      recap: "היפוך: שמור next, הפוך חץ, קדם prev, קדם curr." },
    { id: "C07-Q2",
      question: "הרשימה היא `1 → 2 → 3 → 4` ו-`head` מצביע על 1. מריצים את גוף לולאת ההיפוך (השיעור) פעם אחת בלבד, עם `curr = head` ו-`prev = NULL`. מה ידפיס מעבר על הרשימה דרך המשתנה `head` ?",
      options: [
        { id: "a", value: "`1`" }, { id: "b", value: "`4 3 2 1`" }, { id: "c", value: "`2 3 4`" }, { id: "d", value: "`1 2 3 4`" } ],
      correctId: "a",
      explanation: "אחרי הצעד הראשון `1->next` הוא `NULL`. המשתנה `head` עדיין מצביע על 1, ולכן המעבר דרכו מדפיס רק `1`. הרשימה ההפוכה (`4 3 2 1`) מתקבלת רק אחרי כל הצעדים, ורק מהמצביע `prev` שהוחזר.",
      recap: "אחרי היפוך מתחילים מהראש החדש, לא מ-`head` הישן." },
    { id: "C07-Q3",
      step: { type: "fillblank", code: true,
        prompt: "השלימו את ערך ההחזרה של פונקציית ההשוואה בין שתי רשימות. היא צריכה להחזיר 1 רק כששתי הרשימות זהות.",
        lines: [
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
          "}" ],
        blankIndex: 9,
        options: [
          { id: "a", type: "text", value: "return a == NULL && b == NULL;" },
          { id: "b", type: "text", value: "return 1;" },
          { id: "c", type: "text", value: "return a == NULL;" },
          { id: "d", type: "text", value: "return b == NULL;" } ],
        correctId: "a",
        explain: "אחרי הלולאה לפחות אחת מהרשימות נגמרה, והן זהות רק אם שתיהן נגמרו. `return 1` נכשל על `1 2` מול `1 2 3`, `return a == NULL` נכשל על אותו זוג (a נגמרה אבל b לא), ו-`return b == NULL` נכשל על הזוג ההפוך." },
      recap: "השוואת רשימות: בסוף בודקים ששתיהן נגמרו." },
    { id: "C07-Q4",
      step: { type: "findbug", code: true,
        prompt: "בגרסה הבאה של `contains_all` שורה אחת שונתה. התוכנית קורסת כשערך של `sub` לא נמצא ב-`list`. מצאו את השורה.",
        lines: [
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
          "}" ],
        bugIndex: 5,
        explain: "בלי `p &&` הלולאה הפנימית ממשיכה אחרי האיבר האחרון, מגיעה ל-NULL וקוראת `p->data`. התנאי הנכון הוא `while (p && p->data != sub->data)`." },
      recap: "חיפוש בתוך לולאה: תמיד `p &&` לפני `p->data`." },
    { id: "C07-Q5",
      step: { type: "numeric",
        prompt: "המערך `A` מכיל ארבע רשימות: `1,2`, `2,1,3`, `3`, `1,2,3`, והרשימה `L` היא `1,2`. הלולאה החיצונית קוראת ל-`contains_all(L, A[i])` לכל `i`. בכמה רשימות מ-`A` היא מחזירה 1 ?",
        answer: 3, tol: 0,
        explain: "הרשימות `1,2`, `2,1,3` ו-`1,2,3` מכילות את שני הערכים 1 ו-2 (הסדר לא משנה), והרשימה `3` לא. לכן 3." },
      recap: "contains_all לא מתחשבת בסדר, רק בקיום כל הערכים." },
  ],
});
