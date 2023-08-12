import random


class ChangeColor:
    def __int__(self):
        self.red = 255
        self.green = 0
        self.blue = 0

    def random_rgb_color(self):
        self.red = random.randint(255)
        self.green = random.randint(255)
        self.blue = random.randint(255)
        rgb = (self.red, self.green, self.blue)
        return rgb
   