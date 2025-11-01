from cryptography.fernet import Fernet

key = Fernet.generate_key()
fer = Fernet(key)

def ver():
    with open("password.txt", "r") as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split(" | ")
            print(f"Usuário: {user} | Senha: {fer.decrypt(passw.encode()).decode()}")

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