# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:27:58 2022

@author: orteg
"""

import random
import statistics

def crear_album(figus_total):
    album = []
    for i in range (0, figus_total, 1):
        album.append(0)
    return album

def comprar_figus(figus_total):
    figu = random.randint(1, figus_total)
    return figu

def hay_alguno(album, figu):
    late = 0
    for i in range (0, len(album),1):
        if album[i] == figu:
            late = 1
    return late

def cuantas_figus(figus_total):
    l = crear_album (figus_total)
    paquetes = 0
    while hay_alguno(l,0):
        e = comprar_figus(figus_total)
        l[e-1] = 1
        paquetes += 1
        print(l)
    print(l)
    return paquetes

def experimentar(figus_total, n_rep):
    Lista_paquetes = []
    i = 0
    while i < n_rep:
        Lista_paquetes.append(cuantas_figus(figus_total))
        i += 1 
    print("en promedio son", statistics.mean(Lista_paquetes), "paquetes por album")
    return statistics.mean(Lista_paquetes)
                                                 