n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            value = (i + j + 1) 
            if value > 9:
                value = (value - 1) % 9 + 1 
            print(value, end=" ")
        print()