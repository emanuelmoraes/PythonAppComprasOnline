from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDFlatButton, MDRaisedButton
from kivymd.toast import toast

class ContentSupermecado(BoxLayout):
    pass

class TelaSupermecado(MDScreen):
    dialog = None
    root_db = None
    current_user = None #Usuario
    lista_supermecado = []

    def atualiza_lista_supermecado(self):
        self.remove_tudo_lista()
        resultado = self.root_db.child('Supermecado').order_by_key().get()
        print(resultado)
        if resultado != None:
            for key, value in resultado.items():
                if (type(value) == dict):
                    item = OneLineListItem(text=f"{value['nome']}")
                    self.lista_supermecado.append(item)
                    self.ids.lista.add_widget(item)

    def remove_tudo_lista(self):
        for item in self.lista_supermecado:
            self.ids.lista.remove_widget(item)

    def adicionar_supermecado(self):
        content_cls = ContentSupermecado()
        self.dialog = MDDialog(title='Supermecado', content_cls=content_cls, type='custom',
                               buttons = [
                                MDFlatButton(text="Cancel", on_release=self.close_dialog),
                                MDRaisedButton(text="Ok", on_release=lambda x:self.get_data(x, content_cls))
                                ])
        self.dialog.open()

    def close_dialog(self, instance):
        if self.dialog:
            self.dialog.dismiss()

    def get_data(self, instance_btn, content_cls):
        nomeField = content_cls.ids.nomeField
        siteField = content_cls.ids.siteField
        nome = nomeField._get_text()
        site = siteField._get_text()
        # do stuffs here
        toast(nome)
        self.adicionar_supermecado_bancodados(nome, site)
        self.close_dialog(instance_btn)
        self.atualiza_lista_supermecado()

    def adicionar_supermecado_bancodados(self, nome: str, site: str):
        carrinho_db = self.root_db.child('Supermecado')
        carrinho_db.push({'nome':nome, 'site':site})