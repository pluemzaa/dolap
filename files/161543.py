n = int(input('Enter number: '))
if n <=0     :
    print("Error number must be 1 or greater")
else:
    for j in range(1,n+1):
        x = '*' * (2*j)
        for j in range(2):
            print(x)