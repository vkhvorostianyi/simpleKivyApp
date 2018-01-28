from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from wallet_app import  *



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.redraw()

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
    test = 'a', 'b', 'c'
    def redraw(self):

        self.clear_widgets()
        self.rows = 5
        self.cols =2

        drpName = []
        drpName.append(DropDown())
        drpName.append(DropDown())
        btnName = Button(text="B", size_hint=(None, None))
        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btnName.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[0]:dropdown.select(btn.text))
            drpName[0].add_widget(btn)
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)

class testApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    testApp().run()
