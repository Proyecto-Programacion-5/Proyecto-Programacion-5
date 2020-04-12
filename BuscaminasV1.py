import random
import sys
import time

class Juego:
    #Inicializador de la clase
    def __init__(self, size = 30):
        self.size = size
        self.cont_band = 0
        self.banderas_restantes = 0
        self.banderas_max = 0
        self.estado = ""
        if size < 0:
            cuadricula_negativa = ValueError("No se puede hacer una cuadricula con valores negativos")
            raise cuadricula_negativa

    #Metodo que crea una cuadricula de coordenadas
    def HacerCuadricula(self):
        self.cuadricula = []
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                self.cuadricula.append((j,i))
        self.cc = self.cuadricula[:]
        return self.cuadricula

    #Metodo que asigna minas a una parte de las coordenadas de la cuadricula
    def Colocarminas(self):
        self.minas_d = {}
        lista = self.HacerCuadricula()
        self.banderas_restantes = 0
        self.banderas_max = 0
        for i in lista:
            self.minas_d[i] = self.minas_d.get(i, False)
        rng = random.Random()
        for i in range(len(self.minas_d) // 5):
            Mina = rng.randrange(0, len(lista))
            self.minas_d[lista[Mina]] = self.minas_d.get(i, True)
        for i in self.minas_d:
            if self.minas_d.get(i) == True:
                self.banderas_restantes +=1
                self.banderas_max +=1
        return self.minas_d 

    #Metodo que mezcla las minas para que el jugador no pierda en el primer turno
    def safe(self):
        while self.minasA_dt[self.coordenada] != 0:
            self.Colocarminas()
            self.ContarCuadros()
    
    #Metodo que cuenta las minas que estan alrededor de algun cuadro
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
        for i in self.cuadricula:
            if i not in self.minasA_dt:
                self.minasA_dt[i] = self.minasA_dt.get(i, True)
        return self.minasA_dt
    
    #Metodo que coloca banderas en el mapa
    def Banderas(self, coordenada):
        if self.banderas_restantes == 0:
            print("No quedan banderas para colocar")
        else:
            for i in range(len(self.cc)):
                if self.cc[i] == coordenada:
                    self.cuadricula[i] = "  B   "
                    self.banderas_restantes -=1
                    break
        
    #Metodo que elimina minas del mapa
    def QuitarBanderas(self, coordenada):
        if self.banderas_max == self.banderas_restantes:
            print("No hay banderas que quitar")
        else:    
            for i in range(len(self.cc)):
                if self.cc[i] == coordenada:
                    self.cuadricula[i] = coordenada
                    self.banderas_restantes +=1
                    break
        


    def ejecucion(self, coordenada):
        coord_outrange = ValueError("Coordenada Fuera de rango")
        if coordenada not in self.cc:
            raise coord_outrange
        self.comp_victoria()

        if self.estado == "B" or self.estado == "b":
            self.Banderas(coordenada)
            if self.minas_d[coordenada] == True:
                self.cont_band += 1
        
        elif self.estado == "X" or self.estado == "x":
            self.QuitarBanderas(coordenada)
            if self.minas_d[coordenada] == True:
                self.cont_band -= 1

        else:

            if self.minas_d[coordenada] == True:
                    print("F")
                    juego.MostrarRespuesta()
                    t2 = time.clock()
                    print("Tiempo: {0} segundos.".format(t2-t1))
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
                    a = self.minasA_dt[(y[0], y[1]+1)]
                    self.uncover((y[0], y[1]+1))
                    if a == 0:
                        self.ejecucion((y[0], y[1]+1))
                if (y[0]-1, y[1]) in self.minasA_dt:
                    a = self.minasA_dt[(y[0]-1, y[1])]
                    self.uncover((y[0]-1, y[1]))
                    if a == 0:
                        self.ejecucion((y[0]-1, y[1]))
                if (y[0], y[1]-1) in self.minasA_dt:
                    a = self.minasA_dt[(y[0], y[1]-1)]
                    self.uncover((y[0], y[1]-1))
                    if a == 0:
                        self.ejecucion((y[0], y[1]-1))
                if (y[0]+1,y[1]+1) in self.minas_d:
                    a = self.minasA_dt[(y[0]+1,y[1]+1)]
                    self.uncover((y[0]+1,y[1]+1))
                    if a == 0:
                        self.ejecucion((y[0]+1,y[1]+1))
                if (y[0]-1,y[1]+1) in self.minas_d:
                    a = self.minasA_dt[(y[0]-1,y[1]+1)]
                    self.uncover((y[0]-1,y[1]+1))
                    if a == 0:
                        self.ejecucion((y[0]-1,y[1]+1))
                if (y[0]+1,y[1]-1) in self.minas_d:
                    a = self.minasA_dt[(y[0]+1,y[1]-1)]
                    self.uncover((y[0]+1,y[1]-1))
                    if a == 0:
                        self.ejecucion((y[0]+1,y[1]-1))
                if (y[0]-1,y[1]-1) in self.minas_d:
                    a = self.minasA_dt[(y[0]-1,y[1]-1)]
                    self.uncover((y[0]-1,y[1]-1))
                    if a == 0:
                        self.ejecucion((y[0]-1,y[1]-1))
       
    #Metodo que imprime el estado actual del mapa                 
    def MostrarCuadricula(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.cuadricula[counter], end= " ")
                counter += 1
            print()
        print()
    
    #Metodo que muestra la solucion si el jugador pierde
    def MostrarRespuesta(self):
        resp = []
        for i in self.minas_d.values():
            if i == True:
                resp.append("  *   ")
            else:
                resp.append("  0   ")
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                print(resp[counter], end= " ")
                counter += 1
            print()
        print()

    #Metodo que destapa una casilla del mapa
    def uncover(self, coordenada):
        for i in range(len(self.cuadricula)):
            if self.cuadricula[i] == coordenada:
                self.cuadricula[i] = "  {0}   ".format(self.minasA_dt.get(coordenada))

    #Metodo que envia mensaje de victoria
    def comp_victoria(self):
        if self.cont_band == self.banderas_max:
            print("VICTORIA")
            return "v"
    
    

        
#BOE
m = 0
juego = Juego(int(input("Tamaño de la cuadricula:")))
cuadricula = juego.HacerCuadricula()
minas_d = juego.Colocarminas()
minasA_dt = juego.ContarCuadros()
juego.MostrarCuadricula()
t1 = time.perf_counter()
while True:
    """ DEVELOPMENT 
    print(juego.minas_d)
    print(juego.minasA_dt)
        TOOLS """
        
    juego.estado = input("B para bandera, X para quitar bandera, cualquier otro para continuar:")
    coord_x = int(input("ingrese una coordenada en x:"))
    coord_y = int(input("ingrese una coordenada en y:"))

    juego.coordenada = (coord_x, coord_y)
    
    if m == 0:
        juego.safe()
        m = 1
    juego.ejecucion(juego.coordenada)
    juego.MostrarCuadricula()
    print("Quedan {0} Banderas por colocar.".format(juego.banderas_restantes))
    if juego.cont_band == juego.banderas_max:
        print("VICTORIA")
        print(juego.banderas_max)
        t2 = time.perf_counter()
        print("Tiempo: {0} segundos.".format(t2 - t1))
        print(3 * "\n")
        sys.exit()

#EOE
