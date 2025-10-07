row = int(input("Enter number:"))
if row > 0:
    for i in range(1, row + 1):
        k = '*' * (2 * i)  
        print(k)  
        print(k) 
    print()
else:
    print("Error number must be 1 or greater")