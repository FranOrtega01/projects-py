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

def tablero_oculto(n,m,b):
    
    t = poner_numeros(campo_minado(n,m,b))
    
    return t
    
def mapa(t):
    
    n = t.shape[0]
    m = t.shape[1]
    
    mapa = np.repeat('•',n*m).reshape(n,m)
   
           
    
    return mapa

def seguir_jugando(mapa, toculto): 
    
    n = mapa.shape[0]
    m = mapa.shape[1]
    
    x = True
    oc = np.sum(toculto == -1)
    mc = np.sum(mapa=='•')
    if oc == mc:
        x = False
    return x

"""creo que cambie bastante la idea de seguir_jugando porque no entendi
muy bien la consigna."""

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
#%%%
def ampliar(c,m,o):
    
    if o[c] == 0:
        m[c] = 0                        #este solito funciona, pero como dice 
        for i in vecinos(o,c):          #el codigo solo amplia una vez para sus
            if o[i] == 0:               #vecinos.
                m[i] = 0
    return m

# def ampliar(c,m,o):
    
#     if m[c] == 0:
#         for i in vecinos(o,c):        Porque no funciona y el de arriba si??
#             if o[i] == 0:             si primero aparece el 0 en el mapa y
#                 m[i] = 0              despues amplia.
#     return m

def ampliarmapa(m,o):
    n = m.shape[0]                      #para cada coord que lee, si es cero
    q = m.shape[1]                      #que amplíe, es decir ponga 0 a sus 
    for i in range(0, n):               #vecinos.
        for j in range(0, q):
            if m[(i,j)] == 0:
                ampliar((i,j),m,o)
    return m

def hay_que_ampliar(m,oculto):          #La idea es que recorra el mapa, vea si                    
    q = m.shape[0]                      #hay un 0, en el caso que lo haya se 
    p = m.shape[1]                      #fije si sus vecinos también son 0
                                        #y estan "ocultos". de ser asi da True
    for i in range(0,q):                
        for j in range(0,p):
            if m[i,j] == 0:
                for a in vecinos(oculto, (i,j)): 
                    if oculto[a] == 0 and m[a]== "•":
                        return True
    return False

def ampliartotal(m,o):                  #Loopea ampliarmapa hasta que no haya
    while hay_que_ampliar(m, o):        #mas vecinos por ampliar. 
        ampliarmapa(m,o)                #Pero ampliarmapa no funciona jaja :(
        
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
                print("Ya lo pusiste maestro")
            seguimos = tocar(coord, m, oculto)
            amplia = ampliar(coord,m,oculto)
            #ampliar = ampliartotal(m,oculto)
            
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
        print("ECOLE ganaste pibe")
        print("Vamos Boca mamita querida")
    return exploto
 
# b = tablero_oculto(2,2,1)
# a=mapa(b)
# print(a)
# print(a) 
# a= np.array([['•','•','•'],['•','•',0],['•','•','•']])
# print(a) 
# b = np.array([[-1,1,0],[1,1,0],[0,0,0]])
# c= ampliarmapa(a,b)
# # c = ampliarmapa(a,b)
# print(b)   
# print(c)
    
jugar_una_partida(5, 5, 51)
    