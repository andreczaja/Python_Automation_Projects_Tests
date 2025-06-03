# List comprehension em Python
# List comprehension é uma forma rápida para criar lista a partir de iteráveis
# print(list(range(10)))
# lista = []
# for numero in range(1,10):
#     lista.append(numero)
# print(lista)
    
# lista = [numero for numero in range(10)]
# lista = [
#     numero * 2
#           for numero in range(10)
#         ]

# print(lista)

produtos = [
    {'nome1':'p1', 'preco':20, },
    {'nome2':'p2', 'preco':10, },
    {'nome3':'p3', 'preco':30, },
]

# def exibir(lista):
#     for dicionario in lista:
#         print(dicionario)

# novos_produtos = [
#     produto
#     for produto in produtos
# ]


# exibir(novos_produtos)
# print(novos_produtos)

# novos_produtos = [
#     {**produto,'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]

# print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco':produto['preco'] *1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(novos_produtos)

# print()

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()


# l1 = sorted(novos_produtos, key=lambda item: item['preco'], reverse=True)

# exibir(l1)


# """
# REGRA PRINCIPAL DA AULA: MAPEAMENTO (TRAZER DADOS DE UM DICIONARIO PARA OUTRO), VIRÃO A ESQUERDA DO FOR
# COMO É O CASO DA LINHA     **produto, 'preco': produto['preco'] * 1.05}
# """
# """
# AGORA, SE ESTIVER REALIZANDO FILTROS, ELES VIRÃO APÓS O FOR COMO MOSTRADO ABAIXO:
# """


# novos_produtos = [
#PARTE DE MAPEAMENTO
    # {**produto, 'preco': produto['preco'] * 1.05}
    # if produto['preco'] > 20 else {**produto}
    # for produto in produtos
#PARTE DO FILTRO
#     if produto['preco'] > 10
# ]

# print(*novos_produtos, sep='\n')