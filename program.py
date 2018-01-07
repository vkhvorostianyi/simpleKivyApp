from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty


class InputWindow(BoxLayout):
    pass


class Root(Widget):
    pass

class StartScreen(BoxLayout):
    pass


class SimpleApp(App):

    def build(self):
        app = Root()
        return app


if __name__ == '__main__':
    SimpleApp().run()
