class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def idade_50 (cls, nome, idade = 50):
        return cls(nome, idade)

p1 = Pessoa('André', 26)
p1 = Pessoa('Claudio', 32)
p1 = Pessoa('Jorge', 65)
p1 = Pessoa('Ana', 55)
p1 = Pessoa('Rafael', 46)
p1 = Pessoa('Felipe', 52)
p2 = Pessoa.idade_50('Larissa')