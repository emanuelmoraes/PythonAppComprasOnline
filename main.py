from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem, MDList, OneLineAvatarListItem, IRightBodyTouch
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import BoxLayout
import pyrebase
from usuario import Usuario
from telalogin import TelaLogin
from telacarrinho import TelaCarrinho
from telasupermecado import TelaSupermecado
from telaproduto import TelaProduto
from kivymd.uix.dialog import MDDialog
from telausuario import TelaUsuario

firebaseConfig = {
  'apiKey': "AIzaSyD-mY93Ujdy8a3vZGwM3gSnUqul0aXH6l8",
  'authDomain': "carrinhocompraonline.firebaseapp.com",
  'databaseURL': "https://carrinhocompraonline-default-rtdb.firebaseio.com",
  'projectId': "carrinhocompraonline",
  'storageBucket': "carrinhocompraonline.appspot.com",
  'messagingSenderId': "511983918676",
  'appId': "1:511983918676:web:54383ef65e033b7a56d7c1"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()
current_user = auth.sign_in_with_email_and_password("emanueljsmoraes@gmail.com", "123456")

class MainApp(MDApp):

    def on_start(self):
        tela_login = self.root.get_screen("telalogin")
        tela_login.root_db = database
        tela_login.current_user = current_user
        tela_login.auth = firebase.auth()

        tela_carrinho = self.root.get_screen("telacarrinho")
        tela_carrinho.root_db = database
        tela_carrinho.current_user = current_user

        tela_supermecado = self.root.get_screen("telasupermecado")
        tela_supermecado.root_db = database
        tela_supermecado.current_user = current_user

        tela_produto = self.root.get_screen("telaproduto")
        tela_produto.root_db = database
        tela_produto.current_user = current_user

        tela_usuario = self.root.get_screen("telausuario")
        tela_usuario.current_user = current_user

    def callback(self, tela):
        if tela == "telausuario":
            tela_usuario = self.root.get_screen("telausuario")
            tela_usuario.atualiza_dados_usuario()
        if tela == "telaproduto":
            tela_produto = self.root.get_screen("telaproduto")
            tela_produto.atualiza_lista_produto()
        if tela == "telacarrinho":
            tela_carrinho = self.root.get_screen("telacarrinho")
            tela_carrinho.atualiza_lista_carrinho()
        if tela == "telasupermecado":
            tela_supermecado = self.root.get_screen("telasupermecado")
            tela_supermecado.atualiza_lista_supermecado()
        self.root.current = str(tela)

    def remove_carrinho_button(self, text: str):
        tela_carrinho = self.root.get_screen("telacarrinho")
        tela_carrinho.remove_item_list(text)

    def adiciona_produto_no_carrinho(self, text: str):
        print(f'Adicionar produto {text}')
        items = []
        carrinhos = database.child('Carrinho').get()
        for eachItem in carrinhos.each():
            carrinho = eachItem.val()
            if carrinho['user_key'] == current_user['idToken']:
                newItem = OneLineAvatarListItem(text = carrinho['nome'])
                items.append(newItem)

        self.dialog = MDDialog(title='Escolha um carrinho:', type="simple", items = items)
        self.dialog.open()

    def remove_produto_no_carrinho(self, text: str):
        print(f'Remover produto {text}')

janela = MainApp()
janela.title = 'Carrinho compras online'
janela.run()    