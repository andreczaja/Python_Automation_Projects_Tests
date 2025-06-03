class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo "privado"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return valor
        else:
            return "Saldo insuficiente"

    def obter_saldo(self):
        return self.__saldo

# Exemplo de encapsulamento
conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.obter_saldo())  # 1500
print(conta.sacar(200))     # 200
print(conta.obter_saldo())  # 1300
