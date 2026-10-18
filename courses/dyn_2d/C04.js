/* dyn_2d, level 4 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C04", order: 4, icon: "📋", title: "מטריצה סטטית לדינמית",
  goal: "אחרי השלב הזה אפשר להעתיק מטריצה סטטית A[][N] למטריצה דינמית חדשה ולהבחין בין int A[][N] ל-int **.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>במבחן הקלט הוא לעיתים מטריצה <b>סטטית</b> והפלט מבנה <b>דינמי</b>. הפרמטר הסטטי נכתב עם קבוע עמודות:</p>
    <pre><code>#define N 3
int **copy_matrix(int A[][N], int n);</code></pre>
    <ul>
      <li><code>int A[][N]</code> הוא מצביע לשורה של $N$ מספרים. מעבירים לו מערך כמו <code>int S[3][3]</code>.</li>
      <li><code>int **m</code> הוא מערך מצביעים, <b>טיפוס אחר</b>: לא מעבירים אחד במקום השני.</li>
      <li>הפלט הדינמי נבנה בנפרד (<code>calloc</code>), מועתק מהקלט, ומוחזר ב-<code>return</code>. ההעתק עצמאי מהמקור.</li>
      <li>תא שלא כותבים אליו נשאר 0, כי <code>calloc</code> מאפס.</li>
    </ul>
    <pre><code>#define N 3
int **copy_matrix(int A[][N], int n)
{
    int i, j;
    int **B = (int **)calloc(n, sizeof(int *));
    for (i = 0; i &lt; n; i++)
    {
        B[i] = (int *)calloc(n, sizeof(int));
        for (j = 0; j &lt; n; j++)
            B[i][j] = A[i][j];
    }
    return B;
}</code></pre>
    <div class="lesson-rule">🔑 העתקה: מקצים מטריצה חדשה בגודל המתאים, ואז <code>B[i][j] = A[i][j]</code> בלולאה כפולה.</div>
    <div class="lesson-ex">דוגמה: אחרי <code>B = copy_matrix(A, 3)</code>, השינוי <code>B[0][0] = 9</code> לא משנה את <code>A[0][0]</code>.</div>
    <div class="lesson-trap">⚠️ מערך סטטי שהועבר לפונקציה לא משחררים עם <code>free</code>: הוא לא הוקצה ב-<code>calloc</code>.</div>` },
  questions: [
    {"id": "C04-Q1", "question": "הפונקציה `int sum(int A[][N], int n)` מקבלת מטריצה סטטית (`N` קבוע). יש `int S[3][3]` ו-`int **m` (מטריצה דינמית). איזו קריאה תקינה?", "options": [{"id": "a", "value": "`sum(S, 3)`"}, {"id": "b", "value": "`sum(m, 3)`"}, {"id": "c", "value": "`sum(&m, 3)`"}, {"id": "d", "value": "`sum(*m, 3)`"}], "correctId": "a", "explanation": "הפרמטר `int A[][N]` הוא מצביע לשורה של $N$ מספרים, וזה מה שמתקבל משם של מערך דו-ממדי סטטי. `int **m` הוא מערך מצביעים, טיפוס אחר: ההידור נכשל או מתקבלת אזהרה, ואם מריצים, הקריאה מפרשת מצביעים כמספרים. גם `&m` וגם `*m` אינם מצביע-לשורה.", "recap": "`int A[][N]` לא שווה ל-`int **`. סטטי ודינמי אינם ניתנים להחלפה."},
    {"id": "C04-Q2", "question": "מה מדפיס הקוד?\n```c\n#define N 2\nint **copy_matrix(int A[][N], int n)\n{\n    int i, j;\n    int **B = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i < n; i++)\n    {\n        B[i] = (int *)calloc(n, sizeof(int));\n        for (j = 0; j < n; j++)\n            B[i][j] = A[i][j];\n    }\n    return B;\n}\n\nint main(void)\n{\n    int A[2][2] = {{1, 2}, {3, 4}};\n    int **B = copy_matrix(A, 2);\n    B[0][0] = 9;\n    printf(\"%d %d\", A[0][0], B[0][0]);\n    return 0;\n}\n```", "options": [{"id": "a", "value": "`9 9`"}, {"id": "b", "value": "`1 9`"}, {"id": "c", "value": "`1 1`"}, {"id": "d", "value": "`9 1`"}], "correctId": "b", "explanation": "`copy_matrix` בונה מטריצה דינמית חדשה ומעתיקה אליה ערכים. שינוי `B[0][0]` משנה רק את ההעתק, ולכן `A[0][0]` נשאר 1 ו-`B[0][0]` הוא 9. תשובות אחרות מניחות שהמטריצות חולקות זיכרון.", "recap": "ההעתק עצמאי: שינוי בו לא משנה את המקור."},
    {"id": "C04-Q3", "step": {"type": "fillblank", "prompt": "השלימו את השורה שמעתיקה איבר מהמטריצה הסטטית `A` להעתק `B`, כך ש-`B` זהה ל-`A`.", "code": true, "lines": ["int **copy_matrix(int A[][N], int n)", "{", "    int i, j;", "    int **B = (int **)calloc(n, sizeof(int *));", "    for (i = 0; i < n; i++)", "    {", "        B[i] = (int *)calloc(n, sizeof(int));", "        for (j = 0; j < n; j++)", "            B[i][j] = ___;", "    }", "    return B;", "}"], "blankIndex": 8, "options": [{"id": "a", "type": "text", "value": "A[i][j]"}, {"id": "b", "type": "text", "value": "A[j][i]"}, {"id": "c", "type": "text", "value": "A[i][j] * 2"}, {"id": "d", "type": "text", "value": "A[i][j] + i"}], "correctId": "a", "explain": "ההעתק זהה למקור כשכל תא מועתק מאותו מקום: `A[i][j]`. `A[j][i]` משחלף, והאחרות משנות את הערך."}, "recap": "העתקה: `B[i][j] = A[i][j]`."},
    {"id": "C04-Q4", "step": {"type": "numeric", "prompt": "מה מדפיס הקוד הבא?\n```c\nint main(void)\n{\n    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};\n    int **B = (int **)calloc(3, sizeof(int *));\n    int i, j, s = 0;\n    for (i = 0; i < 3; i++)\n    {\n        B[i] = (int *)calloc(3, sizeof(int));\n        for (j = 0; j <= i; j++)\n            B[i][j] = A[i][j];\n    }\n    for (i = 0; i < 3; i++)\n        for (j = 0; j < 3; j++)\n            s += B[i][j];\n    printf(\"%d\", s);\n    return 0;\n}\n```", "answer": 34, "tol": 0, "explain": "רק התאים עם $j \\le i$ מועתקים, והשאר נשארים אפס (`calloc`): $1 + 4 + 5 + 7 + 8 + 9 = 34$. האיברים $2, 3, 6$ מעל האלכסון לא נכנסים."}, "recap": "תא שלא הועתק נשאר 0."},
    {"id": "C04-Q5", "step": {"type": "order", "prompt": "סדרו את גוף `copy_matrix`, שמשתמשת ב-`alloc_matrix` שכבר כתובה: להקצות, להעתיק, להחזיר.", "code": true, "lines": ["int **B = alloc_matrix(n, n);", "for (i = 0; i < n; i++) for (j = 0; j < n; j++) B[i][j] = A[i][j];", "return B;"], "explain": "קודם מקצים את `B` (אחרת אין לאן להעתיק), אחר כך מעתיקים, ורק אז מחזירים. `return` לפני ההעתקה מחזיר מטריצה מאופסת."}, "recap": "הקצאה, העתקה, `return`."},
  ],
});
