### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1,101)


pares = [num for num in numeros if num % 2 == 0]

print(pares)