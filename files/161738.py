x = int(input('Enter number: '))
a = 1
if x > 0:
    for i in range(x):
        for j in range(2):
            print("**"*a)
        a = a + 1
else :
    print("Error number must be 1 or greater")