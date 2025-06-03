"""
Retorno de valores das funções (return)
"""


def soma22(x, y):
    if x > 10:
        print('Olha')
        print('só')
        print('que')
        print('legal')
        return [10, 20]
    # linha do else abaixo
    return x + y

def soma33(x, y):
        if x + y > 10:
            return "Valor alto pakas"
        # linha do else abaixo
        return x + y



soma1 = soma22(12, 2)
soma2 = soma22(3, 3)
soma3 = soma33(12, 2)
soma4 = soma33(3, 3)
print(soma1)
print(soma2)
soma3 = soma22(11, 55)
print(soma3)


