row = int(input("Enter number: "))
col = row
i = 0
j = 1
if row > 0:
    while i < row:
        j = 0
        while j < col:
            k = ((i+j)%9)+1
            if i + j > 8:
                print(k,end=" ")
            else:
                print((i+1) + (j) , end=" ")
            j += 1
        i += 1
        print()
else:
    print("Error number must be 1 or greater")