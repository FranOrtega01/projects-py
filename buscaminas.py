                                 """
                              Buscaminas
                                 """
                                 
import random
import numpy as np
import matplotlib.pyplot as plt
 
                                 
def campo_minado(n, m, bombas):
    
    t = np.repeat(0,n*m).reshape(n,m)
    for i in range (0,bombas):
        (a,b) = (random.randint(0,n-1),random.randint(0,m-1))
        if t[a,b] == -1:
            while t[a,b] == -1:          
                (a,b) = (random.randint(0,n-1),random.randint(0,m-1))
                
        t[a,b]= -1
        
             
    return t

"""Para que las cantidad de bombas no sea menor al parametro "bombas", hice un 
while que reubique aleatoriamente la bomba si ya había una en ese lugar"""

def en_rango(t,c):
    
    if 0 <= c[0] <= t.shape[0]-1 and 0 <= c[1] <= t.shape[1]-1: # "área" de la matriz
        return True
    else:
        return False
#%%    
def vecinos(t,c):
    
    vecinos = []
    if en_rango(t,c): #Si c esta fuera de rango, no hace la lista.

        #Laterales
        if en_rango(t,(c[0]+1,c[1])) == True:
            vecinos.append((c[0]+1,c[1]))
        if en_rango(t,(c[0]-1,c[1])) == True:
            vecinos.append((c[0]-1,c[1]))
        if en_rango(t,(c[0],c[1]+1)) == True:
            vecinos.append((c[0],c[1]+1))
        if en_rango(t,(c[0],c[1]-1)) == True:
            vecinos.append((c[0],c[1]-1))
        #Diagonales 
        if en_rango(t,(c[0]+1,c[1]+1)) == True:
            vecinos.append((c[0]+1,c[1]+1))
        if en_rango(t,(c[0]+1,c[1]-1)) == True:
            vecinos.append((c[0]+1,c[1]-1))
        if en_rango(t,(c[0]-1,c[1]-1)) == True:
            vecinos.append((c[0]-1,c[1]-1))
        if en_rango(t,(c[0]-1,c[1]+1)) == True:
            vecinos.append((c[0]-1,c[1]+1))
            
        #print(t)
        return vecinos
    else:
        return "La coordenada está fuera de rango"
#%%    
def poner_numeros(t):
    
    n = t.shape[0]
    m = t.shape[1]
    count = 0
        
    for i in range(0, n):
        for j in range(0, m):
            if t[i,j] != -1:
                for x in vecinos(t,(i,j)): 
                    if t[x] == -1:
                        count += 1
                t[i,j] = count    
                count = 0
                
    return t
#%%
def tablero_oculto(n,m,b):
    
    t = poner_numeros(campo_minado(n,m,b))
    
    return t
    
def mapa(t):
    
    n = t.shape[0]
    m = t.shape[1]
    
    mapa = np.repeat('•',n*m).reshape(n,m)
   
           
    
    return mapa
#%%
def seguir_jugando(mapa, toculto):
    
    n = mapa.shape[0]
    m = mapa.shape[1]
    ocultocount = 0
    
    x = False
    if not x:
        for i in range(0, n):
            for j in range(0, m):
                if toculto[i,j] == -1:
                    ocultocount =+ 1
        mc = np.sum(mapa=='•')
    print(mc)
    print(ocultocount)
    if ocultocount == mc:
        x = True
    print(x)
    return x
#%%
def tocar(c,m,t):
    
    if t[c] == -1:
        m[c] = "x"
        return False
    else:
        m[c] = t[c]
        return True

def pedir_c():
    
    f = int(input("Ingrese un valor: "))
    e = int(input("Ingrese un valor: "))
    
    return f,e
#%%
def ampliar(c,m,o):
    
    if o[c] == 0:
        m[c] = 0
        for i in vecinos(o,c):
            if o[i] == 0:
                m[i] = 0
    return m
    
#%%
def jugar_una_partida(filas, columnas, bombas):
    

    oculto = tablero_oculto(filas, columnas, bombas)
    m = mapa(oculto)
    o = m.shape[0]
    n = m.shape[1]
    exploto = False
    
    
    while not exploto and seguir_jugando(m, oculto):
        print(m)
        coord = pedir_c()
        if en_rango(m, coord):
            if m[coord] != '•':
                print("Ya lo pusiste master")
            seguimos = tocar(coord, m, oculto)
            m = ampliar(coord,m,oculto)
            
            if not seguimos:
                print("buuuuuum!")
                exploto = True
        else:
            print("Coordenada fuera de rango.")
            print(m)
    if exploto:
        for i in range(0, o):
            for j in range(0, n):
                if oculto[i,j] == -1:
                    m[i,j] = "x"
        print("El que no hace palma es hincha de Velez")
        print(m)
        
    else:
        print("Vamos Boca mamita querida")
    print(seguir_jugando(m, oculto))
    return exploto
#%%  
    

    

# b = tablero_oculto(2,2,1)
# a=mapa(b)
# print(a)
# print(a) 
# a= np.array([[1,1,"•"],[1,6,1],[1,1,1]])
# b = np.array([[1,1,1],[1,-1,1],[1,1,1]])
# print(mapa)
# a = seguir_jugando(mapa, toculto)
# print(a)
# h = seguir_jugando(a,b)
# print(a) 
# print(b)   
# print(h)
    
jugar_una_partida(3, 3, 1)
    