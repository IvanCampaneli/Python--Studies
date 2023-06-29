"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Ivan'), (1, 'Iasmin'), (2, 'Bot'), (3, 'Npc')]
lista = ['Ivan', 'Iasmin', 'Bot']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')