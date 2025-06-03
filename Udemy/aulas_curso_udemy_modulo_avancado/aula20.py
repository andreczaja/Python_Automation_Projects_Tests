class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, 'ESTOU NA CLASSE:', self.__class__.__name__)

class Aluno(Pessoa):
    ...

class Cliente(Pessoa):
    ...

aluno1 = Aluno('André', 'Czaja')
cliente1 = Cliente('Larissa', 'Padilha')

print(aluno1.nome, aluno1.sobrenome)
print(cliente1.nome, cliente1.sobrenome)

aluno1.falar_nome_classe()
cliente1.falar_nome_classe()