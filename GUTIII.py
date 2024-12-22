# -*- coding: utf-8 -*-
"""
Album figuritas, ahora con paquetes.

@author: orteg
"""
import random
import statistics

def comprar_paquete(figus_total, figus_paquete):
    paquete= []
    for i in range (0, figus_paquete,1):
        figus_paquete = random.randint(1, figus_total)
        paquete.append(figus_paquete)
    return paquete

def crear_album(figus_total):
    album = []
    for i in range (0, figus_total, 1):
        album.append(0)
    return album

def album_lleno(l):
    lleno = False
    for i in range (0, len(l),1):
        if l[i] == 1:
            lleno = True
        
def llenar_album(album,paquete):
    late = False
    for i in range (0, len(album), 1):
        for a in range (0, 2, 1):           #no
            if album[i] == paquete[a]:
                late = True       

# def cuantas_paquetes(figus_total, figus_paquete):
    
#     album = crear_album(figus_total)
#     paquetes = 0 
#     while hay_alguno(album, False):
#         comprar_paquete(4,2)
    

        
  
    