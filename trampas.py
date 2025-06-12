def bomb(y):
    with open("Tablero.txt","r+") as f:
        y=y-1
        borrado=[]
        for i, line in enumerate(f):
            if line[y]=="1" or line[y]=="2":
                x=i-2
                break
        for i in range(-1,2):
            f.seek(11*(x-1) - i+11+y)
            print(11*(x-1) - i+11+y)
            f.write("0")
            f.seek(11*x - i+11+y)
            print(11*x - i+11+y)
            f.write("0")
            f.seek(11*(x+1) - i+11+y)
            f.seek(0)
            borrado.append(f.readline(11*(x+1) - i+11+y))
            f.write("0")
            
    revision_flotante(y,borrado)

def revision_flotante(y,borrado):
    with open("Tablero.txt","r+"):
        print("FALTA REALIZAR EL CODIGO")

def fila_extra():
    with open("Tablero.txt","a") as f:
        if len(f)==8:
            f.write("000000000"+"\n")
        else:
            print("No se puede crear una segunda fila extra.")

def rehacer(ult_y,accion):
    if accion==-1:
        print("No puedes usarlo en el primer turno...")
    elif accion==1:
        print("Se han retrocedido 2 turnos...")

fila_extra()