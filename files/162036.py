num = int(input("Enter number:"))
if num <1:
    print("Error number must be 1 or greater")
else:
    for i in range(num):
        for n in range(i+1):
            print("**",end="")
        print()
        for n in range(i+1):
            print("**",end="")
        print()