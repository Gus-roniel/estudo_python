# O primeiro módulo executado chama-se __main__
# É possível importar o módulo inteiro ou apenas parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# Python conhece todos os módulos e pacotes presentes no caminho de sys.path

import aa
from aa import variavel_modulo

print(aa.variavel_modulo)
print(variavel_modulo)