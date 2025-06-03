# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho_de_Compras:
    def __init__(self):
        self._produto = []

    def total(self):
        return sum([p.preco for p in self._produto])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produto.append(produto)
            
    
    def listar(self):
        for produto in self._produto:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome            
        self.preco = preco            



carrinho = Carrinho_de_Compras()
p1,p2 = Produto('café', 7.50),Produto('agua', 3.00)

carrinho.inserir_produtos(p1,p2)
carrinho.listar()



