s = int(input("Enter number: "))
for i in range(s) :
    if s >= 1 :
        for j in range(i+1) :
            print("**",end = '')
        print()
        for k in range(i+1) :
            print("**",end = '')
        print()
else :
        print("Error number must be 1 or greater")