class Caneta:
    def __init__(self, cor, cor_tampa, preco):
        self.muda_cor = cor
        self.muda_cor_tampa = cor_tampa
        self.muda_preco = preco

    @property
    def cor(self):
        return self.muda_cor  
      
    @property
    def cor_tampa(self):
        return self.muda_cor_tampa
      
    @property
    def preco(self):
        return self.muda_preco    

p1 = Caneta('Azul', 'Vermelha', 5.00)
p2 = Caneta('Roxa', 'Amarela', 9.54)
p3 = Caneta('Verde', 'Preta', 7.58)

print(p1.cor, p1.cor_tampa, p1.preco)
print(p2.cor, p2.cor_tampa, p2.preco)
print(p3.cor, p3.cor_tampa, p3.preco)
