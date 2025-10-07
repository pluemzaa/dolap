n = int(input("Enter number: "))
if n > 0  :
    for i in range(n) :
        i += 1
        for i in range(i):
            print("**",end= '')  
        print('')
    
        i += 1
        for i in range(i):
            print("**",end= '') 
        print('') 
else :
    print("Error number must be 1 or greater")