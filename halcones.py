"""
Nano Jack
"""
import random


def generar_mazos():
    
    mazo = 4*list(range(14))
    random.shuffle(mazo)
    print(mazo)
    return mazo

def jugar(m):
    i = 0
    j = 0
    while j < 21:
        pop = m.pop(i)
        j += pop
        i += 1
    return j

a = jugar(generar_mazos())
print(a)