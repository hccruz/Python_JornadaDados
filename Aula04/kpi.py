# KPI - Key Performance Indicator

# Calcular o salário total de um usuário com base no salário e bônus fornecidos

def validar_valor(texto: str) -> float:
    # Entre com o salário do usuário.     
    while True:
        
        try:
            valor = input(f'Digite o {texto} do usuário: ')

            valor = valor.replace(',', '.')
            
            valor = float(valor)
        except ValueError as e:    
            print(f'O {texto} não pode conter letras ou caracteres inválidos.')
            continue

        try:
            if valor < 0:
                raise ValueError(f'O {texto} não pode ser negativo.')
            elif valor == 0:
                raise ValueError(f'O {texto} não pode ser zero.')
            else:
                return valor
        except ValueError as e:    
            print(e)


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

# Calcule bônus recebido.
salario_validado = validar_valor('salário')

bonus_validado = validar_valor('bônus')
    
bonus_recebido = BONUS_FIXO + salario_validado * bonus_validado

# Exiba o resultado.
print(f'Olá {nome}, o seu salário atual é de R${salario_validado:.2f} e seu bônus final é de R${bonus_recebido:.2f}.')
