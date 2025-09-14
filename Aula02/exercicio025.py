'''
Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
O programa deve converter a string de entrada em uma lista de números inteiros. 
Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista 
convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, 
imprima a lista de inteiros.
'''

# Solicita ao usuário uma lista de números inteiros separados por vírgula
entrada = input("Digite uma lista de números inteiros separados por vírgula: ")

# Divide a string em uma lista de substrings
elementos = entrada.split(',')

# Lista para armazenar os números inteiros convertidos
numeros_inteiros = []
try:
    for elemento in elementos:
        # Remove espaços em branco e tenta converter cada elemento para inteiro
        numero = int(elemento.strip())
        numeros_inteiros.append(numero)
    
    print("Lista de números inteiros:", numeros_inteiros)
except ValueError:
    print("Erro: Certifique-se de que todos os elementos são números inteiros válidos.")
