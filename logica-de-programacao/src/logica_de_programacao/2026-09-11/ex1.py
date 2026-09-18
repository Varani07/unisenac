dados = []

while True:
    nome = input("\nDigite um nome ou ENTER para sair: ")
    if nome == "":
        break

    idade = input("Digite a idade: ")
    try:
        idade = int(idade)
        dados.append((nome, idade))
    except:
        print("\nIdade inválida...")
        continue

if len(dados) == 0:
    print("\nNenhuma pessoa adicionada...\n")
else:
    pessoa_maior_idade = sorted(dados, key=lambda x: x[1], reverse=True)[0]
    pessoas_com_a_mesma_idade = [pessoa[0] for pessoa in dados if pessoa[1] == pessoa_maior_idade[1] and pessoa[0] != pessoa_maior_idade[0]]
    print(f"\nA pessoa mais madura é: {pessoa_maior_idade[0]} com {pessoa_maior_idade[1]} anos.", end="")
    if len(pessoas_com_a_mesma_idade) > 0:
        print(f" Outras pessoas com a mesma idade: {' '.join(pessoas_com_a_mesma_idade)}\n")
    else:
        print("\n")
