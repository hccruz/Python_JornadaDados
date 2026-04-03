# 14. Extração de Chaves e Valores

# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

estoque = {
    'Teclado': 10,
    'Computador': 5,
    'Mouse': 0,
    'Notebook': 2,
    'Monitor': 3,
    'Celular': 0
}

chaves = list(estoque.keys())
valores = list(estoque.values())

print(f'Chaves: {chaves}')
print(f'Valores: {valores}')