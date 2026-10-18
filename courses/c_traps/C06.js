/* c_traps, level 6 - reading files: fgetc/EOF, feof loops, fgets, fscanf. */
COURSE_LEVEL("c_traps", {
  id: "C06", order: 6, icon: "📂", title: "קריאה מקבצים",
  goal: "אחרי השלב הזה אפשר לחשב מה מדפיסה לולאת קריאה מקובץ, ולזהות את המלכודות של EOF, של feof ושל fgets.",
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>הפונקציות לקריאה מקובץ מקבלות מצביע <code>FILE *f</code>. כל אחת מהן היא <b>הכללה</b> של פונקציית הקלט הרגילה: היא עובדת על קובץ שנבחר, והרגילה עובדת על המקלדת. <code>fprintf(stdout, ...)</code> שווה ל-<code>printf(...)</code>, <code>fscanf(stdin, ...)</code> שווה ל-<code>scanf(...)</code> ו-<code>fgetc(stdin)</code> שווה ל-<code>getchar()</code>.</p>
    <ul>
      <li><code>fgetc(f)</code> מחזירה את התו הבא כמספר, או את הקבוע <code>EOF</code> (בדרך כלל -1) בסוף הקובץ. לכן שומרים את התוצאה ב-<code>int</code>.</li>
      <li><code>fscanf(f, ...)</code> מחזירה כמה ערכים נקראו בפועל (אפשר גם <code>EOF</code>). כשהקריאה נכשלת היא לא נוגעת במשתנה.</li>
      <li><code>fgets(st, n, f)</code> קוראת עד <code>n-1</code> תווים, או עד סוף השורה, וכוללת את <code>'\n'</code> במחרוזת. אם <code>n</code> הוא 2 היא קוראת תו אחד. זה שונה מ-<code>gets</code> שלא מקבלת גודל וזורקת את סוף השורה, ולכן <code>fgets</code> אינה הכללה של <code>gets</code>.</li>
      <li><code>feof(f)</code> נעשית אמת רק <b>אחרי</b> שניסינו לקרוא מעבר לסוף הקובץ ולא הצלחנו.</li>
      <li><code>fopen</code> מחזירה <code>NULL</code> אם הפתיחה נכשלה.</li>
    </ul>
    <div class="lesson-rule">🔑 הלולאה הנכונה: <code>int c; while ((c = fgetc(f)) != EOF) ...</code>. הסוגריים סביב ההשמה הכרחיים.</div>
    <div class="lesson-ex">דוגמה: בקובץ <code>abc</code>, הלולאה שלמעלה מקבלת 97, 98 ו-99 ונעצרת כש-<code>fgetc</code> מחזירה <code>EOF</code>.</div>
    <div class="lesson-trap">⚠️ <code>while (c = fgetc(f) != EOF)</code> מחושב כ-<code>c = (fgetc(f) != EOF)</code>, כי <code>!=</code> חזק מ-<code>=</code>. המשתנה <code>c</code> הוא 1 בכל תו, והלולאה מדפיסה 1 פעם אחת לכל תו בקובץ.</div>` },
  questions: [
    { id: "C06-Q1", question: "הקובץ `data.txt` מכיל את הטקסט `abc` (בלי שורה חדשה בסוף). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint c;\nwhile ((c = fgetc(f)) != EOF)\n    printf(\"%d \", c);\nfclose(f);\n```",
      options: [{ id: "a", value: "`97 98 99`" }, { id: "b", value: "`a b c`" }, { id: "c", value: "`1 1 1`" }, { id: "d", value: "`97 98 99 -1`" }],
      correctId: "a",
      explanation: "`fgetc` מחזירה קודים: 97, 98, 99, ואחריהם `EOF` שעוצר את הלולאה בלי להדפיס. התבנית `%d` מדפיסה מספרים ולא תווים. התוצאה `1 1 1` שייכת לגרסה בלי הסוגריים, והערך `-1` לא מודפס כי הוא סיבת העצירה.",
      recap: "(c = fgetc(f)) != EOF, עם סוגריים." },
    { id: "C06-Q2", question: "הקובץ `data.txt` מכיל את הטקסט `hi` (בלי שורה חדשה בסוף). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nchar ch;\nwhile (ch = fgetc(f) != EOF)\n    printf(\"%d\", ch);\nfclose(f);\n```",
      options: [{ id: "a", value: "`11`" }, { id: "b", value: "`104105`" }, { id: "c", value: "`hi`" }, { id: "d", value: "`00`" }],
      correctId: "a",
      explanation: "בלי סוגריים, `!=` חזק מ-`=`, ולכן `ch` מקבל את תוצאת ההשוואה `fgetc(f) != EOF`, כלומר 1 כל עוד יש תו. שני תווים נותנים `11`. הקודים 104 ו-105 היו מודפסים אילו ההשמה הייתה בסוגריים.",
      recap: "!= חזק מ-=, ולכן ch הוא 0 או 1." },
    { id: "C06-Q3", question: "הקובץ `data.txt` מכיל `1 2 3` ואחריהם **תו שורה חדשה** (שלושה מספרים בשורה אחת). מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint x = 0;\nwhile (!feof(f))\n{\n    fscanf(f, \"%d\", &x);\n    printf(\"%d \", x);\n}\nfclose(f);\n```",
      options: [{ id: "a", value: "`1 2 3 3`" }, { id: "b", value: "`1 2 3`" }, { id: "c", value: "`1 2 3 0`" }, { id: "d", value: "`1 2 3 -1`" }],
      correctId: "a",
      explanation: "אחרי קריאת 3, התו שנשאר הוא שורה חדשה, ו-`feof` עדיין שקרית. נכנסים לסיבוב רביעי: `fscanf` נכשלת בגלל סוף הקובץ ולא משנה את `x`, אז מודפס שוב 3, ורק עכשיו `feof` נעשית אמת. זה סיבוב אחד יותר ממספר הערכים.",
      recap: "feof נעשית אמת רק אחרי קריאה שנכשלה." },
    { id: "C06-Q4", step: { type: "numeric",
        prompt: "הקובץ `data.txt` מכיל שתי שורות: `ab` ואחריה `cd`, וכל שורה נגמרת בתו שורה חדשה. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nchar st[10];\nfgets(st, 10, f);\nprintf(\"%d\", (int)strlen(st));\nfclose(f);\n```",
        answer: 3, tol: 0,
        explain: "`fgets` קוראת עד סוף השורה וכוללת את `'\\n'`: המחרוזת היא `ab\\n`, כלומר 3 תווים. `gets` הייתה זורקת את סוף השורה." },
      recap: "fgets שומרת את '\\n'." },
    { id: "C06-Q5", step: { type: "numeric",
        prompt: "הקובץ `data.txt` מכיל את הטקסט `5 x`. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"data.txt\", \"r\");\nint a = 0, b = 0;\nint n = fscanf(f, \"%d %d\", &a, &b);\nprintf(\"%d\", n);\nfclose(f);\n```",
        answer: 1, tol: 0,
        explain: "`fscanf` מחזירה את מספר הערכים שנקראו בהצלחה. הראשון (5) נקרא, והשני נכשל כי `x` אינו מספר, ולכן הערך המוחזר הוא 1." },
      recap: "fscanf מחזירה כמה ערכים נקראו." },
    { id: "C06-Q6", question: "הקובץ `nope.txt` **לא קיים**. מה מדפיס הקוד?\n```c\nFILE *f = fopen(\"nope.txt\", \"r\");\nprintf(\"%d\", f == NULL);\n```",
      options: [{ id: "a", value: "`1`" }, { id: "b", value: "`0`" }, { id: "c", value: "הקוד קורס בשורת ה-`fopen`" }, { id: "d", value: "`-1`" }],
      correctId: "a",
      explanation: "`fopen` על קובץ שלא קיים לקריאה אינה קורסת: היא מחזירה `NULL`. ההשוואה `f == NULL` נותנת 1. התקלה מתרחשת רק אם משתמשים ב-`f` בלי לבדוק אותו.",
      recap: "fopen מחזירה NULL כשנכשלה." },
  ],
});
