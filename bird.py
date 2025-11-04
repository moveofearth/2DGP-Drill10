from pico2d import load_image, get_time, load_font

import game_world
import game_framework
import random

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, speed = 100):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = random.randint(0, 1600), random.randint(300, 600)
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.speed = float(random.randint(50, 150))

