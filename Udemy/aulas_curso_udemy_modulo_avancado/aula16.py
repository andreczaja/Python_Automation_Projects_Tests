class Linguagem:
    def __init__(self, nome, complexidade):
        self.nome = nome
        self.complexidade = complexidade

class Dinamica:
    def __init__(self, grau):
        self.grau = grau

    def frase(self):
        return f'o grau da linguagem é {self.grau}'
    
f1 = Linguagem('vba','fácil')
d1 = Dinamica('fraca')
d2 = Dinamica('forte')

f1.complexidade = d1
# f1.complexidade = d2

# print(d1.frase())
print(f1.complexidade.frase())
print(f1.complexidade)
print(f1)
# print(d1.frase())