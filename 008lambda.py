# LAMBDA usada para escrever função em uma linha só

pessoas = [
    {"nome": "Ana", "sobrenome": "Silva"},
    {"nome": "Bruno", "sobrenome": "Martins"},
    {"nome": "Carla", "sobrenome": "Gomes"},
    {"nome": "Daniel", "sobrenome": "Rocha"}
]

# não consegue realizar porque precisa de um parâmetro para ordenar dicionários
# mexe na lista original
# pessoas.sort()

# cria uma nova lista (uma cópia rasa)
# sorted()

def exibir(lista):
    for item in lista:
        print(item)
    print()


# ordenou pelo que foi escolhido na função lambda
l1 = sorted(pessoas, key=lambda item: item['nome'])
l2 = sorted(pessoas, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)