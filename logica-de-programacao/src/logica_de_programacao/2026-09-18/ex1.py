from random import randint

lista_int = [randint(5, 50) for _ in range(40)]
while True:
    num = input("Digite um número inteiro (5-50) ou q para sair: ")
    if num.lower() == "q":
        break
    try:
        num = int(num)
    except:
        print(f"'{num}' é inválido, tente novamente.")
        continue
    if num < 5 or num > 50:
        print(f"Número: {num}, fora do alcance delimitado")
        continue
    lista_int.append(num)

if len(lista_int) < 1:
    print("Nenhum número foi informado...")
else:
    print(f"Quantia de números digitados: {len(lista_int)}.")
    print(f"Quantia de números pares: {len([num for num in lista_int if num % 2 == 0])}.")
    print(f"Percentual de números ímpares: {round(len([num for num in lista_int if num % 2 != 0])/len(lista_int)*100, 1)}%.")
    print(f"Quantia de aparições do número 10: {lista_int.count(10)}.")
    print(f"Elementos da lista: {', '.join([str(num) for num in lista_int])}.")
