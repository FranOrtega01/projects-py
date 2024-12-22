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
    
    
lista = []
for n in range (1,1000000): #el explota pc
    
    a = len_collatz(n)
    lista.append(a)

a = buscar_argmax(lista)
print(a+1)


# a = [1,2,3,11,3,4]
# print(buscar_argmax(a)+1)
