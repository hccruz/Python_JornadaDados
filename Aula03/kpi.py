# KPI - Key Performance Indicator

# Calcular o salário total de um usuário com base no salário e bônus fornecidos

# Constante do bônus fixo
BONUS_FIXO = 1000

# Entre com o nome do usuário.
while True:
    try:
        nome = input('Digite o nome do usuário: ')
        
        nome_usuario = nome.isspace()
        
        if any(char.isdigit() for char in nome):
            raise ValueError('O nome não pode conter números.')
        elif len(nome) == 0:
            raise ValueError('O nome deve conter ao menos um caractere.')
        elif nome_usuario:
            raise ValueError('O nome não pode conter apenas espaços em branco.')
        else:
            break
    except ValueError as e:    
        print(e)

# Entre com o salário do usuário.   
while True:
    
    try:
        salario = input('Digite o salário do usuário: ')

        salario = salario.replace(',', '.')
        
        salario = float(salario)
    except ValueError as e:    
        print('O salário não pode conter letras ou caracteres inválidos.')
        continue

    try:
        if salario < 0:
            raise ValueError('O salário não pode ser negativo.')
        elif salario == 0:
            raise ValueError('O salário não pode ser zero.')
        else:
            break
    except ValueError as e:    
        print(e)


# Entre com o bônus do usuário.
while True:
    
    try:
        bonus = input('Digite o bônus do usuário: ')

        bonus = bonus.replace(',', '.')
        
        bonus = float(bonus)
    except ValueError as e:    
        print('O bônus não pode conter letras ou caracteres inválidos.')
        continue

    try:
        if bonus < 0:
            raise ValueError('O bônus não pode ser negativo.')
        elif bonus == 0:
            raise ValueError('O bônus não pode ser zero.')
        else:
            break
    except ValueError as e:    
        print(e)

# Calcule bônus recebido.
bonus_recebido = BONUS_FIXO + salario * bonus

# Exiba o resultado.
print(f'Olá {nome}, o seu salário atual é de R${salario:.2f} e seu bônus final é de R${bonus_recebido:.2f}.')
