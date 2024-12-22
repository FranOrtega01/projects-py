                                       """
                                    Mastermind                                                                
                                       """
import random

                                       
def listarandom(n):
    lista = []
    for i in range (0,n):
        lista.append(random.randint(1,9))
    return lista
        
                                     
def contar_con_ubicacion_sinrep(a, b):
    contar = 0
    for i in range (0,len(a)):
        for j in range (0,len(b)):
            if a[i] == b[j] and i == j:
                contar += 1
    return contar

def contar_mal_ubicadas_sinrep(a, b):
    contar = 0
    for i in range (0,len(a)):
        for j in range (0,len(b)):
            if a[i] == b[j] and i != j:
                contar += 1
    return contar
    
def contar_coincidencias_sinrep(a,b):
    
    cuentas = [contar_con_ubicacion_sinrep(a, b),contar_mal_ubicadas_sinrep(a, b)]
    return cuentas


def elevar_al_cuadrado():
    b=input("si me dice un numero, le dire su cuadrado: ")
    c=(b)**2
    print(c)


def pedir_numero():
    
    l = []
    b = input("Dame un número jefe:")
    c = list(b)
    for i in list(b):
        d = int(i)
        l.append(d)
       
    #print(l)
    return l

def jugar_sinrep(b):
    
    intentos=0
    gano=False
    
    while not gano:
        intentos += 1
        a = pedir_numero()
        print(a)
        print(contar_coincidencias_sinrep(a,b))
        if b == a:
            gano = True
            print("Boca!! Ganaste pibe")
    return gano

def contar_coin(a,b):
    aa = a.copy()
    bb = b.copy()
    contar_bien = 0
    contar_mal = 0
    #print(aa)
    for i in range(len(a)):
        for j in range(len(a)):
            if aa[i] == bb[j] and i == j:
                contar_bien += 1
                aa[i] = -aa[i]
    #print(bb)
    for i in range(len(a)):
          for j in range(len(a)):
              if aa[i] == bb[j] and i != j:
                  contar_mal += 1
                  for e in range(len(bb)):
                      if bb[e] == aa[i]:
                        bb[e] =0 
                        #usar bb[e] = -bb[e] como en el caso de arriba me 
                        #generaba problemas, asi que lo cambie por 0
                 
                                 
                  
    # print(bb)
               
    contar = [contar_bien, contar_mal]
    
    return contar
                
                
def jugar(n):  #decidi poner el n por si se queria jugar con una lista de n numeros
    intentos=0
    gano=False
    a = listarandom(n)
    # print(a)
    while not gano:
        intentos += 1
        b = pedir_numero()
        print(b)
        c = contar_coin(a,b)
        print(c)
        print(intentos)
        if b == a:
            gano = True
        
        if intentos == 10:
            print("mira que a los 15 hay prenda pibe")
    print("Boca!! Ganaste pibe")
    if intentos == 1:
        return print("Ganaste en", intentos, "intento") #una gilada esta linea pero me daba toc
    return print("Ganaste en", intentos, "intentos") 
                   
    
pedir_numero()

    













