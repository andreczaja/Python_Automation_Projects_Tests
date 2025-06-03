"""
Closure e funções que retornam outras funções
"""


# def criar_saudacao(saudacao):
#     def saudar(*args):
#         nomes = ', '.join(args)
#         return f'{saudacao}, {nomes}!'
#     return saudar


# falar_bom_dia = criar_saudacao('Bom dia')

# s1 = falar_bom_dia('dé','Larissa', 'Ana', 'Jorge')
# print(s1)
# s2 = falar_bom_dia()
# print(s2)
# falar_boa_noite = criar_saudacao('Boa noite')
# print(falar_boa_noite('larissa'))

# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))


def saudacao(saudacao):
    def mensagem(nome):
        return f"{saudacao}, {nome}!"
    return mensagem

cumprimenta = saudacao("Olá")
print(cumprimenta("Maria"))  # Saída: Olá, Maria!
print(cumprimenta("João"))   # Saída: Olá, João!