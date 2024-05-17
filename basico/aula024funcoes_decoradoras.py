# decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Usada para fazer Python usar funções decoradoras em outras funções

def inverte_string(string):
    return string[::-1]


invertida = inverte_string('Gustavo')
print(invertida)
