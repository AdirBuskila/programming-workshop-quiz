/* dyn_2d, level 7 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C07", order: 7, icon: "🧮", title: "מערך של מבנים ו-realloc",
  goal: "אחרי השלב הזה אפשר לבנות מערך של struct {size, ptr}, למלא כל שורה ולהקטין אותה עם realloc.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>לפעמים כל שורה היא <b>מבנה</b> שמחזיק גם מערך דינמי וגם את גודלו, ומחזירים מערך של מבנים:</p>
    <pre><code>typedef struct
{
    int size;
    int *ptr;
} dyn_array;</code></pre>
    <ul>
      <li><code>calloc(n, sizeof(dyn_array))</code> נותן לכל איבר <code>size = 0</code> ו-<code>ptr = NULL</code>, וזה מתאים לשורה ריקה.</li>
      <li>גישה לשדות באיבר של מערך: <code>B[i].size</code> ו-<code>B[i].ptr[j]</code> (נקודה, כי <code>B[i]</code> הוא מבנה ולא מצביע).</li>
      <li>גודל המבנה ב-64 סיביות הוא 16 בתים: <code>int</code> (4) + ריפוד (4) + מצביע (8).</li>
      <li><b>הקטנה עם <code>realloc</code></b>: מקצים מערך זמני בגודל המרבי, ממלאים ומחשבים <code>k</code>, ואז <code>p = realloc(p, k * sizeof(int))</code>. הגודל בבתים.</li>
      <li>אם <code>k == 0</code>, התנהגות <code>realloc(p, 0)</code> תלויה במימוש: עדיף <code>free(p)</code> ולהשאיר <code>NULL</code>.</li>
    </ul>
    <pre><code>dyn_array *div_numbers(const int *A, int sz, int n)
{
    int i, j, k = 0;
    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));
    for (i = 2; i &lt;= n; i++)
    {
        int *tmp = (int *)calloc(sz, sizeof(int));
        for (j = 0, k = 0; j &lt; sz; j++)
            if (A[j] % i == 0)
                tmp[k++] = A[j];
        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));
        B[i - 2].size = k;
    }
    return B;
}</code></pre>
    <div class="lesson-rule">🔑 מערך מבנים: מקצים עם <code>calloc</code>, ממלאים כל איבר בנפרד, ומקטינים כל מערך פנימי עם <code>realloc</code> בגודל <code>k * sizeof(int)</code>.</div>
    <div class="lesson-ex">דוגמה: עבור <code>A = {4, 6, 8, 9, 10, 12}</code> ו-<code>n = 4</code>: <code>B[0]</code> מחזיק את הזוגיים (5 איברים), <code>B[1]</code> את המתחלקים ב-3, ו-<code>B[2]</code> את המתחלקים ב-4.</div>
    <div class="lesson-trap">⚠️ <code>realloc(tmp, k)</code> בלי <code>sizeof</code> מקצה <code>k</code> בתים ולא <code>k</code> מספרים. ו-<code>malloc</code> במקום <code>calloc</code> משאיר <code>size</code> ו-<code>ptr</code> עם זבל בשורות שלא מילאתם.</div>` },
  questions: [
    {"id": "C07-Q1", "question": "מה מדפיס הקוד?\n```c\ntypedef struct\n{\n    int size;\n    int *ptr;\n} dyn_array;\n\nint main(void)\n{\n    dyn_array *B = (dyn_array *)calloc(3, sizeof(dyn_array));\n    printf(\"%d %s\", B[1].size, B[1].ptr ? \"ptr\" : \"NULL\");\n    return 0;\n}\n```", "options": [{"id": "a", "value": "`0 NULL`"}, {"id": "b", "value": "`0 ptr`"}, {"id": "c", "value": "`3 NULL`"}, {"id": "d", "value": "ערכי זבל, התוצאה אינה צפויה"}], "correctId": "a", "explanation": "`calloc` מאפס את כל הבתים, ולכן בכל איבר `size` הוא 0 ו-`ptr` הוא `NULL`. זה בדיוק מה שמתאים לשורות ריקות. זבל היה מתקבל רק מ-`malloc`.", "recap": "מערך מבנים מ-`calloc`: `size = 0` ו-`ptr = NULL` בכל איבר."},
    {"id": "C07-Q2", "step": {"type": "numeric", "prompt": "ב-64 סיביות, מה `sizeof(dyn_array)` של המבנה מהשיעור (`int size; int *ptr;`)?", "answer": 16, "tol": 0, "explain": "`int` תופס 4 בתים, ואחריו 4 בתים ריפוד כדי שהמצביע (8 בתים) יתחיל בכתובת שמתחלקת ב-8. סך הכל $4 + 4 + 8 = 16$."}, "recap": "גודל מבנה כולל ריפוד לפי השדה הרחב ביותר."},
    {"id": "C07-Q3", "step": {"type": "fillblank", "prompt": "השלימו את גודל ההקטנה של `tmp` למספר האיברים שנמצאו בפועל (`k`).", "code": true, "lines": ["dyn_array *div_numbers(const int *A, int sz, int n)", "{", "    int i, j, k = 0;", "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));", "    for (i = 2; i <= n; i++)", "    {", "        int *tmp = (int *)calloc(sz, sizeof(int));", "        for (j = 0, k = 0; j < sz; j++)", "            if (A[j] % i == 0)", "                tmp[k++] = A[j];", "        B[i - 2].ptr = (int *)realloc(tmp, ___);", "        B[i - 2].size = k;", "    }", "    return B;", "}"], "blankIndex": 10, "options": [{"id": "a", "type": "text", "value": "k * sizeof(int)"}, {"id": "b", "type": "text", "value": "k"}, {"id": "c", "type": "text", "value": "sz * sizeof(int)"}, {"id": "d", "type": "text", "value": "sizeof(int)"}], "correctId": "a", "explain": "`realloc` מקבל גודל בבתים, כלומר `k` איברים כפול `sizeof(int)`. `k` לבד הוא `k` בתים בלבד, `sz * sizeof(int)` לא מקטין כלום, ו-`sizeof(int)` משאיר איבר אחד."}, "recap": "`realloc(p, k * sizeof(int))`: הגודל בבתים."},
    {"id": "C07-Q4", "step": {"type": "order", "prompt": "סדרו את גוף הלולאה של `div_numbers` עבור מחלק `i`: להקצות מערך זמני, למלא אותו, ולהקטין ולשמור.", "code": true, "lines": ["int *tmp = (int *)calloc(sz, sizeof(int));", "for (j = 0, k = 0; j < sz; j++)\n            if (A[j] % i == 0)\n                tmp[k++] = A[j];", "B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));\n        B[i - 2].size = k;"], "explain": "קודם מקצים `tmp` בגודל המרבי, אחר כך ממלאים ומחשבים את `k`, ורק אז מקטינים ל-`k` איברים ושומרים את הגודל. הקטנה לפני המילוי משתמשת ב-`k` שעדיין לא חושב."}, "recap": "מקצים מקסימום, ממלאים, מקטינים ושומרים."},
    {"id": "C07-Q5", "step": {"type": "findbug", "prompt": "בשורה $i$ של התוצאה אמורים להיכנס המספרים מ-`A` שמתחלקים ב-`i`. התוצאה שגויה. מצאו את השורה השגויה.", "code": true, "lines": ["dyn_array *div_numbers(const int *A, int sz, int n)", "{", "    int i, j, k = 0;", "    dyn_array *B = (dyn_array *)calloc(n - 1, sizeof(dyn_array));", "    for (i = 2; i <= n; i++)", "    {", "        int *tmp = (int *)calloc(sz, sizeof(int));", "        for (j = 0, k = 0; j < sz; j++)", "            if (i % A[j] == 0)", "                tmp[k++] = A[j];", "        B[i - 2].ptr = (int *)realloc(tmp, k * sizeof(int));", "        B[i - 2].size = k;", "    }", "    return B;", "}"], "bugIndex": 8, "explain": "התנאי הוא ש-`A[j]` מתחלק ב-`i`: `A[j] % i == 0`. הגרסה `i % A[j] == 0` שואלת את ההפך (האם `i` מתחלק ב-`A[j]`), ולכן אף מספר גדול מ-`i` לא נכנס."}, "recap": "`x % d == 0`: `x` מתחלק ב-`d`."},
  ],
});
