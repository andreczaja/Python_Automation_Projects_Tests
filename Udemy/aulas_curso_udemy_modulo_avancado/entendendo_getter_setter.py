class Caneta:
    def __init__(self, cor):
        self._cor = cor

    # Getter para cor
    @property
    def cor(self):
        return self._cor

    # Setter para cor
    @cor.setter
    def cor(self, nova_cor):
        if not nova_cor:
            raise ValueError("A cor não pode ser vazia.")
        self._cor = nova_cor

# Criando uma instância de Caneta
c1 = Caneta('Azul')

# Usando o getter
print(c1.cor)  # Saída: Azul

# Usando o setter
c1.cor = 'Preta'

# Usando o getter após a modificação
print(c1.cor)  # Saída: Preta

# Tentando definir uma cor vazia (isso irá gerar um erro)
try:
    c1.cor = ''
except ValueError as e:
    print(e)  # Saída: A cor não pode ser vazia.
