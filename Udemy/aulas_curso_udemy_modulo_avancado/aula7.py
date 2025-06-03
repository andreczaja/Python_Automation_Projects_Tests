# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('teste')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


# p1 = Pessoa('João', 34)
# p2 = Pessoa.criar_com_50_anos('Helena')
# p3 = Pessoa('Anônima', 23)
# p4 = Pessoa.criar_sem_nome(25)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
# print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

################################################################



class Cookie:
    def __init__(self, nome):
        self.nome = nome  # instância
 
    def fala_nome(self):
        # Aqui eu vou precisar do nome da instância
        # portanto método de instância
        print(f'O nome do cookie é: {self.nome}')
 
    @classmethod
    def cria_cookie(cls):
        # Isso retorna a própria classe já criando
        # uma instância
        return cls(nome='Sem nome')
 
 
c1 = Cookie('Gato 1')
c1.fala_nome()  # O nome do cookie é: Gato 1
 
# Se, por algum motivo, eu precisar criar um objeto
# sem nome, eu posso utilizar meu método de classe
# isso é apenas um exemplo bobo
c2 = Cookie.cria_cookie()
c2.fala_nome()  # O nome do cookie é: Sem nome




