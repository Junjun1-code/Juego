import os
import time
from itertools import product


if os.path.exists("Tablero.txt") == True:
    os.remove("Tablero.txt")

def crear_tablero():
    with open("Tablero.txt","a") as f:
        for i in range(8):
            for j in range(9):
                if j==8:
                    f.write("0"+"\n")
                else:
                    f.write("0")

def mostrar_tablero():
    with open("Tablero.txt", "r") as f:
        print(f.read(),end="")
        
def verificar_validez_jugada(y,jugador):
    y=y-1
    ult_espacio=0
    if y>-1 and y<9:
        with open("Tablero.txt", "r") as f:
            for i, line in enumerate(f):
                if (line[y]=="1" or line[y]=="2") and i==0:
                    print("Esta columna esta llena")
                    time.sleep(1.5)
                    return False
                elif line[y]=="1" or line[y]=="2":
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
        f.seek(11*fila - 11+columna)
        if jugador==1:
            f.write("1")
            global y_ult
            y_ult=columna
            global accion
            accion=1
            return True
        else:
            f.write("2")
            return True

        
def verificar_fila(y,jugador):
    if jugador==1:
        jugador="1"
    else:
        jugador="2"
    with open("Tablero.txt","r") as f:
        for line in f:
            if line[y-1]==jugador:
                for i in range(6):
                    if line[i]==jugador and line[i+1]==jugador and line[i+2]==jugador and line[i+3]==jugador:
                        global fila
                        fila=1
                        print("Fila!!")
                        return True
    return False

def verificar_victoria(y,jugador):
    if verificar_fila(y,jugador)==True or verificar_columna(y,jugador)==True or verificar_diagonal(y,jugador)==True:
        return True
    else:
        return False

def fila_victoria(y,jugador):
    y=y-1
    ult_espacio=0
    with open("Tablero.txt", "r") as f:
        for line in f:
            if line[y]=="1" or line[y]=="2":
                break
            else:
                ult_espacio+=1
    marcar_todas(ult_espacio,jugador)

def marcar_todas(x,jugador):
    with open("Tablero.txt","r+") as f:
        if columna==0:
            marcar_columna(jugador)
        if fila==1:
            marcar_fila(x,jugador)
        if diagonal==1:
            marcar_diagonal(y,jugador)

def marcar_fila(x,jugador):
    if jugador==1:
        jugador=["1","3"]
    elif jugador==2:
        jugador=["2","4"]
    with open("Tablero.txt","r+") as f:
        for i,line in enumerate(f):
            if i==x:
                for j in range(6):
                    if line[j] in jugador and line[j+1] in jugador and line[j+2] in jugador and line[j+3] in jugador:
                        f.seek(11*(1+i) - 11+j)
                        f.write("3333")
                        try:    
                            for i in range(4,10):
                                if line[j+i] in jugador:
                                    f.write(jugador[1])
                                else:
                                    return
                        except Exception:
                            return

def verificar_columna(y,jugador):
    cont=0
    if jugador==1:
        jugador="1"
    if jugador==2:
        jugador="2"
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
                return False


def marcar_columna(y,jugador):
    if jugador==1:
        jugador=["1","3"]
        jugadorvs="2"
    else:
        jugador=["2","4"]
        jugadorvs="1"
    with open("Tablero.txt","r+") as f:
        for i,line in enumerate(f):
            if line[y-1] in jugador:
                f.seek(i*11 + 11-y)
                f.write(jugador[1])
            elif line[y-1] == jugadorvs:
                return
    return


# REVISAR!!!!!!!!!!!!

def verificar_diagonal(y,jugador):
    if jugador==1:
        jugador="1"
    else:
        jugador="2"
    lista=[]
    x=0
    with open("Tablero.txt","r") as f:
        for line in f:
            lista.append(line)
        for i in range(9):
            if line[y-1]==jugador:
                x=i
                break

        for i in range(-1,2,2):
            cont=1
            global posiciones
            posiciones=[]
            for j in range(3):
                
            # try:
            #     for j in range(3):        
            #         if lista[x-1*j*i][y-1*j*i]==jugador or lista[x+1*i][y-1*i]==jugador:
            #             print(lista[x(-1*j*i)][y(-1*j*i)], cont)
            #             cont+=1
            #             posiciones.append(x-1*j*i)
            #             posiciones.append(y-1*j*i)
            #             if cont==4:
            #                 break
            #         elif lista[x(-1*j*i)][y(-1*j*i)]!=jugador and lista[x+1*i][y-1*i]==jugador:
            #             print(lista[x(-1*j*i)][y(-1*j*i)], cont)
            #             cont+=1
            #             posiciones.append(x+1)
            #             posiciones.append(y-1)
            #             if cont==4:
            #                 break
            #             elif lista[x-1*j*i][y-1*j*i]!=jugador and lista[x+2*i][y-2*i]==jugador:
            #                 cont+=1
            #                 posiciones.append(x+2)
            #                 posiciones.append(y+2)
            #         else:
            #             cont=1
            #     if cont==4:
            #         global diagonal
            #         diagonal=1
            #         print("Diagonal!!")
            #         return True
            #     else:
            #         return False
            # except Exception:
            #     return False

def marcar_diagonal(jugador):
    if jugador==1:
        jugador=["1","3"]
    else:
        jugador=["2","4"]
    with open("Tablero.txt","r+") as f:
        try:
            for i in range(0,len(posiciones),2):
                f.seek(posiciones[i]*11 + posiciones[i+1]-11)
                f.write(jugador[1])
        except Exception:
            return


def marcar_todas(y,jugador):
    if columna==1:
        marcar_columna(y,jugador)
    if fila==1:
        marcar_fila(y,jugador)
    if diagonal==1:
        marcar_diagonal(jugador)



crear_tablero()
jugador=1
global columna
columna=0
global fila
fila=0
global diagonal
diagonal=0
while True:
    mostrar_tablero()
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