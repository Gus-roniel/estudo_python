# métodos em instâncias de classes Python
# hard coded - algo escrito diretamente no código


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
