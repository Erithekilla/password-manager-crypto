from cryptography.fernet import Fernet


def gerar_chave():
    key = Fernet.generate_key()
    try:
        with open("key.key", "wb") as file:
            file.write(key)
    except FileNotFoundError:
        print("Error: O ficheiro não existe.")
        return None

def carregar_chave():
    try:
        with open("key.key", "rb") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: O ficheiro não existe.")
        return None
    

key = carregar_chave()
fer = Fernet(key)

def ver():
    with open("password.txt", "r") as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split(" | ")
            senha = fer.decrypt(passw.encode()).decode()
            print(f"Usuário: {user} | Senha: {senha}")

def add():
    user = input("Digite o nome/email: ")
    pwd = input("Digite sua senha: ")
    with open("password.txt", "a") as f:
        f.write(user + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    sunlight = input("O que quer fazer, ver suas senhas ou adicionar? (ver, add) q para sair: ").lower()

    if sunlight == "q":
        break

    if sunlight == "ver":
        ver()
    elif sunlight == "add":
        add()
    else:
        print("Inválido, tente novamente (q para sair).")
        continue