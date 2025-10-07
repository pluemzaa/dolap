num = int(input("Enter number: "))
if num > 0:
    for i in range (num):
        for k in range (i,i + num):
            f = k
            if k > 8:
                jo = f % 8
                print(jo,end=' ')
            else:
                print(k + 1,end=' ')
        print()
else:
    print("Error number must be 1 or greater")