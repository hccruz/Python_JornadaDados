# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

# Digitar o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcular a área do círculo
area = math.pi * (raio ** 2)

# Exibir o resultado
print(f"A área do círculo com raio {raio} é: {area:.2f}")
