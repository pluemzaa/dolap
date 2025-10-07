n = int(input("Enter number: "))
b = 2
if n > 0:
    for i in range(n):
        for x in range(b):
            for j in range(i+1):
                print("**", end="")
            print()
else:
    print("Error number must be 1 or greater")