num = int(input("Enter number: "))
if num > 0:
    for i in range (num):
        for k in range (i,i + num):
                print(((k % 9)+ 1),end=' ')
        print()
else:
    print("Error number must be 1 or greater")