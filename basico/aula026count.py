# count é um iterador sem fim

from itertools import count

c1 = count()
r1 = range(10)

print(next(c1))
print(next(c1))
