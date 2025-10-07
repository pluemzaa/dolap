num = int(input("Enter number: "))
if num > 0:
    for i in range(num):
        for i in range(i+1):
            print("**",end='')
        print()
else:
    print("Error number must be 1 or greater")