                                        """
                                      Scrabble!
                                        """

from string import ascii_lowercase
import random


def mano(n): 
    mano = []
    abc = list(ascii_lowercase)
    for i in range (n):
        random.shuffle(abc)
        a = abc.pop(0)
        mano.append(a)
        
    return mano

def se_forma(palabra, mano):
    
    a = list(palabra)
    guti = 0
    
    if len(a) > len(mano):
        return "Flaco no te dan las fichas"
        
    else:
        
        for i in range (len(a)):
            for j in range (len(mano)):
                if a[i] == mano[j]:
                    guti += 1
                    mano[j] = 0
    
    if len(mano) == guti:
        return True
    
    return False
                


a = se_forma("manos",["m", "a", "n", "o","s"] )
print(a)


    
