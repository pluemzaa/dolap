n = int(input('Enter number: '))
if n <= 0:
    print('Error number must be 1 or greater')
else:    
    for i in range(n):
        for j in range(n):
            v = (i+j+1) % 9
            if v == 0:
                v=9
            print(v,end=" ") 
        print()