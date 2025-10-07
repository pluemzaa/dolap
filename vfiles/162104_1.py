a = int(input("Enter Number:"))
row = a+1
col = a
c = 1
i = j = 1
while i < row:
    j = 0

    while j < col:
        if i+j > 9:
            print(j, end=' ')
        else:
            print(f"{i+j}", end=' ')
        j = j + 1 
    print()    
    i = i + 1


if a<1:
    print("Error number must be 1 or greater")