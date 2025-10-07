n = int(input("Enter number: "))

if n > 0:
    for i in range(n):
        i += 1
        
        for j in range(i):
            print("**",end = "")
        print("")
        
        for j in range(i):
            print("**",end = "")
        print("")
else:
    print("Error number must be 1 or greater")