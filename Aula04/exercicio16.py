# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_numeros(num: list) -> int:
    return sum(num)


lista = [1,2,3,4,5,6,7,8,9,10]

total = soma_numeros(lista)

print(total)