class Leão:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, idade, alimento):
        return print(f'O leão {self.nome} que tem {idade} anos, está comendo {alimento}')
    
    def executar(self, *args,**kwargs):
        return self.comendo(*args,**kwargs)
    
l1 = Leão('Jonas').executar(30, 'Caju')
l2 = Leão('Anderson').executar(18, 'Boi')