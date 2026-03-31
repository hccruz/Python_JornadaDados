### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [100, 28, 53, 4, 57, 96, 70, 98, 49, 10]

x_max = max(numeros)
x_min = min(numeros)

numeros_normalizados = []

for numero in numeros:
    x_norm = (numero - x_min) / (x_max - x_min)
    numeros_normalizados.append(x_norm)

print(numeros_normalizados)