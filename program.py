from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from wallet_app import  *

class Btn(Screen):
    pass


class Lb(Label):
    pass


class HeadTitle(Screen):
    pass


class MainView(Screen):
    pass


class TransactionScreen(Screen):
    pass


class InputWindow(Screen):
    pass


class Root(ScreenManager):
    pass



class StartScreen(Screen):
    pass




class MyDrop(GridLayout):
    def __init__(self, **kwargs):
        super(MyDrop, self).__init__(**kwargs)
        self.redraw()

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]

    def redraw(self):

        self.clear_widgets()
        self.rows = 5
        self.cols =2

        drpName = []
        drpName.append(DropDown())
        btnName = Button(text="B", size_hint=(None, None))
        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btnName.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[0]:dropdown.select(btn.text))
            drpName[0].add_widget(btn)
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)


class SimpleApp(App):

    def build(self):
        app = Root()
        return app



if __name__ == '__main__':
    SimpleApp().run()
