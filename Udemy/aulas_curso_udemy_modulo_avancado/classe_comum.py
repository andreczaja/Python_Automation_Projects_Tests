class Carro:
    def __init__(self, nome, vel_maxima):
        self._nome = nome
        self.vel_maxima = vel_maxima

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def acelerando(self):
        return print (f'{self.nome} está acelerando e pode chegar até {self.vel_maxima}')
    
    @classmethod
    def carro_anonimo(cls, vel_maxima):
        return cls('Anônimo', vel_maxima)

celta = Carro('Celta', 120)
EcoSport = Carro('EcoSport', 270)
carro_sem_nome = Carro.carro_anonimo(256)

celta.acelerando()
EcoSport.acelerando()
carro_sem_nome.acelerando()

celta.nome = 'Celta_novo'
celta.acelerando()

