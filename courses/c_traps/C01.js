/* c_traps, level 1 - characters are small integers (ASCII). */
COURSE_LEVEL("c_traps", {
  id: "C01", order: 1, icon: "🔤", title: "תווים הם מספרים",
  goal: "אחרי השלב הזה אפשר לחשב מה מדפיסה printf כשמעבירים לה תו, ולהבדיל בין התו '0' לבין המספר 0.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>ב-C תו בגרשיים בודדים, כמו <code>'a'</code>, הוא <b>מספר שלם</b>: קוד ה-ASCII שלו. כמה קודים שכדאי לזכור:</p>
    <table><thead><tr><th>תו</th><th>קוד</th></tr></thead>
    <tbody><tr><td><code>'\0'</code></td><td>0</td></tr><tr><td><code>'0'</code></td><td>48</td></tr><tr><td><code>'A'</code></td><td>65</td></tr><tr><td><code>'a'</code></td><td>97</td></tr></tbody></table>
    <p>הספרות <code>'0'</code> עד <code>'9'</code> רצופות, והאותיות הגדולות והקטנות רצופות גם הן. לכן <code>'a' + 1</code> הוא 98, ו-<code>c - '0'</code> ממיר תו ספרה לערך שלו.</p>
    <p>ההדפסה תלויה בתבנית: <code>%d</code> מדפיסה את המספר, ו-<code>%c</code> מדפיסה את התו שהמספר מייצג.</p>
    <pre><code>printf("%d", 'A');      /* 65 */
printf("%c", 65);       /* A  */
printf("%c", 'A' + 1);  /* B  */</code></pre>
    <div class="lesson-rule">🔑 התו <code>'0'</code> (קוד 48) אינו המספר 0. רק <code>'\0'</code> שווה ל-0.</div>
    <div class="lesson-ex">דוגמה: <code>'7' - '0'</code> הוא <code>55 - 48 = 7</code>, ו-<code>'a' - 'A'</code> הוא <code>97 - 65 = 32</code>.</div>
    <div class="lesson-trap">⚠️ <code>"0"</code> במרכאות כפולות היא מחרוזת, ו-<code>'0'</code> בגרשיים הוא תו. הם לא אותו דבר.</div>` },
  questions: [
    { id: "C01-Q1", question: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", '0');\n```",
      options: [{ id: "a", value: "`0`" }, { id: "b", value: "`48`" }, { id: "c", value: "`'0'`" }, { id: "d", value: "שגיאת הידור" }],
      correctId: "b",
      explanation: "`'0'` הוא תו הספרה אפס, וקוד ה-ASCII שלו הוא 48. התבנית `%d` מדפיסה את הקוד כמספר. התשובה `0` נכונה רק עבור `'\\0'`, והתבנית `%d` אינה מדפיסה גרשיים.",
      recap: "התו '0' שווה 48, לא 0." },
    { id: "C01-Q2", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nprintf(\"%d\", '7' - '0');\n```",
        answer: 7, tol: 0,
        explain: "`'7'` הוא 55 ו-`'0'` הוא 48, ולכן ההפרש הוא 7. כך ממירים תו ספרה לערכו." },
      recap: "c - '0' נותן את ערך הספרה." },
    { id: "C01-Q3", question: "מה מדפיס הקוד?\n```c\nprintf(\"%c%c%c\", 'a' + 1, 'A' + 2, '0' + 3);\n```",
      options: [{ id: "a", value: "`bC3`" }, { id: "b", value: "`98 67 51`" }, { id: "c", value: "`aA0`" }, { id: "d", value: "`b C 3`" }],
      correctId: "a",
      explanation: "התבנית `%c` מדפיסה את התו שמייצג הקוד: 98 הוא `b`, 67 הוא `C`, ו-51 הוא `3`. התשובה `98 67 51` הייתה נכונה עם `%d`, ובתבנית אין רווחים ולכן אין רווחים בפלט.",
      recap: "%c מדפיסה תו, %d מדפיסה את הקוד." },
    { id: "C01-Q4", question: "איזו מההוראות הבאות **לא** מדפיסה 0?",
      options: [
        { id: "a", value: "`printf(\"%d\", '\\0');`" },
        { id: "b", value: "`printf(\"%d\", '0');`" },
        { id: "c", value: "`printf(\"%d\", '0' - '0');`" },
        { id: "d", value: "`printf(\"%d\", 'a' - 'a');`" }],
      correctId: "b",
      explanation: "`'0'` שווה 48. `'\\0'` שווה 0, וההפרש של תו עם עצמו (`'0' - '0'` או `'a' - 'a'`) הוא 0.",
      recap: "רק '\\0' הוא אפס; '0' הוא 48." },
    { id: "C01-Q5", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nchar c = 'x';\nc = c - 'a' + 'A';\nprintf(\"%d\", c);\n```",
        answer: 88, tol: 0,
        explain: "`'x'` הוא 120, `'a'` הוא 97 ו-`'A'` הוא 65. מקבלים $120 - 97 + 65 = 88$, וזה קוד התו `'X'`. כך ממירים אות קטנה לגדולה." },
      recap: "c - 'a' + 'A' הופך אות קטנה לגדולה." },
  ],
});
