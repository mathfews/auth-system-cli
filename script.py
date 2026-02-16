class Auth:
    def __init__(self):
        self.database = {}
    def register(self,email, username, password):
        if email not in self.database.keys():
            self.database[email] = {"username": username, "password": password}
            return "* Usuário cadastrado com sucesso!"
        else:
            return "* O usuário já está cadastrado!"
    def login(self, email, password):
        if email in self.database.keys():
            if password == self.database[email]["password"]:
                return "* Acesso concedido!"
            else:
                return "* Acesso negado!"
        else:
            return "* Usuário não cadastrado!"