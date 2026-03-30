### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = 'Hoje é a nossa terceira aula do bootcamp, bootcamp de python'

texto = texto.replace(',', '')
palavras = texto.lower().split()

print(palavras)

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)