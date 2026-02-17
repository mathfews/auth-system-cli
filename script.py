import json
from pathlib import Path
directory = Path(__file__).resolve().parent
file_path = directory / "database.json"

class Auth:
    def __init__(self):
        try:
            with open(file_path,"r", encoding="utf-8") as arq:
                self.database = json.load(arq)
        except json.JSONDecodeError:
            self.database = {}
    def register(self,email,username, password):
        if email not in self.database.keys():
            self.database[email] = {"username": username, "password": password}
            with open(file_path, "w", encoding="utf-8") as arq:
                json.dump(self.database, arq, indent=4, ensure_ascii=False)
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
    def list_emails(self):
        for email in self.database.keys():
            print(f"* {email}")
auth = Auth() 
