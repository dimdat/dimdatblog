import os
import pyglet

from pyglet.sprite import Sprite
from pyglet.gl import glClearColor
from pyglet.window import (
    Window,
    # key
)

IMAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')


class Character():
    def __init__(self):
        self.x = 400
        self.y = 400
        self.moving = False
        self.move_x = 0
        self.move_y = 0
        self.speed = 5
        self.sprite = Sprite(
            pyglet.image.load(os.path.join(IMAGE_DIR, 'archer.png')),
            self.x, self.y
        )

    def move(self, x, y):
        self.moving = True
        self.move_x = x
        self.move_y = y

    def update(self):
        if self.moving:
            diff_x = (self.x - self.move_x)
            diff_y = (self.y - self.move_y)
            diff_sum = abs(diff_x) + abs(diff_y)
            if diff_sum < 5.5:
                self.x = self.move_x
                self.y = self.move_y
                self.moving = False
            else:
                mx = self.speed * float(diff_x / diff_sum)
                my = self.speed * float(diff_y / diff_sum)
                self.x -= mx
                self.y -= my
            self.sprite.x = self.x
            self.sprite.y = self.y


def update(ts):
    player.update()

window = Window(800, 800)
glClearColor(.8, .8, .8, 1)
player = Character()


@window.event
def on_mouse_release(x, y, button, modifiers):
    player.move(x, y)


@window.event
def on_draw():
    window.clear()
    player.sprite.draw()


if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()
