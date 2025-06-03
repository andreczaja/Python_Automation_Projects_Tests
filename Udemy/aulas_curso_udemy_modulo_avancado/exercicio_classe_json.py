# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
import os
CAMINHO_ARQUIVO =os.path.join(os.path.dirname(__file__),'exercicio_classe_json.json')
print(CAMINHO_ARQUIVO)

class Linguagens:
    def __init__(self, nome, complexidade):
        self.nome = nome
        self.complexidade = complexidade

l1 = Linguagens('vba','easy')
l2 = Linguagens('python','medium')
l3 = Linguagens('java','hard')

dados = [
    vars(l1),
    vars(l2),
    vars(l3)
]
with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo_json:
    json.dump(dados,arquivo_json,ensure_ascii=False, indent=2)
