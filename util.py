from usuario import Usuario
from firebase_admin import db

def validar_usuario(usuarios: db.Reference, current_user: Usuario) -> bool:
    usuario_id = 1;
    for usuario in usuarios.order_by_key().get():
        #print(usuario)
        if (type(usuario) != dict):
            continue
        if (usuario['email'] == current_user.email and usuario['senha'] == current_user.senha):
            current_user.id = usuario_id
            current_user.email = usuario['email']
            current_user.senha = usuario['senha']
            current_user.cep = usuario['cep']
            current_user.nome = usuario['nome']
            return True
        usuario_id += 1
    return False