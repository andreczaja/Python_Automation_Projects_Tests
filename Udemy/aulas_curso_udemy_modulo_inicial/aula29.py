senha_salva = '123456'
senha_digitada = input('Digite sua senha: ')
repeticoes = 0


while senha_salva != senha_digitada:
    senha_digitada = input(f'Você digitou a senha incorreta ({repeticoes} X \
                           se errar mais {5- repeticoes} vezes o sistema bloqueará seu acesso: ')
    
    repeticoes += 1
    if repeticoes == 5:
        print('Sistema bloqueado')
        break

if senha_digitada == senha_salva:
    print('Bem vindo')
