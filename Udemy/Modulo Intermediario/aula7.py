"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
isso serve para você criar uma função para fazer ações com argumentos NÃO NOMEADOS, ou seja,
você pode fazer ações com quantos argumentos quiser sem ter que escrever por exemplo:
def soma (x,y,z,t,g,d,e,y,j,c...etc) é apenas escrever def soma(*args) e passar
quantos argumentos quiser na chamada da função
Lembre-te de desempacotamento
"""
# x, y, *args = 1, 2, 3, 4
# print(x, y, *args)
# print(type(args))


# def soma_1(x, y):
#     return x + y

# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
        
#     return total

# soma_totalzona1 = soma(10,5,259,641,48480,81527,8515)

# print(soma_totalzona1)

"""
TENTANDO FAZER SOZINHO
"""

# def soma_teste( *args):
#     total = 0
#     for elemento in args:
#         total += elemento
#     return total

# chamada_soma_teste = soma_teste(1,2,5,9,8)

     
"""
divisão de exercicio
"""
def soma(*args):
    total = 0
    for elemento in args:
        total += elemento
    return total


# soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

# soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

# soma(1,2,3,4,5,6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# print(numeros, type(numeros))
"""
essa próxima linha desempacota os argumentos de numeros para jogar na função soma,
se retirarmos o * isso irá gerar erro pois na hora da função, ela empacota em tupla,
ou seja, teremos uma tupla dentro de uma tupla, o que gerará erro
"""
outra_soma = soma(*numeros)
print(outra_soma)

# print(sum(numeros))
# print(*numeros)