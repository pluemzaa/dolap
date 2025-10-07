x = int(input("Enter number: "))
if x <= 0 :
    print("Error number must be 1 or greater")
else :
    for i in range(x):
        for j in range(x):
            if (j+i)+1 >= 10:
                j = 0
                print(f"{j} ",end='')
            else:
                print(f"{(j+i)+1} ",end='')
        print()