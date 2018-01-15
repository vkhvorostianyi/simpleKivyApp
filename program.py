from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label


list_item_args_converter = lambda row_index, obj: {'text': obj, 'size_hint_y': None, 'height': 210}


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


class SimpleApp(App):

    def build(self):
        app = Root()
        return app


if __name__ == '__main__':
    SimpleApp().run()
