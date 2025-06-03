class Caneta:
    def __init__(self, cor):
        self._cor = cor

    # GETTER
    @property
    def cor(self):
        return self._cor
    
    # SETTER
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor
    
canetas = [
    Caneta('Azul'),
    Caneta('Vermelha'),
    Caneta('Verde'),
    Caneta('Amarela'),
    Caneta('Laranja'),
    Caneta('Roxa'),
    Caneta('Marrom'),
    Caneta('Rosa'),
    Caneta('Cinza'),
    Caneta('Branca')
]

for caneta in canetas:
    caneta.cor = 'Preta'

for caneta in canetas:    
    print(caneta.cor)

print(canetas)
# print(c1.cor)
# c1.cor = 'Preta'
# print(c1.cor)