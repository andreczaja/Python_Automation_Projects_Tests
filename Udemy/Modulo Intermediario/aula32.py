# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-excepctions
# raise - lançando exceções (erros)

def divide(n , d ):
    try:
        return n/d
    except ZeroDivisionError:
        raise ZeroDivisionError('Deu ruim')
    
# def divide(d ):
#     if d == 0:
#         raise ZeroDivisionError('Deu ruim')
#     divide2
    
soma1 = divide(8,0)

print(soma1)