import os
import time
import keyboard
import pyfiglet
from termcolor import colored



while True:

    software = "SOFTWARE"
    software = pyfiglet.figlet_format("SOFTWARE", font="slant")
    print(colored(software, "cyan"))
    pescolha = input(colored("\nDigite para continuar \n", "cyan"))
    print("Inicializando")
    time.sleep(2)
    break

def software():
    while True:
        os.system("cls")
        print(colored(" ⚙️  Software é um conjunto de instruções que definem os programas de um computador, permitindo que ele execute tarefas específicas. É a parte lógica do computador, o oposto do hardware, que é a parte física.⚙️ ", "cyan"))
        print(colored("\n1 - História do software", "cyan"))
        print(colored("2 - Ranking softwares mais atualizados", "cyan"))
        print(colored("3 - Segurança em software", "cyan"))
        print(colored("3 - Segurança em software", "cyan"))

        escolha = input(colored("\nDigite a opção desejada: ", "green"))

        if escolha == ("1"):
            print("Abrindo arquivo em:")
            time.sleep(1) 
            print("5...")
            time.sleep(1)
            print("4...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            os.startfile ("historia_software.pdf")
        elif escolha == ("2"):
            print("Abrindo arquivo em:")
            time.sleep(1) 
            print("5...")
            time.sleep(1)
            print("4...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            os.startfile ("ranking.pdf")
        elif escolha == ("3"):
            print("Abrindo arquivo em:")
            time.sleep(1) 
            print("5...")
            time.sleep(1)
            print("4...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            os.startfile ("Segurança_em_Software")
        else:
            print(colored("Por favor digite um opção válida! Voltando para tela inicial", "red"))
            time.sleep(3)

software()