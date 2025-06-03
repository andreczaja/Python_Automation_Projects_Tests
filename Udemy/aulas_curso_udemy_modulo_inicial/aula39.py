"""
enumerate - enumera iteráveis (índices)
TUPLA É UMA LISTA IMUTÁVEL
"""

# TUPLA SE UTILIZA PARENTESES OU NADA
# LISTA SE UTILIZAR O COLCHETES


# lista = [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista, start=19))
# print(lista_enumerada)
# # próxima linha dá erro pois não existe mais nada após o ultimo índice
# print(next(lista_enumerada))

for indice , item in enumerate(lista):
    print(indice,  item) 

for i in len(lista):
    print(next(i))

# podemos dividir a tupla em dois elementos - o índice e o próprio valor
# for item in enumerate(lista):
#     a, b = item
#     print(a,b)

# "dando nome aos bois"

# for item in enumerate(lista):
#     indice, valor = item
    # print(indice, valor)

# para sintetizar também podemos eliminar uma linha de código:

# for indice, valor in enumerate(lista):
#     print(indice, valor)

# além disso, podemos dividir esses dois elementos para que apareçam em linhas
# distintas

for tupla_enumerada in enumerate(lista):
    print(f'FOR da tupla: {tupla_enumerada}')
    for valor in tupla_enumerada:     
        print(f'\t{valor}')

"""
EXPLICANDO CÓDIGO ACIMA: 
no primeiro FOR, se está transformando em tupla cada
elemento da lista e enumerando em dois elementos: o indice e o próprio valor
ou seja: (0, 'Maria')
a partir disso, no segundo FOR, se divide esses dois elementos, com isso,
os mostramos em linhas separadas a partir dessa segunda estrutura de looping
"""

