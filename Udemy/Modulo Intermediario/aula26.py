string = "nome"
metodo = 'upper'


if hasattr(string, metodo):
    print(getattr(string,metodo)())


print(string.upper())