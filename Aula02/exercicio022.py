'''
Crie um programa que verifica se uma palavra ou frase é um palíndromo
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
Utilize try-except para garantir que a entrada seja uma string.
Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''

# Digite uma palavra ou frase
entrada = input("Digite uma palavra ou frase: ")

# Verifica se a entrada é uma string
try:
    if isinstance(entrada, str):
        # Remove espaços e pontuações, e converte para minúsculas
        entrada_limpa = entrada.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()
        
        # Verifica se é um palíndromo
        if entrada_limpa == entrada_limpa[::-1]:
            print(f'"{entrada}" é um palíndromo.')
        else:
            print(f'"{entrada}" não é um palíndromo.')
    else:
        raise ValueError("A entrada deve ser uma string.")
except ValueError as e:
    print(e)