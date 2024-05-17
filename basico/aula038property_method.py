# @property - um getter no modo Pythonico
# getter - método para obter um atributo
# @property - propriedade do objeto. Um método que funciona como atributo
# Geralmente usada nas seguintes situações:
# - como getter
# - evitar quebrar código do cliente (onde ele usa seu código)
# - habilitar setter
# - executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

# criar uma property antes de alterar nome da
    @property
    def cor(self):
        return self.cor_tinta


caneta = Caneta('azul')

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
