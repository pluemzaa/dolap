s = int(input("Enter number:"))
if s < 1:
    print('Error number must be 1 or greater')
s
for i in range(s):
    for j in range(i+1):
        print('**',end='')
    print()
    
    for j in range(i+1):
        print('**',end='')
    print()