"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual (desempacotamento com **kwargs)
Argumento não nomeado recebe apenas o argumento (valor) (desempacotamento com *args)
"""


#quando estamos definindo que existem VARIÁVEIS a ser definidas dentro da função, 
# estamos falando em PARÂMETROS

def soma(x, y, z):
    print(f'x = {x} y = {y} z = {z}', '|', end=' ')
    print(f'x + y + z = {x+y+z}')


# quando estamos passando os VALORES a serem atribuídos as variáveis definidas acima,
# estamos falando em ARGUMENTOS


# exemplo de argumento não nomeado
soma(4, 10, 1)

# exemplos de argumento nomeado
soma(y=34, x = 7, z= 1)
soma(1, y = 2, z = 5) 


