import os

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
    if not y<=0:
        with open("Tablero.txt", "r") as f:
            for i, line in enumerate(f):
                if (line[y]=="1" or line[y]=="2") and i==0:
                    return False
                elif line[y]=="1" or line[y]=="2":
                    ult_espacio=ult_espacio
                    break
                else:
                    ult_espacio+=1
        nueva_ficha(y,ult_espacio,jugador)
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




crear_tablero()

jugador=1
while True:
    mostrar_tablero()
    y=int(input(f"realice su jugada, jugador {jugador}"))
    if verificar_validez(y,jugador)==True:
        if jugador==1:
            jugador=2
        else:
            jugador=1