'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer ValueError.
Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
'''

# Digitar a temperatura em Celsius
celsius = input("Digite a temperatura em Celsius: ")

# Converter para Fahrenheit com tratamento de erro
try:
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para a temperatura em Celsius.")
