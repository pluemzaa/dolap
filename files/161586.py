num = int(input('Enter number:'))

i = j = 1
k = 0

if num > 0 :
    while i < num+1 :
        j = 0 
        while j < num :
               
            if i + j > 9 :
                k = (i + j -1)%9 +1 
                print(k,end=' ',sep='')

            else  :
                print(i+j,end=' ',sep='')
            j += 1 
        
          
        print()
        i += 1 
    
else : 
    print("Error number must be 1 or greater")