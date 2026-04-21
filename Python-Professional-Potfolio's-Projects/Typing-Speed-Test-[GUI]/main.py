import tkinter as tk
import random

sample_texts = [
    "The quick brown fox jumps over the lazy dog. Programming is the art of algorithm design and the craft of debugging errant code.",
    "To be or not to be, that is the question. Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune.",
    "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability."
]


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")

        self.time_left = 60
        self.timer_running = False
        self.current_text = random.choice(sample_texts)

        self.title_label = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        self.sample_label = tk.Label(root, text=self.current_text, font=("Helvetica", 14), wraplength=700,
                                     justify="center")
        self.sample_label.pack(pady=20)

        self.input_text = tk.Text(root, height=5, width=60, font=("Helvetica", 14), state='disabled')
        self.input_text.pack(pady=20)
        self.input_text.bind("<KeyRelease>", self.check_start)

        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=20)

        self.timer_label = tk.Label(self.info_frame, text=f"Time left: {self.time_left}s", font=("Helvetica", 14))
        self.timer_label.grid(row=0, column=0, padx=20)

        self.wpm_label = tk.Label(self.info_frame, text="WPM: 0", font=("Helvetica", 14))
        self.wpm_label.grid(row=0, column=1, padx=20)

        self.cpm_label = tk.Label(self.info_frame, text="CPM: 0", font=("Helvetica", 14))
        self.cpm_label.grid(row=0, column=2, padx=20)

        self.reset_btn = tk.Button(root, text="Start / Reset", font=("Helvetica", 14), command=self.reset_app)
        self.reset_btn.pack(pady=10)

    def check_start(self, event):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.input_text.config(state='disabled')
            self.calculate_results()

    def calculate_results(self):
        typed_words = self.input_text.get("1.0", tk.END).strip()
        if not typed_words:
            return

        typed_chars = len(typed_words)
        cpm = typed_chars
        wpm = round(typed_chars / 5)

        self.cpm_label.config(text=f"CPM: {cpm}")
        self.wpm_label.config(text=f"WPM: {wpm}")

    def reset_app(self):
        self.timer_running = False
        self.time_left = 60
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        self.wpm_label.config(text="WPM: 0")
        self.cpm_label.config(text="CPM: 0")

        self.current_text = random.choice(sample_texts)
        self.sample_label.config(text=self.current_text)

        self.input_text.config(state='normal')
        self.input_text.delete("1.0", tk.END)
        self.input_text.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()