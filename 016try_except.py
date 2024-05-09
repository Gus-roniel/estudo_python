# TRY, EXCEPT, ELSE E FINALLY
# TRY sozinho não funciona, deve vir com EXCEPT ou FINALLY

try: 
    a = 18
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome de variável não informado')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')