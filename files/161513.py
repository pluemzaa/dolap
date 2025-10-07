n = int(input("Enter number:"))
if n > 0:
    for i in range(1,n+1):
        for j in range(2):
            print('**' * (i)) 
else:
    print("Error number must be 1 or greater")