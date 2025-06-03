"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# NA LINHA ABAIXO, SE ALTERARMOS ALGO NA LISTA_A, SERÁ ALTERADO TAMBÉM NA LISTA B
lista_b = lista_a


# NA LINHA ABAIXO, SE ALTERARMOS ALGO NA LISTA_A, NÃO SERÁ ALTERADO TAMBÉM NA LISTA B
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

