n = int(input('Enter number:'))
if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            k = (i+j+1)%9
            if k == 0:
                k = 9
            print(k,end=' ')
        print()