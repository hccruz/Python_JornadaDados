# 15. Contagem de Frequência de Itens

# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = 'Sua Jornada de Dados'

frequencia = {}

for letra in texto.lower():
    if letra == ' ':
        continue
    elif letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(frequencia)
