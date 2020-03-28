def ordenarcuadricula(size, c):      
    for i in c:    
        for j in range(size):
            print(i, end = ", ")
        print()
       
            
        
        
c = [2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8]
size = 5
ordenarcuadricula(size, c)
