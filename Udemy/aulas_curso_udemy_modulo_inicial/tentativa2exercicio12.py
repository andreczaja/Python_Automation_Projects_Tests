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

cpf_digitado= input('digite o cpf: ')
cpf_limpo = cpf_digitado.replace(".","").replace("-","")

contador_regressivo = 10
resultado = 0
nove_digitos = cpf_limpo[:9]

while contador_regressivo >= 2:
    for digito in nove_digitos:
        resultado  += int(digito) * contador_regressivo
        contador_regressivo -= 1
        
resultado = (resultado * 10) % 11

print(f'o primeiro dígito ({resultado}) é inválido!' \
      if resultado > 9 else f'o primeiro dígito ({resultado}) é válido!')

# parte 2 - SEGUNDO DÍGITO

contador_regressivo = 11
resultado = 0
dez_digitos = cpf_limpo[:10]

while contador_regressivo >= 2:
    for digito in dez_digitos:
        resultado  += int(digito) * contador_regressivo
        contador_regressivo -= 1
        if contador_regressivo < 2:
            break
        
resultado = (resultado * 10) % 11


print(f'o segundo dígito ({resultado}) é inválido!' if resultado > 9 else f'o segundo dígito ({resultado}) é válido!')

print(f'Seu CPF é o {cpf_digitado}. ')

