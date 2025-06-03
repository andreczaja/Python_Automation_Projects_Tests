# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# }
# print(pessoa, type(pessoa))
# print(pessoa['sobrenome'])

# print(list(pessoa.keys())[2])

# print()

contador_de_indice = 0

for chave in pessoa:
    if type(pessoa[chave]) == list and type(pessoa[chave][0]) == dict:
        for indice in pessoa[chave]:
            print()
            print(chave , contador_de_indice +1, ":")
            for chave_iteravel_dict, valor in pessoa[chave][contador_de_indice].items():     
                print(chave_iteravel_dict.upper(),':',valor)
            contador_de_indice += 1
    else:
        print(chave.upper() , ':', pessoa[chave])

