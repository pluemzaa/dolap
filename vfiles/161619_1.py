n = int(input('Enter number: '))
if n < 1:
    print('Error number must be 1 or greater')
else:
    row = n
    col = n
    i = j = 0
    while i < row:
        j = 0
        while j < col:
            if i+j > 9:
                print((i+j)-n,end=' ')
            else:
                print(i+j, end=' ', sep = ' ')
            j += 1
        print(' ')
        i += 1