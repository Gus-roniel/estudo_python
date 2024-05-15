# atributos de classe


class Pessoa:
    ANO_ATUAL = 2024
    atributo = 'Valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Maria', 20)

print(p1.get_ano_de_nascimento())
