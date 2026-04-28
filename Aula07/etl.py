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


def calcular_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria in dados:
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    
    return vendas_por_categoria


vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo)

print(vendas_itens)

vendas_categoria = calcular_vendas_categoria(vendas_itens)
for categoria, total in vendas_categoria:
    print(f'{categoria}: ${total}')

