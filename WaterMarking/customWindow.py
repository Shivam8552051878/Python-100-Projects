import glob
from tkinter import colorchooser
from tkinter import filedialog

import PIL.Image
from PIL.ImageFont import ImageFont


class HelpFunc():
    def __init__(self):
        self.image_paths = []


    def fonts(self):
        return glob.glob("C://Windows/Fonts/*.ttf")

    def select_multi_images(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            for file_path in file_paths:
                self.image_paths.append(file_path)

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



