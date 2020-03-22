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

    return c_dict, c
        
def ContarCuadros(c, c_l):
    
    h = 0
    for i in c:
        comp = 0
        y = c_l[h]
        if c[i] == False:
            if (y[0]+1,y[1]) in c:
                if c[(y[0]+1,y[1])] == True:
                    comp += 1
            if (y[0]+1,y[1]+1) in c:
                if c[(y[0]+1,y[1]+1)] == True:
                    comp += 1
            if (y[0],y[1]+1) in c:
                if c[(y[0],y[1]+1)] == True:
                    comp += 1
            if (y[0]-1,y[1]+1) in c:
                if c[(y[0]-1,y[1]+1)] == True:
                    comp += 1
            if (y[0]-1,y[1]) in c:
                if c[(y[0]-1,y[1])] == True:
                    comp += 1
            if (y[0]-1,y[1]-1) in c:
                if c[(y[0]-1,y[1]-1)] == True:
                    comp += 1
            if (y[0],y[1]+1) in c:
                if c[(y[0],y[1]+1)] == True:
                    comp += 1
        c_l[h] = (c_l[h], comp)
        h += 1    
    return (c, c_l)
        



#BOE
cuadricula = HacerCuadricula(5)
minas_d, minas = Colocarminas(cuadricula)
cuadricula2, final = ContarCuadros(minas_d, minas)
print(final)
#EOE

