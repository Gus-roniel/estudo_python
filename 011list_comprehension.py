# List Comprehension é uma forma rápida para criar listas a partir de iteráveis

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# Usando list comprehension (antes do for é o que você deseja colocar)
lista2 = [numero for numero in range(10)]
# print(lista2)

lista3 = [3 for numero in range(10)]
# print(lista3)

# Pode ser usado qualquer lógica antes do for
lista4 = [
    numero * 2
    for numero in range(10)
    ]
# print(lista4)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    produto
    for produto in produtos
]

# Mapeamento = Cria nova lista mantendo mesmo tamanho, mas alterando os dados
novos_produtos_aumento_5 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # aumenta apenas se preco for maior que 20 (se colocar apenas PRODUTO, sem **, altera lista original)
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(novos_produtos)
# Mostrar produtos separados por linha nova
print(*novos_produtos, sep='\n')
print(*novos_produtos_aumento_5, sep='\n')