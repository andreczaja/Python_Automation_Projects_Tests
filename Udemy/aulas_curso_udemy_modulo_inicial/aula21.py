# numero = float(input('Vou dobrar o número que você digitar: '))
# numero_int = int(numero)

# print(f'o dobro de {numero} é {numero * 2}')
# print(f' o dexadecimal de {numero} é {numero_int:X}') 

# numero_str = input('Vou dobrar o número que você digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2}')
#     print(numero_str.isdigit())
# else:
#     print('Isso não é um número')

# UTILIZANDO TRY E EXCEPT 
"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
