# Geralmente temos associação quando um objeto tem um atributo que referencia outro objeto
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramenteDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramenteDeEscrever('Caneta BIC')

escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())
