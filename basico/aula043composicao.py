# Composição é uma especialização da agregação
# Nela, quando o objeto pai for apagado, todas as referências dos objetos filhos também são apagadas

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

#   Quando o Cliete nao existir mais, a instancia Endereco, também vai deixar de existir
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            # print(self.enderecos(endereco(rua, numero)))
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 123)

cliente1.listar_enderecos()
