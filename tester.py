from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from wallet_app import  *
from kivy.uix.widget import Widget


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.redraw()

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]

    def redraw(self):

        self.clear_widgets()
        # self.cols =1

        drpName = []
        dd = DropDown()
        drpName.append(dd)
        btnName = Button(text="B", size_hint=(None, None))
        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btnName.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[0]:dropdown.select(btn.text))
            drpName[0].add_widget(btn)
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)

class Root(BoxLayout):
    pass


class MyChild(MyGrid):
    # def __init__(self,**kwargs):
        # super(MyChild,self).__init__(**kwargs)
        # self.redraw()
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
