from functions import *
import numpy 
import sys
sys.setrecursionlimit(2000)
# tablero [y][x] de 0 a 7

tablero = numpy.zeros((8,8))
pos = [0,1]
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
    pasos = 0
    for a in recorrido:      
        pasos = pasos + 1  
        if pasos == 60:
            print ("PASOS: ",pasos)
            print ("RECORRIDO FINAL: ",recorrido)
            sys.exit() 
        if validar (pos, movimientos[a], tablero):            
            pos = mover (pos, movimientos[a])
            iteracion = iteracion + 1
            tablero = marcar (tablero, pos, iteracion)
            #mostrar (tablero)
        else:
            retrocede = 1
            def corregir(iteracion, retrocede, tablero, pos):
                print ("pasos dados:", pasos)
                print (recorrido)
                if recorrido[iteracion - retrocede] + 1 > 7:
                    retrocede = retrocede + 1
                    if retrocede == 4:
                        muerto(iteracion, recorrido, tablero)
                    else:
                        corregir(iteracion, retrocede, tablero, pos)
                else:
                    recorrido[iteracion - retrocede] = recorrido[iteracion - retrocede] + 1
                    for i in range (iteracion, len(recorrido)):
                        recorrido[i] = 0

                    tablero = numpy.zeros((8,8))
                    pos = [0,1]
                    iteracion = 1
                    #print ("recorrido: ",recorrido)
                    tablero = marcar (tablero, pos, iteracion)
                    prueba_camino(tablero, pos, iteracion)  
            corregir(iteracion, retrocede, tablero, pos)
  

print (sys.getrecursionlimit())
prueba_camino(tablero, pos, iteracion)



