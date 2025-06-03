class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO:', self.nome)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO:', self.rua, self.numero)

cliente_1 = Cliente('André')
cliente_1.inserir_endereco('Av. Brasil', 777)
cliente_1.inserir_endereco('Travessa Doutor Flavio Luz', 153)
endereco_1 = Endereco('Rua Sem Nome', 324234)
cliente_1.inserir_endereco_externo(endereco_1)

del cliente_1

print(endereco_1.rua, endereco_1.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')