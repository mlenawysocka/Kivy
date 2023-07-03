import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty()
    surname = ObjectProperty()
    year = ObjectProperty()

    def btn(self):
        print(f'{self.name.text} {self.surname.text} {self.year.text}')

class My4App(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    My4App().run()