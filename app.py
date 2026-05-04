import tkinter as tk
from tkinter import scrolledtext, Menu
from spellchecker import SpellChecker
import re


class SmartSpellCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Spell Checker Pro ✨")
        self.root.geometry("800x600")
        self.root.config(bg="#f5f5f5")

        self.spell = SpellChecker()
        self.current_word = None

        # ---------------- HEADER ----------------
        title = tk.Label(
            root,
            text="Smart Spell Checker (English + Nepali)",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#333"
        )
        title.pack(pady=10)

        # ---------------- TEXT AREA ----------------
        self.text_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 13),
            undo=True
        )
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<Button-3>", self.show_suggestions)  # Right click

        # Highlight style
        self.text_area.tag_config("error", background="#ffcccc")

        # ---------------- BUTTONS ----------------
        btn_frame = tk.Frame(root, bg="#f5f5f5")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Check", width=15, command=self.check_spelling).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Auto Correct", width=15, command=self.correct_text).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear", width=15, command=self.clear_text).pack(side=tk.LEFT, padx=5)

        # ---------------- STATUS BAR ----------------
        self.status = tk.Label(
            root,
            text="Words: 0",
            anchor="w",
            bg="#ddd",
            padx=10
        )
        self.status.pack(fill=tk.X)

    # ---------------------------
    # LANGUAGE DETECTION
    # ---------------------------
    def is_nepali_or_valid(self, word):
        w = word.lower()

        # Valid English word
        if w in self.spell:
            return True

        # If suggestions exist → it's wrong English
        if self.spell.candidates(w):
            return False

        # Otherwise assume Nepali/unknown → ignore
        return True

    # ---------------------------
    # SPELL CHECK
    # ---------------------------
    def check_spelling(self):
        text = self.text_area.get("1.0", tk.END)
        self.text_area.tag_remove("error", "1.0", tk.END)

        words = re.finditer(r"\w+", text)
        errors = 0

        for match in words:
            word = match.group()

            if self.is_nepali_or_valid(word):
                continue

            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"

            self.text_area.tag_add("error", start, end)
            errors += 1

        self.status.config(text=f"Errors found: {errors}")

    # ---------------------------
    # AUTO CORRECT
    # ---------------------------
    def correct_text(self):
        text = self.text_area.get("1.0", tk.END)
        tokens = re.findall(r"\w+|[^\w\s]", text)

        corrected = []

        for token in tokens:
            if token.isalpha():

                if self.is_nepali_or_valid(token):
                    corrected.append(token)
                    continue

                corrected_word = self.spell.correction(token.lower())

                if token[0].isupper():
                    corrected_word = corrected_word.capitalize()

                corrected.append(corrected_word)
            else:
                corrected.append(token)

        result = ""
        for i, t in enumerate(corrected):
            if i > 0 and t.isalnum() and corrected[i - 1].isalnum():
                result += " "
            result += t

        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, result)

        self.status.config(text="Text auto-corrected ✔")

    # ---------------------------
    # RIGHT CLICK SUGGESTIONS
    # ---------------------------
    def show_suggestions(self, event):
        try:
            index = self.text_area.index(f"@{event.x},{event.y}")
            word_start = self.text_area.search(r"\m\w+", index, backwards=True, regexp=True)
            word_end = self.text_area.search(r"\M", index, regexp=True)

            word = self.text_area.get(word_start, word_end)

            if self.is_nepali_or_valid(word):
                return

            suggestions = list(self.spell.candidates(word.lower()))[:5]

            menu = Menu(self.root, tearoff=0)

            for s in suggestions:
                menu.add_command(
                    label=s,
                    command=lambda replacement=s: self.replace_word(word_start, word_end, replacement)
                )

            menu.post(event.x_root, event.y_root)

        except:
            pass

    def replace_word(self, start, end, replacement):
        self.text_area.delete(start, end)
        self.text_area.insert(start, replacement)

    # ---------------------------
    # STATUS UPDATE
    # ---------------------------
    def update_status(self, event=None):
        text = self.text_area.get("1.0", tk.END)
        words = len(re.findall(r"\w+", text))
        self.status.config(text=f"Words: {words}")

    # ---------------------------
    # CLEAR TEXT
    # ---------------------------
    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.status.config(text="Cleared 🧹")


# ---------------------------
# RUN APP
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartSpellCheckerGUI(root)
    root.mainloop()