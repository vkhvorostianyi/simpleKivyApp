from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from wallet_app import *

dropdown = DropDown()
data=["{}:{}".format(x,y) for x,y in wallet.account_list.items()]
for index in data:

    btn = Button(text=index, size_hint_y=None, height=44)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)

mainbutton = Button(text='Choose account', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

runTouchApp(mainbutton)