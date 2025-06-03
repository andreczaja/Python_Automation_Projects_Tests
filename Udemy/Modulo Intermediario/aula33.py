# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-excepctions
# raise - lançando exceções (erros)

# def verificacoes(*args):
#     variaveis_passadas = ""
#     for item in args:
#         if not isinstance(item, (float,int)):
#             variaveis_passadas += item + " -"
#     if variaveis_passadas != "":
#         raise TypeError(
#             f'Os valores digitados não são compatíveis: {variaveis_passadas}')



    
    
# def soma(*args):
#     verificacoes(*args)
#     return sum(args)



# soma1 = soma(8,0, 5,'Olá', 2,7,"Tudo Bem",9) 

# print(soma1)

def verificacoes(*args):
    variaveis_passadas = ""
    tipo_item = ""
    for item in args:
        if not isinstance(item, (float,int)):
            variaveis_passadas += "(" + str(item) + ")" + " - "
            tipo_item += type(item).__name__ + " - "
    if variaveis_passadas != "":
        variaveis_passadas = variaveis_passadas[:-3] + ", "
        tipo_item = tipo_item[:-3]
        raise TypeError(
            f'Os valores digitados não são compatíveis: {variaveis_passadas}'
            f'já que os valores são do tipo {tipo_item}, respectivamente')    
    
def soma(*args):
    verificacoes(*args)
    return sum(args)


soma2 = soma(14,7,8,9,651,15)
print(soma2)
soma1 = soma(8,0, 5,'Olá', 2,7,"Tudo Bem",9) 
print(soma1)
