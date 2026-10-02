pessoas = []
perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? ",
]

while True:
    sair = False
    print("\nPressione q para sair e [y]/n para responder as perguntas.")
    nome = input("Digite seu nome: ")
    if nome.strip() == "":
        print("Nome inválido...")
        continue
    if nome.lower() == "q":
        break
    pontuacao = 0
    for pergunta in perguntas:
        while True:
            resposta = input(pergunta).strip().lower()
            if resposta == "" or resposta == "y":
                pontuacao += 1
                break
            elif resposta == "n":
                break
            elif resposta == "q":
                sair = True
                break
            else:
                print("Valor não identificado.")
        if sair:
            break
    if sair:
        continue
    else:
        pessoas.append((nome, pontuacao))

def classificar(pessoas: list[tuple[str, int]]) -> list[tuple[str, str]]:
    pessoas_classificadas = []
    for pessoa in pessoas:
        pontos = pessoa[1]
        classificacao = ""
        if pontos in range(2):
            classificacao = "Inocente"
        elif pontos in range(3):
            classificacao = "Suspeita"
        elif pontos in range(5):
            classificacao = "Cúmplice"
        else:
            classificacao = "Assassino"
        pessoas_classificadas.append((pessoa[0], classificacao))
    return pessoas_classificadas

if len(pessoas) < 1:
    print("Nenhuma pessoa foi cadastrada...")
else:
    pessoas_classificacao = classificar(pessoas)
    print("\nClassificações:\n")
    for info in pessoas_classificacao:
        print(f"Nome: {info[0]}\nClassificação: {info[1]}\n")
        
