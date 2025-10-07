x = int(input("Enter number: "))
if x <= 0:
    print("Error number must be 1 or greater")
else:
    for i in range(1,x+1):
        for j in range(2):
            print("**"*i)