vec = int(input("Enter number: "))


for i in range(1,vec+1):
    print(i,end = " ")
    j = 0    
    for j in range (1,vec):
        print(j+i,end = " ")
    print("")