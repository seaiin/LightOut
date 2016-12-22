import arcade

class Ship:
    DIR_HOIZONTAL = 0
    DIR_VERTICAL = 1

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Ship.DIR_VERTICAL
        self.angle = 0

    def switch_direction(self):
        if self.direction == Ship.DIR_HOIZONTAL:
            self.direction = Ship.DIR_VERTICAL
            self.angle = 0
        else :
            self.direction = Ship.DIR_HOIZONTAL
            self.angle = -90

    def animate(self, delta):
        if self.direction == Ship.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            # self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            # self.x += 5

class Gold:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ship = Ship(self, 100, 100)

    def animate(self, delta):
        self.ship.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()
