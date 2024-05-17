# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - evitar quebrar código do cliente (onde ele usa seu código)
# - habilitar setter
# - executar ações ao obter um atributo
# atributos que começam com 1 ou 2 underlines, não devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

# pode ser usada para restringir determinado valor
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('não aceito essa cor')
        self._cor = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'

print(caneta.cor)
