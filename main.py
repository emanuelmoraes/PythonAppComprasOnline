import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class TelaInicial(Screen):
    pass

class TelaInicial2(Screen):
    pass

class TelaUsuario(Screen):
    pass

class TelaLogin(Screen):
    def login_press(self):
        user = self.ids.lbLogin.text
        senha = self.ids.lbSenha.text
        if (user == 'eu' and senha == '123'):
            self.manager.current = 'telainicial2'
        else:
            self.ids.lbResposta.text = 'Login ou senha inválido'

class MainApp(App):
    pass

from kivy.core.window import Window
Window.size = (500, 600)

janela = MainApp()
janela.run()