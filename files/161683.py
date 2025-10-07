n = int(input("Enter number: "))
if n > 0:
    for i in range(n):
        for k in range(2):
            for j in range(i+1):
                print("**", end="")
            print()
else:
    print("Error number must be 1 or greater")