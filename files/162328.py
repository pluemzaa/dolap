n = int(input('Enter number:'))
i = 0
j = 0
if n > 0:
    while i in range(n):
        j=0
        while j in range(n):
            x = (i+j+1)
            if x > 9:
                if (x % 9) == 0:
                    x = 9
                    print(x,end=' ')
                else:
                    print(x%9,end=' ')
            else:
                print(x,end=' ')
            j+=1
        print()
        i+=1
else:
    print("Error number must be 1 or greater")