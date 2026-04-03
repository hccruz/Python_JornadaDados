# 13. Filtragem de Dados em Dicionário

# Objetivo: Dado um dicionário de estoque de produtos,
# filtrar aqueles com quantidade maior que 0.

estoque = {
    'Teclado': 10,
    'Computador': 5,
    'Mouse': 0,
    'Notebook': 2,
    'Monitor': 3,
    'Celular': 0
}

print(estoque)

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)