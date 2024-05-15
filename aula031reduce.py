# faz a reducao de um iteravel em um único valor
from functools import reduce

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 1105.87},
    {'nome': 'produto 4', 'preco': 69.90}
]

total = 0
for p in produtos:
    total += p['preco']
print(total)


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total2 = reduce(
    # funcao_do_reduce,
    lambda ac, p: ac + p['preco'],
    produtos,
    0  # valor inicial
)

print(f'O total é: R$ {total2:.2f}')
