import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None
        
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        
    def filtrar_por(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado
    
    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]
    
    
arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro, limite))
print(arquivo_CSV.sub_filtro('preço', '10,50'))
# print(arquivo_CSV.df)

# arquivo_csv = './exemplo2.csv'
# filtro = 'estado'
# limite = 'DF'

# arquivo_CSV2 = CsvProcessor(arquivo_csv)
# arquivo_CSV2.carregar_csv()
# print(arquivo_CSV2.filtrar_por(filtro, limite))