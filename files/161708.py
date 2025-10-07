n = int(input("Enter number: "))
y = "**"
if n > 0:
    for i in range(n):
        for j in range (i+1):
            print(y,end='')
        print()
        for j in range (i+1):
            print(y,end='')
        print()
else:
    print("Error number must be 1 or greater")