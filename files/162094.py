w=int(input('Enter number: '))
if w<1:
    print('Error number must be 1 or greater')
else:
    for i in range(w):
        for j in range(w):
            num=(i+j+1)
            if w>9:
                num=(num-1)%9+1
            print(num,end='')
        print()