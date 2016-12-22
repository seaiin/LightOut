import arcade

class Timer:

    def __init__ (self, time):
        self.world = World
        self.time = 0
    def timer(self, delta, endtime):
        self.time = self.time + delta
        if time == endtime:
            return 1

class Bobby:
    POS_STILL = 10
    POS_WALK = 11
    DIR_FACE = 0
    DIR_BACK = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Bobby.DIR_FACE
        self.angle = 0
        self.speed = 2

    def switch_direction(self, direc):
        self.direction = direc

    def animate(self, delta):
        if self.direction == Bobby.DIR_BACK and self.y > 0:
            self.y = self.y + self.speed
        elif self.direction == Bobby.DIR_FACE and self.y < self.world.height:
            self.y = self.y - self.speed
        elif self.direction == Bobby.DIR_LEFT and self.x < self.world.width:
            self.x = self.x - self.speed
        elif self.direction == Bobby.DIR_RIGHT and self.x > 0:
            self.x = self.x + self.speed

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.bobby = Bobby(self, 100, 100)

    def animate(self, delta):
        self.bobby.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.bobby.switch_direction(self.bobby.DIR_BACK)
        elif key == arcade.key.S:
            self.bobby.switch_direction(self.bobby.DIR_FACE)
        elif key == arcade.key.A:
            self.bobby.switch_direction(self.bobby.DIR_LEFT)
        elif key == arcade.key.D:
            self.bobby.switch_direction(self.bobby.DIR_RIGHT)
