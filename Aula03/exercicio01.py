'''
Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros 
tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos 
e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
'''

while True:
    quantidade = input("Digite a quantidade de produtos: ")
    preco = input("Digite o preço do produto: ")
    
    preco = preco.replace(',','.')

    if quantidade == "" or preco == "":
        print("Digite valores númericos")
        continue
    
    if quantidade.isalpha() == False and preco.isalpha() == False:
        quantidade = int(quantidade)
        preco = float(preco)
    else:
        print("Digite valores númericos")
        continue

    if quantidade >= 0 and preco >= 0:
        print("Dados válidos")
        break
    else:
        print("Dados inválidos")
        break