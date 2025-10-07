j = int(input("Enter number: "))
k = 0
if j > 0:
    for i in range (j):
        for k in range (i + 1):
            print("**",end="")
        print()
        for k in range (i + 1):
            print("**",end="")
        print()
        
else:
    print("Error number must be 1 or greater")