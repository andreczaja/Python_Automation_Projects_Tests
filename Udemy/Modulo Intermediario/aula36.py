import aula36_m

for i in range(10):
    print(aula36_m.variavel)

# recarregando módulo no python:
    
import importlib

import aula36_m

for i in range(10):
    importlib.reload(aula36_m)
    print(i)

print('Fim')