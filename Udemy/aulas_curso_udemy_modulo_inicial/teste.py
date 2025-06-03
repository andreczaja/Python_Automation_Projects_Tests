lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista, start=19))
# print(lista_enumerada)
# # próxima linha dá erro pois não existe mais nada após o ultimo índice
# print(next(lista_enumerada))

for indice , item in enumerate(lista):
    print(indice,  item) 

for i in len(lista):
    print(next(i))