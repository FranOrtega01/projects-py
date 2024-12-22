                                        """
                                      Scrabble!
                                        """

from string import ascii_lowercase
import random
import matplotlib.pyplot as plt

abc_scrabble = open ("scrabble.txt").read() #me arme un txt de las fichas del scrabble
diccionario = open("diccionario.txt").read().splitlines()



def mano(): 
    mano = []
    abecedario = abc_scrabble
    abc = list(abecedario)
    for i in range (7):
        random.shuffle(abc)
        a = abc.pop(0)
        mano.append(a)
    # print(mano)
    return mano

def se_forma(palabra, mano):
    
    a = list(palabra)
    count = 0
    mano2 = mano.copy()
    aa = a.copy()
    
    if len(a) > len(mano):
        return "Master no te dan las fichas"
        
    else:
        
        for i in range (len(a)):
            for j in range (len(mano)):
                if aa[i] == mano2[j]:
                    count += 1
                    mano2[j] = "."
                    aa[i] = ","
                
    if len(palabra) == count:
        return True
    else:
        return False


    
                
def mas_larga(diccionario,mano):
    
    lista_palabra = []
    b =[]
    
    for i in range(0, len(diccionario)):
        if se_forma(diccionario[i],mano)==True:
            a = len(list(diccionario[i])) #asi no me aparecen letras como si fueran palabras
            if a > 1:
                
                lista_palabra.append(diccionario[i])
            
    if lista_palabra == []:
        return ""
    
    a = max(lista_palabra)
  
    return a


def calcular(lista):
    listaplt = []
    count = 0
    for i in range(8):
        for a in lista:
            if i == len(a):
                count += 1
        listaplt.append(count)
        count = 0
    return listaplt

def exp(dic, rep):
    
    lista = []
    
    for k in range (rep):
        manoRep = mano()
        
        palabra_larga = mas_larga(dic,manoRep)
        # print(palabra_larga)
        lista.append(palabra_larga)
        
    a = calcular(lista)
            
    return a
       
freqs = exp(diccionario,200)
plt.bar([0,1,2,3,4,5,6,7], freqs)
plt.show()




























