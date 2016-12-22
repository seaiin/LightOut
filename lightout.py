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
        self.count_key = 5
        self.bobby_sprite = ModelSprite('images/bobby_face_still.png', model=self.world.bobby)
        self.floor_sprite = ModelSprite('images/floor.png', model=self.world.floor)
        self.fog_sprite = ModelSprite('images/fog.png', model=self.world.fog)
        self.bookshelf_sprite = ModelSprite('images/bookshelf.png', model=self.world.bookshelf)
        self.key_icon_sprite = arcade.Sprite('images/key.png', 2)
        self.key_icon_sprite.center_x = 50
        self.key_icon_sprite.center_y = 550
        self.key_sprite_list = arcade.SpriteList()
        self.crete_key()

    def on_draw(self):
        arcade.start_render()
        self.floor_sprite.draw()
        self.bookshelf_sprite.draw()
        self.bobby_sprite.draw()
        self.key_sprite_list.draw()
        self.fog_sprite.draw()
        self.key_icon_sprite.draw()
        arcade.draw_text(str(self.world.score) + " / " + str(self.count_key), 75, 545, arcade.color.WHITE, 15)

    def animate(self, delta):
        self.world.animate(delta)
        self.touch_key()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def crete_key(self):
        self.key_x = [100, 10, 450, 300, 700]
        self.key_y = [600, 400, 200, 800, 100]
        for i in range(self.count_key):
            key = arcade.Sprite('images/key.png', 1)
            key.center_x = self.key_x[i]
            key.center_y = self.key_y[i]
            self.key_sprite_list.append(key)

    def touch_key(self):
        for key in self.key_sprite_list:
            if arcade.check_for_collision(self.bobby_sprite, key):
                key.kill()
                self.world.score = self.world.score + 1

if __name__ == '__main__':
    window = LightOutWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
