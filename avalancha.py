import numpy as np
import matplotlib.pyplot as plt


def crear_tablero(n):
    t = np.repeat(0,n*n).reshape(n,n)
    j=0, n-1
    for i in range (0, n, 1):
        t[i,j] = -1
        
    i=0, n-1
    for j in range (0, n, 1):
        t[i,j] = -1
        
    return t

def es_borde(t,c):
    borde = False
    if t[c] == -1:
          borde = True
    return borde

def tirar_copo(t,c):
    t[c] = t[c]+1
    return t   
         
def vecinos_de(t, c):
    vecinos = []
    
    if es_borde(t,(c[0]+1,c[1])) == False:
        vecinos.append((c[0]+1,c[1]))
    if es_borde(t,(c[0]-1,c[1])) == False:
        vecinos.append((c[0]-1,c[1]))
    if es_borde(t,(c[0],c[1]+1)) == False:
        vecinos.append((c[0],c[1]+1))
    if es_borde(t,(c[0],c[1]-1)) == False:
        vecinos.append((c[0],c[1]-1))
        
    return vecinos

def desbordar_posicion(t,c):
    arriba = (c[0]-1,c[1])
    abajo = (c[0]+1,c[1])
    derecha = (c[0],c[1]+1)
    izquierda = (c[0],c[1]-1)
    if t[c] >= 4:
        t[c] = t[c]-4
        if es_borde(t, arriba) == False:
            t[arriba] = t[arriba] + 1
        if es_borde(t, abajo) == False:
            t[abajo] = t[abajo] + 1
        if es_borde(t, derecha) == False:
            t[derecha] = t[derecha] + 1
        if es_borde(t, izquierda) == False:
            t[izquierda] = t[izquierda] + 1
    return t

def desbordar_valle(t):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[(i,j)] >= 4:
                desbordar_posicion(t, (i,j))
                print("desbordo",i,j)
    return t

def hay_que_desbordar(t):
    cantidad_filas = t.shape[0]
    cantidad_columnas = t.shape[1]
    desbordar = False
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if t[(i,j)] >= 4:
                desbordar = True
    #print(t)
    return desbordar
    
def estabilizar(t):
    
    while hay_que_desbordar(t):
        desbordar_valle(t)
        
    return t

def paso(tablero):
    
                     
             
        
    
t = crear_tablero(9)
t[7,7] = 2
t[3,4] = 6
prueba= estabilizar(t)
print(prueba)



















if beto come asado:
    Estado = feliz

else:  
    Estado = triste
    
return Estado
    
    
