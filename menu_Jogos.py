def menu():
    print("Digite seu nome para entrar no Hub de Jogos")
    nome = input("Digite seu nome: ")
    print("Bem Vindo ao meu Hub de Jogos", nome)
    print("Menu de Jogos")
    print("1 - Jogo da forca - ")
    print("2 - Jogo da adivinhação - ")
    print("3 - Voltar ao hub anterior - (em construção) - ")
    print("4 - Sair - ")
    opcao = input("Digite a opção desejada: ")
    print("Você escolheu a opção"), opcao
    if opcao == "1":
        print("Jogo da forca")
    elif opcao == "2":
        print("Jogo da adivinhação")
    elif opcao == "3":
        print("Voltar ao hub anterior")
    elif opcao == "4":
        print("Sair")
    else:
        print("Opção inválida")
    
    def jogo_da_forca():
        print("Jogo da forca")

        print("Fim do jogo") 
menu()