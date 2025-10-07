x = int(input('Enter number:'))

if x >= 1:
    for i in range(1, x+1):
        y = "*" * (2*i)
        for j in range(2):
            print(y)

else:
    print('Error number must be 1 or greater')