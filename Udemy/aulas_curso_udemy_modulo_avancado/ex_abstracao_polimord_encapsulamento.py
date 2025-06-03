"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

import abc

class Conta(abc.ABC):
    def __init__(self,agencia,conta,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # @abc.abstractmethod
    # def sacar(self, valor):
    #     ...

    def depositar(self,valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO) {valor}')

    def detalhes(self, msg=''):
        print(f'O seu saldo é de {self.saldo:.2f} {msg}')

    
class ContaPoupanca(Conta):
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE) {valor}')
            return self.saldo
        print('Transação Negada')
        return self.detalhes(f'(Saldo Insuficiente) {valor}')
    
class ContaCorrente(Conta):
    def __init__(self,agencia,conta,saldo=0,limite=0):
        super().__init__(agencia,conta,saldo)
        self.limite = limite

    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= -self.limite:
            self.saldo -= valor
            self.detalhes(f'(SAQUE) {valor}')
            return self.saldo
        print('Transação Negada')
        return self.detalhes(f'(Saldo Insuficiente) {valor}')

if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222,0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cc1 = ContaCorrente(111,222,100,100)
    cc1.sacar(15)
    cc1.depositar(1)
    cc1.sacar(700)
    cc1.detalhes()


# class ContaCorrente(Conta):
#     def __init__(self, limite):
#         self.limite = limite
#         self.limite_extra = 1000
        
        



# class Pessoa:
#     def __init__(self,nome, idade):
#         self._nome = nome
#         self._idade = idade

#     @property
#     def nome(self):
#         return self._nome
    
#     @property
#     def idade(self):
#         return self._idade
    
# class Cliente(Pessoa):
#     def __init__(self, agencia,conta, saldo):
#         self.agencia = agencia
#         self.conta = conta
#         self.saldo = saldo


#         # self.pessoa_conta_e_limite = {}
#         # self.lista_clientes = []

# claudio = Pessoa('Claudio', 35)
# conta = ''




