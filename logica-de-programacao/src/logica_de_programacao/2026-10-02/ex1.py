import os

def menu_principal():
    opcoes = ["Finalizar o programa", "Realizar o cadastro de pessoas", "Mostrar a profissão de uma pessoa", "Mostrar todas as pessoas de uma determinada profissão", "Gerar relatório de pessoas e sua profissão"]
    pessoas = []
    profissoes = []

    while True:
        os.system('clear')
        try:
            print("\n==== MENU ====\n")
            for i, opt in enumerate(opcoes):
                print(f"{i} - {opt}.")
            escolha = int(input("\n> "))

            if escolha > len(opcoes) - 1 or escolha < 0:
                raise Exception
            match escolha:
                case 0:
                    break
                case 1:
                    cadastrar_pessoa(pessoas, profissoes)
                case 2:
                    pessoa = escolher_pessoa(pessoas)
                    if pessoa >= 0:
                       mostrar_profissao(pessoa, pessoas, profissoes) 
                       input()
                case 3:
                    profissao = escolher_profissao(profissoes)
                    if profissao != "":
                        mostrar_pessoas_da_profissao_escolhida(pessoas, profissoes, profissao)
                        input()
                case 4:
                    gerar_relatorio(pessoas, profissoes)
        except:
            print("Escolha inválida...")

def cadastrar_pessoa(pessoas: list[str], profissoes: list[str]):
    while True:
        os.system('clear')
        print("\n pressione ENTER para voltar...\n")
        nome = input("Nome: ")
        if nome == "": return
        profissao = input("Profissão: ")
        if profissao == "": return

        if nome in pessoas:
            input(f"\nErro: Registro referente a {nome} já existe...")
            return

        pessoas.append(nome)
        profissoes.append(profissao)
        input("\nPessoa cadastrada com sucesso!")

def escolher_pessoa(pessoas: list[str]) -> int:
    escolha = menu_de_escolha(pessoas, "pessoa")
    return escolha

def mostrar_profissao(id_pessoa: int, pessoas, profissoes: list[str]):
    print(f"\nNome: {pessoas[id_pessoa]}\nProfissão: {profissoes[id_pessoa]}\n")

def escolher_profissao(profissoes: list[str]) -> str:
    profissoes_distintas = list(set(profissoes))
    escolha = menu_de_escolha(profissoes_distintas, "profissão")
    if escolha < 0:
        return ""
    else:
        return profissoes_distintas[escolha]

def mostrar_pessoas_da_profissao_escolhida(pessoas: list[str], profissoes: list[str], profissao: str):
    encontrados = []
    for i, p in enumerate(profissoes):
        if p == profissao:
            encontrados.append(pessoas[i])
    print(f"\n{len(encontrados)} {'pessoas encontradas' if len(encontrados) > 1 else 'pessoa encontrada'} com a profissão: {profissao}\n")
    for pessoa in encontrados:
        print(pessoa)

def gerar_relatorio(pessoas: list[str], profissoes: list[str]):
    if len(pessoas) == 0:
        print("\nNenhuma pessoa foi cadastrada até o momento...\n")
        input()
        return
    os.system('clear')
    for i, pessoa in enumerate(pessoas):
        print(f"\nNome: {pessoa}\nProfissão: {profissoes[i]}\n")
    input()

def menu_de_escolha(conteudo: list[str], tipo: str) -> int:
    if len(conteudo) == 0:
        print(f"\nNenhuma {tipo} foi cadastrada até o momento...\n")
        input()
        return -1
    while True:
        os.system('clear')
        print("\n pressione ENTER para voltar...\n")
        for i, c in enumerate(conteudo, 1):
            print(f"{i} - {c}")
        escolha = input("\nDigite o id: ")
        os.system('clear')
        if escolha == "": return -1
        try:
            escolha = int(escolha)
            if escolha > len(conteudo) or escolha < 1:
                raise Exception
            return escolha - 1
        except:
            print("\nEscolha inválida...\n")
            input()

menu_principal()

