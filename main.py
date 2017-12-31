from kivy.app import App
from kivy.uix.widget import Widget


class InputWindow(Widget):
    pass


class Root(Widget):
    pass


class SimpleApp(App):

    def build(self):
        return Root()


if __name__ == '__main__':
    SimpleApp().run()
