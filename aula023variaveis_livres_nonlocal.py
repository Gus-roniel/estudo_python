def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        # nao pode alterar valor de uma variavel global dentro de um escopo
        # valor_final += valor_a_concatenar
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar("a")

print(c('b'))
print(c('c'))
print(c('d'))
