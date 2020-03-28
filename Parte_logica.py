import random

def HacerCuadricula(size):
    cuadricula = []
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            cuadricula.append((i,j))
    return cuadricula
            
def Colocarminas(lista):
    minas_d= {}
    for i in lista:
        minas_d[i] = minas_d.get(i, False)
    rng = random.Random()
    for i in range(len(lista) // 5):
        Mina = rng.randrange(0, len(lista))
        minas_d[lista[Mina]] = minas_d.get(i, True)
    return minas_d
        
def ContarCuadros(minas_d, cuadricula_ls):
    minasA_dt = {}
    counter = 0
    for i in minas_d:
        minasC = 0
        y = cuadricula_ls[counter]
        if minas_d[i] == False:
            if (y[0]+1,y[1]) in minas_d:
                if minas_d[(y[0]+1,y[1])] == True:
                    minasC += 1
            if (y[0]+1,y[1]+1) in minas_d:
                if minas_d[(y[0]+1,y[1]+1)] == True:
                    minasC += 1
            if (y[0],y[1]+1) in minas_d:
                if minas_d[(y[0],y[1]+1)] == True:
                    minasC += 1
            if (y[0]-1,y[1]+1) in minas_d:
                if minas_d[(y[0]-1,y[1]+1)] == True:
                    minasC += 1
            if (y[0]-1,y[1]) in minas_d:
                if minas_d[(y[0]-1,y[1])] == True:
                    minasC += 1
            if (y[0]-1,y[1]-1) in minas_d:
                if minas_d[(y[0]-1,y[1]-1)] == True:
                    minasC += 1
            if (y[0],y[1]+1) in minas_d:
                if minas_d[(y[0],y[1]+1)] == True:
                    minasC += 1
        minasA_dt[i] = minasA_dt.get(i, minasC)
        counter += 1
    return (minasA_dt)

def ejecucion(dt, dt2, ls):
    while True:
        coord_x = int(input("ingrese una coordenada en x:"))
        coord_y = int(input("ingrese una coordenada en y:"))
        coordenada = (coord_x, coord_y)
        for i in ls:
            if i == coordenada:
                y = i

        if (y[0]+1, y[1]) in dt2:
            a = dt2[(y[0]+1, y[1])]
        if (y[0]+1, y[1]+1) in dt2:
            b = dt2[(y[0]+1, y[1]+1)]
        if (y[0], y[1]+1) in dt2:
            c = dt2[(y[0], y[1]+1)]
        if (y[0]-1, y[1]+1) in dt2:
            d = dt2[(y[0]-1, y[1]+1)]
        if (y[0]-1, y[1]) in dt2:
            e = dt2[(y[0]-1, y[1])]
        if (y[0]-1, y[1]-1) in dt2:
            f = dt2[(y[0]-1, y[1]-1)]
        if (y[0], y[1]-1) in dt2:
            g = dt2[(y[0], y[1]-1)]
        if (y[0]+1, y[1]-1) in dt2:
            h = dt2[(y[0]+1, y[1]-1)]

        if dt[coordenada] == True:
            print("GAME OVER")
            return
        else:
            print(dt2[coordenada])
            """print("(1,0):", a)
            print("(1,1):", b)
            print("(0,1):", c)
            print("(-1,1):", d)
            print("(-1,0):", e)
            print("(-1,-1):", f)
            print("(0,-1):", g)
            print("(1,-1):", h)"""
        
        
def MostrarCuadricula(size, c): 
    a = 0
    for i in range(size):
        for j in range(size):
            print(c[a], end = " ")
            a += 1
        print()

#BOE


sz = int(input("Tamaño de la cuadricula simetrica:"))
cuadricula_ls = HacerCuadricula(sz)
minas_dt = Colocarminas(cuadricula_ls)
minasA_dt = ContarCuadros(minas_dt, cuadricula_ls)
MostrarCuadricula(sz, cuadricula_ls)
ejecucion(minas_dt, minasA_dt, cuadricula_ls)

#EOE
