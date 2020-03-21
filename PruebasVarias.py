import random

def HacerCuadricula(a):
    c = []
    minas = []
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            c.append((i,j))
    rng = random.Random()
    print(len(c))
    for i in range(len(c) // 5):
        Mina = rng.randrange(0, len(c))
        c[Mina] = (c[Mina], "mina")
    h = 0
    comp = 0
    for i in c:
        if "mina" not in i:
            if "mina" in (i[0]+1,i[1]):
                comp += 1
            if "mina" in (i[0]+1,i[1]+1):
                comp += 1
            if "mina" in (i[0],i[1]+1):
                comp += 1
            if "mina" in (i[0]-1,i[1]+1):
                comp += 1
            if "mina" in (i[0]-1,i[1]):
                comp += 1
            if "mina" in (i[0]-1,i[1]-1):
                comp += 1
            if "mina" in (i[0],i[1]+1):
                comp += 1
        

            
            
    for i in c:
        if "mina" not in i:
           c[h] = (c[h], N_minas)
        h += 1
    return c

    
print(HacerCuadricula(10))
