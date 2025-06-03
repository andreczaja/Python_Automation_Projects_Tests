class Melhorias:
    def __init__(self, melhoria, qtde_horas_salvas):
        self._melhoriaoioioi = melhoria
        self.qtde_horas_salvas = qtde_horas_salvas

    @classmethod
    def melhoria_sem_horas_salvas(cls, melhoria):
        return cls(melhoria, 'SEM HORAS SALVAS') 
    
    @property
    def melhoria(self):
        return self._melhoriaoioioi 
    
    @melhoria.setter
    def melhoria(self, novo_nome_melhoria):
        self._melhoriaoioioi = novo_nome_melhoria 

    
m1 = Melhorias('cobrança', '7 horas')
m2 = Melhorias('refacturacion', '10 horas')
m3 = Melhorias.melhoria_sem_horas_salvas('canje')

print(m1.melhoria, m1.qtde_horas_salvas)
print(m2.melhoria, m2.qtde_horas_salvas)
print(m3.melhoria, m3.qtde_horas_salvas)

m1.melhoria = 'cobrança_v_02'

print(m1.melhoria)

