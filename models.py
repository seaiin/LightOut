import arcade
import math
from random import randint

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = 'start'
        self.score = 0
        self.start_time = 0
        self.count_score = 5
        self.door_count = 8
        self.door_open = False
        self.bobby = Bobby(self, randint(50, 750), randint(50, 550))
        self.barrow1 = Barrow(self, randint(50, 750), randint(50, 550))
        self.barrow2 = Barrow(self, randint(50, 750), randint(50, 550))
        self.floor = Floor(self, 400, 300)
        self.fog = Fog(self, self.bobby.x, self.bobby.y)
        self.bookshelf = Bookshelf(self, 500, 300)

    def update(self, delta):
        self.bobby.update(delta)
        self.barrow1.update(delta)
        self.barrow2.update(delta)
        self.fog.update(delta)
        if self.score == self.count_score:
            self.door_open = True
        if self.bobby.touch_barrow or self.bobby.touch_door:
            self.bobby.direction = Bobby.DIR_STILL
            self.score = 0

    def on_key_press(self, key, key_modifiers):
        if self.state == 'start':
            if key == arcade.key.SPACE:
                self.state = 'game'
        elif self.state == 'game':
            if key == arcade.key.W:
                self.bobby.switch_direction(Bobby.DIR_UP)
            elif key == arcade.key.S:
                self.bobby.switch_direction(Bobby.DIR_DOWN)
            elif key == arcade.key.A:
                self.bobby.switch_direction(Bobby.DIR_LEFT)
            elif key == arcade.key.D:
                self.bobby.switch_direction(Bobby.DIR_RIGHT)
        elif self.state == 'over':
            if key == arcade.key.SPACE:
                self.state = 'start'

    # def on_key_release(self, key, key_modifiers):
        # if self.state == 'game':
            # if key == arcade.key.W or key == arcade.key.S or key == arcade.key.A or key == arcade.key.D:
                # self.bobby.switch_direction(Bobby.DIR_STILL)

class Bobby:
    DIR_STILL = 0
    DIR_UP = 1
    DIR_DOWN = 2
    DIR_LEFT = 3
    DIR_RIGHT = 4

    def __init__(self, world, x, y):
        self.world = World
        self.x = x
        self.y = y
        self.speed = 2.5
        self.angle = 0
        self.touch_obj = False
        self.touch_barrow = False
        self.touch_door = False
        self.direction = Bobby.DIR_STILL

    def switch_direction(self, direc):
        self.direction = direc

    def update(self, delta):
        if self.touch_barrow:
            self.direction = self.DIR_STILL
        else:
            if self.direction == Bobby.DIR_UP and self.y < 600:
                self.y += self.speed
            elif self.direction == Bobby.DIR_DOWN and self.y > 0:
                self.y -= self.speed
            elif self.direction == Bobby.DIR_LEFT and self.x > 0:
                self.x -= self.speed
            elif self.direction == Bobby.DIR_RIGHT and self.x < 800:
                self.x += self.speed

class Barrow:

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.speed = 1.25
        self.angle = 0

    def update(self, delta):
        self.dx = self.world.bobby.x - self.x
        self.dy = self.world.bobby.y - self.y
        self.dist = math.hypot(self.dx, self.dy)
        self.dx = self.dx / self.dist
        self.dy = self.dy / self.dist
        if self.dist <= 400:
            self.x += self.dx * self.speed
            self.y += self.dy * self.speed

class Floor:

    def __init__(self, world, x, y):
        self.world = World
        self.x = x
        self.y = y
        self.angle = 0

class Bookshelf:

    def __init__(self, world, x, y):
        self.world = World
        self.x = x
        self.y = y
        self.angle = 0

class Fog:

    def __init__(self, world, x, y):
        self.world = World
        self.bobby = world.bobby
        self.x = self.bobby.x
        self.y = self.bobby.y
        self.angle = 0

    def update(self, delta):
        self.x = self.bobby.x
        self.y = self.bobby.y
