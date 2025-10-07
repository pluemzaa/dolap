x = int(input("Enter number: "))
if x<=0:
    print('Error number must be 1 or greater')
   
for i in range(x):
    for j in range(i+1):
        print('**',end='')
        
    print()
for i in range(x):
    for j in range(i+1):
        print('**',end='')
        
    print()