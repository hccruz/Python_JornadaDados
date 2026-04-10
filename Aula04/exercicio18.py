# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def invertida(frase: str) -> str:
    return frase[::-1]


texto = input('Digite um texto: ')

texto_inverso = invertida(texto)

print(texto_inverso)