num = int(input("Enter number: "))
if num < 1:
    print("Error number must be 1 or greater")
else:
    for row in range(1, num+1):
        for col in range(1, num+1):
            value = (row + col - 1) % 9
            if value == 0:
                value = 9
            print(value, end=" ")
        print()