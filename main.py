import os
from time import sleep


def menu_principal():
    
    while True:
        os.system("cls")
        print("🌐 1 - Python")
        print("🖥️  2 - Hardware")
        print("⚙️  3 - Software")
        print("👮 4 - Cyber Segurança")
        print("🎮 5 - Games")
        print("📝 6 - Termos")
        print("📝 7 - Sair")
        escolha = int(input("Digite o numero que representa sua escolha "))
        if escolha == 1:
            python()
            break
        elif escolha == 7:
            print("Saindo")
            exit()
    

def python():
    print("Abrindo Python!")
    print("Python e feito para programadores")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal()
    
    

print("Olá, bem-vindo à Plataforma Educacional")

senha_correta = "admin"
login_correto = "admin"


while True:
    login = input("Digite a login: ")
    senha = input("Digite o senha: ")
    if login == login_correto and senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Acesso negado. Tente novamente.")
        os.system("cls")
    

menu_principal()

