# finally executa sempre, mesmo que não ocorra um erro
# Ex: você executou o código e deu tudo certo. No final fechar o arquivo
# pode ter o except também, quando quiser tratar o erro
# Pode ter quantos erros quiser, tratando cada erro

try:
    print(1 + "1")
except TypeError as e:
    print("MSG", e.__class__.__name__)
finally:
    print(2)