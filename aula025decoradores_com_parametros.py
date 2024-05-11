# decoradores com parametros

def decoradora(func):
    # print(func)
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        result = func(*args, **kwargs)
        print(args)
        print(kwargs)
        return result
    return aninhada


@decoradora
def soma(*args):
    return sum(args)


dez_mais_cinco = soma(10, 5, 22)
print(dez_mais_cinco)
