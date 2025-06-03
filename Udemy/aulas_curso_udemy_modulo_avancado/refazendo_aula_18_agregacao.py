class Carrinho_de_Compras:
    def __init__(self):
        self._carrinho = []

    def adicionar_ao_carrinho(self, *produtos):
        for produto in produtos:
            self._carrinho.append(produto)
    
    def listar_itens_carrinho(self):
        for produto in self._carrinho:
            print(produto.nome, produto.preco)

    def transformar_em_dict(self):
        lista_de_produtos = []     
        for produto in self._carrinho:
            dicionario_produto_atual = {'nome':produto.nome,'preco':produto.preco}
            lista_de_produtos.append(dicionario_produto_atual)
        for item in lista_de_produtos:
            for item_chave, item_valor in item.items():
                print(item_chave,': ',item_valor)

    def total_em_reais(self):
        return sum([produto.preco for produto in self._carrinho])

class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1,p2,p3,p4 = Produtos('café', 7.50),Produtos('agua',3.00),Produtos('sanduíche',5.50),Produtos('queijo', 8.00)



objeto = Carrinho_de_Compras()

objeto.adicionar_ao_carrinho(p1,p2,p3,p4)

# objeto.listar_itens_carrinho()
objeto.transformar_em_dict()
print(objeto.total_em_reais())



