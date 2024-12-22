"""
Proyecto Euler
"""
import random

def par(n):
    
    Par = False
    if n % 2 == 0:
        Par = True
        
    return Par
        
def collatz(n):  #si es par: n/2, si es impar: 3n+1

    lista_collatz = []
    
    while n != 1:
        #print(n)
        if par(n) == True:
            n = n/2
            lista_collatz.append(n)
        else:
            n = 3*n+1
            lista_collatz.append(n)
           
    return lista_collatz
    
def len_collatz(n):
    
    a = len(collatz(n))
    
    return a

def maximo(l):
    
    a = max(l)
    return a

def buscar_argmax(l):
    
    for i in range (0, len(l)):
        print(i)
        if maximo(l) == l[i]:
            return i
    
    
# lista = []
# for n in range (1,1000000): #el explota pc
    
#     a = len_collatz(n)
#     lista.append(a)

# a = buscar_argmax(lista)
# print(a+1)  # a+1 ya que la lista comienza en 0.


# a = [1,2,3,11,3,4]
# print(buscar_argmax(a)+1)

# =============================================================================
#                            Mayor factor primo
# =============================================================================

def multiplo(n,k):
    
    if n % k == 0:
        return True
    else:
        return False

def factores(n):
    
    factores = []
    
    for i in range (1,n):
        if multiplo(n,i): # o n%i== 0...
            factores.append(i)
    # print(factores)
    return factores

            
def primo(n):
    if len(factores(n)) == 1: #Igual a 1 ya que en factores(n) no se cuenta el 
        return True           # número(n) por la consigna
    return False

def factorizar(n,p):
    
    while n % p == 0:
        n = n / p
        # print(p)    
    return n

def factores_primos(n):
    lista = []
    a = factores(n)
    for i in range (0,n):
        if primo(i) and multiplo(n,i):
            lista.append(i)
            
        
    return lista

def maximo(l):
    
    a = max(l)
    
    return a
    
            
# a = 600851475143 ... no me da la pc pero creanme que da el mayor factor primo jaja, 
# por ejemplo el de 190 es 19 y el de 423 es 47
# b = maximo(factores_primos(a))   
# print(b) 
# aa = 423
# bb = maximo(factores_primos(aa)) 
# print(bb) 
            
   
            
    

































