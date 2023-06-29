primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


if primeiro_valor > segundo_valor:
    print(primeiro_valor, 'é maior que o', segundo_valor)
elif primeiro_valor < segundo_valor:
    print(segundo_valor, 'é maior que o', primeiro_valor)
else:
    print(primeiro_valor, 'é igual a', segundo_valor)    

   

"""
RESOLUÇÃO PROFESSOR:

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'do que {segundo_valor=}'
    )
elif primeiro_valor < segundo_valor:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
else:
    print(
        f'{primeiro_valor=} é igual '
        f'ao {segundo_valor=}'
    )
"""