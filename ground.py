from pico2d import *


class Ground:
    def __init__(self):
        self.image = load_image('big_ground.PNG')

    def update(self):
        pass

    def draw(self):
        self.image.draw(160, 32)
        # self.image.draw(800, 30)
