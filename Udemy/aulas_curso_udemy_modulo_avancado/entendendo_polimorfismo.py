class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

# Exemplo de polimorfismo
formas = [Circulo(5), Retangulo(3, 4)]
for forma in formas:
    print(forma.area())  # Chamará o método `area` correto para cada objeto