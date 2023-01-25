import kivy
kivy.require("2.0.0")
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class TelaLogin(MDScreen):
    def login_press(self):
        user = self.ids.lbLogin.text
        senha = self.ids.lbSenha.text
        if (user == 'eu' and senha == '123'):
            self.manager.current = 'telaproduto'
        else:
            self.ids.lbResposta.text = 'Login ou senha inválido'

class MainApp(MDApp):
    def callback(self, tela):
        self.root.current = str(tela)

janela = MainApp()
janela.title = 'Carrinho compras online'
janela.run()