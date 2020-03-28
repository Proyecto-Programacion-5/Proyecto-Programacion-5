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
    print(minas_d)
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
            if (y[0],y[1]-1) in minas_d:
                if minas_d[(y[0],y[1]-1)] == True:
                    minasC += 1 
            if (y[0]+1,y[1]-1) in minas_d:
                if minas_d[(y[0]+1,y[1]-1)] == True:
                    minasC += 1 
            minasA_dt[i] = minasA_dt.get(i, minasC)
        counter += 1
    print(minasA_dt)
    return (minasA_dt)

def ejecucion(minas_dt, minasA_dt, cuadricula, coordenada, size):
    
    while True:
        if minas_dt[coordenada] == True:
                print("GAME OVER")
                return
        else: 
            uncover(cuadricula, coordenada, minasA_dt, size)    
        y = coordenada
        minasA_dt[coordenada] = "0"
        if (y[0]+1, y[1]) in minasA_dt:
            a = minasA_dt[(y[0]+1, y[1])] 
            if a == 0:
                ejecucion(minas_dt, minasA_dt, cuadricula, (y[0]+1, y[1]), size)
        if (y[0], y[1]+1) in minasA_dt:
            c = minasA_dt[(y[0], y[1]+1)]
            if c == 0:
                ejecucion(minas_dt, minasA_dt, cuadricula, (y[0], y[1]+1), size)
        if (y[0]-1, y[1]) in minasA_dt:
            e = minasA_dt[(y[0]-1, y[1])]
            if e == 0:
                ejecucion(minas_dt, minasA_dt, cuadricula, (y[0]-1, y[1]), size)
        if (y[0], y[1]-1) in minasA_dt:
            g = minasA_dt[(y[0], y[1]-1)]
            if g == 0:
                ejecucion(minas_dt, minasA_dt, cuadricula, (y[0], y[1]-1), size)
            
        coord_x = int(input("ingrese una coordenada en x:"))
        coord_y = int(input("ingrese una coordenada en y:"))
        coordenada = (coord_x, coord_y)
            
    
def MostrarCuadricula(size, cuadricula): 
    counter = 0
    for i in range(size):
        for j in range(size):
            print(cuadricula[counter], end = " ")
            counter += 1
        print()
    print()
        
def uncover(cuadricula, coordenada, minasA_dt, sz):
    for i in range(len(cuadricula)):
        if cuadricula[i] == coordenada:
            cuadricula[i] = "  {0}   ".format(minasA_dt.get(coordenada))
            MostrarCuadricula(sz, cuadricula)
            break
    return cuadricula


#BOE


sz = int(input("Tamaño de la cuadricula simetrica:"))
cuadricula_ls = HacerCuadricula(sz)
minas_dt = Colocarminas(cuadricula_ls)
minasA_dt = ContarCuadros(minas_dt, cuadricula_ls)
MostrarCuadricula(sz, cuadricula_ls)

coord_x = int(input("ingrese una coordenada en x:"))
coord_y = int(input("ingrese una coordenada en y:"))
coordenada = (coord_x, coord_y)
ejecucion(minas_dt, minasA_dt, cuadricula_ls, coordenada, sz)

#EOE
