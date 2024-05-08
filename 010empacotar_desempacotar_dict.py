a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Gustavo',
    'Sobrenome': 'Silva'
}

a, b = pessoa # atribui a chave
a, b = pessoa.values() # atribui a valor
a, b = pessoa.items() # atribui ao conjunto chave/valor

(a1, a2), (b1, b2) = pessoa.items()
# print(a, b)

# print(a1, a2)
# print(b1, b2)

# desempacotamento num iterável
# for chave, valor in pessoa.items():
    # print(chave, valor)

pessoa2 = {
    'nome': 'Niqueli',
    'sobrenomenome': 'Costa'
}
dados_pessoa = {
    'idade': 36,
    'altura': 1.6
}

# desempacotamento de dois dicionários completos dentro de um novo
pessoa2_completa = {**pessoa2, **dados_pessoa}
print(pessoa2_completa)

# KWARGS - serve para receber argumentos nomes (ARGS é para não nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args )

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)