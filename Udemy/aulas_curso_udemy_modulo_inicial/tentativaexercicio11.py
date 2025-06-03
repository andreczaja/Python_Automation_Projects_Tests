"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []

while True:

    print("Você deseja:")
    acao = input("[I]nserir, [A]pagar ou [L]istar: ")

    if acao == "i" or acao == "I":
        os.system('cls')
        if len(lista) == 0:
            print("A lista está vazia")
            item = input("Digite o item que deseja inserir: ")
            lista.append(item)
            continue
        else:
            print(lista)
            item = input("Digite o item que deseja inserir: ")
            lista.append(item)
            continue
    elif acao == "a" or acao == "A":
        os.system('cls')     
        item = input("Selecione o índice da lista que deseja excluir: ")
        try:
            indice = int(item)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
        continue
    elif acao == "l" or acao == "L":
        os.system('cls')
        print("LISTA E SEUS INDICES: ")
        for indice, item in enumerate(lista):
            print(indice, item)
        continue


    

        

    
