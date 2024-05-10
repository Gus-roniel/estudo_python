# Erro na programação é bom porque descobrimos o que corrigir
# RAISE - relança o erro \ criar próprio erro
# Normalmente utilizado quando algo dá errado e quer salvar na memória por exemplo

def nao_aceito_zero(b):
    if b == 0:
        raise ZeroDivisionError ('Você está tentando dividir um número por zero')
    return True
    
def divide(a, b):
    nao_aceito_zero(b)
    return a / b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print("Log de erro:", e)
    raise  # Relança a exceção atual

# Pode ser usado também para criar minhas próprias exceções
class SaldoInsuficienteError(Exception):
    pass

def sacar(valor):
    saldo = 100
    if valor > saldo:
        raise SaldoInsuficienteError("Você não tem saldo suficiente.")
    saldo -= valor
    return saldo

