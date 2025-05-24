#cor
from rich.console import Console 
from rich.text import Text 

Console = Console()

#introdução

def introducao():
    Console.print("[bold gold3]Ola seja bem-vindos ao guia de hardware![/bold gold3]")


#resumindo hardware
    texto = Text("""Hardware é todo componente físico, interno ou externo do seu computador,
ou celular, que determina do que um dispositivo é capaz e como você pode usá-lo.
Embora dependa de um software para funcionar (e vice-versa), o hardware é um elemento a parte e 
igualmente importante.""") 
    texto.justify = "left"
    
    Console.print(texto)

    while True:

        tecla = input("Pressione [H] para continuar.").strip().upper()
        if tecla == "H":
            break
        else:
            Console.print("[bold red]Entrada inválida. Tente novamente.[/bold red]")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
#menu

def menu():
    while True:

        Console.print("[bold green]¨¨¨¨¨¨ MENU DE HARDWARE ¨¨¨¨¨¨[/bold green]")
        Console.print("[bold yellow] [1] [/bold yellow] O que é Hardware?")
        Console.print("[bold yellow] [2] [/bold yellow] Os componentes de Hardware")
        Console.print("[bold yellow] [3] [/bold yellow] Processadores")
        Console.print("[bold yellow] [4] [/bold yellow] Memoria RAM e ROM")
        Console.print("[bold yellow] [5] [/bold yellow] Armazenamento (HDD e SSD)")
        Console.print("[bold yellow] [6] [/bold yellow] Periféricos")
        Console.print("[bold red] [0] [/bold red] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_oque_e_hardware()
        elif opcao == "2":
            mostrar_comoponentes()
        elif opcao == "3":
            mostrar_processadores()
        elif opcao == "4":
            mostrar_memoria()
        elif opcao == "5":
            mostrar_armazenamento()
        elif opcao == "6":
            mostar_perifericos()
        elif opcao == "0":
            print("Saindo... Volte Sempre!!!")
            break
        else:
            Console.print("[bold red]Desculpe, esta opção não esxiste. Tente novamente.[/bold red]")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def esperar_voltar_menu():
    while True:
        tecla = input("Pressione [X] para voltar ao menu: ").strip().upper()
        if tecla == "X":
            break
        else:
            Console.print("[bold red] OPS!. Entrada invalida. Tente novamente.[/bold red]")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_oque_e_hardware():
    Console.print("[bold cyan]¨¨¨¨¨¨ O QUE É HARDWARE ¨¨¨¨¨¨[/bold cyan]")
    print("""Hardware é todo componente físico, interno ou externo do seu computador, ou celular, 
que determina do que um dispositivo é capaz e como você pode usá-lo.""")
    print("""o conceito se aplica aos componentes de dispositivos em geral, 
como processador, placa-mãe, memória RAM, unidades de armazenamento (HDs, SSDs e memória Flash), 
bem como a dispositivos de entrada e saída (teclado, mouse, monitor, caixas de som, controle remoto, controle de videogame, etc).""")
    esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_comoponentes():
    Console.print("[bold green]¨¨¨¨¨¨ COMPONENTES DE HARDWARE ¨¨¨¨¨¨[/bold green]")
    print("Os ptincipais componentes São:")
    Console.print("[bold yellow]- Placa-mãe:[/bold yellow] É uma peça central responsável por conectar e interligar todos os componentesÉ uma peça central responsável por conectar e interligar todos os componentes")
    Console.print("[bold yellow]- Processador:[/bold yellow] A sua função é acelerar, endereçar, resolver ou preparar dados, dependendo da aplicação.")
    Console.print("[bold yellow]- Memória RAM:[/bold yellow] A RAM é usada para armazenar informações que precisam ser usadas rapidamente.")
    Console.print("[bold yellow]- Armazenamento (HDD/SDD):[/bold yellow] são dispositivos de armazenamento de dados que podem ser usados para guardar arquivos, programas e o sistema operacional.")
    esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_processadores():
        Console.print("[bold purple]¨¨¨¨¨¨ PROCESSADORES (CPU) ¨¨¨¨¨¨[/bold purple]")
        print("- O processador é considerado o cérebro do computador.")
        print("- Pois é o componente que executa todas as instruções que o sistema precisa para funcionar.")
        Console.print("[bold yellow]- Exemplos:[/bold yellow] Intel Core, AMD Ryzen, Apple Silicon, Nvidia GeForce, Samsung Exynos, e Qualcomm Snapdragon.")
        esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_memoria():
    Console.print("[bold blue]¨¨¨¨¨¨ MEMÓRIA RAM E ROM ¨¨¨¨¨¨[/bold blue]")
    Console.print("[bold yellow]- memória RAM:[/bold yellow] RAM é a memória volátil que armazena temporariamente os arquivos com os quais você está trabalhando.")
    Console.print("[bold yellow]- Memória ROM:[/bold yellow] ROM é a memória não volátil que armazena permanentemente as instruções no seu computador.")
    esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_armazenamento():
    Console.print("[bold violet]¨¨¨¨¨¨ ARMAZENAMENTO (HDD E SSD) ¨¨¨¨¨¨[/bold violet]")
    Console.print("[bold yellow]- HDD (Hard Disk Drive):[/bold yellow] Mais barato, mas lento")
    Console.print("[bold yellow]- SSD (Solid State Drive):[/bold yellow] Mais rápido e eficiente, e mais caro.")
    esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostar_perifericos():
    Console.print("[bold cyan]¨¨¨¨¨¨ PERIFÉRICOS ¨¨¨¨¨¨[/bold cyan]")
    Console.print("[bold yellow]- Entrada:[/bold yellow] Teclado e mouse.")
    Console.print("[bold yellow]- Saida:[/bold yellow] Monitor, impressora e caixas de som.")
    esperar_voltar_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#inicar o programa
introducao()
menu()