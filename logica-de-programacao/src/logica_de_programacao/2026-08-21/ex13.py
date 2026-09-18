"""
Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:
se n <= 10 imprima MENSAGEM 1,
se n > 10 e <= 100 imprima MENSAGEM 2
se n >100 imprima MENSAGEM 3,
"""

numero = int(input("\nDigite um número: "))

if numero > 100:
    print("\nMENSAGEM 3\n")
elif numero > 10:
    print("\nMENSAGEM 2\n")
else:
    print("\nMENSAGEM 1\n")
