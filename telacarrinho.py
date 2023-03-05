from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
import pyrebase
from carrinho_custom_list_item import CustomCarrinhoListItem
from usuario import Usuario
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast

class Content(MDFloatLayout):
    pass

class TelaCarrinho(MDScreen):
    dialog = None
    root_db = None
    current_user = None #Usuario
    lista_carrinho = []

    def atualiza_lista_carrinho(self):
        self.remove_tudo_lista()
        resultado = self.root_db.child('Carrinho').get()
        try:
            for value in resultado.each():
                carrinho = value.val()
                if carrinho == None:
                    continue
                if (carrinho['user_key'] != self.current_user.key):
                    continue
                item = CustomCarrinhoListItem(text=f"{carrinho['nome']}")
                item.internal_key = value.key()
                self.lista_carrinho.append(item)
                self.ids.lista.add_widget(item)
        except:
            pass

    def remove_tudo_lista(self):
        for item in self.lista_carrinho:
            self.ids.lista.remove_widget(item)

    def remove_item_list(self, text: str):
        item_para_remover = None

        for item in self.lista_carrinho:
            if item.text == text:
                item_para_remover = item
                break;

        if item_para_remover is not None:
            print(f'carrinho = {text}, key = {item_para_remover.internal_key}')
            self.ids.lista.remove_widget(item_para_remover)
            self.remove_carrinho_bancodados(item_para_remover.internal_key)
            self.lista_carrinho.remove(item_para_remover)

    def adicionar_carrinho(self, *args):
        content_cls = Content()
        self.dialog = MDDialog(title='Nome do carrinho', content_cls=content_cls, type='custom',
                               buttons = [
                                MDFlatButton(text="Cancel",on_release=self.close_dialog),
                                MDRaisedButton(text="Ok",on_release=lambda x:self.get_data(x,content_cls))
                                ])
        self.dialog.open()
    
    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()

    def get_data(self, instance_btn, content_cls):
        textfield = content_cls.ids.textField
        value = textfield._get_text()
        # do stuffs here
        toast(value)
        self.adicionar_carrinho_bancodados(value)
        self.close_dialog(instance_btn)
        self.atualiza_lista_carrinho()

    def adicionar_carrinho_bancodados(self, nome: str):
        carrinho_db = self.root_db.child('Carrinho')
        carrinho_db.push({'nome':nome, 'user_key':self.current_user.key})

    def remove_carrinho_bancodados(self, key: str):
        item_carrinho_db = self.root_db.child(f'Carrinho/{key}')
        item_carrinho_db.remove()