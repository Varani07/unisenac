"""
Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
                                    (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
                                                        soma dos pesos
"""

nota_1 = int(input("\nDigite a primeira nota: "))
peso_1 = int(input("Digite o primeiro peso: "))
nota_2 = int(input("Digite a segunda nota: "))
peso_2 = int(input("Digite o segundo peso: "))

print(f"\nResultado Média Ponderada: {((nota_1 * peso_1) + (nota_2 * peso_2)) / peso_1 + peso_2}\n")
