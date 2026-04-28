import csv

path_arquivo = "/media/heraldo/Arquivos/Documentos/JornadaDados/Python_JornadaDados/Aula07/vendas.csv"


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    '''
    Função que lê um arquivo csv e retorna uma lista
    de dicionários
    '''
    
    lista =[]
    with open(nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    
    return lista


def calcular_vendas_categoria(dados: list) -> dict:
    vendas_por_categoria = {}
    for dado in dados:
        if dado.get('Categoria') in vendas_por_categoria.keys():
            vendas_por_categoria[dado.get('Categoria')] += int(dado.get('Quantidade')) * int(dado.get('Venda'))
        else:
            vendas_por_categoria[dado.get('Categoria')] = int(dado.get('Quantidade')) * int(dado.get('Venda'))
    
    return vendas_por_categoria


vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo)

print(vendas_itens)

vendas_categoria = calcular_vendas_categoria(vendas_itens)

for categoria, total in vendas_categoria.items():
    print(f'{categoria}: ${total}')

