class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno_ in self.alunos:
            print(aluno_.nome, aluno_.idade)

aluno1 = Aluno("João", 20)
aluno2 = Aluno("Maria", 25)

curso = Curso("Matemática")

curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

curso.listar_alunos()


