row = int(input("Enter number: "))
i = j = 0
if row >=1:
    while i < row:
        j = 0
        while j < row:
            value = (i + j) % 9 + 1
            print(value, end=" ")
            j = j + 1
        print("")
        i += 1
else:
    print("Error number must be 1 or greater")