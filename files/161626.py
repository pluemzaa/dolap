row = int(input("Enter number: "))
col = row

if row > 0:
    i = 0
    while i < row:
        j = 0
        while j < col:
            value = i + j + 1
            if value > 9:
                value = (value - 1) % 9 + 1
            print(value, end=' ')
            j += 1
        print()
        i += 1
else:
    print("Error number must be 1 or greater")