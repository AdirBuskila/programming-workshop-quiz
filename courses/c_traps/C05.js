/* c_traps, level 5 - strings, arrays and pointers to literals. */
COURSE_LEVEL("c_traps", {
  id: "C05", order: 5, icon: "🧵", title: "מחרוזות ומצביעים",
  goal: "אחרי השלב הזה אפשר להבדיל בין מערך תווים למצביע למחרוזת קבועה, להשוות מחרוזות נכון, ולזהות כתיבה אסורה למחרוזת קבועה.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>מחרוזת היא מערך תווים שנגמר ב-<code>'\0'</code>.</p>
    <ul>
      <li><code>char a[] = "hi";</code> יוצר <b>מערך</b> משלו (3 בתים) שאפשר לשנות.</li>
      <li><code>char *p = "hi";</code> יוצר <b>מצביע</b> למחרוזת קבועה. כתיבה דרכו (<code>p[0] = 'H'</code>) היא התנהגות לא מוגדרת לפי תקן C: ייתכן שהתוכנית תקרוס, וייתכן שלא.</li>
      <li><code>a == b</code> על שני מערכים או מצביעים משווה <b>כתובות</b>, לא תוכן. שני מערכים נפרדים תמיד בכתובות שונות, ולכן <code>==</code> נותן 0 גם כשהתוכן זהה.</li>
      <li><code>strcmp(a, b)</code> משווה תוכן ומחזירה <b>0 כשהמחרוזות שוות</b>, מספר שלילי כש-<code>a</code> קודמת ל-<code>b</code>, וחיובי אחרת.</li>
      <li>מחרוזת קבועה היא כתובת של התו הראשון, ולכן <code>"hello" + 2</code> היא המחרוזת <code>"llo"</code>.</li>
      <li>איברים שלא אותחלו במפורש במערך שיש לו אתחול מקבלים 0: ב-<code>char s[6] = "ab"</code> האיברים <code>s[2]</code> עד <code>s[5]</code> הם <code>'\0'</code>.</li>
    </ul>
    <div class="lesson-rule">🔑 משווים תוכן עם <code>strcmp</code> והתנאי "שווה" הוא <code>strcmp(a, b) == 0</code>, כלומר <code>!strcmp(a, b)</code>.</div>
    <div class="lesson-ex">דוגמה: אחרי <code>char s[] = "hello"; s[2] = '\0';</code> המחרוזת מסתיימת באינדקס 2, ולכן <code>strlen(s)</code> הוא 2 ו-<code>printf("%s", s)</code> מדפיס <code>he</code>.</div>
    <div class="lesson-trap">⚠️ <code>if (strcmp(a, b))</code> מתקיים כשהמחרוזות <b>שונות</b>, כי הערך אינו אפס.</div>` },
  questions: [
    { id: "C05-Q1", question: "מה מדפיס הקוד?\n```c\nchar a[] = \"hi\";\nchar b[] = \"hi\";\nprintf(\"%d\", a == b);\n```",
      options: [{ id: "a", value: "`0`" }, { id: "b", value: "`1`" }, { id: "c", value: "`2`" }, { id: "d", value: "שגיאת הידור" }],
      correctId: "a",
      explanation: "`a == b` משווה את הכתובות של שני מערכים נפרדים, והן תמיד שונות, ולכן התוצאה 0 למרות שהתוכן זהה. להשוואת תוכן משתמשים ב-`strcmp`.",
      recap: "== על מחרוזות משווה כתובות." },
    { id: "C05-Q2", question: "מה מדפיס הקוד?\n```c\nprintf(\"%s\", \"hello\" + 2);\n```",
      options: [{ id: "a", value: "`llo`" }, { id: "b", value: "`hello2`" }, { id: "c", value: "`ello`" }, { id: "d", value: "`he`" }],
      correctId: "a",
      explanation: "המחרוזת הקבועה היא כתובת של התו הראשון, והוספת 2 מזיזה לתו באינדקס 2. מודפס כל מה שנשאר עד `'\\0'`: `llo`. התשובה `ello` נכונה להוספת 1.",
      recap: "s + k מצביע לתו באינדקס k." },
    { id: "C05-Q3", question: "מה מדפיס הקוד?\n```c\nchar s[] = \"hello\";\ns[2] = '\\0';\nprintf(\"%d %s\", (int)strlen(s), s);\n```",
      options: [{ id: "a", value: "`2 he`" }, { id: "b", value: "`5 hello`" }, { id: "c", value: "`3 hel`" }, { id: "d", value: "`2 llo`" }],
      correctId: "a",
      explanation: "הכתיבה של `'\\0'` לאינדקס 2 מסיימת את המחרוזת שם. `strlen` סופר 2 תווים (`he`), ו-`%s` מדפיס עד התו האפס. המערך עצמו עדיין באורך 6, אבל המחרוזת הקצרה יותר.",
      recap: "'\\0' באמצע מקצר את המחרוזת." },
    { id: "C05-Q4", question: "מה מדפיס הקוד?\n```c\nchar *a = \"x\";\nchar *b = \"x\";\nif (strcmp(a, b))\n    printf(\"diff\");\nelse\n    printf(\"same\");\n```",
      options: [{ id: "a", value: "`same`" }, { id: "b", value: "`diff`" }, { id: "c", value: "`diffsame`" }, { id: "d", value: "אין פלט" }],
      correctId: "a",
      explanation: "`strcmp` מחזירה 0 כשהמחרוזות שוות, ו-0 הוא שקר, ולכן נבחר ה-`else` ומודפס `same`. התנאי `if (strcmp(a, b))` מתקיים רק כשהמחרוזות שונות.",
      recap: "strcmp מחזירה 0 כשהמחרוזות שוות." },
    { id: "C05-Q5", question: "מה קורה בקוד הבא לפי תקן שפת C?\n```c\nchar *s = \"hi\";\ns[0] = 'H';\n```",
      options: [
        { id: "a", value: "התנהגות לא מוגדרת: כתיבה למחרוזת קבועה" },
        { id: "b", value: "שגיאת הידור, כי `s` מצביע לקבוע" },
        { id: "c", value: "`s` הופך להיות `\"Hi\"`" },
        { id: "d", value: "נוצר עותק של המחרוזת וה-`H` נכתב אליו" }],
      correctId: "a",
      explanation: "הקוד מתקמפל, אבל התקן קובע שניסיון לשנות מחרוזת קבועה הוא התנהגות לא מוגדרת. בפועל בדרך כלל הוא קורס בזמן הריצה, אך לא מובטח שיקרה משהו מסוים. כדי שאפשר יהיה לשנות כותבים `char s[] = \"hi\";`.",
      recap: "כתיבה למחרוזת קבועה: התנהגות לא מוגדרת." },
    { id: "C05-Q6", step: { type: "numeric",
        prompt: "מה מדפיס הקוד?\n```c\nchar s[6] = \"ab\";\nprintf(\"%d\", s[4]);\n```",
        answer: 0, tol: 0,
        explain: "במערך עם אתחול, האיברים שלא אותחלו במפורש מקבלים 0. לכן `s[4]` הוא `'\\0'` ומודפס 0." },
      recap: "שאר האיברים במערך מאותחל הם 0." },
  ],
});
