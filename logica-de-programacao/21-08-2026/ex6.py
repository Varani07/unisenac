"""
Fazer um algoritmo para ler dois números e mostrar o maior deles.
"""

numbers = []

for i in range(1, 3):
    numbers.append(int(input(f"Informe o {i}° número: ")))

print(f"\nO maior número informado foi {max(numbers)}.\n")
