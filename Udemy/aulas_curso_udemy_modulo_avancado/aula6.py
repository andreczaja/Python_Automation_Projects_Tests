from datetime import datetime

class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def calcula_idade(self):
        ano_nascimento = Pessoa.ano_atual - self.idade
        return print(f'O ano que {self.nome} nasceu é {ano_nascimento}')
    
p1 = Pessoa('Carlos', 35)
p2 = Pessoa('André', 27)
p3 = Pessoa('Larissa', 25)

p1.calcula_idade()
p2.calcula_idade()
p3.calcula_idade()



        
