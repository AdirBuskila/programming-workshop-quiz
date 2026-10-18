/* linked_lists, level 5 - building a NEW list: order, dummy node, "no new items" vs "create a list". */
COURSE_LEVEL("linked_lists", {
  id: "C05", order: 5, icon: "🏗️", title: "בניית רשימה חדשה ושמירת סדר",
  goal: "אחרי השלב הזה אפשר לבנות רשימה חדשה מתוך קלט, לשמור על הסדר המקורי, ולהבדיל בין 'חבר מחדש' ל'צור איברים חדשים'.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>הרבה שאלות מבקשות להחזיר <b>רשימה חדשה</b> שנבנית מתוך רשימה או מערך קיים. יש שלוש דרכים לשמור על הסדר המקורי:</p>
    <ul>
      <li>לעבור על הקלט <b>מהסוף להתחלה</b> ולהכניס כל ערך לראש (כך עובדת <code>from_array</code>).</li>
      <li>להחזיק מצביע <code>tail</code> ולהכניס לסוף ב-O(1).</li>
      <li>להשתמש ב<b>איבר דמה</b> (dummy): משתנה מקומי שה-<code>next</code> שלו הוא תחילת הרשימה החדשה. אין מקרה מיוחד ל"האיבר הראשון".</li>
    </ul>
    <pre><code>Item *from_array(const int *a, int n)
{
    Item *head = NULL;
    int i;
    for (i = n - 1; i &gt;= 0; i--)
        insert_head(&amp;head, a[i]);
    return head;
}

/* copies the even values, in order, into a new list */
Item *evens(const Item *src)
{
    Item dummy, *tail = &amp;dummy;
    dummy.next = NULL;
    for (; src; src = src-&gt;next)
        if (src-&gt;data % 2 == 0)
        {
            tail-&gt;next = new_item(src-&gt;data, NULL);
            tail = tail-&gt;next;
        }
    return dummy.next;
}</code></pre>
    <div class="lesson-rule">🔑 שני ניסוחים שונים: "<b>אל תקצה איברים חדשים</b>" אומר לחבר מחדש את ה-<code>next</code> של האיברים הקיימים בלי <code>malloc</code>. "<b>צור רשימה חדשה</b>" אומר שכל איבר ברשימה החדשה הוא איבר חדש (<code>malloc</code>), גם כשהוא מחזיק רק אינדקס או עותק של ערך.</div>
    <div class="lesson-ex">דוגמה: <code>evens</code> על <code>1 → 2 → 3 → 4</code>: האיבר 2 נוסף אחרי הדמה, ואז 4 אחרי 2. הפונקציה מחזירה את <code>dummy.next</code>, כלומר <code>2 → 4</code>, ומבצעת <code>malloc</code> פעמיים.</div>
    <div class="lesson-trap">⚠️ הכנסה לראש תמיד הופכת סדר. אם עוברים על הקלט מההתחלה ומכניסים לראש, הרשימה החדשה יוצאת הפוכה.</div>` },
  questions: [
    { id: "C05-Q1",
      question: "הרשימה היא `1 → 2 → 3 → 4 → 5 → 6`. לולאה עוברת עליה מההתחלה לסוף, ולכל ערך זוגי קוראת ל-`insert_head(&res, p->data)` כש-`res` מתחיל ב-`NULL`. מה הרשימה `res` בסוף?",
      options: [
        { id: "a", value: "`6 4 2`" }, { id: "b", value: "`2 4 6`" }, { id: "c", value: "`2`" }, { id: "d", value: "`6`" } ],
      correctId: "a",
      explanation: "כל הכנסה לראש שמה את הערך לפני הקודמים. הערכים נכנסים בסדר 2, 4, 6 ולכן מתקבל `6 4 2`. כדי לקבל `2 4 6` צריך tail, איבר דמה או מעבר מהסוף.",
      recap: "מעבר קדימה + הכנסה לראש = סדר הפוך." },
    { id: "C05-Q2",
      step: { type: "fillblank", code: true,
        prompt: "השלימו את הפונקציה שמעתיקה את הערכים הזוגיים לרשימה חדשה בסדר המקורי. על `1 → 2 → 3 → 4` היא צריכה להחזיר `2 → 4`.",
        lines: [
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
          "}" ],
        blankIndex: 8,
        options: [
          { id: "a", type: "text", value: "tail = tail->next;" },
          { id: "b", type: "text", value: "tail = &dummy;" },
          { id: "c", type: "text", value: "tail->next = NULL;" },
          { id: "d", type: "text", value: "tail = src;" } ],
        correctId: "a",
        explain: "אחרי שהאיבר החדש חובר, `tail` צריך לעבור אליו: `tail = tail->next`. התשובה `tail = &dummy` תחבר כל איבר חדש לדמה ותשאיר רק את האחרון, `tail->next = NULL` מנתקת מיד את האיבר החדש והרשימה יוצאת ריקה, ו-`tail = src` מעבירה את `tail` לרשימת הקלט ופוגמת בה." },
      recap: "עם dummy ו-tail: מחברים `tail->next` ואז מקדמים `tail = tail->next`." },
    { id: "C05-Q3",
      step: { type: "numeric",
        prompt: "כמה קריאות `malloc` מבצעת `evens` מהשיעור על הרשימה `1 → 2 → 3 → 4 → 5 → 6 → 7` ?",
        answer: 3, tol: 0,
        explain: "הפונקציה מעתיקה את הערכים הזוגיים 2, 4 ו-6, ולכן יוצרת שלושה איברים חדשים. הדמה היא משתנה מקומי ולא מוקצית ב-`malloc`." },
      recap: "רשימה חדשה = איבר חדש לכל ערך שמועתק." },
    { id: "C05-Q4",
      step: { type: "findbug", code: true,
        prompt: "הפונקציה אמורה להחזיר רשימה עם ערכי המערך בסדר המערך. בגרסה הבאה שורה אחת שונתה והרשימה יוצאת הפוכה: על `{1, 2, 3}` מתקבל `3 2 1`. מצאו את השורה.",
        lines: [
          "Item *from_array(const int *a, int n)",
          "{",
          "    Item *head = NULL;",
          "    int i;",
          "    for (i = 0; i < n; i++)",
          "        insert_head(&head, a[i]);",
          "    return head;",
          "}" ],
        bugIndex: 4,
        explain: "מעבר מההתחלה עם הכנסה לראש הופך את הסדר. הלולאה הנכונה רצה מהסוף: `for (i = n - 1; i >= 0; i--)`." },
      recap: "כדי לשמור סדר עם הכנסה לראש עוברים על הקלט מהסוף." },
    { id: "C05-Q5",
      step: { type: "numeric",
        prompt: "בונים רשימה של 5 ערכים, ערך אחרי ערך, בלי `tail`: כל הכנסה לסוף סורקת מהראש בלולאה `while (p->next) p = p->next;` (ההכנסה הראשונה לרשימה ריקה לא סורקת). כמה פעמים מתבצעת ההוראה `p = p->next` בסך הכל, על פני חמש ההכנסות?",
        answer: 6, tol: 0,
        explain: "ההכנסה הראשונה והשנייה סורקות 0 צעדים (ברשימה בת איבר אחד `p->next` כבר NULL), ואחריהן 1, 2 ו-3 צעדים. הסכום הוא $0+0+1+2+3=6$. בכלל זה $O(n^2)$, ו-`tail` מוריד זאת ל-$O(n)$." },
      recap: "הכנסה לסוף בלי tail n פעמים היא $O(n^2)$." },
  ],
});
