def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x+y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        # mesma coisa que a função SOMA
        lambda x, y: x + y, 2,3
    )
)