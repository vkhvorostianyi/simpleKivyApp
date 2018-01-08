from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty


class HeadTitle(GridLayout):
    pass


class InputWindow(Widget):
    pass


class Root(Widget):
    start_screen = ObjectProperty()
    transaction_window = ObjectProperty()
    head_title = ObjectProperty()


class StartScreen(BoxLayout):
    pass


class SimpleApp(App):

    def build(self):
        app = Root()
        return app


if __name__ == '__main__':
    SimpleApp().run()
