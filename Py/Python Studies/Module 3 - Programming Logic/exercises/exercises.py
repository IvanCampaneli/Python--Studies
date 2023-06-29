"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número inteiro: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas são? ')

horas_float = float(horas)
horas_dia = horas_float <= 11 and horas_float >= 0
horas_tarde = horas_float <= 17 and horas_float >= 12

if horas_dia:
    print('Bom dia!')
elif horas_tarde:
    print('Boa tarde!')
else:
    print('Boa noite!')


"""""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome:')
tamanho_nome = len(nome)
nome_curto = tamanho_nome <= 4
nome_normal = tamanho_nome >= 5 and tamanho_nome <= 6
nome_longo = tamanho_nome > 6

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
else:
    print('Seu nome é longo')



