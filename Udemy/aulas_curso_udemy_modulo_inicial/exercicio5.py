"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um numero inteiro: ')

# # SOLUÇÃO 1
# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = 'par'
#     if entrada_int %2==0:
#         print(f'O número que você digitou é {par_impar}')
#     else:
#         par_impar = 'impar'
#         print(f'O número que você digitou é {par_impar}')
# else:
#     print('Você não digitou um número')

# SOLUÇÃO 2

# try:
#     entrada_int = int(entrada)
#     par_impar = 'par'
#     if entrada_int %2==0:
#         print(f'O número que você digitou é {par_impar}')
#     else:
#         par_impar = 'impar'
#         print(f'O número que você digitou é {par_impar}')
# except:
#     print('Você não digitou um número')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#SOLUÇÃO
# hora = input('Olá, digite a hora atual: ')
# hora_int= int(hora[0:2])
# hora_dia = hora_int <= 11
# hora_tarde = hora_int >= 12 and hora_int <= 17
# hora_noite = hora_int >= 17 and hora_int <= 24
# try:
#     if hora_dia:
#         print('bom dia')
#     elif hora_tarde:
#         print('boa tarde')
#     elif hora_noite:
#         print('boa noite')
# except:
#     print('você não digitou um horário')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Olá, digite o seu nome: ')
nome_str=  str(nome)
nome_curto = len(nome_str) <= 4 and len(nome_str) != 0 and nome_str != " "
nome_normal = len(nome_str) >=5 and len(nome_str) <= 6
nome_longo = len(nome_str) > 6
try:
    if nome_curto:
        print(f'Seu nome {nome} é curto')
    elif nome_normal:
        print(f'Seu nome {nome} é normal')
    elif nome_longo:
        print(f'Seu nome {nome} é longo')
    else:
        print("Você não digitou um nome")
except:
    print('você não digitou um nome')