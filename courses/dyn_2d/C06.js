/* dyn_2d, level 6 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C06", order: 6, icon: "🔁", title: "החזרה by reference: ***out ו-*size",
  goal: "אחרי השלב הזה אפשר להחזיר מערך או מטריצה וגם גודל דרך פרמטרים, עם הכתובות והסוגריים הנכונים.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>פונקציה יכולה להחזיר ב-<code>return</code> רק דבר אחד. כשצריך שניים (מבנה וגם גודל), את השני מעבירים <b>by reference</b>: הקורא שולח <b>כתובת</b> של משתנה, והפונקציה כותבת דרכה.</p>
    <ul>
      <li>כדי להחזיר מערך (<code>int *</code>) דרך פרמטר, הפרמטר הוא <code>int **out</code> והקריאה שולחת <code>&amp;a</code>. כדי להחזיר מטריצה (<code>int **</code>) הפרמטר הוא <code>int ***out</code>.</li>
      <li>כותבים <code>*out = ...</code> כדי לשנות את המשתנה של הקורא. <code>out = ...</code> משנה רק עותק מקומי.</li>
      <li>איבר במערך המוחזר: <code>(*out)[k]</code>. הסוגריים חובה: <code>*out[k]</code> פירושו <code>*(out[k])</code>.</li>
      <li>גודל: <code>int *cnt</code>, והעלאה כ-<code>(*cnt)++</code> (בלי סוגריים, <code>*cnt++</code> מקדם את המצביע עצמו).</li>
    </ul>
    <pre><code>void evens(int *A, int n, int **out, int *cnt)
{
    int i, k;
    *cnt = 0;
    for (i = 0; i &lt; n; i++)
        if (A[i] % 2 == 0)
            (*cnt)++;
    *out = (int *)calloc(*cnt, sizeof(int));
    k = 0;
    for (i = 0; i &lt; n; i++)
        if (A[i] % 2 == 0)
            (*out)[k++] = A[i];
}</code></pre>
    <div class="lesson-rule">🔑 פרמטר פלט מסוג <code>T</code> מוגדר <code>T *p</code>, נכתב <code>*p = ...</code>, ומועבר בקריאה כ-<code>&amp;x</code>.</div>
    <div class="lesson-ex">דוגמה: הקורא כותב <code>int *a; int c; evens(A, 5, &amp;a, &amp;c);</code>. אחרי הקריאה <code>a</code> מצביע על המערך החדש ו-<code>c</code> מחזיק את אורכו.</div>
    <div class="lesson-trap">⚠️ <code>*cnt++</code> במקום <code>(*cnt)++</code>, ו-<code>*out[k]</code> במקום <code>(*out)[k]</code>: שתי טעויות סוגריים נפוצות.</div>` },
  questions: [
    {"id": "C06-Q1", "question": "הפונקציה מחזירה את המשולש התחתון דרך הפרמטר `int ***out` (הקורא מעביר `&T` כש-`T` הוא `int **`). איזו פקודה במקום `___` מוסרת את התוצאה לקורא?\n```c\n#define N 3\nvoid low_triangle(int A[][N], int n, int ***out)\n{\n    int i, j;\n    int **low = (int **)calloc(n, sizeof(int *));\n    for (i = 0; i < n; i++)\n    {\n        low[i] = (int *)calloc(i + 1, sizeof(int));\n        for (j = 0; j <= i; j++)\n            low[i][j] = A[i][j];\n    }\n    ___\n}\n```", "options": [{"id": "a", "value": "`*out = low;`"}, {"id": "b", "value": "`out = low;`"}, {"id": "c", "value": "`**out = low;`"}, {"id": "d", "value": "`out[0] = *low;`"}], "correctId": "a", "explanation": "`out` הוא כתובת של משתנה `int **` אצל הקורא. כדי לשנות את אותו משתנה כותבים דרך הכתובת: `*out = low`. `out = low` משנה רק את העותק המקומי של הפרמטר (וגם הטיפוס לא תואם), ו-`**out = low` ו-`out[0] = *low` מערבבים רמות הפניה: ההידור נכשל.", "recap": "מחזירים דרך פרמטר `X *p` בכתיבה `*p = ...`. כאן `X` הוא `int **`."},
    {"id": "C06-Q2", "question": "מה מדפיס הקוד?\n```c\nvoid fill(int **out, int *cnt)\n{\n    *out = (int *)calloc(3, sizeof(int));\n    (*out)[0] = 4;\n    (*out)[2] = 9;\n    *cnt = 3;\n}\n\nint main(void)\n{\n    int *a;\n    int c;\n    fill(&a, &c);\n    printf(\"%d %d\", a[2], c);\n    return 0;\n}\n```", "options": [{"id": "a", "value": "`9 3`"}, {"id": "b", "value": "`4 3`"}, {"id": "c", "value": "`9 9`"}, {"id": "d", "value": "`3 9`"}], "correctId": "a", "explanation": "`fill` כותבת דרך `out` אל `a`, וגם דרך `cnt` אל `c`. אחרי הקריאה `a` מצביע על מערך `{4, 0, 9}` ו-`c` הוא 3, ולכן `a[2]` הוא 9 והפלט `9 3`. ב-`4 3` נבחר האיבר הראשון, ושתי האפשרויות האחרות מחליפות ערכים.", "recap": "`*out` הוא המצביע של הקורא; `(*out)[k]` הוא האיבר ה-`k` במערך שלו."},
    {"id": "C06-Q3", "step": {"type": "numeric", "prompt": "מה מדפיס הקוד?\n```c\nvoid evens(int *A, int n, int **out, int *cnt)\n{\n    int i, k;\n    *cnt = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;\n    *out = (int *)calloc(*cnt, sizeof(int));\n    k = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];\n}\n\nint main(void)\n{\n    int A[5] = {3, 4, 8, 5, 6};\n    int *a = NULL;\n    int c = 77;\n    evens(A, 5, &a, &c);\n    printf(\"%d\", c);\n    return 0;\n}\n```", "answer": 3, "tol": 0, "explain": "`evens` סופרת את הזוגיים (4, 8, 6) ושומרת 3 ב-`*cnt`. הערך ההתחלתי 77 נדרס בפקודה `*cnt = 0` בתחילת הפונקציה."}, "recap": "ערך שמוחזר בפרמטר נקבע בתוך הפונקציה (`*cnt = ...`)."},
    {"id": "C06-Q4", "step": {"type": "order", "prompt": "סדרו את גוף `evens`: לאפס מונה, לספור זוגיים, להקצות בדיוק לפי המונה, ולמלא.", "code": true, "lines": ["*cnt = 0;", "for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*cnt)++;", "*out = (int *)calloc(*cnt, sizeof(int));", "k = 0;\n    for (i = 0; i < n; i++)\n        if (A[i] % 2 == 0)\n            (*out)[k++] = A[i];"], "explain": "המונה מתאפס קודם, אחר כך נספרים הזוגיים, רק אחר כך מקצים `*cnt` תאים (כך מקצים בדיוק), ובסוף ממלאים. מילוי לפני הקצאה כותב ל-NULL, והקצאה לפני הספירה מקצה לפי הערך הישן."}, "recap": "מאפסים, סופרים, מקצים, ממלאים."},
    {"id": "C06-Q5", "question": "הפונקציה `evens(int *A, int n, int **out, int *cnt)` מחזירה מערך דרך `out` וגודלו דרך `cnt`. הקורא הצהיר `int A[5]; int *a; int c;`. איזו קריאה נכונה?", "options": [{"id": "a", "value": "`evens(A, 5, &a, &c);`"}, {"id": "b", "value": "`evens(A, 5, a, c);`"}, {"id": "c", "value": "`evens(A, 5, &a, c);`"}, {"id": "d", "value": "`evens(A, 5, *a, *c);`"}], "correctId": "a", "explanation": "כדי שהפונקציה תשנה את `a` ואת `c` מעבירים את הכתובות שלהם: `&a` (מסוג `int **`) ו-`&c` (מסוג `int *`). העברת `a` ו-`c` עצמם, או `&a` עם `c`, או `*a` ו-`*c`, לא מתאימה לטיפוסים ולא משנה דבר אצל הקורא.", "recap": "פרמטר פלט: מעבירים `&משתנה`."},
  ],
});
