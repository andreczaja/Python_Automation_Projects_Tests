
try:
    a = 18
    b = 0
    # print (b[0])

    print('Linha1'[1000])
    c= a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por Zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG', error)
    print('Nome do Erro:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')