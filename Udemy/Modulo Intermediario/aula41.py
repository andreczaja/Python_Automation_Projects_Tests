
def direciona_para_verificacao(verificacao):
    def wrapper(*args, **kwargs):
        for item in args:
            verificacao(item)
        for item in kwargs.values():
            verificacao(item)
    return wrapper


def inverte_e_imprime_string(string):
    print(string[::-1]) 

@direciona_para_verificacao
def verificacao(item):
    if isinstance(item, str):
        inverte_e_imprime_string(item)
    elif isinstance(item,(bool,int)):
        item = str(item)
        inverte_e_imprime_string(item)
    elif isinstance(item,(list, tuple)):
        for elemento in item:
            elemento = str(elemento)
            inverte_e_imprime_string(elemento)
    else:
        raise TypeError(f'Infelizmente não foi possível converter o valor {item} em uma string')
    
    

    

strings = verificacao('oi','tchau',123,[64651,1651],nome='André', idade=26)