/* c_traps, level 9 - boss: real exam questions. */
COURSE_LEVEL("c_traps", {
  id: "C09", order: 9, icon: "🏆", title: "אתגר המלכודות",
  goal: "אחרי השלב הזה אפשר לפתור שאלות מלכודת אמיתיות מהמבחנים: סיווג הנחיות, הכללה בין פונקציות קלט, sizeof של מחרוזת, לולאת fgetc וחילוק תווים.",
  boss: true,
  source: "ai-verified",
  lesson: { html: String.raw`
    <p>אתגר סיום: חמש שאלות אמיתיות מבחנים קודמים. לפני שפותרים, הפעילו את הכללים מהשלבים הקודמים.</p>
    <ul>
      <li>תו הוא מספר, והחילוק בין תווים הוא חילוק שלם; לולאה על מערך נעצרת באיבר 0.</li>
      <li><code>sizeof</code> של מחרוזת קבועה כולל את <code>'\0'</code>, והאינדקס חזק מ-<code>sizeof</code>.</li>
      <li><code>!=</code> חזק מ-<code>=</code>, ולכן בלי סוגריים ההשמה מקבלת 0 או 1.</li>
      <li><code>fgets</code> שונה מ-<code>gets</code>; הצורות שמתחילות ב-<code>f</code> הן הכללות של הצורות הרגילות רק כשהן מתנהגות אותו דבר על <code>stdin</code>.</li>
      <li><code>typedef</code> אינה הנחיית קדם-מעבד.</li>
    </ul>
    <div class="lesson-rule">🔑 בכל שאלה כתבו את הכלל שעליו הסתמכתם לפני שאתם בוחרים תשובה.</div>` },
  questions: [
    { bankId: "19S-A-Q4d", recap: "typedef אינה הנחיית קדם-מעבד." },
    { bankId: "20B-A-Q4a", recap: "fgets אינה הכללה של gets." },
    { bankId: "19B-A-Q5", recap: "[ ] חזק מ-sizeof, והגודל הוא של תו." },
    { bankId: "25B-A-Q6", recap: "!= חזק מ-=, ולכן c הוא 1." },
    { bankId: "25B-B-Q6", recap: "חילוק תווים שלם והלולאה נעצרת באפס." },
  ],
});
