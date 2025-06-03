import json
import os
from pathlib import Path

os.system('cls')

NOME_ARQUIVO = 'aula12.json'
# CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         NOME_ARQUIVO
#     )
# )
# print(CAMINHO_ABSOLUTO_ARQUIVO)
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(__file__).replace(os.path.basename(__file__),NOME_ARQUIVO)
# ou
CAMINHO_ABSOLUTO_ARQUIVO = Path(__file__).absolute()
print(CAMINHO_ABSOLUTO_ARQUIVO)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r+') as arquivo_json:
    arquivo_json = dict(json.load(arquivo_json))

NOVO_CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__),'aula13.json')

with open(NOVO_CAMINHO_ARQUIVO, 'w') as novo_arquivo:
    json.dump(arquivo_json,novo_arquivo, ensure_ascii=False,indent = 2)

with open(NOVO_CAMINHO_ARQUIVO, 'r+') as lendo_novo_arquivo:
    lendo_novo_arquivo = dict(json.load(lendo_novo_arquivo))
    for k, v in lendo_novo_arquivo.items():
        print(k, v, sep='\n\t')
    