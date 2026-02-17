import json, os
from pathlib import Path
from hashlib import sha256
directory = Path(__file__).resolve().parent
file_path = directory / "database.json"
def criptografy(_password):
        password = sha256(_password.encode()).hexdigest()
        return password
class Auth:
    def __init__(self):
        try:
            with open(file_path,"r", encoding="utf-8") as arq:
                self.database = json.load(arq)
        except (json.JSONDecodeError, FileNotFoundError):
            self.database = {}
    
    def register(self,email,username, password):
        if email not in self.database:
            self.database[email] = {"username": username, "password": criptografy(password)}
            with open(file_path, "w", encoding="utf-8") as arq:
                json.dump(self.database, arq, indent=4, ensure_ascii=False)
            return True
        else:
            return False
    def login(self, email, password):
        if email in self.database:
            if criptografy(password) == self.database[email]["password"]:
                return True
            else:
                return False
        else:
            return False
    def list_emails(self):
        for email in self.database:
            print(f"* {email}")
    def show_login_results(self, email, password):
        if email in self.database.keys():
            if criptografy(password) == self.database[email]["password"]:
                print("* Acess granted")
            else:
                print("* Acess denied")
        else:
            print("* User not found!")
    def show_register_results(self, email):
        if email not in self.database.keys():
            print("* User successfully registered!")
        else:
            print("Usuário already exists!")