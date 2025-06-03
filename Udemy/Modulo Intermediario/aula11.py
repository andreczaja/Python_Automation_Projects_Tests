# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'idade'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa)

print(pessoa[chave])
print(pessoa['sobrenome'])

pessoa[chave] = 'Maria'

print(pessoa)

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['idade'])
# print()

print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

print('ISSO Não vai')