y = int(input("Enter number:"))
if y < 1:
    print("Error number must be 1 or greater")
for i in range(y):
    for j in range(i+1):
        print('**',end=' ')
    print ( )
    for y in range(i+1):
        print('**',end=' ')
    print ( )