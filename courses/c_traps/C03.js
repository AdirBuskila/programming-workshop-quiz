/* c_traps, level 3 - operator precedence, = versus ==, short-circuit. */
COURSE_LEVEL("c_traps", {
  id: "C03", order: 3, icon: "⚖️", title: "קדימויות והשמה",
  goal: "אחרי השלב הזה אפשר להבחין בין = ל-==, בין פעולות סיביות ללוגיות, ולחשב ביטויים שבהם סדר החישוב מפתיע.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>סדר החישוב נקבע לפי <b>קדימות</b> האופרטורים. מהחזק לחלש, בקצרה:</p>
    <table><thead><tr><th>רמה</th><th>אופרטורים</th></tr></thead>
    <tbody>
    <tr><td>1</td><td><code>!</code> ו-<code>++</code> ו-<code>--</code> (יחידיים)</td></tr>
    <tr><td>2</td><td><code>*</code> <code>/</code> <code>%</code>, אחר כך <code>+</code> <code>-</code></td></tr>
    <tr><td>3</td><td><code>&lt;&lt;</code> <code>&gt;&gt;</code></td></tr>
    <tr><td>4</td><td><code>&lt;</code> <code>&gt;</code> <code>&lt;=</code> <code>&gt;=</code>, אחר כך <code>==</code> <code>!=</code></td></tr>
    <tr><td>5</td><td><code>&amp;</code>, אחר כך <code>^</code>, אחר כך <code>|</code></td></tr>
    <tr><td>6</td><td><code>&amp;&amp;</code>, אחר כך <code>||</code></td></tr>
    <tr><td>7</td><td><code>=</code> (הכי חלש)</td></tr>
    </tbody></table>
    <ul>
      <li><code>=</code> היא השמה והערך שלה הוא הערך שהושם. <code>==</code> היא השוואה.</li>
      <li>השוואה (<code>==</code>) חזקה מ-<code>&amp;</code>, ולכן <code>4 &amp; 3 == 3</code> הוא <code>4 &amp; (3 == 3)</code>, כלומר <code>4 &amp; 1</code>, כלומר 0.</li>
      <li><code>^</code> היא XOR של סיביות ולא חזקה: <code>3 ^ 2</code> הוא 1. ו-<code>1 &lt;&lt; k</code> הוא $2^k$.</li>
      <li>השוואות משורשרות מחושבות משמאל לימין, וכל השוואה נותנת 0 או 1: <code>5 &gt; 3 &gt; 1</code> הוא <code>1 &gt; 1</code>, כלומר 0.</li>
      <li><code>&amp;&amp;</code> ו-<code>||</code> מחשבים משמאל לימין ו<b>עוצרים</b> ברגע שהתוצאה ידועה: הצד הימני של <code>&amp;&amp;</code> לא מחושב אם הצד השמאלי שקרי.</li>
    </ul>
    <div class="lesson-rule">🔑 בספק, שמים סוגריים. ובתנאי <code>if</code> כותבים <code>==</code>.</div>
    <div class="lesson-ex">דוגמה: <code>2 + 3 * 4 % 5</code>. קודם <code>3 * 4 = 12</code>, אחר כך <code>12 % 5 = 2</code> (אותה רמה, משמאל לימין), ולבסוף <code>2 + 2 = 4</code>.</div>
    <div class="lesson-trap">⚠️ <code>if (x = 0)</code> מבצעת השמה, והערך של התנאי הוא 0, כלומר שקר. הקוד מתקמפל, והמשתנה כבר איבד את ערכו.</div>` },
  questions: [
    { id: "C03-Q1", question: "מה מדפיס הקוד?\n```c\nint x = 5;\nif (x = 0)\n    printf(\"A\");\nelse\n    printf(\"B\");\nprintf(\"%d\", x);\n```",
      options: [{ id: "a", value: "`B0`" }, { id: "b", value: "`A0`" }, { id: "c", value: "`B5`" }, { id: "d", value: "`A5`" }],
      correctId: "a",
      explanation: "התנאי הוא השמה: `x` מקבל 0 וערך הביטוי הוא 0, כלומר שקר, ולכן מדפיסים `B`. אחרי ההשמה `x` שווה 0 ולא 5. התשובות `A` מניחות שהתנאי אמת, והתשובות עם 5 מניחות ש-`x` לא השתנה.",
      recap: "if (x = 0) משנה את x והתנאי שקרי." },
    { id: "C03-Q2", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 4 & 3 == 3);\n```",
        answer: 0, tol: 0,
        explain: "`==` חזק מ-`&`, ולכן הביטוי הוא `4 & (3 == 3)`, כלומר `4 & 1`. ב-4 הסיבית הנמוכה כבויה, ולכן התוצאה 0. אילו `&` היה קודם, הייתה התוצאה `(4 & 3) == 3` כלומר 0 == 3, וגם היא 0, אבל מסיבה אחרת." },
      recap: "השוואה חזקה מ-& ו-|." },
    { id: "C03-Q3", question: "מה מדפיס הקוד?\n```c\nprintf(\"%d %d\", 3 ^ 2, 1 << 4);\n```",
      options: [{ id: "a", value: "`1 16`" }, { id: "b", value: "`9 16`" }, { id: "c", value: "`1 4`" }, { id: "d", value: "`9 4`" }],
      correctId: "a",
      explanation: "`^` היא XOR של סיביות: `011 ^ 010 = 001`, כלומר 1, ולא העלאה בחזקה (9). `1 << 4` מזיז את הסיבית ארבע מקומות ונותן $2^4 = 16$, ולא 4.",
      recap: "^ היא XOR, לא חזקה." },
    { id: "C03-Q4", question: "מה מדפיס הקוד?\n```c\nint i = 0, j = 0;\nif (i++ && j++)\n    ;\nprintf(\"%d %d\", i, j);\n```",
      options: [{ id: "a", value: "`1 0`" }, { id: "b", value: "`1 1`" }, { id: "c", value: "`0 0`" }, { id: "d", value: "`0 1`" }],
      correctId: "a",
      explanation: "`i++` נותן את הערך הישן 0 (שקר) ו-`i` נעשה 1. מכיוון שהצד השמאלי של `&&` שקרי, הצד הימני `j++` לא מחושב, ולכן `j` נשאר 0.",
      recap: "&& לא מחשב את הצד הימני אחרי שמאל שקרי." },
    { id: "C03-Q5", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 5 > 3 > 1);\n```",
        answer: 0, tol: 0,
        explain: "מחשבים משמאל לימין: `5 > 3` נותן 1, ואז `1 > 1` שקרי ונותן 0. הביטוי אינו בודק ש-3 גדול מ-1." },
      recap: "השוואות משורשרות נותנות 0 או 1 בכל שלב." },
    { id: "C03-Q6", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", 2 + 3 * 4 % 5);\n```",
        answer: 4, tol: 0,
        explain: "`3 * 4` הוא 12, אחר כך `12 % 5` הוא 2, ולבסוף `2 + 2` הוא 4. הכפל והשארית באותה רמה וחזקים מהחיבור." },
      recap: "כפל, חילוק ושארית לפני חיבור וחיסור." },
  ],
});
