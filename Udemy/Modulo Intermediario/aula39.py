# def concatenar(prefixo_fatura):
#     valor_inicial = prefixo_fatura

#     def interna(numero_fatura):
#         return  prefixo_fatura + numero_fatura  
#     return interna

# # c = concatenar('FAE0')('c')

# fac = concatenar('FAE0')
# nce = concatenar('NCE000')

# print(fac('2276898'))
# print(fac('2299996'))
# print(nce('16898'))
# print(nce('15484'))

# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

