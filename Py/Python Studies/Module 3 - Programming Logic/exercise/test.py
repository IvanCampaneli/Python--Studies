num1 = input('digite o primeiro número: ')
num2 = input('digite o segundo número: ')

num1_float = float(num1)
num2_float = float(num2)

if num1_float >= num2_float:
    print(f'{num1_float=} é maior ou igual a {num2_float=}')

elif num1_float <= num2_float:
    print(f'{num2_float=} é maior ou igual a {num1_float=}')

else:
    print('Você digitou algo inválido, insira apenas números')
