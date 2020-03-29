import random
import sys

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
        
    def ejecucion(self, coordenada):
            if self.minas_d[coordenada] == True:
                    print("F")
                    sys.exit()
            else: 
                self.uncover(coordenada)  
            y = coordenada
            if self.minasA_dt[coordenada] == 0:
                self.minasA_dt[coordenada] = "0"
                if (y[0]+1, y[1]) in self.minasA_dt:
                    a = self.minasA_dt[(y[0]+1, y[1])]
                    self.uncover((y[0]+1, y[1]))
                    if a == 0:
                        self.ejecucion((y[0]+1, y[1]))
                if (y[0], y[1]+1) in self.minasA_dt:
                    c = self.minasA_dt[(y[0], y[1]+1)]
                    self.uncover((y[0], y[1]+1))
                    if c == 0:
                        self.ejecucion((y[0], y[1]+1))
                if (y[0]-1, y[1]) in self.minasA_dt:
                    e = self.minasA_dt[(y[0]-1, y[1])]
                    self.uncover((y[0]-1, y[1]))
                    if e == 0:
                        self.ejecucion((y[0]-1, y[1]))
                if (y[0], y[1]-1) in self.minasA_dt:
                    g = self.minasA_dt[(y[0], y[1]-1)]
                    self.uncover((y[0], y[1]-1))
                    if g == 0:
                        self.ejecucion((y[0], y[1]-1))
                if (y[0]+1,y[1]+1) in self.minas_d:
                    self.uncover((y[0]+1,y[1]+1))
                if (y[0]-1,y[1]+1) in self.minas_d:
                    self.uncover((y[0]-1,y[1]+1))
                if (y[0]+1,y[1]-1) in self.minas_d:
                    self.uncover((y[0]+1,y[1]-1))
                if (y[0]-1,y[1]-1) in self.minas_d:
                    self.uncover((y[0]-1,y[1]-1))
                    
    def MostrarCuadricula(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.cuadricula[counter], end= " ")
                counter += 1
            print()
        print()
    
    def uncover(self, coordenada):
        for i in range(len(self.cuadricula)):
            if self.cuadricula[i] == coordenada:
                self.cuadricula[i] = "  {0}   ".format(self.minasA_dt.get(coordenada))
   
#BOE
juego = Juego(int(input("Tamaño de la cuadricula")))
cuadricula = juego.HacerCuadricula()
minas_d = juego.Colocarminas()
minasA_dt = juego.ContarCuadros()
juego.MostrarCuadricula()
while True:
    coord_x = int(input("ingrese una coordenada en x:"))
    coord_y = int(input("ingrese una coordenada en y:"))
    juego.coordenada = (coord_x, coord_y)
    juego.ejecucion(juego.coordenada)
    juego.MostrarCuadricula()
#EOE
