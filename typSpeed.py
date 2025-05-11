import tkinter as tk
from tkinter import messagebox
import time
import random

# --- Sample text sets for Sentence and Paragraph typing ---
sentences = [
    "Consistent effort leads to noticeable progress over time.",
    "Typing fast requires practice, focus, and muscle memory.",
    "Every keystroke counts when accuracy meets speed."
]

paragraphs = [
    "Imagine waking up one morning to find that the internet has completely vanished. No emails, no social media, no streaming, just silence. At first, it might feel like a nightmare, but soon you start to notice things you’ve been missing. It’s strange, yet oddly peaceful. Maybe, just maybe, we relied too much on a world that was never truly real.",
    "Typing is a fundamental skill in the digital age, essential for students, professionals, and anyone who spends time on a computer. Improving your typing speed not only saves time but also enhances your productivity and focus. The key to becoming a better typist is regular practice, maintaining good posture, and using all ten fingers effectively.",
    "There once was a cat named Professor Whiskers who firmly believed he was a certified engineer. Every morning, he’d knock over coffee mugs, sprawl across keyboards, and “redesign” his human’s spreadsheets with a single tail swipe. One day, he proudly sat on the printer and refused to move, convinced he was guarding top-secret blueprints. Despite being fired three times and banned from Zoom meetings, Professor Whiskers remained committed to his cause, engineering chaos, one paw at a time."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x500")
        self.root.configure(bg="#d63384")  # Dark pink background

        self.start_time = None
        self.selected_text = ""
        self.mode = tk.StringVar(value="sentence")

        self.setup_widgets()
        self.root.bind('<Return>', lambda event: self.check_typing())

    def setup_widgets(self):
        # --- Heading Label ---
        tk.Label(self.root, text="Typing Speed Tester", font=("Arial", 22, "bold"),
                 bg="#d63384", fg="#ffe6f0").pack(pady=10)

        # --- Mode selection: Sentence or Paragraph ---
        mode_frame = tk.Frame(self.root, bg="#d63384")
        mode_frame.pack()

        tk.Label(mode_frame, text="Choose Mode:", font=("Arial", 14),
                 bg="#d63384", fg="#ffe6f0").pack(side=tk.LEFT, padx=5)

        tk.Radiobutton(mode_frame, text="Sentence", variable=self.mode, value="sentence",
                       font=("Arial", 12), bg="#d63384", fg="#ffe6f0", selectcolor="#ffb6c1",
                       command=self.load_text).pack(side=tk.LEFT)
        tk.Radiobutton(mode_frame, text="Paragraph", variable=self.mode, value="paragraph",
                       font=("Arial", 12), bg="#d63384", fg="#ffe6f0", selectcolor="#ffb6c1",
                       command=self.load_text).pack(side=tk.LEFT)

        # --- Display selected text here ---
        self.display = tk.Label(self.root, text="", wraplength=600, font=("Arial", 14),
                                bg="#ffe6f0", fg="#d63384", justify="left", relief="solid", bd=1, padx=10, pady=10)
        self.display.pack(pady=15)

        # --- Text input area ---
        self.text_input = tk.Text(self.root, height=6, font=("Arial", 14), wrap=tk.WORD, fg="#d63384")
        self.text_input.pack(pady=10)
        self.text_input.bind("<FocusIn>", self.start_timer)

        # --- Submit button ---
        tk.Button(self.root, text="Submit", font=("Arial", 14), command=self.check_typing,
                  bg="#ffb6c1", fg="#d63384").pack(pady=10)

        # --- Result area ---
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#d63384", fg="#ffe6f0")
        self.result_label.pack()

        # --- Load the first text set ---
        self.load_text()

    def load_text(self):
        # Load a new sentence or paragraph depending on the selected mode
        if self.mode.get() == "sentence":
            self.selected_text = random.choice(sentences)
        else:
            self.selected_text = random.choice(paragraphs)

        self.display.config(text=self.selected_text)
        self.text_input.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None

    def start_timer(self, event):
        # Start the timer only once when typing starts
        if self.start_time is None:
            self.start_time = time.time()

    def check_typing(self):
        typed = self.text_input.get("1.0", tk.END).strip()
        if not self.start_time:
            messagebox.showinfo("Error", "Please start typing first.")
            return
        end_time = time.time()
        elapsed_time = round(end_time - self.start_time, 2)

        # Count character-level errors
        errors = sum(1 for a, b in zip(typed, self.selected_text) if a != b)
        errors += abs(len(typed) - len(self.selected_text))

        word_count = len(typed.split())
        wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0

        self.result_label.config(
            text=f"⏱ Time: {elapsed_time} seconds\n📄 Words Per Minute: {wpm:.2f}\n❌ Errors: {errors}"
        )

        self.start_time = None  # Reset for next round

# Run the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
