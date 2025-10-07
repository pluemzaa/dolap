n = int(input("Enter number: "))

i = 0

if n > 0:
    while i < n:
        j = 0
        
        while j < n:
            j += 1
            
            sum = j + i
            
            if sum > 9:
                sum = (j + i - 1) % 9 + 1
                
            
            print(sum,sep="",end=" ")
        
        i += 1
        
        print("")
else:
    print("Error number must be 1 or greater")