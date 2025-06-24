import os
import time



if os.path.exists("Tablero.txt") == True:
    os.remove("Tablero.txt")

VERTICAL = 9
HORIZONTAL = 8

def crear_tablero():
    with open("Tablero.txt","a") as f:
        for i in range(HORIZONTAL):
            for j in range(VERTICAL):
                if j==8:
                    f.write("0"+"\n")
                else:
                    f.write("0")

def mostrar_tablero():
    with open("Tablero.txt", "r") as f:
        print(f.read(),end="")
        
def verificar_validez_jugada(y,jugador):
    global ult_espacio
    y=y-1
    ult_espacio=0
    if y>-1 and y<9:
        with open("Tablero.txt", "r") as f:
            for i, line in enumerate(f):
                if (line[y]=="X" or line[y]=="O") and i==0:
                    print("Esta columna esta llena")
                    time.sleep(1.5)
                    return False
                elif line[y]=="X" or line[y]=="O":
                    ult_espacio=ult_espacio
                    break
                else:
                    ult_espacio+=1
        return nueva_ficha(y,ult_espacio,jugador)
    else:
        print("Columna fuera de rango")
        time.sleep(1.5)
        return False
    

def nueva_ficha(columna,fila,jugador):
    with open("Tablero.txt", "r+") as f:
        global accion
        global y_ult
        f.seek(11*fila - 11+columna)
        if jugador==1:
            f.write("X")
            y_ult=columna
            accion=1
            # F1.draw(screen)
            # F1.move(columna,fila)
            # py.display.update()
            return True
        else:
            y_ult=columna
            accion=1            
            f.write("O")
            return True

        
def verificar_fila(jugador):
    if jugador==1:
        jugador="X"
    else:
        jugador="O"
    with open("Tablero.txt","r") as f:
        for i,line in enumerate(f):
            if i==ult_espacio-1:
                for i in range(6):
                    if line[i]==jugador and line[i+1]==jugador and line[i+2]==jugador and line[i+3]==jugador:
                        global fila
                        fila=1
                        print("Fila!!")
                        return True                
    return False

def verificar_victoria(y,jugador):
    if verificar_fila(jugador)==True or verificar_columna(y,jugador)==True or verificar_diagonal(jugador)==True:
        return True
    else:
        return False

def fila_victoria(y,jugador):
    y=y-1
    ult_espacio2=0
    with open("Tablero.txt", "r") as f:
        for line in f:
            if line[y]=="1" or line[y]=="2":
                break
            else:
                ult_espacio2+=1
    marcar_todas(ult_espacio2,jugador)

def marcar_todas(jugador):
    with open("Tablero.txt","r+") as f:
        if columna==1:
            marcar_columna(jugador)
        if fila==1:
            marcar_fila(jugador)
        if diagonal==1:
            marcar_diagonal(y,jugador)

def marcar_fila(jugador):
    if jugador==1:
        jugador=["X","1"]
    elif jugador==2:
        jugador=["O","2"]
    with open("Tablero.txt","r+") as f:
        for i,line in enumerate(f):
            if i==ult_espacio-1:
                for j in range(6):
                    if line[j] in jugador and line[j+1] in jugador and line[j+2] in jugador and line[j+3] in jugador:                
                        f.seek(11*ult_espacio + j-11)
                        f.write(jugador[1]+jugador[1]+jugador[1]+jugador[1])

def verificar_columna(y,jugador):
    cont=0
    if jugador==1:
        jugador="X"
    if jugador==2:
        jugador="O"
    with open("Tablero.txt","r") as f:
        for line in f:
            if line[y-1]==jugador:
                cont+=1
                if cont==4:
                    global columna
                    columna=1
                    print("Columna!!")
                    return True
            else:
                cont=0


def marcar_columna(y,jugador):
    if jugador==1:
        jugador=["X","1"]
    else:
        jugador=["O","2"]
    with open("Tablero.txt","r+") as f:
        for i in range(4):
            f.seek(11*ult_espacio + 11*i-1 + y-11)
            f.write(jugador[1])
    return




def verificar_diagonal(jugador):
    if jugador==1:
        jugador="X"
    else:
        jugador="O"    
    global posiciones
    global diagonal
    posiciones = []
    lista=[]
    with open("Tablero.txt","r") as f:
        for line in f:
            lista.append(line)
    # Diagonal descendente ↘ (i+1, j+1)
    for i in range(-HORIZONTAL,5 + -HORIZONTAL):
        for j in range(VERTICAL - 3):
            if lista[i][j] == jugador and \
               lista[i+1][j+1] == jugador and \
               lista[i+2][j+2] == jugador and \
               lista[i+3][j+3] == jugador:
                    posiciones.append([i, j])
                    posiciones.append([i+1, j+1])
                    posiciones.append([i+2, j+2])
                    posiciones.append([i+3, j+3])                                                            
                    print("Diagonal descendiente!!")
                    diagonal=1
                    return True
                
    # Diagonal ascendente ↗ (i-1, j+1)
    for i in range(3, HORIZONTAL):
        for j in range(VERTICAL - 3):
            if lista[i][j] == jugador and \
               lista[i-1][j+1] == jugador and \
               lista[i-2][j+2] == jugador and \
               lista[i-3][j+3] == jugador:
                    print(i)
                    posiciones.append([i, j])
                    posiciones.append([i-1, j+1])
                    posiciones.append([i-2, j+2])
                    posiciones.append([i-3, j+3])                                                            
                    print("diagonal ascendiente!!")
                    diagonal=2
                    return True
    

def marcar_diagonal(jugador):
    if jugador==1:
        jugador=["X","1"]
    else:
        jugador=["O","2"]
    with open("Tablero.txt","r+") as f:
            if diagonal==1:
                for i in range(4):
                    f.seek(((9+posiciones[-i][0])*11) + posiciones[-i][1]-11)              
                    f.write(jugador[1])
            else:
                for i in range(3,-1,-1):
                    f.seek(11*posiciones[i][0] + posiciones[i][1])
                    f.write(jugador[1])

def marcar_todas(y,jugador):
    if columna==1:
        marcar_columna(y,jugador)
    if fila==1:
        marcar_fila(jugador)
    if diagonal==1 or diagonal==2:
        marcar_diagonal(jugador)

# import pygame as py

# py.init()
# ANCHO = 1600
# ALTO = 880
# FPS=20
# FramePerSec = py.time.Clock()
# screen = py.display.set_mode((ANCHO , ALTO))

# class ficha1(py.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = py.image.load("Ficha1.png")
#         self.rect = self.image.get_rect()
#         self.rect.center=(400,120)

#     def draw(self,surface):
#             py.transform.scale(self.image, (80,80))
#             surface.blit(self.image, self.rect)

#     def move(self,posicion,altura):
#             self.rect.move_ip((600 + 88 * posicion), (120+50*altura))



# class ficha3(py.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.rect.center(ficha1.copy())



crear_tablero()
jugador=1
global columna
columna=0
global fila
fila=0
global diagonal
diagonal=0

# F1=ficha1()
while True:
    # for event in py.event.get():
    #     if event.type == py.QUIT:
    #         py.quit()   
    # screen.fill((0,0,20))
    mostrar_tablero()
    try:
        y=int(input(f"realice su jugada, jugador {jugador}: "))
        if verificar_validez_jugada(y,jugador)==True:
            if jugador==1:
                if verificar_victoria(y,jugador)==True:
                    marcar_todas(y,jugador)
                    mostrar_tablero()
                    print("Jugador 1 ha ganado!")
                    break
                jugador=2
            else:
                if verificar_victoria(y,jugador)==True:
                    marcar_todas(y,jugador)
                    mostrar_tablero()
                    print("Jugador 2 ha ganado!")
                    break
                jugador=1
    except Exception:
        print("[X] Ha ingresado una posición invalida para su ficha, vuelva a intentarlo...")
        time.sleep(1.5)









# class ficha2(py.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = py.image.load("Ficha2.png")
#         self.rect = self.image.get_rect()
#         self.rect.center=(300,80)
#    def draw(self,surface):
#       keys=py.key.get_pressed()
#         if keys[py.K_5]:
#            surface.blit(self.image, self.rect) ; py.display.update()
#     def move(self,posicion,altura):
#             self.rect.move_ip((600 + 88 * posicion), 800)
#             if self.rect.bottom>450+50*altura:
#                 self.move(0,15) ; py.display.update()

# F1=ficha1()
# # F2=ficha2()
# Run=True
# while Run:
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             py.quit()           

#     screen.fill((0,0,10))                
#     F1.draw(screen)
#     F1.move(posicion,altura)