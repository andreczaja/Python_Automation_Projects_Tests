"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# Print(1, 1, 1)

# def imprimir(a, b, c):
#     return a, b, c



# s1 = imprimir(1, 2, 3)
# s2 = imprimir(4, 5, 6)

# print(*s1)
# print(*s2)

# for numero in s1:
#     print(numero)

"""
um argumento pode receber um nome padrão, se alterado na função, receberá o novo nome, 
se não, será o padrão
"""

# def saudacao(nome='Sem nome'):
#     print(f'Olá, {nome}!')


# saudacao('Luiz Otávio')
# saudacao('Maria')
# saudacao('Helena')
# saudacao()

def Minha_Funcao():
    print(5+14-6)
Minha_Funcao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)