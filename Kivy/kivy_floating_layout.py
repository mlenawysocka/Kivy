import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class My5floatingApp(App):
    def build(self):
        return FloatLayout()

if __name__ == '__main__':
    My5floatingApp().run()