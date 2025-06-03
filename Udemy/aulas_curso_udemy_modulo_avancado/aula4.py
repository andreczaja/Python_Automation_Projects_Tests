class Animal:
    # nome = 'Leão'
    variavel = 'valor'
    print(variavel)
    def __init__(self, nome):
        self.nome = nome



    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))
animal = Animal.variavel
print(animal)