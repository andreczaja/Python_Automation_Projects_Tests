from pathlib import Path
import os

CAMINHO_ABSOLUTO_ARQUIVO = Path(__file__).absolute()
# CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(__file__)
print(CAMINHO_ABSOLUTO_ARQUIVO)
print(CAMINHO_ABSOLUTO_ARQUIVO.parent)
print(CAMINHO_ABSOLUTO_ARQUIVO.parent.parent)
arquivo_criado = Path.home() / 'OneDrive - Electrolux' / 'Documents' / 'arquivo2222.txt'
arquivo_criado.touch(exist_ok=True)

with open(arquivo_criado, 'w+') as escrevendo_arquivo:
    escrevendo_arquivo.write('Linha 1\n')
    escrevendo_arquivo.write('Linha 2\n')

# print(Path.home() / 'OneDrive - Electrolux' / 'Documents' / 'arquivo2222.txt')
    
with arquivo_criado.open('a+') as file:
    file.write('linha 3\n')
    file.write('linha 4\n')

print(arquivo_criado.read_text())
    
