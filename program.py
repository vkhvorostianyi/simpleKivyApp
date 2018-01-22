from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty


class Btn(Screen):
    pass


class Lb(Label):
    pass


class HeadTitle(Screen):
    pass


class MainView(Screen):
    pass


class TransactionScreen(Screen):
    pass


class InputWindow(Screen):
    pass


class Root(ScreenManager):
    pass



class StartScreen(Screen):
    pass


class CustomDropDown(BoxLayout):
    data = ListProperty()
    dropdown = ObjectProperty()
    def make_btn(self):
        for item in self.data:
            btn = Button(text='Value %d' % item, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)


class SimpleApp(App):

    def build(self):
        drop = CustomDropDown()
        drop.make_btn()
        app = Root()
        return app



if __name__ == '__main__':
    SimpleApp().run()
