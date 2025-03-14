import os


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
    


os.system("clear")
def menu_principal():
    print("1 - Python")
    print("2 - Hardware")
    print("3 - Software")
    print("4 - Cyber Segurança")
    print("5 - Games")
    print("6 - Termos")






while True:
    menu_principal()
    escolha = input("Digite o numero que representa sua escolha")
    if escolha == 7:
        print("Saindo")
        break

