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
    c2 = {}
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
        #c_l[h] = (c_l[h], comp)
        c2[i] = c2.get(i, comp)
        h += 1
    return (c, c2, c_l)

def ejecucion(coord_ing, dt, dt2, ls):

    if dt[coord_ing] == True:
        print("GAME OVER")
    else:
        print("(1,0): {0}".format(dt2[(ls[0]+1,ls[1])]))
        print("(1,1):{0}".format(dt2[(ls[0]+1,ls[1]+1)]))
        print("(0,1):{0}".format(dt2[(ls[0],ls[1]+1)]))
        print("(-1,1):{0}".format(dt2[(ls[0]-1,ls[1]+1)]))
        print("(-1,0):{0}".format(dt2[(ls[0]-1,ls[1])]))
        print("(-1,-1):{0}".format(dt2[(ls[0]-1,ls[1]-1)]))
        print("(0,-1):{0}".format(dt2[(ls[0],ls[1]-1)]))
        print("(1,-1):{0}".format(dt2[(ls[0]+1,ls[1]-1)]))
    
        



#BOE
sz = int(input("Tamaño de la cuadricula simetrica:"))
intento_x = int(input("ingrese una coordenada en x:"))
intento_y = int(input("ingrese una coordenada en y:"))
intento = (intento_x, intento_y)
cuadricula_ls = HacerCuadricula(5)
minas_d, minas = Colocarminas(cuadricula_ls)
mapa, cuadricula2_dt, final_ls = ContarCuadros(minas_d, minas)
ejecucion(intento, mapa, cuadricula2_dt, final_ls)

#EOE


