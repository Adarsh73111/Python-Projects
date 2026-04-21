import tkinter as tk


class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        self.root.geometry("800x600")

        self.timer = None
        self.timeout = 5000

        self.title_label = tk.Label(root, text="Keep typing! Don't stop for more than 5 seconds...",
                                    font=("Helvetica", 18, "bold"), fg="#d32f2f")
        self.title_label.pack(pady=20)

        self.text_area = tk.Text(root, font=("Helvetica", 14), wrap="word", padx=10, pady=10)
        self.text_area.pack(expand=True, fill="both", padx=40, pady=20)
        self.text_area.focus()

        self.text_area.bind("<KeyPress>", self.reset_timer)

    def reset_timer(self, event):
        if self.timer is not None:
            self.root.after_cancel(self.timer)

        self.timer = self.root.after(self.timeout, self.clear_text)

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.timer = None


if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()