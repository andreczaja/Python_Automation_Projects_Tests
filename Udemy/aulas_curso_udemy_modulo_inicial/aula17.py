# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
print(nome[0])
print(nome[-2])
print('vio' in nome)
print('zero' in nome)
print(10 * '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
procurar = input('Digite o que deseja procurar: ')

if procurar in nome:
    print(f'{procurar} está em {nome}')
else:
    print(f'{procurar} não está em {nome}')








