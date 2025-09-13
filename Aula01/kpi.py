# KPI - Key Performance Indicator

# Calcular o salário total de um usuário com base no salário e bônus fornecidos

# Constante do bônus fixo
BONUS_FIXO = 1000

# Entre com o nome do usuário.
nome = input('Digite o nome do usuário: ')

# Entre com o salário do usuário.
salario = float(input('Digite o salário do usuário: '))

# Entre com o bônus do usuário.
bonus = float(input('Digite o bônus do usuário: '))

# Calcule o salário total.
salario_total = BONUS_FIXO + salario * bonus

# Exiba o resultado.
print(f'Olá {nome}, o seu bônus foi de R${salario_total:.2f}')