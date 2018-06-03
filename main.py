from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from wallet_app import *
from kivy.uix.textinput import TextInput
import re


class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class AccountScreen(Screen):
    pass


class CategoryScreen(Screen):
    pass


class Lb(Label):
    pass


class HeadTitle(BoxLayout):
    pass


class MainView(BoxLayout):
    pass


class MainViewIncome(BoxLayout):
    pass


class TransactionScreen(Screen):
    pass


class InputWindow(Screen):
    pass


class Root(ScreenManager):
    ...


class StartScreen(Screen):
    pass


class BlueCanvas(BoxLayout):
    def __init__(self):
        super(BlueCanvas, self).__init__()
        self.orientation = 'vertical'
        self.size_hint = .75, .25


class CatAddIn(BlueCanvas):
    pass

class DelCat(BlueCanvas):
    pass


class DelAcc(BlueCanvas):
    pass


class CatAdd(BlueCanvas):
    pass


class AccountAdd(BlueCanvas):
    pass


class CustomDrop(BoxLayout):
    def __init__(self, title="Choose item",data=None,**kwargs):

        super(CustomDrop, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.data = data
        self.drop_down = DropDown()
        self.title = title
        self.btn_name = Button(text=self.title, size_hint=(1,1))
        self.redraw()

    def redraw(self):
        for i in self.data:
            btn = Button(text=i, size_hint_y=None, height=self.btn_name.height)
            btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(btn.text))
            self.drop_down.add_widget(btn)
        else:
            self.build_func()
        self.btn_name.bind(on_release=self.drop_down.open)
        self.drop_down.bind(on_select=lambda instance, x, btn=self.btn_name: setattr(btn, 'text', x))
        self.add_widget(self.btn_name)

    def build_func(self):
        ...


class DeleteAccDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(DeleteAccDrop,self).__init__(data=["{}:{}".format(x, y) for x, y in wallet.account_list.items()],**kwargs)

    def build_func(self):
        pass


class DeleteCatDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(DeleteCatDrop,self).__init__(data=["{}".format(x) for x in wallet.category_list.keys()], **kwargs)


class AccDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(AccDrop,self).__init__(title="Set account", data=["{}:{}".format(x, y) for x, y in wallet.account_list.items()],**kwargs)

    def call_acc_add_btn(self, e=None):
        self.parent.parent.parent.add_widget(AccountAdd())

    def call_del_acc(self, e=None):
        self.parent.parent.parent.add_widget(DelAcc())

    def build_func(self):
        btn = Button(text='add...', size_hint_y=None, height=self.btn_name.height)
        btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        btn.bind(on_press=self.call_acc_add_btn)
        self.drop_down.add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.btn_name.height)
        del_btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        del_btn.bind(on_press=self.call_del_acc)
        self.drop_down.add_widget(del_btn)


class CatDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(CatDrop,self).__init__(title="Set category", data=["{}".format(x)
                                                                 for x in wallet.category_list.keys()
                                                                 if wallet.category_list[x] is True], **kwargs)

    def call_cat_add_btn(self, e=None):
        self.parent.parent.parent.add_widget(CatAdd())

    def call_del_cat(self, e=None):
        self.parent.parent.parent.add_widget(DelCat())

    def build_func(self):
        btn = Button(text='add...', size_hint_y=None, height=self.btn_name.height)
        btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        btn.bind(on_press = self.call_cat_add_btn)
        self.drop_down.add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.btn_name.height)
        del_btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        del_btn.bind(on_press = self.call_del_cat)
        self.drop_down.add_widget(del_btn)


class InCat(CustomDrop):
    def __init__(self, **kwargs):
        super().__init__(title="Set category", data=["{}".format(x)
                                                     for x in wallet.category_list.keys()
                                                     if wallet.category_list[x] is False], **kwargs)

    def call_cat_add(self, e=None):
        self.parent.parent.parent.add_widget(CatAddIn())

    def del_cat(self, e=None):
        self.parent.parent.parent.add_widget(DelCat())

    def build_func(self):
        btn = Button(text='add...', size_hint_y=None, height=self.btn_name.height)
        btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        btn.bind(on_press=self.call_cat_add)
        self.drop_down.add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.btn_name.height)
        del_btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(self.title))
        del_btn.bind(on_press=self.del_cat)
        self.drop_down.add_widget(del_btn)


class SimpleApp(App):

    def build(self):
        app = Root(transition=FadeTransition())
        app.add_widget(StartScreen(name='main'))
        return app


if __name__ == '__main__':
    myapp = SimpleApp()
    myapp.run()

