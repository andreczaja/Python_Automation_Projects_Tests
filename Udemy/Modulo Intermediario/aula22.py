# string = "Andre Felipe"
# numero_de_caracteres = 2
# indice = 0 

# nova_string = [
#     string[indice:indice + numero_de_caracteres]
#     for indice in range(0,len(string), numero_de_caracteres)
# ]

# print(nova_string)


nomes = ['Andre', 'Felipe', 'Czaja', 'Cardozo']

novos_nomes = [
    f'{iteravel[:-1].lower()}{iteravel[-1].upper()}'
    for iteravel in nomes

]

print(novos_nomes)