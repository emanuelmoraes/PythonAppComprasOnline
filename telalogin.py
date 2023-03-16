from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
import util
import pyrebase

class TelaLogin(MDScreen):
    root_db = None
    current_user = None
    auth = None

    def login_press(self):
        try:
            self.current_user = self.auth.sign_in_with_email_and_password(self.ids.lbLogin.text, self.ids.lbSenha.text)
            #usuarioValido = util.validar_usuario(self.root_db.child('Usuario'), self.current_user)
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
        auth.send_password_reset_email(email)

    def sign_up(self):
        email = self.ids.lbLogin.text
        senha = self.ids.lbSenha.text
        if len(email) == 0:
            toast('Forneça email')
            return
        if len(senha) == 0:
            toast('Forneça senha')
            return

        try:
            self.current_user = self.auth.create_user_with_email_and_password(email, senha)

            data = {
                'nome': '',
                'email': email,
                'senha': senha,
                'cep': ''
            }

            self.root_db.child('Usuario').push(data, self.current_user['idToken'])
        except Exception as e:
            toast(str(e))