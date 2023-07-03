import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1, mode='rgba')
            self.rect1 = Rectangle(pos=(0, 0), size=(50, 50))
            Color(1, 0, 0, 1, mode='rgba')
            self.rect2 = Rectangle(pos=(100, 100), size=(80, 80))
            Color(1, 0, 0, 1, mode='rgba')
            self.rect3 = Rectangle(pos=(200, 400), size=(140, 50))

    def on_touch_down(self, touch):
        self.rect1.pos = touch.pos
        x = touch.pos[0] - 40
        y = touch.pos[1] - 40
        self.rect2.pos = (x, y)
        print("Mouse down ", touch)

    def on_touch_move(self, touch):
        self.rect3.pos = touch.pos
        print("Mouse move ", touch)


class My7drawingApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    My7drawingApp().run()
