from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from wallet_app import  *

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
    pass



class StartScreen(Screen):
    pass


class BlueCanvas(BoxLayout):
    def __init__(self):
        super(BlueCanvas, self).__init__()
        self.orientation = 'vertical'
        self.size_hint  = .75,.25

class DelCat(BlueCanvas):
    def __init__(self):
        super(DelCat,self).__init__()

class DelAcc(BlueCanvas):
    pass

class CatAdd(BlueCanvas):
    def __init__(self):
        super(CatAdd, self).__init__()



class AccountAdd(BlueCanvas):
    def __init__(self):
        super(AccountAdd,self).__init__()

class DeleteDrop(BoxLayout):
    def __init__(self, **kwargs):
        super(DeleteDrop, self).__init__(**kwargs)
        self.redraw()

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]

    def redraw(self):
        self.clear_widgets()
        # self.cols =1

        drpName = []
        dd = DropDown()
        drpName.append(dd)
        btnName = Button(text="accounts", size_hint=(1, 1))
        for i in self.sel:
            btn = Button(text=i, size_hint_y=None, height=btnName.height)
            btn.bind(on_release=lambda btn=btn, dropdown=drpName[0]: dropdown.select(btn.text))
            drpName[0].add_widget(btn)
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)


class DeleteCatDrop(DeleteDrop):
    sel = ["{}".format(x) for x in wallet.category_list.keys()]


class DeleteAccDrop(DeleteDrop):
    pass

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
            btn.bind(on_release=lambda btn=btn, dropdown=drpName[0]: dropdown.select(btn.text))
            btn.bind(on_press=self.call_acc_add_btn)
            drpName[0].add_widget(btn)
            del_btn = Button(text='delete...',size_hint_y=None,height =btnName.height)
            del_btn.bind(on_release=lambda btn=btn, dropdown=drpName[0]: dropdown.select(btn.text))
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
            btn.bind(on_release = lambda btn=btn,dropdown=drpName[1]:dropdown.select(btn.text))
            btn.bind(on_press = self.call_cat_add_btn)
            drpName[1].add_widget(btn)
            del_btn = Button(text='delete...', size_hint_y=None, height=BtnCat.height)
            del_btn.bind(on_release=lambda btn=btn, dropdown=drpName[1]: dropdown.select(btn.text))
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
