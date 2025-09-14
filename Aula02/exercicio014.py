# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# Digitar uma data no formato "dd/mm/aaaa"
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Separar a data em dia, mês e ano
dia, mes, ano = data.split('/')

# Imprimir o dia, o mês e o ano separadamente
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
