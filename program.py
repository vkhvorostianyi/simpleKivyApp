from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App


class InputWindow(BoxLayout):
    pass


class Root(BoxLayout):
    pass


class SimpleApp(App):

    def build(self):
        app = Root()
        return app


if __name__ == '__main__':
    SimpleApp().run()
