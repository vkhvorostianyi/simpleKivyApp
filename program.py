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




class MyDrop(Screen):
    def __init__(self, **kwargs):
        super(MyDrop, self).__init__(**kwargs)
        self.redraw()
    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]

    def redraw(self):

        self.clear_widgets()
        drp_name = DropDown()
        btn_name = Button(text="Choose account", size_hint=(1, .5))

        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btn_name.height)
            btn.bind(on_release=lambda btn=btn, dropdown=drp_name: dropdown.select(btn.text))
            drp_name.add_widget(btn)
        btn_name.bind(on_release=drp_name.open)
        drp_name.bind(on_select=lambda instance, x, btn=btn_name: setattr(btn, 'text', x))
        self.add_widget(btn_name)

class SimpleApp(App):

    def build(self):
        app = Root()
        return app



if __name__ == '__main__':
    SimpleApp().run()
