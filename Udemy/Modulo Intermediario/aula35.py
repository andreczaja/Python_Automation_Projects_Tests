# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se _main_
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o _main_ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do _main_ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula35_m

print('Este módulo se chama', __name__)


# é possível manipular apenas módulos que estão na mesma pasta do módulo atual ou em pastas na mesma path da pasta atual
# se for necessário acessar módulos de outros locais do computador, será necessário manipular a sys.path

print(aula35_m.variavel_modulo)

print(aula35_m.soma(2,3))
