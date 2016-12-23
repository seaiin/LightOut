import arcade
from random import randint
from models import World, Bobby

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class LightOutWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width, height)
        self.time = 0
        self.start1_sprite = arcade.Sprite('images/start1.png', 1)
        self.start1_sprite.center_x = width/2
        self.start1_sprite.center_y = height/2
        self.start2_sprite = arcade.Sprite('images/start2.png', 1)
        self.start2_sprite.center_x = width/2
        self.start2_sprite.center_y = height/2
        self.key_icon_sprite = arcade.Sprite('images/key.png', 2)
        self.key_icon_sprite.center_x = 50
        self.key_icon_sprite.center_y = 550
        self.key_sprite_list = arcade.SpriteList()
        self.crete_key()
        self.door_close_sprite_list = arcade.SpriteList()
        self.door_open_sprite_list = arcade.SpriteList()
        self.crete_door()
        self.bobby_sprite = ModelSprite('images/bobby_face_still.png', model=self.world.bobby)
        self.bobby_dead_sprite = ModelSprite('images/bobby_dead.png', model=self.world.bobby)
        self.floor_sprite = ModelSprite('images/floor.png', model=self.world.floor)
        self.fog_sprite = ModelSprite('images/fog.png', model=self.world.fog)
        self.bookshelf_sprite = ModelSprite('images/bookshelf.png', model=self.world.bookshelf)
        self.barrow1_sprite = ModelSprite('images/barrow.png', model=self.world.barrow1)
        self.barrow2_sprite = ModelSprite('images/barrow.png', model=self.world.barrow2)

    def on_draw(self):
        arcade.start_render()
        if self.world.state == 'start':
            self.start1_sprite.draw()
            if self.time >= 0.5:
                self.start2_sprite.draw()
            if self.time >= 1:
                self.time = 0
        elif self.world.state == 'game':
            self.floor_sprite.draw()
            self.bookshelf_sprite.draw()
            if self.world.door_open:
                self.door_open_sprite_list.draw()
            else:
                self.door_close_sprite_list.draw()
            if self.world.bobby.touch_barrow:
                self.bobby_dead_sprite.draw()
            else:
                self.bobby_sprite.draw()
            self.key_sprite_list.draw()
            self.barrow1_sprite.draw()
            self.barrow2_sprite.draw()
            self.fog_sprite.draw()
            self.key_icon_sprite.draw()
            arcade.draw_text(str(self.world.score) + " / " + str(self.world.count_score), 75, 545, arcade.color.WHITE, 15)

    def animate(self, delta):
        self.time += delta
        if self.world.state == 'game':
            self.world.start_time += delta
            self.world.animate(delta)
            self.touch_key()
            self.touch_door()
            self.touch_barrow()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def crete_key(self):
        for i in range(self.world.count_score):
            key = arcade.Sprite('images/key.png', 1)
            key.center_x = randint(50, 750)
            key.center_y = randint(50, 550)
            self.key_sprite_list.append(key)

    def crete_door(self):
        self.door_x = []
        self.door_y = []
        for i in range(self.world.door_count):
            self.door_x.append(randint(50, 750))
            self.door_y.append(randint(50, 550))
        for i in range(int(self.world.door_count/2)):
            door_close = arcade.Sprite('images/door_close.png', 1)
            door_open = arcade.Sprite('images/door_open.png', 1)
            if i <= 1:
                door_close.center_x = self.door_x[i]
                door_close.center_y = 16
                door_open.center_x = self.door_x[i]
                door_open.center_y = 16
            if i > 1:
                door_close.center_x = self.door_x[i]
                door_close.center_y = 584
                door_open.center_x = self.door_x[i]
                door_open.center_y = 584
            self.door_close_sprite_list.append(door_close)
            self.door_open_sprite_list.append(door_open)
        for i in range(int(self.world.door_count/2)):
            door_close = arcade.Sprite('images/door_close.png', 1)
            door_open = arcade.Sprite('images/door_open.png', 1)
            if i <= 1:
                door_close.center_x = 20
                door_close.center_y = self.door_y[i]
                door_open.center_x = 20
                door_open.center_y = self.door_y[i]
            if i > 1:
                door_close.center_x = 780
                door_close.center_y = self.door_y[i]
                door_open.center_x = 780
                door_open.center_y = self.door_y[i]
            self.door_close_sprite_list.append(door_close)
            self.door_open_sprite_list.append(door_open)

    def touch_key(self):
        for key in self.key_sprite_list:
            if arcade.check_for_collision(self.bobby_sprite, key):
                key.kill()
                self.world.score = self.world.score + 1

    def touch_door(self):
        for door in self.door_open_sprite_list:
            if arcade.check_for_collision(self.bobby_sprite, door) and self.world.door_open:
                self.world.bobby.touch_door = True

    def touch_barrow(self):
        if arcade.check_for_collision(self.bobby_sprite, self.barrow1_sprite) or arcade.check_for_collision(self.bobby_sprite, self.barrow2_sprite):
            if self.world.start_time >= 3:
                self.world.bobby.touch_barrow = True

if __name__ == '__main__':
    window = LightOutWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
