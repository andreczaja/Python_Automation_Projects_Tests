class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def idade_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def sem_nome (cls, idade):
        return cls('Anônimo', idade)
    
p1 = Pessoa('Carlos', 56)
p2 = Pessoa.idade_50_anos('André')
p3 = Pessoa.sem_nome(64)

print(p1.nome)
print(p1.idade)
print(p2.nome)
print(p2.idade)
print(p3.nome)
print(p3.idade)
