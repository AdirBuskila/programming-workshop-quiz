/* dyn_2d, level 8 - generated and machine-checked by tools/verify/needhelp/dyn_2d/check.py */
COURSE_LEVEL("dyn_2d", {
  id: "C08", order: 8, icon: "🏆", title: "אלוף: שאלות אמיתיות ממבחנים",
  goal: "אחרי השלב הזה אפשר לפתור שאלות אמיתיות על מטריצות דינמיות, משולשים ומערכי מבנים.",
  boss: true,
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>זה שלב האלוף: שאלות אמיתיות ממבחנים קודמים. בכל אחת מהן אותו שלד:</p>
    <ul>
      <li>שרטטו קלט ופלט עם דוגמה 3×3, וכתבו אורך כל שורה ונוסחת אינדקס (מקור מול יעד).</li>
      <li>הקצו קודם את מערך המצביעים, ואז כל שורה בלולאה. <code>calloc</code> כשצריך אפסים.</li>
      <li>החזרה: ב-<code>return</code> או דרך <code>int ***out</code> / <code>int *size</code>, עם <code>*out = ...</code> ו-<code>(*out)[k]</code>.</li>
      <li>שחרור: קודם השורות ואז המערך החיצוני, ורק אחרי שהעתקתם.</li>
    </ul>
    <div class="lesson-rule">🔑 בדקו תמיד מקרה קטן (למשל $n = 1$) ואת כל הקצאה: האם יש לה שחרור, והאם הגודל הוא <code>sizeof</code> של הטיפוס הנכון.</div>` },
  questions: [
    {"bankId": "24B-B-Q2", "recap": "מסגרת סביב מטריצה: `calloc` לאפסים, העתקה עם היסט 1, ושחרור המקור אחרי ההעתקה."},
    {"bankId": "24B-A-Q2", "recap": "מערך של מבנים: `calloc` נותן `size = 0` ו-`ptr = NULL`, ו-`realloc` מקטין לגודל הסופי."},
    {"bankId": "25B-A-Q2", "recap": "ממטריצה סטטית לשני משולשים משוננים דרך `int ***`."},
    {"bankId": "25B-B-Q2", "recap": "משני משולשים למטריצה $(n+1) \\times (n+1)$ עם אלכסון אפס: נוסחאות אינדקס."},
    {"bankId": "23B-A-Q2", "recap": "שני מערכי פלט דרך פרמטרים, אורך מקסימלי ואז `realloc`."},
  ],
});
