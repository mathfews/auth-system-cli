class Auth:
    def __init__(self):
        self.database = {}
    def register(self,username, password):
        if username not in self.database.keys():
            self.database[username] = password
            return "* Usuário cadastrado com sucesso!"
        else:
            return "* O usuário já está cadastrado!"
    def login(self,username, password):
        if username in self.database.keys():
            if password == self.database[username]:
                return "* Acesso concedido!"
            else:
                return "* Acesso negado!"
        else:
            return "* Usuário não cadastrado!"