def ordenarcuadricula(size, c): 
    a = 0
    for i in range(size):
        for j in range(size):
            print(c[a], end = ", ")
            a += 1
        print()
       
