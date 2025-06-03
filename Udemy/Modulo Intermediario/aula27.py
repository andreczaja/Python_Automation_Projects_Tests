import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu','tenho', '__iter__']
iterador = iter(iterable) #tem __iter__ e __next__
lista = [n for n in range(1000)]
generator = (n for n in range(1000))

# print(lista)
# print(generator)

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

# print(generator)

# for n in generator:
#     print(n)

print(next(generator))
print(next(generator))
print(next(generator))
