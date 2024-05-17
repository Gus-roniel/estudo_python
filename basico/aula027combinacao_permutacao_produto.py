# combinations, permutations and product - Itertool
# combinacao - ordem nao importa - iterável - tamanho do grupo
# permutacao - ordem importa
# produto - ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['P', 'M']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
