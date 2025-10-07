n1 = int(input("Enter number:"))

if n1 > 0:
    for i in range(1,n1+1):#row
        print(i*"**")
        print(i*"**")
else:
    print("Error number must be 1 or greater")