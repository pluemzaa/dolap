N = int(input("Enter a number N:"))
i = 2
if N == 2 :
    print(2)
    quit()
if N >= 3 :
    print('2\n3')
    
while i<N :
    j = 2
    while j < i/2 and i % j != 0 :
        j += 1 
        if j >= i/2 :
            print(i)
    i+=1