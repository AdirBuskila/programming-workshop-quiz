/* files_strings, level 8 - C08 */
COURSE_LEVEL("files_strings", {
  "id": "C08",
  "order": 8,
  "icon": "🏆",
  "title": "מבחן גמר: שאלות מהמבחן",
  "goal": "אחרי השלב הזה אפשר לפתור שאלות קבצים בגודל של שאלת מבחן אמיתית.",
  "boss": true,
  "source": "ai-verified",
  "lesson": {
    "html": "<p>ארבע שאלות אמיתיות מהמבחנים, חלקן עם צעדים מודרכים. לפני שכותבים קוד, עוברים על הרשימה:</p><ul><li>איזה סוג קובץ זה (טקסט או בינארי) ואיזו קריאה מתאימה: <code>fscanf</code> למילים ומספרים, <code>fgets</code> לשורות, <code>fgetc</code> לתווים, <code>fread</code> לרשומות?</li><li>מה מחזירים אם הקובץ לא נפתח?</li><li>האם צריך את <code>'\\n'</code>: מורידים אחרי <code>fgets</code>, וכותבים אותו חזרה עם <code>\"%s\\n\"</code>?</li><li>בשאלות פלט: רושמים אחרי כל קריאה מה נקרא ואיפה הסמן, ולא סומכים על <code>feof</code>.</li><li>סוגרים את כל הקבצים בכל מסלול יציאה.</li></ul><div class=\"lesson-rule\">🔑 בודקים את ערך ההחזרה של הקריאה עצמה, ולא את <code>feof</code>: <code>fscanf == 1</code>, <code>fgets != NULL</code>, <code>fread == 1</code>.</div>"
  },
  "questions": [
    {
      "bankId": "24B-A-Q6",
      "recap": "`fgets(st, 2, f)` קוראת תו אחד בכל קריאה, והקריאה הפנימית בלולאה צורכת את התו הבא."
    },
    {
      "bankId": "25B-A-Q3",
      "recap": "מילה שלמה: `fscanf` עם `%100s` ו-`strcmp`, כשמחזירים `-1` אם הקובץ לא נפתח."
    },
    {
      "bankId": "25B-B-Q3",
      "recap": "טקסט לבינארי: `fscanf` עם `%9s%30s%lf` והכתיבה של הרשומה כולה עם `fwrite`."
    },
    {
      "bankId": "24B-B-Q3",
      "recap": "סינון שורות: הסרת `'\\n'`, פונקציית עזר לאותיות שונות, ושורות הפוכות לקובץ הפלט."
    }
  ]
});
