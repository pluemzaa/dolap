row = int(input('Enter number: '))
if row > 0:
    for i in range(row):
        for j in range(row):
            print((i+j) % 9 + 1, end=' ')
        print()
else:
    print('Error number must be 1 or greater')