row = int(input("Enter number:"))#แถว
if row < 1:
    print("Error number must be 1 or greater")
else :
    for i in range(row):
        for j in range(row):
            num = (i+j)%9+1
            print(num, end='',sep=',')
        print()