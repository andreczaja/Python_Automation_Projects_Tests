import time

def calcula_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {(fim - inicio):.5f} segundos")
        return resultado
    return wrapper

@calcula_tempo
def funcao_lenta():
    print("Função lenta executada")

funcao_lenta()