from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


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

class SimpleApp(App):

    def build(self):
        app = Root()
        return app



if __name__ == '__main__':
    SimpleApp().run()
