n = int(input('Enter number: '))

if n < 1:
    print('Error number must be 1 or greater')
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            value = (i + j - 1) % 9
            if value == 0:
                print(9, end=' ')
            else:
                print(value, end=' ')
        print()