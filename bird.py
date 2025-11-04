from pico2d import load_image, get_time, load_font

import game_world
import game_framework
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


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

    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 0:
            self.x = 0
            self.dir = 1
            self.face_dir = 1
        elif self.x > 1600:
            self.x = 1600
            self.dir = -1
            self.face_dir = -1

        self.frame = (self.frame + 1) % 14
