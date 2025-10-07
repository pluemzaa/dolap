x = int(input("Enter number: "))
if x<=0:
    print('Error number must be 1 or greater')
if x >= 1:   
    for i in range(x):
        for j in range(i+1):
            print('**',end='')
        print()
        for j in range(i+1):
            print('**',end='')
        print()