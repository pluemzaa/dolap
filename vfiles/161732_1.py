row = int(input('Enter number: '))
col = row
i = j = 0
if row<=0 :
    print('Error number must be 1 or greater')
else:
    while i < row:
        i+=1
        j = 0
        while j < col:
            if i+j>9:
                 print((i+j-1) % 9 + 1, end = ' ',sep = ',')
            else:
                 print(i+j, end = ' ',sep = ',')
            j=j+1
        print()