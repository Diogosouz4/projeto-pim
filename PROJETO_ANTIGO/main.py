import os
import time
import pyglet

#função menu principal
def menu_principal():
    #toda vez que for chamada a funçao será executado esse while
    while True:
        os.system("cls")
        print("🌐 1 - Disciplinas")
        print("⚙️  3 - Notas")
        print("👮 4 - Termos")
        print("📝 5 - Privacidade")
        print("📝 5 - Sair")
        escolha = int(input("Digite o numero que representa sua escolha "))
        if escolha == 1:
            menu_conteudos()
            break
        elif escolha == 2:
            menu_notas()
            break
        elif escolha == 3:
            termos()
            break
        elif escolha == 4:
            privacidade()
            break
        else:
            print("Saindo")
            exit()

# uma função de menu principal
def menu_conteudos():
    #toda vez que for chamada a funçao será executado esse while
    while True:
        os.system("cls")
        print("🌐 1 - Python")
        print("🖥️  2 - Hardware")
        print("⚙️  3 - Software")
        print("👮 4 - Cyber Segurança")
        print("📝 5 - Sair")
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
        else:
            print("Saindo")
            exit()
    
#função python referente a primeira opçao do menu principal
def python():
    while True:
        os.system("cls")
        print("🌐 1 - Conteudos")
        print("🖥️  2 - Prova")
        cescolha = int(input("Digite o numero que representa sua escolha "))
        if cescolha == 1:
            conteudos_python()
            break
        elif cescolha == 2:
            prova_python()
            break
        else:
            print("Voltando ao Menu de Conteudos")
            time.sleep(2)
            menu_conteudos()
            
    
def conteudos_python():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS\Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
       menu_conteudos()

def prova_python():
    if ppythonfeita == 1:
        print("Está prova ja foi feita")
        menu_conteudos()
    else:
        pontuacao_python = 0

        print("=== Prova Básica de Python ===\n")

        # Pergunta 1
        print("1) O que será impresso pelo código: x = 10; y = 5; print(x + y * 2)?")
        print("A) 30\nB) 20\nC) 25\nD) 15")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "C":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: C\n")

        # Pergunta 2
        print("2) Qual é a saída de: nome = 'Python'; print(nome[1:4])?")
        print("A) yth\nB) ytho\nC) Pyt\nD) ythn")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "A":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: A\n")

        # Pergunta 3
        print("3) Qual código verifica se um número é par?")
        print("A) if num % 2 = 0\nB) if num // 2 == 0\nC) if num % 2 == 0\nD) if num % 2 != 0")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "C":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: C\n")

        # Pergunta 4
        print("4) Qual é a principal diferença entre listas e tuplas?")
        print("A) Listas são mais rápidas\nB) Tuplas são mutáveis\nC) Listas são mutáveis\nD) Não há diferença")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "C":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: C\n")

        # Pergunta 5
        print("5) Qual função lê dados do usuário no terminal?")
        print("A) scanf()\nB) console.log()\nC) read()\nD) input()")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "D":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: D\n")

        # Pergunta 6
        print("6) O que o código imprime: for i in range(3): print(i)")
        print("A) 1 2 3\nB) 0 1 2\nC) 0 1 2 3\nD) 1 2")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "B":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: B\n")

        # Pergunta 7
        print("7) Qual define corretamente uma função chamada soma?")
        print("A) def soma(x, y): return x + y\nB) function soma(x, y) => x + y\nC) soma = (x, y) -> x + y\nD) def soma = x + y")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "A":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: A\n")

        # Pergunta 8
        print("8) Qual define corretamente um dicionário com nome e idade?")
        print("A) {'nome': 'Ana', 'idade': 30}\nB) ['nome' = 'Ana', 'idade' = 30]\nC) {nome = 'Ana', idade = 30}\nD) (nome: 'Ana', idade: 30)")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "A":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: A\n")

        # Pergunta 9
        print("9) O que é um erro de indentação?")
        print("A) Quando o Python não encontra variável\nB) Espaços/tabulações fora do padrão\nC) Erro de digitação\nD) Falta de biblioteca")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "B":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: B\n")

        # Pergunta 10
        print("10) Qual o valor final de x no código: x = 1; while x < 5: x += 1?")
        print("A) 4\nB) 5\nC) 6\nD) 1")
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == "B":
            pontuacao_python += 1
            print("✅ Correto!\n")
        else:
            print("❌ Errado. Resposta correta: B\n")


        # Resultado final
        print(f"🎉 Você terminou a prova! Pontuação final: {pontuacao_python}/10")
        ppythonfeita += 1
        
#função python referente a primeira opçao do menu principal
def hardware():
    print("Abrindo apostila de Python!")
    os.startfile("Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
            menu_conteudos()    

#função python referente a primeira opçao do menu principal
def software():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS/Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
        menu_conteudos() 

#função python referente a primeira opçao do menu principal
def cybersegurança():
    print("Abrindo apostila de Python!")
    os.startfile("PDFS/Apostila-de-Python.pdf")
    Voltar = int(input("Tecle 9 para sair "))
    if Voltar == 9:
        menu_conteudos()

    
# chamando a funçao menu principal
menu_conteudos()