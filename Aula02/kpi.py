# KPI - Key Performance Indicator

# Calcular o salário total de um usuário com base no salário e bônus fornecidos

# Constante do bônus fixo
BONUS_FIXO = 1000

# Entre com o nome do usuário.
nome = input('Digite o nome do usuário: ')
try:
    if any(char.isdigit() for char in nome):
        raise ValueError('O nome não pode conter números.')
except ValueError as e:
    print(e)
    exit()

try:
    if len(nome) == 0:
        raise ValueError('O nome deve conter ao menos um caractere.')
except ValueError as e:
    print(e)
    exit()

try:
    nome_usuario = nome.isspace()
    if nome_usuario:
        raise ValueError('O nome não pode conter apenas espaços em branco.')
except ValueError as e:    
    print(e)
    exit()

# Entre com o salário do usuário.
salario = input('Digite o salário do usuário: ')

salario = salario.replace(',', '.')

try:
    salario_usuario = salario.isspace()
    if salario_usuario:
        raise ValueError('O salário não pode conter apenas espaços em branco.')
except ValueError as e:    
    print(e)
    exit()

try:
    salario = float(salario)
except ValueError as e:    
    print('O salário não pode conter letras ou caracteres inválidos.')
    exit()

try:
    if salario < 0:
        raise ValueError('O salário não pode ser negativo.')
except ValueError as e:    
    print(e)
    exit()

try:
    if salario == 0:
        raise ValueError('O salário não pode ser zero.')
except ValueError as e:    
    print(e)
    exit()

# Entre com o bônus do usuário.
bonus = input('Digite o bônus do usuário: ')

bonus = bonus.replace(',', '.')

try:
    bonus_usuario = bonus.isspace()
    if bonus_usuario:
        raise ValueError('O bônus não pode conter apenas espaços em branco.')
except ValueError as e:    
    print(e)
    exit()

try:
    bonus = float(bonus)
except ValueError as e:    
    print('O bônus não pode conter letras ou caracteres inválidos.')
    exit()

try:
    if bonus < 0:
        raise ValueError('O bônus não pode ser negativo.')
except ValueError as e:    
    print(e)
    exit()

try:
    if bonus == 0:
        raise ValueError('O bônus não pode ser zero.')
except ValueError as e:    
    print(e)
    exit()

# Calcule o salário total.
salario_total = BONUS_FIXO + salario * bonus

# Exiba o resultado.
print(f'Olá {nome}, o seu salário atual é de R${salario_total:.2f}.')
