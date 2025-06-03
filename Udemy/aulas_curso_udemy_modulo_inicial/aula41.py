"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
# frase = '    Olha só     :      que coisa interessante    '
# lista_frases = frase.split(': ')
# print(lista_frases)

# for i, frase in enumerate(lista_frases):
#     print(f'O indice atual é {i}. A frase sem espaçoes é "{lista_frases[i].strip()}",\
#  A frase com espaçoes é "{lista_frases[i]}"')


"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""


frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

print(lista_frases_cruas)

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)
print(*lista_frases) # desempacotando
"""JOIN: primeiro argumento é o separador dos itens da lista nesse caso escolhemos o ", "
"""
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)


# frases_unidas = 'struvb wef '.join(lista_frases)
# print(frases_unidas)


