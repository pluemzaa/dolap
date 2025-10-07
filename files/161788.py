n = int(input("enter number: "))

if n <= 0: 
    print("Error number must be 1 or greater")
else:
    for i in range(1, n+1):
        for j in range(n):
            v = i+j
            while v > 9:
                v -= 9
            print(v, sep=" ", end=" ")
        print()