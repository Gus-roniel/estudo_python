# class - são moldes para criar novos objetos
# Geram novos objetos que podem ter seus proóprios atributos e métodos
# objetos gerados pela classe podem usar seus dados internos para realizar várias ações
# Por convenção, usamos PascalCase para nomes de classes

class Pessoa:
    def __init__(self, nome: int, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Gustavo", "Silva")

print(p1.nome)
print(p1.sobrenome)
