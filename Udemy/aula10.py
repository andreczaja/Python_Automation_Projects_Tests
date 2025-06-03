# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil
import pathlib

HOME = os.path.expanduser('~')
PASTA_ORIGINAL = os.path.join(HOME, 'Downloads')
NOVA_PASTA = r'C:\Users\CardoAnd03\OneDrive - Electrolux\Documents\Pasta_Cartolas1'

NOVA_PASTA_2 = pathlib.Path.home() / 'OneDrive - Electrolux' / 'Documents' / 'Pasta Cartolas 2'

NOVA_PASTA_2.mkdir(exist_ok=True)

print(os.path.isdir(NOVA_PASTA_2))

os.makedirs(NOVA_PASTA, exist_ok=True)
print(os.path.isdir(NOVA_PASTA))

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for file_ in files:
#         caminho_arquivo = os.path.join(root, file_)
#         novo_caminho_arquivo = os.path.join(root, file_).replace(PASTA_ORIGINAL,NOVA_PASTA)
#         nome_arquivo, extensao_arquivo = os.path.splitext(file_)
#         if 'artola' in file_ and (extensao_arquivo == '.xlsx' or extensao_arquivo == '.pdf'):
#             shutil.copy(caminho_arquivo, novo_caminho_arquivo)