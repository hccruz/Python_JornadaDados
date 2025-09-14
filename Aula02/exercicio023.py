'''
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /)
do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
Imprima o resultado ou uma mensagem de erro apropriada.
'''

# Digite o primeiro número
try:
    num1 = float(input("Digite o primeiro número: "))
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira um número válido.")
    exit()

# Digite o segundo número
try:
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira um número válido.")
    exit()

# Digite o operador
try:
    operador = input("Digite o operador (+, -, *, /): ")
    if operador not in ['+', '-', '*', '/']:
        raise ValueError("Operador inválido.")
except ValueError as e:
    print(f"Erro: {e}")
    exit()

# Realiza a operação com base no operador fornecido
try:
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        resultado = num1 / num2
    print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
except ZeroDivisionError as e:
    print(f"Erro: {e}") 
