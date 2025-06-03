# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8 /0
except ZeroDivisionError:
    print('DIVIDIU ZERO')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')

# finally é sempre executado
# else é mostrado caso o except não ocorra