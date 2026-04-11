# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def ordenar_dicionario(dicio: dict) -> list:
    ordenado = []
    for valor in dicionario.keys():
        ordenado.append(valor)
    
    ordenado.sort()
    return ordenado


dicionario = {
    'nome': 'Heraldo', 
    'sobrenome': 'Cruz', 
    'idade': 54, 
    'ano': 1972, 
    'sexo': 'Masculino',
    'cpf': '10769212808',
    'profissão': 'Analista de Dados'
    }

lista_ordenada = ordenar_dicionario(dicionario)

print(lista_ordenada)