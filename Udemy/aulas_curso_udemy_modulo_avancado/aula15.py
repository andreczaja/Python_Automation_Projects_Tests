
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    def frase(self):
        return print(f'o nome do animal é {self.nome} e sua idade é {self._idade}.')
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

l1 = Animal('Leão', idade = 22)

l1.frase()

