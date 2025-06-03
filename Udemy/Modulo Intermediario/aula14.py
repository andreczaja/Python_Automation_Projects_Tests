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
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# del(p1['nome'])
# print(p1)
# if p1.get('nome') is None:
#     print('Não existe') 

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })


# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# primeira forma de usar o update
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})

print(p1)
# segunda forma
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(lista)
# print(p1)