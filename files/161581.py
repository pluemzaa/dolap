row = col = int(input("Enter number: "))
if row <= 0:
    print("Error number must be 1 or greater")
else:
    i = 0
    while i < row:
        j = 0
        while j < col:
            num = (i + j) % 9 + 1
            print(num, end=' ')
            j += 1
        print('')
        i += 1