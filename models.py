import arcade

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bobby = Bobby(self, 100, 100)
        self.floor = Floor(self, 400, 300)
        self.fog = Fog(self, 100, 100)
        self.bookshelf = Bookshelf(self, 500, 300)

    def animate(self, delta):
        self.bobby.animate(delta)
        self.fog.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.bobby.switch_direction(Bobby.DIR_UP)
        elif key == arcade.key.S:
            self.bobby.switch_direction(Bobby.DIR_DOWN)
        elif key == arcade.key.A:
            self.bobby.switch_direction(Bobby.DIR_LEFT)
        elif key == arcade.key.D:
            self.bobby.switch_direction(Bobby.DIR_RIGHT)

    # def on_key_release(self, key, key_modifiers):
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
        self.speed = 2
        self.angle = 0
        self.direction = Bobby.DIR_STILL

    def switch_direction(self, direc):
        self.direction = direc

    def animate(self, delta):
            if self.direction == Bobby.DIR_UP and self.y < 600:
                self.y = self.y + self.speed
            elif self.direction == Bobby.DIR_DOWN and self.y > 0:
                self.y = self.y - self.speed
            elif self.direction == Bobby.DIR_LEFT and self.x > 0:
                self.x = self.x - self.speed
            elif self.direction == Bobby.DIR_RIGHT and self.x < 800:
                self.x = self.x + self.speed

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
        self.box = [self.x + 15, self.x - 30, self.y + 30, self.y - 30]

class Fog:

    def __init__(self, world, x, y):
        self.world = World
        self.bobby = world.bobby
        self.x = self.bobby.x
        self.y = self.bobby.y
        self.angle = 0

    def animate(self, delta):
        self.x = self.bobby.x
        self.y = self.bobby.y
