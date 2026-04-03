# 12. Fusão de Dicionários

# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario01 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dicionario02 = {'e': 5, 'f': 6, 'g': 7, 'h': 8}

dicionario_unido = {**dicionario01, **dicionario02}

print(dicionario_unido)
