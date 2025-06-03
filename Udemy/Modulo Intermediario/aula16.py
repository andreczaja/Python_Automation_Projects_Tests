# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# print(s1)
# l2 = list(l1)
# print(l2)
# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)
# Métodos úteis:
# add, update, clear, discard

# LEGENDA DOS MÉTODOS:
# add: adiciona um item por vez
# update: adiciona um ou vários itens por vez
# clear: limpa o set inteiro
# discard: limpa o elemento especificado no set, por exemplo set = {1,2,3}, se dermos um set.discard(3), o set novo será igual a {1,2}


# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
# s1.discard('Olá mundo')
# s1.discard('Luiz')
# print(s1)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s2 - s1
s6 = s1 ^ s2
print(*s3)
print(*s4)
print(*s5)
print(*s6)