/* dyn_2d, level 3 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C03", order: 3, icon: "🧹", title: "שחרור: שורות ואז המערך החיצוני",
  goal: "אחרי השלב הזה אפשר לשחרר מטריצה דינמית נכון, לספור את השחרורים הנדרשים ולזהות דליפות.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>כל <code>calloc</code> צריך <code>free</code> אחד. במטריצה דינמית יש <b>$r + 1$ בלוקים נפרדים</b>, ולכן $r + 1$ שחרורים.</p>
    <pre><code>void free_matrix(int **m, int rows)
{
    int i;
    for (i = 0; i &lt; rows; i++)
        free(m[i]);
    free(m);
}</code></pre>
    <ul>
      <li><b>קודם השורות, אחר כך מערך המצביעים.</b> השורות מוכרות רק דרך <code>m[i]</code>; אחרי <code>free(m)</code> הכתובות האלה אבדו.</li>
      <li><code>free(m)</code> לבד משחרר רק את מערך המצביעים, והשורות דולפות (דליפת זיכרון).</li>
      <li><code>free(NULL)</code> בטוח ולא עושה כלום. אבל <code>free</code> פעמיים על אותה כתובת אמיתית הוא באג.</li>
      <li>מערך סטטי (<code>int A[3][3]</code>) לא הוקצה ב-<code>calloc</code>, ולכן אסור לעשות לו <code>free</code>.</li>
    </ul>
    <div class="lesson-rule">🔑 שחרור מטריצה: לולאה על כל השורות עם <code>free(m[i])</code>, ורק אחריה <code>free(m)</code>.</div>
    <div class="lesson-ex">דוגמה: עבור מטריצה עם 3 שורות מבצעים <code>free(m[0])</code>, <code>free(m[1])</code>, <code>free(m[2])</code> ואז <code>free(m)</code>: ארבעה שחרורים לארבע הקצאות.</div>
    <div class="lesson-trap">⚠️ לולאת שחרור שמתחילה מ-<code>i = 1</code>, או שמסתיימת מוקדם מדי, משאירה שורה בלי שחרור. ולולאה עם <code>i &lt;= rows</code> קוראת את <code>m[rows]</code> שאינו קיים.</div>` },
  questions: [
    {"id": "C03-Q1", "step": {"type": "numeric", "prompt": "כמה קריאות ל-`free` נדרשות כדי לשחרר מטריצה דינמית עם 5 שורות?", "answer": 6, "tol": 0, "explain": "כל שורה משוחררת בנפרד (5 קריאות) ועוד מערך המצביעים עצמו: $5 + 1 = 6$, בדיוק כמספר ההקצאות."}, "recap": "כל `calloc` מקבל `free`: $r + 1$ שחרורים."},
    {"id": "C03-Q2", "step": {"type": "order", "prompt": "סדרו את הפקודות כך שהמטריצה תשוחרר נכון: קודם השורות ואחר כך מערך המצביעים.", "code": true, "lines": ["int i, **m = alloc_matrix(3, 2);", "for (i = 0; i < 3; i++)\n        free(m[i]);", "free(m);"], "explain": "אם משחררים את `m` לפני השורות, כתובות השורות (`m[i]`) אבדו ואי אפשר לשחרר אותן אחרי כן באופן חוקי. הסדר הנכון הוא שורות ואז `m`."}, "recap": "קודם השורות, אחר כך המערך החיצוני."},
    {"id": "C03-Q3", "question": "בסוף התוכנית הבאה, כמה בלוקים שהוקצו נשארו בלי שחרור (דליפה)?\n```c\nint **alloc_matrix(int rows, int cols)\n{\n    int i;\n    int **m = (int **)calloc(rows, sizeof(int *));\n    for (i = 0; i < rows; i++)\n        m[i] = (int *)calloc(cols, sizeof(int));\n    return m;\n}\n\nint main(void)\n{\n    int **m = alloc_matrix(3, 4);\n    free(m);\n    return 0;\n}\n```", "options": [{"id": "a", "value": "`0`"}, {"id": "b", "value": "`1`"}, {"id": "c", "value": "`3`"}, {"id": "d", "value": "`4`"}], "correctId": "c", "explanation": "הוקצו 4 בלוקים: מערך המצביעים ו-3 שורות. שוחרר רק מערך המצביעים, ולכן 3 שורות דלפו. התשובה 4 שוכחת שאחד מהם שוחרר, ו-1 סופרת רק את המערך החיצוני.", "recap": "`free(m)` לבד משחרר רק את מערך המצביעים; השורות דולפות."},
    {"id": "C03-Q4", "step": {"type": "findbug", "prompt": "הפונקציה אמורה לשחרר את כל המטריצה בלי דליפות, אבל שורה אחת נשארת. מצאו את השורה השגויה.", "code": true, "lines": ["void free_matrix(int **m, int rows)", "{", "    int i;", "    for (i = 1; i < rows; i++)", "        free(m[i]);", "    free(m);", "}"], "bugIndex": 3, "explain": "הלולאה מתחילה מ-`i = 1` ולכן שורה 0 לא משוחררת. אינדקסים בלולאה על שורות מתחילים מ-0."}, "recap": "לולאה על שורות: `i` מ-0 עד `rows - 1`."},
    {"id": "C03-Q5", "question": "מה קורה בקוד הבא?\n```c\nint main(void)\n{\n    int *p = NULL;\n    free(p);\n    printf(\"A\");\n    free(p);\n    printf(\"B\");\n    return 0;\n}\n```", "options": [{"id": "a", "value": "`AB`"}, {"id": "b", "value": "`A`"}, {"id": "c", "value": "קריסה לפני כל פלט"}, {"id": "d", "value": "שגיאת הידור"}], "correctId": "a", "explanation": "`free(NULL)` מוגדר היטב ולא עושה כלום, גם פעמיים. לכן מודפס `AB`. לא קורסים ולא מקבלים שגיאת הידור. (`free` כפול על כתובת שאינה NULL הוא כבר באג.)", "recap": "`free(NULL)` בטוח ולא עושה כלום."},
  ],
});
