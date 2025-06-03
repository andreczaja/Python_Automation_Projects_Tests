class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('André', 'Cardozo')
p2 = Pessoa('Larissa', 'Padilha')

print(p1.sobrenome)
print(p2.nome)
print(p1.__dir__)
print(p2)
    