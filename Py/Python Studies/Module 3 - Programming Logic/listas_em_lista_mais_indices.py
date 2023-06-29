"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Ivan', 'Iasmin', ],  # 0
    # 0
    ['Bot', ],  # 1
    # 0       1       2
    ['Npc', 'Map', 'Travel', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)