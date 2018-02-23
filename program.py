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
    def __init__(self, **kwargs):

        super(CustomDrop, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.data = []
        self.drop_down = DropDown()
        self.btn_name = Button(text="set the text", size_hint=(.5, None))
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

        btn = Button(text='add...', size_hint_y=None, height=self.btn_name.height)
        btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(''))
        self.drop_down.add_widget(btn)
        del_btn = Button(text='delete...', size_hint_y=None, height=self.btn_name.height)
        del_btn.bind(on_release=lambda btn=btn, drop_down=self.drop_down: drop_down.select(''))
        self.drop_down.add_widget(del_btn)


class DeleteAccDrop(CustomDrop):
    def __init__(self, **kwargs):
        super(DeleteAccDrop,self).__init__(**kwargs)
        self.data = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
    def build_func(self):
        pass


class DeleteCatDrop(CustomDrop):
    sel = ["{}".format(x) for x in wallet.category_list.keys()]




class MyDrop(BoxLayout):
    def __init__(self, **kwargs):
        super(MyDrop, self).__init__(**kwargs)
        self.redraw()

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
    cat = ["{}".format(x) for x in wallet.category_list.keys()]
    def call_cat_add_btn(self,e=None):
        self.parent.parent.add_widget(CatAdd())
        # self.remove_widget(self)
        # self.parent.parent.parent.manager.current = 'add_cat'
    def call_acc_add_btn(self,e=None):
        self.parent.parent.add_widget(AccountAdd())
        # self.remove_widget(self)
        # self.parent.parent.parent.manager.current = 'add_cat'
    def call_del_cat(self,e=None):
        self.parent.parent.add_widget(DelCat())

    def call_del_acc(self,e=None):
        self.parent.parent.add_widget(DelAcc())

    def redraw(self):

        self.clear_widgets()
        self.cols =2
        drpName = []
        dd1 = DropDown()
        dd2 = DropDown()
        drpName.append(dd1)
        drpName.append(dd2)
        btnName = Button(text="choose account", size_hint=(.5, None))
        BtnCat = Button(text="choose category", size_hint=(.5, None))

        for i in self.sel:
            btn=Button(text=i, size_hint_y=None, height=btnName.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[0]:dropdown.select(btn.text))
            drpName[0].add_widget(btn)
        else:
            btn = Button(text='add...', size_hint_y=None, height=BtnCat.height)
            btn.bind(on_release=lambda btn=btn, dropdown=drpName[0]: dropdown.select("choose account"))
            btn.bind(on_press=self.call_acc_add_btn)
            drpName[0].add_widget(btn)
            del_btn = Button(text='delete...',size_hint_y=None,height =btnName.height)
            del_btn.bind(on_release=lambda btn=btn, dropdown=drpName[0]: dropdown.select("choose account"))
            del_btn.bind(on_press=self.call_del_acc)
            drpName[0].add_widget(del_btn)
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)

        for i in self.cat:
            btn=Button(text=i, size_hint_y=None, height=BtnCat.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[1]:dropdown.select(btn.text))
            drpName[1].add_widget(btn)
        else:
            btn = Button(text='add...', size_hint_y=None, height=BtnCat.height)
            btn.bind(on_release = lambda btn=btn,dropdown=drpName[1]:dropdown.select('choose category'))
            btn.bind(on_press = self.call_cat_add_btn)
            drpName[1].add_widget(btn)
            del_btn = Button(text='delete...', size_hint_y=None, height=BtnCat.height)
            del_btn.bind(on_release=lambda btn=btn, dropdown=drpName[1]: dropdown.select("choose category"))
            del_btn.bind(on_press=self.call_del_cat)
            drpName[1].add_widget(del_btn)
        BtnCat.bind(on_release=drpName[1].open)
        drpName[1].bind(on_select=lambda instance, x, btn=BtnCat: setattr(btn, 'text', x))
        self.add_widget(BtnCat)


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
