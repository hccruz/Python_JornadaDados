# 7. Filtragem de Dados

# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [11, 27, 15, 85, 62, 53, 9, 5, 35, 48]

idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)
