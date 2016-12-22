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
        self.bobby_sprite = ModelSprite('images/bobby_face_still.png', model=self.world.bobby)
        self.floor_sprite = ModelSprite('images/floor.png', model=self.world.floor)
        self.fog_sprite = ModelSprite('images/fog.png', model=self.world.fog)
        self.bookshelf_sprite = ModelSprite('images/bookshelf.png', model=self.world.bookshelf)

    def on_draw(self):
        arcade.start_render()
        self.floor_sprite.draw()
        self.bookshelf_sprite.draw()
        self.bobby_sprite.draw()
        self.fog_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    # def on_key_release(self, key, key_modifiers):
        # self.world.on_key_release(key, key_modifiers)

    def check_touch(self):
        if arcade.check_for_collision(self.bobby_sprite, self.bookshelf_sprite):
            self.world.check_touch = True
        else:
            self.world.check_touch = False

if __name__ == '__main__':
    window = LightOutWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
