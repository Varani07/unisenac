"""
Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.

Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.
"""

distancia = int(input("\nDigite a distância: "))
consumo = int(input("Digite o consumo: "))
preco = float(input("Digite o valor do litro de combustível: R$"))

quantia_combustivel_lt = distancia / consumo
print(f"\nA quantia de litros de combustível para a viagem é: {round(quantia_combustivel_lt, 2)} litros\nCusto da viagem: R${round(quantia_combustivel_lt * preco, 2)}\n")

# 43 litros
# R$195,00
