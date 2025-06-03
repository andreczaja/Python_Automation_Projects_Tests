class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, novo_motor):
        self._motor = novo_motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, novo_fabricante):
        self._fabricante = novo_fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


focus = Carro('Focus')
m3 = Carro('m3')
ka = Carro('ka')
quattro = Carro('quattro')

motor1 = Motor(1.0)
motor2 = Motor(2.5)
motor3 = Motor(3.0)

fabricante1 = Fabricante('Ford')
fabricante2 = Fabricante('BMW')
fabricante3 = Fabricante('Audi')

focus.motor = motor2
focus.fabricante = fabricante1

m3.motor = motor3
m3.fabricante = fabricante2

ka.motor = motor1
ka.fabricante = fabricante1

quattro.motor = motor2
quattro.fabricante = fabricante3

print(focus.nome, focus.motor.nome, focus.fabricante.nome)
print(m3.nome, m3.motor.nome, m3.fabricante.nome)
print(ka.nome, ka.motor.nome, ka.fabricante.nome)
print(quattro.nome, quattro.motor.nome, quattro.fabricante.nome)



