"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = input('Digite seu nome: ')
preco = float(input('Digite o preço em R$:'))
precoint = int(preco)

# MÉTODO 1: utilizando INTERPOLAÇÃO
variavel = '%s, o preço é de R$%.2f. o qual, tem seu equivalente hexadecimal como %X' %(nome, preco, precoint)
print(variavel)

# MÉTODO 2: utilizando F'STRINGS
variavel = f'{nome}, o preço é de R${precoint:.2f} , o qual, tem seu equivalente hexadecimal como {precoint:X}'
print(variavel)


