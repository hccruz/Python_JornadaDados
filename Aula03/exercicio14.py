### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
import time

max_tentativas = 3
tentativa = 1
conexao = False

while tentativa <= max_tentativas:
    print('Tentando conexão ao servidor')
    print(f'Tentativa {tentativa} de {max_tentativas}')
    time.sleep(3)
    
    if conexao:
        print('Conexão reestabelecida')
        break
    else:
        print('Conexão não estabelecida')
        tentativa += 1
else:
    print('Falha ao conectar após vaŕias tentativas')