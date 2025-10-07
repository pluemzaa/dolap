n = input("Enter number: ")
n = int(n)
if n > 0:
    for i in range(n):
        i += 1
        for j in range(i+1):
            if j < 2:    
                print('*'*i*2,end='')
                print()
else:
    print("Error number must be 1 or greater")