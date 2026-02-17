from auth import Auth
auth = Auth()
def clean_terminal():
    os.system("cls" if os.name == "nt" else "clear")
while True:
    print("Menu \n🔐1) Login\n📝2) Register")
    userInput = input("> ").lower().strip()
    if userInput == "login" or userInput == "1":
        clean_terminal()
        while True:
            email = input("> Enter your email(Enter 0 to return): ").strip()
            if email == "0":
                clean_terminal()
                break
            password = input("> Enter your password: ").strip()
            result = auth.login(email,password)
            auth.show_login_results(email, password)
            if result == True:
                exit()
    elif userInput == "register" or userInput == "2":
        while True:
            clean_terminal()
            email = input("> Enter your email(Enter 0 to return): ").strip()
            if email == "0":
                clean_terminal()
                break
            username = input("> Enter your username: ").strip()
            password = input("> Enter your password: ").strip()
            result = auth.register(email,username, password)
            auth.show_register_results(email)
            if result == True:
                clean_terminal()
                break