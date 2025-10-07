row = int(input("Enter number:"))
col = row


i = j = 0
if row < 1:
    print("Error number must be 1 or greater")
while i < row:
    j = 1
    while j < col:
        if i + j > 9:
            
            print(0, end=' ')
        else:
            print(i+j, sep=',', end=' ')
        
        j = j+1
    i = i+1
    print()