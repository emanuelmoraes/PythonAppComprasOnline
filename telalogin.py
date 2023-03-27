from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
import pyrebase

class TelaLogin(MDScreen):
    root_db = None
    current_user = None
    auth = None

    def login_press(self):
        try:
            self.current_user = self.auth.sign_in_with_email_and_password(self.ids.lbLogin.text, self.ids.lbSenha.text)
            screenProduto = self.manager.get_screen('telaproduto')
            screenProduto.atualiza_lista_produto()
            self.manager.current = 'telaproduto'
        except:
            toast('Login ou senha invalido')

    def recuperar_senha(self):
        email = self.ids.lbLogin.text
        if len(email) == 0:
            toast('Forneça email cadastrado')
            return
        self.auth.send_password_reset_email(email)
        toast('Email de reset foi enviado por email')