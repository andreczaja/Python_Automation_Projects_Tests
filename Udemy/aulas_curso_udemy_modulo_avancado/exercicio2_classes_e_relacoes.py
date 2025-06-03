# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome_carro):
        self._nome = nome_carro
        self._motores = []
        self._fabricantes = []    

    @property
    def nome_carro(self):
        return self._nome
    
    @property
    def motores(self):
        return self._motores
    
    @property
    def fabricantes(self):
        return self._fabricantes

    def inserir_motor(self, nome_motor, potencia):
        self._motores.append(Motor(nome_motor, potencia))

    def definir_fabricante(self, nome_fabricante, pais_origem):
        self._fabricantes.append(Fabricante(nome_fabricante, pais_origem))
    
    def listar_carro(self):
        for motor in self._motores:
            print('MODELO DO CARRO: ', self._nome, 'MOTOR: ', motor.nome_motor, 'POTÊNCIA: ', motor.potencia)
        for fabricante in self._fabricantes:
            print('NOME DO FABRICANTE: ', fabricante.nome, fabricante.pais_origem, end='\n\n')


class Motor:
    def __init__(self, nome_motor, potencia):
        self.nome_motor = nome_motor
        self.potencia = potencia


class Fabricante:
    def __init__(self, nome, pais_origem):
        self.nome = nome
        self.pais_origem = pais_origem


civic = Carro(nome_carro='Civic')
city = Carro(nome_carro='City')
focus = Carro(nome_carro='Focus')
m3 = Carro(nome_carro='M3')
x6 = Carro(nome_carro='X6')

civic.inserir_motor('HCR 400', '150CV')
civic.definir_fabricante('Honda', 'Japão')

city.inserir_motor('FB 550C', '210CV')
city.definir_fabricante('Honda', 'Japão')

focus.inserir_motor('FB 550C', '210CV')
focus.definir_fabricante('Ford', 'USA')

m3.inserir_motor('FB 650C', '550CV')
m3.definir_fabricante('BMW', 'Alemanha')

x6.inserir_motor('FB 650C', '550CV')
x6.definir_fabricante('BMW', 'Alemanha')

civic.listar_carro()
city.listar_carro()
focus.listar_carro()
m3.listar_carro()
x6.listar_carro()








