n = int(input("Enter number: "))

if n >= 1:
    for i in range(n):
        for j in range(n):
            if j + i  < 9:
                print(j+i+1,end=" ")
            elif j + i < 18:
                print(j+i-8,end=" ")
            else:
                print(j+i-17,end=" ")
        print()
else:
    print("Error number must be 1 or greater")