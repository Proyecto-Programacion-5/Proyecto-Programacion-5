import pygame
import time
import Main_class as MC

#----------------------------- Bloque de ejecucion -------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.init()
m = 0                                                                                                               #Variable que regula el metodo safe
juego = MC.Juego(700,600)                                                                                           #Inicializa el juego
t1 = time.perf_counter()                                                                                            #Obtiene el momento en que se inicio el juego
juega = True                                                                                                        #Permite leer o no las acciones sobre el mapa
pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (juego.size/2) - 40)                      #Posicion de los mensajes arriba de la cuadricula
pos_abajo = (juego.centro[0], juego.centro[1] + (juego.width + 5) * (juego.size/2) + 15)                            #Posicion de los mensajes abajo de la cuadricula

run = True                                                                                                          #Regula el ciclo
#----------------------------- Mainloop ------------------------------------------------------------------------------------------------------------------------------------------------------------------
while run:    

    juego.MostrarCuadricula()                                                                   
    event = pygame.event.poll()                                                                                     #Lee los eventos
    if event.type == pygame.QUIT:   
        run = False                                                                                                 #Termina el ciclo
    if event.type == pygame.MOUSEBUTTONDOWN and juega:  
        pos = event.dict['pos']                                                                                     #Lee la posicion del mouse
        if event.button == 1:   
            if m == 0:  
                m = juego.safe(pos)                                                                                 #Ejecuta el metodo safe, si se ejecuta adecuadamente retorna 1 y no se vuelve a hacer
            juego.ejecucion(pos)
        if event.button == 3:
            juego.PonerOQuitarBandera(pos)

    msg_banderas = juego.temp.render("Banderas: {0}".format(juego.banderas_restantes), 1, (255,255,0))              #Mensaje de las banderas restantes
    pygame.draw.rect(juego.ventana, (0,0,0), (pos_abajo[0] + 100, pos_abajo[1], juego.width * 20, 30))              #Fondo del mensaje
    juego.ventana.blit(msg_banderas, (pos_abajo[0] + 100,pos_abajo[1]))                                             #Imprime el mensaje
    
    if juego.cont_band == juego.banderas_max:                                                                       #Si todas las banderas estan bien colodadas
        msg = juego.msg.render("Victoria", 1, (255,255,0))                                                          #Mensaje de victoria
        pygame.draw.rect(juego.ventana, (0,0,0), (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))               #Imprime el fondo del mensaje
        juego.ventana.blit(msg, pos_arriba)                                                                         #Imprime el mensaje
        pygame.display.update()                                                                                     #Actualiza por ultima vez
        juega = False                                                                                               #Hace que deje de leer clicks en la cuadricula
        
    elif not juego.est:                                                                                             #Si clickeo una mina
        msg = juego.msg.render("Perdiste", 1, (255,255,0))                                                          #Mensaje de derrota
        pygame.draw.rect(juego.ventana, (0,0,0), (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))              #Imprime el fondo del mensaje
        juego.ventana.blit(msg, pos_arriba)                                                                         #Imprime el mensaje
        juego.MostrarRespuesta()
        pygame.display.update()                                                                                     #Actualiza por ultima vez
        juega = False                                                                                               #Hace que deje de leer clicks en la cuadricula

    else:
        juego.ImpTiempo(t1)
        pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.quit()
#------------------------------ Fin de la ejecucion ------------------------------------------------------------------------------------------------------------------------------------------------------
