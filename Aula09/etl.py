import pandas as pd
import os
import glob
from utils_log import log_decorator


# Função de extract que lê e consolida os jsons
@log_decorator
def extrair_dados_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Função que transforma
@log_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df
    

# Função que da load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, format_exit: list):
    '''
    Parâmetro que vai ser ou "csv" ou "parquet" ou "os dois"
    '''
    
    for formato in format_exit:
        if formato == 'csv':
            df.to_csv('dados.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados.parquet', index=False)


# Função para o pipeline da etl
@log_decorator
def pipeline_calcular_kpi_vendas_consolidado(pasta: str, formato_saida: list):
    data_frame = extrair_dados_consolidar(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_saida)

    