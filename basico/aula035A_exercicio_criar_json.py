# criar arquivo json

import json

CAMINHO_ARQUIVO = 'aula035.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 25)
p2 = Pessoa('Joana', 18)
p3 = Pessoa('Helena', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
