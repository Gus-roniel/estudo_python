# __dict__ e vers para atributos de instância
# __dict__ mostra ou altera um dicionário com as informações geradas

class Pessoa:
    ANO_ATUAL = 2024
    atributo = 'Valor'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade


p1 = Pessoa('João', 35)
dados = {'nome': 'Maria', 'idade': 22, }
p1.__dict__['outra coisa'] = "coisa"
# print(p1.__dict__)
# print(vars(p1))

# desempacota os dados de um arquivo json e gera um novo objeto
p2 = Pessoa(**dados)
print(vars(p2))
