import os
import time



if os.path.exists("Tablero.txt") == True:
    os.remove("Tablero.txt")

def crear_tablero():
    with open("Tablero.txt","a") as f:
        for i in range(9):
            for j in range(9):
                if j==8:
                    f.write("0"+"\n")
                else:
                    f.write("0")

def mostrar_tablero():
    with open("Tablero.txt", "r") as f:
        print(f.read(),end="")
        
def verificar_validez(y,jugador):
    y=y-1
    ult_espacio=0
    if not y<=0 or y>=10:
        with open("Tablero.txt", "r") as f:
            for i, line in enumerate(f):
                if (line[y]=="1" or line[y]=="2") and i==0:
                    return False
                elif line[y]=="1" or line[y]=="2":
                    ult_espacio=ult_espacio
                    break
                else:
                    ult_espacio+=1
        return nueva_ficha(y,ult_espacio,jugador)
    else:
        print("Columna fuera de rango")
        return False

    


def nueva_ficha(columna,fila,jugador):
    with open("Tablero.txt", "r+") as f:
        f.seek(11*fila - 11+columna)
        if jugador==1:
            f.write("1")
            return True
        else:
            f.write("2")
            return True

def verificar_victoria(y,jugador):
    if verificar_fila(y,jugador)==True or verificar_columna(y,jugador)==True or verificar_diagonal(y,jugador)==True:
        return True
    else:
        return False
        
def verificar_fila(y,jugador):
    cont=0
    if jugador==1:
        jugador="1"
    else:
        jugador="2"
    with open("Tablero.txt","r") as f:
        for line in f:
            if line[y-1]==jugador:
                for i in range(6):
                    if line[i]==jugador and line[i+1]==jugador and line[i+2]==jugador and line[i+3]==jugador:
                        return True
    return False

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
                    return True
            else:
                cont==0
    return False

# def verificar_diagonal(y,jugador):
#     if jugador==1:
#         jugador="1"
#     else:
#         jugador="2"
#     lista=[]
#     x=0
#     with open("Tablero.txt","r") as f:
#         for i,line in enumerate(f):
#             lista.append(line)
#             if line[y-1]==jugador:
#                 if x!=0:
#                     x=i
#     try:
#         if lista[x+1][y]==jugador:    #+1 +1
#             print("no")
#     except Exception:
#         print("hola")    
#     try:
#         if lista[x]
        
#     return False



crear_tablero()

jugador=1
while True:
    mostrar_tablero()
    y=int(input(f"realice su jugada, jugador {jugador}: "))
    if verificar_validez(y,jugador)==True:
        if jugador==1:
            if verificar_victoria(y,jugador)==True:
                #marcar_victoria(y,jugador)
                mostrar_tablero()
                print("Jugador 1 ha ganado!")
                break
            jugador=2
        else:
            if verificar_victoria(y,jugador)==True:
                #marcar_victoria(y,jugador)
                mostrar_tablero()
                print("Jugador 2 ha ganado!")
                break
            jugador=1