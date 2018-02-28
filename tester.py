from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from wallet_app import  *
from kivy.uix.widget import Widget

a = Category('test',True)
data = dict(test_item = a)

class MyGrid(BoxLayout):
    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.data = []
        self.drop_down = DropDown()
        self.btn_name = Button(text="set the text", size_hint=(.5, None))
        self.redraw()

    def redraw(self):
        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=self.btn_name.height)
            btn.bind(on_release=lambda btn=btn,drop_down=self.drop_down:drop_down.select(btn.text))
            self.drop_down.add_widget(btn)
        else:
            self.build_func()
        self.btn_name.bind(on_release=self.drop_down.open)
        self.drop_down.bind(on_select=lambda instance, x, btn=self.btn_name: setattr(btn, 'text', x))
        self.add_widget(self.btn_name)

    def build_func(self):

        btn = Button(text='add...', size_hint_y=None, height=self.btn_name.height)
        btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(''))
        self.drop_down.add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.btn_name.height)
        del_btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(''))
        self.drop_down.add_widget(del_btn)

class Root(BoxLayout):
    pass


class MyChild(MyGrid):
    sel = [str(i) for i in range(0,5,1)]


class SecChild(MyGrid):
    pass


class Separator(Widget):
    pass


class testApp(App):
    def build(self):
        return Root()

if __name__=="__main__":
    testApp().run()
