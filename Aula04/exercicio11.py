# 11. Atualização de Dados

# Objetivo: Dada uma lista de dicionários representando produtos,
# atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300},
    {"id": 4, "nome": "Computador", "preço": 3000},
    {"id": 5, "nome": "Notebook", "preço": 6500},
    {"id": 6, "nome": "Celular", "preço": 1300}
]

print(produtos)

# Atualizar os preços dos produtos com id 2 para 90 e id 5 para 7500
for produto in produtos:
    if produto['id'] == 2:
        produto['preço'] = 90
    if produto['id'] == 5:
        produto['preço'] = 7500

print(produtos)