import os

os.system('cls')

class MyOpen:
    def __init__(self, caminho_arquivo,modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('abrindo')
        self._arquivo = open(self.caminho_arquivo,self.modo,encoding='UTF8')
        return self._arquivo
    
    def __exit__(self, class_exception,exception_, traceback):
        print('fechando')
        print(class_exception)
        print(exception_)
        print(traceback)
        if not class_exception is None: 
            raise class_exception('Minha mensagem')
        self._arquivo.close()


caminho_arquivo = os.path.abspath(__file__).replace('.py','.txt')

with MyOpen(caminho_arquivo, 'w+') as escrevendo_arquivo:
    print('escrevendo...')
    escrevendo_arquivo.write('Linha 1\n',123)
    escrevendo_arquivo.write('Linha 2\n')
    escrevendo_arquivo.write('Linha 3\n')

with MyOpen(caminho_arquivo, 'r') as escrevendo_arquivo:
    print(escrevendo_arquivo.read())