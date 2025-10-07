n = int(input('Enter number:'))
if n<=0:
    print('Error number must be 1 or greater')
else:
    for i in range(n):
        for j in range(2):
            for j in range(i+1):
                print('**',end='')
            print()