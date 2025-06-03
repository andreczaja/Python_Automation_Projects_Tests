# Dictionary Comprehension e Set Comprehension


# produto = {
#     'nome':'Caneta Azul',
#     'preco':2.5,
#     'categoria':'Escritório',
# }

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
# }

# print(dc)


# método 1 de trazer a chave alternando entre letras maiusculas e minusculas

# qtde_itens_dc = len(dc)
# for chave, valor in dc.items():
#         stringchave = ""
#         contador_caracteres = 0
#         qtde_caracteres = len(chave)
#         if contador_caracteres < qtde_caracteres:
#             contador_caracteres += 1
#             for indice in range(0,qtde_caracteres, 1):
#                 if indice % 2 == 0:
#                     stringchave += chave[indice].upper()
#                 else:
#                     stringchave += chave[indice].lower()
#             print(stringchave)



# método 2 de trazer a chave alternando entre letras maiusculas e minusculas

# indice_atual = 0
# for chave, valor in produto.items():
#     stringchave = ""
#     stringvalor = ""
#     for letra in chave:
#         if indice_atual % 2 == 0:
#             stringchave += chave[indice_atual].upper()
#         else:
#             stringchave += chave[indice_atual].lower()
#         indice_atual +=1
#     indice_atual = 0
#     try:
#         for letra in valor: 
#             if isinstance(valor, str) and indice_atual % 2 == 0:
#                 stringvalor += valor[indice_atual].upper()
#             elif isinstance(valor, str) and indice_atual % 2 != 0:
#                 stringvalor += valor[indice_atual].lower()
#             indice_atual += 1
#     except TypeError:
#         stringvalor = valor
#     print(stringchave,' :', stringvalor)
#     indice_atual = 0


# método 3, utilizando hasattr e getattr
    
metodo1 = 'upper'
metodo2 = 'lower'

# if hasattr(string, metodo):
#     print(getattr(string,metodo)())

# print('nome'.upper())

produto = {
    'nome':'Caneta Azul',
    'preco':2.5,
    'categoria':'Escritório',
}

indice_atual = 0
for chave, valor in produto.items():
    stringchave = ""
    stringvalor = ""
    for letra in chave:
        if indice_atual % 2 == 0:
            stringchave += chave[indice_atual].upper()
        else:
            stringchave += chave[indice_atual].lower()
        indice_atual +=1
    indice_atual = 0
    try:
        for letra in valor: 
            if hasattr(valor, metodo1) and indice_atual % 2 == 0:
                stringvalor += valor[indice_atual].upper()
            elif hasattr(valor, metodo2) and indice_atual % 2 != 0:
                stringvalor += valor[indice_atual].lower()
            indice_atual += 1
    except TypeError:
        stringvalor = valor
    print(stringchave,':', stringvalor)
    indice_atual = 0
