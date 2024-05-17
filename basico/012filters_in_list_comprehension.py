# Filtros servem para que determinadas coisas não sejam inclusas na lista


# esquerda do FOR é MAPEAMENTO
# adicionar um if a direita do FOR
lista = [n for n in range(10) if n > 5]
print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
    {'nome': 'p4', 'preco': 22},
    {'nome': 'p5', 'preco': 25},
]

novos_produtos_aumento_5 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # aumenta apenas se preco for maior que 20 (se colocar apenas PRODUTO, sem **, altera lista original)
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 20
]

print(novos_produtos_aumento_5)

# Um FOR dentro de outro FOR
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
# Os 2 representam a mesma coisa
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)