n = int(input('Enter number:'))
row = n
col = n
i = 0
if n > 0:
    while i < row:
        j = 0
        while j < col:
            if i + j > 9:
                print(0, end=' ', sep=',')
            else:
                print(i + j, end=' ', sep=',')
            j = j + 1
        print()
        i = i + 1
    
else:
    print('Error number must be 1 or greater')