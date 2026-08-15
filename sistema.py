from .usuario import Usuario

# funcionalidade de alteração de senha

class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, login, senha):
        for usuario in self.usuarios:
            if usuario.login == login:
                print('Usuario já cadastrado!')
                return False
        usuario = Usuario(login, senha, True)
        self.usuarios.append(usuario)
        print('Usuario cadastrado com sucesso!')
        return usuario

    def login(self, login, senha):
        if not login or not senha:
            return None
        for usuario in self.usuarios:
            if usuario.login == login and usuario.senha == senha and usuario.ativo:
                return usuario
        return None

    def buscar_usuario(self, login):
        for usuario in self.usuarios:
            if usuario.login == login:
                return usuario
        return None

    def desativar_usuario(self, login):
        usuario = self.buscar_usuario(login)
        if usuario:
            usuario.desativar()
        return None

    def reativar_usuario(self, login):
        usuario = self.buscar_usuario(login)
        if usuario:
            usuario.reativar()
        return None

    def remover_usuario(self, login):
        usuario = self.buscar_usuario(login)
        if usuario:
            self.usuarios.remove(usuario)
        return None

    def total_usuarios(self):
        numero = (len(self.usuarios))
        return numero
