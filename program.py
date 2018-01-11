# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class HeadTitle(Screen):
    pass


class MyBtn(Screen):
    pass


class TransactionScreen(Screen):
    pass


class InputWindow(Screen):
    pass


class Root(ScreenManager):
    pass
    # start_screen = ObjectProperty()
    # transaction_window = ObjectProperty()
    # head_title = ObjectProperty()


class StartScreen(Screen):
    pass


class SimpleApp(App):

    def build(self):
        app = Root()
        return app


if __name__ == '__main__':
    SimpleApp().run()
