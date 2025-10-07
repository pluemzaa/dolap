n = int(input('Enter number:'))
i = 1
if n > 0:
    while i < n + 1:
        j = 0
        while j < n:
            if i + j > 9:
                print(((i + j) - 1) % 9 + 1, end=' ')
            else:
                print(i + j, end=' ')
            j = j + 1
        print()
        i = i + 1
else:
    print('Error number must be 1 or greater')