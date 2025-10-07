n = int(input("Enter number: "))
'''
*
**
***
****
*****
'''
if(n >= 1):
    for i in range(1,n+1):
        print('**'*i)
        print('**'*i)
else:
    print("Error number must be 1 or greater")