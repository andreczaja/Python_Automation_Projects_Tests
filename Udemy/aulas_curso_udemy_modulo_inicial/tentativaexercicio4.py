"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
while True:

    if idade.isnumeric():
    
        condicao_tudo_ok = (nome != '' and nome != ' ') and (idade != '' and idade != ' ')
        condicao_sem_nome = (nome == '' or nome == ' ') and (idade != "" and idade != ' ')
        condicao_sem_idade = (nome != '' and nome != ' ') and (idade == '' or idade == ' ')
        espaco_no_nome = " " in nome

        if condicao_tudo_ok == True:
            print(f'Seu nome é {nome}')
            print(f'Seu nome invertido é {nome[::-1]}')
            print(f'Seu nome contém {len(nome)} caracteres.')
            print(f'A primeira letra do seu nome é a {nome[0]}')
            print(f'A última letra do seu nome é a {nome[-1]}')
            if espaco_no_nome == True:
                print("Seu nome contém espaços.")
            else:
                print("Seu nome não contém espaços.")

        if condicao_sem_nome == True:
            print("Você não digitou seu nome!")
            break
        if condicao_sem_idade == True:
            print("Você não digitou sua idade!")
            break

        break
    else:
        print("Você não digitou sua idade!")
    break
    



    
