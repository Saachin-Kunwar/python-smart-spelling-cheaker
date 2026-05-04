# 🧠 Smart Spell Checker Pro (English + Nepali)

<p align="center">
  An intelligent <b>Spell Checker Application</b> built using <b>Python</b> and <b>Tkinter</b>.<br>
  Designed to handle <b>mixed-language input (English + Nepali)</b> with smart detection and correction.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Library-PySpellChecker-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

---

## 🚀 Features

### 🔤 Spell Checking
- Detects incorrect English words
- Highlights errors in real-time
- Provides correction suggestions

### 🇳🇵 Nepali Language Support
- Ignores Romanized Nepali (e.g., *mero, naam, khelchu*)
- Supports Unicode Nepali (e.g., *मेरो नाम*)
- Prevents wrong auto-corrections

### 🧠 Smart Language Detection
- Differentiates between:
  - Correct English words ✔  
  - Incorrect English words ❌  
  - Nepali / unknown words 🇳🇵 (ignored)

### 🖱️ Interactive UI
- Clean Tkinter-based interface
- Right-click suggestion menu (Grammarly-like)
- Error highlighting system

### ⚡ Auto Correction
- One-click correction of all English mistakes
- Preserves capitalization and formatting

### 📊 Live Feedback
- Word count display
- Error count tracking

---

## 🛠️ Tech Stack

| Category        | Technology |
|----------------|-----------|
| Language        | Python 🐍 |
| GUI Framework   | Tkinter |
| Library         | PySpellChecker |
| Processing      | Regex (re) |

---

📌 How It Works
<details> <summary>🎮 Click to expand</summary>
- User enters text in the editor <br>
- System scans each word using SpellChecker<br>
- If: <br>
   - Word is correct → ✔ accepted <br>
   - Suggestions exist → ❌ marked as error <br>
   - No suggestions → 🇳🇵 treated as Nepali (ignored) <br>
- Errors are highlighted <br>
- User can: <br>
  - Right-click for suggestions <br>
  - Auto-correct entire text <br>
</details>
📈 What I Learned
<details> <summary>🧠 Click to expand</summary>
- Building intelligent text processing systems <br>
- GUI development using Tkinter <br>
- Language detection techniques <br>
- Handling mixed-language input <br>
- Improving user experience in desktop apps <br>
</details>


⚠️ Challenges Faced
<details> <summary>🚧 Click to expand</summary>
- Differentiating English vs Nepali words <br>
- Avoiding incorrect auto-corrections <br>
- Managing text tokenization properly <br>
- Designing interactive suggestion system <br>
- Maintaining formatting after correction <br>
</details>

💡 Solutions
<details> <summary>🛠️ Click to expand</summary>
- Implemented smart detection logic <br>
- Used SpellChecker candidate filtering <br>
- Applied regex-based tokenization <br>
- Added right-click suggestion feature <br>
- Preserved formatting with custom logic <br>
</details>

## 🔮 Future Improvements
- 🌙 Dark mode support <br>
- 📂 File open/save (.txt) <br>
- 🌐 Web version (Django/React) <br>
- 🤖 Grammar checking (LanguageTool API) <br>
- 🎤 Voice input support <br>

🤝 Contributing

Contributions are welcome!
Feel free to fork and submit a pull request.

⭐ Support

If you like this project, give it a ⭐ on GitHub!
👨‍💻 Author

Saachin Kunwar

<p align="center"> Made with ❤️ using Python & Tkinter </p>












