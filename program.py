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




class MyDrop(BoxLayout):
    def __init__(self, **kwargs):
        super(MyDrop, self).__init__(**kwargs)
        self.redraw()
    sel = [str(i) for i in range(2,16,2)]
    btn_text = 'a'
    def redraw(self):

        self.clear_widgets()
        __drp_name = DropDown()
        btn_name = Button(text=self.btn_text, size_hint=(.5, .5))

        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btn_name.height)
            btn.bind(on_release=lambda btn=btn, dropdown=__drp_name: dropdown.select(btn.text))
            __drp_name.add_widget(btn)
        btn_name.bind(on_release=__drp_name.open)
        __drp_name.bind(on_select=lambda instance, x, btn=btn_name: setattr(btn, 'text', x))
        self.add_widget(btn_name)


class AccountDrop(MyDrop):
    def __init__(self, **kwargs):
        super(AccountDrop, self).__init__(**kwargs)
        self.redraw()
    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
    btn_text = 'Choose account'


class CategoryDrop(MyDrop):
    def __init__(self, **kwargs):
        super(CategoryDrop, self).__init__(**kwargs)
        self.redraw()
    sel = ["{}".format(x) for x in wallet.category_list.keys()]
    btn_text = 'Choose category'


class SimpleApp(App):

    def build(self):
        app = Root()
        return app



if __name__ == '__main__':
    SimpleApp().run()
