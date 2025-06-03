# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua,numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_enderecos(self):
        # indice_atual = 0
        # while True:
        #     try:
        #         print(cliente_1.enderecos[indice_atual].rua, cliente_1.enderecos[indice_atual].numero)
        #         indice_atual += 1
        #     except IndexError:
        #         break
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('APAGANDO:,', self.rua, self.numero)

cliente_1 = Cliente('André')
cliente_1.inserir_endereco('Rua B', 65468) 
cliente_1.inserir_endereco('Av Atlantica', 2345)
cliente_1.listar_enderecos()

del cliente_1

print('########## terminou o código')

