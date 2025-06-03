from contextlib import contextmanager
import os

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo,modo, encoding = 'UTF8')
        yield arquivo
    except Exception as e:
        print('ocorreu um erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

caminho_arquivo = os.path.abspath(__file__).replace('.py','.txt')
with my_open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
