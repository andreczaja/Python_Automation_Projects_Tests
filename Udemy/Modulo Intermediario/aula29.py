# Yield from
def gen1():
    print('comecou gen1')
    yield 1
    yield 2
    yield 3
    print('acabou gen1')

def gen3():
    print('comecou gen3')
    yield 1000
    yield 2000
    yield 3000
    print('acabou gen3')

def gen2(gen):
    yield from gen()
    yield 7
    yield 8
    yield 9
    print('acabou gen2')

g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)
