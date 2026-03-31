### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

intervalo_valido = range(1,3)

while True:
    numero = int(input('Digite um número inteiro: '))
    
    if numero in intervalo_valido:
        print('Entrada válida')
        break
    else:
        print('Entrada inválida')