import arcade
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
        self.bobby_sprite = ModelSprite('images/bobby_face_still.png', model=self.world.bobby)
        self.bobby_dead_sprite = ModelSprite('images/bobby_dead.png', model=self.world.bobby)
        self.floor_sprite = ModelSprite('images/floor.png', model=self.world.floor)
        self.fog_sprite = ModelSprite('images/fog.png', model=self.world.fog)
        self.bookshelf_sprite = ModelSprite('images/bookshelf.png', model=self.world.bookshelf)
        self.barrow_sprite = ModelSprite('images/barrow.png', model=self.world.barrow)

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
            if self.world.bobby.touch_barrow:
                self.bobby_dead_sprite.draw()
            else:
                self.bobby_sprite.draw()
            self.barrow_sprite.draw()
            self.key_sprite_list.draw()
            self.fog_sprite.draw()
            self.key_icon_sprite.draw()
            arcade.draw_text(str(self.world.score) + " / " + str(self.world.count_score), 75, 545, arcade.color.WHITE, 15)

    def animate(self, delta):
        if self.world.state == 'game':
            self.world.animate(delta)
            self.touch_key()
            self.touch_barrow()
            self.time = self.time + delta

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def crete_key(self):
        self.key_x = [100, 100, 450, 300, 700]
        self.key_y = [399, 400, 200, 250, 100]
        for i in range(self.world.count_score):
            key = arcade.Sprite('images/key.png', 1)
            key.center_x = self.key_x[i]
            key.center_y = self.key_y[i]
            self.key_sprite_list.append(key)

    def touch_key(self):
        for key in self.key_sprite_list:
            if arcade.check_for_collision(self.bobby_sprite, key):
                key.kill()
                self.world.score = self.world.score + 1
    def touch_barrow(self):
        if arcade.check_for_collision(self.bobby_sprite, self.barrow_sprite):
            self.world.bobby.touch_barrow = True

if __name__ == '__main__':
    window = LightOutWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
