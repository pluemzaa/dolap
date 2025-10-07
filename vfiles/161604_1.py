n = int(input('Enter number:'))
i = 1
if n > 0:
    while i < n:
        j = 0
        while j < n:
            if i + j > 9:
                print(0, end=' ', sep=',')
            else:
                print(i + j, end=' ', sep=',')
            j = j + 1
        print()
        i = i + 1
    
else:
    print('Error number must be 1 or greater')