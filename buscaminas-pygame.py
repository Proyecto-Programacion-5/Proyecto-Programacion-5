import random
import time
import pygame

class Juego:
    #Inicializador de la clase. Crea la cuadricula, las minas y los valores de cada cuadro
    def __init__(self):
        self.size = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 4:"))
        while self.size < 4:
            print("La cuadricula debe ser mayor que 4\n")
            self.size = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 4:"))
        
        self.fuente = pygame.font.SysFont('newyorkitalicttf', 50, True)
        self.ventana = pygame.display.set_mode((1800, 1000))
        pygame.display.set_caption("Buscaminas")    
        self.centro = self.ventana.get_rect().center
    
        mina = pygame.image.load("Mina.png")
        self.mina = pygame.transform.scale(mina, (50 , 50))
    
        bandera = pygame.image.load("Bandera.png")
        self.bandera = pygame.transform.scale(bandera, (50, 50))
        self.coord = {}
        self.width = 50
        self.cont_band = 0
        self.banderas_restantes = 0
        self.banderas_max = 0
        self.estado = {}       
        self.est = ""
        self.cuadricula = []
        self.HacerCuadricula()
        self.minas_d = {}
        self.ColocarMinas()
        self.minasA_dt = {}
        self.ContarCuadros()
        

    #Metodo que crea una cuadricula de coordenadas
    def HacerCuadricula(self):
        x = self.centro[0] - (self.size * (self.width + 5) / 2)
        y = self.centro[1] - (self.size * (self.width + 5) / 2)
        for i in range(self.size):
            for j in range(self.size):
                self.coord[(x,y)] = self.coord.get((x,y), (192, 192, 192))
                self.cuadricula.append((x,y))
                x += self.width + 5
            x -= (self.width + 5) * self.size
            y += self.width + 5
        
    #Metodo que imprime el mapa              
    def MostrarCuadricula(self):
        for i in self.cuadricula:
            color = self.coord.get(i)
            x = i[0]
            y = i[1]
            pygame.draw.polygon(self.ventana, (224, 224, 224), [(x + self.width, y),(x + self.width + 2.5, y - 2.5),  (x - 2.5, y - 2.5), (x - 2.5, y + self.width + 2.5), (x, y + self.width), (x, y)])
            pygame.draw.polygon(self.ventana, (96, 96, 96), [(x, y + self.width), (x - 2.5, y + self.width + 2.5), (x + self.width + 2.5, y + self.width + 2.5), (x + self.width + 2.5, y - 2.5), (x + self.width, y), (x + self.width, y + self.width)])
            pygame.draw.rect(self.ventana, (color), (x, y, self.width, self.width))

        
    #Metodo que asigna minas a una parte de las coordenadas de la cuadricula
    def ColocarMinas(self):
        self.minas_d = {}
        self.banderas_restantes = 0
        self.banderas_max = 0
        for i in self.cuadricula:
            self.minas_d[i] = self.minas_d.get(i, False)
        rng = random.Random()
        for i in range(len(self.minas_d) // 5):
            Mina = rng.randrange(0, len(self.cuadricula))
            self.minas_d[self.cuadricula[Mina]] = self.minas_d.get(i, True)
        for i in self.minas_d:
            if self.minas_d.get(i) == True:
                self.banderas_restantes +=1
                self.banderas_max +=1

    #Metodo que mezcla las minas para que el jugador no pierda en el primer turno
    def safe(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                while self.minasA_dt[i] != 0:
                    self.ColocarMinas()
                    self.ContarCuadros()
                    
   
    #Metodo que cuenta las minas que estan alrededor de algun cuadro
    def ContarCuadros(self):
        self.minasA_dt = {}
        counter = 0
        for i in self.minas_d:
            minasC = 0
            y = self.cuadricula[counter]
            if self.minas_d[i] == True:
                self.minasA_dt[i] = True
            else:
                if (y[0]+55,y[1]) in self.minas_d:
                    if self.minas_d[(y[0]+55,y[1])] == True:
                        minasC += 1
                if (y[0]+55,y[1]+55) in self.minas_d:
                    if self.minas_d[(y[0]+55,y[1]+55)] == True:
                        minasC += 1
                if (y[0],y[1]+55) in self.minas_d:
                    if self.minas_d[(y[0],y[1]+55)] == True:
                        minasC += 1
                if (y[0]-55,y[1]+55) in self.minas_d:
                    if self.minas_d[(y[0]-55,y[1]+55)] == True:
                        minasC += 1
                if (y[0]-55,y[1]) in self.minas_d:
                    if self.minas_d[(y[0]-55,y[1])] == True:
                        minasC += 1
                if (y[0]-55,y[1]-55) in self.minas_d:
                    if self.minas_d[(y[0]-55,y[1]-55)] == True:
                        minasC += 1
                if (y[0],y[1]-55) in self.minas_d:
                    if self.minas_d[(y[0],y[1]-55)] == True:
                        minasC += 1 
                if (y[0]+55,y[1]-55) in self.minas_d:
                    if self.minas_d[(y[0]+55,y[1]-55)] == True:
                        minasC += 1 
                self.minasA_dt[i] = self.minasA_dt.get(i, minasC)
            counter += 1

   
    #Metodo que destapa una casilla del mapa
    def uncover(self, i):
        val = self.minasA_dt.get(i)
        pos = [i[0] + 10, i[1] - 5]
        self.coord[i] = (96,96,96)
        self.MostrarCuadricula()
        if str(val) == "1":
            val = self.fuente.render(str(val), 1, (0,128,255))
            self.ventana.blit(val, pos)
        if val == 2:
            val = self.fuente.render(str(val), 1, (0,204,0))
            self.ventana.blit(val, pos)
        if val == 3:
            val = self.fuente.render(str(val), 1, (255,0,0))
            self.ventana.blit(val, pos)
        if val == 4:
            val = self.fuente.render(str(val), 1, (0,0,204))
            self.ventana.blit(val, pos)
        if val == 5:
            val = self.fuente.render(str(val), 1, (102,51,0))
            self.ventana.blit(val, pos)
        if val == 6:
            val = self.fuente.render(str(val), 1, (0,255,255))
            self.ventana.blit(val, pos)
        if val == 7:
            val = self.fuente.render(str(val), 1, (51,0,0))
            self.ventana.blit(val, pos)
        if val == 8:
            val = self.fuente.render(str(val), 1, (64,64,64))
            self.ventana.blit(val, pos)
        if val == 9:
            val = self.fuente.render(str(val), 1, (0,0,0))
            self.ventana.blit(val, pos)
        if i in self.cuadricula:
            self.cuadricula.remove(i)
        
    #Metodo que coloca banderas en el mapa
    def PonerOQuitarBandera(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                self.estado[i] = self.estado.get(i, False)
                pos = [i[0], i[1]]
                if self.estado[i] == False:
                    if self.banderas_restantes != 0:
                        self.cuadricula.remove(i)
                        self.ventana.blit(self.bandera, pos)
                        self.banderas_restantes -=1
                        self.estado[i] = True
                        if self.minasA_dt[i] ==  True:
                            self.cont_band +=1
                        break
                else:
                    if self.banderas_restantes < self.banderas_max:
                        self.coord[i] =  self.coord.get(i, (192, 192, 192))
                        self.cuadricula.append(i)
                        self.banderas_restantes +=1
                        self.estado[i] = False
                        if self.minasA_dt[i] == True:
                            self.cont_band -=1
                        break
        
    def ejecucion(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                if self.minas_d[i] == True:
                    pos = [i[0], i[1] + 4]
                    self.ventana.blit(self.mina, pos)
                    self.est= "Pierde"                    
                else:
                    self.uncover(i)
                    if self.minasA_dt[i] == 0:
                        self.minasA_dt[i] = "0"
                        if (i[0]+55, i[1]) in self.minasA_dt:
                            a = self.minasA_dt[(i[0]+55, i[1])]
                            self.uncover((i[0]+55, i[1]))
                            if a == 0:
                                self.ejecucion((i[0]+55, i[1]))
                        if (i[0], i[1]+55) in self.minasA_dt:
                            a = self.minasA_dt[(i[0], i[1]+55)]
                            self.uncover((i[0], i[1]+55))
                            if a == 0:
                                self.ejecucion((i[0], i[1]+55))
                        if (i[0]-55, i[1]) in self.minasA_dt:
                            a = self.minasA_dt[(i[0]-55, i[1])]
                            self.uncover((i[0]-55, i[1]))
                            if a == 0:
                                self.ejecucion((i[0]-55, i[1]))
                        if (i[0], i[1]-55) in self.minasA_dt:
                            a = self.minasA_dt[(i[0], i[1]-55)]
                            self.uncover((i[0], i[1]-55))
                            if a == 0:
                                self.ejecucion((i[0], i[1]-55))
                        if (i[0]+55,i[1]+55) in self.minas_d:
                            a = self.minasA_dt[(i[0]+55,i[1]+55)]
                            self.uncover((i[0]+55,i[1]+55))
                            if a == 0:
                                self.ejecucion((i[0]+55,i[1]+55))
                        if (i[0]-55,i[1]+55) in self.minas_d:
                            a = self.minasA_dt[(i[0]-55,i[1]+55)]
                            self.uncover((i[0]-55,i[1]+55))
                            if a == 0:
                                self.ejecucion((i[0]-55,i[1]+55))
                        if (i[0]+55,i[1]-55) in self.minas_d:
                            a = self.minasA_dt[(i[0]+55,i[1]-55)]
                            self.uncover((i[0]+55,i[1]-55))
                            if a == 0:
                                self.ejecucion((i[0]+55,i[1]-55))
                        if (i[0]-55,i[1]-55) in self.minas_d:
                            a = self.minasA_dt[(i[0]-55,i[1]-55)]
                            self.uncover((i[0]-55,i[1]-55))
                            if a == 0:
                                self.ejecucion((i[0]-55,i[1]-55))
                break
    
    #Metodo que muestra el tiempo que lleva el usuario
    def ImpTiempo(self, t1):
            pos = (juego.centro[0] - 650, juego.centro [1] - juego.size * 5)
            t2 = time.perf_counter()
            t = str(int(t2-t1))
            t = juego.fuente.render(t, 1, (255,255,0))        
            pygame.draw.rect(self.ventana, (0,0,0), (pos[0], pos[1], self.width * 2, self.width))
            self.ventana.blit(t, (pos))
            
    #Metodo que muestra la solucion si el jugador pierde
    def MostrarRespuesta(self):
        for i in self.minas_d:
            if self.minas_d[i] == True:
                pos = [i[0], i[1] + 4]
                self.ventana.blit(self.mina, pos)
            
            
            
            
#BOE
pygame.init()


m = 0
juego = Juego()
t1 = time.perf_counter()
clock = pygame.time.Clock()

run = True
while run:    
    clock.tick(60)
    
    juego.MostrarCuadricula()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
        pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN  and juego.est != "Pierde":
        pos = event.dict['pos']
        if event.button == 1:
            if m == 0:
                juego.safe(pos)
                m = 1
            juego.ejecucion(pos)
        if event.button == 3:
            juego.PonerOQuitarBandera(pos)

    if juego.est == "Pierde":
        msg = juego.fuente.render("Pierde", 1, (255,255,0))
        juego.ventana.blit(msg, (juego.centro[0] - 80, juego.centro[1] - 430))
        juego.MostrarRespuesta()
        t2 = time.perf_counter()
        pygame.display.update()
 

        
    elif juego.cont_band == juego.banderas_max:
        msg = juego.fuente.render("Victoria", 1, (255,255,0))
        juego.ventana.blit(msg, (juego.centro[0] - 110, juego.centro[1] - 430))
        t2 = time.perf_counter()
        pygame.display.update()

    else:
        juego.ImpTiempo(t1)

        pygame.display.update()



##EOE
