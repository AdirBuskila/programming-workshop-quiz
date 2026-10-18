/* dyn_2d, level 5 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C05", order: 5, icon: "📐", title: "מערך משונן: משולשים",
  goal: "אחרי השלב הזה אפשר להקצות משולש תחתון או עליון עם שורות באורכים שונים ולחשב אורכי שורות ואינדקסים.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>שורות המטריצה הדינמית יכולות להיות <b>באורכים שונים</b>: מערך משונן (jagged). כך חוסכים זיכרון כשצריך רק חלק מהמטריצה, והמבחן אוהב את זה.</p>
    <pre><code>#define N 4
int **low_triangle(int A[][N], int n)
{
    int i, j;
    int **low = (int **)calloc(n, sizeof(int *));
    for (i = 0; i &lt; n; i++)
    {
        low[i] = (int *)calloc(i + 1, sizeof(int));
        for (j = 0; j &lt;= i; j++)
            low[i][j] = A[i][j];
    }
    return low;
}</code></pre>
    <ul>
      <li><b>משולש תחתון</b> (כולל האלכסון): שורה $i$ מכילה את <code>A[i][0..i]</code>, כלומר $i+1$ איברים. סך הכל $\frac{n(n+1)}{2}$.</li>
      <li><b>משולש עליון ממש</b> (בלי האלכסון): שורה $i$ מכילה את <code>A[i][i+1..n-1]</code>, כלומר $n-1-i$ איברים. הערך <code>A[i][j]</code> נשמר באינדקס <code>j - i - 1</code>.</li>
      <li>השורה האחרונה במשולש העליון ריקה (אורך 0), ו-<code>calloc(0, ...)</code> תלוי במימוש. בשאלה אמיתית קראו כמה איברים יש בכל שורה.</li>
    </ul>
    <pre><code>#define N 4
int **strict_upper(int A[][N], int n)
{
    int i, j;
    int **up = (int **)calloc(n, sizeof(int *));
    for (i = 0; i &lt; n; i++)
    {
        up[i] = (int *)calloc(n - 1 - i, sizeof(int));
        for (j = i + 1; j &lt; n; j++)
            up[i][j - i - 1] = A[i][j];
    }
    return up;
}</code></pre>
    <div class="lesson-rule">🔑 לפני שכותבים קוד: רשמו אורך כל שורה ונוסחה של אינדקס מקור מול אינדקס יעד. אחר כך הקצו שורה בגודל הנכון והעתיקו.</div>
    <div class="lesson-ex">דוגמה: עבור $n = 4$ אורכי השורות במשולש העליון הם $3, 2, 1, 0$. האיבר <code>A[1][3]</code> נשמר ב-<code>up[1][1]</code> כי $3 - 1 - 1 = 1$.</div>
    <div class="lesson-trap">⚠️ <code>up[i][j]</code> במקום <code>up[i][j - i - 1]</code> כותב מחוץ לגבולות השורה הקצרה.</div>` },
  questions: [
    {"id": "C05-Q1", "step": {"type": "numeric", "prompt": "כמה איברים נשמרים בסך הכל במשולש התחתון (כולל האלכסון) של מטריצה 6 על 6, כששורה $i$ מקבלת $i+1$ איברים?", "answer": 21, "tol": 0, "explain": "$1 + 2 + 3 + 4 + 5 + 6 = 21$, כלומר $\\frac{6 \\cdot 7}{2}$. זה חצי ממטריצה מלאה (36), בלי מקום מבוזבז."}, "recap": "משולש עם $n$ שורות: $\\frac{n(n+1)}{2}$ איברים."},
    {"id": "C05-Q2", "question": "ב-`strict_upper` למטריצה 4 על 4 (המשולש שמעל האלכסון, בלי האלכסון), מה אורכי השורות `up[0]` עד `up[3]`?", "options": [{"id": "a", "value": "`3 2 1 0`"}, {"id": "b", "value": "`4 3 2 1`"}, {"id": "c", "value": "`3 3 3 3`"}, {"id": "d", "value": "`1 2 3 4`"}], "correctId": "a", "explanation": "שורה $i$ מכילה את `A[i][i+1..n-1]`, כלומר $n-1-i$ איברים: $3, 2, 1, 0$. הרצף `4 3 2 1` כולל את האלכסון, `1 2 3 4` הפוך, ו-`3 3 3 3` שומר מקום מבוזבז.", "recap": "משולש עליון ממש: שורה $i$ באורך $n-1-i$."},
    {"id": "C05-Q3", "step": {"type": "numeric", "prompt": "ב-`strict_upper` נשמר האיבר `A[i][j]` (עבור $j > i$) בתא `up[i][j - i - 1]`. באיזה אינדקס בתוך `up[1]` נשמר `A[1][3]`?", "answer": 1, "tol": 0, "explain": "$j - i - 1 = 3 - 1 - 1 = 1$. השורה `up[1]` מחזיקה את `A[1][2]` באינדקס 0 ואת `A[1][3]` באינדקס 1."}, "recap": "אינדקס בתוך שורת המשולש העליון: $j - i - 1$."},
    {"id": "C05-Q4", "step": {"type": "fillblank", "prompt": "השלימו את אורך השורה `i` במשולש התחתון (עם האלכסון).", "code": true, "lines": ["#define N 4", "int **low_triangle(int A[][N], int n)", "{", "    int i, j;", "    int **low = (int **)calloc(n, sizeof(int *));", "    for (i = 0; i < n; i++)", "    {", "        low[i] = (int *)calloc(___, sizeof(int));", "        for (j = 0; j <= i; j++)", "            low[i][j] = A[i][j];", "    }", "    return low;", "}"], "blankIndex": 7, "options": [{"id": "a", "type": "text", "value": "i + 1"}, {"id": "b", "type": "text", "value": "i"}, {"id": "c", "type": "text", "value": "n"}, {"id": "d", "type": "text", "value": "n - i"}], "correctId": "a", "explain": "שורה $i$ מכילה את `A[i][0..i]`, כלומר $i+1$ איברים. עם `i` הלולאה `j <= i` כותבת איבר אחד מעבר לסוף. עם `n` כל השורות ארוכות (בזבוז), ועם `n - i` המשולש הפוך."}, "recap": "משולש תחתון: שורה $i$ באורך $i+1$."},
    {"id": "C05-Q5", "step": {"type": "findbug", "prompt": "הפונקציה אמורה לשמור בשורה $i$ את `A[i][i+1..n-1]` החל מאינדקס 0, אבל התוצאה שגויה. מצאו את השורה השגויה.", "code": true, "lines": ["#define N 4", "int **strict_upper(int A[][N], int n)", "{", "    int i, j;", "    int **up = (int **)calloc(n, sizeof(int *));", "    for (i = 0; i < n; i++)", "    {", "        up[i] = (int *)calloc(n - 1 - i, sizeof(int));", "        for (j = i + 1; j < n; j++)", "            up[i][j] = A[i][j];", "    }", "    return up;", "}"], "bugIndex": 9, "explain": "השורה `up[i]` קצרה ($n-1-i$ איברים), ואינדקס `j` הולך עד $n-1$. הכתיבה ל-`up[i][j]` חורגת מהגבולות ומשאירה את התא הראשון ריק. האינדקס הנכון הוא `j - i - 1`."}, "recap": "מקור בעמודה $j$ הולך ליעד $j - i - 1$."},
  ],
});
