"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_digitado = "746.824.890-70"
cpf_limpo = int(cpf_digitado.replace(".","").replace("-",""))
print(cpf_limpo, type(cpf_limpo))
# MINHA SOLUÇÃO:

# # 1) multiplicando o primeiro até o nono digito por uma contagem regressiva de 10 até 2

# primeira_verificacao_digitos = (int(cpf_limpo[0])*10) + (int(cpf_limpo[1]) *9) + (int(cpf_limpo[2]) *8)\
# + (int(cpf_limpo[3]) *7) + (int(cpf_limpo[4]) *6) + (int(cpf_limpo[5]) *5) + (int(cpf_limpo[6]) *4)\
# + (int(cpf_limpo[7]) *3) + (int(cpf_limpo[8]) *2) 

# print(primeira_verificacao_digitos)

# # 2) multiplicando a primeira verificacao por 10

# segunda_verificacao_digitos = primeira_verificacao_digitos * 10

# print(segunda_verificacao_digitos)

# # 3) pegando o resto da segunda verificacao por 11

# terceira_verificacao_digitos  = segunda_verificacao_digitos % 11 

# print(terceira_verificacao_digitos)

# # 4) o décimo digito se maior que 9, será 0, se não, será o próprio resto

# if terceira_verificacao_digitos > 9:
#     verificacao_decimo_digito = 0
# else: verificacao_decimo_digito = terceira_verificacao_digitos

# print(verificacao_decimo_digito)

# if verificacao_decimo_digito == int(cpf_limpo[9]):
#     print('O primeiro dígito do seu CPF é válido')
# else: print("digite um CPF válido")



# SOLUÇÃO DO CURSO:

# nove_digitos = cpf_limpo[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito = (resultado *10) % 11
digito = digito if digito <= 9 else 0
print(digito)
if digito == int(cpf_limpo[9]):
    print('O primeiro dígito do seu CPF é válido')
else: print("Digite um CPF válido")

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

dez_digitos = cpf_limpo[:10]
contador_regressivo = 11

resultado = 0
for digito in dez_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito = (resultado *10) % 11
digito = digito if digito <= 9 else 0
print(digito)
if digito == int(cpf_limpo[10]):
    print('O segundo dígito do seu CPF é válido')
else: print("Digite um CPF válido")














