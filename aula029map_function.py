# MAP - usada para mapear dados
from functools import partial


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
    {**p, 'preco': 123} for p in produtos
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)  # duas casas decimais


aumentar_dez_porcento = partial(
    aumentar_porcentagem, porcentagem=1.1
)


def muda_preco_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos2 = map(
    muda_preco_produtos, produtos
)

print_iter(produtos)
print_iter(novos_produtos2)

number = [1, 2, 3, 4,]

new_numbers = list(map(
    lambda x: x * 3,
    number
))
print(new_numbers)
