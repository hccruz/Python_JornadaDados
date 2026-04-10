# 17. Crie uma função que receba um número como argumento e 
# retorne True se o número for primo e False caso contrário.

def numero_primo(num: int) -> bool:
    for i in range(2, num + 1):
        if num % i == 0 and num != i:
            return False
    return True
        
        
numero = int(input('Digite um número inteiro: '))

eh_primo = numero_primo(numero)

print(eh_primo)