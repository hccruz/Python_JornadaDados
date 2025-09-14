# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# Insirir a expressão booleana
valor1 = input("Digite o primeiro valor booleano (True/False): ")

# Insirir a expressão booleana
valor2 = input("Digite o segundo valor booleano (True/False): ")

# Avaliar as expressões booleanas com o operador OR
resultado = eval(valor1) or eval(valor2)

# Exibir o resultado
print("O resultado da operação OR entre", valor1, "e", valor2, "é:", resultado)
