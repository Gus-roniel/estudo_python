# métodos de classe + factories
# são métodos onde "self" será "cls"
# Ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2024  # atributos de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod  # consegue criar um objeto, sem precisar de uma instância
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


p2 = Pessoa.criar_com_50_anos('Helena')
