from pico2d import load_image, get_time, load_font

import game_world
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.3)

FLY_SPEED_KMPH = 10.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, speed = 100):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = random.randint(0, 1600), random.randint(300, 600)
        self.frame = 0
        self.face_dir = 1
        self.dir = 1

    def update(self):
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x < 0:
            self.x = 0
            self.dir = 1
            self.face_dir = 1
        elif self.x > 1600:
            self.x = 1600
            self.dir = -1
            self.face_dir = -1

        self.frame = (self.frame + 1) % 14

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * 183, 506 - (int(self.frame) // 5) * 168, 183, 168, self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183, 506 - (int(self.frame) // 5) * 168, 183, 168, 0, 'h', self.x, self.y, 50, 50)

        self.font.draw(self.x - 60, self.y + 50, f'(Speed: {FLY_SPEED_PPS:.2f})', (255, 255, 0))
