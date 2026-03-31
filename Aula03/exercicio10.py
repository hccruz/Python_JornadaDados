### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'produto': 'Celular', 'categoria': 'Eletrônicos', 'valor': 1500},
    {'produto': 'TV', 'categoria': 'Eletrônicos', 'valor': 2000},
    {'produto': 'Computador', 'categoria': 'Eletrônicos', 'valor': 5000},
    {'produto': 'Mesa', 'categoria': 'Móveis', 'valor': 500},
    {'produto': 'Fogão', 'categoria': 'Móveis', 'valor': 1000},
    {'produto': 'Geladeira', 'categoria': 'Móveis', 'valor': 3000},
    {'produto': 'Camisa', 'categoria': 'Vestuário', 'valor': 50},
    {'produto': 'Calça', 'categoria': 'Vestuário', 'valor': 80},
    {'produto': 'Blusa', 'categoria': 'Vestuário', 'valor': 100},
    {'produto': 'Bermuda', 'categoria': 'Vestuário', 'valor': 30}
]

vendas_categoria = {}

for venda in vendas:
    if venda['categoria'] in vendas_categoria:
        vendas_categoria[venda['categoria']] += venda['valor']
    else:
        vendas_categoria[venda['categoria']] = venda['valor']
        
print(vendas_categoria)