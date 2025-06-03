""" calculo do IMC
    IMC = Peso ÷ (Altura × Altura)
"""
nome = "André Cardozo"
altura = 1.81
peso = 86.2
imc = peso / (altura ** 2)

# print('Seu nome é', nome)
# print('Sua altura é de ', altura,'m ', 'de altura', sep="" )
# print('Seu peso é', peso)
# print('Logo, seu IMC é igual a', imc)
"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'seu peso é {peso:.2f}'
linha_3 = f'então calculando seu IMC temos o valor de {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)





