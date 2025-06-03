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

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)




print('utilizando o deep copy')
import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)

d1 = [0,1,2,[0,1,2]]
d2 = copy.deepcopy(d1)

d2[3][1] = 'teste'

print(d1)
print(d2)


"""
quando estamos falando de variaveis imutaveis (int, str e boolean) se alterarmos
o valor da chave de um dicionario, não alterará no outro, porém se estivermos falando de 
variaveis mutaveis (dicionario ou lista) se alteramos um dos elementos, alterará no outro
dicionário também, por isso, no exemplo acima, importou-se o módulo deep copy, isso fará
com que mesmo varíaveis mutáveis sejam alteradas apenas no dicionário solicitado
"""