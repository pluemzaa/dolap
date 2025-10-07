n = int(input("Enter number: "))
row = n

if n < 1: 
    print("Error number must be 1 or greater")
    
else:
    
    for i in range(1,row+1,1):
        for j in range(n):
            number = (i + j - 1 ) % 9 + 1
            print(number , end=" ")
        print("")