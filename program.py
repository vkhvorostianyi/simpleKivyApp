from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from wallet_app import  *
from kivy.clock import Clock

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


class TransactionScreen(Screen):
    pass


class InputWindow(Screen):
    pass


class Root(ScreenManager):

    def update(self, dt):
        self.clear_widgets()
        self.add_widget((StartScreen(name='main')))


class StartScreen(Screen):
    pass


class BlueCanvas(BoxLayout):
    def __init__(self):
        super(BlueCanvas, self).__init__()
        self.orientation = 'vertical'
        self.size_hint  = .75,.25

class DelCat(BlueCanvas):
    pass


class DelAcc(BlueCanvas):
    pass


class CatAdd(BlueCanvas):
    pass

class AccountAdd(BlueCanvas):
    pass

class CustomDrop(BoxLayout):
    def __init__(self,title="Choose item",data=None,**kwargs):

        super(CustomDrop, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.data = data
        self.drop_down = DropDown()
        self.title = title
        self.btn_name = Button(text=self.title, size_hint=(1, None))
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
        super(DeleteAccDrop,self).__init__(data = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()],**kwargs)

    def build_func(self):
        pass


class DeleteCatDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(DeleteCatDrop,self).__init__(data = ["{}".format(x) for x in wallet.category_list.keys()], **kwargs)



class AccDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(AccDrop,self).__init__(data = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()],**kwargs)

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
        super(CatDrop,self).__init__(data = ["{}".format(x) for x in wallet.category_list.keys()] ,**kwargs)

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

class SimpleApp(App):

    def build(self):
        app = Root()
        app.add_widget(StartScreen(name='main'))
        app.add_widget(InputWindow(name="add_out_tr"))
        app.add_widget(TransactionScreen(name='out_tr_screen'))
        app.add_widget(CategoryScreen(name='in_tr_screen'))
        app.add_widget(AccountScreen(name='add_in_tr'))
        return app



if __name__ == '__main__':
    SimpleApp().run()
