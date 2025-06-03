# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou no sistema')
elif  (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print('Você digitou a senha incorreta.')
elif entrada == 'S' or entrada == 's':
    print('Você saiu do sistema')

# # Avaliação de curto circuito
# print(True and False and True) # False
# print(True and 0 and True) # 0

# print(bool(" ")) # True