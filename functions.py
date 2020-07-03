import sys

def mostrar(tablero):
    print (tablero[0])
    print (tablero[1])
    print (tablero[2])
    print (tablero[3])
    print (tablero[4])
    print (tablero[5])
    print (tablero[6])
    print (tablero[7])

def validar (pos, mov, tablero, valido=True):
    if pos[0]+mov[0] < 0 or pos[0]+mov[0] > 7:
        valido = False
    if pos[1]+mov[1] < 0 or pos[1]+mov[1] > 7:
        valido = False
    if valido:
        if tablero[pos[0]+mov[0]][pos[1]+mov[1]] > 0:
            valido = False
    return valido

def marcar (tablero, pos, iteracion):
    tablero[pos[0]][pos[1]] = iteracion
    return tablero

def mover (pos, mov):
    pos[0] = pos[0]+mov[0]
    pos[1] = pos[1]+mov[1]
    return pos

def muerto(iteracion, recorrido, tablero):
    mostrar (tablero)
    print ("en un callejon en paso: ", iteracion-1, " del recorrido")
    print ("recorrido: ",recorrido)
    sys.exit() 