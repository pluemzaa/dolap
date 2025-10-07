row = int(input("Enter number:"))
if row < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(row):
        for j in range(row):
            value  = (i+j+1) % 9
            if value == 0:
                value = 9
            print(value, end=" ")
        print()