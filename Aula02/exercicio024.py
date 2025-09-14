'''
Escreva um programa que solicite ao usuário para digitar um número. 
Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para 
classificar o número como "positivo", "negativo" ou "zero". 
Adicionalmente, identifique se o número é "par" ou "ímpar".
'''

# Digite um número
try:
    numero = float(input("Digite um número: "))
    
    # Classificação do número
    if numero > 0:
        classificacao = "positivo"
    elif numero < 0:
        classificacao = "negativo"
    else:
        classificacao = "zero"
    
    # Verificação de paridade
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
    
    print(f"O número {numero} é {classificacao} e {paridade}.")
except ValueError:
    print("Por favor, digite um valor numérico válido.")
