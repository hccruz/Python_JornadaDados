import csv

# Caminho para o arquivo CSV
caminho_arquivo: str = '/media/heraldo/Arquivos/Documentos/JornadaDados/Python_JornadaDados/Aula04/exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados: list = []

# Usa o gerenciador de contexto 'with' para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
    # Cria um objeto leitor de CSV
    leitor_csv: csv.DictReader = csv.DictReader(file)

    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        dados.append(linha)

print(dados)