#*
#**
#***
#****
#*****
n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")

else:
    for i in range(n):
        
        for i in range(i+1):
            print("**",end='')
        print("")
        for i in range(i+1):
            print("**",end='')
        print("")