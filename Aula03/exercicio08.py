### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando

usuarios = [
    {'nome': 'Heraldo', 'idade': 53, 'cpf': '12345678905'},
    {'nome': 'Renata', 'idade': 48, 'cpf': '98765432168'},
    {'nome': 'Giovane', 'idade': 21, 'cpf': None},
    {'nome': 'João', 'idade': 35, 'cpf': None},
    {'nome': 'Maria', 'idade': 45, 'cpf': None},
]

usuarios_validos = [usuario for usuario in usuarios if usuario['cpf'] != None]

print(usuarios_validos)