"""
Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.
"""

numeros = []

for i in range(1, 6):
    numeros.append(int(input(f"Digite o {i}° número: ")))

print(f"\nA soma e média do conjunto de números informados é:\n\nSoma: {sum(numeros)}\nMédia: {sum(numeros)/len(numeros)}\n")
