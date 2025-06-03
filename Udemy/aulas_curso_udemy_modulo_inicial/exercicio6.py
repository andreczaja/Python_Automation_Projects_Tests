# nome = 'André Czaja'

# qte_caracteres = len(nome)

# i = 0

# while i < qte_caracteres:
#     print(nome[i], i)
#     i += 1


# nome = input("Vou colocar * entre as letras do seu nome:")  # Iteráveis

# indice = 0
# novo_nome = ''
# qtd_letras_nome = len(nome)
# while indice < qtd_letras_nome: 
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)

nome= input('Digite seu nome: ')

indice = 0
novo_nome = ''
i= len(nome)
while indice < i:
    nome_format = (f'*{nome[indice]}')
    novo_nome += nome_format
    indice = indice +1

novo_nome += '*'
print(novo_nome)


# print('pronto')















