import random

def HacerCuadricula(a):
    c = []
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            c.append((i,j))
    rng = random.Random()
    print(len(c))
    for i in range(len(c) // 5):
        Mina = rng.randrange(0, len(c))
        c[Mina] = (c[Mina], 1)
    return c

    
print(HacerCuadricula(10))
