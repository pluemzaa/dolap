n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for row in range(1, n + 1):
        for col in range(n):
            value = (row + col - 1) % 9 + 1
            print(value, end=" ")
        print()