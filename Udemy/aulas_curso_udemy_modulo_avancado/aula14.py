# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Teste:
    def __init__(self):
        self.publica = 'publica'
        self._protected = 'protected'
        self.__privada = 'privada'
        

    def metodo_publica(self):
        print(self.publica)
        self._metodo_protegida()

    def _metodo_protegida(self):
        print(self._protected)
        self.__metodo_privada()

    def __metodo_privada(self):
        print(self.__privada)
    

t1 = Teste()
t1.metodo_publica()

