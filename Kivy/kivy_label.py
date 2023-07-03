import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Surname: '))
        self.surname = TextInput(multiline=False)
        self.inside.add_widget(self.surname)

        self.inside.add_widget(Label(text='Year of birth: '))
        self.year_of_birth = TextInput(multiline=False)
        self.inside.add_widget(self.year_of_birth)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=42)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('You have pushed the button')
        name = self.name.text
        surname = self.surname.text
        year_of_birth = self.year_of_birth.text
        print(f'Name: {name}\nSurname: {surname}\nYear of birth: {year_of_birth}')




class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()
