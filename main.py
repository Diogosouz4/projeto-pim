import os
import time
import pyglet

# uma função de menu principal
def menu_principal():
    #toda vez que for chamada a funçao será executado esse while
    while True:
        os.system("cls")
        print("🌐 1 - Python")
        print("🖥️  2 - Hardware")
        print("⚙️  3 - Software")
        print("👮 4 - Cyber Segurança")
        print("📝 5 - Termos")
        print("📝 6 - Sair")
        escolha = int(input("Digite o numero que representa sua escolha "))
        if escolha == 1:
            python()
            break
        elif escolha == 2:
            hardware()
            break
        elif escolha == 3:
            software()
            break
        elif escolha == 4:
            cybersegurança()
            break
        elif escolha == 5:
            termos()
            break
        else:
            print("Saindo")
            exit()
    
#função python referente a primeira opçao do menu principal
def python():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS\Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal()

#função python referente a primeira opçao do menu principal
def hardware():
    print("Abrindo apostila de Python!")
    os.startfile("Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal()    

#função python referente a primeira opçao do menu principal
def software():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS/Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal() 

#função python referente a primeira opçao do menu principal
def cybersegurança():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS/Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal()

#função python referente a primeira opçao do menu principal
def termos():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS/Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_principal()

# tela de Bem vindo
print("Olá, bem-vindo à Plataforma Educacional")

login_correto = "admin"  #login correto para entrar no aplicativo
senha_correta = "admin"  #senha correta para entrar no aplicativo 

# while feito para comparar o que a pessoa digitou com a senha se estiver correta segue normalmente, se não fica no loop até acertar
while True:
    login = input("Digite a login: ")
    senha = input("Digite o senha: ")
    if login == login_correto and senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Acesso negado. Aguarde 3 Segundos e Tente novamente.")
        time.sleep(3) 
        os.system("cls")
    
# chamando a funçao menu principal
menu_principal()