# Formas de importar módulos

# INTEIRO => import nome_modulo 
    # não altera performance do programa
    # VANTAGEM: tem o namespace do módulo
    # DESVANTAGEM: nomes grandes
import sys
print(sys.platform)

# PARTES => from nome_modulo import objeto1, objeto2
    # VANTAGEM: nome pequeno
    # DESVANTAGEM: sem namespace no módulo
from sys import exit
exit() # não precisa colocar "sys.exit"
# se for criado uma variável com o mesmo nome, ela irá sobrescrever o módulo

# ALIAS 1 => import nome_modulo as apelido
# ALIAS 1 => from nome_modulo import objeto as apelido
    # VANTAGEM: pode reservar nome para código
    # DESVANTAGEM: pode ficar fora do padrão de linguagem

# MÁ PRÁTICA => from nome_modulo import *
    # VANTAGEM: importa tudo de um módulo
    # DESVANTAGEM: importa tudo de um módulo
