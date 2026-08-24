"""
Ler 3 números e imprimi-los em ordem crescente.
"""

numbers = []

for i in range(1, 4):
    numbers.append(int(input(f"Informe o {i}º número: ")))

print()

numbers.sort()
for n in numbers:
    print(n)

print()
