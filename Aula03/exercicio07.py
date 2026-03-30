### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [100, 28, 53, 4, 57, 96, 70, 98, 49, 10]

numeros_normalizados = []

for numero in numeros:
    numeros_normalizados.append(numero / max(numeros))

print(numeros_normalizados)