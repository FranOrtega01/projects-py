"""
tirar_hasta_seis(): devuelve una lista con los valores observados en el dado tirado hasta que se
obtiene un 6, incluyendo el 6 por último valor de la lista.
"""
import random

def tirar_dado():
    dado=random.randint(1,6)
    return dado


def tirar_hasta_6():
    i = 0
    lista = []
    lista.append(tirar_dado())
    return lista
    
a=tirar_hasta_6()    
    