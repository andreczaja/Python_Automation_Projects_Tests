# Empacotamento e desempacotamento de dicionários
# a,b = 1, 2
# a,b = b, a
# print(a, b)

pessoa = {
    'nome':'Andre',
    'sobrenome':'Souza',
}



(a1, a2), (b1,b2) = pessoa.items()

print(a1, a2)
print(b1, b2)

# for chave,valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (argumentos não nomeados)
# kwargs (argumentos nomeados)


# def mostro_argumentos_nomeados(*args, **kwargs):
#     lista_args = dict(*args)
#     for chave, valor in lista_args.items():
#         print(chave, valor)
#     for chave, valor in kwargs.items():
#         print(chave, valor)

# mostro_argumentos_nomeados(pessoa, idade='35', condicao_cadastro='False')
