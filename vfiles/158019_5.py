n = int(input("Enter number N:"))
for i in range (2,n+1):
    if i%2 != 0:
        print("Prime number from 1 to {} are:".format(n),i)