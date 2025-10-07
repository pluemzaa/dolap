row = int(input('Enter number: '))
col = row
i = 0
if row < 1:
    print('Error number must be 1 or greater')
else:
    while i < row:
        m = 0
        while m < col:
            num = i + m + 1
            while num > 9:   
                num = num - 9
            print(num, end=' ')
            m += 1
        print()
        i += 1