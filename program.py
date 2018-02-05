from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from wallet_app import  *

class AccountScreen(Screen):
    pass


class CategoryScreen(Screen):
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

    sel = ["{}:{}".format(x, y) for x, y in wallet.account_list.items()]
    cat = ["{}".format(x) for x in wallet.category_list.keys()]
    def clear(self,e=None):
        self.parent.clear_widgets()


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
        btnName.bind(on_release=drpName[0].open)
        drpName[0].bind(on_select=lambda instance, x, btn=btnName: setattr(btn, 'text', x))
        self.add_widget(btnName)

        for i in self.cat:
            btn=Button(text=i, size_hint_y=None, height=BtnCat.height)
            btn.bind(on_release=lambda btn=btn,dropdown=drpName[1]:dropdown.select(btn.text))
            drpName[1].add_widget(btn)
        else:
            btn = Button(text='add category', size_hint_y=None, height=BtnCat.height)
            btn.bind(on_release = self.clear)
            drpName[1].add_widget(btn)
        BtnCat.bind(on_release=drpName[1].open)
        drpName[1].bind(on_select=lambda instance, x, btn=BtnCat: setattr(btn, 'text', x))
        self.add_widget(BtnCat)

class SimpleApp(App):

    def build(self):
        app = Root()
        app.add_widget(StartScreen(name='main'))
        app.add_widget(InputWindow(name="add_tr"))
        app.add_widget(TransactionScreen(name='tr_screen'))
        app.add_widget(CategoryScreen(name='add_cat'))
        app.add_widget(AccountScreen(name='add_acc'))
        return app



if __name__ == '__main__':
    SimpleApp().run()
