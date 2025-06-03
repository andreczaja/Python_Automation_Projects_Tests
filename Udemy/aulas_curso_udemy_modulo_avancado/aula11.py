class Caneta:
    def __init__(self, cor, cor_tampa, preco):
        self.muda_cor = cor
        self.muda_cor_tampa = cor_tampa
        self.muda_preco = preco

    @property
    def cor(self):
        print('PROPERTY')
        return self.muda_cor  
    
def mostrar(caneta):
    caneta.cor