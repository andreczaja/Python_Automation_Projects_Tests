nome = 'André'
idade = 25
maior_de_idade = idade >= 18

if maior_de_idade is True:
    maior_de_idade_yes_no = str("Sim")
else: maior_de_idade_yes_no = str("Não")

print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade_yes_no)