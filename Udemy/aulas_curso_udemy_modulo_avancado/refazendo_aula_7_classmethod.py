import json

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def pessoa_sem_nome (cls, idade):
        return cls('Anônimo', idade)
    
    @classmethod
    def idade_50_anos (cls, nome):
        return cls(nome, '50')
    
p1 = Pessoa('Carlos', 53)
p2 = Pessoa.pessoa_sem_nome(53)
p3 = Pessoa.idade_50_anos('Carlos')


print(p1.nome)
print(p1.idade)
print(p2.nome)
print(p2.idade)
print(p3.nome)
print(p3.idade)