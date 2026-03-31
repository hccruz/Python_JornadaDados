### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavras = []
while True:
    palavra = input('Digite uma palavra ou digite "sair" para encerrar o programa: ')
    
    if palavra.lower() == 'sair':
        break
    else:
        palavras.append(palavra)

print(palavras)