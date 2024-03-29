from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
import pyrebase
from usuario import Usuario
from produto_custom_list_item import CustomProdutoListItem

class TelaProduto(MDScreen):
    root_db = None
    current_user = None
    lista_produto = []
    filtro = ""

    def atualiza_lista_produto(self, *args):
        self.remove_tudo_lista()
        resultado = self.root_db.child('Produto').get()
        print(resultado.val())
        for i in resultado.each():
            produto = i.val()
            if self.filtro:
                if self.filtro not in produto['nome']:
                    continue
            item = CustomProdutoListItem(text=f"{produto['nome']}")
            item.internal_key = i.key()
            self.lista_produto.append(item)
            self.ids.lista.add_widget(item)

    def remove_tudo_lista(self):
        for item in self.lista_produto:
            self.ids.lista.remove_widget(item)

    def adicionar_produto(self):
        pass

    def filtra_produtos(self, text: str):
        self.filtro = text
        self.atualiza_lista_produto()