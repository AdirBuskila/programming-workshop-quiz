/* dyn_2d, level 2 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C02", order: 2, icon: "🏗️", title: "הקצאת מטריצה rows × cols",
  goal: "אחרי השלב הזה אפשר לכתוב פונקציה שמקצה מטריצה דינמית מאופסת, ולחשב כמה בתים היא תופסת.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>בונים מטריצה <code>rows × cols</code> בשני שלבים: קודם <b>מערך המצביעים</b>, ואז <b>כל שורה בנפרד</b> בלולאה.</p>
    <pre><code>int **alloc_matrix(int rows, int cols)
{
    int i;
    int **m = (int **)calloc(rows, sizeof(int *));
    for (i = 0; i &lt; rows; i++)
        m[i] = (int *)calloc(cols, sizeof(int));
    return m;
}</code></pre>
    <ul>
      <li><code>calloc(n, size)</code> מקצה <code>n</code> איברים בגודל <code>size</code> ומאפס אותם. <code>malloc</code> לא מאפס, והתאים מכילים זבל.</li>
      <li>גודל איבר במערך המצביעים: <code>sizeof(int *)</code> (8 בתים). גודל איבר בשורה: <code>sizeof(int)</code> (4 בתים).</li>
      <li>סך הבתים הוא <code>n * size</code> של כל קריאה: למטריצה 3×4 מקבלים $3 \cdot 8 + 3 \cdot 4 \cdot 4 = 72$.</li>
    </ul>
    <div class="lesson-rule">🔑 מערך המצביעים: <code>rows</code> איברים של <code>sizeof(int *)</code>. כל שורה: <code>cols</code> איברים של <code>sizeof(int)</code>.</div>
    <div class="lesson-ex">דוגמה: <code>alloc_matrix(2, 3)</code> קורא ל-<code>calloc(2, 8)</code> ואז פעמיים ל-<code>calloc(3, 4)</code>. כל התאים מתחילים באפס.</div>
    <div class="lesson-trap">⚠️ <code>calloc(rows, sizeof(int))</code> למערך המצביעים מקצה חצי ממה שצריך ב-64 סיביות. ו-<code>malloc</code> במקום <code>calloc</code> משאיר ערכי זבל כשהמטריצה אמורה להתחיל באפסים.</div>` },
  questions: [
    {"id": "C02-Q1", "step": {"type": "order", "prompt": "הפונקציה `alloc_matrix` כבר כתובה. סדרו את הפקודות ב-`main` כך שתוקצה מטריצה, יוכנס 7 לשורה 1 עמודה 2, והערך יודפס.", "code": true, "lines": ["int **m = alloc_matrix(2, 3);", "m[1][2] = 7;", "printf(\"%d\", m[1][2]);", "return 0;"], "explain": "קודם מקצים (בלי מטריצה אין לאן לכתוב), אחר כך כותבים, אחר כך קוראים ומדפיסים, ורק בסוף `return`."}, "recap": "הקצאה, כתיבה, שימוש, ואז `return`."},
    {"id": "C02-Q2", "question": "צריך להקצות את מערך המצביעים של מטריצה עם 3 שורות ו-4 עמודות, ב-64 סיביות, בגודל של בדיוק מצביע אחד לכל שורה. איזו קריאה מבקשת בדיוק את הכמות הזאת?", "options": [{"id": "a", "value": "`calloc(3, sizeof(int *))`"}, {"id": "b", "value": "`calloc(3, sizeof(int))`"}, {"id": "c", "value": "`calloc(4, sizeof(int))`"}, {"id": "d", "value": "`calloc(3, 3 * sizeof(int *))`"}], "correctId": "a", "explanation": "שלוש שורות = שלושה מצביעים = $3 \\cdot 8 = 24$ בתים, וזה `calloc(3, sizeof(int *))`. `calloc(3, sizeof(int))` מבקשת $3 \\cdot 4 = 12$ בתים, `calloc(4, sizeof(int))` מבקשת $4 \\cdot 4 = 16$, ו-`calloc(3, 3 * sizeof(int *))` מבקשת $3 \\cdot 24 = 72$. רק הראשונה מבקשת בדיוק 24 (נבדק עם מקצה מתעד).", "recap": "למערך המצביעים: מספר השורות כפול `sizeof(int *)`."},
    {"id": "C02-Q3", "step": {"type": "fillblank", "prompt": "השלימו את גודל האיבר בהקצאת מערך המצביעים.", "code": true, "lines": ["int **alloc_matrix(int rows, int cols)", "{", "    int i;", "    int **m = (int **)calloc(rows, ___);", "    for (i = 0; i < rows; i++)", "        m[i] = (int *)calloc(cols, sizeof(int));", "    return m;", "}"], "blankIndex": 3, "options": [{"id": "a", "type": "text", "value": "sizeof(int *)"}, {"id": "b", "type": "text", "value": "sizeof(int)"}, {"id": "c", "type": "text", "value": "cols * sizeof(int)"}, {"id": "d", "type": "text", "value": "rows"}], "correctId": "a", "explain": "איבר במערך המצביעים הוא `int *`, ולכן גודלו `sizeof(int *)`. כל אחת מהאפשרויות האחרות מבקשת גודל איבר שאינו 8 בתים."}, "recap": "גודל איבר במערך השורות: `sizeof(int *)`."},
    {"id": "C02-Q4", "step": {"type": "numeric", "prompt": "כמה בתים בסך הכל מקצה הקריאה `alloc_matrix(3, 4)` ב-64 סיביות, כולל מערך המצביעים?", "answer": 72, "tol": 0, "explain": "מערך המצביעים: $3 \\cdot 8 = 24$ בתים. שלוש שורות של 4 מספרים: $3 \\cdot 4 \\cdot 4 = 48$ בתים. סך הכל $24 + 48 = 72$."}, "recap": "בתים = שורות$\\cdot 8$ + שורות$\\cdot$עמודות$\\cdot 4$."},
    {"id": "C02-Q5", "step": {"type": "findbug", "prompt": "הפונקציה אמורה להקצות מטריצה `rows` על `cols`, אבל במטריצה 2 על 3 השורות קצרות מדי. מצאו את השורה השגויה.", "code": true, "lines": ["int **alloc_matrix(int rows, int cols)", "{", "    int i;", "    int **m = (int **)calloc(rows, sizeof(int *));", "    for (i = 0; i < rows; i++)", "        m[i] = (int *)calloc(rows, sizeof(int));", "    return m;", "}"], "bugIndex": 5, "explain": "אורך כל שורה הוא מספר העמודות. `calloc(rows, ...)` מקצה שורות באורך `rows`, ובמטריצה לא ריבועית זה קטן (או גדול) מדי."}, "recap": "אורך שורה = `cols`, מספר השורות = `rows`."},
  ],
});
