from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

class TelaUsuario(MDScreen):
    def atualiza_dados_usuario(self, id: str, nome: str, email: str, senha: str, cep: str):
        self.ids.lbId.text = id
        self.ids.lbNome.text = nome
        self.ids.lbEmail.text = email
        self.ids.lbSenha.text = senha
        self.ids.lbCep.text = cep

    def atualiza_dados_usuario(self):
        self.ids.lbId.text = self.current_user['idToken']
        self.ids.lbEmail.text = self.current_user['email']

    def salvar(self):
        id = self.ids.lbId.text
        nome = self.ids.lbNome.text
        email = self.ids.lbEmail.text
        senha = self.ids.lbSenha.text
        cep = self.ids.lbCep.text
        
        if len(nome) == 0:
            toast('Forneça nome')
            return
        if len(email) == 0:
            toast('Forneça email')
            return
        if len(senha) == 0:
            toast('Forneça senha')
            return
        if len(cep) == 0:
            toast('Forneça cep')
            return

        try:
            data = {
                    'nome': nome,
                    'email': email,
                    'senha': senha,
                    'cep': cep
                }
            if (len(id) == 0):
                self.current_user = self.auth.create_user_with_email_and_password(email, senha)
                self.root_db.child('Usuario').push(data, id)
            else:
                self.root_db.child('Usuario').child(id).update(data)
        except Exception as e:
            toast(str(e))