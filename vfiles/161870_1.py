x = int(input("Enter number: "))
if x < 1:
    print("Error number must be 1 or greater")
row = x
col = x
i = j = 1
while i < row+1:
    j = 0
    while j < col:
        if i+j > 100:
            print(0,end='')
        else:    
            print(i+j,end='')
        j = j + 1
    i = i + 1
    print()