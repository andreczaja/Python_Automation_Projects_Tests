a='Aaaaaa'
b='B'
c=1.1


string = 'a={0} a={0} a={0} a={0} b={1} c={2:.2f} c= {2:.5f}'
formato = string.format(a,b,c)
print(formato)

# nessa primeira estrutura, foi estabelecido por nível de índice (0,1,2) para referir-se à
# ordem dos fatores dentro a função format
# quando uma função está dentro de um objeto, essa função se chama MÉTODO
# nesse caso, a função format é um MÉTODO


string = 'a={nome1} a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
nome1=a,
nome2=b,
nome3=c
)
print(formato)
"""
1) nessa segunda estrutura, ao invés de referir-se aos objetos da string pelo índice
foi utilizado o parametro nomeado, conforme estrutura dentro dos parenteses da format
 mostrando que onde estiver 'nome1', isto se referirá ao 'a', 'nome2' será b e 'nome3' será 'c'
2) tudo que vier depois de um parametro nomeado (nome1) também precisa ser nomeado (a)
3) outra obs legal é a de que dentro da linha que inicia-se com string, o 'a=', 'b=' e 'c=' são apenas
 prefixos então, não é uma estrutura obrigatória
 """


string = 'a={a} a={a} a={a} a={a} b={b} c={c:.2f}'
formato = string.format(
    a=a,
    b=b,
    c=c
    )
print(formato)