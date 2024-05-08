import sys

# Pode acessar itens por índice
lista = [n for n in range(1000000)]

# diminui bastante o uso de memória, mas não tem índice, nem sabe o tamanho, apenas manda o próximo número
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))