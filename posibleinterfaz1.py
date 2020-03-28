from pprint import pprint

def ordenarcuadricula(size, c):      
    x = 0
    y = size
    e = []
    for i in range(size):    
        e.append((c[x:y]))
        x += size
        y += size
        
    return e
            
        
        
c = [2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8]
size = 5
a = ordenarcuadricula(size, c)
pprint(a)