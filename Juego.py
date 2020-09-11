import pygame as pg
import numpy as np
import time
import random

##PANTALLA
pg.init()
size = (800, 600)
screen = pg.display.set_mode(size)
bg = (200, 200, 200)
screen.fill(bg)
pg.display.flip()
myFont = pg.font.SysFont("areial black", 48)
fontObj =  pg.font.SysFont("areial black", 58)

##MATRIZ
numCx, numCy = 30, 30
dimX = 600 // numCx
dimY = size[1] // numCy
nivel = ['nivel1.out', 'nivel2.out', 'nivel3.out']
numNivel = 0
matriz = np.loadtxt(nivel[numNivel])
metaNivel = [(16, 29),(14,29), (15,29)]
playerx, playery = 14, 0
avatarx, avatary = 29, 0
ava2x, ava2y = 15, 0
matriz[playerx, playery] = 4
matriz[playerx, playery+1] = 1
move = 10
#avatarx, avatary = 29, 0

#BUCLE EN EJECUCION
pg.display.flip()
game_over = False
edit = False
opcion = 0
cambio = 20
flag = True
while not game_over:
    pos = [(playerx, playery), (avatarx, avatary)]
    ##JUGADOR AL AZAR
    flag = True
    if cambio > 0 and numNivel > 1:
        pos.append((ava2x, ava2y))
        random.shuffle(pos)
        playerx, playery = pos[0][0], pos[0][1]
        avatarx, avatary = pos[1][0], pos[1][1]
        ava2x, ava2y = pos[2][0], pos[2][1]
        matriz[pos[0]] = 4
        matriz[pos[1]] = 7
        matriz[pos[2]] = 7
        cambio-=1
    elif cambio > 0 and numNivel >= 1:
        random.shuffle(pos)
        playerx, playery = pos[0][0], pos[0][1]
        avatarx, avatary = pos[1][0], pos[1][1]
        matriz[pos[0]] = 4
        matriz[pos[1]] = 7
        cambio-=1
    ##TERMINA JUGADOR AL AZAR
    time.sleep(0.02)
    screen.fill((150,200,200))
    
    if move < 0:
        print("PERDISTE :(")
        game_over = True
    ##GRAVEDAD
    try:
        ###GRAVEDAD JUGADOR
        if matriz[playerx,playery+1] == 0:
            matriz[playerx, playery] = 0
            playery+=1
            matriz[playerx, playery] = 4

        if matriz[playerx, playery+1] == 3:
            matriz[playerx, playery] = 0
            playerx+=1
            playery+=1
            matriz[playerx,playery] = 4 
         
        if matriz[playerx, playery+1] == 2:
            matriz[playerx, playery] = 0
            playerx-=1
            playery+=1
            matriz[playerx,playery] = 4 
        
        if numNivel > 0:
            try:
                if matriz[avatarx,avatary+1] == 0:
                    matriz[avatarx, avatary] = 0
                    avatary+=1
                    matriz[avatarx, avatary] = 7
            except:
                matriz[avatarx, avatary] = 0
                avatarx, avatary = 0, 0
                print("Avatar no se mueve")
            
            if matriz[avatarx,avatary+1] == 2:
                matriz[avatarx, avatary] = 0
                avatarx-=1
                avatary+=1
                matriz[avatarx, avatary] = 7

            if matriz[avatarx,avatary+1] == 3:
                matriz[avatarx, avatary] = 0
                avatarx+=1
                avatary+=1
                matriz[avatarx, avatary] = 7
        if numNivel > 1:
            try:
                if matriz[ava2x,ava2y+1] == 0:
                    matriz[ava2x, ava2y] = 0
                    ava2y+=1
                    matriz[ava2x, ava2y] = 7
            except:
                matriz[ava2x, ava2y] = 0
                ava2x, ava2y = 0, 0
                print("Avatar no se mueve")
            
            if matriz[ava2x,ava2y+1] == 2:
                matriz[ava2x, ava2y] = 0
                ava2x-=1
                ava2y+=1
                matriz[ava2x, ava2y] = 7

            if matriz[ava2x,ava2y+1] == 3:
                matriz[ava2x, ava2y] = 0
                ava2x+=1
                ava2y+=1
                matriz[ava2x, ava2y] = 7
    except:
        if matriz[metaNivel[numNivel]]== 4:
            matriz[playerx, playery] = 0
            numNivel+=1
            try:
                matriz = np.loadtxt(nivel[numNivel])
            except:
                print("GANASTE!!!")
                game_over=True
            if numNivel==1:
                playerx, playery = 0, 0
                matriz[playerx, playery] = 4
                avatarx, avatary = 29, 0
                matriz[avatarx, avatary] = 7
            if numNivel==2:
                playerx, playery = 0, 0
                matriz[playerx, playery] = 4
                avatarx, avatary = 29, 0
                matriz[avatarx, avatary] = 7
                ava2x, ava2y = 15, 0
                matriz[ava2x, ava2y] = 7
            move = 10
    ##TERMINA GRAVEDAD

    #BOTONES
    ## BOTONES PARA EDITAR
    press = False
    if opcion == 'e':
        print("Modo edicion")
        edit= True
        matriz[playerx, playery] = 0
        bg = (100, 200, 150)
        opcion = "null"
    elif opcion == 'r':
        print("cerrado modo edicion")
        matriz[playerx,playery]=4
        move = 10
        edit = False
        bg = (200, 200, 200)
        opcion = "null"
    if opcion == '1':
        print("Piso")
    if opcion == '2':
        print("deslizar izq")
    if opcion == '3':
        print("Deslizar derecha")
    if opcion == '5':
        print("Corazon")
    if opcion == '6':
        print("nube")
    if opcion== '0':
        print("Borrar")
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            opcion = event.unicode

            ##MOVIMIENTO JUGADOR
            key = pg.key.name(event.key)
            if matriz[playerx, playery+1] == 1 and not edit:
                if move%2==0:
                    cambio = 20
                if key == 'right' and playerx+1 < numCx:
                    if flag:
                        move-=1
                        flag =False

                    if matriz[playerx+1, playery]== 0 or matriz[playerx+1, playery] == 5 or matriz[playerx+1, playery]== 6:
                        matriz[playerx, playery] = 0
                        playerx+=1
                    
                        if matriz[playerx, playery]==5:
                            move+=1
                    
                        if matriz[playerx, playery]==6:
                            move+=3

                        matriz[playerx, playery] = 4
                
                if key == 'left' and playerx > 0:
                    if flag:
                        move-=1
                        flag = False
                    if matriz[playerx-1, playery]== 0 or matriz[playerx-1, playery] == 5 or matriz[playerx-1, playery] == 6:
                        matriz[playerx, playery] = 0
                        playerx-=1

                        if matriz[playerx, playery]==5:
                            move+=1
                    
                        if matriz[playerx, playery]==6:
                            move+=3
                        
                        matriz[playerx, playery] = 4
                    
            ##TERMINA MOVIMIENTO DE JUGADOR
            ##MOVIMIENTO AVATAR
            if numNivel > 0 and avatary < 29:
                if matriz[avatarx, avatary+1] == 1 and not edit:
                        if key == 'right' and avatarx+1 < numCx:
                            if flag:
                                move-=1
                                flag = False
                            if matriz[avatarx+1, avatary]== 0 or matriz[avatarx+1, avatary] == 5 or matriz[avatarx+1, avatary] == 6:
                                matriz[avatarx, avatary] = 0
                                avatarx+=1

                                if matriz[avatarx, avatary]==5:
                                    move+=1
                            
                                if matriz[avatarx, avatary]==6:
                                    move+=3

                                matriz[avatarx, avatary] = 7

                        if key == 'left' and avatarx > 0:
                            if flag: 
                                move-=1
                                flag = False
                            if matriz[avatarx-1, avatary]==0 or matriz[avatarx-1, avatary] == 5 or matriz[avatarx-1, avatary] == 6:
                                matriz[avatarx, avatary] = 0
                                avatarx-=1
                                    
                                if matriz[avatarx, avatary]==5:
                                    move+=1
                            
                                if matriz[avatarx, avatary]==6:
                                    move+=3
                                matriz[avatarx, avatary] = 7
            
            if numNivel > 1 and ava2y < 29:
                if matriz[ava2x, ava2y+1] == 1 and not edit:
                        if key == 'right' and ava2x+1 < numCx:
                            if flag:
                                move-=1
                                flag = False
                            if matriz[ava2x+1, ava2y]==0 or matriz[ava2x-1, ava2y] == 5 or matriz[ava2x-1, ava2y] == 6:
                                matriz[ava2x, ava2y] = 0
                                ava2x+=1

                                if matriz[ava2x, ava2y]==5:
                                    move+=1
                            
                                if matriz[ava2x, ava2y]==6:
                                    move+=3

                                matriz[ava2x, ava2y] = 7

                        if key == 'left' and ava2x > 0:
                            if flag: 
                                move-=1
                                flag = False
                            if matriz[ava2x-1, ava2y]==0 or matriz[ava2x-1, ava2y] == 5 or matriz[ava2x-1, ava2y] == 6:
                                    matriz[ava2x, ava2y] = 0
                                    ava2x-=1
                                    matriz[ava2x, ava2y] = 7
            ##TERMINA OVIMIENTO AVATAR

        if event.type == pg.MOUSEBUTTONDOWN and edit:
            if event.button == 1:
                press = True
        if event.type == pg.QUIT:       
            game_over = True
    if press:
        pos = pg.mouse.get_pos()
        press_celda = (pos[0]//dimX, pos[1]//dimY);
        try:
            matriz[press_celda] = int(opcion)
        except: 
            print("Error")
        matriz[playerx, playery] = 0
        np.savetxt(nivel[numNivel], matriz, fmt = "%f")
        press = False
    ##TERMINA BOTONES PARA EDITAR
    
    #DIBUJAR
    for y in range (0, numCy):
        for x in range (0, numCx):
            celda = [
                (x*dimX, y*dimY),
                ((x+1)*dimX, y*dimY),
                ((x+1)*dimX, (y+1)*dimY),
                (x*dimX, (y+1)*dimY)
            ]
            diaIz = [
                (x*dimX, (y+1)*dimY),
                ((x+1)*dimX, y*dimY),
                ((x+1)*dimX, (y+1)*dimY),
            ]
            diaDe = [
                (x*dimX, y*dimY),
                (x*dimX, (y+1)*dimY),
                ((x+1)*dimX, (y+1)*dimY),
            ]
            circle = ((x*dimX)+ dimX//2, (y*dimY)+ dimY//2)

            nube = (x*dimX+1,y*dimY+5,20,8)

            diagCircle = ((x*dimX), (y*dimY))
            
            if matriz[x, y] == 0:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
            if matriz[x, y] == 1:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.polygon(screen, (0,0,0), celda, 0)
            if matriz[x, y] == 2:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.polygon(screen, (0,0,0), diaIz, 0)
            if matriz[x, y] == 3:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.polygon(screen, (0,0,0), diaDe, 0)
            if matriz[x, y] == 4:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.circle(screen, (0,0,250), circle, 10, 0)
            if matriz[x, y] == 5:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.circle(screen, (255,0,0), circle, 8, 0)
            if matriz[x, y] == 6:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.ellipse(screen, (250,250, 100), nube, 0)
            if matriz[x, y] == 7:
                pg.draw.polygon(screen, bg, celda, 0)
                pg.draw.polygon(screen, (0,0,0), celda, 1)
                pg.draw.circle(screen, (0,0,250), circle, 10, 1)
    
    ##MENSAJES E INSTRUCCIONES
    numMove = myFont.render(str(move), 1, (50, 80, 80))
    moves = myFont.render("Moves: ", 1, (50, 80, 80))
    screen.blit(moves, (620, 100))
    screen.blit(numMove, (745, 100))
    
    pg.display.flip()