
from kivy.uix.widget import Widget
from kivy.app import App



class InputWindow(Widget):
    pass


class Root(Widget):
    pass



class SimpleApp(App):

    def build(self):
        return InputWindow()


if __name__ == '__main__':
    SimpleApp().run()
