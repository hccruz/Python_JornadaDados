# 4. Contar ocorrências de caracteres

def contar_letras(frase):
    frase = frase.lower()
    letras = {}
    for letra in frase:
        letras[letra] = letras.get(letra, 0) + 1
    return letras


print(contar_letras('Engenharia de Dados'))