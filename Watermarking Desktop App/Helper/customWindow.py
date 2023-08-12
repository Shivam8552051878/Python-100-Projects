import glob
from tkinter import colorchooser
from tkinter import filedialog

import PIL.Image
from PIL.ImageFont import ImageFont


class HelpFunc():
    # def __init__(self):
    #     super().__init__()
    #     self.image_paths = []
    #     self.logo_image_path = None
    #     self.fonts = self.fonts()
    #     self.title("Watermarking Desktop App")
    #     self.config(width=600, height=600, bg="lightblue")
    #     self.add_text_image = tkinter.Button(text="Add text watermark", command=lambda : self.show_page(2))
    #     self.add_logo_image = tkinter.Button(text="Add logo to image", command=lambda : self.show_page(1))
    #     self.upload_multiple_image = tkinter.Button(text="Upload Images", command=self.select_multi_images)
    #     self.upload_single_image = tkinter.Button(text="Upload Logo", command=self.select_single_image)
    #     self.label_data = tkinter.Label(text="hello")
    #     self.startfrom = tkinter.Entry()
    #     self.show_page(1)
    #     self.mainloop()

    def fonts(self):
        return glob.glob("C://Windows/Fonts/*.ttf")

    def select_multi_images(self):
        image_paths = []
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            for file_path in file_paths:
                image_paths.append(file_path)
        return image_paths

    def select_single_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            return file_path

    def add_text(self, img, startfrom, steps, text, color=(0, 0, 0), font_name="Swis721 Blk BT Black.ttf",
                 font_size=10):
        font = ImageFont.truetype(font_name, size=font_size)
        draw_img = PIL.ImageDraw(img)
        for i in range(startfrom, img.size[0], steps):
            for j in range(startfrom, img.size[1], steps):
                draw_img.multiline_text((i, j), text=text, fill=color, font=font)
        return img

    def add_logo(self, img, startfrom, steps, log_img_path, logo_width, logo_hight):
        log_img = self.image(log_img_path)
        log_img.resize((logo_width, logo_hight))
        for i in range(startfrom, img.size[0], steps):
            for j in range(startfrom, img.size[1], steps):
                img.paste(log_img, (i, j))
        return img

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        return color_code[0]



