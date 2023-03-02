from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from firebase_admin import db
from usuario import Usuario
from produto_custom_list_item import CustomProdutoListItem

class TelaProduto(MDScreen):
    root_db = None
    current_user = None #Usuario
    lista_produto = []

    def atualiza_lista_produto(self, *args):
        self.remove_tudo_lista()
        resultado = self.root_db.child('Produto').order_by_key().get()
        for produto in resultado:
            if (type(produto) == dict):
                item = OneLineListItem(text=f"{produto['nome']}")
                self.lista_produto.append(item)
                self.ids.lista.add_widget(item)

    def remove_tudo_lista(self):
        for item in self.lista_produto:
            self.ids.lista.remove_widget(item)

    def adicionar_produto(self):
        pass