import random
import time
import pygame

class Juego:
    
#-------------------- Inicializador de la clase. Crea la cuadricula, las minas y los valores de cada cuadro -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, ancho, alto):
        
    #-------------------- Tamaño de cuadricula entre 4 y 20 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.size = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 3 y menor que 21:"))
        while self.size < 4 or self.size > 20:
            print("La cuadricula debe ser mayor que 4 y menor que 20\n")
            self.size = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 4:"))
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        self.width = 400//self.size                                                 #Ancho de la cuadricula
        
    #---------------------- Atributos propios de pygame ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.fuente = pygame.font.SysFont('newyorkitalicttf', self.width, True)     #Numeros
        self.temp = pygame.font.SysFont('newyorkitalicttf', 20, True)               #Tiempo
        self.msg = pygame.font.SysFont('newyorkitalicttf', 30, True)                #Mensaje de victoria y derrota
        self.p_ancho = ancho
        self.p_alto = alto
        self.ventana = pygame.display.set_mode((self.p_ancho, self.p_alto))         #Ventana y dimensiones
        pygame.display.set_caption("Buscaminas")    
        self.centro = self.ventana.get_rect().center                                #Centro de la ventana
        mina = pygame.image.load("Mina .png")               
        self.mina = pygame.transform.scale(mina, (self.width , self.width))         #Imagen de la mina
        bandera = pygame.image.load("Bandera.png")
        self.bandera = pygame.transform.scale(bandera, (self.width, self.width))    #Imagen de la bandera
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    #------------------- Atributos propios del buscaminas -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.coord = {}                                                             #Diccionario con coordenadas y color del cuadro
        self.cont_band = 0                                                          #Contador de banderas bien colocadas
        self.banderas_restantes = 0                                                 #Banderas que tiene el jugador
        self.banderas_max = 0                                                       #Banderas maximas que puede tener el jugador
        self.estado = {}                                                            #Diccionario con coordenadas y valores booleanos que indican la presencia de banderas
        self.est = True                                                             #Indica con un booleano si se esta en juego o no                                                               
        self.cuadricula = []                                                        #Lista de coordenadas del tablero
        self.HacerCuadricula()                                                      
        self.minas_d = {}                                                           #Diccionario que indica si hay minas o no en una coorenada
        self.ColocarMinas()                                                         
        self.minasA_dt = {}                                                         #Diccionario con el valor del nimero de minas aledañas a un cuadro
        self.ContarCuadros()                                                        
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------- Metodo que llena la cuadricula y el diccionario de coordenadas ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
#--------------------- Metodo que imprime el mapa en pantalla ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def MostrarCuadricula(self):
        for i in self.cuadricula:
            color = self.coord.get(i)
            x = i[0]
            y = i[1]
            pygame.draw.polygon(self.ventana, (224, 224, 224), [(x + self.width, y),(x + self.width + 2.5, y - 2.5),  (x - 2.5, y - 2.5), (x - 2.5, y + self.width + 2.5), (x, y + self.width), (x, y)])                                                        #Borde superior e izquierdo de cada cuadro
            pygame.draw.polygon(self.ventana, (96, 96, 96), [(x, y + self.width), (x - 2.5, y + self.width + 2.5), (x + self.width + 2.5, y + self.width + 2.5), (x + self.width + 2.5, y - 2.5), (x + self.width, y), (x + self.width, y + self.width)])       #Borde inferior y derecho de cada cuadro
            pygame.draw.rect(self.ventana, (color), (x, y, self.width, self.width))                                                                                                                                                                             #Cuadros
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
#---------------------- Metodo que asigna minas a una parte de las coordenadas de la cuadricula -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def ColocarMinas(self):
        self.minas_d = {}                                                               #Vacia el diccionario para reasignar en la primera jugada
        self.banderas_restantes = 0                                                     #Reinicia el numero de banderas restantes
        self.banderas_max = 0                                                           #Reinicia el numero de banderas maximas
        for i in self.cuadricula:
            self.minas_d[i] = self.minas_d.get(i, False)                                #False indica que no hay mina
        rng = random.Random()
        while self.banderas_restantes < len(self.minas_d) // 5:
            M = rng.randrange(0, len(self.cuadricula))                                  
            if self.minas_d.get(self.cuadricula[M]) == False:
                self.minas_d[self.cuadricula[M]] = True                                 #True indica que hay una mina en la posicion M
                self.banderas_restantes +=1                                             #Cada que asigna una mina aumenta en 1 el numero de banderas restantes
                self.banderas_max +=1                                                   #Cada que asigna una mina aumenta en 1 el numero de banderas maximas
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------- Metodo que mezcla las minas para que el jugador no pierda en el primer turno -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def safe(self, pos):
        print(pos)
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                print(i)
                while self.minasA_dt[i] != 0:
                    self.ColocarMinas()
                    self.ContarCuadros()
                return 1
        return 0
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
   
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
                if (y[0] + self.width + 5 ,y[1]) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5 ,y[1])] == True:
                        minasC += 1
                if (y[0] + self.width + 5 ,y[1] + self.width + 5 ) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5 ,y[1] + self.width + 5 )] == True:
                        minasC += 1
                if (y[0],y[1] + self.width + 5 ) in self.minas_d:
                    if self.minas_d[(y[0],y[1] + self.width + 5 )] == True:
                        minasC += 1
                if (y[0] - self.width - 5 ,y[1] + self.width + 5 ) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5 ,y[1] + self.width + 5 )] == True:
                        minasC += 1
                if (y[0] - self.width - 5 ,y[1]) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5 ,y[1])] == True:
                        minasC += 1
                if (y[0] - self.width - 5 ,y[1] - self.width - 5 ) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5 ,y[1] - self.width - 5 )] == True:
                        minasC += 1
                if (y[0],y[1] - self.width - 5 ) in self.minas_d:
                    if self.minas_d[(y[0],y[1] - self.width - 5 )] == True:
                        minasC += 1 
                if (y[0] + self.width + 5 ,y[1] - self.width - 5 ) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5 ,y[1] - self.width - 5 )] == True:
                        minasC += 1 
                self.minasA_dt[i] = self.minasA_dt.get(i, minasC)
            counter += 1


   
    #Metodo que destapa una casilla del mapa
    def uncover(self, i):
        val = self.minasA_dt.get(i)
        pos = [i[0] + (self.width // 5), i[1]]
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
            
        #Este esta mal nmms
        if val == 9:
            val = self.fuente.render(str(val), 1, (0,0,0))
            self.ventana.blit(val, pos)
        #hasta aqui
        
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
                    pos = [i[0], i[1] - 5]
                    self.ventana.blit(self.mina, pos)
                    self.est = False                    
                else:
                    self.uncover(i)
                    if self.minasA_dt[i] == 0:
                        self.minasA_dt[i] = "0"
                        if (i[0] + self.width + 5 , i[1]) in self.minasA_dt:
                            a = self.minasA_dt[(i[0] + self.width + 5 , i[1])]
                            self.uncover((i[0] + self.width + 5 , i[1]))
                            if a == 0:
                                self.ejecucion((i[0] + self.width + 5 , i[1]))
                        if (i[0], i[1] + self.width + 5 ) in self.minasA_dt:
                            a = self.minasA_dt[(i[0], i[1] + self.width + 5 )]
                            self.uncover((i[0], i[1] + self.width + 5 ))
                            if a == 0:
                                self.ejecucion((i[0], i[1] + self.width + 5 ))
                        if (i[0] - self.width - 5 , i[1]) in self.minasA_dt:
                            a = self.minasA_dt[(i[0] - self.width - 5 , i[1])]
                            self.uncover((i[0] - self.width - 5 , i[1]))
                            if a == 0:
                                self.ejecucion((i[0] - self.width - 5 , i[1]))
                        if (i[0], i[1] - self.width - 5 ) in self.minasA_dt:
                            a = self.minasA_dt[(i[0], i[1] - self.width - 5 )]
                            self.uncover((i[0], i[1] - self.width - 5 ))
                            if a == 0:
                                self.ejecucion((i[0], i[1] - self.width - 5 ))
                        if (i[0] + self.width + 5 ,i[1] + self.width + 5 ) in self.minas_d:
                            a = self.minasA_dt[(i[0] + self.width + 5 ,i[1] + self.width + 5 )]
                            self.uncover((i[0] + self.width + 5 ,i[1] + self.width + 5 ))
                            if a == 0:
                                self.ejecucion((i[0] + self.width + 5 ,i[1] + self.width + 5 ))
                        if (i[0] - self.width - 5 ,i[1] + self.width + 5 ) in self.minas_d:
                            a = self.minasA_dt[(i[0] - self.width - 5 ,i[1] + self.width + 5 )]
                            self.uncover((i[0] - self.width - 5 ,i[1] + self.width + 5 ))
                            if a == 0:
                                self.ejecucion((i[0] - self.width - 5 ,i[1] + self.width + 5 ))
                        if (i[0] + self.width + 5 ,i[1] - self.width - 5 ) in self.minas_d:
                            a = self.minasA_dt[(i[0] + self.width + 5 ,i[1] - self.width - 5 )]
                            self.uncover((i[0] + self.width + 5 ,i[1] - self.width - 5 ))
                            if a == 0:
                                self.ejecucion((i[0] + self.width + 5 ,i[1] - self.width - 5 ))
                        if (i[0] - self.width - 5 ,i[1] - self.width - 5 ) in self.minas_d:
                            a = self.minasA_dt[(i[0] - self.width - 5 ,i[1] - self.width - 5 )]
                            self.uncover((i[0] - self.width - 5 ,i[1] - self.width - 5 ))
                            if a == 0:
                                self.ejecucion((i[0] - self.width - 5 ,i[1] - self.width - 5 ))
                break

    
    #Metodo que muestra el tiempo que lleva el usuario
    def ImpTiempo(self, t1):
        pos = (self.centro[0] - 100, self.centro[1] + (self.width + 5) * (self.size/2) + 15)
        t2 = time.perf_counter()
        t = str(int(t2-t1))
        t = self.temp.render("Tiempo : {0} sec".format(t), 1, (255,255,0))        
        pygame.draw.rect(self.ventana, (0,0,0), (pos[0], pos[1], self.width * 20, self.width))
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
juego = Juego(700,600)
t1 = time.perf_counter()
clock = pygame.time.Clock()
juega = True

run = True
while run:    
    clock.tick(60)
    
    juego.MostrarCuadricula()
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    if event.type == pygame.MOUSEBUTTONDOWN and juega:
        pos = event.dict['pos']
        if event.button == 1:
            if m == 0:
                m = juego.safe(pos)
            juego.ejecucion(pos)
        if event.button == 3:
            juego.PonerOQuitarBandera(pos)


    if juego.cont_band == juego.banderas_max:
        msg = juego.msg.render("Victoria", 1, (255,255,0))
        pos = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (juego.size/2) - 40)
        pygame.draw.rect(juego.ventana, (0,0,0), (pos[0], pos[1], juego.width * 20, 30))
        juego.ventana.blit(msg, (pos[0], pos[1]))
        t2 = time.perf_counter()
        pygame.display.update()
        juega = False
        
    elif not juego.est:
        msg = juego.msg.render("Pierde", 1, (255,255,0))
        pos = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (juego.size/2) - 40)
        pygame.draw.rect(juego.ventana, (0,0,0), (pos[0], pos[1], juego.width * 20, 30))
        juego.ventana.blit(msg, (pos[0], pos[1]))
        juego.MostrarRespuesta()
        t2 = time.perf_counter()
        pygame.display.update()
        juega = False

    else:
        juego.ImpTiempo(t1)

        pygame.display.update()

pygame.quit()

##EOE
