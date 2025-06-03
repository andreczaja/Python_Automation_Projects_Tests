from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
''
print_iter(combinations(pessoas,2))
print('----------------')
print_iter(permutations(pessoas,2))
print('----------------')
print_iter(product(*camisetas))
# print(teste)
