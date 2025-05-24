# -*- coding: utf-8 -*-
"""
Programa de Ensino para Crianças Carentes
Disciplinas: Python Básico, Hardwares, Softwares, Cibersegurança
Funcionalidades:
 - Login e criação de conta (autenticação via JSON com senha criptografada SHA-256)
 - Menu principal com opções: Disciplinas, Notas, Termos, Privacidade, Sair
 - Em Disciplinas: conteúdos (PDFs) e opção de prova (cada prova pode ser feita apenas uma vez)
 - Provas de múltipla escolha (10 questões) com confirmação antes de iniciar
 - Salvamento de nota final de cada disciplina em JSON, por usuário
 - No menu Notas: cálculo de média, moda e mediana
 - Termos de uso e Política de Privacidade exibidos no menu
 - No terminal, PDFs são abertos no aplicativo padrão do sistema
Tudo documentado em português.
"""
import json
import os
import statistics
import subprocess
import sys
import hashlib

# --- Constantes e Arquivos ---
ARQUIVO_CONTAS = 'contas.json'
ARQUIVO_NOTAS = 'notas.json'
DISCIPLINAS = ['Python Básico', 'Hardwares', 'Softwares', 'Cibersegurança']
NUM_QUESTOES = 10

# --- Banco de Questões ---
QUESTOES = {
    'Python Básico': [
        {'enunciado': 'O que faz o comando `print()` em Python?', 'opcoes': {'A': 'Lê dados do usuário', 'B': 'Imprime texto na tela', 'C': 'Cria variáveis', 'D': 'Executa cálculos automaticamente'}, 'resposta': 'B'},
        {'enunciado': 'Qual operador lógico em Python significa “e” lógico?', 'opcoes': {'A': '&', 'B': 'and', 'C': '&&', 'D': 'E'}, 'resposta': 'B'},
        {'enunciado': 'Qual valor é considerado False em uma condição?', 'opcoes': {'A': '0', 'B': '1', 'C': '"False"', 'D': 'Todas as anteriores'}, 'resposta': 'A'},
        {'enunciado': 'Como você verifica se duas variáveis x e y são iguais?', 'opcoes': {'A': 'x = y', 'B': 'x == y', 'C': 'x === y', 'D': 'x equals y'}, 'resposta': 'B'},
        {'enunciado': 'Qual estrutura é usada para escolher entre duas ações?', 'opcoes': {'A': 'for', 'B': 'while', 'C': 'if/else', 'D': 'switch'}, 'resposta': 'C'},
        {'enunciado': 'O que faz o operador `%` em Python?', 'opcoes': {'A': 'Divisão inteira', 'B': 'Potenciação', 'C': 'Resto da divisão', 'D': 'Multiplicação'}, 'resposta': 'C'},
        {'enunciado': 'Em Python, qual resultado de `bool("")`?', 'opcoes': {'A': 'True', 'B': 'False', 'C': 'Erro', 'D': 'None'}, 'resposta': 'B'},
        {'enunciado': 'Como se escreve um comentário de múltiplas linhas?', 'opcoes': {'A': '# Comentário', 'B': '/* Comentário */', 'C': '"""Comentário"""', 'D': '// Comentário'}, 'resposta': 'C'},
        {'enunciado': 'Qual expressão verifica se x é maior que 10 ou y menor que 5?', 'opcoes': {'A': 'x > 10 or y < 5', 'B': 'x > 10 || y < 5', 'C': 'x gt 10 or y lt 5', 'D': 'if x > 10, y < 5'}, 'resposta': 'A'},
        {'enunciado': 'Em Python, o que retorna `len([1, 2, 3])`?', 'opcoes': {'A': '2', 'B': '3', 'C': '1', 'D': 'Erro'}, 'resposta': 'B'}
    ],
    'Hardwares': [
        {'enunciado': 'Qual componente é considerado o “cérebro” do computador?', 'opcoes': {'A': 'Placa-mãe', 'B': 'Disco Rígido', 'C': 'Processador', 'D': 'Memória RAM'}, 'resposta': 'C'},
        {'enunciado': 'Qual tipo de memória é volátil e perde dados ao desligar?', 'opcoes': {'A': 'ROM', 'B': 'RAM', 'C': 'SSD', 'D': 'HD'}, 'resposta': 'B'},
        {'enunciado': 'O que faz a unidade de fonte de alimentação (PSU)?', 'opcoes': {'A': 'Armazenar dados', 'B': 'Fornecer energia elétrica', 'C': 'Controlar a temperatura', 'D': 'Executar programas'}, 'resposta': 'B'},
        {'enunciado': 'Qual componente armazena dados permanentemente?', 'opcoes': {'A': 'RAM', 'B': 'Cache', 'C': 'HD/SSD', 'D': 'BIOS'}, 'resposta': 'C'},
        {'enunciado': 'A placa-mãe é responsável por:', 'opcoes': {'A': 'Armazenar arquivos', 'B': 'Interligar componentes', 'C': 'Executar instruções', 'D': 'Configurar antivírus'}, 'resposta': 'B'},
        {'enunciado': 'O BIOS é um firmware que:', 'opcoes': {'A': 'Carrega o sistema operacional', 'B': 'Realiza backups', 'C': 'Gerencia antivírus', 'D': 'Edita fotos'}, 'resposta': 'A'},
        {'enunciado': 'Qual slot de expansão é usado por placas de vídeo modernas?', 'opcoes': {'A': 'PCI', 'B': 'PCIe', 'C': 'AGP', 'D': 'ISA'}, 'resposta': 'B'},
        {'enunciado': 'O que é um socket de processador?', 'opcoes': {'A': 'Uma memória cache', 'B': 'Um padrão de encaixe', 'C': 'Um tipo de disco', 'D': 'Uma interface de rede'}, 'resposta': 'B'},
        {'enunciado': 'Qual a principal diferença entre HD e SSD?', 'opcoes': {'A': 'SSD é mecânico, HD é sólido', 'B': 'HD é mais rápido', 'C': 'SSD usa memória flash', 'D': 'HD usa memória flash'}, 'resposta': 'C'},
        {'enunciado': 'As memórias cache servem para:', 'opcoes': {'A': 'Armazenar dados de longa duração', 'B': 'Guardar arquivos do usuário', 'C': 'Acelerar acesso do processador', 'D': 'Executar programas antivírus'}, 'resposta': 'C'}
    ],
    'Softwares': [
        {'enunciado': 'O que é software de sistema?', 'opcoes': {'A': 'Programa que gerencia hardware', 'B': 'Programa de edição de texto', 'C': 'Programa de jogo', 'D': 'Programa de antivírus'}, 'resposta': 'A'},
        {'enunciado': 'O que é software de aplicação?', 'opcoes': {'A': 'Programa que gerencia hardware', 'B': 'Programa de usuário para tarefas específicas', 'C': 'Sistema operacional', 'D': 'Firmware de placa-mãe'}, 'resposta': 'B'},
        {'enunciado': 'Qual dos seguintes é um exemplo de software de sistema?', 'opcoes': {'A': 'Microsoft Word', 'B': 'Linux', 'C': 'Photoshop', 'D': 'Excel'}, 'resposta': 'B'},
        {'enunciado': 'Qual dos seguintes é um exemplo de software de aplicação?', 'opcoes': {'A': 'Windows 10', 'B': 'Ubuntu Server', 'C': 'Google Chrome', 'D': 'BIOS'}, 'resposta': 'C'},
        {'enunciado': 'O que caracteriza um software livre?', 'opcoes': {'A': 'Gratuito para download', 'B': 'Acesso ao código-fonte e liberdade de alteração', 'C': 'Pago e licenciado', 'D': 'Só executa em Linux'}, 'resposta': 'B'},
        {'enunciado': 'Qual não é uma liberdade do software livre?', 'opcoes': {'A': 'Executar para qualquer propósito', 'B': 'Estudar e modificar o código-fonte', 'C': 'Redistribuir cópias', 'D': 'Vender hardware junto'}, 'resposta': 'D'},
        {'enunciado': 'O que é freeware?', 'opcoes': {'A': 'Software gratuito, mas sem acesso ao código-fonte', 'B': 'Software livre com código aberto', 'C': 'Shareware de avaliação', 'D': 'Software pago por assinatura'}, 'resposta': 'A'},
        {'enunciado': 'Qual programa é utilitário de sistema?', 'opcoes': {'A': 'WinRAR', 'B': 'GIMP', 'C': 'Steam', 'D': 'Spotify'}, 'resposta': 'A'},
        {'enunciado': 'Qual software é usado para criar planilhas eletrônicas?', 'opcoes': {'A': 'Word', 'B': 'Excel', 'C': 'PowerPoint', 'D': 'Outlook'}, 'resposta': 'B'},
        {'enunciado': 'Qual a função principal de um sistema operacional?', 'opcoes': {'A': 'Editar vídeos', 'B': 'Gerenciar recursos de hardware e software', 'C': 'Desenvolver aplicativos', 'D': 'Enviar e-mails automaticamente'}, 'resposta': 'B'}
    ],
    'Cibersegurança': [
        {'enunciado': 'Quem é responsável pela segurança cibernética na empresa?', 'opcoes': {'A': 'O departamento de marketing', 'B': 'A equipe de vendas', 'C': 'A gestão da empresa', 'D': 'Os clientes'}, 'resposta': 'C'},
        {'enunciado': 'Você usa programas antivírus em todos os dispositivos?', 'opcoes': {'A': 'Sim, sempre atualizados', 'B': 'Não, antivírus não é necessário', 'C': 'Apenas em servidores', 'D': 'Apenas em computadores pessoais'}, 'resposta': 'A'},
        {'enunciado': 'Quão bem você conhece seus sistemas de TI e dados vitais?', 'opcoes': {'A': 'Não conheço nada', 'B': 'Conheço parcialmente', 'C': 'Tenho inventário completo', 'D': 'Conheço só o hardware'}, 'resposta': 'C'},
        {'enunciado': 'Você realiza backups de dados periodicamente?', 'opcoes': {'A': 'Sim, com frequência definida', 'B': 'Só quando lembro', 'C': 'Nunca fiz backup', 'D': 'Somente manualmente'}, 'resposta': 'A'},
        {'enunciado': 'Você aplica atualizações de sistema e software assim que são lançadas?', 'opcoes': {'A': 'Sempre imediatamente', 'B': 'Raramente', 'C': 'Nunca atualizo', 'D': 'Só uma vez por ano'}, 'resposta': 'A'},
        {'enunciado': 'Você desativou macros em documentos para evitar malwares?', 'opcoes': {'A': 'Sim, macros estão proibidos', 'B': 'Macros ativados por padrão', 'C': 'Desativo só em PDFs', 'D': 'Não sei o que são macros'}, 'resposta': 'A'},
        {'enunciado': 'Você tem uma política de senhas seguras e autenticação multifator?', 'opcoes': {'A': 'Sim, política e MFA', 'B': 'Só senhas simples', 'C': 'Só MFA', 'D': 'Não há política'}, 'resposta': 'A'},
        {'enunciado': 'Como você protege suas contas de e-mail contra phishing?', 'opcoes': {'A': 'Usando scanner antivírus', 'B': 'Ignorando e-mails', 'C': 'Sem proteção especial', 'D': 'Compartilhando senha com colegas'}, 'resposta': 'A'},
        {'enunciado': 'Você separa contas de administrador de contas de usuário comuns?', 'opcoes': {'A': 'Sim, separadas', 'B': 'Todos são administradores', 'C': 'Não existe distinção', 'D': 'Só uso conta convidado'}, 'resposta': 'A'},
        {'enunciado': 'Você controla riscos de TI em home office e viagens de negócios?', 'opcoes': {'A': 'Sim, uso VPN e criptografia', 'B': 'Não controlo nada', 'C': 'Só em viagens', 'D': 'Apenas em home office'}, 'resposta': 'A'}
    ]
}

# --- PDFs de Conteúdo ---
PDFS_CONTEUDO = {
    'Python Básico': [r'PDFS\\EBOOK - INTRODUÇÃO A PYTHON (EDITORA IFRN).pdf'],
    'Hardwares': [r'PDFS\\HARDWARE.pdf'],
    'Softwares': [r'PDFS\\SISTEMAS OPERACIONAIS.pdf', r'PDFS\\SOFTWARES DE SISTEMAS E DE APLICAÇÕES AOS NEGOCIOS.pdf'],
    'Cibersegurança': [r'PDFS\\CIBERSEGURANÇA.pdf']
}

# --- Termos e Privacidade ---
TERMOS_USO = (
    "Este software é destinado ao uso educacional de crianças carentes. "
    "Não nos responsabilizamos por uso indevido. Ao prosseguir, você concorda em usar o programa apenas para fins de estudo."
)
PRIVACIDADE = (
    "Coletamos apenas nome de usuário e senha criptografada para autenticação. "
    "Nenhum dado pessoal será compartilhado com terceiros. "
    "As notas são armazenadas localmente em JSON."
)

# --- Funções de Persistência ---
def carregar_json(caminho, valor_padrao):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return valor_padrao


def salvar_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- Gerenciamento de Contas ---
def criar_conta():
    contas = carregar_json(ARQUIVO_CONTAS, [])
    nome_completo = input('Digite seu nome completo: ').strip()
    if not nome_completo:
        print('⚠️ Nome não pode ser vazio!')
        return None
    while True:
        usuario = input('Escolha um nome de usuário (único): ').strip()
        if not usuario:
            print('⚠️ Nome de usuário não pode ser vazio!')
        elif any(c['usuario'].lower() == usuario.lower() for c in contas):
            print('⚠️ Nome de usuário já existe!')
        else:
            break
    while True:
        senha = input('Digite uma senha: ').strip()
        senha_conf = input('Confirme sua senha: ').strip()
        if senha != senha_conf:
            print('⚠️ Senhas não conferem. Tente novamente.')
        else:
            break
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    contas.append({'usuario': usuario, 'senha_hash': hash_senha, 'nome_completo': nome_completo})
    salvar_json(ARQUIVO_CONTAS, contas)
    print('✅ Conta criada com sucesso.')
    return {'usuario': usuario, 'nome_completo': nome_completo}


def autenticar():
    contas = carregar_json(ARQUIVO_CONTAS, [])
    usuario = input('Nome de usuário: ').strip()
    senha = input('Senha: ').strip()
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    for c in contas:
        if c['usuario'].lower() == usuario.lower() and c.get('senha_hash') == hash_senha:
            print('✅ Autenticado com sucesso.')
            return c
    print('❌ Usuário ou senha incorretos.')
    return None

# --- Funções de PDF ---
def listar_pdfs(disciplina):
    arquivos = PDFS_CONTEUDO.get(disciplina, [])
    if not arquivos:
        print('Nenhum material disponível.')
        return
    print(f"\nMateriais de {disciplina}:")
    for i, pdf in enumerate(arquivos, start=1):
        print(f"{i}. {os.path.basename(pdf)}")
    escolha = input('Digite o número do PDF para abrir (ou Enter para voltar): ').strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(arquivos):
        path = arquivos[int(escolha)-1]
        if os.path.exists(path):
            if sys.platform.startswith('win'):
                os.startfile(path)
            else:
                subprocess.run(['xdg-open', path])
        else:
            print('Arquivo não encontrado:', path)

# --- Estatísticas de Notas ---
def calcular_estatisticas():
    notas = carregar_json(ARQUIVO_NOTAS, {})
    todas = []
    for lista in notas.values():
        if isinstance(lista, dict):
            todas.extend(lista.values())
        else:
            todas.extend(lista)
    if not todas:
        print('Nenhuma nota registrada.')
        return
    media = statistics.mean(todas)
    try:
        moda = statistics.mode(todas)
    except statistics.StatisticsError:
        moda = 'Não há moda única.'
    mediana = statistics.median(todas)
    print(f"Média: {media:.2f}\nModa: {moda}\nMediana: {mediana}")

# --- Funções de Prova ---
def fazer_prova(disciplina, conta):
    notas = carregar_json(ARQUIVO_NOTAS, {})
    usuario = conta['usuario']
    notas.setdefault(disciplina, {})
    if usuario in notas[disciplina]:
        print(f"Você já realizou a prova de {disciplina}. Pontuação: {notas[disciplina][usuario]}")
        return
    questoes = QUESTOES.get(disciplina, [])
    if len(questoes) < NUM_QUESTOES:
        print('⚠️ Banco de questões incompleto.')
        return
    if input(f"Iniciar prova de {disciplina}? (s/n): ").strip().lower() != 's':
        return
    pont = 0
    for i, q in enumerate(questoes[:NUM_QUESTOES], 1):
        print(f"\n{i}. {q['enunciado']}")
        for opc, txt in q['opcoes'].items(): print(f"{opc}) {txt}")
        if input('Resp: ').strip().upper() == q['resposta']:
            pont += 1
    print(f"Sua pontuação: {pont}/{NUM_QUESTOES}")
    notas[disciplina][usuario] = pont
    salvar_json(ARQUIVO_NOTAS, notas)

# --- Função Principal ---
def main():
    print('=== Bem-vindo ao Programa Educacional ===')
    conta = None
    while not conta:
        print('\n1. Login\n2. Criar Conta\n3. Sair')
        esc = input('Opção: ').strip()
        if esc == '1':
            conta = autenticar()
        elif esc == '2':
            conta = criar_conta()
        elif esc == '3':
            print('Até logo!')
            return
        else:
            print('Opção inválida.')
    primeiro = conta['nome_completo'].split()[0]
    while True:
        print(f"\n=== Menu (Usuário: {primeiro}) ===")
        print('1. Disciplinas\n2. Notas\n3. Termos\n4. Privacidade\n5. Sair')
        op = input('Selecione: ').strip()
        if op == '1':
            print('\n--- Disciplinas ---')
            for i, d in enumerate(DISCIPLINAS,1): print(f"{i}. {d}")
            s = input('Disciplina: ').strip()
            if s.isdigit() and 1 <= int(s) <= len(DISCIPLINAS):
                d = DISCIPLINAS[int(s)-1]
                print(f"\nConteúdo de {d}:")
                print('1. Ver Conteúdo\n2. Fazer Prova\n3. Voltar')
                sub = input('Opção: ').strip()
                if sub == '1':
                    listar_pdfs(d)
                elif sub == '2':
                    fazer_prova(d, conta)
        elif op == '2':
            calcular_estatisticas()
        elif op == '3':
            print(f"\n--- Termos de Uso ---\n{TERMOS_USO}")
        elif op == '4':
            print(f"\n--- Política de Privacidade ---\n{PRIVACIDADE}")
        elif op == '5':
            print('Até logo!')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
