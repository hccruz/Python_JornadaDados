# import pandas as pd
import os
import glob

# Uma função de extract que lê e consolida os jsons

pasta = '/media/heraldo/Arquivos/Documentos/JornadaDados/Python_JornadaDados/Aula08/data'
arquivos_json = glob.glob(os.path.json(pasta, '*.json'))
print(arquivos_json)

# Uma função que transforma

# Uma função que da load em csv ou parquet