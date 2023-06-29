# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Ivan', 'Iasmin', 1, 2, 3, 'Npc']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Ivan', 'Iasmin', ],  # 0
    # 0
    ['Bot', ],  # 1
    # 0       1       2
    ['Map', 'Travel', 'Npc', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Ivan', 'Iasmin', 1, 2, 3, 'Npc')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')