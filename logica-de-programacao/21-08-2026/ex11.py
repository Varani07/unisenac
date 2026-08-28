"""
Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
                        (Fahrenheit – 32) x 5
Fórmula: Centígrados = ----------------------------
                                    9
"""

fahrenheit = int(input("\nDigite a temperatura em Farenheit: "))
print(f"Coversão para graus centígrados: {round(((fahrenheit - 32) * 5) / 9, 1)}\n")
