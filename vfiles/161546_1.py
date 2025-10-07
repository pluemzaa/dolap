n = int(input("Enter number: "))
if n>0:
    for i in range(n):
        for j in range(i*n+1):
            print("**")
            print("**")
else:
    print("Error: number must be 1 or greater")