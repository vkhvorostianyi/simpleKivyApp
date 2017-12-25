from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.layout import Layout
from kivy.properties import ObjectProperty

class Root(Widget):
    pass

class InputForm(Layout):
    pass
    form = ObjectProperty(None)

class SimpleApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    SimpleApp().run()