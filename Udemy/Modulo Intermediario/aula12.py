# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

# if pessoa.get('idade', 'Não existe') is None:
#     print('Não existe')
# else: 
#     print(pessoa['idade'])

# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# print(len(pessoa), pessoa)
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()), type(list(pessoa.items())))
# print(list(pessoa))

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)