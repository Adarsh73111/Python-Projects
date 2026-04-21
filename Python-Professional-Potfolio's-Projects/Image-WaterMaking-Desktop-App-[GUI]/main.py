import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Desktop App")
        self.root.geometry("500x600")

        self.image_path = None
        self.tk_image = None

        self.upload_btn = tk.Button(root, text="Upload Image", font=("Arial", 12), command=self.upload_image)
        self.upload_btn.pack(pady=20)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="#e0e0e0", highlightthickness=1,
                                highlightbackground="gray")
        self.canvas.pack()

        self.text_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.text_entry.insert(0, "Enter Watermark Text")
        self.text_entry.pack(pady=20)

        self.apply_btn = tk.Button(root, text="Apply Watermark & Save", font=("Arial", 12, "bold"), bg="#4caf50",
                                   fg="white", command=self.apply_watermark)
        self.apply_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(self.image_path)
            img.thumbnail((400, 400))
            self.tk_image = ImageTk.PhotoImage(img)
            self.canvas.delete("all")
            self.canvas.create_image(200, 200, image=self.tk_image)

    def apply_watermark(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        watermark_text = self.text_entry.get()
        if not watermark_text or watermark_text == "Enter Watermark Text":
            messagebox.showerror("Error", "Please enter valid watermark text.")
            return

        try:
            img = Image.open(self.image_path).convert("RGBA")
            txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))

            draw = ImageDraw.Draw(txt_layer)

            font_size = max(int(img.width / 15), 10)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x = img.width - text_width - 20
            y = img.height - text_height - 20

            draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)

            watermarked_img = Image.alpha_composite(img, txt_layer)
            watermarked_img = watermarked_img.convert("RGB")

            save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                     filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])

            if save_path:
                watermarked_img.save(save_path)
                messagebox.showinfo("Success", "Watermarked image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()