from usuario import Usuario
import pyrebase

def validar_usuario(usuarios: pyrebase.pyrebase.Database.child, current_user: Usuario) -> bool:
    for item in usuarios.get().each():
        usuario = item.val()
        if usuario == None:
            continue
        if (usuario['email'] == current_user.email and usuario['senha'] == current_user.senha):
            current_user.key = item.key()
            current_user.email = usuario['email']
            current_user.senha = usuario['senha']
            current_user.cep = usuario['cep']
            current_user.nome = usuario['nome']
            return True
    return False