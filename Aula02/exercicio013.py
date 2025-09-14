# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# Digitar uma frase
frase = input("Digite uma frase: ")

# Remover espaços em branco no início e no final
frase_sem_espacos = frase.strip()

# Imprimir a frase sem espaços em branco no início e no final
print("Frase sem espaços em branco no início e no final:", frase_sem_espacos)
