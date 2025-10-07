num = int(input('Enter number: '))
i = 1
if num < 1:
    print('Error number must be 1 or greater')
else:
    while i < num+1:
        j = 0
        while j < num:
            if i+j >= 9:
                print((i+j-1)%9+1,sep =',' ,end=' ')
            else:
                print(i+j,sep =',',end=' ')
            j = j+1
        i = i+1
        print()