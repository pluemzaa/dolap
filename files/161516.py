n = input("Enter number: ")
n = int(n)
if n >0:  
    for i in range(n):
        i+=1
        for j in range(i):
            print('**',end = '')
        print('')
            
        for j in range(i):
            print('**',end = '')
        print('')
else:
     print("Error number must be 1 or greater")