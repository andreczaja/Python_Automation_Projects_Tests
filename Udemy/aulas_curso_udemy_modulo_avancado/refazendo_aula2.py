class Linguagens:
    def __init__(self, nome, complexidade):
        self.nome = nome
        self.complexidade = complexidade

    def padrao(self):
        print(f'a complexidade da linguagem {self.nome} é {self.complexidade}')

l1 = Linguagens('vba','easy')
l2 = Linguagens('python','medium')
l3 = Linguagens('java','hard')

print(l1.nome)
l1.padrao()
Linguagens.padrao(l1)
print(l2.nome)
l2.padrao()
Linguagens.padrao(l2)
print(l3.nome)
l3.padrao()
Linguagens.padrao(l3)