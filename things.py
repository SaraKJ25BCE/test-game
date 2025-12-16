from conf import *

class Meteor:
    def __init__(self):
        self.p = (0,0)
        self.color = METEOR_COLOR
        self.size = 0
        self.vertices_num = 3
        self.vertices = []
        self.spin = ANGULAR_VELOCITY_METEOR


class Blaster:
    def __init__(self):
        self.p = (0,0)
        self.color = BLASTER_COLOR
        self.size = 0


class Spaceship:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0


class Explosion:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0
        self.conc = 0


class Enemy:
    def __init__(self):
        self.p = (0,0)
        self.color = (0,0,0)
        self.size = 0
