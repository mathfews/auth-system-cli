import json, os
from pathlib import Path
from hashlib import sha256
directory = Path(__file__).resolve().parent
file_path = directory / "database.json"
def cryptography(_password):
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
            self.database[email] = {"username": username, "password": cryptography(password)}
            with open(file_path, "w", encoding="utf-8") as arq:
                json.dump(self.database, arq, indent=4, ensure_ascii=False)
            return True, "* User successfully registered"
        else:
            return False, "* User already exists!"
    def login(self, email, password):
        if email not in self.database:
            return False, "* User not found!"
        if cryptography(password) != self.database[email]["password"]:
            return False, "* Acess denied!"
        return True, "* Acess granted!"
    def list_emails(self):
        for email in self.database:
            print(f"* {email}")