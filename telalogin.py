from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
import util

class TelaLogin(MDScreen):
    root_db = None
    current_user = None

    def login_press(self):
        self.current_user.email = self.ids.lbLogin.text
        self.current_user.senha = self.ids.lbSenha.text

        usuarioValido = util.validar_usuario(self.root_db.child('Usuario'), self.current_user)
        if (usuarioValido):
            screenProduto = self.manager.get_screen('telaproduto')
            screenProduto.atualiza_lista_produto()
            self.manager.current = 'telaproduto'
        else:
            toast('Login ou senha invalido')