n = input("Enter number: ")
n = int(n)
if n ==0:
    print("Error number must be 1 or greater")
else:    
    for i in range(n):
        i = 0
        for j in range(i+1):
            print('**',end = '')
            print('')
        for j in range(i+1):
            print('**',end = '')
            print('')