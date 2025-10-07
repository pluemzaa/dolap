n=int(input("Enter number: "))

if n>=1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            b=i+j-1
            while b>9:
                b=b-9
            print(b,end=" ")
        print()
else:
    print("Error number must be 1 or greater")