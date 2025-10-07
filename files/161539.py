n = int(input("Enter number: "))
if n >= 1:
    for i in range(n):
        for j in range(i+1):
            print('**',end='')
        print()
        for j in range(i+1):
            print('**',end='')
        print()
else:
    print('Error number must be 1 or greater')