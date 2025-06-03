# introdução às Generator functions em Python
# generator = (n for n in range(100000))


def generator(n=0):
    yield 1 # pausar
    print('continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Terminar')    
    return 'ACABOU'

gen = generator(n=0)
print(next(gen))
print(next(gen))

# for n in gen:
#     print(n)


# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1

#         if n > maximum:
#             return 'acabou'

# gen = generator()
# for n in gen:
#     print(n)
