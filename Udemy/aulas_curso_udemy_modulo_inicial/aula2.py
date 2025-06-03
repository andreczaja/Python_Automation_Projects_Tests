# nesse caso, o \n no fim da linha 3 está determinando uma quebra de linha, por isso,
# ao rodarmos esse primeiro código, os prints aparecerão em linhas separadas no terminal
print(12, 34,"oi", sep="-",end='\n')
print(12, 34,sep='oi')
 
 # nesse caso, o ## no fim da linha 3 não determina quebra de linha pois são apenas caracteres comuns, por isso,
# ao rodarmos esse segundo código, os prints aparecerão NA MESMA LINHA

print(12, 34,"oi", sep="-",end='##')
print(12, 34,sep='oi')