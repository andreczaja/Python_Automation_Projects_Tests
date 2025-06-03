# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você Entrou no Sistema')
elif (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print('Sua Senha Está Incorreta') 
elif (entrada == 'S' or entrada == 's'):
    print("Você Saiu do Sistema")
else: 
    print("Por favor, digite E ou S.")




# # Avaliação de curto circuito
# senha = input('Senha: ') or 'Sem senha'
# print(senha)