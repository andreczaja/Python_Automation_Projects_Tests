import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.mensagem(f'Saldo Atualizado, seu saldo é de {self.saldo}')
    
    def mensagem(self,msg):
        print(f'O seu saldo é de {self.saldo}. {msg}')

        
class ContaPoupanca(Conta):
    def sacar(self,valor):
        valor_com_saque = self.saldo - valor
        if valor_com_saque > 0:
            self.saldo -= valor
            return self.saldo
        return self.mensagem(f'Saldo Insuficiente, seu saldo é de apenas {self.saldo} e o saque solicitado é de {valor}')
    
    def exibir_saldo(self):
        print(self.saldo)
    

c1 = Conta(111,222,0)
c1.exibir_saldo()
c1.depositar(1)
c1.exibir_saldo()
c1.sacar(1)
c1.exibir_saldo()