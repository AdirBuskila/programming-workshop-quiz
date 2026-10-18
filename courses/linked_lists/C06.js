/* linked_lists, level 6 - circular lists: do-while, no NULL, single item points to itself. */
COURSE_LEVEL("linked_lists", {
  id: "C06", order: 6, icon: "🔄", title: "רשימות מעגליות",
  goal: "אחרי השלב הזה אפשר לעבור על רשימה מעגלית בלי לתקוע את התוכנית, ולמצוא בה את האיבר המקסימלי כשהיא ממוינת.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>ברשימה <b>מעגלית</b> האיבר האחרון מצביע על הראשון, ולכן <b>אין NULL</b> בשום מקום. רשימה בת איבר אחד מצביעה על עצמה: <code>p-&gt;next == p</code>.</p>
    <div class="lesson-rule">🔑 לולאה שמחכה ל-NULL לא תיגמר על רשימה מעגלית. עוצרים כשחוזרים לנקודת ההתחלה.</div>
    <p>כדי לעבור על כל האיברים פעם אחת מתחילים ב-<code>start</code> ומשתמשים ב-<code>do ... while</code>. הגוף רץ לפחות פעם אחת, ורק אחר כך נבדק אם חזרנו להתחלה:</p>
    <pre><code>Item *p = start;
do
{
    /* work on p */
    p = p-&gt;next;
} while (p != start);</code></pre>
    <div class="lesson-trap">⚠️ <code>p = start; while (p != start) { ... }</code> לא תרוץ אפילו פעם אחת, כי התנאי כבר שקר בהתחלה.</div>
    <div class="lesson-ex">דוגמה: ברשימה המעגלית <code>2 → 4 → 7 → 9 → (חוזר ל-2)</code> עם <code>start</code> על 7 סדר הביקור הוא 7, 9, 2, 4. אחרי 4 הצעד הבא מחזיר ל-7 והלולאה נעצרת.</div>
    <h3>רשימה מעגלית ממוינת</h3>
    <p>אם הערכים עולים ממש לאורך הרשימה, ורק האיבר האחרון (המקסימלי) מצביע חזרה על הקטן ביותר, אז האיבר המקסימלי הוא היחיד ש-<code>p-&gt;data</code> שלו <b>לא קטן</b> מזה של <code>p-&gt;next</code>. לכן הלולאה</p>
    <pre><code>while (p-&gt;data &lt; p-&gt;next-&gt;data)
    p = p-&gt;next;</code></pre>
    <p>מתקדמת עד האיבר המקסימלי מכל נקודת התחלה. ברשימה בת איבר אחד התנאי שקר מיד, כי ערך אינו קטן מעצמו.</p>` },
  questions: [
    { id: "C06-Q1",
      question: "מה קורה כשמריצים `while (p->next) p = p->next;` על רשימה מעגלית לא ריקה?",
      options: [
        { id: "a", value: "הלולאה אינסופית, כי אין איבר ש-`next` שלו `NULL`" },
        { id: "b", value: "הלולאה עוצרת באיבר האחרון" },
        { id: "c", value: "הלולאה עוצרת כשהיא חוזרת להתחלה" },
        { id: "d", value: "קריסה מיידית" } ],
      correctId: "a",
      explanation: "ברשימה מעגלית כל `next` מצביע על איבר אמיתי, ולכן התנאי תמיד אמת והלולאה לא נגמרת (נבדק עם clang). הלולאה לא יודעת מתי חזרנו להתחלה, אלא אם משווים ל-`start`. אין כאן גישה ל-NULL, ולכן אין קריסה.",
      recap: "ברשימה מעגלית עוצרים בחזרה ל-`start`, לא ב-NULL." },
    { id: "C06-Q2",
      step: { type: "numeric",
        prompt: "הרשימה המעגלית היא `2 → 4 → 7 → 9` (אחרי 9 חוזרים ל-2), ו-`start` מצביע על 7. מה ידפיס הקוד?\n```c\nint s = 0;\nItem *p = start;\ndo\n{\n    s += p->data;\n    p = p->next;\n} while (p != start);\nprintf(\"%d\", s);\n```",
        answer: 22, tol: 0,
        explain: "הלולאה מבקרת בכל ארבעת האיברים פעם אחת בסדר 7, 9, 2, 4: $7+9+2+4=22$, ללא תלות בנקודת ההתחלה." },
      recap: "do-while על מעגלית מבקר בכל איבר פעם אחת." },
    { id: "C06-Q3",
      question: "ברשימה מעגלית ממוינת יש איבר אחד, `L`, ו-`L->next == L`. כמה פעמים רץ גוף הלולאה `while (L->data < L->next->data) L = L->next;` ?",
      options: [
        { id: "a", value: "אף פעם" }, { id: "b", value: "פעם אחת" }, { id: "c", value: "לנצח" }, { id: "d", value: "קריסה" } ],
      correctId: "a",
      explanation: "`L->next` הוא `L` עצמו, ולכן התנאי הוא `L->data < L->data`, שתמיד שקר. הלולאה לא נכנסת וגם אין גישה לא חוקית, כי `L->next` הוא כתובת של איבר אמיתי (נבדק עם clang).",
      recap: "איבר יחיד מצביע על עצמו, והתנאי `<` ממש מסתיים מיד." },
    { id: "C06-Q4",
      step: { type: "numeric",
        prompt: "הרשימה המעגלית הממוינת היא `3 → 5 → 8 → 12` (אחרי 12 חוזרים ל-3), ו-`L` מצביע על 5. כמה פעמים ירוץ גוף הלולאה `while (L->data < L->next->data) L = L->next;` ?",
        answer: 2, tol: 0,
        explain: "מ-5 עוברים ל-8 (כי $5<8$), מ-8 ל-12 (כי $8<12$), וב-12 התנאי $12<3$ שקר. הגוף רץ פעמיים ו-`L` מסיים על האיבר המקסימלי 12." },
      recap: "הלולאה עוצרת באיבר המקסימלי, כי אחריו בא הקטן ביותר." },
    { id: "C06-Q5",
      step: { type: "findbug", code: true,
        prompt: "הפונקציה אמורה לספור את האיברים ברשימה מעגלית. בגרסה הבאה שורה אחת שונתה, ועל רשימה בת 4 איברים מתקבל 3. מצאו את השורה.",
        lines: [
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
          "}" ],
        bugIndex: 8,
        explain: "התנאי `p->next != start` עוצר כשהאיבר הבא הוא `start`, כלומר כש-`p` הוא האחרון, לפני שספרנו אותו. התנאי הנכון הוא `p != start` אחרי ההתקדמות." },
      recap: "תנאי העצירה במעגלית: `while (p != start)` אחרי `p = p->next`." },
  ],
});
