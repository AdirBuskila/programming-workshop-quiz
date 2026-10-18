/* linked_lists, level 3 - traversal patterns: count, last node, search, and the order of the && test. */
COURSE_LEVEL("linked_lists", {
  id: "C03", order: 3, icon: "🔍", title: "מעבר, ספירה וחיפוש",
  goal: "אחרי השלב הזה אפשר לספור איברים לפי תנאי, להגיע לאיבר האחרון, לחפש ערך, ולכתוב תנאי עצירה בטוח.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>רוב השאלות על רשימות מתחילות בלולאת מעבר. יש שלוש צורות שכדאי להכיר:</p>
    <ul>
      <li><b>לכל איבר</b>: <code>for (p = head; p; p = p-&gt;next)</code>. מתאים לספירה, לסכום ולהדפסה. בסוף הלולאה <code>p == NULL</code>.</li>
      <li><b>עד האיבר האחרון</b>: <code>while (p-&gt;next) p = p-&gt;next;</code>. בסוף <code>p</code> מצביע על האיבר האחרון עצמו. אבל <code>p</code> חייב להיות לא NULL לפני הלולאה, כלומר צריך לטפל ברשימה ריקה בנפרד.</li>
      <li><b>חיפוש</b>: מתקדמים כל עוד לא מצאנו וגם לא נגמרה הרשימה.</li>
    </ul>
    <pre><code>Item *find(Item *head, int x)
{
    Item *p = head;
    while (p &amp;&amp; p-&gt;data != x)
        p = p-&gt;next;
    return p;          /* the found item, or NULL */
}</code></pre>
    <div class="lesson-rule">🔑 בתנאי <code>p &amp;&amp; p-&gt;data != x</code> הסדר חשוב. האופרטור <code>&amp;&amp;</code> מעריך משמאל לימין ועוצר ברגע שהתוצאה ידועה, ולכן <code>p-&gt;data</code> נבדק רק אם <code>p</code> אינו NULL.</div>
    <div class="lesson-ex">דוגמה: חיפוש 9 ברשימה <code>4 → 9 → 1</code>. הלולאה מתקדמת פעם אחת, <code>p</code> מצביע על 9 והתנאי שקר, ולכן מוחזר האיבר 9. חיפוש 7 מתקדם עד NULL ומחזיר NULL.</div>
    <div class="lesson-trap">⚠️ אם כותבים <code>p-&gt;data != x &amp;&amp; p</code>, כשהערך לא ברשימה <code>p</code> מגיע ל-NULL ומיד אחר כך נקרא <code>p-&gt;data</code>. זו התנהגות לא מוגדרת (UB), בדרך כלל קריסה.</div>` },
  questions: [
    { id: "C03-Q1",
      step: { type: "numeric",
        prompt: "הרשימה היא `5 → 1 → 4 → 3 → 8`. כמה איברים עם ערך גדול מ-3 מונה הקוד?\n```c\nint c = 0;\nfor (p = head; p; p = p->next)\n    if (p->data > 3)\n        c++;\n```",
        answer: 3, tol: 0,
        explain: "הערכים 5, 4 ו-8 גדולים מ-3, והערכים 1 ו-3 לא. לכן c שווה 3." },
      recap: "ספירה לפי תנאי: לולאה על כל האיברים עם `if` ו-`c++`." },
    { id: "C03-Q2",
      question: "מריצים `while (p->next) p = p->next;` כש-`p` הוא `head` והרשימה ריקה (`head == NULL`). מה קורה?",
      options: [
        { id: "a", value: "התנהגות לא מוגדרת (UB): קריאת `NULL->next`, בדרך כלל קריסה" },
        { id: "b", value: "הלולאה לא רצה ו-`p` נשאר `NULL`" },
        { id: "c", value: "הלולאה רצה לנצח" },
        { id: "d", value: "הלולאה מסתיימת מיד, כי רשימה ריקה נחשבת לבעלת איבר אחד" } ],
      correctId: "a",
      explanation: "כבר הבדיקה הראשונה קוראת `p->next` כש-`p` הוא NULL, ולכן זו גישה ל-NULL: התנהגות לא מוגדרת (UB). בדרך כלל התוכנית קורסת, אבל התקן לא מבטיח זאת, ולכן גם \"הלולאה לא רצה\" אינה תוצאה מובטחת. בלולאה `while (p)` אין בעיה כזו, אבל כאן הבדיקה נוגעת בשדה של `p`. מי שמשתמש ב-`p->next` חייב לוודא קודם ש-`head != NULL`.",
      recap: "`p->next` בתנאי לולאה דורש `p != NULL` מראש." },
    { id: "C03-Q3",
      step: { type: "findbug", code: true,
        prompt: "הפונקציה אמורה להחזיר את האיבר האחרון ברשימה לא ריקה. בגרסה הבאה שורה אחת שונתה, והפונקציה מחזירה `NULL`. מצאו את השורה.",
        lines: [
          "Item *last(Item *head)",
          "{",
          "    Item *p = head;",
          "    while (p)",
          "        p = p->next;",
          "    return p;",
          "}" ],
        bugIndex: 3,
        explain: "התנאי `while (p)` ממשיך עד ש-`p` הוא NULL, ולכן מוחזר NULL. התנאי הנכון הוא `while (p && p->next)`, שעוצר על האיבר האחרון." },
      recap: "כדי לעצור על האחרון משתמשים בתנאי `p->next`." },
    { id: "C03-Q4",
      step: { type: "fillblank", code: true,
        prompt: "השלימו את תנאי הלולאה בפונקציית החיפוש. היא צריכה להחזיר את האיבר הראשון עם הערך `x`, או `NULL` אם אין כזה.",
        lines: [
          "Item *find(Item *head, int x)",
          "{",
          "    Item *p = head;",
          "    while (___)",
          "        p = p->next;",
          "    return p;",
          "}" ],
        blankIndex: 3,
        options: [
          { id: "a", type: "text", value: "p && p->data != x" },
          { id: "b", type: "text", value: "p && p->data == x" },
          { id: "c", type: "text", value: "p && p->data < x" },
          { id: "d", type: "text", value: "p->next->data != x" } ],
        correctId: "a",
        explain: "ממשיכים להתקדם כל עוד לא נגמרה הרשימה והערך שונה מ-`x`. התנאי `p->data == x` עוצר דווקא על איברים לא נכונים, התנאי `p->data < x` תלוי בסדר ולא בשוויון, והתנאי `p->next->data != x` קורס בסוף הרשימה ומדלג על הראשון." },
      recap: "חיפוש: `while (p && p->data != x)`." },
    { id: "C03-Q5",
      question: "מה הבעיה בתנאי הלולאה `while (p->data != x && p)` בחיפוש הערך `x` ברשימה?",
      options: [
        { id: "a", value: "כש-`x` לא נמצא ברשימה, `p` מגיע ל-`NULL` ואז נקרא `p->data` לפני הבדיקה: UB / התנהגות לא מוגדרת, בדרך כלל קריסה" },
        { id: "b", value: "אין בעיה, כי האופרטור `&&` חילופי" },
        { id: "c", value: "שגיאת הידור, כי אי אפשר לכתוב מצביע בתוך תנאי" },
        { id: "d", value: "הלולאה אף פעם לא מסתיימת כשהערך נמצא" } ],
      correctId: "a",
      explanation: "האופרטור `&&` מוערך משמאל לימין, ולכן `p->data` נקרא לפני שבדקנו אם `p` הוא NULL. כשהערך חסר, זו גישה ל-NULL: התנהגות לא מוגדרת (UB), שבדרך כלל מסתיימת בקריסה. כשהערך נמצא, הלולאה עוצרת לפני כן ואין בעיה (נבדק עם clang), ולכן התשובה האחרונה שגויה. `&&` לא חילופי כשיש תלות בין האגפים, והקוד מתקמפל.",
      recap: "קודם `p`, אחר כך `p->data`." },
  ],
});
