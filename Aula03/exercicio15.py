### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

numeros= range(1, 21)
i = 0

while True:
    if numeros[i] == 12:
        print('Encerrando o programa')
        break
    else:
        print('Processando os dados')
        i += 1
