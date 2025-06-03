"""
Lista de listas e seus indices
"""

# salas = [
#     ['Maria','Helena', ],
#     ['Elaine', ],
#     ['Luiz','João','Eduarda', (0, 10, 20, 30, 40)],

# ]

# print (salas[1][0])
# print (salas[0][1])
# print (salas[2][3][2])

salas = [
    ['Maria','Helena', ],
    ['Elaine', ],
    ['Luiz','João','Eduarda', ],

]

for sala in salas:
    for aluno in sala:
        print(aluno)

# indice = 1
# for sala in salas:
#     print (f'Os alunos na sala {indice} são:')
#     indice += 1
#     for aluno in sala:
#         print(aluno)


