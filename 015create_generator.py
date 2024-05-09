# Generator é uma função que pode pausar, quando chamada novamento, ela continua de onde parou
# Sempre que tiver um yield, é um generator 

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        


gen = generator()

for n in gen:
    print(n)