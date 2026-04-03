# 5. Preço total da lista de compras

lista_compras: list = ['maçã', 'banana', 'cereja', 'laranja', 'abacate']

precos: dict = {'maçã': 2.10, 'banana': 1.35, 'cereja': 2.05, 'laranja': 1.99, 'abacate': 3.50}

total: float = sum(precos[item] for item in lista_compras)

print(f'Preço total = {total}')