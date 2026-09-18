nomes = []

break_line = "\n"
while True:
    nome = input(f"{break_line}Digite o nome de uma pessoa ou q para sair do loop: ")
    if nome.lower() == "q":
        match input("Confirma [y/n]: ").lower():
            case "y":
                break
            case "n":
                continue
            case _:
                print("Valor não identificado...")
                continue
    nomes.append(nome)
    break_line = ""

break_line = "\n"
for i, nome in enumerate(nomes, 1):
    print(f"{break_line}{i}° nome: {nome}, quantidade de caracteres: {len(nome)}")
    break_line = ""

print()
