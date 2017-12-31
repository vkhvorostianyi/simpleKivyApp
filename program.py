
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class InputWindow(Widget):
    pass


class Root(Widget):
    obj = ObjectProperty(None)


class SimpleApp(App):

    def build(self):
        return Root()


if __name__ == '__main__':
    SimpleApp().run()
