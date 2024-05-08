# Sets são conjuntos com tipos de dados
# São mutáveis, mas aceitam apenas tipos imutáveis
# eficientes para remover valores duplicados
# Valores são sempre únicos
# não tem índexes
# não garantem ordem
# São interáveis (for, in, not in)

s1 = set()
s2 = {'Gustavo', 1, 2, 3} # pareceidos com objetos, mas não tem chave

# MÉTODOS ÚTEIS

# ADD - Adiciona apenas um valor
s1 = set()
s1.add('Gustavo')
# print(s1)

# UPDATE - adiciona fora de ordem
s2 = set()
s2.update('Roniel') #adiciona letras separadas
s2.update(('Roniel', 2, 4)) # adiciona palavras inteiras (tuplas)
# print(s2)

# CLEAR - limpa todo ele
# DISCARD - elimina o valor digitado dentro


# OPERADORES ÚTEIS
q1 = {1, 2, 3}
q2 = {2, 3, 4}
q3 = q1 

# UNIÃO | UNION = une
q3 = q1 | q2
print(q3)
# INTESECÇÃO | INTERSECTION = itens presentes em ambos
q4 = q2 & q1
print(q4)
# DIFERENÇA - itens presentes apenas no set da esquerda
q5 = q3 - q2
print(q5)
# DIFERENÇA SIMÉTRICA ^- itens que não estão em ambos
q6 = q1 ^ q2
print(q6)

