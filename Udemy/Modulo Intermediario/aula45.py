# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]



"""
nesse código, o primeiro passo foi ordenar a lista de alunos com a chave NOTA na linha 28 a partir da função ordena, com isso, na linha 29
a variavel grupos está novamente utilizando a função ordena porém dentro do group by, que gera as chave disponíveis e o iterador
nesse iterador, é onde estamos trazendo cada aluno compátivel com essa chave disponível, por isso, temos na linha 32 o seguinte código:
for nota, iterador in grupos:
"""


def ordena(item):
    return item['nota']
alunos_ordenada = sorted(alunos, key = ordena)
grupos = groupby(alunos_ordenada, key = ordena)


for nota, iterador in grupos:
    print(nota)
    for aluno in iterador:
        print(*aluno.values())
