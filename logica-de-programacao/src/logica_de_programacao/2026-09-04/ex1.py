nomes = []

first_break_line = ""
second_break_line = ""

for i in range(1, 6):
    if i != 1:
        first_break_line = ""
    else:
        first_break_line = "\n"
    nomes.append(input(f"{first_break_line}Digite o {i}º nome: "))

for i, nome in enumerate(nomes, 1):
    if i != 1:
        first_break_line = ""
    else:
        first_break_line = "\n"
    if i != 5:
        second_break_line = ""
    else:
        second_break_line = "\n"
    print(f"{first_break_line}{i}: {nome}, quantidade de letras: {len(nome)}{second_break_line}")
