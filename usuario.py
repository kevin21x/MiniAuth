class Usuario:
    def __init__(self, login, senha, ativo):
        self.login = login
        self.ativo = ativo
        self.senha = senha
    def desativar(self):
        self.ativo = False

    def reativar(self):
        self.ativo = True