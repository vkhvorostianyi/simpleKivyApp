from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App


class InputWindow(Widget):
    pass


class Root(BoxLayout):
    pass


class SimpleApp(App):

    def build(self):
        root = Root()
        return root


if __name__ == '__main__':
    SimpleApp().run()
