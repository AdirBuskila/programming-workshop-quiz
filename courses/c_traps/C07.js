/* c_traps, level 7 - default initialization and dynamic allocation. */
COURSE_LEVEL("c_traps", {
  id: "C07", order: 7, icon: "🧠", title: "אתחול והקצאה",
  goal: "אחרי השלב הזה אפשר לדעת מה הערך ההתחלתי של כל סוג משתנה, ולהבדיל בין malloc, calloc ו-realloc.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>מה הערך ההתחלתי של משתנה שלא אותחל במפורש?</p>
    <table><thead><tr><th>סוג</th><th>ערך התחלתי</th></tr></thead>
    <tbody>
    <tr><td>משתנה גלובלי או <code>static</code></td><td>0</td></tr>
    <tr><td>משתנה מקומי רגיל</td><td>לא מוגדר (זבל)</td></tr>
    <tr><td>איברי מערך עם אתחול חלקי (<code>int a[5] = {1, 2}</code>)</td><td>0 לשאר האיברים, גם במערך מקומי</td></tr>
    <tr><td>זיכרון מ-<code>malloc</code></td><td>לא מוגדר</td></tr>
    <tr><td>זיכרון מ-<code>calloc</code></td><td>0</td></tr>
    </tbody></table>
    <ul>
      <li><code>malloc(n)</code> מקצה <code>n</code> בתים בלי לאפס. <code>calloc(k, size)</code> מקצה <code>k * size</code> בתים ומאפסת.</li>
      <li><code>realloc(p, n)</code> משנה את הגודל ושומרת את התוכן הקיים. הכתובת עשויה להשתנות, ולכן משימים את התוצאה ב-<code>p</code>.</li>
      <li><code>free(p)</code> מותרת רק על כתובת שהוחזרה מ-<code>malloc</code>, <code>calloc</code> או <code>realloc</code> (או על <code>NULL</code>). שחרור מערך רגיל הוא התנהגות לא מוגדרת.</li>
      <li>משתנה <code>static</code> בתוך פונקציה מאותחל פעם אחת ושומר את ערכו בין קריאות.</li>
    </ul>
    <div class="lesson-rule">🔑 קריאה של ערך שלא אותחל (מקומי או מ-<code>malloc</code>) נותנת ערך לא מוגדר. אין להסתמך עליו, ושאלה טובה לא תבנה עליו תשובה.</div>
    <div class="lesson-ex">דוגמה: פונקציה עם <code>static int n = 0; n++;</code> שנקראת שלוש פעמים מדפיסה 1, אחר כך 2, אחר כך 3. בלי <code>static</code> היא הייתה מדפיסה 1 שלוש פעמים.</div>
    <div class="lesson-trap">⚠️ <code>malloc</code> לא מאפסת. זיכרון ש"נראה" נקי בהרצה אחת הוא מקרה.</div>` },
  questions: [
    { id: "C07-Q1", question: "מה מדפיס הקוד?\n```c\nint g;\nstatic int s;\nint main(void)\n{\n    int a[5] = {1, 2};\n    printf(\"%d %d %d %d %d\", g, s, a[0], a[2], a[4]);\n    return 0;\n}\n```",
      options: [{ id: "a", value: "`0 0 1 0 0`" }, { id: "b", value: "`0 0 1 2 2`" }, { id: "c", value: "ערכי זבל לא ידועים" }, { id: "d", value: "`0 0 1 1 1`" }],
      correctId: "a",
      explanation: "משתנים גלובליים ו-`static` מאותחלים ל-0. במערך עם אתחול חלקי, כל האיברים שלא נכתבו מקבלים 0 (גם במערך מקומי). לכן `a[2]` ו-`a[4]` הם 0, ו-`a[0]` הוא 1.",
      recap: "גלובלי/static ואתחול חלקי: אפסים." },
    { id: "C07-Q2", question: "מה מדפיס הקוד?\n```c\nint *p = (int *)calloc(3, sizeof(int));\nprintf(\"%d%d%d\", p[0], p[1], p[2]);\n```",
      options: [{ id: "a", value: "`000`" }, { id: "b", value: "`123`" }, { id: "c", value: "ערכי זבל לא ידועים" }, { id: "d", value: "`0`" }],
      correctId: "a",
      explanation: "`calloc` מאפסת את הזיכרון שהקצתה, ולכן שלושת האיברים הם 0. אילו הקצינו עם `malloc`, הערכים היו לא מוגדרים.",
      recap: "calloc מאפסת; malloc לא." },
    { id: "C07-Q3", question: "מה הערך של `p[0]` מיד אחרי ההקצאה?\n```c\nint *p = (int *)malloc(sizeof(int));\n```",
      options: [
        { id: "a", value: "לא מוגדר: `malloc` לא מאתחלת" },
        { id: "b", value: "תמיד 0" },
        { id: "c", value: "תמיד `NULL`" },
        { id: "d", value: "תמיד -1" }],
      correctId: "a",
      explanation: "`malloc` מחזירה זיכרון בלי לאתחל אותו, ולכן הערך לא מוגדר. הערך 0 מובטח רק ב-`calloc`. `NULL` הוא ערך של מצביע ולא של `int`, ו-`malloc` לא מציבה את -1.",
      recap: "זיכרון של malloc אינו מאותחל." },
    { id: "C07-Q4", question: "מה מדפיס הקוד?\n```c\nvoid f(void)\n{\n    static int n = 0;\n    n++;\n    printf(\"%d\", n);\n}\nint main(void)\n{\n    f(); f(); f();\n    return 0;\n}\n```",
      options: [{ id: "a", value: "`123`" }, { id: "b", value: "`111`" }, { id: "c", value: "`012`" }, { id: "d", value: "`000`" }],
      correctId: "a",
      explanation: "המשתנה `static` מאותחל פעם אחת בלבד ושומר את ערכו בין קריאות, ולכן מודפסים 1, 2, 3. התשובה `111` הייתה נכונה אילו `n` היה משתנה מקומי רגיל.",
      recap: "static מקומי זוכר את ערכו." },
    { id: "C07-Q5", question: "מה נכון לגבי הקוד הבא?\n```c\nint a[3];\nfree(a);\n```",
      options: [
        { id: "a", value: "התנהגות לא מוגדרת: `a` לא הוקצה בהקצאה דינמית" },
        { id: "b", value: "`free` משחררת את המערך ללא בעיה" },
        { id: "c", value: "שגיאת הידור" },
        { id: "d", value: "`free` לא עושה כלום כי המערך קטן" }],
      correctId: "a",
      explanation: "`free` מותרת רק על כתובת שהתקבלה מ-`malloc`, `calloc` או `realloc`. מערך רגיל שייך למחסנית, ולכן שחרורו הוא התנהגות לא מוגדרת. הקוד כן מתקמפל.",
      recap: "free על מערך רגיל: התנהגות לא מוגדרת." },
    { id: "C07-Q6", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nint *p = (int *)malloc(3 * sizeof(int));\np[0] = 7;\np = (int *)realloc(p, 6 * sizeof(int));\nprintf(\"%d\", p[0]);\n```",
        answer: 7, tol: 0,
        explain: "`realloc` שומרת את התוכן הקיים (גם אם היא מעבירה אותו לכתובת חדשה), ולכן `p[0]` נשאר 7. רק האיברים החדשים אינם מאותחלים." },
      recap: "realloc שומרת את התוכן הקיים." },
  ],
});
