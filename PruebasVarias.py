import random

def HacerCuadricula(a):
    c = []
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            c.append((i,j))
    return c
            
def Colocarminas(c):
    c_dict = {}
    for i in c:
        c_dict[i] = c_dict.get(i, False)
    rng = random.Random()
    for i in range(len(c) // 5):
        Mina = rng.randrange(0, len(c))
        # c[Mina] = (c[Mina], "mina")
        c_dict[c[Mina]] = c_dict.get(i, True)
    print(c_dict)

    return c_dict, c
        
def ContarCuadros(c, c_l):
    comp = 0
    h = 0
    for i in c:
        
        if c[i] == False:
            if (i[0]+1,i[1]) == True:
                comp += 1
            if (i[0]+1,i[1]+1) == T:
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
        c[h] = (c[h], comp)
        h += 1    
    return c
        



#BOE
cuadricula = HacerCuadricula(5)
minas_d, minas = Colocarminas(cuadricula)
cuadricula2 = ContarCuadros(minas_d, minas)
print(cuadricula2)
#EOE
