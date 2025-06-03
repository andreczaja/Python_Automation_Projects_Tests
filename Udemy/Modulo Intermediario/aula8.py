"""
Higher Order Functions
Funções de primeira classe
"""


# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'


# def executa(funcao, *args):
#     return funcao(*args)


# print(
#     executa(saudacao, 'Bom dia', 'Luiz')
# )
# print(
#     executa(saudacao, 'Boa noite', 'Maria')
# )


"""
entendendo por passos a aula
"""

# def saudacao_2(msg):
#     return msg

# v = saudacao_2('bom dia')
# print(v)

# saudacao_3 = saudacao_2

# saudacao_teste = saudacao_3

# print(saudacao_3('bom dia'))
# print(saudacao_teste('oi'))


def saudacao(*args):
    return args


def executa(funcao, *args):
    return funcao(*args)



executa1 = executa(saudacao, 'Bom dia', 'Luiz', '25')
executa2 = executa(saudacao, 'Boa noite', 'Maria', '25')

print(*executa1, sep=', ')
print(*executa2, sep=', ')


for item in executa1:
    print(item)

for item in executa2:
    print(item)

