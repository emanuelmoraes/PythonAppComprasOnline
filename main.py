import kivy
kivy.require("2.0.0")
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.list import OneLineListItem, MDList, OneLineAvatarIconListItem, IRightBodyTouch
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
import firebase_admin
from firebase_admin import credentials
from usuario import Usuario
from telalogin import TelaLogin
from telacarrinho import TelaCarrinho
from telasupermecado import TelaSupermecado
from telaproduto import TelaProduto

###########################################################################
# CONFIGURACAO PARA O FIREBASE
###########################################################################
database_host = 'https://carrinhocompraonline-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('carrinhocompraonline-firebase-adminsdk-edoxn-0c76c68a16.json')
default_app = firebase_admin.initialize_app(cred)

from firebase_admin import db
root_db = db.reference(url = database_host)

current_user = Usuario()

class TelaUsuario(MDScreen):
    def atualiza_dados_usuario(self):
        self.ids.lbNome.text = current_user.nome
        self.ids.lbEmail.text = current_user.email
        self.ids.lbSenha.text = current_user.senha
        self.ids.lbCep.text = current_user.cep

class MainApp(MDApp):

    def on_start(self):
        tela_login = self.root.get_screen("telalogin")
        tela_login.root_db = root_db
        tela_login.current_user = current_user

        tela_carrinho = self.root.get_screen("telacarrinho")
        tela_carrinho.root_db = root_db
        tela_carrinho.current_user = current_user

        tela_supermecado = self.root.get_screen("telasupermecado")
        tela_supermecado.root_db = root_db
        tela_supermecado.current_user = current_user

        tela_produto = self.root.get_screen("telaproduto")
        tela_produto.root_db = root_db
        tela_produto.current_user = current_user

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

    def remove_carrinho_button(self, text):
        tela_carrinho = self.root.get_screen("telacarrinho")
        tela_carrinho.remove_item_list(text)

janela = MainApp()
janela.title = 'Carrinho compras online'
janela.run()    