/* c_traps, level 8 - struct copy, union, scope, preprocessor. */
COURSE_LEVEL("c_traps", {
  id: "C08", order: 8, icon: "🧩", title: "מבנים, איחוד וטווח",
  goal: "אחרי השלב הזה אפשר לחשב מה קורה בהעתקת מבנה, בכתיבה לאיחוד, ובהסתרת משתנה גלובלי, ולהכיר מהן הנחיות קדם-מעבד.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p><b>העתקת מבנה</b> (<code>s2 = s1</code>) מעתיקה את כל השדות ערך אחר ערך. שדה מערך מועתק במלואו (העתק נפרד), ושדה מצביע מועתק ככתובת בלבד: שני המבנים מצביעים לאותו מקום.</p>
    <pre><code>struct S { int a; int *p; };</code></pre>
    <p><b>איחוד</b> (<code>union</code>) מחזיק את כל השדות באותו זיכרון. הכתיבה האחרונה קובעת את הערך שנקרא. באיחוד ששני שדותיו מאותו טיפוס, הכתיבה לשדה אחד משנה את השני.</p>
    <p><b>טווח (scope)</b>: פרמטר או משתנה מקומי באותו שם כמו משתנה גלובלי <b>מסתיר</b> אותו בתוך הפונקציה או הבלוק. הפרמטר הוא עותק (העברה לפי ערך), ושינויו לא משפיע על הקורא.</p>
    <p><b>הנחיות קדם-מעבד</b> הן שורות שמתחילות ב-<code>#</code> ומעובדות לפני ההידור: <code>#include</code>, <code>#define</code>, <code>#undef</code>, <code>#ifdef</code>, <code>#ifndef</code>, <code>#if</code>, <code>#endif</code>. המילה <code>typedef</code> אינה הנחיית קדם-מעבד: היא הצהרה רגילה של השפה.</p>
    <div class="lesson-rule">🔑 העתקת מבנה היא שטוחה: מצביעים מועתקים כתובת, מערכים בתוך המבנה מועתקים תוכן.</div>
    <div class="lesson-ex">דוגמה: ב-<code>struct T { int v[2]; }</code>, אחרי <code>t2 = t1; t2.v[0] = 9;</code> המערך של <code>t1</code> לא השתנה, כי <code>t2.v</code> הוא עותק.</div>
    <div class="lesson-trap">⚠️ שינוי של <code>*s2.p</code> משנה את הערך ש-<code>s1.p</code> מצביע אליו, כי שני המצביעים מכילים אותה כתובת.</div>` },
  questions: [
    { id: "C08-Q1", question: "מה מדפיס הקוד?\n```c\nstruct S { int a; int *p; };\nint x = 1;\nstruct S s1 = {5, &x};\nstruct S s2 = s1;\ns2.a = 9;\n*s2.p = 7;\nprintf(\"%d %d %d\", s1.a, *s1.p, x);\n```",
      options: [{ id: "a", value: "`5 7 7`" }, { id: "b", value: "`9 7 7`" }, { id: "c", value: "`5 1 1`" }, { id: "d", value: "`9 1 1`" }],
      correctId: "a",
      explanation: "`s2.a` הוא עותק, ולכן `s1.a` נשאר 5. `s2.p` ו-`s1.p` מכילים אותה כתובת (של `x`), ולכן הכתיבה `*s2.p = 7` משנה את `x` ונראית דרך שניהם.",
      recap: "העתקת מבנה: שדה רגיל עותק, מצביע משותף." },
    { id: "C08-Q2", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nstruct T { int v[2]; };\nstruct T t1 = {{1, 2}};\nstruct T t2 = t1;\nt2.v[0] = 9;\nprintf(\"%d\", t1.v[0]);\n```",
        answer: 1, tol: 0,
        explain: "מערך בתוך מבנה מועתק במלואו, ולכן `t2.v` הוא עותק נפרד. שינוי בו לא משפיע על `t1.v[0]`, שנשאר 1." },
      recap: "מערך בתוך מבנה מועתק במלואו." },
    { id: "C08-Q3", question: "מה מדפיס הקוד?\n```c\nunion U { int a; int b; } u;\nu.a = 5;\nu.b = 8;\nprintf(\"%d\", u.a);\n```",
      options: [{ id: "a", value: "`8`" }, { id: "b", value: "`5`" }, { id: "c", value: "`13`" }, { id: "d", value: "`0`" }],
      correctId: "a",
      explanation: "שדות האיחוד חולקים את אותו זיכרון, והכתיבה האחרונה (`u.b = 8`) דורסת את הקודמת. לכן קוראים 8 גם דרך `u.a`.",
      recap: "באיחוד הכתיבה האחרונה קובעת." },
    { id: "C08-Q4", question: "מה מדפיס הקוד?\n```c\nint x = 10;\nvoid f(int x)\n{\n    x = x + 1;\n    printf(\"%d \", x);\n}\nint main(void)\n{\n    f(1);\n    printf(\"%d\", x);\n    return 0;\n}\n```",
      options: [{ id: "a", value: "`2 10`" }, { id: "b", value: "`11 11`" }, { id: "c", value: "`2 2`" }, { id: "d", value: "`11 10`" }],
      correctId: "a",
      explanation: "הפרמטר `x` מסתיר את הגלובלי בתוך `f`: הוא מקבל 1, גדל ל-2 ומודפס. הגלובלי לא נגע, ולכן ב-`main` מודפס 10.",
      recap: "פרמטר באותו שם מסתיר את הגלובלי." },
    { id: "C08-Q5", question: "מה מדפיס הקוד?\n```c\nint x = 1;\n{\n    int x = 2;\n    x++;\n}\nprintf(\"%d\", x);\n```",
      options: [{ id: "a", value: "`1`" }, { id: "b", value: "`2`" }, { id: "c", value: "`3`" }, { id: "d", value: "שגיאת הידור" }],
      correctId: "a",
      explanation: "בתוך הבלוק `x` הוא משתנה חדש שמסתיר את החיצוני, וה-`x++` משנה אותו בלבד. אחרי הבלוק הוא נעלם, והחיצוני נשאר 1. הצהרה באותו שם בבלוק פנימי מותרת.",
      recap: "משתנה בבלוק פנימי מסתיר ולא משנה את החיצוני." },
    { id: "C08-Q6", question: "מה מהבאים **אינו** חלק מהנחיית קדם-מעבד?",
      options: [
        { id: "a", value: "`typedef`" }, { id: "b", value: "`define`" },
        { id: "c", value: "`ifndef`" }, { id: "d", value: "`include`" }],
      correctId: "a",
      explanation: "`define`, `ifndef` ו-`include` הן הנחיות קדם-מעבד שנכתבות אחרי `#`. `typedef` היא הצהרה רגילה של שפת C שמעובדת בהידור עצמו.",
      recap: "typedef אינה הנחיית קדם-מעבד." },
  ],
});
