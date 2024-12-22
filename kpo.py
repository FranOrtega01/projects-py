import random
import matplotlib.pyplot as plt

def una_jugada(p):
    numero = random.random()
    gana_juan = False
    if numero <= p:
        gana_juan = True
    return gana_juan

def n_rep (p, rep):
    gana_juan=0
    for i in range (0, rep, 1):
        if una_jugada(p) == True:
            gana_juan += 1
    return gana_juan

def juan_ruina (j,m,p):
    juan_ruina = False
    c = m-j
    while j > 0 and c > 0:
        if una_jugada(p) == True:
            j += 1
            c -= 1
        else:
            j -= 1
            c += 1
    if j == 0:
        juan_ruina = True
    return juan_ruina

def estimacion_juan_gana(j, m, p, rep):
    juan_gana = 0
    for i in range (0 , rep, 1):
        if juan_ruina(j,m,p) == False:
            juan_gana += 1
    # print("Proporción:",juan_gana/rep)
    return juan_gana/rep


# =============================================================================
# Gráficos
# =============================================================================
       
Xjuan = []
Yjuan_gana = []
Yjuan_gana2 = []
Yjuan_gana3 = []

j = 0
m = 5

while 0 <= j <= m:
    x=estimacion_juan_gana(j,5,1/6,1000)
    Yjuan_gana.append(x)    
    Xjuan.append(j)
    j += 1

j = 0

while 0 <= j <= m:
    x =estimacion_juan_gana(j,5,0.5,1000)
    Yjuan_gana2.append(x)    
  
    j += 1

j = 0

while 0 <= j <= m:
    x=estimacion_juan_gana(j,5,0.8,1000)
    Yjuan_gana3.append(x)
    j += 1

plt.title("Proporción de veces que juan gana cambiando p")
plt.plot(Xjuan, Yjuan_gana, ".")
plt.plot(Xjuan, Yjuan_gana2, "*")
plt.plot(Xjuan, Yjuan_gana3, "+")
plt.show()


#9)

Xjuan_9 = []
Yjuan_gana_9 = []

j = 0
m = 50
while j <= m:
    x=estimacion_juan_gana(j,m,0.5,1000)
    Yjuan_gana_9.append(x)    
    Xjuan_9.append(j)
    j += 1

plt.title("asd")
plt.plot (Xjuan_9, Yjuan_gana_9, ".")    
plt.show()
    





