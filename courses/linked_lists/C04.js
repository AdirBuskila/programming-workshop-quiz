/* linked_lists, level 4 - deleting items: prev, changing head, saving next before free. */
COURSE_LEVEL("linked_lists", {
  id: "C04", order: 4, icon: "✂️", title: "מחיקת איברים",
  goal: "אחרי השלב הזה אפשר למחוק איבר מהרשימה (כולל הראש) בלי לאבד את המשך הרשימה ובלי לגשת לזיכרון משוחרר.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>כדי להוציא איבר מהרשימה צריך לשנות את המצביע של <b>האיבר שלפניו</b> כך שידלג עליו. לכן במחיקה מחזיקים שני מצביעים: <code>curr</code> לאיבר הנבדק ו-<code>prev</code> לאיבר שלפניו.</p>
    <pre><code>prev-&gt;next = curr-&gt;next;   /* unlink */
free(curr);                /* then release */</code></pre>
    <div class="lesson-rule">🔑 לא קוראים שדה של איבר אחרי <code>free</code> שלו. לכן שומרים <code>next</code> לפני המחיקה, ורק אז משחררים ומתקדמים.</div>
    <h3>מחיקת הראש</h3>
    <p>לראש אין איבר קודם (<code>prev == NULL</code>). המחיקה משנה את הראש עצמו: <code>*head = curr-&gt;next</code>, ולכן הפונקציה מקבלת <code>Item **head</code>.</p>
    <pre><code>void delete_value(Item **head, int val)
{
    Item *curr = *head, *prev = NULL;
    while (curr)
    {
        Item *next = curr-&gt;next;   /* save first */
        if (curr-&gt;data == val)
        {
            if (prev == NULL)
                *head = next;
            else
                prev-&gt;next = next;
            free(curr);
        }
        else
            prev = curr;            /* advance prev only when nothing was deleted */
        curr = next;
    }
}</code></pre>
    <p>שימו לב: אחרי מחיקה <code>prev</code> לא זז, כי האיבר שאחריו הוא עכשיו <code>next</code>.</p>
    <div class="lesson-ex">דוגמה: מוחקים את הערך 2 מ-<code>2 → 2 → 5</code>. האיבר הראשון נמחק (<code>*head</code> עובר לאיבר השני), גם הוא נמחק (<code>*head</code> עובר ל-5), ונשארת הרשימה <code>5</code>.</div>
    <div class="lesson-trap">⚠️ מי שמוחק את הראש בפונקציה שמקבלת <code>Item *head</code> רק משנה עותק. הקורא ממשיך להחזיק כתובת של איבר שהשתחרר.</div>
    <p>צורה שקולה: מצביע למצביע <code>pp</code> שמחזיק את הכתובת של השדה שמצביע על <code>curr</code>. אז אין צורך במקרה מיוחד לראש:</p>
    <pre><code>Item **pp = head;
while (*pp)
{
    if ((*pp)-&gt;data == val)
    {
        Item *dead = *pp;
        *pp = dead-&gt;next;      /* the pointer that pointed to dead now skips it */
        free(dead);
    }
    else
        pp = &amp;(*pp)-&gt;next;
}</code></pre>` },
  questions: [
    { id: "C04-Q1",
      question: "ברשימה `1 → 2 → 3` מצביע `prev` על 1 ומצביע `curr` על 2. רוצים להוציא את 2 מהרשימה כך שהמעבר מ-`head` ידפיס `1 3`, ואחר כך מבצעים `free(curr)`. איזו שורה מתאימה לפני ה-`free`?",
      options: [
        { id: "a", value: "`prev->next = curr->next;`" },
        { id: "b", value: "`prev = curr->next;`" },
        { id: "c", value: "`curr->next = prev;`" },
        { id: "d", value: "`prev->next = curr;`" } ],
      correctId: "a",
      explanation: "האיבר 1 צריך לדלג על 2 ולהצביע על 3, כלומר `prev->next = curr->next`. התשובה `prev = curr->next` משנה רק משתנה מקומי והרשימה נשארת `1 2 3`. התשובה `curr->next = prev` יוצרת מעגל בין 1 ל-2 והמעבר לא נגמר. התשובה `prev->next = curr` לא משנה כלום.",
      recap: "מחיקה: `prev->next = curr->next;` ואז `free(curr);`." },
    { id: "C04-Q2",
      step: { type: "numeric",
        prompt: "מפעילים את `delete_value(&h, 2)` מהשיעור על הרשימה `2 → 2 → 5 → 2 → 7`. כמה קריאות `free` מתבצעות?",
        answer: 3, tol: 0,
        explain: "שלושה איברים בעלי הערך 2 נמחקים, וכל אחד משוחרר בקריאה אחת. הרשימה שנשארת היא `5 → 7`." },
      recap: "כל איבר שנמחק משוחרר פעם אחת." },
    { id: "C04-Q3",
      step: { type: "findbug", code: true,
        prompt: "בגרסה הבאה של `delete_value` שורה אחת שונתה. התוכנית קורסת כשמוחקים את הראש. מצאו את השורה.",
        lines: [
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
          "}" ],
        bugIndex: 8,
        explain: "התנאי `prev != NULL` הפוך. כשמוחקים את הראש `prev` הוא NULL, והקוד נכנס לענף `prev->next = next` וניגש ל-NULL. התנאי הנכון הוא `prev == NULL` לשינוי הראש." },
      recap: "ראש נמחק כש-`prev == NULL`, ואז משנים `*head`." },
    { id: "C04-Q4",
      question: "הרשימה היא `4 → 4 → 1 → 4 → 4 → 2 → 4`. מפעילים `delete_value(&h, 4)` מהשיעור. מה מדפיס מעבר על `h` ?",
      options: [
        { id: "a", value: "`1 2`" }, { id: "b", value: "`4 4 1 2`" }, { id: "c", value: "`1 4 2`" }, { id: "d", value: "`2`" } ],
      correctId: "a",
      explanation: "כל ההופעות של 4 נמחקות, גם הרצופות, כי `prev` לא זז אחרי מחיקה ו-`next` נשמר מראש. נשארים `1` ו-`2`.",
      recap: "מחיקת ערך מחייבת לבדוק גם הופעות רצופות והופעות בראש ובסוף." },
    { id: "C04-Q5",
      step: { type: "fillblank", code: true,
        prompt: "השלימו את הגרסה עם מצביע למצביע. היא צריכה למחוק את כל האיברים בעלי הערך `val`.",
        lines: [
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
          "}" ],
        blankIndex: 8,
        options: [
          { id: "a", type: "text", value: "*pp = dead->next;" },
          { id: "b", type: "text", value: "*pp = (*pp)->next->next;" },
          { id: "c", type: "text", value: "*pp = NULL;" },
          { id: "d", type: "text", value: "*head = dead->next;" } ],
        correctId: "a",
        explain: "המצביע ש-`pp` מצביע עליו (ה-`next` של הקודם, או הראש) צריך לדלג על `dead`: `*pp = dead->next`. התשובה `(*pp)->next->next` מדלגת גם על איבר נוסף ומקריסה בסוף הרשימה, התשובה `*pp = NULL` חותכת את שאר הרשימה, והתשובה `*head = dead->next` תמיד משנה את הראש, גם כשהמחיקה באמצע." },
      recap: "עם `Item **pp`: `*pp = dead->next;` ואין מקרה מיוחד לראש." },
  ],
});
