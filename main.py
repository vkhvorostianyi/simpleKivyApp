from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from wallet_app import *


class Root(Widget):

    def layout(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text=wallet.list_view(wallet.account_list)))
        layout.add_widget(Label(text=wallet.last_transaction_view()))
        layout.add_widget(Button(text='Add new transaction'))
        layout.add_widget(Button(text='View all transaction'))
        return layout


class SimpleApp(App):

    def build(self):
        root = Root()
        return root.layout()


if __name__ == '__main__':
    SimpleApp().run()
