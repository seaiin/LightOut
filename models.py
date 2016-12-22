import arcade

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
        self.direction = Bobby.DIR_STILL
        self.speed = 2
        self.angle = 0

    def switch_direction(self, direc):
        self.direction = direc

    def animate(self, delta):
            if self.direction == Bobby.DIR_UP and self.y > 0:
                self.y = self.y + self.speed
            elif self.direction == Bobby.DIR_DOWN and self.y < 800:
                self.y = self.y - self.speed
            elif self.direction == Bobby.DIR_LEFT and self.x < 600:
                self.x = self.x - self.speed
            elif self.direction == Bobby.DIR_RIGHT and self.x > 0:
                self.x = self.x + self.speed

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.time = 0
        self.bobby = Bobby(self, 100, 100)
        self.wall = Wall(self, 400, 300)
        self.flog = Flog(self, 100, 100)

    def animate(self, delta):
        self.bobby.animate(delta)

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

class Wall:

    def __init__(self, world, x, y):
        self.world = World
        self.x = x
        self.y = y
        self.angle = 0

class Flog:

    def __init__(self, world, x, y):
        self.world = World
        self.bobby = self.world.bobby
        self.x = self.world.bobby.x
        self.y = self.world.bobby.y
        self.angle = 0

    def animate(self, delta):
        self.x = self.world.bobby.x
        self.y = self.world.bobby.y
