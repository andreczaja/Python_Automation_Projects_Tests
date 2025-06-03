frase = 'O Python é uma linguagem de programação' \
        'multiparadigma. Python foi criado por Guido van Rossum'


i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
lenfrase = len(frase)


while i < lenfrase:
    letra_atual = frase[i]
    qtd_apareceu_letra_atual = frase.count(letra_atual)
    if letra_atual == " ":
        i += 1
        continue

    if qtd_apareceu_letra_atual > qtd_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_apareceu_letra_atual 
        letra_apareceu_mais_vezes = letra_atual
        print( letra_atual, qtd_apareceu_letra_atual)
        i += 1
    else:
        print(letra_atual, qtd_apareceu_letra_atual)
        i += 1

print(f'A letra que mais apareceu na frase foi a letra "{letra_apareceu_mais_vezes.upper()}" que \
apareceu {qtd_apareceu_mais_vezes}X. Joia ;D"')


# DEU BOA!!


        