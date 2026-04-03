# 10. Divisão de Dados em Grupos

# Objetivo: Dada uma lista de valores, dividir em duas listas:
#     uma para valores pares e outra para ímpares.

numeros = range(1, 101)

pares = [numero for numero in numeros if numero % 2 == 0]

impares = list(set(numeros) - set(pares))

print(f'Pares: {pares}')
print(f'Impares: {impares}')