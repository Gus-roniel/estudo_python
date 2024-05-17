# TRY, EXCEPT, ELSE E FINALLY
# TRY sozinho não funciona, deve vir com EXCEPT ou FINALLY

try: 
    a = 18
    b = 0
    print('Linha 1' [1000])
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Nome de variável não informado')
except (TypeError, IndexError) as error: # qual variável quero jogar o nome do erro
    print('MSG:', error.__class__.__name__) # descobrir qual erro está ocorrendo
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')