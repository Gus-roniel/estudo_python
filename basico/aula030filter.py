def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90}
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
]

novos_produtos2 = filter(
    lambda p: p['preco'] > 30,  # funcao
    produtos  # qual variavel usar
)

print_iter(novos_produtos)
print_iter(novos_produtos2)
