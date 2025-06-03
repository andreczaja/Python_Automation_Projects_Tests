class Linguagens:
    def __init__(self, nome, complexidade):
        self._nome = nome
        self.complexidade = complexidade

    @property
    def nome(self):
        return self._nome

    @classmethod
    def linguagem_sem_complexidade(cls, nome):
        return cls(nome, 'Nula')
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


l1 = Linguagens('vba', 'facil')
l2 = Linguagens('python', 'medio')
l3 = Linguagens.linguagem_sem_complexidade('Java')

print(l1.nome, l1.complexidade)
print(l2.nome, l2.complexidade)
print(l3.nome, l3.complexidade)

l1.nome = 'vba7'
print(l1.nome, l1.complexidade)

