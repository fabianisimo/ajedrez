from functions import *
import numpy 
import sys

# tablero [y][x] de 0 a 7

tablero = numpy.zeros((8,8))
pos = [0,0]
iteracion = 1
movimientos = (
    (1,2),
    (2,1),
    (2,-1),
    (1,-2),
    (-1,-2),
    (-2,-1),
    (-2,1),
    (-1,2)
)
recorrido = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# validar (pos, mov, tablero):
        
# marcar (tablero, pos, iteracion):

# mover (pos, mov):

tablero = marcar (tablero, pos, iteracion)

def prueba_camino (tablero, pos, iteracion):
    for a in recorrido:        
        if validar (pos, movimientos[a], tablero):            
            pos = mover (pos, movimientos[a])
            iteracion = iteracion + 1
            tablero = marcar (tablero, pos, iteracion)
            #mostrar (tablero)
            #print ("-----------------------")
        else:
            retrocede = 1
            def corregir(iteracion, retrocede):
                if recorrido[iteracion - retrocede] + 1 >7:
                    retrocede = retrocede + 1
                    corregir(iteracion, retrocede)
                else:
                    recorrido[iteracion - retrocede] = recorrido[iteracion - retrocede] + 1
                    tablero = numpy.zeros((8,8))
                    pos = [0,0]
                    iteracion = 1
                    #print ("recorrido: ",recorrido)
                    prueba_camino(tablero, pos, iteracion)  
            corregir(iteracion, retrocede)
  

print (sys.getrecursionlimit())
#prueba_camino(tablero, pos, iteracion)


