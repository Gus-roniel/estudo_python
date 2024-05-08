import os

def multiplicate(*args):
    os.system("cls")
    total = 1
    for number in args:
        total*= number

    if total % 2 == 0:
        return f'O número {total} é par'
    return f'O número {total} é ímpar'

print(multiplicate(23, 77, 49, 51))