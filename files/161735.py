n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
else :
    for j in range(1, n+1):
        for i in range(n):
            print((j + i - 1) % 9 + 1, end="")
        print()