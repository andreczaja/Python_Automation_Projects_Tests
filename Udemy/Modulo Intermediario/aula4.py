"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# def escopo(x):
#     print(x)

# escopo(1)


# x = 1


# def escopo():

#     x=10
    
#     def outra_funcao():
#         y=2
#         print(x,y)

#     outra_funcao()
#     print(x)


# escopo()

"""
definindo um valor global para x muda tudo que estiver no escopo acima onde o x foi definido
dessa maneira, ou seja, aquilo de que estiver num escopo abaixo dele, não será alterado
na pparte abaixo desse código isso será explicitado
"""


# x = 1

# def escopo():
#     global x
#     x=10

#     def outra_funcao():
#         x = 11
#         y=2
#         print(x,y)

#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x)

""" no código abaixo, estamos definindo x como global no escopo do módulo do código,
ou seja, os x dentro das funções, permanecerão sem se alterar, diferente seria se por exemplo
definissemos o x como global dentro da função dentro da outra_funçao (veremos a seguir)
""" 

# global x
# x = 1

# def escopo():
    
#     x=10

#     def outra_funcao():
#         global x
#         x = 11
#         y=2
#         print(x,y)

#     outra_funcao()
#     print(x)

# print(x)
# escopo()
# print(x)


""" x definido como global na funcao dentro da funcao abaixo e na funcao principal
"""


x = 1

def escopo():
    global x
    x=10

    def outra_funcao():
        global x
        x = 11
        y=2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)