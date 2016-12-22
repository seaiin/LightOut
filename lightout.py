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

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width, height)
        self.bobby_sprite = ModelSprite('images/bobby_face_still.png', model=self.world.bobby)
        self.wall_sprite = ModelSprite('images/floor.png', model=self.world.wall)
        self.flog_sprite = ModelSprite('images/flog.png', model=self.world.flog)

    def on_draw(self):
        arcade.start_render()
        self.wall_sprite.draw()
        self.bobby_sprite.draw()
        self.flog_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    # def on_key_release(self, key, key_modifiers):
        # self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
