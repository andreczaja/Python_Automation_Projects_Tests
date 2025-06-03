import os

os.system('cls')

class Linguagens:
    def __init__(self, nome):
        self.nome = nome
    
    def complexa(self):
        return f'A linguagem {self.nome} é muito complexa!'
    
java = Linguagens('java')
print(java.nome)
print(java.complexa())


