from PIL import Image, ImageTk

class Draw:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.images = []  # 이미지 참조 저장용

    def clear(self):
        self.canvas.delete("all")

    def rect(self, x, y, w, h, fill="black"):
        self.canvas.create_rectangle(x, y, x+w, y+h, fill=fill)

    def image(self, img_path, x=0, y=0):
        pil_image = Image.open(img_path)
        tk_image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(x, y, image=tk_image, anchor="nw")
        self.images.append(tk_image)  # 이미지 참조 유지

    def draw_text(self, canvas, x, y, txt, size=16, color="black"):
        fnt = ("Arial", size)
        canvas.create_text(x, y, text=txt, fill=color, font=fnt)

