person = {
    "nome": "Gustavo",
    "sobrenome": "Silva",
    "idade": 30,
    "altura": 1.75,
}

# for chave, valor in person.items():
#     print(f'{chave}: {valor}')

d1 = {
    "v1": 1,
    "v2": 2
}

# faz uma cópia rasa dos dicionarios, nao alterando as infomações do primeiro (apenas copia valores imutáveis)
d2 = d1.copy() 

# faz uma copy profunda, copiando itens mutáveis (list, dict, etc)
import copy
d2 = copy.deepcopy(d1)

# pegar valor do chave GET (segundo argumento escolhe o que retorna se não existir)
print(person.get('nome', "não existe"))

# faz todo CRUD ao mesmo tempo UPDATE
person.update({
    "idade": 31,
    "carro": "Gol 1.0"
})

#outra forma, sem precisar adicionar as chaves como strings
person.update(nome='novo valor', idade=35)

print(person)