row = col = int(input("Enter number: "))
if row and col <= 0:
    print ("Error number must be 1 or greater")
else:
    i = j = 1
    while i < row:
        j=0
        while j < col:
            if i+j > 9:
                print(0,end = ' ', sep=',')
            else:
                print(i+j,end = ' ',sep=',')
            j = j + 1
        print ('')
        i = i + 1