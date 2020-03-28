import random
class Juego:
    def __init__(self, size = 30):
        self.size = size

    def HacerCuadricula(self):
        self.cuadricula = []
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                self.cuadricula.append((i,j))
        return self.cuadricula

    def Colocarminas(self):
        self.minas_d = {}
        lista = self.HacerCuadricula()
        for i in lista:
            self.minas_d[i] = self.minas_d.get(i, False)
        rng = random.Random()
        for i in range(len(self.minas_d) // 5):
            Mina = rng.randrange(0, len(lista))
            self.minas_d[lista[Mina]] = self.minas_d.get(i, True)
        return self.minas_d 

    def ContarCuadros(self):
        self.minasA_dt = {}
        counter = 0
        for i in self.minas_d:
            minasC = 0
            y = self.cuadricula[counter]
            if self.minas_d[i] == False:
                if (y[0]+1,y[1]) in self.minas_d:
                    if self.minas_d[(y[0]+1,y[1])] == True:
                        minasC += 1
                if (y[0]+1,y[1]+1) in self.minas_d:
                    if self.minas_d[(y[0]+1,y[1]+1)] == True:
                        minasC += 1
                if (y[0],y[1]+1) in self.minas_d:
                    if self.minas_d[(y[0],y[1]+1)] == True:
                        minasC += 1
                if (y[0]-1,y[1]+1) in self.minas_d:
                    if self.minas_d[(y[0]-1,y[1]+1)] == True:
                        minasC += 1
                if (y[0]-1,y[1]) in self.minas_d:
                    if self.minas_d[(y[0]-1,y[1])] == True:
                        minasC += 1
                if (y[0]-1,y[1]-1) in self.minas_d:
                    if self.minas_d[(y[0]-1,y[1]-1)] == True:
                        minasC += 1
                if (y[0],y[1]-1) in self.minas_d:
                    if self.minas_d[(y[0],y[1]-1)] == True:
                        minasC += 1 
                if (y[0]+1,y[1]-1) in self.minas_d:
                    if self.minas_d[(y[0]+1,y[1]-1)] == True:
                        minasC += 1 
                self.minasA_dt[i] = self.minasA_dt.get(i, minasC)
            counter += 1
        return self.minasA_dt
        
    def ejecucion(self):
        while True:
            self.coord_x = int("Ingrese la cordenada en X")
            self.coord_y = int("Ingrese la cordenada en Y")
            self.coordenada = (self.coord_x, self.coord_y)
            
            for i in self.cuadricula:
                if i == self.coordenada:
                    if (i[0]+1, i[1]) in minasA_dt:
                        a = minasA_dt[(i[0]+1, i[1])]
                    if (i[0]+1, i[1]+1) in minasA_dt:
                        b = minasA_dt[(i[0]+1, i[1]+1)]
                    if (i[0], i[1]+1) in minasA_dt:
                        c = minasA_dt[(i[0], i[1]+1)]
                    if (i[0]-1, i[1]+1) in minasA_dt:
                        d = minasA_dt[(i[0]-1, i[1]+1)]
                    if (i[0]-1, i[1]) in minasA_dt:
                        e = minasA_dt[(i[0]-1, i[1])]
                    if (i[0]-1, i[1]-1) in minasA_dt:
                        f = minasA_dt[(i[0]-1, i[1]-1)]
                    if (i[0], i[1]-1) in minasA_dt:
                        g = minasA_dt[(i[0], i[1]-1)]
                    if (i[0]+1, i[1]-1) in minasA_dt:
                        h = minasA_dt[(i[0]+1, i[1]-1)]
            if self.minas_d[self.coordenada] == True:
                print("GAME OVER")
                return
            else:
                uncover(self.cuadricula, self.coordenada, self.minasA_dt, self.size)

    def MostrarCuadricula(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.cuadricula[counter], end= " ")
                counter += 1
            print()
    
    def uncover(self):
        for i in range(len(self.cuadricula)):
            if self.cuadricula == self.cordenadas:
                self.cuadricula = "  {0}   ".format(self.minasA_dt.get(self.coordenada))
                MostrarCuadricula(self.size, self.cuadricula)
                break
        return self.cuadricula
