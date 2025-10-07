vec = int(input("Enter number: "))

if vec >0:
    for i in range(1,vec+1):
        print(i,end = " ")
        j = 0    
        for j in range (1,vec):
            print(j+i,end = " ")
        print("")
elif vec <= 0:
    print("Error number must be 1 or greater")