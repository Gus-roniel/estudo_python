produto = {
    'nome': 'caneta azul',
    'valor': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    # detalhe no tupla onde pode ser definido mais de um valor
    if isinstance(valor, (str, int)) else valor
    for chave, valor
    in produto.items()
}

print(dc)

# o que verifica / qual o tipo (pode ser criado tuplas para mais de um tipo)
for item in produto.values():
    print(isinstance(item, str))