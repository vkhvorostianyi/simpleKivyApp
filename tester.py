from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from wallet_app import  *
from kivy.uix.widget import Widget


class MyGrid(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
        self.dd1 = DropDown()
        self.dd2 = DropDown()
        self.drpName = []
        self.drpName.append(self.dd1)
        self.drpName.append(self.dd2)
        self.btnName = Button(text="choose account", size_hint=(.5, None))
        self.BtnCat = Button(text="choose category", size_hint=(.5, None))
        self.redraw()
    def redraw(self):
        #
        # drpName = []
        # dd1 = DropDown()
        # dd2 = DropDown()
        # drpName.append(dd1)
        # drpName.append(dd2)
        # btnName = Button(text="choose account", size_hint=(.5, None))
        # BtnCat = Button(text="choose category", size_hint=(.5, None))

        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=self.BtnCat.height)
            btn.bind(on_release=lambda btn=btn,dropdown=self.drpName[1]:dropdown.select(btn.text))
            self.drpName[1].add_widget(btn)
        else:
            self.build_func()
        self.BtnCat.bind(on_release=self.drpName[1].open)
        self.drpName[1].bind(on_select=lambda instance, x, btn=self.BtnCat: setattr(btn, 'text', x))
        self.add_widget(self.BtnCat)

    def build_func(self):

        btn = Button(text='add...', size_hint_y=None, height=self.BtnCat.height)
        btn.bind(on_release=lambda btn=btn, dropdown=self.drpName[1]: dropdown.select('choose category'))
        # btn.bind(on_press = self.call_cat_add_btn)
        self.drpName[1].add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.BtnCat.height)
        del_btn.bind(on_release=lambda btn=btn, dropdown=self.drpName[1]: dropdown.select("choose category"))
        # del_btn.bind(on_press=self.call_del_cat)
        self.drpName[1].add_widget(del_btn)

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
