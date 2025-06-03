# Decoradores com parâmetros
# def fabrica_de_decoradores(a=None, b=None, c=None):
#     def fabrica_de_funcoes(func):
#         print('Decoradora 1')
#         def aninhada(*args, **kwargs):
#             print('Parâmetros do decorador, ', a, b, c)
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
#     return fabrica_de_funcoes


# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y):
#     return x + y


# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y: x * y)

# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)
# dez_vezes_cinco = multiplica(10, 5)
# print(dez_vezes_cinco)

def verificacao_de_string(func):
    print('Decoradora 1')
    def wrapper(*args, **kwargs):
        lista_strings_invertidas = []

        for item in args:
            if not isinstance(item,str):
                item = str(item)
            string_atual = func(item)
            lista_strings_invertidas.append(string_atual)

        for item in kwargs.values():
            if not isinstance(item,str):
                item = str(item)
            string_atual = func(item)
            lista_strings_invertidas.append(string_atual)
        return lista_strings_invertidas
    return wrapper


@verificacao_de_string
def inverte_string(string_recebida):
    string_recebida = string_recebida[::-1]
    return string_recebida

strings = inverte_string('123', 5578, 'André','True', sobrenome = 'Czaja', idade = 26)

for item in strings:
    print(item)