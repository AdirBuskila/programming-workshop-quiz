/* c_traps, level 4 - sizeof. */
COURSE_LEVEL("c_traps", {
  id: "C04", order: 4, icon: "📏", title: "sizeof",
  goal: "אחרי השלב הזה אפשר לחשב sizeof של מערכים ושל מחרוזות קבועות, ולהבחין בינו לבין strlen.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p><code>sizeof</code> הוא אופרטור (לא פונקציה) שמחשב בזמן ההידור את גודל הטיפוס או הביטוי בבתים. הערך שלו מטיפוס <code>size_t</code> (מספר שלם חיובי), ולכן מדפיסים אותו עם המרה: <code>printf("%d", (int)sizeof x)</code>.</p>
    <ul>
      <li><b>מערך</b>: <code>sizeof a</code> הוא מספר האיברים כפול גודל איבר. לכן <code>sizeof a / sizeof a[0]</code> הוא מספר האיברים.</li>
      <li><b>מחרוזת קבועה</b>: <code>sizeof "hello"</code> הוא 6, כי הגודל כולל את <code>'\0'</code> הסופי. לעומת זאת <code>strlen("hello")</code> הוא 5, והוא סופר רק עד התו האפס.</li>
      <li>מערך <code>char s[10] = "abc"</code>: ה-<code>sizeof</code> הוא 10 (גודל המערך) וה-<code>strlen</code> הוא 3 (אורך הטקסט).</li>
      <li><code>sizeof</code> <b>לא מריץ</b> את הביטוי שלו: ב-<code>sizeof(i++)</code> המשתנה <code>i</code> לא משתנה.</li>
      <li>האינדקס <code>[ ]</code> חזק מ-<code>sizeof</code>, ולכן <code>sizeof "abc"[1]</code> הוא הגודל של התו <code>"abc"[1]</code>, כלומר 1.</li>
      <li>התו <code>'a'</code> ב-C הוא מטיפוס <code>int</code>, לכן <code>sizeof('a') == sizeof(int)</code>.</li>
    </ul>
    <div class="lesson-rule">🔑 פרמטר מערך של פונקציה (<code>void f(int a[])</code>) הוא בעצם מצביע. בתוך הפונקציה <code>sizeof a</code> הוא גודל מצביע ולא גודל המערך, ולכן אי אפשר לחשב שם את מספר האיברים כך.</div>
    <div class="lesson-ex">דוגמה: <code>int a[10]</code>. מקבלים <code>sizeof a / sizeof a[0]</code>, שזה 10 איברים, בלי קשר לגודל של <code>int</code> במחשב.</div>
    <div class="lesson-trap">⚠️ גודל של מצביע תלוי במחשב (4 או 8 בתים). בשאלה שתלויה בו חייבים לכתוב את ההנחה, ואם אפשר מעדיפים לא להסתמך עליו.</div>` },
  questions: [
    { id: "C04-Q1", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", (int)sizeof \"hello\");\n```",
        answer: 6, tol: 0,
        explain: "המחרוזת הקבועה כוללת 5 תווים ועוד `'\\0'` סופי, ולכן הגודל הוא 6. הערך 5 היה `strlen`." },
      recap: "sizeof של מחרוזת כולל את '\\0'." },
    { id: "C04-Q2", question: "מה מדפיס הקוד?\n```c\nchar s[10] = \"abc\";\nprintf(\"%d %d\", (int)sizeof s, (int)strlen(s));\n```",
      options: [{ id: "a", value: "`10 3`" }, { id: "b", value: "`4 3`" }, { id: "c", value: "`3 3`" }, { id: "d", value: "`10 10`" }],
      correctId: "a",
      explanation: "`sizeof s` הוא גודל המערך כולו, 10 בתים. `strlen(s)` סופר עד התו האפס הראשון, כלומר 3. הערך 4 היה נכון אילו המערך הוגדר `char s[] = \"abc\"`.",
      recap: "sizeof הוא גודל המערך; strlen הוא אורך הטקסט." },
    { id: "C04-Q3", step: { type: "numeric",
        prompt: "מה מדפיס הקוד (המספר שמודפס אינו תלוי בגודל של `int`)?\n```c\nint a[10];\nprintf(\"%d\", (int)(sizeof a / sizeof a[0]));\n```",
        answer: 10, tol: 0,
        explain: "`sizeof a` הוא 10 איברים כפול גודל איבר, ו-`sizeof a[0]` הוא גודל איבר אחד. המנה היא מספר האיברים, 10." },
      recap: "sizeof a / sizeof a[0] הוא מספר האיברים." },
    { id: "C04-Q4", question: "מה מדפיס הקוד?\n```c\nint i = 5;\nint n = sizeof(i++);\nprintf(\"%d\", i);\n```",
      options: [{ id: "a", value: "`5`" }, { id: "b", value: "`6`" }, { id: "c", value: "`4`" }, { id: "d", value: "`n`" }],
      correctId: "a",
      explanation: "`sizeof` מחשב רק את הטיפוס של הביטוי ולא מריץ אותו, ולכן `i++` לא מתבצע ו-`i` נשאר 5. התשובה 6 מניחה שההגדלה התבצעה.",
      recap: "sizeof לא מריץ את הביטוי." },
    { id: "C04-Q5", question: "הפונקציה:\n```c\nvoid f(int a[])\n{\n    int n = sizeof a / sizeof a[0];\n}\n```\nנקראת עם מערך של 10 איברים. איזו טענה נכונה?",
      options: [
        { id: "a", value: "`sizeof a` בתוך `f` הוא גודל של מצביע, ולכן `n` אינו מספר האיברים של המערך" },
        { id: "b", value: "`n` שווה תמיד ל-10" },
        { id: "c", value: "הקוד לא מתקמפל כי אי אפשר להשתמש ב-`sizeof` על פרמטר" },
        { id: "d", value: "`sizeof a` הוא גודל כל המערך שהועבר" }],
      correctId: "a",
      explanation: "פרמטר שנכתב כמערך הוא מצביע לאיבר הראשון. לכן `sizeof a` הוא גודל מצביע ו-`n` אינו מספר האיברים. הקוד מתקמפל, ו-`n` לא שווה בהכרח ל-10.",
      recap: "פרמטר מערך הוא מצביע; sizeof שלו הוא גודל מצביע." },
    { id: "C04-Q6", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", (int)sizeof \"abc\"[1]);\n```",
        answer: 1, tol: 0,
        explain: "האינדקס `[ ]` חזק מ-`sizeof`, ולכן מחשבים את הגודל של האיבר `\"abc\"[1]`, שהוא תו מטיפוס `char`. הגודל הוא 1. אילו `sizeof` חל על המחרוזת כולה, התוצאה הייתה 4." },
      recap: "[ ] חזק מ-sizeof." },
  ],
});
