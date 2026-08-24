"""
Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
"""

vA = input("Digite o primeiro número: ")
vB = input("Digite o segundo número: ")

print(f"vA = {vA}, vB = {vB}")

vA, vB = vB, vA

print(f"vA = {vA}, vB = {vB}")
