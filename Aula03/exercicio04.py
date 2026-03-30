### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = input('Digite a sua idade: ')
email = input('Digite o seu email: ')

idade = idade.strip()
email = email.strip()

try:
    # Conventer string para inteiro
    idade_int = int(idade)
    
    if idade_int >= 18 and idade_int <= 65:
        if '@' in email or '.' in email:
            print('Dados de usuário válidos')
        else:
            print('Email inválido')
    else:
        print('A idade deve estar entre 18 e 65 anos.')
        
except ValueError:
    # Mensagem executada se a exceção ValueError for levantada
    print('A idade não pode ter letras.')
