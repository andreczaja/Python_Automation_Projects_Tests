"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.clear()
# argumentos no método insert (abaixo) 1º: índice onde será inserido / 2º: valor que será inserido
# nesse caso então será inserido no índice 100 o valor 5
# obs: escolheu-se um índice alto no exemplo apenas para colocar no fim da lista
lista.insert(100, 5)

try:
    print(lista[4])
except IndexError:
    print("Escolha um índice válido")
