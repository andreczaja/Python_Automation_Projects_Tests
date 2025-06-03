import pathlib
import os

def verifica_caminho(func):
    def wrapper(pasta):
        if not os.path.isdir(pasta):
            return print('Pasta não encontrada')
        else:
            func(pasta)
    return wrapper


@verifica_caminho
def imprimir_arquivos_pasta(pasta):
    for root_,dirs_,files_ in os.walk(pasta):
        print(root_)
        for dir_ in dirs_:
            print(dir_)
        for file_ in files_:
            if file_ == 'desktop.ini':
                continue
            caminho_completo_arquivo = os.path.join(root_, file_)
            print(caminho_completo_arquivo)


pasta_downloads = os.path.join(pathlib.Path.home() , r'Downloads')

imprimir_arquivos_pasta(pasta_downloads)