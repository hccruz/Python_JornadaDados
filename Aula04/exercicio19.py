# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número.
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def pares_numeros(numeros: list, num: int) -> list:
    par_numero = []
    for numero_i in numeros:
        for numero_j in numeros:
            if sum((numero_i, numero_j)) == num:
                par_numero.append((numero_i, numero_j))
    return par_numero
    
    
numeros = range(1, 20)
n = 20
pares = pares_numeros(numeros, n)

print(pares)
