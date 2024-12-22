"""
Halcones y Palomas
"""
import random


def generar_poblacion(p):
    poblacion = []
    for i in range (0,p):
        poblacion.append("p")
    return poblacion

def distribuir(p,f):
    distribucion = list(range(0,f))
    random.shuffle(distribucion)
    return distribucion