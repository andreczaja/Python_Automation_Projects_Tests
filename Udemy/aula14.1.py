# from pathlib import Path
# import os

# caminho_home = Path.home()

# while True:
#     for root, dirs, files in os.walk(caminho_home):
#         for dir in dirs:
#             if 'OneDrive - Electrolux' in dir:
#                 print('achou pasta OneDrive - Electrolux')
#                 for root_, dirs_, files_ in os.walk(caminho_home / dir):
#                     for dir_ in dirs_:
#                         if 'Documents' in dir_:
#                             print(os.path.isdir(os.path.join(root_, dir_)))
#                             print('achou pasta docs')           
#                             arquivo_criado = caminho_home / dir / dir_/ 'arquivo2223.txt'
#                             arquivo_criado.touch(exist_ok=True)

#                             with open(arquivo_criado, 'w+') as escrevendo_arquivo:
#                                 print(escrevendo_arquivo.readline(), end='')
#                                 escrevendo_arquivo.write('Linha 1\n')
#                                 escrevendo_arquivo.write('Linha 2\n')
#                                 break

from pathlib import Path

# Definindo o caminho inicial como o diretório home do usuário
caminho_home = Path.home()

# Variável de controle para parar a busca após encontrar a pasta
found = False

# Percorrendo a árvore de diretórios no caminho inicial
for root in caminho_home.rglob('*OneDrive - Electrolux/Documents'):
    if root.is_dir():  # Verifica se o caminho encontrado é uma pasta
        print('Achou pasta OneDrive - Electrolux/Documents')

        # Cria o arquivo desejado no diretório especificado
        arquivo_criado = root / 'arquivo2223.txt'
        arquivo_criado.touch(exist_ok=True)

        # Escreve no arquivo criado
        with open(arquivo_criado, 'w+') as escrevendo_arquivo:
            escrevendo_arquivo.write('Linha 1\n')
            escrevendo_arquivo.write('Linha 2\n')
        
        found = True
        break  # Encerra o loop após encontrar a pasta e criar o arquivo

if not found:
    print('Pasta "OneDrive - Electrolux/Documents" não encontrada')

print(arquivo_criado.read_text())
arquivo_criado.unlink()

