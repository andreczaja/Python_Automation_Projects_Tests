class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return f'Saldo Atual: {self.__saldo}'
        else:
            return 'Saldo Insuficiente'

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            return f'Saldo Atual: {self.__saldo}'
    
    
    def obter_saldo(self):
        return self.__saldo



conta = ContaBancaria(1000)
print(conta.obter_saldo())
print(conta.sacar(200))
print(conta.obter_saldo())
print(conta.depositar(500))
print(conta.obter_saldo())