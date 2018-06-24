from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.app import App


class Root(ScreenManager):
    pass


class StartScreen(Screen):
    pass


class ViewIncomeTransaction(Screen):
    pass


class ViewOutcomeTransaction(Screen):
    pass


class NewIncomeTransaction(Screen):
    pass


class NewOutcomeTransaction(Screen):
    pass


class WalletApp(App):

    def build(self):
        app = Root(transition=FadeTransition())
        app.add_widget(StartScreen(name='main'))
        return app


if __name__ == '__main__':
    myapp = WalletApp()
    myapp.run()
